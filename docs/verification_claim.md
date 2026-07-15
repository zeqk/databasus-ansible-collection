# verification_claim -- Manage verification\_claim resources in Databasus\.

## Synopsis
Allows managing verification\_claim resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| agent_id | optional, str, default=None. Agent UUID |
| capacity | optional, dict, default=None. Body field capacity\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.verification_claim:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        capacity: null

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.backup_id | success, str. Field backupId\. |
| resource.backup_size_mb | success, float. Field backupSizeMb\. |
| resource.database | success, dict. Field database\. |
| resource.database.health_status | success, str. Field healthStatus\. |
| resource.database.id | success, str. Field id\. |
| resource.database.last_backup_error_message | success, str. Field lastBackupErrorMessage\. |
| resource.database.last_backup_time | success, str. these fields are not reliable\, but they are used for pretty UI |
| resource.database.mariadb | success, dict. Field mariadb\. |
| resource.database.mariadb.database | success, str. Field database\. |
| resource.database.mariadb.database_id | success, str. Field databaseId\. |
| resource.database.mariadb.exclude_tables | success, list. Field excludeTables\. |
| resource.database.mariadb.host | success, str. Field host\. |
| resource.database.mariadb.id | success, str. Field id\. |
| resource.database.mariadb.is_exclude_events | success, bool. Field isExcludeEvents\. |
| resource.database.mariadb.is_https | success, bool. Field isHttps\. |
| resource.database.mariadb.is_skip_galera_disable | success, bool. Field isSkipGaleraDisable\. |
| resource.database.mariadb.is_use_extended_insert | success, bool. Field isUseExtendedInsert\. |
| resource.database.mariadb.password | success, str. Field password\. |
| resource.database.mariadb.port | success, int. Field port\. |
| resource.database.mariadb.privileges | success, str. Field privileges\. |
| resource.database.mariadb.username | success, str. Field username\. |
| resource.database.mariadb.version | success, str. Field version\. |

| resource.database.mongodb | success, dict. Field mongodb\. |
| resource.database.mongodb.auth_database | success, str. Field authDatabase\. |
| resource.database.mongodb.cpu_count | success, int. Field cpuCount\. |
| resource.database.mongodb.database | success, str. Field database\. |
| resource.database.mongodb.database_id | success, str. Field databaseId\. |
| resource.database.mongodb.exclude_collections | success, list. Field excludeCollections\. |
| resource.database.mongodb.host | success, str. Field host\. |
| resource.database.mongodb.id | success, str. Field id\. |
| resource.database.mongodb.is_direct_connection | success, bool. Field isDirectConnection\. |
| resource.database.mongodb.is_https | success, bool. Field isHttps\. |
| resource.database.mongodb.is_srv | success, bool. Field isSrv\. |
| resource.database.mongodb.password | success, str. Field password\. |
| resource.database.mongodb.port | success, int. Field port\. |
| resource.database.mongodb.username | success, str. Field username\. |
| resource.database.mongodb.version | success, str. Field version\. |

| resource.database.mysql | success, dict. Field mysql\. |
| resource.database.mysql.database | success, str. Field database\. |
| resource.database.mysql.database_id | success, str. Field databaseId\. |
| resource.database.mysql.exclude_tables | success, list. Field excludeTables\. |
| resource.database.mysql.host | success, str. Field host\. |
| resource.database.mysql.id | success, str. Field id\. |
| resource.database.mysql.is_https | success, bool. Field isHttps\. |
| resource.database.mysql.is_use_extended_insert | success, bool. Field isUseExtendedInsert\. |
| resource.database.mysql.is_zstd_supported | success, bool. Field isZstdSupported\. |
| resource.database.mysql.password | success, str. Field password\. |
| resource.database.mysql.port | success, int. Field port\. |
| resource.database.mysql.privileges | success, str. Field privileges\. |
| resource.database.mysql.username | success, str. Field username\. |
| resource.database.mysql.version | success, str. Field version\. |

| resource.database.name | success, str. Field name\. |
| resource.database.notifiers | success, list. Field notifiers\. |
| resource.database.notifiers.discord_notifier | success, dict. Field discordNotifier\. |
| resource.database.notifiers.discord_notifier.channel_webhook_url | success, str. Field channelWebhookUrl\. |
| resource.database.notifiers.discord_notifier.notifier_id | success, str. Field notifierId\. |

| resource.database.notifiers.email_notifier | success, dict. Field emailNotifier\. |
| resource.database.notifiers.email_notifier.from | success, str. Field from\. |
| resource.database.notifiers.email_notifier.is_insecure_skip_verify | success, bool. Field isInsecureSkipVerify\. |
| resource.database.notifiers.email_notifier.notifier_id | success, str. Field notifierId\. |
| resource.database.notifiers.email_notifier.smtp_host | success, str. Field smtpHost\. |
| resource.database.notifiers.email_notifier.smtp_password | success, str. Field smtpPassword\. |
| resource.database.notifiers.email_notifier.smtp_port | success, int. Field smtpPort\. |
| resource.database.notifiers.email_notifier.smtp_user | success, str. Field smtpUser\. |
| resource.database.notifiers.email_notifier.target_email | success, str. Field targetEmail\. |

| resource.database.notifiers.id | success, str. Field id\. |
| resource.database.notifiers.last_send_error | success, str. Field lastSendError\. |
| resource.database.notifiers.name | success, str. Field name\. |
| resource.database.notifiers.notifier_type | success, str. Field notifierType\. |
| resource.database.notifiers.slack_notifier | success, dict. Field slackNotifier\. |
| resource.database.notifiers.slack_notifier.bot_token | success, str. Field botToken\. |
| resource.database.notifiers.slack_notifier.notifier_id | success, str. Field notifierId\. |
| resource.database.notifiers.slack_notifier.target_chat_id | success, str. Field targetChatId\. |

| resource.database.notifiers.teams_notifier | success, dict. Field teamsNotifier\. |
| resource.database.notifiers.teams_notifier.notifier_id | success, str. Field notifierId\. |
| resource.database.notifiers.teams_notifier.power_automate_url | success, str. Field powerAutomateUrl\. |

| resource.database.notifiers.telegram_notifier | success, dict. specific notifier |
| resource.database.notifiers.telegram_notifier.bot_token | success, str. Field botToken\. |
| resource.database.notifiers.telegram_notifier.is_proxy_enabled | success, bool. Field isProxyEnabled\. |
| resource.database.notifiers.telegram_notifier.notifier_id | success, str. Field notifierId\. |
| resource.database.notifiers.telegram_notifier.proxy_url | success, str. Field proxyUrl\. |
| resource.database.notifiers.telegram_notifier.target_chat_id | success, str. Field targetChatId\. |
| resource.database.notifiers.telegram_notifier.thread_id | success, int. Field threadId\. |

| resource.database.notifiers.webhook_notifier | success, dict. Field webhookNotifier\. |
| resource.database.notifiers.webhook_notifier.body_template | success, str. Field bodyTemplate\. |
| resource.database.notifiers.webhook_notifier.headers | success, list. Field headers\. |
| resource.database.notifiers.webhook_notifier.notifier_id | success, str. Field notifierId\. |
| resource.database.notifiers.webhook_notifier.webhook_method | success, str. Field webhookMethod\. |
| resource.database.notifiers.webhook_notifier.webhook_url | success, str. Field webhookUrl\. |

| resource.database.notifiers.workspace_id | success, str. Field workspaceId\. |

| resource.database.postgresql_logical | success, dict. Field postgresqlLogical\. |
| resource.database.postgresql_logical.cpu_count | success, int. Field cpuCount\. |
| resource.database.postgresql_logical.database | success, str. Field database\. |
| resource.database.postgresql_logical.database_id | success, str. Field databaseId\. |
| resource.database.postgresql_logical.exclude_tables | success, list. Field excludeTables\. |
| resource.database.postgresql_logical.host | success, str. Field host\. |
| resource.database.postgresql_logical.id | success, str. Field id\. |
| resource.database.postgresql_logical.include_schemas | success, list. backup settings |
| resource.database.postgresql_logical.is_exclude_extensions | success, bool. restore settings \(not saved to DB\) |
| resource.database.postgresql_logical.is_restore_ownership | success, bool. Field isRestoreOwnership\. |
| resource.database.postgresql_logical.is_restore_privileges | success, bool. Field isRestorePrivileges\. |
| resource.database.postgresql_logical.is_skip_user_mappings | success, bool. Field isSkipUserMappings\. |
| resource.database.postgresql_logical.password | success, str. Field password\. |
| resource.database.postgresql_logical.port | success, int. Field port\. |
| resource.database.postgresql_logical.ssl_client_cert | success, str. Field sslClientCert\. |
| resource.database.postgresql_logical.ssl_client_key | success, str. Field sslClientKey\. |
| resource.database.postgresql_logical.ssl_mode | success, dict. SSL / TLS connection settings |
| resource.database.postgresql_logical.ssl_root_cert | success, str. Field sslRootCert\. |
| resource.database.postgresql_logical.username | success, str. Field username\. |
| resource.database.postgresql_logical.version | success, str. Field version\. |

| resource.database.postgresql_physical | success, dict. Field postgresqlPhysical\. |
| resource.database.postgresql_physical.backup_type | success, str. Field backupType\. |
| resource.database.postgresql_physical.database_id | success, str. Field databaseId\. |
| resource.database.postgresql_physical.host | success, str. Field host\. |
| resource.database.postgresql_physical.id | success, str. Field id\. |
| resource.database.postgresql_physical.password | success, str. Field password\. |
| resource.database.postgresql_physical.port | success, int. Field port\. |
| resource.database.postgresql_physical.ssl_client_cert | success, str. Field sslClientCert\. |
| resource.database.postgresql_physical.ssl_client_key | success, str. Field sslClientKey\. |
| resource.database.postgresql_physical.ssl_mode | success, dict. SSL / TLS connection settings |
| resource.database.postgresql_physical.ssl_root_cert | success, str. Field sslRootCert\. |
| resource.database.postgresql_physical.system_identifier | success, str. Field systemIdentifier\. |
| resource.database.postgresql_physical.username | success, str. Field username\. |
| resource.database.postgresql_physical.version | success, str. Field version\. |
| resource.database.postgresql_physical.wal_segment_size_bytes | success, int. WalSegmentSizeBytes captures the source cluster\'s wal\_segment\_size at first connect\. |

| resource.database.type | success, str. Field type\. |
| resource.database.workspace_id | success, str. WorkspaceID can be null when a database is created via restore operation outside the context of any workspace |

| resource.max_container_disk_mb | success, float. Field maxContainerDiskMb\. |
| resource.timescaledb_version | success, str. Field timescaledbVersion\. |
| resource.verification_id | success, str. Field verificationId\. |

| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

