# notifier_is_using -- Manage notifier\_is\_using resources in Databasus\.

## Synopsis
Allows managing notifier\_is\_using resources using the Databasus API\.

This module is read\-only and does not support state\=absent\.

Uses \`\`GET /databases/notifier/\{id\}/is\-using\`\`\.



## Parameters

| parameter | comments |
|---|---|
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Notifier ID |


## Examples

```yaml
    
    - name: Query resource
      zeqk.databasus.notifier_is_using:
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

