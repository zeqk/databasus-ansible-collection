# all_modules_smoke coverage

Scope for phase 1:
- Cover every generated module with an executable smoke invocation.
- Validate module runtime stability: no Python traceback and structured Ansible result.
- Allow business/API errors for missing fixtures in smoke (deep behavior is validated in dedicated core targets).

Modules covered (51 with api_token + user_signin):
- agent
- agent_rotate_token
- audit_log
- auth
- backup
- backup_cancel
- backup_config
- backup_config_physical
- backup_download_token
- backup_file
- backup_restore_token
- database
- database_backup
- database_copy
- database_info
- database_restore_token
- database_test_connection
- database_transfer
- database_trigger
- disk
- healthcheck_attempt
- healthcheck_config
- membership_member
- membership_transfer_ownership
- notifier
- notifier_databases_count
- notifier_info
- notifier_is_using
- notifier_test
- notifier_transfer
- restore
- restore_restore
- storage
- storage_databases_count
- storage_info
- storage_is_using
- storage_test
- storage_transfer
- system
- user
- user_activate
- user_deactivate
- verification
- verification_cancel
- verification_claim
- verification_config
- verification_heartbeat
- verification_info
- workspace
- workspace_audit_log
- workspace_info
- user_signin

Out of scope for phase 1:
- Deep CRUD assertions for non-core modules.
- Full fixture orchestration for action modules requiring resource IDs.

Phase 2 candidates (deep coverage targets):
- workspace (already implemented)
- database
- storage
- backup
