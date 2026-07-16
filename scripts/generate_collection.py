#!/usr/bin/env python3
"""Generate zeqk.databasus Ansible collection from an OpenAPI/Swagger spec.

Usage:
  python3 scripts/generate_collection.py \
      --spec openapi.json \
      --output zeqk/databasus
"""

from __future__ import annotations

import argparse
import json
import re
import textwrap
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - fallback for Python < 3.11
    import tomli as tomllib

from jinja2 import Environment, FileSystemLoader

HTTP_METHODS = {"get", "post", "put", "patch", "delete"}
PUBLIC_ACTION_MODULES = {
    ("post", "/users/signin"): "user_signin",
}


def is_param(token: str) -> bool:
    return token.startswith("{") and token.endswith("}")


def snake(name: str) -> str:
    name = name.strip("{}")
    name = re.sub(r"[^0-9a-zA-Z]+", "_", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = name.lower().strip("_")
    if not name:
        return "field"
    if name[0].isdigit():
        name = f"field_{name}"
    return name


def singular(word: str) -> str:
    if word.endswith("ies") and len(word) > 3:
        return word[:-3] + "y"
    if word.endswith(("sses", "xes", "zes", "ches", "shes")):
        return word[:-2]
    if word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def sanitize_text(value: str) -> str:
    value = (value or "").replace("\n", " ").replace("\r", " ")
    value = re.sub(r"\s+", " ", value).strip()
    return value


def resource_from_path(path: str) -> str:
    parts = [p for p in path.split("/") if p]
    non_param = [p for p in parts if not is_param(p)]
    if not non_param:
        return "resource"

    for i in range(len(parts) - 2):
        if not is_param(parts[i]) and is_param(parts[i + 1]) and not is_param(parts[i + 2]):
            return f"{singular(snake(parts[i]))}_{singular(snake(parts[i + 2]))}"

    return singular(snake(non_param[0]))


def classify(method: str, path: str) -> Optional[str]:
    parts = [p for p in path.split("/") if p]
    if not parts:
        return None
    end_param = is_param(parts[-1])
    if method == "post" and not end_param:
        return "create"
    if method == "get" and not end_param:
        return "list"
    if method == "get" and end_param:
        return "get"
    if method in {"put", "patch"} and end_param:
        return "update"
    if method == "delete" and end_param:
        return "delete"
    return None


def json_type_to_ansible(t: str) -> str:
    return {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "array": "list",
        "object": "dict",
    }.get(t or "string", "raw")


def resolve_schema(schema: Any, definitions: Dict[str, Any], depth: int = 0) -> Dict[str, Any]:
    if not isinstance(schema, dict) or depth > 6:
        return {}
    if "$ref" in schema:
        ref = schema["$ref"]
        prefix = "#/definitions/"
        if ref.startswith(prefix):
            return resolve_schema(definitions.get(ref[len(prefix) :], {}), definitions, depth + 1)
        return {}

    if "allOf" in schema:
        merged_props: Dict[str, Any] = {}
        merged_required: List[str] = []
        enum_part: Optional[Dict[str, Any]] = None
        for sub in schema["allOf"]:
            part = resolve_schema(sub, definitions, depth + 1)
            if "enum" in part and not part.get("properties"):
                enum_part = part  # scalar/enum sub-schema (e.g. allOf:[{$ref: SomeStringEnum}])
            merged_props.update(part.get("properties", {}))
            merged_required.extend(part.get("required", []))
        if enum_part is not None and not merged_props:
            # allOf resolves to a scalar enum; return it directly
            return enum_part
        return {"type": "object", "properties": merged_props, "required": sorted(set(merged_required))}

    return schema


def _needs_yaml_quoting(value: str) -> bool:
    """Return True when the string value needs YAML quoting to remain a string type."""
    if not value:
        return True
    if value.lower() in ("true", "false", "null", "yes", "no", "on", "off"):
        return True
    try:
        float(value)
        return True
    except ValueError:
        return False


_SECRET_SUBSTRINGS = ("token", "secret", "password", "apikey", "api_key", "key")


def _get_enum_choices(raw_pdef: Dict[str, Any], definitions: Dict[str, Any]) -> Optional[List[str]]:
    """Return enum values as strings if the schema describes an enum type, else None."""
    if not isinstance(raw_pdef, dict):
        return None
    # 1. Inline enum on the raw property (e.g. TriggerBackupRequest.type has both enum and allOf)
    if "enum" in raw_pdef:
        return [str(v) for v in raw_pdef["enum"]]
    # 2. After full resolution ($ref → enum, allOf → scalar enum)
    resolved = resolve_schema(raw_pdef, definitions)
    if "enum" in resolved:
        return [str(v) for v in resolved["enum"]]
    return None


def _build_field_meta(
    api_name: str,
    raw_pdef: Dict[str, Any],
    definitions: Dict[str, Any],
    required: bool,
    source: str,
    depth: int = 0,
) -> Dict[str, Any]:
    """Build complete field metadata for one OpenAPI property, including nested suboptions."""
    _MAX_DEPTH = 3
    resolved = resolve_schema(raw_pdef, definitions)
    ptype = json_type_to_ansible(resolved.get("type", "string"))
    description = sanitize_text(
        (raw_pdef.get("description") if isinstance(raw_pdef, dict) else None)
        or resolved.get("description")
        or f"Body field {api_name}."
    )
    meta: Dict[str, Any] = {
        "api_name": api_name,
        "description": description,
        "type": ptype,
        "required": required,
        "source": source,
    }
    lname = api_name.lower()
    if any(s in lname for s in _SECRET_SUBSTRINGS):
        meta["no_log"] = True

    # Detect enum choices (handles direct enum, $ref→enum, allOf→scalar enum)
    choices = _get_enum_choices(raw_pdef, definitions)
    if choices:
        meta["choices"] = choices
        return meta

    if ptype == "list":
        raw_items: Dict[str, Any] = (raw_pdef.get("items") or {}) if isinstance(raw_pdef, dict) else {}
        if not raw_items:
            raw_items = resolved.get("items") or {}
        items_resolved = resolve_schema(raw_items, definitions)
        items_type = json_type_to_ansible(items_resolved.get("type", "string"))

        # Array of enum scalars (e.g. sendNotificationsOn: [BackupNotificationType, ...])
        item_choices = _get_enum_choices(raw_items, definitions)
        if item_choices:
            meta["elements"] = "str"
            meta["choices"] = item_choices
            return meta

        # Array of objects
        if items_type == "dict" and depth < _MAX_DEPTH and items_resolved.get("properties"):
            items_props = items_resolved.get("properties", {})
            items_req = set(items_resolved.get("required") or [])
            sub_opts: Dict[str, Any] = {}
            for child_api_name, child_raw in items_props.items():
                child_meta = _build_field_meta(
                    child_api_name, child_raw, definitions,
                    required=(child_api_name in items_req),
                    source=source,
                    depth=depth + 1,
                )
                sub_opts[snake(child_api_name)] = child_meta
            meta["elements"] = "dict"
            if sub_opts:
                meta["options"] = sub_opts
        else:
            meta["elements"] = items_type if items_type != "dict" else "str"
        return meta

    # Nested object
    if ptype == "dict" and depth < _MAX_DEPTH and resolved.get("properties"):
        props = resolved.get("properties", {})
        req_set = set(resolved.get("required") or [])
        sub_opts = {}
        for child_api_name, child_raw in props.items():
            child_meta = _build_field_meta(
                child_api_name, child_raw, definitions,
                required=(child_api_name in req_set),
                source=source,
                depth=depth + 1,
            )
            sub_opts[snake(child_api_name)] = child_meta
        if sub_opts:
            meta["options"] = sub_opts

    return meta


def extract_body_fields(schema: Dict[str, Any], definitions: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    schema = resolve_schema(schema, definitions)
    if not isinstance(schema, dict):
        return {}
    props = schema.get("properties") or {}
    required = set(schema.get("required") or [])
    out: Dict[str, Dict[str, Any]] = {}
    for api_name, pdef in props.items():
        name = snake(api_name)
        out[name] = _build_field_meta(
            api_name, pdef, definitions,
            required=(api_name in required),
            source="body",
            depth=0,
        )
    return out


def success_response_schema(op_spec: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    responses = (op_spec or {}).get("responses", {}) or {}
    for code in ("200", "201"):
        response = responses.get(code)
        if isinstance(response, dict) and isinstance(response.get("schema"), dict):
            return response["schema"]
    return None


def schema_fields(schema: Any, definitions: Dict[str, Any], depth: int = 0) -> Dict[str, Dict[str, Any]]:
    schema = resolve_schema(schema, definitions)
    if not isinstance(schema, dict):
        return {}

    props = schema.get("properties") or {}
    out: Dict[str, Dict[str, Any]] = {}
    for api_name, raw_field in props.items():
        field_schema = resolve_schema(raw_field, definitions)
        field_name = snake(api_name)
        field_type = json_type_to_ansible(field_schema.get("type", "string"))
        field_meta: Dict[str, Any] = {
            "description": sanitize_text(
                (raw_field.get("description") if isinstance(raw_field, dict) else None)
                or field_schema.get("description")
                or f"Field {api_name}."
            ),
            "type": field_type,
        }

        if field_type == "list":
            items = resolve_schema(field_schema.get("items", {}), definitions)
            field_meta["elements"] = json_type_to_ansible(items.get("type", "string"))
            if depth < 3 and items.get("properties"):
                nested = schema_fields(items, definitions, depth + 1)
                if nested:
                    field_meta["contains"] = nested
        elif field_type == "dict" and depth < 3 and field_schema.get("properties"):
            nested = schema_fields(field_schema, definitions, depth + 1)
            if nested:
                field_meta["contains"] = nested

        out[field_name] = field_meta

    return out


def resource_response_fields(ops: Dict[str, Any], definitions: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    for operation_name in ("get", "create", "update", "list"):
        op = ops.get(operation_name)
        if not op:
            continue

        schema = success_response_schema(op.get("spec", {}))
        if not schema:
            continue

        resolved = resolve_schema(schema, definitions)

        if operation_name == "list":
            list_item_schema = None
            for list_field in (resolved.get("properties") or {}).values():
                list_field_schema = resolve_schema(list_field, definitions)
                if json_type_to_ansible(list_field_schema.get("type", "string")) != "list":
                    continue
                candidate_items = resolve_schema(list_field_schema.get("items", {}), definitions)
                if isinstance(candidate_items, dict) and candidate_items.get("properties"):
                    list_item_schema = candidate_items
                    break
            if list_item_schema is not None:
                resolved = list_item_schema

        fields = schema_fields(resolved, definitions)
        if fields:
            return fields

    return {}


def render_return_fields(fields: Dict[str, Dict[str, Any]], indent: int = 4) -> List[str]:
    padding = " " * indent
    lines: List[str] = []
    for name in sorted(fields):
        field_meta = fields[name]
        description = sanitize_text(field_meta.get("description") or f"Field {name}.")
        wrapped_description = textwrap.wrap(description, width=100) or [description]

        lines.append(f"{padding}{name}:")
        lines.append(f"{padding}    description:")
        for desc_line in wrapped_description:
            escaped_line = desc_line.replace("\\", "\\\\").replace('"', '\\"')
            lines.append(f'{padding}      - "{escaped_line}"')
        lines.append(f"{padding}    type: {field_meta.get('type', 'raw')}")
        if field_meta.get("elements"):
            lines.append(f"{padding}    elements: {field_meta['elements']}")
        lines.append(f"{padding}    returned: success")

        nested = field_meta.get("contains")
        if isinstance(nested, dict) and nested:
            lines.append(f"{padding}    contains:")
            lines.extend(render_return_fields(nested, indent + 8))

    return lines


def pick_best(ops: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    if not ops:
        return None
    return sorted(ops, key=lambda x: (len(x["path"]), x["path"]))[0]


def option_doc_block(name: str, meta: Dict[str, Any], indent: int = 0) -> str:
    i = indent
    lines = [f"{' ' * (i + 2)}{name}:"]
    lines.append(f"{' ' * (i + 4)}description:")
    desc = sanitize_text(meta.get("description", "No description.")).replace(":", ";")
    lines.append(f"{' ' * (i + 6)}- {desc}")
    lines.append(f"{' ' * (i + 4)}type: {meta.get('type', 'str')}")
    if meta.get("type") == "list":
        lines.append(f"{' ' * (i + 4)}elements: {meta.get('elements', 'str')}")
    if meta.get("required"):
        lines.append(f"{' ' * (i + 4)}required: true")
    if "choices" in meta:
        lines.append(f"{' ' * (i + 4)}choices:")
        for choice in meta["choices"]:
            choice_str = str(choice)
            if _needs_yaml_quoting(choice_str):
                lines.append(f"{' ' * (i + 6)}- '{choice_str}'")
            else:
                lines.append(f"{' ' * (i + 6)}- {choice_str}")
    if "default" in meta:
        lines.append(f"{' ' * (i + 4)}default: {meta['default']}")
    sub_opts = meta.get("options")
    if sub_opts:
        lines.append(f"{' ' * (i + 4)}suboptions:")
        for sub_name in sorted(sub_opts):
            lines.append(option_doc_block(sub_name, sub_opts[sub_name], indent=i + 4))
    return "\n".join(lines)


def arg_spec_line(meta: Dict[str, Any]) -> str:
    """Return the dict(...) fragment for a simple (non-nested) arg_spec entry."""
    chunks = [f"type='{meta.get('type', 'str')}'"]
    if meta.get("type") == "list":
        chunks.append(f"elements='{meta.get('elements', 'str')}'")
    if meta.get("required"):
        chunks.append("required=True")
    if "default" in meta:
        chunks.append(f"default='{meta['default']}'")
    if "choices" in meta:
        choices = ", ".join([f"'{c}'" for c in meta["choices"]])
        chunks.append(f"choices=[{choices}]")
    if meta.get("no_log"):
        chunks.append("no_log=True")
    return f"dict({', '.join(chunks)})"


def format_list_literal(values: List[str]) -> str:
    if not values:
        return "[]"
    return "[\n" + "\n".join(f"    {repr(value)}," for value in values) + "\n]"


def format_dict_literal(values: Dict[str, str]) -> str:
    if not values:
        return "{}"
    lines = [f"    {repr(key)}: {repr(val)}," for key, val in values.items()]
    return "{\n" + "\n".join(lines) + "\n}"


def _meta_to_schema_info(meta: Dict[str, Any]) -> Dict[str, Any]:
    """Convert internal field meta to the compact form stored in BODY_SCHEMA."""
    info: Dict[str, Any] = {"api": meta.get("api_name", ""), "type": meta.get("type", "str")}
    sub_opts = meta.get("options")
    if sub_opts:
        info["nested"] = {k: _meta_to_schema_info(v) for k, v in sub_opts.items()}
    return info


def _format_schema_literal(schema: Dict[str, Any], indent: int = 0) -> str:
    """Render a BODY_SCHEMA dict as valid Python source code."""
    if not schema:
        return "{}"
    prefix = " " * indent
    inner = " " * (indent + 4)
    lines = ["{"]
    for name, info in schema.items():
        nested = info.get("nested")
        ftype = info.get("type", "str")
        api = info.get("api", "")
        if nested:
            nested_str = _format_schema_literal(nested, indent + 8)
            lines.append(f"{inner}{repr(name)}: {{")
            lines.append(f"{inner}    'api': {repr(api)},")
            lines.append(f"{inner}    'type': {repr(ftype)},")
            lines.append(f"{inner}    'nested': {nested_str},")
            lines.append(f"{inner}}},")
        else:
            lines.append(f"{inner}{repr(name)}: {{'api': {repr(api)}, 'type': {repr(ftype)}}},")
    lines.append(f"{prefix}}}")
    return "\n".join(lines)


def _format_nested_arg_spec(meta: Dict[str, Any], indent: int) -> str:
    """Return the dict(...) fragment for one arg_spec entry, with recursive suboptions."""
    ptype = meta.get("type", "str")
    chunks: List[str] = [f"type='{ptype}'"]
    if ptype == "list":
        chunks.append(f"elements='{meta.get('elements', 'str')}'")
    if meta.get("required"):
        chunks.append("required=True")
    if "default" in meta:
        chunks.append(f"default='{meta['default']}'")
    if "choices" in meta:
        choices_str = ", ".join(f"'{c}'" for c in meta["choices"])
        chunks.append(f"choices=[{choices_str}]")
    if meta.get("no_log"):
        chunks.append("no_log=True")

    sub_opts = meta.get("options")
    if not sub_opts:
        simple = f"dict({', '.join(chunks)})"
        # Break onto multiple lines when too long to avoid pep8 E501
        if len(simple) > 110:
            inner_indent = indent + 4
            chunks_joined = f",\n{' ' * inner_indent}".join(chunks)
            return f"dict(\n{' ' * inner_indent}{chunks_joined},\n{' ' * indent})"
        return simple

    # Has nested options → emit multiline.
    # Use dict-literal syntax {key: val} (not dict(key=val) kwargs) so that
    # API field names that are Python keywords (e.g. 'from') remain valid.
    inner_indent = indent + 4
    chunks_joined = f",\n{' ' * inner_indent}".join(chunks)
    sub_lines = []
    for sub_name in sorted(sub_opts):
        sub_spec = _format_nested_arg_spec(sub_opts[sub_name], inner_indent + 4)
        sub_lines.append(f"{' ' * (inner_indent + 4)}{repr(sub_name)}: {sub_spec},")
    sub_block = "\n".join(sub_lines)
    return (
        f"dict(\n"
        f"{' ' * inner_indent}{chunks_joined},\n"
        f"{' ' * inner_indent}options={{\n"
        f"{sub_block}\n"
        f"{' ' * inner_indent}}},\n"
        f"{' ' * indent})"
    )


def format_arg_spec_entry(name: str, meta: Dict[str, Any], indent: int = 8) -> str:
    """Return the complete arg_spec line(s) for one module parameter."""
    spec = _format_nested_arg_spec(meta, indent)
    return f"{' ' * indent}{name}={spec},"


def create_jinja_env(template_dir: Path) -> Environment:
    return Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=False,
        keep_trailing_newline=True,
    )


def derive_collection_names(output_dir: Path) -> Tuple[str, str]:
    parts = output_dir.parts
    if "ansible_collections" in parts:
        idx = parts.index("ansible_collections")
        if idx + 2 < len(parts):
            return parts[idx + 1], parts[idx + 2]
    return "zeqk", "databasus"


def _project_readme(readme_value: Any) -> Optional[str]:
    if isinstance(readme_value, str) and readme_value.strip():
        return Path(readme_value.strip()).name
    if isinstance(readme_value, dict):
        file_value = readme_value.get("file")
        if isinstance(file_value, str) and file_value.strip():
            return Path(file_value.strip()).name
    return None


def _project_license(license_value: Any) -> Optional[str]:
    if isinstance(license_value, str) and license_value.strip():
        return license_value.strip()
    if isinstance(license_value, dict):
        for key in ("text", "file"):
            raw_value = license_value.get(key)
            if isinstance(raw_value, str) and raw_value.strip():
                return raw_value.strip()
    return None


def load_galaxy_metadata(pyproject_path: Path, output_dir: Path) -> Dict[str, Any]:
    namespace, name = derive_collection_names(output_dir)
    metadata: Dict[str, Any] = {
        "namespace": namespace,
        "name": name,
        "version": "1.0.0",
        "readme": "README.md",
        "description": "Ansible collection to manage Databasus resources via REST API.",
        "license": ["MIT"],
        "authors": ["zeqk"],
        "tags": ["database", "api", "crud"],
        "dependencies": {},
    }

    if not pyproject_path.exists():
        return metadata

    pyproject = tomllib.loads(pyproject_path.read_text())
    project = pyproject.get("project", {}) if isinstance(pyproject, dict) else {}
    if not isinstance(project, dict):
        return metadata

    version = project.get("version")
    if isinstance(version, str) and version.strip():
        metadata["version"] = version.strip()

    description = project.get("description")
    if isinstance(description, str) and description.strip():
        metadata["description"] = description.strip().rstrip(".") + "."

    readme = _project_readme(project.get("readme"))
    if readme:
        metadata["readme"] = readme

    license_name = _project_license(project.get("license"))
    if license_name:
        metadata["license"] = [license_name]

    authors = project.get("authors")
    if isinstance(authors, list):
        parsed_authors: List[str] = []
        for author in authors:
            if isinstance(author, dict):
                author_name = author.get("name")
                if isinstance(author_name, str) and author_name.strip():
                    parsed_authors.append(author_name.strip())
        if parsed_authors:
            metadata["authors"] = parsed_authors

    keywords = project.get("keywords")
    if isinstance(keywords, list):
        parsed_keywords = [k.strip() for k in keywords if isinstance(k, str) and k.strip()]
        if parsed_keywords:
            metadata["tags"] = parsed_keywords

    return metadata


def build_resources(spec: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    paths = spec.get("paths", {})
    definitions = spec.get("definitions", {})

    resource_ops: Dict[str, Dict[str, List[Dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    for path, op_map in paths.items():
        resource = resource_from_path(path)
        for method, op in op_map.items():
            m = method.lower()
            if m not in HTTP_METHODS:
                continue
            crud = classify(m, path)
            if not crud:
                continue
            resource_ops[resource][crud].append(
                {
                    "method": m,
                    "path": path,
                    "spec": op,
                    "operation_id": op.get("operationId", ""),
                    "parameters": op.get("parameters", []),
                }
            )

    resources: Dict[str, Dict[str, Any]] = {}
    for resource, grouped in resource_ops.items():
        selected = {k: pick_best(v) for k, v in grouped.items()}
        ops_present = [k for k, v in selected.items() if v]
        if not ops_present:
            continue

        mutable = any(selected.get(k) for k in ("create", "update", "delete"))

        params: Dict[str, Dict[str, Any]] = {
            "api_url": {
                "api_name": "api_url",
                "description": "Base API URL.",
                "type": "str",
                "required": True,
                "source": "base",
            },
            "api_token": {
                "api_name": "api_token",
                "description": "Bearer authentication token.",
                "type": "str",
                "required": True,
                "source": "base",
                "no_log": True,
            },
        }
        if mutable:
            params["state"] = {
                "api_name": "state",
                "description": "Desired state of the resource.",
                "type": "str",
                "required": False,
                "default": "present",
                "choices": ["present", "absent"],
                "source": "base",
            }

        for _, op in selected.items():
            if not op:
                continue
            for p in op.get("parameters", []):
                pin = p.get("in")
                if pin == "header":
                    continue

                if pin == "body":
                    for k, v in extract_body_fields(p.get("schema", {}), definitions).items():
                        if k in params and params[k].get("source") in {"path", "query"}:
                            continue
                        params[k] = v
                    continue

                pname = snake(p.get("name", "param"))
                existing = params.get(pname)
                required = bool(p.get("required", False))
                source = "path" if pin == "path" else "query"
                desc = sanitize_text(p.get("description") or f"Parameter {p.get('name', pname)}.")
                ptype = json_type_to_ansible(p.get("type", "string"))
                elements = None
                if ptype == "list":
                    elements = json_type_to_ansible(p.get("items", {}).get("type", "string"))

                if existing:
                    # Path/query requiredness is operation-specific and enforced at runtime.
                    # Do not promote it to a global argument requirement.
                    if source in {"path", "query"}:
                        existing["required_in_api"] = existing.get("required_in_api", False) or required
                    else:
                        existing["required"] = existing.get("required", False) or required
                    continue

                params[pname] = {
                    "api_name": p.get("name", pname),
                    "description": desc,
                    "type": ptype,
                    "required": False if source in {"path", "query"} else required,
                    "source": source,
                    "required_in_api": required,
                }
                if elements:
                    params[pname]["elements"] = elements
                # Capture enum choices for query/path params
                p_enum = p.get("enum")
                if p_enum:
                    params[pname]["choices"] = [str(v) for v in p_enum]
                elif ptype == "list":
                    items_spec = p.get("items") or {}
                    item_enum = items_spec.get("enum") if isinstance(items_spec, dict) else None
                    if item_enum:
                        params[pname]["choices"] = [str(v) for v in item_enum]
                lname = str(p.get("name", pname)).lower()
                if any(secret in lname for secret in ("token", "secret", "password", "apikey", "api_key", "key")):
                    params[pname]["no_log"] = True

        resources[resource] = {
            "name": resource,
            "mutable": mutable,
            "ops": selected,
            "params": params,
            "ops_present": ops_present,
        }

    return resources


def generate_collection(spec_path: Path, output_dir: Path) -> Tuple[int, List[Tuple[str, str]]]:
    spec = json.loads(spec_path.read_text())
    paths = spec.get("paths", {})
    definitions = spec.get("definitions", {})
    resources = build_resources(spec)
    template_dir = Path(__file__).resolve().parent / "templates"
    template_env = create_jinja_env(template_dir)
    pyproject_path = Path(__file__).resolve().parent.parent / "pyproject.toml"
    galaxy_metadata = load_galaxy_metadata(pyproject_path, output_dir)

    modules_dir = output_dir / "plugins" / "modules"
    roles_dir = output_dir / "roles"
    modules_dir.mkdir(parents=True, exist_ok=True)
    roles_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "galaxy.yml").write_text(template_env.get_template("galaxy.yml.j2").render(**galaxy_metadata))

    (roles_dir / ".gitkeep").write_text("")

    module_rows: List[Tuple[str, str]] = []

    for resource in sorted(resources):
        data = resources[resource]
        ops = data["ops"]
        params = data["params"]
        mutable = data["mutable"]

        body_field_names: List[str] = []
        body_field_api_map: Dict[str, str] = {}
        path_params_by_op: Dict[str, List[str]] = {}
        query_params_by_op: Dict[str, List[str]] = {}

        for opname, op in ops.items():
            if not op:
                continue
            pnames: List[str] = []
            qnames: List[str] = []
            for p in op.get("parameters", []):
                if p.get("in") == "path":
                    pnames.append(snake(p["name"]))
                elif p.get("in") == "query":
                    qnames.append(snake(p["name"]))
                elif p.get("in") == "body":
                    fields = extract_body_fields(p.get("schema", {}), definitions)
                    body_field_names.extend(fields.keys())
                    for field_name, field_meta in fields.items():
                        body_field_api_map[field_name] = field_meta.get("api_name", field_name)
            path_params_by_op[opname] = sorted(set(pnames))
            query_params_by_op[opname] = sorted(set(qnames))

        body_field_names = sorted(set(body_field_names))

        body_schema = {}
        for field_name in body_field_names:
            if field_name not in params:
                continue
            meta = dict(params[field_name])
            # The query/path param for this field may have been recorded with a
            # snake_case api_name (e.g. "workspace_id") while the body uses the
            # original camelCase name (e.g. "workspaceId"). Always prefer the
            # body's api_name so the request payload uses the correct key.
            if field_name in body_field_api_map:
                meta["api_name"] = body_field_api_map[field_name]
            body_schema[field_name] = _meta_to_schema_info(meta)
        body_schema_literal = _format_schema_literal(body_schema)

        name_addressable = "name" in body_field_names and bool(ops.get("list"))
        create_spec = (ops.get("create") or {}).get("spec", {})
        create_text = " ".join(
            [
                sanitize_text(create_spec.get("summary") or ""),
                sanitize_text(create_spec.get("description") or ""),
            ]
        )
        create_is_upsert = bool(re.search(r"\bcreate\s+or\s+update\b", create_text, flags=re.IGNORECASE))

        if name_addressable and "name" in params:
            params["name"]["required"] = True

        input_excluded: set[str] = set()
        if name_addressable and "id" in params:
            input_excluded.add("id")

        name_field = "name" if name_addressable and "name" in params else ""
        id_field = "id" if name_addressable and "id" in params else ""
        name_api = body_field_api_map.get(name_field, name_field) if name_field else ""
        id_api = body_field_api_map.get(id_field, id_field) if id_field else ""
        match_fields: List[Tuple[str, str]] = []
        if name_addressable:
            for field_name in sorted(body_field_names):
                field_api_name = body_field_api_map.get(field_name, field_name)
                if re.fullmatch(r"workspace_?id", field_name, flags=re.IGNORECASE) or re.fullmatch(
                    r"workspace_?id", field_api_name, flags=re.IGNORECASE
                ):
                    match_fields.append((field_name, field_api_name))

        def op_const(name: str) -> Tuple[str, str, str, str]:
            op = ops.get(name)
            if not op:
                return "None", "None", "[]", "[]"
            return (
                repr(op["method"].upper()),
                repr(op["path"]),
                repr(path_params_by_op.get(name, [])),
                repr(query_params_by_op.get(name, [])),
            )

        c_method, c_path, c_pp, c_qp = op_const("create")
        l_method, l_path, l_pp, l_qp = op_const("list")
        g_method, g_path, g_pp, g_qp = op_const("get")
        u_method, u_path, u_pp, u_qp = op_const("update")
        d_method, d_path, d_pp, d_qp = op_const("delete")

        operation_ids = []
        for key in ("create", "list", "get", "update", "delete"):
            op = ops.get(key)
            if op and op.get("operation_id"):
                operation_ids.append(f"{key}={op['operation_id']}")

        option_blocks = []
        ordered = ["state", "api_url", "api_token"] + sorted(
            [k for k in params if k not in {"state", "api_url", "api_token"} and k not in input_excluded]
        )
        for k in ordered:
            if k in params:
                option_blocks.append(option_doc_block(k, params[k]))

        desc_lines = [f"  - Allows managing {resource} resources using the Databasus API."]
        if operation_ids:
            desc_lines.append("  - operationId references are included in generated operation constants.")
        if not mutable:
            desc_lines.append("  - This module is read-only and does not support state=absent.")

        examples = [
            "- name: Query resource",
            f"  zeqk.databasus.{resource}:",
            "    api_url: https://api.example.com",
            '    api_token: "{{ databasus_token }}"',
        ]
        if mutable:
            examples = [
                "- name: Create or update resource",
                f"  zeqk.databasus.{resource}:",
                "    state: present",
                "    api_url: https://api.example.com",
                '    api_token: "{{ databasus_token }}"',
            ]
        if mutable and name_field:
            examples.append("    name: example-name")
        for name in sorted(params):
            if name in {"state", "api_url", "api_token"}:
                continue
            if name in input_excluded or (name_field and name == name_field):
                continue
            if params[name]["source"] == "body":
                examples.append(f"    {name}: null")
                break
        if ops.get("delete"):
            examples += [
                "",
                "- name: Delete resource",
                f"  zeqk.databasus.{resource}:",
                "    state: absent",
                "    api_url: https://api.example.com",
                '    api_token: "{{ databasus_token }}"',
            ]
            if name_field:
                examples.append("    name: example-name")

        arg_lines = [format_arg_spec_entry(p, params[p]) for p in ordered if p in params]

        required_delete = [p for p in path_params_by_op.get("delete", []) if params.get(p, {}).get("required_in_api")]
        required_get = [p for p in path_params_by_op.get("get", []) if params.get(p, {}).get("required_in_api")]
        required_create = [p for p in path_params_by_op.get("create", []) if params.get(p, {}).get("required_in_api")]
        required_list_query = [p for p in query_params_by_op.get("list", []) if params.get(p, {}).get("required_in_api")]

        api_name_map = {k: v["api_name"] for k, v in params.items() if "api_name" in v}

        match_fields_literal = repr(match_fields)
        api_name_map_literal = format_dict_literal(api_name_map)
        resource_return_fields = resource_response_fields(ops, definitions)
        return_resource_contains_block = ""
        if resource_return_fields:
            return_resource_contains_block = "\n    contains:\n" + "\n".join(
                render_return_fields(resource_return_fields, indent=8)
            )

        module_template = template_env.get_template("module.py.j2")
        code = module_template.render(
            resource=resource,
            desc_block="\n".join(desc_lines),
            option_blocks_block="\n".join(option_blocks),
            examples_block="\n".join(examples),
            return_resource_contains_block=return_resource_contains_block,
            c_method=c_method,
            c_path=c_path,
            c_pp=c_pp,
            c_qp=c_qp,
            l_method=l_method,
            l_path=l_path,
            l_pp=l_pp,
            l_qp=l_qp,
            g_method=g_method,
            g_path=g_path,
            g_pp=g_pp,
            g_qp=g_qp,
            u_method=u_method,
            u_path=u_path,
            u_pp=u_pp,
            u_qp=u_qp,
            d_method=d_method,
            d_path=d_path,
            d_pp=d_pp,
            d_qp=d_qp,
            body_schema_literal=body_schema_literal,
            read_only=str(not mutable),
            api_name_map_literal=api_name_map_literal,
            required_delete=repr(required_delete),
            required_get=repr(required_get),
            required_create=repr(required_create),
            required_list_query=repr(required_list_query),
            name_addressable=str(name_addressable),
            name_field_repr=repr(name_field),
            name_api_repr=repr(name_api),
            id_field_repr=repr(id_field),
            id_api_repr=repr(id_api),
            match_fields_literal=match_fields_literal,
            create_is_upsert=str(create_is_upsert),
            arg_lines_block="\n".join(arg_lines),
        )

        (modules_dir / f"{resource}.py").write_text(code)
        module_rows.append((resource, ", ".join(sorted(data["ops_present"]))))

        if name_addressable and name_field and ops.get("list"):
            info_ordered = ["api_url", "api_token", name_field]
            for field_name, _field_api_name in match_fields:
                if field_name in params and field_name not in info_ordered:
                    info_ordered.append(field_name)
            for field_name in required_list_query:
                if field_name in params and field_name not in info_ordered:
                    info_ordered.append(field_name)

            info_option_blocks = [option_doc_block(k, params[k]) for k in info_ordered if k in params]
            info_arg_lines = [f"        {p}={arg_spec_line(params[p])}," for p in info_ordered if p in params]

            info_template = template_env.get_template("module_info.py.j2")
            info_code = info_template.render(
                resource=resource,
                module_name=f"{resource}_info",
                option_blocks_block="\n".join(info_option_blocks),
                return_resource_contains_block=return_resource_contains_block,
                l_method=l_method,
                l_path=l_path,
                l_pp=l_pp,
                l_qp=l_qp,
                api_name_map_literal=api_name_map_literal,
                required_list_query=repr(required_list_query),
                name_field_repr=repr(name_field),
                name_api_repr=repr(name_api),
                match_fields_literal=match_fields_literal,
                arg_lines_block="\n".join(info_arg_lines),
            )

            (modules_dir / f"{resource}_info.py").write_text(info_code)
            module_rows.append((f"{resource}_info", "get_by_name"))

    for (method, path), module_name in PUBLIC_ACTION_MODULES.items():
        path_item = paths.get(path) if isinstance(paths, dict) else None
        op = path_item.get(method) if isinstance(path_item, dict) else None
        if not isinstance(op, dict):
            continue

        params: Dict[str, Dict[str, Any]] = {
            "api_url": {
                "api_name": "api_url",
                "description": "Base API URL.",
                "type": "str",
                "required": True,
                "source": "base",
            }
        }

        for p in op.get("parameters", []):
            if p.get("in") != "body":
                continue
            params.update(extract_body_fields(p.get("schema", {}), definitions))

        ordered = ["api_url"] + sorted([k for k in params if k != "api_url"])
        option_blocks = [option_doc_block(k, params[k]) for k in ordered if k in params]
        arg_lines = [f"        {p}={arg_spec_line(params[p])}," for p in ordered if p in params]

        response_fields: Dict[str, Dict[str, Any]] = {}
        response_schema = success_response_schema(op)
        if response_schema:
            response_fields = schema_fields(response_schema, definitions)

        return_resource_contains_block = ""
        if response_fields:
            return_resource_contains_block = "\n    contains:\n" + "\n".join(
                render_return_fields(response_fields, indent=8)
            )

        signin_template = template_env.get_template("user_signin.py.j2")
        signin_code = signin_template.render(
            module_name=module_name,
            option_blocks_block="\n".join(option_blocks),
            arg_lines_block="\n".join(arg_lines),
            return_resource_contains_block=return_resource_contains_block,
            signin_method=repr(method.upper()),
            signin_path=repr(path),
        )

        (modules_dir / f"{module_name}.py").write_text(signin_code)
        module_rows.append((module_name, "signin"))

    readme = template_env.get_template("README.md.j2").render(module_rows=sorted(module_rows))
    (output_dir / "README.md").write_text(readme)

    return len(module_rows), module_rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate zeqk.databasus collection from OpenAPI/Swagger spec")
    parser.add_argument("--spec", default="openapi.json", help="Path to OpenAPI/Swagger JSON spec")
    parser.add_argument("--output", default="zeqk/databasus", help="Collection output directory")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    spec_path = Path(args.spec)
    output_dir = Path(args.output)

    if not spec_path.exists():
        raise SystemExit(f"Spec not found: {spec_path}")

    count, _ = generate_collection(spec_path, output_dir)
    print(f"Collection generated in: {output_dir}")
    print(f"Modules generated: {count}")


if __name__ == "__main__":
    main()
