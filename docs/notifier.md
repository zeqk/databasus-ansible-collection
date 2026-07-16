# notifier -- Manage notifier resources in Databasus\.

## Synopsis
Allows managing notifier resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. Possible values\; present\, absent\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| discord_notifier | optional, dict, default=None. Body field discordNotifier\. |
| discord_notifier.channel_webhook_url | optional, str, default=None. Body field channelWebhookUrl\. |
| discord_notifier.notifier_id | optional, str, default=None. Body field notifierId\. |
| email_notifier | optional, dict, default=None. Body field emailNotifier\. |
| email_notifier.from | optional, str, default=None. Body field from\. |
| email_notifier.is_insecure_skip_verify | optional, bool, default=None. Body field isInsecureSkipVerify\. |
| email_notifier.notifier_id | optional, str, default=None. Body field notifierId\. |
| email_notifier.smtp_host | optional, str, default=None. Body field smtpHost\. |
| email_notifier.smtp_password | optional, str, default=None. Body field smtpPassword\. |
| email_notifier.smtp_port | optional, int, default=None. Body field smtpPort\. |
| email_notifier.smtp_user | optional, str, default=None. Body field smtpUser\. |
| email_notifier.target_email | optional, str, default=None. Body field targetEmail\. |
| last_send_error | optional, str, default=None. Body field lastSendError\. |
| name | True, str, default=None. Body field name\. |
| notifier_type | optional, str, default=None. Body field notifierType\. Possible values\; EMAIL\, TELEGRAM\, WEBHOOK\, SLACK\, DISCORD\, TEAMS\. |
| slack_notifier | optional, dict, default=None. Body field slackNotifier\. |
| slack_notifier.bot_token | optional, str, default=None. Body field botToken\. |
| slack_notifier.notifier_id | optional, str, default=None. Body field notifierId\. |
| slack_notifier.target_chat_id | optional, str, default=None. Body field targetChatId\. |
| teams_notifier | optional, dict, default=None. Body field teamsNotifier\. |
| teams_notifier.notifier_id | optional, str, default=None. Body field notifierId\. |
| teams_notifier.power_automate_url | optional, str, default=None. Body field powerAutomateUrl\. |
| telegram_notifier | optional, dict, default=None. specific notifier |
| telegram_notifier.bot_token | optional, str, default=None. Body field botToken\. |
| telegram_notifier.is_proxy_enabled | optional, bool, default=None. Body field isProxyEnabled\. |
| telegram_notifier.notifier_id | optional, str, default=None. Body field notifierId\. |
| telegram_notifier.proxy_url | optional, str, default=None. Body field proxyUrl\. |
| telegram_notifier.target_chat_id | optional, str, default=None. Body field targetChatId\. |
| telegram_notifier.thread_id | optional, int, default=None. Body field threadId\. |
| webhook_notifier | optional, dict, default=None. Body field webhookNotifier\. |
| webhook_notifier.body_template | optional, str, default=None. Body field bodyTemplate\. |
| webhook_notifier.headers | optional, list, default=None. Body field headers\. |
| webhook_notifier.headers.key | optional, str, default=None. Body field key\. |
| webhook_notifier.headers.value | optional, str, default=None. Body field value\. |
| webhook_notifier.notifier_id | optional, str, default=None. Body field notifierId\. |
| webhook_notifier.webhook_method | optional, str, default=None. Body field webhookMethod\. Possible values\; POST\, GET\. |
| webhook_notifier.webhook_url | optional, str, default=None. Body field webhookUrl\. |
| workspace_id | optional, str, default=None. Workspace ID |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.notifier:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        name: example-name
        discord_notifier: null

    - name: Delete resource
      zeqk.databasus.notifier:
        state: absent
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        name: example-name

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.discord_notifier | success, dict. Field discordNotifier\. |
| resource.discord_notifier.channel_webhook_url | success, str. Field channelWebhookUrl\. |
| resource.discord_notifier.notifier_id | success, str. Field notifierId\. |
| resource.email_notifier | success, dict. Field emailNotifier\. |
| resource.email_notifier.from | success, str. Field from\. |
| resource.email_notifier.is_insecure_skip_verify | success, bool. Field isInsecureSkipVerify\. |
| resource.email_notifier.notifier_id | success, str. Field notifierId\. |
| resource.email_notifier.smtp_host | success, str. Field smtpHost\. |
| resource.email_notifier.smtp_password | success, str. Field smtpPassword\. |
| resource.email_notifier.smtp_port | success, int. Field smtpPort\. |
| resource.email_notifier.smtp_user | success, str. Field smtpUser\. |
| resource.email_notifier.target_email | success, str. Field targetEmail\. |
| resource.id | success, str. Field id\. |
| resource.last_send_error | success, str. Field lastSendError\. |
| resource.name | success, str. Field name\. |
| resource.notifier_type | success, str. Field notifierType\. |
| resource.slack_notifier | success, dict. Field slackNotifier\. |
| resource.slack_notifier.bot_token | success, str. Field botToken\. |
| resource.slack_notifier.notifier_id | success, str. Field notifierId\. |
| resource.slack_notifier.target_chat_id | success, str. Field targetChatId\. |
| resource.teams_notifier | success, dict. Field teamsNotifier\. |
| resource.teams_notifier.notifier_id | success, str. Field notifierId\. |
| resource.teams_notifier.power_automate_url | success, str. Field powerAutomateUrl\. |
| resource.telegram_notifier | success, dict. specific notifier |
| resource.telegram_notifier.bot_token | success, str. Field botToken\. |
| resource.telegram_notifier.is_proxy_enabled | success, bool. Field isProxyEnabled\. |
| resource.telegram_notifier.notifier_id | success, str. Field notifierId\. |
| resource.telegram_notifier.proxy_url | success, str. Field proxyUrl\. |
| resource.telegram_notifier.target_chat_id | success, str. Field targetChatId\. |
| resource.telegram_notifier.thread_id | success, int. Field threadId\. |
| resource.webhook_notifier | success, dict. Field webhookNotifier\. |
| resource.webhook_notifier.body_template | success, str. Field bodyTemplate\. |
| resource.webhook_notifier.headers | success, list. Field headers\. |
| resource.webhook_notifier.headers.key | success, str. Field key\. |
| resource.webhook_notifier.headers.value | success, str. Field value\. |
| resource.webhook_notifier.notifier_id | success, str. Field notifierId\. |
| resource.webhook_notifier.webhook_method | success, str. Field webhookMethod\. |
| resource.webhook_notifier.webhook_url | success, str. Field webhookUrl\. |
| resource.workspace_id | success, str. Field workspaceId\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

