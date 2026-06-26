# storage_transfer -- Manage storage\_transfer resources in Databasus\.

## Synopsis
Allows managing storage\_transfer resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| id | optional, str, default=None. Storage ID |
| target_workspace_id | True, str, default=None. Body field targetWorkspaceId\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.storage_transfer:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        target_workspace_id: null

```
