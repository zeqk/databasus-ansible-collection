# backup_config_physical -- Manage backup\_config\_physical resources in Databasus\.

## Synopsis
Allows managing backup\_config\_physical resources using the Databasus API\.

Uses \`\`GET /backup\-configs/physical/database/\{id\}\`\`\.

Uses \`\`POST /backup\-configs/physical/save\`\`\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. Possible values\; present\, absent\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| chains_retention | optional, dict, default=None. Body field chainsRetention\. |
| chains_retention.count | optional, int, default=None. Body field count\. |
| database_id | optional, str, default=None. Body field databaseId\. |
| encryption | optional, str, default=None. Body field encryption\. Possible values\; NONE\, ENCRYPTED\. |
| full_backup_interval | optional, dict, default=None. Body field fullBackupInterval\. |
| full_backup_interval.cron_expression | optional, str, default=None. Body field cronExpression\. |
| full_backup_interval.day_of_month | optional, int, default=None. Body field dayOfMonth\. |
| full_backup_interval.time_of_day | optional, str, default=None. Body field timeOfDay\. |
| full_backup_interval.type | optional, str, default=None. Body field type\. Possible values\; HOURLY\, DAILY\, WEEKLY\, MONTHLY\, CRON\. |
| full_backup_interval.weekday | optional, int, default=None. Body field weekday\. |
| full_backups_retention | optional, dict, default=None. Body field fullBackupsRetention\. |
| full_backups_retention.count | optional, int, default=None. Body field count\. |
| full_backups_retention.gfs_days | optional, int, default=None. Body field gfsDays\. |
| full_backups_retention.gfs_hours | optional, int, default=None. Body field gfsHours\. |
| full_backups_retention.gfs_months | optional, int, default=None. Body field gfsMonths\. |
| full_backups_retention.gfs_weeks | optional, int, default=None. Body field gfsWeeks\. |
| full_backups_retention.gfs_years | optional, int, default=None. Body field gfsYears\. |
| full_backups_retention.policy | optional, str, default=None. Body field policy\. Possible values\; LAST\_N\, GFS\. |
| id | optional, str, default=None. Database ID |
| incremental_backup_interval | optional, dict, default=None. Body field incrementalBackupInterval\. |
| incremental_backup_interval.cron_expression | optional, str, default=None. Body field cronExpression\. |
| incremental_backup_interval.day_of_month | optional, int, default=None. Body field dayOfMonth\. |
| incremental_backup_interval.time_of_day | optional, str, default=None. Body field timeOfDay\. |
| incremental_backup_interval.type | optional, str, default=None. Body field type\. Possible values\; HOURLY\, DAILY\, WEEKLY\, MONTHLY\, CRON\. |
| incremental_backup_interval.weekday | optional, int, default=None. Body field weekday\. |
| is_backups_enabled | optional, bool, default=None. Body field isBackupsEnabled\. |
| retention | optional, str, default=None. Body field retention\. Possible values\; CHAINS\, FULL\_BACKUPS\, CHAINS\_AND\_FULL\_BACKUPS\. |
| send_notifications_on | optional, list, default=None. Body field sendNotificationsOn\. Possible values\; BACKUP\_SUCCESS\, BACKUP\_FAILED\, CHAIN\_BROKEN\, WAL\_GAP\. |
| storage_id | optional, str, default=None. Body field storageId\. |
| wal_lag_threshold_bytes | optional, int, default=None. Body field walLagThresholdBytes\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.backup_config_physical:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        chains_retention: null

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.chains_retention | success, dict. Field chainsRetention\. |
| resource.chains_retention.count | success, int. Field count\. |
| resource.database_id | success, str. Field databaseId\. |
| resource.encryption | success, str. Field encryption\. |
| resource.full_backup_interval | success, dict. Field fullBackupInterval\. |
| resource.full_backup_interval.cron_expression | success, str. Field cronExpression\. |
| resource.full_backup_interval.day_of_month | success, int. Field dayOfMonth\. |
| resource.full_backup_interval.time_of_day | success, str. Field timeOfDay\. |
| resource.full_backup_interval.type | success, str. Field type\. |
| resource.full_backup_interval.weekday | success, int. Field weekday\. |
| resource.full_backups_retention | success, dict. Field fullBackupsRetention\. |
| resource.full_backups_retention.count | success, int. Field count\. |
| resource.full_backups_retention.gfs_days | success, int. Field gfsDays\. |
| resource.full_backups_retention.gfs_hours | success, int. Field gfsHours\. |
| resource.full_backups_retention.gfs_months | success, int. Field gfsMonths\. |
| resource.full_backups_retention.gfs_weeks | success, int. Field gfsWeeks\. |
| resource.full_backups_retention.gfs_years | success, int. Field gfsYears\. |
| resource.full_backups_retention.policy | success, str. Field policy\. |
| resource.incremental_backup_interval | success, dict. Field incrementalBackupInterval\. |
| resource.incremental_backup_interval.cron_expression | success, str. Field cronExpression\. |
| resource.incremental_backup_interval.day_of_month | success, int. Field dayOfMonth\. |
| resource.incremental_backup_interval.time_of_day | success, str. Field timeOfDay\. |
| resource.incremental_backup_interval.type | success, str. Field type\. |
| resource.incremental_backup_interval.weekday | success, int. Field weekday\. |
| resource.is_backups_enabled | success, bool. Field isBackupsEnabled\. |
| resource.retention | success, str. Field retention\. |
| resource.send_notifications_on | success, list. Field sendNotificationsOn\. |
| resource.storage | success, dict. Field storage\. |
| resource.storage.azure_blob_storage | success, dict. Field azureBlobStorage\. |
| resource.storage.azure_blob_storage.account_key | success, str. Field accountKey\. |
| resource.storage.azure_blob_storage.account_name | success, str. Field accountName\. |
| resource.storage.azure_blob_storage.auth_method | success, str. Field authMethod\. |
| resource.storage.azure_blob_storage.connection_string | success, str. Field connectionString\. |
| resource.storage.azure_blob_storage.container_name | success, str. Field containerName\. |
| resource.storage.azure_blob_storage.endpoint | success, str. Field endpoint\. |
| resource.storage.azure_blob_storage.prefix | success, str. Field prefix\. |
| resource.storage.azure_blob_storage.storage_id | success, str. Field storageId\. |
| resource.storage.ftp_storage | success, dict. Field ftpStorage\. |
| resource.storage.ftp_storage.host | success, str. Field host\. |
| resource.storage.ftp_storage.password | success, str. Field password\. |
| resource.storage.ftp_storage.path | success, str. Field path\. |
| resource.storage.ftp_storage.port | success, int. Field port\. |
| resource.storage.ftp_storage.skip_tls_verify | success, bool. Field skipTlsVerify\. |
| resource.storage.ftp_storage.storage_id | success, str. Field storageId\. |
| resource.storage.ftp_storage.use_ssl | success, bool. Field useSsl\. |
| resource.storage.ftp_storage.username | success, str. Field username\. |
| resource.storage.google_drive_storage | success, dict. Field googleDriveStorage\. |
| resource.storage.google_drive_storage.client_id | success, str. Field clientId\. |
| resource.storage.google_drive_storage.client_secret | success, str. Field clientSecret\. |
| resource.storage.google_drive_storage.storage_id | success, str. Field storageId\. |
| resource.storage.google_drive_storage.token_json | success, str. Field tokenJson\. |
| resource.storage.id | success, str. Field id\. |
| resource.storage.last_save_error | success, str. Field lastSaveError\. |
| resource.storage.local_storage | success, dict. specific storage |
| resource.storage.local_storage.storage_id | success, str. Field storageId\. |
| resource.storage.name | success, str. Field name\. |
| resource.storage.nas_storage | success, dict. Field nasStorage\. |
| resource.storage.nas_storage.domain | success, str. Field domain\. |
| resource.storage.nas_storage.host | success, str. Field host\. |
| resource.storage.nas_storage.password | success, str. Field password\. |
| resource.storage.nas_storage.path | success, str. Field path\. |
| resource.storage.nas_storage.port | success, int. Field port\. |
| resource.storage.nas_storage.share | success, str. Field share\. |
| resource.storage.nas_storage.storage_id | success, str. Field storageId\. |
| resource.storage.nas_storage.use_ssl | success, bool. Field useSsl\. |
| resource.storage.nas_storage.username | success, str. Field username\. |
| resource.storage.rclone_storage | success, dict. Field rcloneStorage\. |
| resource.storage.rclone_storage.config_content | success, str. Field configContent\. |
| resource.storage.rclone_storage.remote_path | success, str. Field remotePath\. |
| resource.storage.rclone_storage.storage_id | success, str. Field storageId\. |
| resource.storage.s3_storage | success, dict. Field s3Storage\. |
| resource.storage.s3_storage.s3_access_key | success, str. Field s3AccessKey\. |
| resource.storage.s3_storage.s3_bucket | success, str. Field s3Bucket\. |
| resource.storage.s3_storage.s3_endpoint | success, str. Field s3Endpoint\. |
| resource.storage.s3_storage.s3_prefix | success, str. Field s3Prefix\. |
| resource.storage.s3_storage.s3_region | success, str. Field s3Region\. |
| resource.storage.s3_storage.s3_secret_key | success, str. Field s3SecretKey\. |
| resource.storage.s3_storage.s3_storage_class | success, str. Field s3StorageClass\. |
| resource.storage.s3_storage.s3_use_virtual_hosted_style | success, bool. Field s3UseVirtualHostedStyle\. |
| resource.storage.s3_storage.skip_tlsverify | success, bool. Field skipTLSVerify\. |
| resource.storage.s3_storage.storage_id | success, str. Field storageId\. |
| resource.storage.sftp_storage | success, dict. Field sftpStorage\. |
| resource.storage.sftp_storage.host | success, str. Field host\. |
| resource.storage.sftp_storage.password | success, str. Field password\. |
| resource.storage.sftp_storage.path | success, str. Field path\. |
| resource.storage.sftp_storage.port | success, int. Field port\. |
| resource.storage.sftp_storage.private_key | success, str. Field privateKey\. |
| resource.storage.sftp_storage.skip_host_key_verify | success, bool. Field skipHostKeyVerify\. |
| resource.storage.sftp_storage.storage_id | success, str. Field storageId\. |
| resource.storage.sftp_storage.username | success, str. Field username\. |
| resource.storage.type | success, str. Field type\. |
| resource.storage.workspace_id | success, str. Field workspaceId\. |
| resource.storage_id | success, str. Field storageId\. |
| resource.wal_lag_threshold_bytes | success, int. Field walLagThresholdBytes\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

