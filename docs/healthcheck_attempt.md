# healthcheck_attempt -- Manage healthcheck\_attempt resources in Databasus\.

## Synopsis
Allows managing healthcheck\_attempt resources using the Databasus API\.

This module is read\-only and does not support state\=absent\.



## Parameters

| parameter | comments |
|---|---|
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| after_date | optional, str, default=None. After date \(RFC3339 format\) |
| database_id | optional, str, default=None. Database ID |


## Examples

```yaml
    
    - name: Query resource
      zeqk.databasus.healthcheck_attempt:
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
