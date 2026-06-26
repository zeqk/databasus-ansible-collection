# database_backup -- Manage database\_backup resources in Databasus\.

## Synopsis
Allows managing database\_backup resources using the Databasus API\.

operationId references are included in generated operation constants\.

This module is read\-only and does not support state\=absent\.



## Parameters

| parameter | comments |
|---|---|
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| before_date | optional, str, default=None. Keep only backups created before this date \(RFC3339\) |
| id | optional, str, default=None. Database ID |
| limit | optional, int, default=None. Page size \(default 50\, max 1000\) |
| offset | optional, int, default=None. Offset for pagination |
| status | optional, list, default=None. Filter by status \- repeatable\, matches any \(e\.g\. COMPLETED\, IN\_PROGRESS\) |
| type | optional, list, default=None. Filter by backup type \- repeatable\, matches any |


## Examples

```yaml
    
    - name: Query resource
      zeqk.databasus.database_backup:
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
