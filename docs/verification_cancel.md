# verification_cancel -- Manage verification\_cancel resources in Databasus\.

## Synopsis
Allows managing verification\_cancel resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Verification ID |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.verification_cancel:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
