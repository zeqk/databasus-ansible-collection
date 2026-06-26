# restore_restore -- Manage restore\_restore resources in Databasus\.

## Synopsis
Allows managing restore\_restore resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| backup_id | optional, str, default=None. Backup ID |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.restore_restore:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
