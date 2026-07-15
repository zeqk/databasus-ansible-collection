# database -- Manage database resources in Databasus\.

## Synopsis
Allows managing database resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| health_status | optional, str, default=None. Body field healthStatus\. |
| last_backup_error_message | optional, str, default=None. Body field lastBackupErrorMessage\. |
| last_backup_time | optional, str, default=None. these fields are not reliable\, but they are used for pretty UI |
| mariadb | optional, dict, default=None. Body field mariadb\. |
| mariadb.database | optional, str, default=None. Body field database\. |
| mariadb.database_id | optional, str, default=None. Body field databaseId\. |
| mariadb.exclude_tables | optional, list, default=None. Body field excludeTables\. |
| mariadb.host | optional, str, default=None. Body field host\. |
| mariadb.id | optional, str, default=None. Body field id\. |
| mariadb.is_exclude_events | optional, bool, default=None. Body field isExcludeEvents\. |
| mariadb.is_https | optional, bool, default=None. Body field isHttps\. |
| mariadb.is_skip_galera_disable | optional, bool, default=None. Body field isSkipGaleraDisable\. |
| mariadb.is_use_extended_insert | optional, bool, default=None. Body field isUseExtendedInsert\. |
| mariadb.password | optional, str, default=None. Body field password\. |
| mariadb.port | optional, int, default=None. Body field port\. |
| mariadb.privileges | optional, str, default=None. Body field privileges\. |
| mariadb.username | optional, str, default=None. Body field username\. |
| mariadb.version | optional, str, default=None. Body field version\. |

| mongodb | optional, dict, default=None. Body field mongodb\. |
| mongodb.auth_database | optional, str, default=None. Body field authDatabase\. |
| mongodb.cpu_count | optional, int, default=None. Body field cpuCount\. |
| mongodb.database | optional, str, default=None. Body field database\. |
| mongodb.database_id | optional, str, default=None. Body field databaseId\. |
| mongodb.exclude_collections | optional, list, default=None. Body field excludeCollections\. |
| mongodb.host | optional, str, default=None. Body field host\. |
| mongodb.id | optional, str, default=None. Body field id\. |
| mongodb.is_direct_connection | optional, bool, default=None. Body field isDirectConnection\. |
| mongodb.is_https | optional, bool, default=None. Body field isHttps\. |
| mongodb.is_srv | optional, bool, default=None. Body field isSrv\. |
| mongodb.password | optional, str, default=None. Body field password\. |
| mongodb.port | optional, int, default=None. Body field port\. |
| mongodb.username | optional, str, default=None. Body field username\. |
| mongodb.version | optional, str, default=None. Body field version\. |

| mysql | optional, dict, default=None. Body field mysql\. |
| mysql.database | optional, str, default=None. Body field database\. |
| mysql.database_id | optional, str, default=None. Body field databaseId\. |
| mysql.exclude_tables | optional, list, default=None. Body field excludeTables\. |
| mysql.host | optional, str, default=None. Body field host\. |
| mysql.id | optional, str, default=None. Body field id\. |
| mysql.is_https | optional, bool, default=None. Body field isHttps\. |
| mysql.is_use_extended_insert | optional, bool, default=None. Body field isUseExtendedInsert\. |
| mysql.is_zstd_supported | optional, bool, default=None. Body field isZstdSupported\. |
| mysql.password | optional, str, default=None. Body field password\. |
| mysql.port | optional, int, default=None. Body field port\. |
| mysql.privileges | optional, str, default=None. Body field privileges\. |
| mysql.username | optional, str, default=None. Body field username\. |
| mysql.version | optional, str, default=None. Body field version\. |

| name | True, str, default=None. Body field name\. |
| notifiers | optional, list, default=None. Body field notifiers\. |
| notifiers.discord_notifier | optional, dict, default=None. Body field discordNotifier\. |
| notifiers.discord_notifier.channel_webhook_url | optional, str, default=None. Body field channelWebhookUrl\. |
| notifiers.discord_notifier.notifier_id | optional, str, default=None. Body field notifierId\. |

| notifiers.email_notifier | optional, dict, default=None. Body field emailNotifier\. |
| notifiers.email_notifier.from | optional, str, default=None. Body field from\. |
| notifiers.email_notifier.is_insecure_skip_verify | optional, bool, default=None. Body field isInsecureSkipVerify\. |
| notifiers.email_notifier.notifier_id | optional, str, default=None. Body field notifierId\. |
| notifiers.email_notifier.smtp_host | optional, str, default=None. Body field smtpHost\. |
| notifiers.email_notifier.smtp_password | optional, str, default=None. Body field smtpPassword\. |
| notifiers.email_notifier.smtp_port | optional, int, default=None. Body field smtpPort\. |
| notifiers.email_notifier.smtp_user | optional, str, default=None. Body field smtpUser\. |
| notifiers.email_notifier.target_email | optional, str, default=None. Body field targetEmail\. |

| notifiers.id | optional, str, default=None. Body field id\. |
| notifiers.last_send_error | optional, str, default=None. Body field lastSendError\. |
| notifiers.name | optional, str, default=None. Body field name\. |
| notifiers.notifier_type | optional, str, default=None. Body field notifierType\. |
| notifiers.slack_notifier | optional, dict, default=None. Body field slackNotifier\. |
| notifiers.slack_notifier.bot_token | optional, str, default=None. Body field botToken\. |
| notifiers.slack_notifier.notifier_id | optional, str, default=None. Body field notifierId\. |
| notifiers.slack_notifier.target_chat_id | optional, str, default=None. Body field targetChatId\. |

| notifiers.teams_notifier | optional, dict, default=None. Body field teamsNotifier\. |
| notifiers.teams_notifier.notifier_id | optional, str, default=None. Body field notifierId\. |
| notifiers.teams_notifier.power_automate_url | optional, str, default=None. Body field powerAutomateUrl\. |

| notifiers.telegram_notifier | optional, dict, default=None. specific notifier |
| notifiers.telegram_notifier.bot_token | optional, str, default=None. Body field botToken\. |
| notifiers.telegram_notifier.is_proxy_enabled | optional, bool, default=None. Body field isProxyEnabled\. |
| notifiers.telegram_notifier.notifier_id | optional, str, default=None. Body field notifierId\. |
| notifiers.telegram_notifier.proxy_url | optional, str, default=None. Body field proxyUrl\. |
| notifiers.telegram_notifier.target_chat_id | optional, str, default=None. Body field targetChatId\. |
| notifiers.telegram_notifier.thread_id | optional, int, default=None. Body field threadId\. |

| notifiers.webhook_notifier | optional, dict, default=None. Body field webhookNotifier\. |
| notifiers.webhook_notifier.body_template | optional, str, default=None. Body field bodyTemplate\. |
| notifiers.webhook_notifier.headers | optional, list, default=None. Body field headers\. |
| notifiers.webhook_notifier.headers.key | optional, str, default=None. Body field key\. |
| notifiers.webhook_notifier.headers.value | optional, str, default=None. Body field value\. |

| notifiers.webhook_notifier.notifier_id | optional, str, default=None. Body field notifierId\. |
| notifiers.webhook_notifier.webhook_method | optional, str, default=None. Body field webhookMethod\. |
| notifiers.webhook_notifier.webhook_url | optional, str, default=None. Body field webhookUrl\. |

| notifiers.workspace_id | optional, str, default=None. Body field workspaceId\. |

| postgresql_logical | optional, dict, default=None. Body field postgresqlLogical\. |
| postgresql_logical.cpu_count | optional, int, default=None. Body field cpuCount\. |
| postgresql_logical.database | optional, str, default=None. Body field database\. |
| postgresql_logical.database_id | optional, str, default=None. Body field databaseId\. |
| postgresql_logical.exclude_tables | optional, list, default=None. Body field excludeTables\. |
| postgresql_logical.host | optional, str, default=None. Body field host\. |
| postgresql_logical.id | optional, str, default=None. Body field id\. |
| postgresql_logical.include_schemas | optional, list, default=None. backup settings |
| postgresql_logical.is_exclude_extensions | optional, bool, default=None. restore settings \(not saved to DB\) |
| postgresql_logical.is_restore_ownership | optional, bool, default=None. Body field isRestoreOwnership\. |
| postgresql_logical.is_restore_privileges | optional, bool, default=None. Body field isRestorePrivileges\. |
| postgresql_logical.is_skip_user_mappings | optional, bool, default=None. Body field isSkipUserMappings\. |
| postgresql_logical.password | optional, str, default=None. Body field password\. |
| postgresql_logical.port | optional, int, default=None. Body field port\. |
| postgresql_logical.ssl_client_cert | optional, str, default=None. Body field sslClientCert\. |
| postgresql_logical.ssl_client_key | optional, str, default=None. Body field sslClientKey\. |
| postgresql_logical.ssl_mode | optional, str, default=None. SSL / TLS connection settings |
| postgresql_logical.ssl_root_cert | optional, str, default=None. Body field sslRootCert\. |
| postgresql_logical.username | optional, str, default=None. Body field username\. |
| postgresql_logical.version | optional, str, default=None. Body field version\. |

| postgresql_physical | optional, dict, default=None. Body field postgresqlPhysical\. |
| postgresql_physical.backup_type | optional, str, default=None. Body field backupType\. |
| postgresql_physical.database_id | optional, str, default=None. Body field databaseId\. |
| postgresql_physical.host | optional, str, default=None. Body field host\. |
| postgresql_physical.id | optional, str, default=None. Body field id\. |
| postgresql_physical.password | optional, str, default=None. Body field password\. |
| postgresql_physical.port | optional, int, default=None. Body field port\. |
| postgresql_physical.ssl_client_cert | optional, str, default=None. Body field sslClientCert\. |
| postgresql_physical.ssl_client_key | optional, str, default=None. Body field sslClientKey\. |
| postgresql_physical.ssl_mode | optional, str, default=None. SSL / TLS connection settings |
| postgresql_physical.ssl_root_cert | optional, str, default=None. Body field sslRootCert\. |
| postgresql_physical.system_identifier | optional, str, default=None. Body field systemIdentifier\. |
| postgresql_physical.username | optional, str, default=None. Body field username\. |
| postgresql_physical.version | optional, str, default=None. Body field version\. |
| postgresql_physical.wal_segment_size_bytes | optional, int, default=None. WalSegmentSizeBytes captures the source cluster\'s wal\_segment\_size at first connect\. |

| type | optional, str, default=None. Body field type\. |
| workspace_id | optional, str, default=None. Workspace ID |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.database:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        name: example-name
        health_status: null

    - name: Delete resource
      zeqk.databasus.database:
        state: absent
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        name: example-name

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.health_status | success, str. Field healthStatus\. |
| resource.id | success, str. Field id\. |
| resource.last_backup_error_message | success, str. Field lastBackupErrorMessage\. |
| resource.last_backup_time | success, str. these fields are not reliable\, but they are used for pretty UI |
| resource.mariadb | success, dict. Field mariadb\. |
| resource.mariadb.database | success, str. Field database\. |
| resource.mariadb.database_id | success, str. Field databaseId\. |
| resource.mariadb.exclude_tables | success, list. Field excludeTables\. |
| resource.mariadb.host | success, str. Field host\. |
| resource.mariadb.id | success, str. Field id\. |
| resource.mariadb.is_exclude_events | success, bool. Field isExcludeEvents\. |
| resource.mariadb.is_https | success, bool. Field isHttps\. |
| resource.mariadb.is_skip_galera_disable | success, bool. Field isSkipGaleraDisable\. |
| resource.mariadb.is_use_extended_insert | success, bool. Field isUseExtendedInsert\. |
| resource.mariadb.password | success, str. Field password\. |
| resource.mariadb.port | success, int. Field port\. |
| resource.mariadb.privileges | success, str. Field privileges\. |
| resource.mariadb.username | success, str. Field username\. |
| resource.mariadb.version | success, str. Field version\. |

| resource.mongodb | success, dict. Field mongodb\. |
| resource.mongodb.auth_database | success, str. Field authDatabase\. |
| resource.mongodb.cpu_count | success, int. Field cpuCount\. |
| resource.mongodb.database | success, str. Field database\. |
| resource.mongodb.database_id | success, str. Field databaseId\. |
| resource.mongodb.exclude_collections | success, list. Field excludeCollections\. |
| resource.mongodb.host | success, str. Field host\. |
| resource.mongodb.id | success, str. Field id\. |
| resource.mongodb.is_direct_connection | success, bool. Field isDirectConnection\. |
| resource.mongodb.is_https | success, bool. Field isHttps\. |
| resource.mongodb.is_srv | success, bool. Field isSrv\. |
| resource.mongodb.password | success, str. Field password\. |
| resource.mongodb.port | success, int. Field port\. |
| resource.mongodb.username | success, str. Field username\. |
| resource.mongodb.version | success, str. Field version\. |

| resource.mysql | success, dict. Field mysql\. |
| resource.mysql.database | success, str. Field database\. |
| resource.mysql.database_id | success, str. Field databaseId\. |
| resource.mysql.exclude_tables | success, list. Field excludeTables\. |
| resource.mysql.host | success, str. Field host\. |
| resource.mysql.id | success, str. Field id\. |
| resource.mysql.is_https | success, bool. Field isHttps\. |
| resource.mysql.is_use_extended_insert | success, bool. Field isUseExtendedInsert\. |
| resource.mysql.is_zstd_supported | success, bool. Field isZstdSupported\. |
| resource.mysql.password | success, str. Field password\. |
| resource.mysql.port | success, int. Field port\. |
| resource.mysql.privileges | success, str. Field privileges\. |
| resource.mysql.username | success, str. Field username\. |
| resource.mysql.version | success, str. Field version\. |

| resource.name | success, str. Field name\. |
| resource.notifiers | success, list. Field notifiers\. |
| resource.notifiers.discord_notifier | success, dict. Field discordNotifier\. |
| resource.notifiers.discord_notifier.channel_webhook_url | success, str. Field channelWebhookUrl\. |
| resource.notifiers.discord_notifier.notifier_id | success, str. Field notifierId\. |

| resource.notifiers.email_notifier | success, dict. Field emailNotifier\. |
| resource.notifiers.email_notifier.from | success, str. Field from\. |
| resource.notifiers.email_notifier.is_insecure_skip_verify | success, bool. Field isInsecureSkipVerify\. |
| resource.notifiers.email_notifier.notifier_id | success, str. Field notifierId\. |
| resource.notifiers.email_notifier.smtp_host | success, str. Field smtpHost\. |
| resource.notifiers.email_notifier.smtp_password | success, str. Field smtpPassword\. |
| resource.notifiers.email_notifier.smtp_port | success, int. Field smtpPort\. |
| resource.notifiers.email_notifier.smtp_user | success, str. Field smtpUser\. |
| resource.notifiers.email_notifier.target_email | success, str. Field targetEmail\. |

| resource.notifiers.id | success, str. Field id\. |
| resource.notifiers.last_send_error | success, str. Field lastSendError\. |
| resource.notifiers.name | success, str. Field name\. |
| resource.notifiers.notifier_type | success, str. Field notifierType\. |
| resource.notifiers.slack_notifier | success, dict. Field slackNotifier\. |
| resource.notifiers.slack_notifier.bot_token | success, str. Field botToken\. |
| resource.notifiers.slack_notifier.notifier_id | success, str. Field notifierId\. |
| resource.notifiers.slack_notifier.target_chat_id | success, str. Field targetChatId\. |

| resource.notifiers.teams_notifier | success, dict. Field teamsNotifier\. |
| resource.notifiers.teams_notifier.notifier_id | success, str. Field notifierId\. |
| resource.notifiers.teams_notifier.power_automate_url | success, str. Field powerAutomateUrl\. |

| resource.notifiers.telegram_notifier | success, dict. specific notifier |
| resource.notifiers.telegram_notifier.bot_token | success, str. Field botToken\. |
| resource.notifiers.telegram_notifier.is_proxy_enabled | success, bool. Field isProxyEnabled\. |
| resource.notifiers.telegram_notifier.notifier_id | success, str. Field notifierId\. |
| resource.notifiers.telegram_notifier.proxy_url | success, str. Field proxyUrl\. |
| resource.notifiers.telegram_notifier.target_chat_id | success, str. Field targetChatId\. |
| resource.notifiers.telegram_notifier.thread_id | success, int. Field threadId\. |

| resource.notifiers.webhook_notifier | success, dict. Field webhookNotifier\. |
| resource.notifiers.webhook_notifier.body_template | success, str. Field bodyTemplate\. |
| resource.notifiers.webhook_notifier.headers | success, list. Field headers\. |
| resource.notifiers.webhook_notifier.headers.key | success, str. Field key\. |
| resource.notifiers.webhook_notifier.headers.value | success, str. Field value\. |

| resource.notifiers.webhook_notifier.notifier_id | success, str. Field notifierId\. |
| resource.notifiers.webhook_notifier.webhook_method | success, str. Field webhookMethod\. |
| resource.notifiers.webhook_notifier.webhook_url | success, str. Field webhookUrl\. |

| resource.notifiers.workspace_id | success, str. Field workspaceId\. |

| resource.postgresql_logical | success, dict. Field postgresqlLogical\. |
| resource.postgresql_logical.cpu_count | success, int. Field cpuCount\. |
| resource.postgresql_logical.database | success, str. Field database\. |
| resource.postgresql_logical.database_id | success, str. Field databaseId\. |
| resource.postgresql_logical.exclude_tables | success, list. Field excludeTables\. |
| resource.postgresql_logical.host | success, str. Field host\. |
| resource.postgresql_logical.id | success, str. Field id\. |
| resource.postgresql_logical.include_schemas | success, list. backup settings |
| resource.postgresql_logical.is_exclude_extensions | success, bool. restore settings \(not saved to DB\) |
| resource.postgresql_logical.is_restore_ownership | success, bool. Field isRestoreOwnership\. |
| resource.postgresql_logical.is_restore_privileges | success, bool. Field isRestorePrivileges\. |
| resource.postgresql_logical.is_skip_user_mappings | success, bool. Field isSkipUserMappings\. |
| resource.postgresql_logical.password | success, str. Field password\. |
| resource.postgresql_logical.port | success, int. Field port\. |
| resource.postgresql_logical.ssl_client_cert | success, str. Field sslClientCert\. |
| resource.postgresql_logical.ssl_client_key | success, str. Field sslClientKey\. |
| resource.postgresql_logical.ssl_mode | success, str. SSL / TLS connection settings |
| resource.postgresql_logical.ssl_root_cert | success, str. Field sslRootCert\. |
| resource.postgresql_logical.username | success, str. Field username\. |
| resource.postgresql_logical.version | success, str. Field version\. |

| resource.postgresql_physical | success, dict. Field postgresqlPhysical\. |
| resource.postgresql_physical.backup_type | success, str. Field backupType\. |
| resource.postgresql_physical.database_id | success, str. Field databaseId\. |
| resource.postgresql_physical.host | success, str. Field host\. |
| resource.postgresql_physical.id | success, str. Field id\. |
| resource.postgresql_physical.password | success, str. Field password\. |
| resource.postgresql_physical.port | success, int. Field port\. |
| resource.postgresql_physical.ssl_client_cert | success, str. Field sslClientCert\. |
| resource.postgresql_physical.ssl_client_key | success, str. Field sslClientKey\. |
| resource.postgresql_physical.ssl_mode | success, str. SSL / TLS connection settings |
| resource.postgresql_physical.ssl_root_cert | success, str. Field sslRootCert\. |
| resource.postgresql_physical.system_identifier | success, str. Field systemIdentifier\. |
| resource.postgresql_physical.username | success, str. Field username\. |
| resource.postgresql_physical.version | success, str. Field version\. |
| resource.postgresql_physical.wal_segment_size_bytes | success, int. WalSegmentSizeBytes captures the source cluster\'s wal\_segment\_size at first connect\. |

| resource.type | success, str. Field type\. |
| resource.workspace_id | success, str. WorkspaceID can be null when a database is created via restore operation outside the context of any workspace |

| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

