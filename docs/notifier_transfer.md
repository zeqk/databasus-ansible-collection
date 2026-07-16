# notifier_transfer -- Manage notifier\_transfer resources in Databasus\.

## Synopsis
Allows managing notifier\_transfer resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. Possible values\; present\, absent\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Notifier ID |
| target_workspace_id | True, str, default=None. Body field targetWorkspaceId\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.notifier_transfer:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        target_workspace_id: null

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

