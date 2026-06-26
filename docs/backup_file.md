# backup_file -- Manage backup\_file resources in Databasus\.

## Synopsis
Allows managing backup\_file resources using the Databasus API\.

This module is read\-only and does not support state\=absent\.



## Parameters

| parameter | comments |
|---|---|
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Backup ID |
| token | optional, str, default=None. Download token |


## Examples

```yaml
    
    - name: Query resource
      zeqk.databasus.backup_file:
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
