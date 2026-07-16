# audit_log -- Manage audit\_log resources in Databasus\.

## Synopsis
Allows managing audit\_log resources using the Databasus API\.

This module is read\-only and does not support state\=absent\.



## Parameters

| parameter | comments |
|---|---|
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| before_date | optional, str, default=None. Filter logs created before this date \(RFC3339 format\) |
| limit | optional, int, default=None. Limit number of results |
| offset | optional, int, default=None. Offset for pagination |
| user_id | optional, str, default=None. User ID |


## Examples

```yaml
    
    - name: Query resource
      zeqk.databasus.audit_log:
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.audit_logs | success, list. Field auditLogs\. |
| resource.audit_logs.created_at | success, str. Field createdAt\. |
| resource.audit_logs.id | success, str. Field id\. |
| resource.audit_logs.message | success, str. Field message\. |
| resource.audit_logs.user_email | success, str. Field userEmail\. |
| resource.audit_logs.user_id | success, str. Field userId\. |
| resource.audit_logs.user_name | success, str. Field userName\. |
| resource.audit_logs.workspace_id | success, str. Field workspaceId\. |
| resource.audit_logs.workspace_name | success, str. Field workspaceName\. |
| resource.limit | success, int. Field limit\. |
| resource.offset | success, int. Field offset\. |
| resource.total | success, int. Field total\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

