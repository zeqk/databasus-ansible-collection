# workspace -- Manage workspace resources in Databasus\.

## Synopsis
Allows managing workspace resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. Possible values\; present\, absent\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| created_at | optional, str, default=None. Body field createdAt\. |
| name | True, str, default=None. Body field name\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.workspace:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        name: example-name
        created_at: null

    - name: Delete resource
      zeqk.databasus.workspace:
        state: absent
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

| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

