# workspace -- Manage workspace resources in Databasus\.

## Synopsis
Allows managing workspace resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| created_at | optional, str, default=None. Body field createdAt\. |
| id | True, str, default=None. Workspace ID |
| name | optional, str, default=None. Body field name\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.workspace:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        created_at: null

    - name: Delete resource
      zeqk.databasus.workspace:
        state: absent
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
