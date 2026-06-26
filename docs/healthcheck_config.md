# healthcheck_config -- Manage healthcheck\_config resources in Databasus\.

## Synopsis
Allows managing healthcheck\_config resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| attempts_before_concidered_as_down | optional, int, default=None. Body field attemptsBeforeConcideredAsDown\. |
| database_id | True, str, default=None. Body field databaseId\. |
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
