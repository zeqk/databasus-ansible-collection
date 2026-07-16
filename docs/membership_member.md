# membership_member -- Manage membership\_member resources in Databasus\.

## Synopsis
Allows managing membership\_member resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. Possible values\; present\, absent\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| email | True, str, default=None. Body field email\. |
| id | optional, str, default=None. Workspace ID |
| role | True, str, default=None. Body field role\. Possible values\; WORKSPACE\_OWNER\, WORKSPACE\_ADMIN\, WORKSPACE\_MEMBER\, WORKSPACE\_VIEWER\. |
| user_id | optional, str, default=None. User ID |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.membership_member:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        email: null

    - name: Delete resource
      zeqk.databasus.membership_member:
        state: absent
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.status | success, str. Field status\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

