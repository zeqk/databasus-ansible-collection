# backup -- Manage backup resources in Databasus\.

## Synopsis
Allows managing backup resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| before_date | optional, str, default=None. Filter backups created before this date \(RFC3339\) |
| database_id | optional, str, default=None. Database ID |
| id | optional, str, default=None. Backup ID |
| limit | optional, int, default=None. Number of items per page |
| offset | optional, int, default=None. Offset for pagination |
| pg_wal_backup_type | optional, str, default=None. Filter by WAL backup type |
| status | optional, list, default=None. Filter by backup status \(can be repeated\) |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.backup:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

    - name: Delete resource
      zeqk.databasus.backup:
        state: absent
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.backup_duration_ms | success, int. Field backupDurationMs\. |
| resource.backup_raw_db_size_mb | success, float. Field backupRawDbSizeMb\. |
| resource.backup_size_mb | success, float. Field backupSizeMb\. |
| resource.created_at | success, str. Field createdAt\. |
| resource.database_id | success, str. Field databaseId\. |
| resource.encryption | success, str. Field encryption\. |
| resource.fail_message | success, str. Field failMessage\. |
| resource.file_name | success, str. Field fileName\. |
| resource.id | success, str. Field id\. |
| resource.is_skip_retry | success, bool. Field isSkipRetry\. |
| resource.restore_verification_status | success, str. Field restoreVerificationStatus\. |
| resource.status | success, str. Field status\. |
| resource.storage_id | success, str. Field storageId\. |
| resource.timescaledb_version | success, str. TimescaledbVersion is the source\'s timescaledb extension version captured at backup time\, or \"\" when the source has no timescaledb\. Non\-empty marks the backup as needing the TimescaleDB restore procedure\, and the verification agent uses the exact version to pull a matching engine image \(pg\_restore cannot cross extension versions\)\. |

| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

