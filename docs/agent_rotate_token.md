# agent_rotate_token -- Manage agent\_rotate\_token resources in Databasus\.

## Synopsis
Allows managing agent\_rotate\_token resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
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
