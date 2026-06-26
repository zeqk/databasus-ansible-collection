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

HTTP_METHODS = {"get", "post", "put", "patch", "delete"}


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
        merged = {"type": "object", "properties": {}, "required": []}
        for sub in schema["allOf"]:
            part = resolve_schema(sub, definitions, depth + 1)
            merged["properties"].update(part.get("properties", {}))
            merged["required"].extend(part.get("required", []))
        merged["required"] = sorted(set(merged["required"]))
        return merged

    return schema


def extract_body_fields(schema: Dict[str, Any], definitions: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    schema = resolve_schema(schema, definitions)
    if not isinstance(schema, dict):
        return {}

    props = schema.get("properties") or {}
    required = set(schema.get("required") or [])
    out: Dict[str, Dict[str, Any]] = {}
    for api_name, pdef in props.items():
        pdef = resolve_schema(pdef, definitions)
        name = snake(api_name)
        ptype = json_type_to_ansible(pdef.get("type", "string"))
        elements = None
        if ptype == "list":
            items = resolve_schema(pdef.get("items", {}), definitions)
            elements = json_type_to_ansible(items.get("type", "string"))
        out[name] = {
            "api_name": api_name,
            "description": sanitize_text(pdef.get("description") or f"Body field {api_name}."),
            "type": ptype,
            "required": api_name in required,
            "source": "body",
        }
        if elements:
            out[name]["elements"] = elements
        lname = api_name.lower()
        if any(secret in lname for secret in ("token", "secret", "password", "apikey", "api_key", "key")):
            out[name]["no_log"] = True
    return out


def pick_best(ops: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    if not ops:
        return None
    return sorted(ops, key=lambda x: (len(x["path"]), x["path"]))[0]


def option_doc_block(name: str, meta: Dict[str, Any]) -> str:
    lines = [f"  {name}:"]
    lines.append("    description:")
    lines.append(f"      - {sanitize_text(meta.get('description', 'No description.')).replace(':', ';')}")
    lines.append(f"    type: {meta.get('type', 'str')}")
    if meta.get("type") == "list":
        lines.append(f"    elements: {meta.get('elements', 'str')}")
    if meta.get("required"):
        lines.append("    required: true")
    if "choices" in meta:
        lines.append("    choices:")
        for choice in meta["choices"]:
            lines.append(f"      - {choice}")
    if "default" in meta:
        lines.append(f"    default: {meta['default']}")
    return "\n".join(lines)


def arg_spec_line(meta: Dict[str, Any]) -> str:
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
    definitions = spec.get("definitions", {})
    resources = build_resources(spec)

    modules_dir = output_dir / "plugins" / "modules"
    roles_dir = output_dir / "roles"
    modules_dir.mkdir(parents=True, exist_ok=True)
    roles_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "galaxy.yml").write_text(
        "\n".join(
            [
                "namespace: zeqk",
                "name: databasus",
                "version: 1.0.0",
                "readme: README.md",
                "description: Ansible collection to manage Databasus resources via REST API.",
                "license:",
                "  - MIT",
                "authors:",
                "  - zeqk",
                "tags:",
                "  - database",
                "  - api",
                "  - crud",
                "dependencies: {}",
                "",
            ]
        )
    )

    (roles_dir / ".gitkeep").write_text("")

    module_rows: List[Tuple[str, str]] = []

    for resource in sorted(resources):
        data = resources[resource]
        ops = data["ops"]
        params = data["params"]
        mutable = data["mutable"]

        body_field_names: List[str] = []
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
                    body_field_names.extend(extract_body_fields(p.get("schema", {}), definitions).keys())
            path_params_by_op[opname] = sorted(set(pnames))
            query_params_by_op[opname] = sorted(set(qnames))

        body_field_names = sorted(set(body_field_names))

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
        ordered = ["state", "api_url", "api_token"] + sorted([k for k in params if k not in {"state", "api_url", "api_token"}])
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
        for name in sorted(params):
            if name in {"state", "api_url", "api_token"}:
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

        arg_lines = [f"        {p}={arg_spec_line(params[p])}," for p in ordered if p in params]

        required_delete = [p for p in path_params_by_op.get("delete", []) if params.get(p, {}).get("required_in_api")]
        required_get = [p for p in path_params_by_op.get("get", []) if params.get(p, {}).get("required_in_api")]
        required_create = [p for p in path_params_by_op.get("create", []) if params.get(p, {}).get("required_in_api")]

        api_name_map = {k: v["api_name"] for k, v in params.items() if "api_name" in v}

        body_fields_literal = format_list_literal(body_field_names)
        api_name_map_literal = format_dict_literal(api_name_map)

        code = textwrap.dedent(
            f'''
#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2026, zeqk (@zeqk)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: {resource}
short_description: Manage {resource} resources in Databasus.
description:
{chr(10).join(desc_lines)}
options:
{chr(10).join(option_blocks)}
author:
    - zeqk (@zeqk)
"""

EXAMPLES = r"""
{chr(10).join(examples)}
"""

RETURN = r"""
resource:
    description: Resource object as returned by the API.
    type: dict
    returned: always
changed:
    description: Indicates whether any change was made.
    type: bool
    returned: always
msg:
    description: Descriptive operation message.
    type: str
    returned: always
"""


import json
from typing import Any, Dict, List, Optional, Tuple
from urllib import error, parse

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import open_url


CREATE_METHOD = {c_method}
CREATE_PATH = {c_path}
CREATE_PATH_PARAMS = {c_pp}
CREATE_QUERY_PARAMS = {c_qp}
LIST_METHOD = {l_method}
LIST_PATH = {l_path}
LIST_PATH_PARAMS = {l_pp}
LIST_QUERY_PARAMS = {l_qp}
GET_METHOD = {g_method}
GET_PATH = {g_path}
GET_PATH_PARAMS = {g_pp}
GET_QUERY_PARAMS = {g_qp}
UPDATE_METHOD = {u_method}
UPDATE_PATH = {u_path}
UPDATE_PATH_PARAMS = {u_pp}
UPDATE_QUERY_PARAMS = {u_qp}
DELETE_METHOD = {d_method}
DELETE_PATH = {d_path}
DELETE_PATH_PARAMS = {d_pp}
DELETE_QUERY_PARAMS = {d_qp}
BODY_FIELDS = {body_fields_literal}
READ_ONLY = {str(not mutable)}
API_NAME_MAP = {api_name_map_literal}
REQUIRED_DELETE_PATH_PARAMS = {repr(required_delete)}
REQUIRED_GET_PATH_PARAMS = {repr(required_get)}
REQUIRED_CREATE_PATH_PARAMS = {repr(required_create)}


def _build_url(api_url: str, path_template: str, path_params: Dict[str, Any], query_params: Optional[Dict[str, Any]] = None) -> str:
    encoded = {{k: parse.quote(str(v), safe='') for k, v in path_params.items()}}
    path = path_template.format(**encoded)
    url = api_url.rstrip('/') + path
    clean_query = {{k: v for k, v in (query_params or {{}}).items() if v is not None}}
    if clean_query:
        url += '?' + parse.urlencode(clean_query, doseq=True)
    return url


def _decode_body(raw: str) -> Any:
    if not raw:
        return {{}}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {{'raw': raw}}


def _request_json(
    module: AnsibleModule,
    method: str,
    url: str,
    token: str,
    payload: Optional[Dict[str, Any]] = None,
    expected_statuses: Optional[List[int]] = None,
    allow_statuses: Optional[List[int]] = None,
) -> Tuple[int, Any]:
    headers = {{
        'Accept': 'application/json',
        'Authorization': f'Bearer {{token}}',
    }}
    data = None
    if payload is not None:
        headers['Content-Type'] = 'application/json'
        data = json.dumps(payload).encode('utf-8')

    try:
        with open_url(
            url,
            data=data,
            headers=headers,
            method=method,
            timeout=30,
        ) as response:
            status = int(response.getcode())
            raw = response.read().decode('utf-8')
    except error.HTTPError as exc:
        status = int(exc.code)
        raw = exc.read().decode('utf-8', errors='replace')
        if allow_statuses and status in allow_statuses:
            return status, _decode_body(raw)
        module.fail_json(msg=f'HTTP {{status}} on {{method}} {{url}}: {{raw}}')
    except error.URLError as exc:
        module.fail_json(msg=f'Connection error on {{method}} {{url}}: {{exc}}')

    if expected_statuses and status not in expected_statuses:
        module.fail_json(msg=f'Unexpected HTTP {{status}} on {{method}} {{url}}: {{raw}}')

    return status, _decode_body(raw)


def _collect_params(module_params: Dict[str, Any], names: List[str]) -> Dict[str, Any]:
    out: Dict[str, Any] = {{}}
    for name in names:
        value = module_params.get(name)
        if value is not None:
            out[API_NAME_MAP.get(name, name)] = value
    return out


def _desired_payload(module_params: Dict[str, Any]) -> Dict[str, Any]:
    payload: Dict[str, Any] = {{}}
    for name in BODY_FIELDS:
        value = module_params.get(name)
        if value is not None:
            payload[API_NAME_MAP.get(name, name)] = value
    return payload


def _needs_update(current: Any, desired: Dict[str, Any]) -> bool:
    if not desired:
        return False
    if not isinstance(current, dict):
        return True
    for key, value in desired.items():
        if current.get(key) != value:
            return True
    return False


def _has_required(module_params: Dict[str, Any], names: List[str]) -> bool:
    return all(module_params.get(name) is not None for name in names)


def _ensure_required(module: AnsibleModule, module_params: Dict[str, Any], names: List[str], context: str) -> None:
    missing = [name for name in names if module_params.get(name) is None]
    if missing:
        module.fail_json(msg=f'Missing required parameters for {{context}}: {{", ".join(missing)}}')


def run_module() -> None:
    module_args = dict(
{chr(10).join(arg_lines)}
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=not READ_ONLY)
    params = module.params

    api_url = params['api_url']
    api_token = params['api_token']
    state = params.get('state', 'present')

    result: Dict[str, Any] = dict(changed=False, resource={{}}, msg='No changes')

    if READ_ONLY:
        if GET_PATH and _has_required(params, GET_PATH_PARAMS):
            get_url = _build_url(api_url, GET_PATH, _collect_params(params, GET_PATH_PARAMS), _collect_params(params, GET_QUERY_PARAMS))
            current = _request_json(module, GET_METHOD, get_url, api_token, expected_statuses=[200])[1]
            result['resource'] = current if isinstance(current, dict) else {{'value': current}}
            result['msg'] = 'Single-resource query completed'
            module.exit_json(**result)

        if LIST_PATH:
            list_url = _build_url(api_url, LIST_PATH, _collect_params(params, LIST_PATH_PARAMS), _collect_params(params, LIST_QUERY_PARAMS))
            listing = _request_json(module, LIST_METHOD, list_url, api_token, expected_statuses=[200])[1]
            result['resource'] = listing if isinstance(listing, dict) else {{'items': listing}}
            result['msg'] = 'List query completed'
            module.exit_json(**result)

        result['msg'] = 'No usable GET endpoint for this module'
        module.fail_json(**result)

    exists = False
    current: Any = {{}}

    if GET_PATH and _has_required(params, GET_PATH_PARAMS):
        get_url = _build_url(api_url, GET_PATH, _collect_params(params, GET_PATH_PARAMS), _collect_params(params, GET_QUERY_PARAMS))
        status, body = _request_json(module, GET_METHOD, get_url, api_token, expected_statuses=[200], allow_statuses=[404])
        if status == 200:
            exists = True
            current = body

    desired = _desired_payload(params)

    if state == 'absent':
        if not DELETE_PATH:
            result['msg'] = 'Resource does not support delete operation'
            module.fail_json(**result)
        _ensure_required(module, params, REQUIRED_DELETE_PATH_PARAMS or DELETE_PATH_PARAMS, 'delete')

        if not exists:
            result['msg'] = 'Resource is already absent'
            module.exit_json(**result)

        if module.check_mode:
            result['changed'] = True
            result['msg'] = 'Delete planned (check_mode)'
            module.exit_json(**result)

        delete_url = _build_url(api_url, DELETE_PATH, _collect_params(params, DELETE_PATH_PARAMS), _collect_params(params, DELETE_QUERY_PARAMS))
        _request_json(module, DELETE_METHOD, delete_url, api_token, expected_statuses=[200, 202, 204])
        result['changed'] = True
        result['resource'] = {{}}
        result['msg'] = 'Resource deleted'
        module.exit_json(**result)

    if exists:
        if UPDATE_PATH:
            if not _needs_update(current, desired):
                result['resource'] = current if isinstance(current, dict) else {{'value': current}}
                result['msg'] = 'Resource already in desired state'
                module.exit_json(**result)

            if module.check_mode:
                result['changed'] = True
                result['resource'] = current if isinstance(current, dict) else {{'value': current}}
                result['msg'] = 'Update planned (check_mode)'
                module.exit_json(**result)

            _ensure_required(module, params, UPDATE_PATH_PARAMS, 'update')
            update_url = _build_url(api_url, UPDATE_PATH, _collect_params(params, UPDATE_PATH_PARAMS), _collect_params(params, UPDATE_QUERY_PARAMS))
            updated = _request_json(module, UPDATE_METHOD, update_url, api_token, payload=desired, expected_statuses=[200, 201])[1]
            result['changed'] = True
            result['resource'] = updated if isinstance(updated, dict) else {{'value': updated}}
            result['msg'] = 'Resource updated'
            module.exit_json(**result)

        result['resource'] = current if isinstance(current, dict) else {{'value': current}}
        result['msg'] = 'Resource exists; no update endpoint available'
        module.exit_json(**result)

    if not CREATE_PATH:
        result['msg'] = 'Resource does not exist and there is no create endpoint'
        module.fail_json(**result)

    _ensure_required(module, params, REQUIRED_CREATE_PATH_PARAMS or CREATE_PATH_PARAMS, 'create')

    if module.check_mode:
        result['changed'] = True
        result['msg'] = 'Create planned (check_mode)'
        module.exit_json(**result)

    create_url = _build_url(api_url, CREATE_PATH, _collect_params(params, CREATE_PATH_PARAMS), _collect_params(params, CREATE_QUERY_PARAMS))
    created = _request_json(module, CREATE_METHOD, create_url, api_token, payload=desired, expected_statuses=[200, 201, 202])[1]
    result['changed'] = True
    result['resource'] = created if isinstance(created, dict) else {{'value': created}}
    result['msg'] = 'Resource created'
    module.exit_json(**result)


def main() -> None:
    run_module()


if __name__ == '__main__':
    main()
'''
        ).lstrip()

        (modules_dir / f"{resource}.py").write_text(code)
        module_rows.append((resource, ", ".join(sorted(data["ops_present"]))))

    readme = [
        "# zeqk.databasus",
        "",
        "Ansible collection generated from `openapi.json` to manage Databasus API resources.",
        "",
        "## Requirements",
        "",
        "- Ansible Core 2.14+",
        "- Python 3 on the controller node",
        "",
        "## Generated modules",
        "",
        "| Module | FQCN | Detected operations |",
        "|---|---|---|",
    ]
    for module_name, ops_text in sorted(module_rows):
        readme.append(f"| `{module_name}` | `zeqk.databasus.{module_name}` | `{ops_text}` |")

    readme += [
        "",
        "## Basic usage",
        "",
        "```yaml",
        "- name: Manage database",
        "  hosts: localhost",
        "  tasks:",
        "    - name: Create database",
        "      zeqk.databasus.database:",
        "        state: present",
        "        api_url: \"https://api.databasus.example.com\"",
        "        api_token: \"{{ lookup('env', 'DATABASUS_TOKEN') }}\"",
        "        name: \"production-db\"",
        "",
        "    - name: Delete database",
        "      zeqk.databasus.database:",
        "        state: absent",
        "        api_url: \"https://api.databasus.example.com\"",
        "        api_token: \"{{ lookup('env', 'DATABASUS_TOKEN') }}\"",
        "        id: \"db-abc123\"",
        "```",
    ]
    (output_dir / "README.md").write_text("\n".join(readme) + "\n")

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
