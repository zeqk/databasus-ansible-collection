# Integration Test Plan (Databasus Ansible Collection)

Fecha de corte: 2026-07-16

## Objetivo
Agregar integration tests para todos los modulos, con cobertura en dos niveles:
- Smoke global para todos los modulos.
- Cobertura profunda (CRUD/acciones) para modulos core.

## Decisiones acordadas
- Estrategia de tests: manuales en `tests/integration/targets`.
- Infra local: `docker-compose.yml` con Databasus + PostgreSQL.
- Cobertura fase 1: smoke en todos los modulos.
- Core para cobertura profunda: `workspace`, `database`, `storage`, `backup`.

## Estado actual

### Fase 1 (completada)
1. Bootstrap comun de autenticacion/readiness implementado a nivel target.
2. Target smoke global implementado y ejecutado con exito.
3. Target `workspace` refactorizado para usar bootstrap local y validado.
4. `docker-compose.yml` extendido con servicio PostgreSQL y `depends_on` healthy.
5. README actualizado con comandos de ejecucion.
6. Sanity `yamllint` en verde.

Resultado de ejecucion reciente:
- `all_modules_smoke`: `failed=0`.
- `workspace`: `failed=0`.

## Archivos clave modificados
- `ansible_collections/zeqk/databasus/tests/integration/targets/all_modules_smoke/tasks/main.yml`
- `ansible_collections/zeqk/databasus/tests/integration/targets/all_modules_smoke/tasks/run_module_smoke.yml`
- `ansible_collections/zeqk/databasus/tests/integration/targets/all_modules_smoke/tasks/bootstrap.yml`
- `ansible_collections/zeqk/databasus/tests/integration/targets/all_modules_smoke/COVERAGE.md`
- `ansible_collections/zeqk/databasus/tests/integration/targets/workspace/tasks/main.yml`
- `ansible_collections/zeqk/databasus/tests/integration/targets/workspace/tasks/bootstrap.yml`
- `docker-compose.yml`
- `README.md`

## Proximas fases

### Fase 2 (pendiente): cobertura profunda de modulos core
Objetivo: crear targets dedicados para `database`, `storage`, `backup` con asserts de comportamiento e idempotencia.

Lineamientos:
1. Reusar bootstrap local por target.
2. Preparar fixtures minimos por suite (nombres unicos por ejecucion).
3. Verificar al menos:
   - create/present
   - idempotencia (`changed == false` en segunda corrida)
   - delete/absent cuando aplique
   - validaciones de errores esperados en acciones puntuales
4. Cleanup explicito de recursos creados.

Targets a crear:
- `tests/integration/targets/database/tasks/main.yml`
- `tests/integration/targets/storage/tasks/main.yml`
- `tests/integration/targets/backup/tasks/main.yml`

### Fase 3 (pendiente): endurecimiento y consolidacion
1. Reducir flakes (retries/timeouts uniformes en waits y asserts de readiness).
2. Ajustar asserts para endpoints con semantica particular (403/404 esperados, etc.).
3. Ejecutar suite completa de integration targets y registrar resultados.

## Comandos de continuidad
Desde la raiz del repo:

```bash
docker compose up -d
```

```bash
cd ansible_collections/zeqk/databasus
uv run ansible-test integration all_modules_smoke -v
uv run ansible-test integration workspace -v
```

Para desarrollar fase 2:

```bash
cd ansible_collections/zeqk/databasus
uv run ansible-test integration database -v
uv run ansible-test integration storage -v
uv run ansible-test integration backup -v
```

Sanity:

```bash
cd ansible_collections/zeqk/databasus
uv run ansible-test sanity
```

Apagado de entorno:

```bash
cd /home/zeqk/MyProjects/databasus-ansible-collection
docker compose down
```

## Riesgos conocidos
- Varios modulos requieren IDs/fixtures especificos; en smoke se permiten errores funcionales esperados sin traceback.
- El comportamiento exacto de algunos endpoints depende del estado de Databasus y datos previos.
- Si cambia el OpenAPI y se regenera la coleccion, revisar impacto en tests y cobertura.

## Regla importante del repo
Este proyecto es generator-driven. Cambios funcionales de modulos deben hacerse en:
- `scripts/generate_collection.py`

No editar a mano modulos generados en:
- `ansible_collections/zeqk/databasus/plugins/modules/`
