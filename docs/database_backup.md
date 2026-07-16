# database_backup -- Manage database\_backup resources in Databasus\.

## Synopsis
Allows managing database\_backup resources using the Databasus API\.

operationId references are included in generated operation constants\.

This module is read\-only and does not support state\=absent\.

Uses \`\`GET /backups/physical/database/\{id\}/backups\`\`\.



## Parameters

| parameter | comments |
|---|---|
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| before_date | optional, str, default=None. Keep only backups created before this date \(RFC3339\) |
| id | optional, str, default=None. Database ID |
| limit | optional, int, default=None. Page size \(default 50\, max 1000\) |
| offset | optional, int, default=None. Offset for pagination |
| status | optional, list, default=None. Filter by status \- repeatable\, matches any \(e\.g\. COMPLETED\, IN\_PROGRESS\) |
| type | optional, list, default=None. Filter by backup type \- repeatable\, matches any Possible values\; FULL\, INCREMENTAL\, WAL\. |


## Examples

```yaml
    
    - name: Query resource
      zeqk.databasus.database_backup:
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.completed_at | success, str. Field completedAt\. |
| resource.created_at | success, str. Field createdAt\. |
| resource.fail_message | success, str. FailMessage is the human\-readable failure detail\, ERROR / CHAIN\_BROKEN rows only\. |
| resource.id | success, str. Field id\. |
| resource.parent_incremental_backup_id | success, str. Field parentIncrementalBackupId\. |
| resource.root_full_backup_id | success, str. Chain links\, incremental rows only\. |
| resource.size_mb | success, float. Field sizeMb\. |
| resource.start_lsn | success, str. Field startLsn\. |
| resource.status | success, str. Field status\. |
| resource.stop_lsn | success, str. Field stopLsn\. |
| resource.timeline_id | success, int. Field timelineId\. |
| resource.type | success, str. Field type\. |
| resource.wal_filename | success, str. WalFilename is the bare PG segment name\, WAL rows only\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

