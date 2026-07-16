# membership_transfer_ownership -- Manage membership\_transfer\_ownership resources in Databasus\.

## Synopsis
Allows managing membership\_transfer\_ownership resources using the Databasus API\.

Uses \`\`POST /workspaces/memberships/\{id\}/transfer\-ownership\`\`\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. Possible values\; present\, absent\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Workspace ID |
| new_owner_email | True, str, default=None. Body field newOwnerEmail\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.membership_transfer_ownership:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        new_owner_email: null

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

