# Databasus Local Example

This example starts Databasus plus PostgreSQL 18 with Docker Compose, then runs a playbook that:

- signs in with the Databasus admin user,
- creates a workspace,
- creates a LOCAL storage,
- creates a POSTGRES_PHYSICAL database,
- configures physical backup with FULL_INCREMENTAL_WAL_STREAM.

## Prerequisites

- Docker and Docker Compose
- Ansible available in your environment
- Collection generated and available from this repository

## 1. Prepare environment variables

Copy and edit the example env file:

```bash
cp docs/example/.env.example docs/example/.env
```

Set the admin credentials in docs/example/.env:

- `DATABASUS_ADMIN_EMAIL`
- `DATABASUS_ADMIN_PASSWORD`

These must match the admin account created on your first Databasus startup.

## 2. Start local services

```bash
docker compose --env-file docs/example/.env -f docs/example/docker-compose.yml up -d
```

## 3. Export variables for Ansible

```bash
set -a
source docs/example/.env
set +a
```

## 4. Run the playbook

```bash
ansible-playbook docs/example/setup_workspace_storage_backup.yml
```

## 5. Stop local services

```bash
docker compose -f docs/example/docker-compose.yml down
```

## Notes

- PostgreSQL host default is `postgres18` because Databasus runs in Docker and resolves service names on the compose network.
- Databasus API URL default is `http://127.0.0.1:4005/api/v1`.
- Re-running the playbook should keep resources in `state: present`.
