# verification_heartbeat -- Manage verification\_heartbeat resources in Databasus\.

## Synopsis
Allows managing verification\_heartbeat resources using the Databasus API\.



## Parameters

| parameter | comments |
|---|---|
| state | optional, str, default=present. Desired state of the resource\. Possible values\; present\, absent\. |
| api_url | True, str, default=None. Base API URL\. |
| api_token | True, str, default=None. Bearer authentication token\. |
| agent_id | optional, str, default=None. Agent UUID |
| current_verification_ids | optional, list, default=None. What the agent thinks it\'s running\. Server returns the subset to abort if some information is outdated |
| max_concurrent_jobs | optional, int, default=None. Body field maxConcurrentJobs\. |
| max_cpu | optional, int, default=None. Body field maxCpu\. |
| max_disk_gb | optional, int, default=None. Body field maxDiskGb\. |
| max_ram_gb | optional, int, default=None. Body field maxRamGb\. |


## Examples

```yaml
    
    - name: Create or update resource
      zeqk.databasus.verification_heartbeat:
        state: present
        api_url: https://api.example.com
        api_token: "{{ databasus_token }}"
        current_verification_ids: null

```


## Return Values

| return value | comments |
|---|---|
| resource | always, dict. Resource object as returned by the API\. |
| resource.abort_verification_ids | success, list. IDs that vanished\, were flipped to CANCELED or are no longer owned by this agent\. So it needs to drop them\. |
| resource.last_seen_at | success, str. Field lastSeenAt\. |

| changed | always, bool. Indicates whether any change was made\. |
| msg | always, str. Descriptive operation message\. |

