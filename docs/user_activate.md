# user_activate -- Manage user\_activate resources in Databasus\.

## Synopsis
Allows managing user\_activate resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. User ID |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.user_activate:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
