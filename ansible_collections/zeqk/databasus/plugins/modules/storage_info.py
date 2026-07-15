#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2026, zeqk (@zeqk)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: storage_info
short_description: Gather information about storage resources in Databasus.
description:
  - Retrieves a storage resource by name using Databasus list endpoints.
  - This module is read-only and never changes remote state.
options:
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
  workspace_id:
    description:
      - Workspace ID
    type: str
author:
    - zeqk (@zeqk)
"""

EXAMPLES = r"""
- name: Lookup storage by name
  zeqk.databasus.storage_info:
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
found:
    description: Whether a resource matching the requested name (and scope) was found.
    type: bool
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
import shlex
from typing import Any, Dict, List, Optional, Tuple
from urllib import error, parse

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import open_url


LIST_METHOD = 'GET'
LIST_PATH = '/storages'
LIST_PATH_PARAMS = []
LIST_QUERY_PARAMS = ['workspace_id']
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
REQUIRED_LIST_QUERY_PARAMS = ['workspace_id']
NAME_FIELD = 'name'
NAME_API = 'name'
MATCH_FIELDS = [('workspace_id', 'workspaceId')]


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
    expected_statuses: Optional[List[int]] = None,
) -> Tuple[int, Any]:
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    data = None
    response_headers: Dict[str, Any] = {}

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


def _ensure_required(module: AnsibleModule, module_params: Dict[str, Any], names: List[str], context: str) -> None:
    missing = [name for name in names if module_params.get(name) is None]
    if missing:
        module.fail_json(msg=f'Missing required parameters for {context}: {", ".join(missing)}')


def run_module() -> None:
    module_args = dict(
        api_url=dict(type='str', required=True),
        api_token=dict(type='str', required=True, no_log=True),
        name=dict(type='str', required=True),
        workspace_id=dict(type='str'),
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    params = module.params

    _ensure_required(module, params, [NAME_FIELD], 'name-based lookup')
    _ensure_required(module, params, REQUIRED_LIST_QUERY_PARAMS, 'name-based lookup')

    api_url = params['api_url']
    api_token = params['api_token']

    list_url = _build_url(api_url, LIST_PATH, _collect_params(params, LIST_PATH_PARAMS), _collect_params(params, LIST_QUERY_PARAMS))
    listing = _request_json(module, LIST_METHOD, list_url, api_token, expected_statuses=[200])[1]

    scoped_match_fields = [(api_name, params.get(field_name)) for field_name, api_name in MATCH_FIELDS]
    matched = _find_by_name(listing, NAME_API, params.get(NAME_FIELD), scoped_match_fields)

    result: Dict[str, Any] = dict(changed=False, found=False, resource={}, msg='Resource not found')
    if matched is not None:
        result['found'] = True
        result['resource'] = matched
        result['msg'] = 'Resource found'

    module.exit_json(**result)


def main() -> None:
    run_module()


if __name__ == '__main__':
    main()
