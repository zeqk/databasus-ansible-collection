# storage -- Manage storage resources in Databasus\.

## Synopsis
Allows managing storage resources using the Databasus API\.

operationId references are included in generated operation constants\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| azure_blob_storage | optional, dict, default=None. Body field azureBlobStorage\. |
| ftp_storage | optional, dict, default=None. Body field ftpStorage\. |
| google_drive_storage | optional, dict, default=None. Body field googleDriveStorage\. |
| id | True, str, default=None. Body field id\. |
| last_save_error | optional, str, default=None. Body field lastSaveError\. |
| local_storage | optional, dict, default=None. Body field localStorage\. |
| name | optional, str, default=None. Body field name\. |
| nas_storage | optional, dict, default=None. Body field nasStorage\. |
| rclone_storage | optional, dict, default=None. Body field rcloneStorage\. |
| s3_storage | optional, dict, default=None. Body field s3Storage\. |
| sftp_storage | optional, dict, default=None. Body field sftpStorage\. |
| type | optional, str, default=None. Body field type\. |
| workspace_id | optional, str, default=None. Workspace ID |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.storage:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        azure_blob_storage: null

    - name: Delete resource
      zeqk.databasus.storage:
        state: absent
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"

```
