# agent_rotate_token -- Manage agent\_rotate\_token resources in Databasus\.

## Synopsis
Allows managing agent\_rotate\_token resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. Possible values\; present\, absent\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Agent ID |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.agent_rotate_token:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.token | success, str. Field token\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

