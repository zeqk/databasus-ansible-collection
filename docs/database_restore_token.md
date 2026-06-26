# database_restore_token -- Manage database\_restore\_token resources in Databasus\.

## Synopsis
Allows managing database\_restore\_token resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Database ID |
| target_time | optional, str, default=None. TargetTime is the PITR target\; omit for a restore to the latest available point\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.database_restore_token:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        target_time: null

```
