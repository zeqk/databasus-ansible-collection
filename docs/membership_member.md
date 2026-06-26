# membership_member -- Manage membership\_member resources in Databasus\.

## Synopsis
Allows managing membership\_member resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| email | True, str, default=None. Body field email\. |
| id | True, str, default=None. Workspace ID |
| role | True, str, default=None. Body field role\. |
| user_id | optional, str, default=None. User ID |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.membership_member:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        email: null

    - name: Delete resource
      zeqk.databasus.membership_member:
        state: absent
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
