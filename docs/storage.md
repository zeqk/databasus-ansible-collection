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
| last_save_error | optional, str, default=None. Body field lastSaveError\. |
| local_storage | optional, dict, default=None. Body field localStorage\. |
| name | True, str, default=None. Body field name\. |
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
        name: example-name
        azure_blob_storage: null

    - name: Delete resource
      zeqk.databasus.storage:
        state: absent
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        name: example-name

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.azure_blob_storage | success, dict. Field azureBlobStorage\. |
| resource.azure_blob_storage.account_key | success, str. Field accountKey\. |
| resource.azure_blob_storage.account_name | success, str. Field accountName\. |
| resource.azure_blob_storage.auth_method | success, str. Field authMethod\. |
| resource.azure_blob_storage.connection_string | success, str. Field connectionString\. |
| resource.azure_blob_storage.container_name | success, str. Field containerName\. |
| resource.azure_blob_storage.endpoint | success, str. Field endpoint\. |
| resource.azure_blob_storage.prefix | success, str. Field prefix\. |
| resource.azure_blob_storage.storage_id | success, str. Field storageId\. |

| resource.ftp_storage | success, dict. Field ftpStorage\. |
| resource.ftp_storage.host | success, str. Field host\. |
| resource.ftp_storage.password | success, str. Field password\. |
| resource.ftp_storage.path | success, str. Field path\. |
| resource.ftp_storage.port | success, int. Field port\. |
| resource.ftp_storage.skip_tls_verify | success, bool. Field skipTlsVerify\. |
| resource.ftp_storage.storage_id | success, str. Field storageId\. |
| resource.ftp_storage.use_ssl | success, bool. Field useSsl\. |
| resource.ftp_storage.username | success, str. Field username\. |

| resource.google_drive_storage | success, dict. Field googleDriveStorage\. |
| resource.google_drive_storage.client_id | success, str. Field clientId\. |
| resource.google_drive_storage.client_secret | success, str. Field clientSecret\. |
| resource.google_drive_storage.storage_id | success, str. Field storageId\. |
| resource.google_drive_storage.token_json | success, str. Field tokenJson\. |

| resource.id | success, str. Field id\. |
| resource.last_save_error | success, str. Field lastSaveError\. |
| resource.local_storage | success, dict. specific storage |
| resource.local_storage.storage_id | success, str. Field storageId\. |

| resource.name | success, str. Field name\. |
| resource.nas_storage | success, dict. Field nasStorage\. |
| resource.nas_storage.domain | success, str. Field domain\. |
| resource.nas_storage.host | success, str. Field host\. |
| resource.nas_storage.password | success, str. Field password\. |
| resource.nas_storage.path | success, str. Field path\. |
| resource.nas_storage.port | success, int. Field port\. |
| resource.nas_storage.share | success, str. Field share\. |
| resource.nas_storage.storage_id | success, str. Field storageId\. |
| resource.nas_storage.use_ssl | success, bool. Field useSsl\. |
| resource.nas_storage.username | success, str. Field username\. |

| resource.rclone_storage | success, dict. Field rcloneStorage\. |
| resource.rclone_storage.config_content | success, str. Field configContent\. |
| resource.rclone_storage.remote_path | success, str. Field remotePath\. |
| resource.rclone_storage.storage_id | success, str. Field storageId\. |

| resource.s3_storage | success, dict. Field s3Storage\. |
| resource.s3_storage.s3_access_key | success, str. Field s3AccessKey\. |
| resource.s3_storage.s3_bucket | success, str. Field s3Bucket\. |
| resource.s3_storage.s3_endpoint | success, str. Field s3Endpoint\. |
| resource.s3_storage.s3_prefix | success, str. Field s3Prefix\. |
| resource.s3_storage.s3_region | success, str. Field s3Region\. |
| resource.s3_storage.s3_secret_key | success, str. Field s3SecretKey\. |
| resource.s3_storage.s3_storage_class | success, str. Field s3StorageClass\. |
| resource.s3_storage.s3_use_virtual_hosted_style | success, bool. Field s3UseVirtualHostedStyle\. |
| resource.s3_storage.skip_tlsverify | success, bool. Field skipTLSVerify\. |
| resource.s3_storage.storage_id | success, str. Field storageId\. |

| resource.sftp_storage | success, dict. Field sftpStorage\. |
| resource.sftp_storage.host | success, str. Field host\. |
| resource.sftp_storage.password | success, str. Field password\. |
| resource.sftp_storage.path | success, str. Field path\. |
| resource.sftp_storage.port | success, int. Field port\. |
| resource.sftp_storage.private_key | success, str. Field privateKey\. |
| resource.sftp_storage.skip_host_key_verify | success, bool. Field skipHostKeyVerify\. |
| resource.sftp_storage.storage_id | success, str. Field storageId\. |
| resource.sftp_storage.username | success, str. Field username\. |

| resource.type | success, str. Field type\. |
| resource.workspace_id | success, str. Field workspaceId\. |

| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

