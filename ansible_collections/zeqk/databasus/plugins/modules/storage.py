#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2026, zeqk (@zeqk)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: storage
short_description: Manage storage resources in Databasus.
description:
  - Allows managing storage resources using the Databasus API.
  - operationId references are included in generated operation constants.
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
  azure_blob_storage:
    description:
      - Body field azureBlobStorage.
    type: dict
  ftp_storage:
    description:
      - Body field ftpStorage.
    type: dict
  google_drive_storage:
    description:
      - Body field googleDriveStorage.
    type: dict
  id:
    description:
      - Body field id.
    type: str
  last_save_error:
    description:
      - Body field lastSaveError.
    type: str
  local_storage:
    description:
      - Body field localStorage.
    type: dict
  name:
    description:
      - Body field name.
    type: str
  nas_storage:
    description:
      - Body field nasStorage.
    type: dict
  rclone_storage:
    description:
      - Body field rcloneStorage.
    type: dict
  s3_storage:
    description:
      - Body field s3Storage.
    type: dict
  sftp_storage:
    description:
      - Body field sftpStorage.
    type: dict
  type:
    description:
      - Body field type.
    type: str
  workspace_id:
    description:
      - Workspace ID
    type: str
author:
    - zeqk (@zeqk)
"""

EXAMPLES = r"""
- name: Create or update resource
  zeqk.databasus.storage:
    state: present
    api_url: https://api.example.com
    api_token: "{{ databasus_token }}"
    azure_blob_storage: null

- name: Delete resource
  zeqk.databasus.storage:
    state: absent
    api_url: https://api.example.com
    api_token: "{{ databasus_token }}"
"""

RETURN = r"""
resource:
    description: Resource object as returned by the API.
    type: dict
    returned: always
    contains:
        azure_blob_storage:
            description:
              - "Field azureBlobStorage."
            type: dict
            returned: success
            contains:
                account_key:
                    description:
                      - "Field accountKey."
                    type: str
                    returned: success
                account_name:
                    description:
                      - "Field accountName."
                    type: str
                    returned: success
                auth_method:
                    description:
                      - "Field authMethod."
                    type: str
                    returned: success
                connection_string:
                    description:
                      - "Field connectionString."
                    type: str
                    returned: success
                container_name:
                    description:
                      - "Field containerName."
                    type: str
                    returned: success
                endpoint:
                    description:
                      - "Field endpoint."
                    type: str
                    returned: success
                prefix:
                    description:
                      - "Field prefix."
                    type: str
                    returned: success
                storage_id:
                    description:
                      - "Field storageId."
                    type: str
                    returned: success
        ftp_storage:
            description:
              - "Field ftpStorage."
            type: dict
            returned: success
            contains:
                host:
                    description:
                      - "Field host."
                    type: str
                    returned: success
                password:
                    description:
                      - "Field password."
                    type: str
                    returned: success
                path:
                    description:
                      - "Field path."
                    type: str
                    returned: success
                port:
                    description:
                      - "Field port."
                    type: int
                    returned: success
                skip_tls_verify:
                    description:
                      - "Field skipTlsVerify."
                    type: bool
                    returned: success
                storage_id:
                    description:
                      - "Field storageId."
                    type: str
                    returned: success
                use_ssl:
                    description:
                      - "Field useSsl."
                    type: bool
                    returned: success
                username:
                    description:
                      - "Field username."
                    type: str
                    returned: success
        google_drive_storage:
            description:
              - "Field googleDriveStorage."
            type: dict
            returned: success
            contains:
                client_id:
                    description:
                      - "Field clientId."
                    type: str
                    returned: success
                client_secret:
                    description:
                      - "Field clientSecret."
                    type: str
                    returned: success
                storage_id:
                    description:
                      - "Field storageId."
                    type: str
                    returned: success
                token_json:
                    description:
                      - "Field tokenJson."
                    type: str
                    returned: success
        id:
            description:
              - "Field id."
            type: str
            returned: success
        last_save_error:
            description:
              - "Field lastSaveError."
            type: str
            returned: success
        local_storage:
            description:
              - "specific storage"
            type: dict
            returned: success
            contains:
                storage_id:
                    description:
                      - "Field storageId."
                    type: str
                    returned: success
        name:
            description:
              - "Field name."
            type: str
            returned: success
        nas_storage:
            description:
              - "Field nasStorage."
            type: dict
            returned: success
            contains:
                domain:
                    description:
                      - "Field domain."
                    type: str
                    returned: success
                host:
                    description:
                      - "Field host."
                    type: str
                    returned: success
                password:
                    description:
                      - "Field password."
                    type: str
                    returned: success
                path:
                    description:
                      - "Field path."
                    type: str
                    returned: success
                port:
                    description:
                      - "Field port."
                    type: int
                    returned: success
                share:
                    description:
                      - "Field share."
                    type: str
                    returned: success
                storage_id:
                    description:
                      - "Field storageId."
                    type: str
                    returned: success
                use_ssl:
                    description:
                      - "Field useSsl."
                    type: bool
                    returned: success
                username:
                    description:
                      - "Field username."
                    type: str
                    returned: success
        rclone_storage:
            description:
              - "Field rcloneStorage."
            type: dict
            returned: success
            contains:
                config_content:
                    description:
                      - "Field configContent."
                    type: str
                    returned: success
                remote_path:
                    description:
                      - "Field remotePath."
                    type: str
                    returned: success
                storage_id:
                    description:
                      - "Field storageId."
                    type: str
                    returned: success
        s3_storage:
            description:
              - "Field s3Storage."
            type: dict
            returned: success
            contains:
                s3_access_key:
                    description:
                      - "Field s3AccessKey."
                    type: str
                    returned: success
                s3_bucket:
                    description:
                      - "Field s3Bucket."
                    type: str
                    returned: success
                s3_endpoint:
                    description:
                      - "Field s3Endpoint."
                    type: str
                    returned: success
                s3_prefix:
                    description:
                      - "Field s3Prefix."
                    type: str
                    returned: success
                s3_region:
                    description:
                      - "Field s3Region."
                    type: str
                    returned: success
                s3_secret_key:
                    description:
                      - "Field s3SecretKey."
                    type: str
                    returned: success
                s3_storage_class:
                    description:
                      - "Field s3StorageClass."
                    type: str
                    returned: success
                s3_use_virtual_hosted_style:
                    description:
                      - "Field s3UseVirtualHostedStyle."
                    type: bool
                    returned: success
                skip_tlsverify:
                    description:
                      - "Field skipTLSVerify."
                    type: bool
                    returned: success
                storage_id:
                    description:
                      - "Field storageId."
                    type: str
                    returned: success
        sftp_storage:
            description:
              - "Field sftpStorage."
            type: dict
            returned: success
            contains:
                host:
                    description:
                      - "Field host."
                    type: str
                    returned: success
                password:
                    description:
                      - "Field password."
                    type: str
                    returned: success
                path:
                    description:
                      - "Field path."
                    type: str
                    returned: success
                port:
                    description:
                      - "Field port."
                    type: int
                    returned: success
                private_key:
                    description:
                      - "Field privateKey."
                    type: str
                    returned: success
                skip_host_key_verify:
                    description:
                      - "Field skipHostKeyVerify."
                    type: bool
                    returned: success
                storage_id:
                    description:
                      - "Field storageId."
                    type: str
                    returned: success
                username:
                    description:
                      - "Field username."
                    type: str
                    returned: success
        type:
            description:
              - "Field type."
            type: str
            returned: success
        workspace_id:
            description:
              - "Field workspaceId."
            type: str
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
CREATE_PATH = '/storages'
CREATE_PATH_PARAMS = []
CREATE_QUERY_PARAMS = []
LIST_METHOD = 'GET'
LIST_PATH = '/storages'
LIST_PATH_PARAMS = []
LIST_QUERY_PARAMS = ['workspace_id']
GET_METHOD = 'GET'
GET_PATH = '/storages/{id}'
GET_PATH_PARAMS = ['id']
GET_QUERY_PARAMS = []
UPDATE_METHOD = None
UPDATE_PATH = None
UPDATE_PATH_PARAMS = []
UPDATE_QUERY_PARAMS = []
DELETE_METHOD = 'DELETE'
DELETE_PATH = '/storages/{id}'
DELETE_PATH_PARAMS = ['id']
DELETE_QUERY_PARAMS = []
BODY_FIELDS = [
    'azure_blob_storage',
    'ftp_storage',
    'google_drive_storage',
    'id',
    'last_save_error',
    'local_storage',
    'name',
    'nas_storage',
    'rclone_storage',
    's3_storage',
    'sftp_storage',
    'type',
    'workspace_id',
]
BODY_FIELD_MAP = {
    'azure_blob_storage': 'azureBlobStorage',
    'ftp_storage': 'ftpStorage',
    'google_drive_storage': 'googleDriveStorage',
    'id': 'id',
    'last_save_error': 'lastSaveError',
    'local_storage': 'localStorage',
    'name': 'name',
    'nas_storage': 'nasStorage',
    'rclone_storage': 'rcloneStorage',
    's3_storage': 's3Storage',
    'sftp_storage': 'sftpStorage',
    'type': 'type',
    'workspace_id': 'workspaceId',
}
READ_ONLY = False
API_NAME_MAP = {
    'api_url': 'api_url',
    'api_token': 'api_token',
    'state': 'state',
    'workspace_id': 'workspace_id',
    'azure_blob_storage': 'azureBlobStorage',
    'ftp_storage': 'ftpStorage',
    'google_drive_storage': 'googleDriveStorage',
    'id': 'id',
    'last_save_error': 'lastSaveError',
    'local_storage': 'localStorage',
    'name': 'name',
    'nas_storage': 'nasStorage',
    'rclone_storage': 'rcloneStorage',
    's3_storage': 's3Storage',
    'sftp_storage': 'sftpStorage',
    'type': 'type',
}
REQUIRED_DELETE_PATH_PARAMS = ['id']
REQUIRED_GET_PATH_PARAMS = ['id']
REQUIRED_CREATE_PATH_PARAMS = []


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


def _desired_payload(module_params: Dict[str, Any]) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    for name in BODY_FIELDS:
        value = module_params.get(name)
        if value is not None:
            payload[BODY_FIELD_MAP.get(name, API_NAME_MAP.get(name, name))] = value
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
        azure_blob_storage=dict(type='dict'),
        ftp_storage=dict(type='dict'),
        google_drive_storage=dict(type='dict'),
        id=dict(type='str'),
        last_save_error=dict(type='str'),
        local_storage=dict(type='dict'),
        name=dict(type='str'),
        nas_storage=dict(type='dict'),
        rclone_storage=dict(type='dict'),
        s3_storage=dict(type='dict'),
        sftp_storage=dict(type='dict'),
        type=dict(type='str'),
        workspace_id=dict(type='str'),
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
