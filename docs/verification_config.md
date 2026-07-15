# verification_config -- Manage verification\_config resources in Databasus\.

## Synopsis
Allows managing verification\_config resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| database_id | optional, str, default=None. Database ID |
| is_scheduled_verification_enabled | optional, bool, default=None. Body field isScheduledVerificationEnabled\. |
| schedule_type | optional, str, default=None. Body field scheduleType\. |
| send_notifications_on | optional, list, default=None. Body field sendNotificationsOn\. |
| verification_interval | optional, dict, default=None. Body field verificationInterval\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.verification_config:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        is_scheduled_verification_enabled: null

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.created_at | success, str. Field createdAt\. |
| resource.database_id | success, str. Field databaseId\. |
| resource.is_scheduled_verification_enabled | success, bool. Field isScheduledVerificationEnabled\. |
| resource.schedule_type | success, str. Field scheduleType\. |
| resource.send_notifications_on | success, list. Field sendNotificationsOn\. |
| resource.updated_at | success, str. Field updatedAt\. |
| resource.verification_interval | success, dict. Field verificationInterval\. |
| resource.verification_interval.cron_expression | success, str. Field cronExpression\. |
| resource.verification_interval.day_of_month | success, int. Field dayOfMonth\. |
| resource.verification_interval.time_of_day | success, str. Field timeOfDay\. |
| resource.verification_interval.type | success, str. Field type\. |
| resource.verification_interval.weekday | success, int. Field weekday\. |


| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

