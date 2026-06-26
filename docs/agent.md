# agent -- Manage agent resources in Databasus\.

## Synopsis
Allows managing agent resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| agent_id | True, str, default=None. Agent UUID |
| db_size_bytes_after_restore | optional, int, default=None. Body field dbSizeBytesAfterRestore\. |
| fail_message | optional, str, default=None. Body field failMessage\. |
| failure_kind | optional, str, default=None. Body field failureKind\. |
| id | True, str, default=None. Verification UUID |
| pg_restore_exit_code | optional, int, default=None. Body field pgRestoreExitCode\. |
| restore_duration_ms | optional, int, default=None. Body field restoreDurationMs\. |
| schema_count | optional, int, default=None. Body field schemaCount\. |
| status | True, dict, default=None. Body field status\. |
| table_count | optional, int, default=None. Body field tableCount\. |
| table_stats | optional, list, default=None. Body field tableStats\. |
| verify_duration_ms | optional, int, default=None. Body field verifyDurationMs\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.agent:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        db_size_bytes_after_restore: null

```
