# backup_cancel -- Manage backup\_cancel resources in Databasus\.

## Synopsis
Allows managing backup\_cancel resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Backup ID |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.backup_cancel:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
