# membership_transfer_ownership -- Manage membership\_transfer\_ownership resources in Databasus\.

## Synopsis
Allows managing membership\_transfer\_ownership resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Workspace ID |
| new_owner_email | True, str, default=None. Body field newOwnerEmail\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.membership_transfer_ownership:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        new_owner_email: null

```
