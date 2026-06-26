# audit_log -- Manage audit\_log resources in Databasus\.

## Synopsis
Allows managing audit\_log resources using the Databasus API\.

This module is read\-only and does not support state\=absent\.



## Parameters

| parameter | comments |
|---|---|
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| before_date | optional, str, default=None. Filter logs created before this date \(RFC3339 format\) |
| limit | optional, int, default=None. Limit number of results |
| offset | optional, int, default=None. Offset for pagination |
| user_id | optional, str, default=None. User ID |


## Examples

```yaml
    
    - name: Query resource
      zeqk.databasus.audit_log:
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
