# backup_restore_token -- Manage backup\_restore\_token resources in Databasus\.

## Synopsis
Allows managing backup\_restore\_token resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| backup_id | optional, str, default=None. Backup ID \(FULL or incremental\) |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.backup_restore_token:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
