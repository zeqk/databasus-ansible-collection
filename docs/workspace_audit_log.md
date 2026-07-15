# workspace_audit_log -- Manage workspace\_audit\_log resources in Databasus\.

## Synopsis
Allows managing workspace\_audit\_log resources using the Databasus API\.

This module is read\-only and does not support state\=absent\.



## Parameters

| parameter | comments |
|---|---|
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| before_date | optional, str, default=None. Filter logs created before this date \(RFC3339 format\) |
| id | optional, str, default=None. Workspace ID |
| limit | optional, int, default=None. Limit number of results |
| offset | optional, int, default=None. Offset for pagination |


## Examples

```yaml
    
    - name: Query resource
      zeqk.databasus.workspace_audit_log:
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.created_at | success, str. Field createdAt\. |
| resource.id | success, str. Field id\. |
| resource.message | success, str. Field message\. |
| resource.user_email | success, str. Field userEmail\. |
| resource.user_id | success, str. Field userId\. |
| resource.user_name | success, str. Field userName\. |
| resource.workspace_id | success, str. Field workspaceId\. |
| resource.workspace_name | success, str. Field workspaceName\. |

| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

