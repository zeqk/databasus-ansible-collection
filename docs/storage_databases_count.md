# storage_databases_count -- Manage storage\_databases\_count resources in Databasus\.

## Synopsis
Allows managing storage\_databases\_count resources using the Databasus API\.

This module is read\-only and does not support state\=absent\.



## Parameters

| parameter | comments |
|---|---|
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Storage ID |


## Examples

```yaml
    
    - name: Query resource
      zeqk.databasus.storage_databases_count:
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
