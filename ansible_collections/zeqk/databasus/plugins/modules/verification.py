#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2026, zeqk (@zeqk)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: verification
short_description: Manage verification resources in Databasus.
description:
  - Allows managing verification resources using the Databasus API.
  - operationId references are included in generated operation constants.
  - Uses ``GET /verification/agents``.
  - Uses ``GET /verifications/{id}``.
  - Uses ``POST /verification/agents``.
  - Uses ``DELETE /verification/agents/{id}``.
options:
  state:
    description:
      - Desired state of the resource. Possible values; present, absent.
    type: str
    choices:
      - present
      - absent
    default: present
  api_url:
    description:
      - Base API URL.
    type: str
    required: true
  api_token:
    description:
      - Bearer authentication token.
    type: str
    required: true
  name:
    description:
      - Body field name.
    type: str
    required: true
author:
    - zeqk (@zeqk)
"""

EXAMPLES = r"""
- name: Create or update resource
  zeqk.databasus.verification:
    state: present
    api_url: https://api.example.com
    api_token: "{{ databasus_token }}"
    name: example-name

- name: Delete resource
  zeqk.databasus.verification:
    state: absent
    api_url: https://api.example.com
    api_token: "{{ databasus_token }}"
    name: example-name
"""

RETURN = r"""
resource:
    description: Resource object as returned by the API.
    type: dict
    returned: always
    contains:
        agent_id:
            description:
              - "Field agentId."
            type: str
            returned: success
        attempt_count:
            description:
              - "Field attemptCount."
            type: int
            returned: success
        backup_id:
            description:
              - "Field backupId."
            type: str
            returned: success
        created_at:
            description:
              - "Field createdAt."
            type: str
            returned: success
        database_id:
            description:
              - "Field databaseId."
            type: str
            returned: success
        db_size_bytes_after_restore:
            description:
              - "Field dbSizeBytesAfterRestore."
            type: int
            returned: success
        fail_message:
            description:
              - "Field failMessage."
            type: str
            returned: success
        finished_at:
            description:
              - "Field finishedAt."
            type: str
            returned: success
        id:
            description:
              - "Field id."
            type: str
            returned: success
        pg_restore_exit_code:
            description:
              - "Field pgRestoreExitCode."
            type: int
            returned: success
        restore_duration_ms:
            description:
              - "Field restoreDurationMs."
            type: int
            returned: success
        schema_count:
            description:
              - "Field schemaCount."
            type: int
            returned: success
        started_at:
            description:
              - "Field startedAt."
            type: str
            returned: success
        status:
            description:
              - "Field status."
            type: str
            returned: success
        table_count:
            description:
              - "Field tableCount."
            type: int
            returned: success
        table_stats:
            description:
              - "Field tableStats."
            type: list
            elements: dict
            returned: success
            contains:
                id:
                    description:
                      - "Field id."
                    type: str
                    returned: success
                name:
                    description:
                      - "Field name."
                    type: str
                    returned: success
                row_count:
                    description:
                      - "Field rowCount."
                    type: int
                    returned: success
                schema_name:
                    description:
                      - "Field schemaName."
                    type: str
                    returned: success
        trigger:
            description:
              - "Field trigger."
            type: str
            returned: success
        verify_duration_ms:
            description:
              - "Field verifyDurationMs."
            type: int
            returned: success
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
import shlex
from typing import Any, Dict, List, Optional, Tuple
from urllib import error, parse

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import open_url


CREATE_METHOD = 'POST'
CREATE_PATH = '/verification/agents'
CREATE_PATH_PARAMS = []
CREATE_QUERY_PARAMS = []
LIST_METHOD = 'GET'
LIST_PATH = '/verification/agents'
LIST_PATH_PARAMS = []
LIST_QUERY_PARAMS = []
GET_METHOD = 'GET'
GET_PATH = '/verifications/{id}'
GET_PATH_PARAMS = ['id']
GET_QUERY_PARAMS = []
UPDATE_METHOD = None
UPDATE_PATH = None
UPDATE_PATH_PARAMS = []
UPDATE_QUERY_PARAMS = []
DELETE_METHOD = 'DELETE'
DELETE_PATH = '/verification/agents/{id}'
DELETE_PATH_PARAMS = ['id']
DELETE_QUERY_PARAMS = []
BODY_SCHEMA = {
    'name': {'api': 'name', 'type': 'str'},
}
READ_ONLY = False
API_NAME_MAP = {
    'api_url': 'api_url',
    'api_token': 'api_token',
    'state': 'state',
    'name': 'name',
    'id': 'id',
}
REQUIRED_DELETE_PATH_PARAMS = ['id']
REQUIRED_GET_PATH_PARAMS = ['id']
REQUIRED_CREATE_PATH_PARAMS = []
REQUIRED_LIST_QUERY_PARAMS = []
NAME_ADDRESSABLE = True
NAME_FIELD = 'name'
NAME_API = 'name'
ID_FIELD = 'id'
ID_API = 'id'
MATCH_FIELDS = []
CREATE_IS_UPSERT = False


def _build_url(api_url: str, path_template: str, path_params: Dict[str, Any], query_params: Optional[Dict[str, Any]] = None) -> str:
    encoded = {k: parse.quote(str(v), safe='') for k, v in path_params.items()}
    path = path_template.format(**encoded)
    url = api_url.rstrip('/') + path
    clean_query = {k: v for k, v in (query_params or {}).items() if v is not None}
    if clean_query:
        url += '?' + parse.urlencode(clean_query, doseq=True)
    return url


def _decode_body(raw: str) -> Any:
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {'raw': raw}


def _build_curl(method: str, url: str, headers: Dict[str, Any], data: Optional[bytes]) -> str:
    parts = ['curl', '-sS', '-X', method.upper()]
    for key, value in headers.items():
        header_value = str(value)
        if key.lower() == 'authorization':
            header_value = 'Bearer <REDACTED>'
        parts += ['-H', shlex.quote(f'{key}: {header_value}')]
    if data is not None:
        parts += ['--data', shlex.quote(data.decode('utf-8', errors='replace'))]
    parts.append(shlex.quote(url))
    return ' '.join(parts)


def _request_json(
    module: AnsibleModule,
    method: str,
    url: str,
    token: str,
    payload: Optional[Dict[str, Any]] = None,
    expected_statuses: Optional[List[int]] = None,
    allow_statuses: Optional[List[int]] = None,
) -> Tuple[int, Any]:
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    data = None
    response_headers: Dict[str, Any] = {}
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
            response_headers = dict(getattr(response, 'headers', {}) or {})
            raw = response.read().decode('utf-8')
    except error.HTTPError as exc:
        status = int(exc.code)
        raw = exc.read().decode('utf-8', errors='replace')
        decoded = _decode_body(raw)
        reason = str(getattr(exc, 'reason', '') or '')
        response_headers = dict(getattr(exc, 'headers', {}) or {})
        if allow_statuses and status in allow_statuses:
            return status, decoded
        equivalent_curl = _build_curl(method, url, headers, data)
        module.fail_json(
            msg=f'HTTP {status} on {method} {url}. Reason: {reason}. Response body: {raw}. Equivalent curl: {equivalent_curl}',
            http_status=status,
            method=method,
            url=url,
            reason=reason,
            response_headers=response_headers,
            response_body=raw,
            response_json=decoded,
            equivalent_curl=equivalent_curl,
        )
    except error.URLError as exc:
        reason = str(getattr(exc, 'reason', exc))
        module.fail_json(
            msg=f'Connection error on {method} {url}: {reason}',
            method=method,
            url=url,
            reason=reason,
        )

    if expected_statuses and status not in expected_statuses:
        decoded = _decode_body(raw)
        equivalent_curl = _build_curl(method, url, headers, data)
        module.fail_json(
            msg=f'Unexpected HTTP {status} on {method} {url}. Response body: {raw}. Equivalent curl: {equivalent_curl}',
            http_status=status,
            expected_statuses=expected_statuses,
            method=method,
            url=url,
            response_headers=response_headers,
            response_body=raw,
            response_json=decoded,
            equivalent_curl=equivalent_curl,
        )

    return status, _decode_body(raw)


def _collect_params(module_params: Dict[str, Any], names: List[str]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for name in names:
        value = module_params.get(name)
        if value is not None:
            out[API_NAME_MAP.get(name, name)] = value
    return out


def _build_payload(values: Dict[str, Any], schema: Dict[str, Any]) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    for field_name, field_info in schema.items():
        val = values.get(field_name)
        if val is None:
            continue
        api_name = field_info['api']
        nested = field_info.get('nested')
        ftype = field_info.get('type', 'str')
        if nested and ftype == 'dict' and isinstance(val, dict):
            inner = _build_payload(val, nested)
            if inner:
                payload[api_name] = inner
        elif nested and ftype == 'list' and isinstance(val, list):
            payload[api_name] = [
                _build_payload(item, nested) for item in val if isinstance(item, dict)
            ]
        else:
            payload[api_name] = val
    return payload


def _desired_payload(module_params: Dict[str, Any]) -> Dict[str, Any]:
    return _build_payload(module_params, BODY_SCHEMA)


def _needs_update(current: Any, desired: Dict[str, Any]) -> bool:
    if not desired:
        return False
    if not isinstance(current, dict):
        return True
    for key, value in desired.items():
        if current.get(key) != value:
            return True
    return False


def _extract_items(listing: Any) -> List[Any]:
    if isinstance(listing, list):
        return listing
    if isinstance(listing, dict):
        for value in listing.values():
            if isinstance(value, list):
                return value
    return []


def _find_by_name(
    listing: Any,
    name_api: str,
    desired_name: str,
    match_fields: List[Tuple[str, Any]],
) -> Optional[Dict[str, Any]]:
    if not name_api or desired_name is None:
        return None
    for item in _extract_items(listing):
        if not isinstance(item, dict) or item.get(name_api) != desired_name:
            continue
        matches_scope = True
        for field_api_name, desired_value in match_fields:
            if desired_value is None:
                continue
            if item.get(field_api_name) != desired_value:
                matches_scope = False
                break
        if matches_scope:
            return item
    return None


def _has_required(module_params: Dict[str, Any], names: List[str]) -> bool:
    return all(module_params.get(name) is not None for name in names)


def _ensure_required(module: AnsibleModule, module_params: Dict[str, Any], names: List[str], context: str) -> None:
    missing = [name for name in names if module_params.get(name) is None]
    if missing:
        module.fail_json(msg=f'Missing required parameters for {context}: {", ".join(missing)}')


def run_module() -> None:
    module_args = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        api_url=dict(type='str', required=True),
        api_token=dict(type='str', required=True, no_log=True),
        name=dict(type='str', required=True),
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=not READ_ONLY)
    params = module.params

    api_url = params['api_url']
    api_token = params['api_token']
    state = params.get('state', 'present')

    result: Dict[str, Any] = dict(changed=False, resource={}, msg='No changes')

    if READ_ONLY:
        if GET_PATH and _has_required(params, GET_PATH_PARAMS):
            get_url = _build_url(api_url, GET_PATH, _collect_params(params, GET_PATH_PARAMS), _collect_params(params, GET_QUERY_PARAMS))
            current = _request_json(module, GET_METHOD, get_url, api_token, expected_statuses=[200])[1]
            result['resource'] = current if isinstance(current, dict) else {'value': current}
            result['msg'] = 'Single-resource query completed'
            module.exit_json(**result)

        if LIST_PATH:
            list_url = _build_url(api_url, LIST_PATH, _collect_params(params, LIST_PATH_PARAMS), _collect_params(params, LIST_QUERY_PARAMS))
            listing = _request_json(module, LIST_METHOD, list_url, api_token, expected_statuses=[200])[1]
            result['resource'] = listing if isinstance(listing, dict) else {'items': listing}
            result['msg'] = 'List query completed'
            module.exit_json(**result)

        result['msg'] = 'No usable GET endpoint for this module'
        module.fail_json(**result)

    exists = False
    current: Any = {}

    if NAME_ADDRESSABLE:
        if not LIST_PATH:
            module.fail_json(msg='Name-based idempotency requires a list endpoint')
        _ensure_required(module, params, [NAME_FIELD], 'name-based lookup')
        _ensure_required(module, params, REQUIRED_LIST_QUERY_PARAMS, 'name-based lookup')

        list_url = _build_url(api_url, LIST_PATH, _collect_params(params, LIST_PATH_PARAMS), _collect_params(params, LIST_QUERY_PARAMS))
        listing = _request_json(module, LIST_METHOD, list_url, api_token, expected_statuses=[200])[1]
        scoped_match_fields = [(api_name, params.get(field_name)) for field_name, api_name in MATCH_FIELDS]
        matched = _find_by_name(listing, NAME_API, params.get(NAME_FIELD), scoped_match_fields)
        if matched is not None:
            exists = True
            current = matched
            if ID_FIELD and ID_API and matched.get(ID_API) is not None:
                params[ID_FIELD] = matched.get(ID_API)

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

        if not exists:
            result['msg'] = 'Resource is already absent'
            module.exit_json(**result)

        _ensure_required(module, params, REQUIRED_DELETE_PATH_PARAMS or DELETE_PATH_PARAMS, 'delete')

        if module.check_mode:
            result['changed'] = True
            result['msg'] = 'Delete planned (check_mode)'
            module.exit_json(**result)

        delete_url = _build_url(api_url, DELETE_PATH, _collect_params(params, DELETE_PATH_PARAMS), _collect_params(params, DELETE_QUERY_PARAMS))
        _request_json(module, DELETE_METHOD, delete_url, api_token, expected_statuses=[200, 202, 204])
        result['changed'] = True
        result['resource'] = {}
        result['msg'] = 'Resource deleted'
        module.exit_json(**result)

    if exists:
        if UPDATE_PATH:
            if not _needs_update(current, desired):
                result['resource'] = current if isinstance(current, dict) else {'value': current}
                result['msg'] = 'Resource already in desired state'
                module.exit_json(**result)

            if module.check_mode:
                result['changed'] = True
                result['resource'] = current if isinstance(current, dict) else {'value': current}
                result['msg'] = 'Update planned (check_mode)'
                module.exit_json(**result)

            _ensure_required(module, params, UPDATE_PATH_PARAMS, 'update')
            update_url = _build_url(api_url, UPDATE_PATH, _collect_params(params, UPDATE_PATH_PARAMS), _collect_params(params, UPDATE_QUERY_PARAMS))
            updated = _request_json(module, UPDATE_METHOD, update_url, api_token, payload=desired, expected_statuses=[200, 201])[1]
            result['changed'] = True
            result['resource'] = updated if isinstance(updated, dict) else {'value': updated}
            result['msg'] = 'Resource updated'
            module.exit_json(**result)

        if CREATE_IS_UPSERT:
            if not _needs_update(current, desired):
                result['resource'] = current if isinstance(current, dict) else {'value': current}
                result['msg'] = 'Resource already in desired state'
                module.exit_json(**result)

            if module.check_mode:
                result['changed'] = True
                result['resource'] = current if isinstance(current, dict) else {'value': current}
                result['msg'] = 'Update planned (check_mode)'
                module.exit_json(**result)

            _ensure_required(module, params, REQUIRED_CREATE_PATH_PARAMS or CREATE_PATH_PARAMS, 'create')
            create_url = _build_url(api_url, CREATE_PATH, _collect_params(params, CREATE_PATH_PARAMS), _collect_params(params, CREATE_QUERY_PARAMS))
            updated = _request_json(module, CREATE_METHOD, create_url, api_token, payload=desired, expected_statuses=[200, 201, 202])[1]
            result['changed'] = True
            result['resource'] = updated if isinstance(updated, dict) else {'value': updated}
            result['msg'] = 'Resource updated'
            module.exit_json(**result)

        result['resource'] = current if isinstance(current, dict) else {'value': current}
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
    result['resource'] = created if isinstance(created, dict) else {'value': created}
    result['msg'] = 'Resource created'
    module.exit_json(**result)


def main() -> None:
    run_module()


if __name__ == '__main__':
    main()
