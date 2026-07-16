# verification -- Manage verification resources in Databasus\.

## Synopsis
Allows managing verification resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. Possible values\; present\, absent\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| name | True, str, default=None. Body field name\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.verification:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        name: example-name

    - name: Delete resource
      zeqk.databasus.verification:
        state: absent
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        name: example-name

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.agent_id | success, str. Field agentId\. |
| resource.attempt_count | success, int. Field attemptCount\. |
| resource.backup_id | success, str. Field backupId\. |
| resource.created_at | success, str. Field createdAt\. |
| resource.database_id | success, str. Field databaseId\. |
| resource.db_size_bytes_after_restore | success, int. Field dbSizeBytesAfterRestore\. |
| resource.fail_message | success, str. Field failMessage\. |
| resource.finished_at | success, str. Field finishedAt\. |
| resource.id | success, str. Field id\. |
| resource.pg_restore_exit_code | success, int. Field pgRestoreExitCode\. |
| resource.restore_duration_ms | success, int. Field restoreDurationMs\. |
| resource.schema_count | success, int. Field schemaCount\. |
| resource.started_at | success, str. Field startedAt\. |
| resource.status | success, str. Field status\. |
| resource.table_count | success, int. Field tableCount\. |
| resource.table_stats | success, list. Field tableStats\. |
| resource.table_stats.id | success, str. Field id\. |
| resource.table_stats.name | success, str. Field name\. |
| resource.table_stats.row_count | success, int. Field rowCount\. |
| resource.table_stats.schema_name | success, str. Field schemaName\. |

| resource.trigger | success, str. Field trigger\. |
| resource.verify_duration_ms | success, int. Field verifyDurationMs\. |

| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

