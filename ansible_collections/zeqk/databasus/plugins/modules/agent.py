from __future__ import annotations

import json
from typing import Any, Dict, List, Optional, Tuple
from urllib import error, parse

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import open_url


DOCUMENTATION = r"""
---
module: agent
short_description: Manage agent resources in Databasus.
description:
  - Allows managing agent resources using the Databasus API.
options:
  state:
    description:
      - Desired state of the resource.
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
    no_log: true
  agent_id:
    description:
      - Agent UUID
    type: str
    required: true
  db_size_bytes_after_restore:
    description:
      - Body field dbSizeBytesAfterRestore.
    type: int
  fail_message:
    description:
      - Body field failMessage.
    type: str
  failure_kind:
    description:
      - Body field failureKind.
    type: str
  id:
    description:
      - Verification UUID
    type: str
    required: true
  pg_restore_exit_code:
    description:
      - Body field pgRestoreExitCode.
    type: int
  restore_duration_ms:
    description:
      - Body field restoreDurationMs.
    type: int
  schema_count:
    description:
      - Body field schemaCount.
    type: int
  status:
    description:
      - Body field status.
    type: dict
    required: true
  table_count:
    description:
      - Body field tableCount.
    type: int
  table_stats:
    description:
      - Body field tableStats.
    type: list
  verify_duration_ms:
    description:
      - Body field verifyDurationMs.
    type: int
author:
  - zeqk
"""

EXAMPLES = r"""
- name: Create or update resource
  zeqk.databasus.agent:
    state: present
    api_url: https://api.example.com
    api_token: "{{ databasus_token }}"
    db_size_bytes_after_restore: null
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


CREATE_METHOD = 'POST'
CREATE_PATH = '/agent/verifications/{agentId}/{id}/report'
CREATE_PATH_PARAMS = ['agent_id', 'id']
CREATE_QUERY_PARAMS = []
LIST_METHOD = 'GET'
LIST_PATH = '/agent/verifications/{agentId}/{id}/backup-stream'
LIST_PATH_PARAMS = ['agent_id', 'id']
LIST_QUERY_PARAMS = []
GET_METHOD = None
GET_PATH = None
GET_PATH_PARAMS = []
GET_QUERY_PARAMS = []
UPDATE_METHOD = None
UPDATE_PATH = None
UPDATE_PATH_PARAMS = []
UPDATE_QUERY_PARAMS = []
DELETE_METHOD = None
DELETE_PATH = None
DELETE_PATH_PARAMS = []
DELETE_QUERY_PARAMS = []
BODY_FIELDS = ['db_size_bytes_after_restore', 'fail_message', 'failure_kind', 'pg_restore_exit_code', 'restore_duration_ms', 'schema_count', 'status', 'table_count', 'table_stats', 'verify_duration_ms']
READ_ONLY = False
API_NAME_MAP = {'api_url': 'api_url', 'api_token': 'api_token', 'state': 'state', 'agent_id': 'agentId', 'id': 'id', 'db_size_bytes_after_restore': 'dbSizeBytesAfterRestore', 'fail_message': 'failMessage', 'failure_kind': 'failureKind', 'pg_restore_exit_code': 'pgRestoreExitCode', 'restore_duration_ms': 'restoreDurationMs', 'schema_count': 'schemaCount', 'status': 'status', 'table_count': 'tableCount', 'table_stats': 'tableStats', 'verify_duration_ms': 'verifyDurationMs'}
REQUIRED_DELETE_PATH_PARAMS = []
REQUIRED_GET_PATH_PARAMS = []
REQUIRED_CREATE_PATH_PARAMS = ['agent_id', 'id']


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
        module.fail_json(msg=f'HTTP {status} on {method} {url}: {raw}')
    except error.URLError as exc:
        module.fail_json(msg=f'Connection error on {method} {url}: {exc}')

    if expected_statuses and status not in expected_statuses:
        module.fail_json(msg=f'Unexpected HTTP {status} on {method} {url}: {raw}')

    return status, _decode_body(raw)


def _collect_params(module_params: Dict[str, Any], names: List[str]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for name in names:
        value = module_params.get(name)
        if value is not None:
            out[API_NAME_MAP.get(name, name)] = value
    return out


def _desired_payload(module_params: Dict[str, Any]) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
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
        module.fail_json(msg=f'Missing required parameters for {context}: {", ".join(missing)}')


def run_module() -> None:
    module_args = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        api_url=dict(type='str', required=True),
        api_token=dict(type='str', required=True, no_log=True),
        agent_id=dict(type='str', required=True),
        db_size_bytes_after_restore=dict(type='int'),
        fail_message=dict(type='str'),
        failure_kind=dict(type='str'),
        id=dict(type='str', required=True),
        pg_restore_exit_code=dict(type='int'),
        restore_duration_ms=dict(type='int'),
        schema_count=dict(type='int'),
        status=dict(type='dict', required=True),
        table_count=dict(type='int'),
        table_stats=dict(type='list'),
        verify_duration_ms=dict(type='int'),
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
            _, current = _request_json(module, GET_METHOD, get_url, api_token, expected_statuses=[200])
            result['resource'] = current if isinstance(current, dict) else {'value': current}
            result['msg'] = 'Single-resource query completed'
            module.exit_json(**result)

        if LIST_PATH:
            list_url = _build_url(api_url, LIST_PATH, _collect_params(params, LIST_PATH_PARAMS), _collect_params(params, LIST_QUERY_PARAMS))
            _, listing = _request_json(module, LIST_METHOD, list_url, api_token, expected_statuses=[200])
            result['resource'] = listing if isinstance(listing, dict) else {'items': listing}
            result['msg'] = 'List query completed'
            module.exit_json(**result)

        module.fail_json(msg='No usable GET endpoint for this module', **result)

    exists = False
    current: Any = {}

    if GET_PATH and _has_required(params, GET_PATH_PARAMS):
        get_url = _build_url(api_url, GET_PATH, _collect_params(params, GET_PATH_PARAMS), _collect_params(params, GET_QUERY_PARAMS))
        status, body = _request_json(module, GET_METHOD, get_url, api_token, expected_statuses=[200], allow_statuses=[404])
        if status == 200:
            exists = True
            current = body

    desired = _desired_payload(params)

    if state == 'absent':
        if not DELETE_PATH:
            module.fail_json(msg='Resource does not support delete operation', **result)
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
            _, updated = _request_json(module, UPDATE_METHOD, update_url, api_token, payload=desired, expected_statuses=[200, 201])
            result['changed'] = True
            result['resource'] = updated if isinstance(updated, dict) else {'value': updated}
            result['msg'] = 'Resource updated'
            module.exit_json(**result)

        result['resource'] = current if isinstance(current, dict) else {'value': current}
        result['msg'] = 'Resource exists; no update endpoint available'
        module.exit_json(**result)

    if not CREATE_PATH:
        module.fail_json(msg='Resource does not exist and there is no create endpoint', **result)

    _ensure_required(module, params, REQUIRED_CREATE_PATH_PARAMS or CREATE_PATH_PARAMS, 'create')

    if module.check_mode:
        result['changed'] = True
        result['msg'] = 'Create planned (check_mode)'
        module.exit_json(**result)

    create_url = _build_url(api_url, CREATE_PATH, _collect_params(params, CREATE_PATH_PARAMS), _collect_params(params, CREATE_QUERY_PARAMS))
    _, created = _request_json(module, CREATE_METHOD, create_url, api_token, payload=desired, expected_statuses=[200, 201, 202])
    result['changed'] = True
    result['resource'] = created if isinstance(created, dict) else {'value': created}
    result['msg'] = 'Resource created'
    module.exit_json(**result)


def main() -> None:
    run_module()


if __name__ == '__main__':
    main()
