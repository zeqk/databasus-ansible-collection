#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2026, zeqk (@zeqk)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: database_copy
short_description: Manage database_copy resources in Databasus.
description:
  - Allows managing database_copy resources using the Databasus API.
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
  id:
    description:
      - Database ID
    type: str
author:
    - zeqk (@zeqk)
"""

EXAMPLES = r"""
- name: Create or update resource
  zeqk.databasus.database_copy:
    state: present
    api_url: https://api.example.com
    api_token: "{{ databasus_token }}"
"""

RETURN = r"""
resource:
    description: Resource object as returned by the API.
    type: dict
    returned: always
    contains:
        health_status:
            description:
              - "Field healthStatus."
            type: str
            returned: success
        id:
            description:
              - "Field id."
            type: str
            returned: success
        last_backup_error_message:
            description:
              - "Field lastBackupErrorMessage."
            type: str
            returned: success
        last_backup_time:
            description:
              - "these fields are not reliable, but they are used for pretty UI"
            type: str
            returned: success
        mariadb:
            description:
              - "Field mariadb."
            type: dict
            returned: success
            contains:
                database:
                    description:
                      - "Field database."
                    type: str
                    returned: success
                database_id:
                    description:
                      - "Field databaseId."
                    type: str
                    returned: success
                exclude_tables:
                    description:
                      - "Field excludeTables."
                    type: list
                    elements: str
                    returned: success
                host:
                    description:
                      - "Field host."
                    type: str
                    returned: success
                id:
                    description:
                      - "Field id."
                    type: str
                    returned: success
                is_exclude_events:
                    description:
                      - "Field isExcludeEvents."
                    type: bool
                    returned: success
                is_https:
                    description:
                      - "Field isHttps."
                    type: bool
                    returned: success
                is_skip_galera_disable:
                    description:
                      - "Field isSkipGaleraDisable."
                    type: bool
                    returned: success
                is_use_extended_insert:
                    description:
                      - "Field isUseExtendedInsert."
                    type: bool
                    returned: success
                password:
                    description:
                      - "Field password."
                    type: str
                    returned: success
                port:
                    description:
                      - "Field port."
                    type: int
                    returned: success
                privileges:
                    description:
                      - "Field privileges."
                    type: str
                    returned: success
                username:
                    description:
                      - "Field username."
                    type: str
                    returned: success
                version:
                    description:
                      - "Field version."
                    type: str
                    returned: success
        mongodb:
            description:
              - "Field mongodb."
            type: dict
            returned: success
            contains:
                auth_database:
                    description:
                      - "Field authDatabase."
                    type: str
                    returned: success
                cpu_count:
                    description:
                      - "Field cpuCount."
                    type: int
                    returned: success
                database:
                    description:
                      - "Field database."
                    type: str
                    returned: success
                database_id:
                    description:
                      - "Field databaseId."
                    type: str
                    returned: success
                exclude_collections:
                    description:
                      - "Field excludeCollections."
                    type: list
                    elements: str
                    returned: success
                host:
                    description:
                      - "Field host."
                    type: str
                    returned: success
                id:
                    description:
                      - "Field id."
                    type: str
                    returned: success
                is_direct_connection:
                    description:
                      - "Field isDirectConnection."
                    type: bool
                    returned: success
                is_https:
                    description:
                      - "Field isHttps."
                    type: bool
                    returned: success
                is_srv:
                    description:
                      - "Field isSrv."
                    type: bool
                    returned: success
                password:
                    description:
                      - "Field password."
                    type: str
                    returned: success
                port:
                    description:
                      - "Field port."
                    type: int
                    returned: success
                username:
                    description:
                      - "Field username."
                    type: str
                    returned: success
                version:
                    description:
                      - "Field version."
                    type: str
                    returned: success
        mysql:
            description:
              - "Field mysql."
            type: dict
            returned: success
            contains:
                database:
                    description:
                      - "Field database."
                    type: str
                    returned: success
                database_id:
                    description:
                      - "Field databaseId."
                    type: str
                    returned: success
                exclude_tables:
                    description:
                      - "Field excludeTables."
                    type: list
                    elements: str
                    returned: success
                host:
                    description:
                      - "Field host."
                    type: str
                    returned: success
                id:
                    description:
                      - "Field id."
                    type: str
                    returned: success
                is_https:
                    description:
                      - "Field isHttps."
                    type: bool
                    returned: success
                is_use_extended_insert:
                    description:
                      - "Field isUseExtendedInsert."
                    type: bool
                    returned: success
                is_zstd_supported:
                    description:
                      - "Field isZstdSupported."
                    type: bool
                    returned: success
                password:
                    description:
                      - "Field password."
                    type: str
                    returned: success
                port:
                    description:
                      - "Field port."
                    type: int
                    returned: success
                privileges:
                    description:
                      - "Field privileges."
                    type: str
                    returned: success
                username:
                    description:
                      - "Field username."
                    type: str
                    returned: success
                version:
                    description:
                      - "Field version."
                    type: str
                    returned: success
        name:
            description:
              - "Field name."
            type: str
            returned: success
        notifiers:
            description:
              - "Field notifiers."
            type: list
            elements: dict
            returned: success
            contains:
                discord_notifier:
                    description:
                      - "Field discordNotifier."
                    type: dict
                    returned: success
                    contains:
                        channel_webhook_url:
                            description:
                              - "Field channelWebhookUrl."
                            type: str
                            returned: success
                        notifier_id:
                            description:
                              - "Field notifierId."
                            type: str
                            returned: success
                email_notifier:
                    description:
                      - "Field emailNotifier."
                    type: dict
                    returned: success
                    contains:
                        from:
                            description:
                              - "Field from."
                            type: str
                            returned: success
                        is_insecure_skip_verify:
                            description:
                              - "Field isInsecureSkipVerify."
                            type: bool
                            returned: success
                        notifier_id:
                            description:
                              - "Field notifierId."
                            type: str
                            returned: success
                        smtp_host:
                            description:
                              - "Field smtpHost."
                            type: str
                            returned: success
                        smtp_password:
                            description:
                              - "Field smtpPassword."
                            type: str
                            returned: success
                        smtp_port:
                            description:
                              - "Field smtpPort."
                            type: int
                            returned: success
                        smtp_user:
                            description:
                              - "Field smtpUser."
                            type: str
                            returned: success
                        target_email:
                            description:
                              - "Field targetEmail."
                            type: str
                            returned: success
                id:
                    description:
                      - "Field id."
                    type: str
                    returned: success
                last_send_error:
                    description:
                      - "Field lastSendError."
                    type: str
                    returned: success
                name:
                    description:
                      - "Field name."
                    type: str
                    returned: success
                notifier_type:
                    description:
                      - "Field notifierType."
                    type: str
                    returned: success
                slack_notifier:
                    description:
                      - "Field slackNotifier."
                    type: dict
                    returned: success
                    contains:
                        bot_token:
                            description:
                              - "Field botToken."
                            type: str
                            returned: success
                        notifier_id:
                            description:
                              - "Field notifierId."
                            type: str
                            returned: success
                        target_chat_id:
                            description:
                              - "Field targetChatId."
                            type: str
                            returned: success
                teams_notifier:
                    description:
                      - "Field teamsNotifier."
                    type: dict
                    returned: success
                    contains:
                        notifier_id:
                            description:
                              - "Field notifierId."
                            type: str
                            returned: success
                        power_automate_url:
                            description:
                              - "Field powerAutomateUrl."
                            type: str
                            returned: success
                telegram_notifier:
                    description:
                      - "specific notifier"
                    type: dict
                    returned: success
                    contains:
                        bot_token:
                            description:
                              - "Field botToken."
                            type: str
                            returned: success
                        is_proxy_enabled:
                            description:
                              - "Field isProxyEnabled."
                            type: bool
                            returned: success
                        notifier_id:
                            description:
                              - "Field notifierId."
                            type: str
                            returned: success
                        proxy_url:
                            description:
                              - "Field proxyUrl."
                            type: str
                            returned: success
                        target_chat_id:
                            description:
                              - "Field targetChatId."
                            type: str
                            returned: success
                        thread_id:
                            description:
                              - "Field threadId."
                            type: int
                            returned: success
                webhook_notifier:
                    description:
                      - "Field webhookNotifier."
                    type: dict
                    returned: success
                    contains:
                        body_template:
                            description:
                              - "Field bodyTemplate."
                            type: str
                            returned: success
                        headers:
                            description:
                              - "Field headers."
                            type: list
                            elements: dict
                            returned: success
                            contains:
                                key:
                                    description:
                                      - "Field key."
                                    type: str
                                    returned: success
                                value:
                                    description:
                                      - "Field value."
                                    type: str
                                    returned: success
                        notifier_id:
                            description:
                              - "Field notifierId."
                            type: str
                            returned: success
                        webhook_method:
                            description:
                              - "Field webhookMethod."
                            type: str
                            returned: success
                        webhook_url:
                            description:
                              - "Field webhookUrl."
                            type: str
                            returned: success
                workspace_id:
                    description:
                      - "Field workspaceId."
                    type: str
                    returned: success
        postgresql_logical:
            description:
              - "Field postgresqlLogical."
            type: dict
            returned: success
            contains:
                cpu_count:
                    description:
                      - "Field cpuCount."
                    type: int
                    returned: success
                database:
                    description:
                      - "Field database."
                    type: str
                    returned: success
                database_id:
                    description:
                      - "Field databaseId."
                    type: str
                    returned: success
                exclude_tables:
                    description:
                      - "Field excludeTables."
                    type: list
                    elements: str
                    returned: success
                host:
                    description:
                      - "Field host."
                    type: str
                    returned: success
                id:
                    description:
                      - "Field id."
                    type: str
                    returned: success
                include_schemas:
                    description:
                      - "backup settings"
                    type: list
                    elements: str
                    returned: success
                is_exclude_extensions:
                    description:
                      - "restore settings (not saved to DB)"
                    type: bool
                    returned: success
                is_restore_ownership:
                    description:
                      - "Field isRestoreOwnership."
                    type: bool
                    returned: success
                is_restore_privileges:
                    description:
                      - "Field isRestorePrivileges."
                    type: bool
                    returned: success
                is_skip_user_mappings:
                    description:
                      - "Field isSkipUserMappings."
                    type: bool
                    returned: success
                password:
                    description:
                      - "Field password."
                    type: str
                    returned: success
                port:
                    description:
                      - "Field port."
                    type: int
                    returned: success
                ssl_client_cert:
                    description:
                      - "Field sslClientCert."
                    type: str
                    returned: success
                ssl_client_key:
                    description:
                      - "Field sslClientKey."
                    type: str
                    returned: success
                ssl_mode:
                    description:
                      - "SSL / TLS connection settings"
                    type: dict
                    returned: success
                ssl_root_cert:
                    description:
                      - "Field sslRootCert."
                    type: str
                    returned: success
                username:
                    description:
                      - "Field username."
                    type: str
                    returned: success
                version:
                    description:
                      - "Field version."
                    type: str
                    returned: success
        postgresql_physical:
            description:
              - "Field postgresqlPhysical."
            type: dict
            returned: success
            contains:
                backup_type:
                    description:
                      - "Field backupType."
                    type: str
                    returned: success
                database_id:
                    description:
                      - "Field databaseId."
                    type: str
                    returned: success
                host:
                    description:
                      - "Field host."
                    type: str
                    returned: success
                id:
                    description:
                      - "Field id."
                    type: str
                    returned: success
                password:
                    description:
                      - "Field password."
                    type: str
                    returned: success
                port:
                    description:
                      - "Field port."
                    type: int
                    returned: success
                ssl_client_cert:
                    description:
                      - "Field sslClientCert."
                    type: str
                    returned: success
                ssl_client_key:
                    description:
                      - "Field sslClientKey."
                    type: str
                    returned: success
                ssl_mode:
                    description:
                      - "SSL / TLS connection settings"
                    type: dict
                    returned: success
                ssl_root_cert:
                    description:
                      - "Field sslRootCert."
                    type: str
                    returned: success
                system_identifier:
                    description:
                      - "Field systemIdentifier."
                    type: str
                    returned: success
                username:
                    description:
                      - "Field username."
                    type: str
                    returned: success
                version:
                    description:
                      - "Field version."
                    type: str
                    returned: success
                wal_segment_size_bytes:
                    description:
                      - "WalSegmentSizeBytes captures the source cluster's wal_segment_size at first connect."
                    type: int
                    returned: success
        type:
            description:
              - "Field type."
            type: str
            returned: success
        workspace_id:
            description:
              - "WorkspaceID can be null when a database is created via restore operation outside the context of any"
              - "workspace"
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
CREATE_PATH = '/databases/{id}/copy'
CREATE_PATH_PARAMS = ['id']
CREATE_QUERY_PARAMS = []
LIST_METHOD = None
LIST_PATH = None
LIST_PATH_PARAMS = []
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
BODY_FIELDS = []
BODY_FIELD_MAP = {}
READ_ONLY = False
API_NAME_MAP = {
    'api_url': 'api_url',
    'api_token': 'api_token',
    'state': 'state',
    'id': 'id',
}
REQUIRED_DELETE_PATH_PARAMS = []
REQUIRED_GET_PATH_PARAMS = []
REQUIRED_CREATE_PATH_PARAMS = ['id']


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
        id=dict(type='str'),
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
