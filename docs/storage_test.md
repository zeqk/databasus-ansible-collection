# storage_test -- Manage storage\_test resources in Databasus\.

## Synopsis
Allows managing storage\_test resources using the Databasus API\.

Uses \`\`POST /storages/\{id\}/test\`\`\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. Possible values\; present\, absent\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Storage ID |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.storage_test:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

