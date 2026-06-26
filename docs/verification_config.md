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
| database_id | True, str, default=None. Database ID |
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
