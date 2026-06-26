# notifier -- Manage notifier resources in Databasus\.

## Synopsis
Allows managing notifier resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| discord_notifier | optional, dict, default=None. Body field discordNotifier\. |
| email_notifier | optional, dict, default=None. Body field emailNotifier\. |
| id | True, str, default=None. Body field id\. |
| last_send_error | optional, str, default=None. Body field lastSendError\. |
| name | optional, str, default=None. Body field name\. |
| notifier_type | optional, str, default=None. Body field notifierType\. |
| slack_notifier | optional, dict, default=None. Body field slackNotifier\. |
| teams_notifier | optional, dict, default=None. Body field teamsNotifier\. |
| telegram_notifier | optional, dict, default=None. Body field telegramNotifier\. |
| webhook_notifier | optional, dict, default=None. Body field webhookNotifier\. |
| workspace_id | optional, str, default=None. Workspace ID |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.notifier:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        discord_notifier: null

    - name: Delete resource
      zeqk.databasus.notifier:
        state: absent
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
