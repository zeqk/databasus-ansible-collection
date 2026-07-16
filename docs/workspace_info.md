# workspace_info -- Gather information about workspace resources in Databasus\.

## Synopsis
Retrieves a workspace resource by name using Databasus list endpoints\.

This module is read\-only and never changes remote state\.



## Parameters

| parameter | comments |
|---|---|
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| name | True, str, default=None. Body field name\. |


## Examples

```yaml
    
    - name: Lookup workspace by name
      zeqk.databasus.workspace_info:
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        name: example-name

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.created_at | success, str. Field createdAt\. |
| resource.id | success, str. Field id\. |
| resource.name | success, str. Field name\. |
| found | always, bool. Whether a resource matching the requested name \(and scope\) was found\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

