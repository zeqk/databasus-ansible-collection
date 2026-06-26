# zeqk.databasus

Ansible collection generated from `openapi.json` to manage Databasus API resources.

## Requirements

- Ansible Core 2.14+
- Python 3 on the controller node

## Generated modules

| Module | FQCN | Detected operations |
|---|---|---|
| `agent` | `zeqk.databasus.agent` | `create, list` |
| `agent_rotate_token` | `zeqk.databasus.agent_rotate_token` | `create` |
| `audit_log` | `zeqk.databasus.audit_log` | `get, list` |
| `auth` | `zeqk.databasus.auth` | `create` |
| `backup` | `zeqk.databasus.backup` | `create, delete, list` |
| `backup_cancel` | `zeqk.databasus.backup_cancel` | `create` |
| `backup_config` | `zeqk.databasus.backup_config` | `create, get` |
| `backup_download_token` | `zeqk.databasus.backup_download_token` | `create` |
| `backup_file` | `zeqk.databasus.backup_file` | `list` |
| `backup_restore_token` | `zeqk.databasus.backup_restore_token` | `create` |
| `database` | `zeqk.databasus.database` | `create, delete, get, list` |
| `database_backup` | `zeqk.databasus.database_backup` | `list` |
| `database_copy` | `zeqk.databasus.database_copy` | `create` |
| `database_restore_token` | `zeqk.databasus.database_restore_token` | `create` |
| `database_test_connection` | `zeqk.databasus.database_test_connection` | `create` |
| `database_transfer` | `zeqk.databasus.database_transfer` | `create` |
| `database_trigger` | `zeqk.databasus.database_trigger` | `create` |
| `disk` | `zeqk.databasus.disk` | `list` |
| `healthcheck_attempt` | `zeqk.databasus.healthcheck_attempt` | `get` |
| `healthcheck_config` | `zeqk.databasus.healthcheck_config` | `create, get` |
| `membership_member` | `zeqk.databasus.membership_member` | `create, delete, list` |
| `membership_transfer_ownership` | `zeqk.databasus.membership_transfer_ownership` | `create` |
| `notifier` | `zeqk.databasus.notifier` | `create, delete, get, list` |
| `notifier_databases_count` | `zeqk.databasus.notifier_databases_count` | `list` |
| `notifier_is_using` | `zeqk.databasus.notifier_is_using` | `list` |
| `notifier_test` | `zeqk.databasus.notifier_test` | `create` |
| `notifier_transfer` | `zeqk.databasus.notifier_transfer` | `create` |
| `restore` | `zeqk.databasus.restore` | `get` |
| `restore_restore` | `zeqk.databasus.restore_restore` | `create` |
| `storage` | `zeqk.databasus.storage` | `create, delete, get, list` |
| `storage_databases_count` | `zeqk.databasus.storage_databases_count` | `list` |
| `storage_is_using` | `zeqk.databasus.storage_is_using` | `list` |
| `storage_test` | `zeqk.databasus.storage_test` | `create` |
| `storage_transfer` | `zeqk.databasus.storage_transfer` | `create` |
| `system` | `zeqk.databasus.system` | `list` |
| `user` | `zeqk.databasus.user` | `create, get, list` |
| `user_activate` | `zeqk.databasus.user_activate` | `create` |
| `user_deactivate` | `zeqk.databasus.user_deactivate` | `create` |
| `verification` | `zeqk.databasus.verification` | `create, delete, get, list` |
| `verification_cancel` | `zeqk.databasus.verification_cancel` | `create` |
| `verification_claim` | `zeqk.databasus.verification_claim` | `create` |
| `verification_config` | `zeqk.databasus.verification_config` | `get, update` |
| `verification_heartbeat` | `zeqk.databasus.verification_heartbeat` | `create` |
| `workspace` | `zeqk.databasus.workspace` | `create, delete, get, list, update` |
| `workspace_audit_log` | `zeqk.databasus.workspace_audit_log` | `list` |

## Basic usage

```yaml
- name: Manage database
  hosts: localhost
  tasks:
    - name: Create database
      zeqk.databasus.database:
        state: present
        api_url: "https://api.databasus.example.com"
        api_token: "{{ lookup('env', 'DATABASUS_TOKEN') }}"
        name: "production-db"

    - name: Delete database
      zeqk.databasus.database:
        state: absent
        api_url: "https://api.databasus.example.com"
        api_token: "{{ lookup('env', 'DATABASUS_TOKEN') }}"
        id: "db-abc123"
```
