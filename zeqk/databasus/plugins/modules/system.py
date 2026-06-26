from __future__ import annotations

import json
from typing import Any, Dict, List, Optional, Tuple
from urllib import error, parse, request

from ansible.module_utils.basic import AnsibleModule


DOCUMENTATION = r"""
---
module: system
short_description: Gestiona recursos system en Databasus.
description:
  - Permite gestionar recursos system usando la API de Databasus.
  - Este modulo es de solo lectura y no admite state=absent.
options:
  api_url:
    description:
      - URL base de la API.
    type: str
    required: true
  api_token:
    description:
      - Token de autenticacion Bearer.
    type: str
    required: true
    no_log: true
author:
  - zeqk
"""

EXAMPLES = r"""
- name: Consultar recurso
  zeqk.databasus.system:
    api_url: https://api.example.com
    api_token: "{{ databasus_token }}"
"""

RETURN = r"""
resource:
  description: Objeto del recurso tal como lo retorna la API.
  type: dict
  returned: always
changed:
  description: Indica si se realizo algun cambio.
  type: bool
  returned: always
msg:
  description: Mensaje descriptivo de la operacion.
  type: str
  returned: always
"""


CREATE_METHOD = None
CREATE_PATH = None
CREATE_PATH_PARAMS = []
CREATE_QUERY_PARAMS = []
LIST_METHOD = 'GET'
LIST_PATH = '/system/health'
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
READ_ONLY = True
API_NAME_MAP = {'api_url': 'api_url', 'api_token': 'api_token'}
REQUIRED_DELETE_PATH_PARAMS = []
REQUIRED_GET_PATH_PARAMS = []
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

    req = request.Request(url=url, data=data, headers=headers, method=method)
    try:
        with request.urlopen(req, timeout=30) as response:
            status = int(response.getcode())
            raw = response.read().decode('utf-8')
    except error.HTTPError as exc:
        status = int(exc.code)
        raw = exc.read().decode('utf-8', errors='replace')
        if allow_statuses and status in allow_statuses:
            return status, _decode_body(raw)
        module.fail_json(msg=f'HTTP {status} en {method} {url}: {raw}')
    except error.URLError as exc:
        module.fail_json(msg=f'Error de conexion en {method} {url}: {exc}')

    if expected_statuses and status not in expected_statuses:
        module.fail_json(msg=f'HTTP {status} inesperado en {method} {url}: {raw}')

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
        module.fail_json(msg=f'Faltan parametros requeridos para {context}: {", ".join(missing)}')


def run_module() -> None:
    module_args = dict(
        api_url=dict(type='str', required=True),
        api_token=dict(type='str', required=True, no_log=True),
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=not READ_ONLY)
    params = module.params

    api_url = params['api_url']
    api_token = params['api_token']
    state = params.get('state', 'present')

    result: Dict[str, Any] = dict(changed=False, resource={}, msg='Sin cambios')

    if READ_ONLY:
        if GET_PATH and _has_required(params, GET_PATH_PARAMS):
            get_url = _build_url(api_url, GET_PATH, _collect_params(params, GET_PATH_PARAMS), _collect_params(params, GET_QUERY_PARAMS))
            _, current = _request_json(module, GET_METHOD, get_url, api_token, expected_statuses=[200])
            result['resource'] = current if isinstance(current, dict) else {'value': current}
            result['msg'] = 'Consulta individual completada'
            module.exit_json(**result)

        if LIST_PATH:
            list_url = _build_url(api_url, LIST_PATH, _collect_params(params, LIST_PATH_PARAMS), _collect_params(params, LIST_QUERY_PARAMS))
            _, listing = _request_json(module, LIST_METHOD, list_url, api_token, expected_statuses=[200])
            result['resource'] = listing if isinstance(listing, dict) else {'items': listing}
            result['msg'] = 'Consulta de lista completada'
            module.exit_json(**result)

        module.fail_json(msg='No hay endpoint GET utilizable para este modulo', **result)

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
            module.fail_json(msg='El recurso no soporta operacion delete', **result)
        _ensure_required(module, params, REQUIRED_DELETE_PATH_PARAMS or DELETE_PATH_PARAMS, 'delete')

        if not exists:
            result['msg'] = 'Recurso ya ausente'
            module.exit_json(**result)

        if module.check_mode:
            result['changed'] = True
            result['msg'] = 'Delete planificado (check_mode)'
            module.exit_json(**result)

        delete_url = _build_url(api_url, DELETE_PATH, _collect_params(params, DELETE_PATH_PARAMS), _collect_params(params, DELETE_QUERY_PARAMS))
        _request_json(module, DELETE_METHOD, delete_url, api_token, expected_statuses=[200, 202, 204])
        result['changed'] = True
        result['resource'] = {}
        result['msg'] = 'Recurso eliminado'
        module.exit_json(**result)

    if exists:
        if UPDATE_PATH:
            if not _needs_update(current, desired):
                result['resource'] = current if isinstance(current, dict) else {'value': current}
                result['msg'] = 'Recurso ya en estado deseado'
                module.exit_json(**result)

            if module.check_mode:
                result['changed'] = True
                result['resource'] = current if isinstance(current, dict) else {'value': current}
                result['msg'] = 'Update planificado (check_mode)'
                module.exit_json(**result)

            _ensure_required(module, params, UPDATE_PATH_PARAMS, 'update')
            update_url = _build_url(api_url, UPDATE_PATH, _collect_params(params, UPDATE_PATH_PARAMS), _collect_params(params, UPDATE_QUERY_PARAMS))
            _, updated = _request_json(module, UPDATE_METHOD, update_url, api_token, payload=desired, expected_statuses=[200, 201])
            result['changed'] = True
            result['resource'] = updated if isinstance(updated, dict) else {'value': updated}
            result['msg'] = 'Recurso actualizado'
            module.exit_json(**result)

        result['resource'] = current if isinstance(current, dict) else {'value': current}
        result['msg'] = 'Recurso existente; no hay endpoint de update'
        module.exit_json(**result)

    if not CREATE_PATH:
        module.fail_json(msg='El recurso no existe y no hay endpoint create', **result)

    _ensure_required(module, params, REQUIRED_CREATE_PATH_PARAMS or CREATE_PATH_PARAMS, 'create')

    if module.check_mode:
        result['changed'] = True
        result['msg'] = 'Create planificado (check_mode)'
        module.exit_json(**result)

    create_url = _build_url(api_url, CREATE_PATH, _collect_params(params, CREATE_PATH_PARAMS), _collect_params(params, CREATE_QUERY_PARAMS))
    _, created = _request_json(module, CREATE_METHOD, create_url, api_token, payload=desired, expected_statuses=[200, 201, 202])
    result['changed'] = True
    result['resource'] = created if isinstance(created, dict) else {'value': created}
    result['msg'] = 'Recurso creado'
    module.exit_json(**result)


def main() -> None:
    run_module()


if __name__ == '__main__':
    main()
