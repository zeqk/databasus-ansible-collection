# verification_claim -- Manage verification\_claim resources in Databasus\.

## Synopsis
Allows managing verification\_claim resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| agent_id | optional, str, default=None. Agent UUID |
| capacity | optional, dict, default=None. Body field capacity\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.verification_claim:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        capacity: null

```
