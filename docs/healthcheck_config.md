# healthcheck_config -- Manage healthcheck\_config resources in Databasus\.

## Synopsis
Allows managing healthcheck\_config resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. Possible values\; present\, absent\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| attempts_before_concidered_as_down | optional, int, default=None. Body field attemptsBeforeConcideredAsDown\. |
| database_id | optional, str, default=None. Body field databaseId\. |
| interval_minutes | optional, int, default=None. Body field intervalMinutes\. |
| is_healthcheck_enabled | optional, bool, default=None. Body field isHealthcheckEnabled\. |
| is_sent_notification_when_unavailable | optional, bool, default=None. Body field isSentNotificationWhenUnavailable\. |
| store_attempts_days | optional, int, default=None. Body field storeAttemptsDays\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.healthcheck_config:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        attempts_before_concidered_as_down: null

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.attempts_before_concidered_as_down | success, int. Field attemptsBeforeConcideredAsDown\. |
| resource.database_id | success, str. Field databaseId\. |
| resource.interval_minutes | success, int. Field intervalMinutes\. |
| resource.is_healthcheck_enabled | success, bool. Field isHealthcheckEnabled\. |
| resource.is_sent_notification_when_unavailable | success, bool. Field isSentNotificationWhenUnavailable\. |
| resource.store_attempts_days | success, int. Field storeAttemptsDays\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

