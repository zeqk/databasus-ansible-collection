# auth -- Manage auth resources in Databasus\.

## Synopsis
Allows managing auth resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
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
