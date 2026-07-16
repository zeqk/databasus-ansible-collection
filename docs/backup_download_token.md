# backup_download_token -- Manage backup\_download\_token resources in Databasus\.

## Synopsis
Allows managing backup\_download\_token resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. Possible values\; present\, absent\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Backup ID |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.backup_download_token:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.backup_id | success, str. Field backupId\. |
| resource.filename | success, str. Field filename\. |
| resource.token | success, str. Field token\. |
| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

