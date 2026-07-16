# auth -- Manage auth resources in Databasus\.

## Synopsis
Allows managing auth resources using the Databasus API\.

Uses \`\`POST /auth/github/callback\`\`\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. Possible values\; present\, absent\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| code | True, str, default=None. Body field code\. |
| redirect_uri | True, str, default=None. Body field redirectUri\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.auth:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        code: null

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.email | success, str. Field email\. |
| resource.is_new_user | success, bool. Field isNewUser\. |
| resource.token | success, str. Field token\. |
| resource.user_id | success, str. Field userId\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

