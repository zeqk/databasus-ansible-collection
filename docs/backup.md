# backup -- Manage backup resources in Databasus\.

## Synopsis
Allows managing backup resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| before_date | optional, str, default=None. Filter backups created before this date \(RFC3339\) |
| database_id | optional, str, default=None. Database ID |
| id | optional, str, default=None. Backup ID |
| limit | optional, int, default=None. Number of items per page |
| offset | optional, int, default=None. Offset for pagination |
| pg_wal_backup_type | optional, str, default=None. Filter by WAL backup type |
| status | optional, list, default=None. Filter by backup status \(can be repeated\) |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.backup:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

    - name: Delete resource
      zeqk.databasus.backup:
        state: absent
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
