# backup_config -- Manage backup\_config resources in Databasus\.

## Synopsis
Allows managing backup\_config resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| backup_interval | optional, dict, default=None. Body field backupInterval\. |
| database_id | optional, str, default=None. Body field databaseId\. |
| encryption | optional, str, default=None. Body field encryption\. |
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
| retention_policy_type | optional, str, default=None. Body field retentionPolicyType\. |
| retention_time_period | optional, str, default=None. Body field retentionTimePeriod\. |
| send_notifications_on | optional, list, default=None. Body field sendNotificationsOn\. |
| storage | optional, dict, default=None. Body field storage\. |
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
