# database -- Manage database resources in Databasus\.

## Synopsis
Allows managing database resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| health_status | optional, str, default=None. Body field healthStatus\. |
| id | True, str, default=None. Body field id\. |
| last_backup_error_message | optional, str, default=None. Body field lastBackupErrorMessage\. |
| last_backup_time | optional, str, default=None. these fields are not reliable\, but they are used for pretty UI |
| mariadb | optional, dict, default=None. Body field mariadb\. |
| mongodb | optional, dict, default=None. Body field mongodb\. |
| mysql | optional, dict, default=None. Body field mysql\. |
| name | optional, str, default=None. Body field name\. |
| notifiers | optional, list, default=None. Body field notifiers\. |
| postgresql_logical | optional, dict, default=None. Body field postgresqlLogical\. |
| postgresql_physical | optional, dict, default=None. Body field postgresqlPhysical\. |
| type | optional, str, default=None. Body field type\. |
| workspace_id | optional, str, default=None. Workspace ID |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.database:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        health_status: null

    - name: Delete resource
      zeqk.databasus.database:
        state: absent
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
