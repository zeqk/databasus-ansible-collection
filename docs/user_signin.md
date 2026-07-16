# user_signin -- Authenticate a user and obtain a Databasus token\.

## Synopsis
Performs user login against the Databasus API\.

Uses a public endpoint and does not require an existing bearer token\.

This module is read\-only and never changes remote state\.

Uses \`\`POST /users/signin\`\`\.



## Parameters

| parameter | comments |
|---|---|
| api_url | True, str, default=None. Base API URL\. |
| cloudflare_turnstile_token | optional, str, default=None. Body field cloudflareTurnstileToken\. |
| email | True, str, default=None. Body field email\. |
| password | True, str, default=None. Body field password\. |


## Examples

```yaml
    
    - name: Sign in and retrieve JWT token
      zeqk.databasus.user_signin:
        api_url: https://api.example.com
        email: user@example.com
        password: "{{ databasus_password }}"

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Response object as returned by the API\. |
| resource.email | success, str. Field email\. |
| resource.token | success, str. Field token\. |
| resource.user_id | success, str. Field userId\. |
| token | when available, str. JWT token returned by the signin endpoint\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

