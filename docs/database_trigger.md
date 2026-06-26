# database_trigger -- Manage database\_trigger resources in Databasus\.

## Synopsis
Allows managing database\_trigger resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Database ID |
| type | True, dict, default=None. Body field type\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.database_trigger:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        type: null

```
