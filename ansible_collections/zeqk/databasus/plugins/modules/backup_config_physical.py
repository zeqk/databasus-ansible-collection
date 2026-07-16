#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2026, zeqk (@zeqk)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: backup_config_physical
short_description: Manage backup_config_physical resources in Databasus.
description:
  - Allows managing backup_config_physical resources using the Databasus API.
  - Uses ``GET /backup-configs/physical/database/{id}``.
  - Uses ``POST /backup-configs/physical/save``.
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
  chains_retention:
    description:
      - Body field chainsRetention.
    type: dict
    suboptions:
      count:
        description:
          - Body field count.
        type: int
  database_id:
    description:
      - Body field databaseId.
    type: str
  encryption:
    description:
      - Body field encryption. Possible values; NONE, ENCRYPTED.
    type: str
    choices:
      - NONE
      - ENCRYPTED
  full_backup_interval:
    description:
      - Body field fullBackupInterval.
    type: dict
    suboptions:
      cron_expression:
        description:
          - Body field cronExpression.
        type: str
      day_of_month:
        description:
          - Body field dayOfMonth.
        type: int
      time_of_day:
        description:
          - Body field timeOfDay.
        type: str
      type:
        description:
          - Body field type. Possible values; HOURLY, DAILY, WEEKLY, MONTHLY, CRON.
        type: str
        choices:
          - HOURLY
          - DAILY
          - WEEKLY
          - MONTHLY
          - CRON
      weekday:
        description:
          - Body field weekday.
        type: int
  full_backups_retention:
    description:
      - Body field fullBackupsRetention.
    type: dict
    suboptions:
      count:
        description:
          - Body field count.
        type: int
      gfs_days:
        description:
          - Body field gfsDays.
        type: int
      gfs_hours:
        description:
          - Body field gfsHours.
        type: int
      gfs_months:
        description:
          - Body field gfsMonths.
        type: int
      gfs_weeks:
        description:
          - Body field gfsWeeks.
        type: int
      gfs_years:
        description:
          - Body field gfsYears.
        type: int
      policy:
        description:
          - Body field policy. Possible values; LAST_N, GFS.
        type: str
        choices:
          - LAST_N
          - GFS
  id:
    description:
      - Database ID
    type: str
  incremental_backup_interval:
    description:
      - Body field incrementalBackupInterval.
    type: dict
    suboptions:
      cron_expression:
        description:
          - Body field cronExpression.
        type: str
      day_of_month:
        description:
          - Body field dayOfMonth.
        type: int
      time_of_day:
        description:
          - Body field timeOfDay.
        type: str
      type:
        description:
          - Body field type. Possible values; HOURLY, DAILY, WEEKLY, MONTHLY, CRON.
        type: str
        choices:
          - HOURLY
          - DAILY
          - WEEKLY
          - MONTHLY
          - CRON
      weekday:
        description:
          - Body field weekday.
        type: int
  is_backups_enabled:
    description:
      - Body field isBackupsEnabled.
    type: bool
  retention:
    description:
      - Body field retention. Possible values; CHAINS, FULL_BACKUPS, CHAINS_AND_FULL_BACKUPS.
    type: str
    choices:
      - CHAINS
      - FULL_BACKUPS
      - CHAINS_AND_FULL_BACKUPS
  send_notifications_on:
    description:
      - Body field sendNotificationsOn. Possible values; BACKUP_SUCCESS, BACKUP_FAILED, CHAIN_BROKEN, WAL_GAP.
    type: list
    elements: str
    choices:
      - BACKUP_SUCCESS
      - BACKUP_FAILED
      - CHAIN_BROKEN
      - WAL_GAP
  storage_id:
    description:
      - Body field storageId.
    type: str
  wal_lag_threshold_bytes:
    description:
      - Body field walLagThresholdBytes.
    type: int
author:
    - zeqk (@zeqk)
"""

EXAMPLES = r"""
- name: Create or update resource
  zeqk.databasus.backup_config_physical:
    state: present
    api_url: https://api.example.com
    api_token: "{{ databasus_token }}"
    chains_retention: null
"""

RETURN = r"""
resource:
    description: Resource object as returned by the API.
    type: dict
    returned: always
    contains:
        chains_retention:
            description:
              - "Field chainsRetention."
            type: dict
            returned: success
            contains:
                count:
                    description:
                      - "Field count."
                    type: int
                    returned: success
        database_id:
            description:
              - "Field databaseId."
            type: str
            returned: success
        encryption:
            description:
              - "Field encryption."
            type: str
            returned: success
        full_backup_interval:
            description:
              - "Field fullBackupInterval."
            type: dict
            returned: success
            contains:
                cron_expression:
                    description:
                      - "Field cronExpression."
                    type: str
                    returned: success
                day_of_month:
                    description:
                      - "Field dayOfMonth."
                    type: int
                    returned: success
                time_of_day:
                    description:
                      - "Field timeOfDay."
                    type: str
                    returned: success
                type:
                    description:
                      - "Field type."
                    type: str
                    returned: success
                weekday:
                    description:
                      - "Field weekday."
                    type: int
                    returned: success
        full_backups_retention:
            description:
              - "Field fullBackupsRetention."
            type: dict
            returned: success
            contains:
                count:
                    description:
                      - "Field count."
                    type: int
                    returned: success
                gfs_days:
                    description:
                      - "Field gfsDays."
                    type: int
                    returned: success
                gfs_hours:
                    description:
                      - "Field gfsHours."
                    type: int
                    returned: success
                gfs_months:
                    description:
                      - "Field gfsMonths."
                    type: int
                    returned: success
                gfs_weeks:
                    description:
                      - "Field gfsWeeks."
                    type: int
                    returned: success
                gfs_years:
                    description:
                      - "Field gfsYears."
                    type: int
                    returned: success
                policy:
                    description:
                      - "Field policy."
                    type: str
                    returned: success
        incremental_backup_interval:
            description:
              - "Field incrementalBackupInterval."
            type: dict
            returned: success
            contains:
                cron_expression:
                    description:
                      - "Field cronExpression."
                    type: str
                    returned: success
                day_of_month:
                    description:
                      - "Field dayOfMonth."
                    type: int
                    returned: success
                time_of_day:
                    description:
                      - "Field timeOfDay."
                    type: str
                    returned: success
                type:
                    description:
                      - "Field type."
                    type: str
                    returned: success
                weekday:
                    description:
                      - "Field weekday."
                    type: int
                    returned: success
        is_backups_enabled:
            description:
              - "Field isBackupsEnabled."
            type: bool
            returned: success
        retention:
            description:
              - "Field retention."
            type: str
            returned: success
        send_notifications_on:
            description:
              - "Field sendNotificationsOn."
            type: list
            elements: str
            returned: success
        storage:
            description:
              - "Field storage."
            type: dict
            returned: success
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
        storage_id:
            description:
              - "Field storageId."
            type: str
            returned: success
        wal_lag_threshold_bytes:
            description:
              - "Field walLagThresholdBytes."
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
CREATE_PATH = '/backup-configs/physical/save'
CREATE_PATH_PARAMS = []
CREATE_QUERY_PARAMS = []
LIST_METHOD = None
LIST_PATH = None
LIST_PATH_PARAMS = []
LIST_QUERY_PARAMS = []
GET_METHOD = 'GET'
GET_PATH = '/backup-configs/physical/database/{id}'
GET_PATH_PARAMS = ['id']
GET_QUERY_PARAMS = []
UPDATE_METHOD = None
UPDATE_PATH = None
UPDATE_PATH_PARAMS = []
UPDATE_QUERY_PARAMS = []
DELETE_METHOD = None
DELETE_PATH = None
DELETE_PATH_PARAMS = []
DELETE_QUERY_PARAMS = []
BODY_SCHEMA = {
    'chains_retention': {
        'api': 'chainsRetention',
        'type': 'dict',
        'nested': {
            'count': {'api': 'count', 'type': 'int'},
        },
    },
    'database_id': {'api': 'databaseId', 'type': 'str'},
    'encryption': {'api': 'encryption', 'type': 'str'},
    'full_backup_interval': {
        'api': 'fullBackupInterval',
        'type': 'dict',
        'nested': {
            'cron_expression': {'api': 'cronExpression', 'type': 'str'},
            'day_of_month': {'api': 'dayOfMonth', 'type': 'int'},
            'time_of_day': {'api': 'timeOfDay', 'type': 'str'},
            'type': {'api': 'type', 'type': 'str'},
            'weekday': {'api': 'weekday', 'type': 'int'},
        },
    },
    'full_backups_retention': {
        'api': 'fullBackupsRetention',
        'type': 'dict',
        'nested': {
            'count': {'api': 'count', 'type': 'int'},
            'gfs_days': {'api': 'gfsDays', 'type': 'int'},
            'gfs_hours': {'api': 'gfsHours', 'type': 'int'},
            'gfs_months': {'api': 'gfsMonths', 'type': 'int'},
            'gfs_weeks': {'api': 'gfsWeeks', 'type': 'int'},
            'gfs_years': {'api': 'gfsYears', 'type': 'int'},
            'policy': {'api': 'policy', 'type': 'str'},
        },
    },
    'incremental_backup_interval': {
        'api': 'incrementalBackupInterval',
        'type': 'dict',
        'nested': {
            'cron_expression': {'api': 'cronExpression', 'type': 'str'},
            'day_of_month': {'api': 'dayOfMonth', 'type': 'int'},
            'time_of_day': {'api': 'timeOfDay', 'type': 'str'},
            'type': {'api': 'type', 'type': 'str'},
            'weekday': {'api': 'weekday', 'type': 'int'},
        },
    },
    'is_backups_enabled': {'api': 'isBackupsEnabled', 'type': 'bool'},
    'retention': {'api': 'retention', 'type': 'str'},
    'send_notifications_on': {'api': 'sendNotificationsOn', 'type': 'list'},
    'storage_id': {'api': 'storageId', 'type': 'str'},
    'wal_lag_threshold_bytes': {'api': 'walLagThresholdBytes', 'type': 'int'},
}
READ_ONLY = False
API_NAME_MAP = {
    'api_url': 'api_url',
    'api_token': 'api_token',
    'state': 'state',
    'id': 'id',
    'chains_retention': 'chainsRetention',
    'database_id': 'databaseId',
    'encryption': 'encryption',
    'full_backup_interval': 'fullBackupInterval',
    'full_backups_retention': 'fullBackupsRetention',
    'incremental_backup_interval': 'incrementalBackupInterval',
    'is_backups_enabled': 'isBackupsEnabled',
    'retention': 'retention',
    'send_notifications_on': 'sendNotificationsOn',
    'storage_id': 'storageId',
    'wal_lag_threshold_bytes': 'walLagThresholdBytes',
}
REQUIRED_DELETE_PATH_PARAMS = []
REQUIRED_GET_PATH_PARAMS = ['id']
REQUIRED_CREATE_PATH_PARAMS = []
REQUIRED_LIST_QUERY_PARAMS = []
NAME_ADDRESSABLE = False
NAME_FIELD = ''
NAME_API = ''
ID_FIELD = ''
ID_API = ''
MATCH_FIELDS = []
CREATE_IS_UPSERT = True
EXPAND_STORAGE_ID_TO_STORAGE = True


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


def _is_verbose_enabled(module: AnsibleModule) -> bool:
    return int(getattr(module, '_verbosity', 0) or 0) >= 3


def _verbose_http_log(module: AnsibleModule, message: str) -> None:
    if _is_verbose_enabled(module):
        module.warn(message)


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
    equivalent_curl = _build_curl(method, url, headers, data)
    _verbose_http_log(module, f'Databasus API request: {equivalent_curl}')

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
            _verbose_http_log(module, f'Databasus API response: HTTP {status} on {method.upper()} {url}')
    except error.HTTPError as exc:
        status = int(exc.code)
        raw = exc.read().decode('utf-8', errors='replace')
        decoded = _decode_body(raw)
        reason = str(getattr(exc, 'reason', '') or '')
        response_headers = dict(getattr(exc, 'headers', {}) or {})
        if allow_statuses and status in allow_statuses:
            _verbose_http_log(module, f'Databasus API response: HTTP {status} on {method.upper()} {url} (allowed status)')
            return status, decoded
        _verbose_http_log(module, f'Databasus API response: HTTP {status} on {method.upper()} {url}')
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
        _verbose_http_log(module, f'Databasus API connection error on {method.upper()} {url}: {reason}')
        module.fail_json(
            msg=f'Connection error on {method} {url}: {reason}',
            method=method,
            url=url,
            reason=reason,
        )

    if expected_statuses and status not in expected_statuses:
        decoded = _decode_body(raw)
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


def _expand_storage_id_to_storage(
    module: AnsibleModule,
    api_url: str,
    api_token: str,
    desired: Dict[str, Any],
) -> Dict[str, Any]:
    if not EXPAND_STORAGE_ID_TO_STORAGE:
        return desired
    storage_id = desired.get('storageId')
    if not storage_id:
        return desired
    storage_url = _build_url(api_url, '/storages/{id}', {'id': storage_id})
    storage_resource = _request_json(module, 'GET', storage_url, api_token, expected_statuses=[200])[1]
    if not isinstance(storage_resource, dict):
        module.fail_json(msg='Unexpected storage response while resolving storage_id to storage object')
    expanded = dict(desired)
    expanded.pop('storageId', None)
    expanded['storage'] = storage_resource
    return expanded


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
        chains_retention=dict(
            type='dict',
            options={
                'count': dict(type='int'),
            },
        ),
        database_id=dict(type='str'),
        encryption=dict(type='str', choices=['NONE', 'ENCRYPTED']),
        full_backup_interval=dict(
            type='dict',
            options={
                'cron_expression': dict(type='str'),
                'day_of_month': dict(type='int'),
                'time_of_day': dict(type='str'),
                'type': dict(type='str', choices=['HOURLY', 'DAILY', 'WEEKLY', 'MONTHLY', 'CRON']),
                'weekday': dict(type='int'),
            },
        ),
        full_backups_retention=dict(
            type='dict',
            options={
                'count': dict(type='int'),
                'gfs_days': dict(type='int'),
                'gfs_hours': dict(type='int'),
                'gfs_months': dict(type='int'),
                'gfs_weeks': dict(type='int'),
                'gfs_years': dict(type='int'),
                'policy': dict(type='str', choices=['LAST_N', 'GFS']),
            },
        ),
        id=dict(type='str'),
        incremental_backup_interval=dict(
            type='dict',
            options={
                'cron_expression': dict(type='str'),
                'day_of_month': dict(type='int'),
                'time_of_day': dict(type='str'),
                'type': dict(type='str', choices=['HOURLY', 'DAILY', 'WEEKLY', 'MONTHLY', 'CRON']),
                'weekday': dict(type='int'),
            },
        ),
        is_backups_enabled=dict(type='bool'),
        retention=dict(type='str', choices=['CHAINS', 'FULL_BACKUPS', 'CHAINS_AND_FULL_BACKUPS']),
        send_notifications_on=dict(type='list', elements='str', choices=['BACKUP_SUCCESS', 'BACKUP_FAILED', 'CHAIN_BROKEN', 'WAL_GAP']),
        storage_id=dict(type='str'),
        wal_lag_threshold_bytes=dict(type='int'),
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
    desired = _expand_storage_id_to_storage(module, api_url, api_token, desired)

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
