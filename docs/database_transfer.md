# database_transfer -- Manage database\_transfer resources in Databasus\.

## Synopsis
Allows managing database\_transfer resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Database ID |
| is_transfer_with_notifiers | optional, bool, default=None. Body field isTransferWithNotifiers\. |
| is_transfer_with_storage | optional, bool, default=None. Body field isTransferWithStorage\. |
| target_notifier_ids | optional, list, default=None. Body field targetNotifierIds\. |
| target_storage_id | optional, str, default=None. Body field targetStorageId\. |
| target_workspace_id | True, str, default=None. Body field targetWorkspaceId\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.database_transfer:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        is_transfer_with_notifiers: null

```
