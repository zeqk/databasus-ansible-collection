# backup_config -- Manage backup\_config resources in Databasus\.

## Synopsis
Allows managing backup\_config resources using the Databasus API\.

Uses \`\`GET /backup\-configs/database/\{id\}\`\`\.

Uses \`\`POST /backup\-configs/save\`\`\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. Possible values\; present\, absent\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| backup_interval | optional, dict, default=None. Body field backupInterval\. |
| backup_interval.cron_expression | optional, str, default=None. Body field cronExpression\. |
| backup_interval.day_of_month | optional, int, default=None. Body field dayOfMonth\. |
| backup_interval.time_of_day | optional, str, default=None. Body field timeOfDay\. |
| backup_interval.type | optional, str, default=None. Body field type\. Possible values\; HOURLY\, DAILY\, WEEKLY\, MONTHLY\, CRON\. |
| backup_interval.weekday | optional, int, default=None. Body field weekday\. |
| database_id | optional, str, default=None. Body field databaseId\. |
| encryption | optional, str, default=None. Body field encryption\. Possible values\; NONE\, ENCRYPTED\. |
| id | optional, str, default=None. Database ID |
| is_backups_enabled | optional, bool, default=None. Body field isBackupsEnabled\. |
| is_retry_if_failed | optional, bool, default=None. Body field isRetryIfFailed\. |
| max_failed_tries_count | optional, int, default=None. Body field maxFailedTriesCount\. |
| retention_count | optional, int, default=None. Body field retentionCount\. |
| retention_gfs_days | optional, int, default=None. Body field retentionGfsDays\. |
| retention_gfs_hours | optional, int, default=None. Body field retentionGfsHours\. |
| retention_gfs_months | optional, int, default=None. Body field retentionGfsMonths\. |
| retention_gfs_weeks | optional, int, default=None. Body field retentionGfsWeeks\. |
| retention_gfs_years | optional, int, default=None. Body field retentionGfsYears\. |
| retention_policy_type | optional, str, default=None. Body field retentionPolicyType\. Possible values\; TIME\_PERIOD\, COUNT\, GFS\. |
| retention_time_period | optional, str, default=None. Body field retentionTimePeriod\. Possible values\; DAY\, WEEK\, MONTH\, 3\_MONTH\, 6\_MONTH\, YEAR\, 2\_YEARS\, 3\_YEARS\, 4\_YEARS\, 5\_YEARS\, FOREVER\. |
| send_notifications_on | optional, list, default=None. Body field sendNotificationsOn\. Possible values\; BACKUP\_FAILED\, BACKUP\_SUCCESS\. |
| storage | optional, dict, default=None. Body field storage\. |
| storage.azure_blob_storage | optional, dict, default=None. Body field azureBlobStorage\. |
| storage.azure_blob_storage.account_key | optional, str, default=None. Body field accountKey\. |
| storage.azure_blob_storage.account_name | optional, str, default=None. Body field accountName\. |
| storage.azure_blob_storage.auth_method | optional, str, default=None. Body field authMethod\. Possible values\; CONNECTION\_STRING\, ACCOUNT\_KEY\. |
| storage.azure_blob_storage.connection_string | optional, str, default=None. Body field connectionString\. |
| storage.azure_blob_storage.container_name | optional, str, default=None. Body field containerName\. |
| storage.azure_blob_storage.endpoint | optional, str, default=None. Body field endpoint\. |
| storage.azure_blob_storage.prefix | optional, str, default=None. Body field prefix\. |
| storage.azure_blob_storage.storage_id | optional, str, default=None. Body field storageId\. |
| storage.ftp_storage | optional, dict, default=None. Body field ftpStorage\. |
| storage.ftp_storage.host | optional, str, default=None. Body field host\. |
| storage.ftp_storage.password | optional, str, default=None. Body field password\. |
| storage.ftp_storage.path | optional, str, default=None. Body field path\. |
| storage.ftp_storage.port | optional, int, default=None. Body field port\. |
| storage.ftp_storage.skip_tls_verify | optional, bool, default=None. Body field skipTlsVerify\. |
| storage.ftp_storage.storage_id | optional, str, default=None. Body field storageId\. |
| storage.ftp_storage.use_ssl | optional, bool, default=None. Body field useSsl\. |
| storage.ftp_storage.username | optional, str, default=None. Body field username\. |
| storage.google_drive_storage | optional, dict, default=None. Body field googleDriveStorage\. |
| storage.google_drive_storage.client_id | optional, str, default=None. Body field clientId\. |
| storage.google_drive_storage.client_secret | optional, str, default=None. Body field clientSecret\. |
| storage.google_drive_storage.storage_id | optional, str, default=None. Body field storageId\. |
| storage.google_drive_storage.token_json | optional, str, default=None. Body field tokenJson\. |
| storage.id | optional, str, default=None. Body field id\. |
| storage.last_save_error | optional, str, default=None. Body field lastSaveError\. |
| storage.local_storage | optional, dict, default=None. specific storage |
| storage.local_storage.storage_id | optional, str, default=None. Body field storageId\. |
| storage.name | optional, str, default=None. Body field name\. |
| storage.nas_storage | optional, dict, default=None. Body field nasStorage\. |
| storage.nas_storage.domain | optional, str, default=None. Body field domain\. |
| storage.nas_storage.host | optional, str, default=None. Body field host\. |
| storage.nas_storage.password | optional, str, default=None. Body field password\. |
| storage.nas_storage.path | optional, str, default=None. Body field path\. |
| storage.nas_storage.port | optional, int, default=None. Body field port\. |
| storage.nas_storage.share | optional, str, default=None. Body field share\. |
| storage.nas_storage.storage_id | optional, str, default=None. Body field storageId\. |
| storage.nas_storage.use_ssl | optional, bool, default=None. Body field useSsl\. |
| storage.nas_storage.username | optional, str, default=None. Body field username\. |
| storage.rclone_storage | optional, dict, default=None. Body field rcloneStorage\. |
| storage.rclone_storage.config_content | optional, str, default=None. Body field configContent\. |
| storage.rclone_storage.remote_path | optional, str, default=None. Body field remotePath\. |
| storage.rclone_storage.storage_id | optional, str, default=None. Body field storageId\. |
| storage.s3_storage | optional, dict, default=None. Body field s3Storage\. |
| storage.s3_storage.s3_access_key | optional, str, default=None. Body field s3AccessKey\. |
| storage.s3_storage.s3_bucket | optional, str, default=None. Body field s3Bucket\. |
| storage.s3_storage.s3_endpoint | optional, str, default=None. Body field s3Endpoint\. |
| storage.s3_storage.s3_prefix | optional, str, default=None. Body field s3Prefix\. |
| storage.s3_storage.s3_region | optional, str, default=None. Body field s3Region\. |
| storage.s3_storage.s3_secret_key | optional, str, default=None. Body field s3SecretKey\. |
| storage.s3_storage.s3_storage_class | optional, str, default=None. Body field s3StorageClass\. Possible values\; \, STANDARD\, STANDARD\_IA\, ONEZONE\_IA\, INTELLIGENT\_TIERING\, REDUCED\_REDUNDANCY\, GLACIER\_IR\. |
| storage.s3_storage.s3_use_virtual_hosted_style | optional, bool, default=None. Body field s3UseVirtualHostedStyle\. |
| storage.s3_storage.skip_tlsverify | optional, bool, default=None. Body field skipTLSVerify\. |
| storage.s3_storage.storage_id | optional, str, default=None. Body field storageId\. |
| storage.sftp_storage | optional, dict, default=None. Body field sftpStorage\. |
| storage.sftp_storage.host | optional, str, default=None. Body field host\. |
| storage.sftp_storage.password | optional, str, default=None. Body field password\. |
| storage.sftp_storage.path | optional, str, default=None. Body field path\. |
| storage.sftp_storage.port | optional, int, default=None. Body field port\. |
| storage.sftp_storage.private_key | optional, str, default=None. Body field privateKey\. |
| storage.sftp_storage.skip_host_key_verify | optional, bool, default=None. Body field skipHostKeyVerify\. |
| storage.sftp_storage.storage_id | optional, str, default=None. Body field storageId\. |
| storage.sftp_storage.username | optional, str, default=None. Body field username\. |
| storage.type | optional, str, default=None. Body field type\. Possible values\; LOCAL\, S3\, GOOGLE\_DRIVE\, NAS\, AZURE\_BLOB\, FTP\, SFTP\, RCLONE\. |
| storage.workspace_id | optional, str, default=None. Body field workspaceId\. |
| storage_id | optional, str, default=None. Body field storageId\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.backup_config:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        backup_interval: null

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.backup_interval | success, dict. Field backupInterval\. |
| resource.backup_interval.cron_expression | success, str. Field cronExpression\. |
| resource.backup_interval.day_of_month | success, int. Field dayOfMonth\. |
| resource.backup_interval.time_of_day | success, str. Field timeOfDay\. |
| resource.backup_interval.type | success, str. Field type\. |
| resource.backup_interval.weekday | success, int. Field weekday\. |
| resource.database_id | success, str. Field databaseId\. |
| resource.encryption | success, str. Field encryption\. |
| resource.is_backups_enabled | success, bool. Field isBackupsEnabled\. |
| resource.is_retry_if_failed | success, bool. Field isRetryIfFailed\. |
| resource.max_failed_tries_count | success, int. Field maxFailedTriesCount\. |
| resource.retention_count | success, int. Field retentionCount\. |
| resource.retention_gfs_days | success, int. Field retentionGfsDays\. |
| resource.retention_gfs_hours | success, int. Field retentionGfsHours\. |
| resource.retention_gfs_months | success, int. Field retentionGfsMonths\. |
| resource.retention_gfs_weeks | success, int. Field retentionGfsWeeks\. |
| resource.retention_gfs_years | success, int. Field retentionGfsYears\. |
| resource.retention_policy_type | success, str. Field retentionPolicyType\. |
| resource.retention_time_period | success, str. Field retentionTimePeriod\. |
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
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

