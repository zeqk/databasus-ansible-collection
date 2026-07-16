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
  - Uses ``GET /storages``.
  - Uses ``GET /storages/{id}``.
  - Uses ``POST /storages``.
  - Uses ``DELETE /storages/{id}``.
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
  azure_blob_storage:
    description:
      - Body field azureBlobStorage.
    type: dict
    suboptions:
      account_key:
        description:
          - Body field accountKey.
        type: str
      account_name:
        description:
          - Body field accountName.
        type: str
      auth_method:
        description:
          - Body field authMethod. Possible values; CONNECTION_STRING, ACCOUNT_KEY.
        type: str
        choices:
          - CONNECTION_STRING
          - ACCOUNT_KEY
      connection_string:
        description:
          - Body field connectionString.
        type: str
      container_name:
        description:
          - Body field containerName.
        type: str
      endpoint:
        description:
          - Body field endpoint.
        type: str
      prefix:
        description:
          - Body field prefix.
        type: str
      storage_id:
        description:
          - Body field storageId.
        type: str
  ftp_storage:
    description:
      - Body field ftpStorage.
    type: dict
    suboptions:
      host:
        description:
          - Body field host.
        type: str
      password:
        description:
          - Body field password.
        type: str
      path:
        description:
          - Body field path.
        type: str
      port:
        description:
          - Body field port.
        type: int
      skip_tls_verify:
        description:
          - Body field skipTlsVerify.
        type: bool
      storage_id:
        description:
          - Body field storageId.
        type: str
      use_ssl:
        description:
          - Body field useSsl.
        type: bool
      username:
        description:
          - Body field username.
        type: str
  google_drive_storage:
    description:
      - Body field googleDriveStorage.
    type: dict
    suboptions:
      client_id:
        description:
          - Body field clientId.
        type: str
      client_secret:
        description:
          - Body field clientSecret.
        type: str
      storage_id:
        description:
          - Body field storageId.
        type: str
      token_json:
        description:
          - Body field tokenJson.
        type: str
  last_save_error:
    description:
      - Body field lastSaveError.
    type: str
  local_storage:
    description:
      - specific storage
    type: dict
    suboptions:
      storage_id:
        description:
          - Body field storageId.
        type: str
  name:
    description:
      - Body field name.
    type: str
    required: true
  nas_storage:
    description:
      - Body field nasStorage.
    type: dict
    suboptions:
      domain:
        description:
          - Body field domain.
        type: str
      host:
        description:
          - Body field host.
        type: str
      password:
        description:
          - Body field password.
        type: str
      path:
        description:
          - Body field path.
        type: str
      port:
        description:
          - Body field port.
        type: int
      share:
        description:
          - Body field share.
        type: str
      storage_id:
        description:
          - Body field storageId.
        type: str
      use_ssl:
        description:
          - Body field useSsl.
        type: bool
      username:
        description:
          - Body field username.
        type: str
  rclone_storage:
    description:
      - Body field rcloneStorage.
    type: dict
    suboptions:
      config_content:
        description:
          - Body field configContent.
        type: str
      remote_path:
        description:
          - Body field remotePath.
        type: str
      storage_id:
        description:
          - Body field storageId.
        type: str
  s3_storage:
    description:
      - Body field s3Storage.
    type: dict
    suboptions:
      s3_access_key:
        description:
          - Body field s3AccessKey.
        type: str
      s3_bucket:
        description:
          - Body field s3Bucket.
        type: str
      s3_endpoint:
        description:
          - Body field s3Endpoint.
        type: str
      s3_prefix:
        description:
          - Body field s3Prefix.
        type: str
      s3_region:
        description:
          - Body field s3Region.
        type: str
      s3_secret_key:
        description:
          - Body field s3SecretKey.
        type: str
      s3_storage_class:
        description:
          - Body field s3StorageClass. Possible values; , STANDARD, STANDARD_IA, ONEZONE_IA, INTELLIGENT_TIERING, REDUCED_REDUNDANCY, GLACIER_IR.
        type: str
        choices:
          - ''
          - STANDARD
          - STANDARD_IA
          - ONEZONE_IA
          - INTELLIGENT_TIERING
          - REDUCED_REDUNDANCY
          - GLACIER_IR
      s3_use_virtual_hosted_style:
        description:
          - Body field s3UseVirtualHostedStyle.
        type: bool
      skip_tlsverify:
        description:
          - Body field skipTLSVerify.
        type: bool
      storage_id:
        description:
          - Body field storageId.
        type: str
  sftp_storage:
    description:
      - Body field sftpStorage.
    type: dict
    suboptions:
      host:
        description:
          - Body field host.
        type: str
      password:
        description:
          - Body field password.
        type: str
      path:
        description:
          - Body field path.
        type: str
      port:
        description:
          - Body field port.
        type: int
      private_key:
        description:
          - Body field privateKey.
        type: str
      skip_host_key_verify:
        description:
          - Body field skipHostKeyVerify.
        type: bool
      storage_id:
        description:
          - Body field storageId.
        type: str
      username:
        description:
          - Body field username.
        type: str
  type:
    description:
      - Body field type. Possible values; LOCAL, S3, GOOGLE_DRIVE, NAS, AZURE_BLOB, FTP, SFTP, RCLONE.
    type: str
    choices:
      - LOCAL
      - S3
      - GOOGLE_DRIVE
      - NAS
      - AZURE_BLOB
      - FTP
      - SFTP
      - RCLONE
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
    name: example-name
    azure_blob_storage: null

- name: Delete resource
  zeqk.databasus.storage:
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
BODY_SCHEMA = {
    'azure_blob_storage': {
        'api': 'azureBlobStorage',
        'type': 'dict',
        'nested': {
            'account_key': {'api': 'accountKey', 'type': 'str'},
            'account_name': {'api': 'accountName', 'type': 'str'},
            'auth_method': {'api': 'authMethod', 'type': 'str'},
            'connection_string': {'api': 'connectionString', 'type': 'str'},
            'container_name': {'api': 'containerName', 'type': 'str'},
            'endpoint': {'api': 'endpoint', 'type': 'str'},
            'prefix': {'api': 'prefix', 'type': 'str'},
            'storage_id': {'api': 'storageId', 'type': 'str'},
        },
    },
    'ftp_storage': {
        'api': 'ftpStorage',
        'type': 'dict',
        'nested': {
            'host': {'api': 'host', 'type': 'str'},
            'password': {'api': 'password', 'type': 'str'},
            'path': {'api': 'path', 'type': 'str'},
            'port': {'api': 'port', 'type': 'int'},
            'skip_tls_verify': {'api': 'skipTlsVerify', 'type': 'bool'},
            'storage_id': {'api': 'storageId', 'type': 'str'},
            'use_ssl': {'api': 'useSsl', 'type': 'bool'},
            'username': {'api': 'username', 'type': 'str'},
        },
    },
    'google_drive_storage': {
        'api': 'googleDriveStorage',
        'type': 'dict',
        'nested': {
            'client_id': {'api': 'clientId', 'type': 'str'},
            'client_secret': {'api': 'clientSecret', 'type': 'str'},
            'storage_id': {'api': 'storageId', 'type': 'str'},
            'token_json': {'api': 'tokenJson', 'type': 'str'},
        },
    },
    'id': {'api': 'id', 'type': 'str'},
    'last_save_error': {'api': 'lastSaveError', 'type': 'str'},
    'local_storage': {
        'api': 'localStorage',
        'type': 'dict',
        'nested': {
            'storage_id': {'api': 'storageId', 'type': 'str'},
        },
    },
    'name': {'api': 'name', 'type': 'str'},
    'nas_storage': {
        'api': 'nasStorage',
        'type': 'dict',
        'nested': {
            'domain': {'api': 'domain', 'type': 'str'},
            'host': {'api': 'host', 'type': 'str'},
            'password': {'api': 'password', 'type': 'str'},
            'path': {'api': 'path', 'type': 'str'},
            'port': {'api': 'port', 'type': 'int'},
            'share': {'api': 'share', 'type': 'str'},
            'storage_id': {'api': 'storageId', 'type': 'str'},
            'use_ssl': {'api': 'useSsl', 'type': 'bool'},
            'username': {'api': 'username', 'type': 'str'},
        },
    },
    'rclone_storage': {
        'api': 'rcloneStorage',
        'type': 'dict',
        'nested': {
            'config_content': {'api': 'configContent', 'type': 'str'},
            'remote_path': {'api': 'remotePath', 'type': 'str'},
            'storage_id': {'api': 'storageId', 'type': 'str'},
        },
    },
    's3_storage': {
        'api': 's3Storage',
        'type': 'dict',
        'nested': {
            's3_access_key': {'api': 's3AccessKey', 'type': 'str'},
            's3_bucket': {'api': 's3Bucket', 'type': 'str'},
            's3_endpoint': {'api': 's3Endpoint', 'type': 'str'},
            's3_prefix': {'api': 's3Prefix', 'type': 'str'},
            's3_region': {'api': 's3Region', 'type': 'str'},
            's3_secret_key': {'api': 's3SecretKey', 'type': 'str'},
            's3_storage_class': {'api': 's3StorageClass', 'type': 'str'},
            's3_use_virtual_hosted_style': {'api': 's3UseVirtualHostedStyle', 'type': 'bool'},
            'skip_tlsverify': {'api': 'skipTLSVerify', 'type': 'bool'},
            'storage_id': {'api': 'storageId', 'type': 'str'},
        },
    },
    'sftp_storage': {
        'api': 'sftpStorage',
        'type': 'dict',
        'nested': {
            'host': {'api': 'host', 'type': 'str'},
            'password': {'api': 'password', 'type': 'str'},
            'path': {'api': 'path', 'type': 'str'},
            'port': {'api': 'port', 'type': 'int'},
            'private_key': {'api': 'privateKey', 'type': 'str'},
            'skip_host_key_verify': {'api': 'skipHostKeyVerify', 'type': 'bool'},
            'storage_id': {'api': 'storageId', 'type': 'str'},
            'username': {'api': 'username', 'type': 'str'},
        },
    },
    'type': {'api': 'type', 'type': 'str'},
    'workspace_id': {'api': 'workspaceId', 'type': 'str'},
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
REQUIRED_LIST_QUERY_PARAMS = ['workspace_id']
NAME_ADDRESSABLE = True
NAME_FIELD = 'name'
NAME_API = 'name'
ID_FIELD = 'id'
ID_API = 'id'
MATCH_FIELDS = [('workspace_id', 'workspaceId')]
CREATE_IS_UPSERT = True


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
        azure_blob_storage=dict(
            type='dict',
            options={
                'account_key': dict(type='str', no_log=True),
                'account_name': dict(type='str'),
                'auth_method': dict(type='str', choices=['CONNECTION_STRING', 'ACCOUNT_KEY']),
                'connection_string': dict(type='str'),
                'container_name': dict(type='str'),
                'endpoint': dict(type='str'),
                'prefix': dict(type='str'),
                'storage_id': dict(type='str'),
            },
        ),
        ftp_storage=dict(
            type='dict',
            options={
                'host': dict(type='str'),
                'password': dict(type='str', no_log=True),
                'path': dict(type='str'),
                'port': dict(type='int'),
                'skip_tls_verify': dict(type='bool'),
                'storage_id': dict(type='str'),
                'use_ssl': dict(type='bool'),
                'username': dict(type='str'),
            },
        ),
        google_drive_storage=dict(
            type='dict',
            options={
                'client_id': dict(type='str'),
                'client_secret': dict(type='str', no_log=True),
                'storage_id': dict(type='str'),
                'token_json': dict(type='str', no_log=True),
            },
        ),
        last_save_error=dict(type='str'),
        local_storage=dict(
            type='dict',
            options={
                'storage_id': dict(type='str'),
            },
        ),
        name=dict(type='str', required=True),
        nas_storage=dict(
            type='dict',
            options={
                'domain': dict(type='str'),
                'host': dict(type='str'),
                'password': dict(type='str', no_log=True),
                'path': dict(type='str'),
                'port': dict(type='int'),
                'share': dict(type='str'),
                'storage_id': dict(type='str'),
                'use_ssl': dict(type='bool'),
                'username': dict(type='str'),
            },
        ),
        rclone_storage=dict(
            type='dict',
            options={
                'config_content': dict(type='str'),
                'remote_path': dict(type='str'),
                'storage_id': dict(type='str'),
            },
        ),
        s3_storage=dict(
            type='dict',
            options={
                's3_access_key': dict(type='str', no_log=True),
                's3_bucket': dict(type='str'),
                's3_endpoint': dict(type='str'),
                's3_prefix': dict(type='str'),
                's3_region': dict(type='str'),
                's3_secret_key': dict(type='str', no_log=True),
                's3_storage_class': dict(
                    type='str',
                    choices=['', 'STANDARD', 'STANDARD_IA', 'ONEZONE_IA', 'INTELLIGENT_TIERING', 'REDUCED_REDUNDANCY', 'GLACIER_IR'],
                ),
                's3_use_virtual_hosted_style': dict(type='bool'),
                'skip_tlsverify': dict(type='bool'),
                'storage_id': dict(type='str'),
            },
        ),
        sftp_storage=dict(
            type='dict',
            options={
                'host': dict(type='str'),
                'password': dict(type='str', no_log=True),
                'path': dict(type='str'),
                'port': dict(type='int'),
                'private_key': dict(type='str', no_log=True),
                'skip_host_key_verify': dict(type='bool', no_log=True),
                'storage_id': dict(type='str'),
                'username': dict(type='str'),
            },
        ),
        type=dict(type='str', choices=['LOCAL', 'S3', 'GOOGLE_DRIVE', 'NAS', 'AZURE_BLOB', 'FTP', 'SFTP', 'RCLONE']),
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
