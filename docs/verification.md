# verification -- Manage verification resources in Databasus\.

## Synopsis
Allows managing verification resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Agent ID |
| name | True, str, default=None. Body field name\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.verification:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        name: null

    - name: Delete resource
      zeqk.databasus.verification:
        state: absent
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

