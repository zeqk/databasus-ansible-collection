# user -- Manage user resources in Databasus\.

## Synopsis
Allows managing user resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. Possible values\; present\, absent\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| before_date | optional, str, default=None. Filter users created before this date \(RFC3339 format\) |
| email | True, str, default=None. Body field email\. |
| id | optional, str, default=None. User ID |
| intended_workspace_id | optional, str, default=None. Body field intendedWorkspaceId\. |
| intended_workspace_role | optional, str, default=None. Body field intendedWorkspaceRole\. Possible values\; WORKSPACE\_OWNER\, WORKSPACE\_ADMIN\, WORKSPACE\_MEMBER\, WORKSPACE\_VIEWER\. |
| limit | optional, int, default=None. Number of items per page |
| offset | optional, int, default=None. Page offset |
| query | optional, str, default=None. Search by email or name \(case\-insensitive\) |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.user:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        email: null

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.created_at | success, str. Field createdAt\. |
| resource.email | success, str. Field email\. |
| resource.id | success, str. Field id\. |
| resource.is_active | success, bool. Field isActive\. |
| resource.name | success, str. Field name\. |
| resource.role | success, str. Field role\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

