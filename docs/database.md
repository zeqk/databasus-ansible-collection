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
| mongodb | optional, dict, default=None. Body field mongodb\. |
| mysql | optional, dict, default=None. Body field mysql\. |
| name | True, str, default=None. Body field name\. |
| notifiers | optional, list, default=None. Body field notifiers\. |
| postgresql_logical | optional, dict, default=None. Body field postgresqlLogical\. |
| postgresql_physical | optional, dict, default=None. Body field postgresqlPhysical\. |
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
| resource.postgresql_logical.ssl_mode | success, dict. SSL / TLS connection settings |
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
| resource.postgresql_physical.ssl_mode | success, dict. SSL / TLS connection settings |
| resource.postgresql_physical.ssl_root_cert | success, str. Field sslRootCert\. |
| resource.postgresql_physical.system_identifier | success, str. Field systemIdentifier\. |
| resource.postgresql_physical.username | success, str. Field username\. |
| resource.postgresql_physical.version | success, str. Field version\. |
| resource.postgresql_physical.wal_segment_size_bytes | success, int. WalSegmentSizeBytes captures the source cluster\'s wal\_segment\_size at first connect\. |

| resource.type | success, str. Field type\. |
| resource.workspace_id | success, str. WorkspaceID can be null when a database is created via restore operation outside the context of any workspace |

| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

