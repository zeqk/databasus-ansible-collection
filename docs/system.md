# system -- Manage system resources in Databasus\.

## Synopsis
Allows managing system resources using the Databasus API\.

This module is read\-only and does not support state\=absent\.



## Parameters

| parameter | comments |
|---|---|
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |


## Examples

```yaml
    
    - name: Query resource
      zeqk.databasus.system:
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
