#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2026, zeqk (@zeqk)
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: database
short_description: Manage database resources in Databasus.
description:
  - Allows managing database resources using the Databasus API.
  - operationId references are included in generated operation constants.
options:
  state:
    description:
      - Desired state of the resource.
    type: str
    choices:
      - present
      - absent
    default: present
  api_url:
    description:
      - Base API URL.
    type: str
    required: true
  api_token:
    description:
      - Bearer authentication token.
    type: str
    required: true
  health_status:
    description:
      - Body field healthStatus.
    type: str
    choices:
      - AVAILABLE
      - UNAVAILABLE
  last_backup_error_message:
    description:
      - Body field lastBackupErrorMessage.
    type: str
  last_backup_time:
    description:
      - these fields are not reliable, but they are used for pretty UI
    type: str
  mariadb:
    description:
      - Body field mariadb.
    type: dict
    suboptions:
      database:
        description:
          - Body field database.
        type: str
      database_id:
        description:
          - Body field databaseId.
        type: str
      exclude_tables:
        description:
          - Body field excludeTables.
        type: list
        elements: str
      host:
        description:
          - Body field host.
        type: str
      id:
        description:
          - Body field id.
        type: str
      is_exclude_events:
        description:
          - Body field isExcludeEvents.
        type: bool
      is_https:
        description:
          - Body field isHttps.
        type: bool
      is_skip_galera_disable:
        description:
          - Body field isSkipGaleraDisable.
        type: bool
      is_use_extended_insert:
        description:
          - Body field isUseExtendedInsert.
        type: bool
      password:
        description:
          - Body field password.
        type: str
      port:
        description:
          - Body field port.
        type: int
      privileges:
        description:
          - Body field privileges.
        type: str
      username:
        description:
          - Body field username.
        type: str
      version:
        description:
          - Body field version.
        type: str
        choices:
          - '5.5'
          - '10.1'
          - '10.2'
          - '10.3'
          - '10.4'
          - '10.5'
          - '10.6'
          - '10.11'
          - '11.4'
          - '11.8'
          - '12.0'
  mongodb:
    description:
      - Body field mongodb.
    type: dict
    suboptions:
      auth_database:
        description:
          - Body field authDatabase.
        type: str
      cpu_count:
        description:
          - Body field cpuCount.
        type: int
      database:
        description:
          - Body field database.
        type: str
      database_id:
        description:
          - Body field databaseId.
        type: str
      exclude_collections:
        description:
          - Body field excludeCollections.
        type: list
        elements: str
      host:
        description:
          - Body field host.
        type: str
      id:
        description:
          - Body field id.
        type: str
      is_direct_connection:
        description:
          - Body field isDirectConnection.
        type: bool
      is_https:
        description:
          - Body field isHttps.
        type: bool
      is_srv:
        description:
          - Body field isSrv.
        type: bool
      password:
        description:
          - Body field password.
        type: str
      port:
        description:
          - Body field port.
        type: int
      username:
        description:
          - Body field username.
        type: str
      version:
        description:
          - Body field version.
        type: str
        choices:
          - '4'
          - '5'
          - '6'
          - '7'
          - '8'
  mysql:
    description:
      - Body field mysql.
    type: dict
    suboptions:
      database:
        description:
          - Body field database.
        type: str
      database_id:
        description:
          - Body field databaseId.
        type: str
      exclude_tables:
        description:
          - Body field excludeTables.
        type: list
        elements: str
      host:
        description:
          - Body field host.
        type: str
      id:
        description:
          - Body field id.
        type: str
      is_https:
        description:
          - Body field isHttps.
        type: bool
      is_use_extended_insert:
        description:
          - Body field isUseExtendedInsert.
        type: bool
      is_zstd_supported:
        description:
          - Body field isZstdSupported.
        type: bool
      password:
        description:
          - Body field password.
        type: str
      port:
        description:
          - Body field port.
        type: int
      privileges:
        description:
          - Body field privileges.
        type: str
      username:
        description:
          - Body field username.
        type: str
      version:
        description:
          - Body field version.
        type: str
        choices:
          - '5.7'
          - '8.0'
          - '8.4'
          - '9'
  name:
    description:
      - Body field name.
    type: str
    required: true
  notifiers:
    description:
      - Body field notifiers.
    type: list
    elements: dict
    suboptions:
      discord_notifier:
        description:
          - Body field discordNotifier.
        type: dict
        suboptions:
          channel_webhook_url:
            description:
              - Body field channelWebhookUrl.
            type: str
          notifier_id:
            description:
              - Body field notifierId.
            type: str
      email_notifier:
        description:
          - Body field emailNotifier.
        type: dict
        suboptions:
          from:
            description:
              - Body field from.
            type: str
          is_insecure_skip_verify:
            description:
              - Body field isInsecureSkipVerify.
            type: bool
          notifier_id:
            description:
              - Body field notifierId.
            type: str
          smtp_host:
            description:
              - Body field smtpHost.
            type: str
          smtp_password:
            description:
              - Body field smtpPassword.
            type: str
          smtp_port:
            description:
              - Body field smtpPort.
            type: int
          smtp_user:
            description:
              - Body field smtpUser.
            type: str
          target_email:
            description:
              - Body field targetEmail.
            type: str
      id:
        description:
          - Body field id.
        type: str
      last_send_error:
        description:
          - Body field lastSendError.
        type: str
      name:
        description:
          - Body field name.
        type: str
      notifier_type:
        description:
          - Body field notifierType.
        type: str
        choices:
          - EMAIL
          - TELEGRAM
          - WEBHOOK
          - SLACK
          - DISCORD
          - TEAMS
      slack_notifier:
        description:
          - Body field slackNotifier.
        type: dict
        suboptions:
          bot_token:
            description:
              - Body field botToken.
            type: str
          notifier_id:
            description:
              - Body field notifierId.
            type: str
          target_chat_id:
            description:
              - Body field targetChatId.
            type: str
      teams_notifier:
        description:
          - Body field teamsNotifier.
        type: dict
        suboptions:
          notifier_id:
            description:
              - Body field notifierId.
            type: str
          power_automate_url:
            description:
              - Body field powerAutomateUrl.
            type: str
      telegram_notifier:
        description:
          - specific notifier
        type: dict
        suboptions:
          bot_token:
            description:
              - Body field botToken.
            type: str
          is_proxy_enabled:
            description:
              - Body field isProxyEnabled.
            type: bool
          notifier_id:
            description:
              - Body field notifierId.
            type: str
          proxy_url:
            description:
              - Body field proxyUrl.
            type: str
          target_chat_id:
            description:
              - Body field targetChatId.
            type: str
          thread_id:
            description:
              - Body field threadId.
            type: int
      webhook_notifier:
        description:
          - Body field webhookNotifier.
        type: dict
        suboptions:
          body_template:
            description:
              - Body field bodyTemplate.
            type: str
          headers:
            description:
              - Body field headers.
            type: list
            elements: dict
            suboptions:
              key:
                description:
                  - Body field key.
                type: str
              value:
                description:
                  - Body field value.
                type: str
          notifier_id:
            description:
              - Body field notifierId.
            type: str
          webhook_method:
            description:
              - Body field webhookMethod.
            type: str
            choices:
              - POST
              - GET
          webhook_url:
            description:
              - Body field webhookUrl.
            type: str
      workspace_id:
        description:
          - Body field workspaceId.
        type: str
  postgresql_logical:
    description:
      - Body field postgresqlLogical.
    type: dict
    suboptions:
      cpu_count:
        description:
          - Body field cpuCount.
        type: int
      database:
        description:
          - Body field database.
        type: str
      database_id:
        description:
          - Body field databaseId.
        type: str
      exclude_tables:
        description:
          - Body field excludeTables.
        type: list
        elements: str
      host:
        description:
          - Body field host.
        type: str
      id:
        description:
          - Body field id.
        type: str
      include_schemas:
        description:
          - backup settings
        type: list
        elements: str
      is_exclude_extensions:
        description:
          - restore settings (not saved to DB)
        type: bool
      is_restore_ownership:
        description:
          - Body field isRestoreOwnership.
        type: bool
      is_restore_privileges:
        description:
          - Body field isRestorePrivileges.
        type: bool
      is_skip_user_mappings:
        description:
          - Body field isSkipUserMappings.
        type: bool
      password:
        description:
          - Body field password.
        type: str
      port:
        description:
          - Body field port.
        type: int
      ssl_client_cert:
        description:
          - Body field sslClientCert.
        type: str
      ssl_client_key:
        description:
          - Body field sslClientKey.
        type: str
      ssl_mode:
        description:
          - SSL / TLS connection settings
        type: str
        choices:
          - disable
          - require
          - verify-ca
          - verify-full
      ssl_root_cert:
        description:
          - Body field sslRootCert.
        type: str
      username:
        description:
          - Body field username.
        type: str
      version:
        description:
          - Body field version.
        type: str
        choices:
          - '12'
          - '13'
          - '14'
          - '15'
          - '16'
          - '17'
          - '18'
  postgresql_physical:
    description:
      - Body field postgresqlPhysical.
    type: dict
    suboptions:
      backup_type:
        description:
          - Body field backupType.
        type: str
        choices:
          - FULL
          - FULL_INCREMENTAL
          - FULL_INCREMENTAL_WAL_STREAM
      database_id:
        description:
          - Body field databaseId.
        type: str
      host:
        description:
          - Body field host.
        type: str
      id:
        description:
          - Body field id.
        type: str
      password:
        description:
          - Body field password.
        type: str
      port:
        description:
          - Body field port.
        type: int
      ssl_client_cert:
        description:
          - Body field sslClientCert.
        type: str
      ssl_client_key:
        description:
          - Body field sslClientKey.
        type: str
      ssl_mode:
        description:
          - SSL / TLS connection settings
        type: str
        choices:
          - disable
          - require
          - verify-ca
          - verify-full
      ssl_root_cert:
        description:
          - Body field sslRootCert.
        type: str
      system_identifier:
        description:
          - Body field systemIdentifier.
        type: str
      username:
        description:
          - Body field username.
        type: str
      version:
        description:
          - Body field version.
        type: str
        choices:
          - '12'
          - '13'
          - '14'
          - '15'
          - '16'
          - '17'
          - '18'
      wal_segment_size_bytes:
        description:
          - WalSegmentSizeBytes captures the source cluster's wal_segment_size at first connect.
        type: int
  type:
    description:
      - Body field type.
    type: str
    choices:
      - POSTGRES_LOGICAL
      - POSTGRES_PHYSICAL
      - MYSQL
      - MARIADB
      - MONGODB
  workspace_id:
    description:
      - Workspace ID
    type: str
author:
    - zeqk (@zeqk)
"""

EXAMPLES = r"""
- name: Create or update resource
  zeqk.databasus.database:
    state: present
    api_url: https://api.example.com
    api_token: "{{ databasus_token }}"
    name: example-name
    health_status: null

- name: Delete resource
  zeqk.databasus.database:
    state: absent
    api_url: https://api.example.com
    api_token: "{{ databasus_token }}"
    name: example-name
"""

RETURN = r"""
resource:
    description: Resource object as returned by the API.
    type: dict
    returned: always
    contains:
        health_status:
            description:
              - "Field healthStatus."
            type: str
            returned: success
        id:
            description:
              - "Field id."
            type: str
            returned: success
        last_backup_error_message:
            description:
              - "Field lastBackupErrorMessage."
            type: str
            returned: success
        last_backup_time:
            description:
              - "these fields are not reliable, but they are used for pretty UI"
            type: str
            returned: success
        mariadb:
            description:
              - "Field mariadb."
            type: dict
            returned: success
            contains:
                database:
                    description:
                      - "Field database."
                    type: str
                    returned: success
                database_id:
                    description:
                      - "Field databaseId."
                    type: str
                    returned: success
                exclude_tables:
                    description:
                      - "Field excludeTables."
                    type: list
                    elements: str
                    returned: success
                host:
                    description:
                      - "Field host."
                    type: str
                    returned: success
                id:
                    description:
                      - "Field id."
                    type: str
                    returned: success
                is_exclude_events:
                    description:
                      - "Field isExcludeEvents."
                    type: bool
                    returned: success
                is_https:
                    description:
                      - "Field isHttps."
                    type: bool
                    returned: success
                is_skip_galera_disable:
                    description:
                      - "Field isSkipGaleraDisable."
                    type: bool
                    returned: success
                is_use_extended_insert:
                    description:
                      - "Field isUseExtendedInsert."
                    type: bool
                    returned: success
                password:
                    description:
                      - "Field password."
                    type: str
                    returned: success
                port:
                    description:
                      - "Field port."
                    type: int
                    returned: success
                privileges:
                    description:
                      - "Field privileges."
                    type: str
                    returned: success
                username:
                    description:
                      - "Field username."
                    type: str
                    returned: success
                version:
                    description:
                      - "Field version."
                    type: str
                    returned: success
        mongodb:
            description:
              - "Field mongodb."
            type: dict
            returned: success
            contains:
                auth_database:
                    description:
                      - "Field authDatabase."
                    type: str
                    returned: success
                cpu_count:
                    description:
                      - "Field cpuCount."
                    type: int
                    returned: success
                database:
                    description:
                      - "Field database."
                    type: str
                    returned: success
                database_id:
                    description:
                      - "Field databaseId."
                    type: str
                    returned: success
                exclude_collections:
                    description:
                      - "Field excludeCollections."
                    type: list
                    elements: str
                    returned: success
                host:
                    description:
                      - "Field host."
                    type: str
                    returned: success
                id:
                    description:
                      - "Field id."
                    type: str
                    returned: success
                is_direct_connection:
                    description:
                      - "Field isDirectConnection."
                    type: bool
                    returned: success
                is_https:
                    description:
                      - "Field isHttps."
                    type: bool
                    returned: success
                is_srv:
                    description:
                      - "Field isSrv."
                    type: bool
                    returned: success
                password:
                    description:
                      - "Field password."
                    type: str
                    returned: success
                port:
                    description:
                      - "Field port."
                    type: int
                    returned: success
                username:
                    description:
                      - "Field username."
                    type: str
                    returned: success
                version:
                    description:
                      - "Field version."
                    type: str
                    returned: success
        mysql:
            description:
              - "Field mysql."
            type: dict
            returned: success
            contains:
                database:
                    description:
                      - "Field database."
                    type: str
                    returned: success
                database_id:
                    description:
                      - "Field databaseId."
                    type: str
                    returned: success
                exclude_tables:
                    description:
                      - "Field excludeTables."
                    type: list
                    elements: str
                    returned: success
                host:
                    description:
                      - "Field host."
                    type: str
                    returned: success
                id:
                    description:
                      - "Field id."
                    type: str
                    returned: success
                is_https:
                    description:
                      - "Field isHttps."
                    type: bool
                    returned: success
                is_use_extended_insert:
                    description:
                      - "Field isUseExtendedInsert."
                    type: bool
                    returned: success
                is_zstd_supported:
                    description:
                      - "Field isZstdSupported."
                    type: bool
                    returned: success
                password:
                    description:
                      - "Field password."
                    type: str
                    returned: success
                port:
                    description:
                      - "Field port."
                    type: int
                    returned: success
                privileges:
                    description:
                      - "Field privileges."
                    type: str
                    returned: success
                username:
                    description:
                      - "Field username."
                    type: str
                    returned: success
                version:
                    description:
                      - "Field version."
                    type: str
                    returned: success
        name:
            description:
              - "Field name."
            type: str
            returned: success
        notifiers:
            description:
              - "Field notifiers."
            type: list
            elements: dict
            returned: success
            contains:
                discord_notifier:
                    description:
                      - "Field discordNotifier."
                    type: dict
                    returned: success
                    contains:
                        channel_webhook_url:
                            description:
                              - "Field channelWebhookUrl."
                            type: str
                            returned: success
                        notifier_id:
                            description:
                              - "Field notifierId."
                            type: str
                            returned: success
                email_notifier:
                    description:
                      - "Field emailNotifier."
                    type: dict
                    returned: success
                    contains:
                        from:
                            description:
                              - "Field from."
                            type: str
                            returned: success
                        is_insecure_skip_verify:
                            description:
                              - "Field isInsecureSkipVerify."
                            type: bool
                            returned: success
                        notifier_id:
                            description:
                              - "Field notifierId."
                            type: str
                            returned: success
                        smtp_host:
                            description:
                              - "Field smtpHost."
                            type: str
                            returned: success
                        smtp_password:
                            description:
                              - "Field smtpPassword."
                            type: str
                            returned: success
                        smtp_port:
                            description:
                              - "Field smtpPort."
                            type: int
                            returned: success
                        smtp_user:
                            description:
                              - "Field smtpUser."
                            type: str
                            returned: success
                        target_email:
                            description:
                              - "Field targetEmail."
                            type: str
                            returned: success
                id:
                    description:
                      - "Field id."
                    type: str
                    returned: success
                last_send_error:
                    description:
                      - "Field lastSendError."
                    type: str
                    returned: success
                name:
                    description:
                      - "Field name."
                    type: str
                    returned: success
                notifier_type:
                    description:
                      - "Field notifierType."
                    type: str
                    returned: success
                slack_notifier:
                    description:
                      - "Field slackNotifier."
                    type: dict
                    returned: success
                    contains:
                        bot_token:
                            description:
                              - "Field botToken."
                            type: str
                            returned: success
                        notifier_id:
                            description:
                              - "Field notifierId."
                            type: str
                            returned: success
                        target_chat_id:
                            description:
                              - "Field targetChatId."
                            type: str
                            returned: success
                teams_notifier:
                    description:
                      - "Field teamsNotifier."
                    type: dict
                    returned: success
                    contains:
                        notifier_id:
                            description:
                              - "Field notifierId."
                            type: str
                            returned: success
                        power_automate_url:
                            description:
                              - "Field powerAutomateUrl."
                            type: str
                            returned: success
                telegram_notifier:
                    description:
                      - "specific notifier"
                    type: dict
                    returned: success
                    contains:
                        bot_token:
                            description:
                              - "Field botToken."
                            type: str
                            returned: success
                        is_proxy_enabled:
                            description:
                              - "Field isProxyEnabled."
                            type: bool
                            returned: success
                        notifier_id:
                            description:
                              - "Field notifierId."
                            type: str
                            returned: success
                        proxy_url:
                            description:
                              - "Field proxyUrl."
                            type: str
                            returned: success
                        target_chat_id:
                            description:
                              - "Field targetChatId."
                            type: str
                            returned: success
                        thread_id:
                            description:
                              - "Field threadId."
                            type: int
                            returned: success
                webhook_notifier:
                    description:
                      - "Field webhookNotifier."
                    type: dict
                    returned: success
                    contains:
                        body_template:
                            description:
                              - "Field bodyTemplate."
                            type: str
                            returned: success
                        headers:
                            description:
                              - "Field headers."
                            type: list
                            elements: dict
                            returned: success
                            contains:
                                key:
                                    description:
                                      - "Field key."
                                    type: str
                                    returned: success
                                value:
                                    description:
                                      - "Field value."
                                    type: str
                                    returned: success
                        notifier_id:
                            description:
                              - "Field notifierId."
                            type: str
                            returned: success
                        webhook_method:
                            description:
                              - "Field webhookMethod."
                            type: str
                            returned: success
                        webhook_url:
                            description:
                              - "Field webhookUrl."
                            type: str
                            returned: success
                workspace_id:
                    description:
                      - "Field workspaceId."
                    type: str
                    returned: success
        postgresql_logical:
            description:
              - "Field postgresqlLogical."
            type: dict
            returned: success
            contains:
                cpu_count:
                    description:
                      - "Field cpuCount."
                    type: int
                    returned: success
                database:
                    description:
                      - "Field database."
                    type: str
                    returned: success
                database_id:
                    description:
                      - "Field databaseId."
                    type: str
                    returned: success
                exclude_tables:
                    description:
                      - "Field excludeTables."
                    type: list
                    elements: str
                    returned: success
                host:
                    description:
                      - "Field host."
                    type: str
                    returned: success
                id:
                    description:
                      - "Field id."
                    type: str
                    returned: success
                include_schemas:
                    description:
                      - "backup settings"
                    type: list
                    elements: str
                    returned: success
                is_exclude_extensions:
                    description:
                      - "restore settings (not saved to DB)"
                    type: bool
                    returned: success
                is_restore_ownership:
                    description:
                      - "Field isRestoreOwnership."
                    type: bool
                    returned: success
                is_restore_privileges:
                    description:
                      - "Field isRestorePrivileges."
                    type: bool
                    returned: success
                is_skip_user_mappings:
                    description:
                      - "Field isSkipUserMappings."
                    type: bool
                    returned: success
                password:
                    description:
                      - "Field password."
                    type: str
                    returned: success
                port:
                    description:
                      - "Field port."
                    type: int
                    returned: success
                ssl_client_cert:
                    description:
                      - "Field sslClientCert."
                    type: str
                    returned: success
                ssl_client_key:
                    description:
                      - "Field sslClientKey."
                    type: str
                    returned: success
                ssl_mode:
                    description:
                      - "SSL / TLS connection settings"
                    type: str
                    returned: success
                ssl_root_cert:
                    description:
                      - "Field sslRootCert."
                    type: str
                    returned: success
                username:
                    description:
                      - "Field username."
                    type: str
                    returned: success
                version:
                    description:
                      - "Field version."
                    type: str
                    returned: success
        postgresql_physical:
            description:
              - "Field postgresqlPhysical."
            type: dict
            returned: success
            contains:
                backup_type:
                    description:
                      - "Field backupType."
                    type: str
                    returned: success
                database_id:
                    description:
                      - "Field databaseId."
                    type: str
                    returned: success
                host:
                    description:
                      - "Field host."
                    type: str
                    returned: success
                id:
                    description:
                      - "Field id."
                    type: str
                    returned: success
                password:
                    description:
                      - "Field password."
                    type: str
                    returned: success
                port:
                    description:
                      - "Field port."
                    type: int
                    returned: success
                ssl_client_cert:
                    description:
                      - "Field sslClientCert."
                    type: str
                    returned: success
                ssl_client_key:
                    description:
                      - "Field sslClientKey."
                    type: str
                    returned: success
                ssl_mode:
                    description:
                      - "SSL / TLS connection settings"
                    type: str
                    returned: success
                ssl_root_cert:
                    description:
                      - "Field sslRootCert."
                    type: str
                    returned: success
                system_identifier:
                    description:
                      - "Field systemIdentifier."
                    type: str
                    returned: success
                username:
                    description:
                      - "Field username."
                    type: str
                    returned: success
                version:
                    description:
                      - "Field version."
                    type: str
                    returned: success
                wal_segment_size_bytes:
                    description:
                      - "WalSegmentSizeBytes captures the source cluster's wal_segment_size at first connect."
                    type: int
                    returned: success
        type:
            description:
              - "Field type."
            type: str
            returned: success
        workspace_id:
            description:
              - "WorkspaceID can be null when a database is created via restore operation outside the context of any"
              - "workspace"
            type: str
            returned: success
changed:
    description: Indicates whether any change was made.
    type: bool
    returned: always
msg:
    description: Descriptive operation message.
    type: str
    returned: always
"""


import json
import shlex
from typing import Any, Dict, List, Optional, Tuple
from urllib import error, parse

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import open_url


CREATE_METHOD = 'POST'
CREATE_PATH = '/databases/create'
CREATE_PATH_PARAMS = []
CREATE_QUERY_PARAMS = []
LIST_METHOD = 'GET'
LIST_PATH = '/databases'
LIST_PATH_PARAMS = []
LIST_QUERY_PARAMS = ['workspace_id']
GET_METHOD = 'GET'
GET_PATH = '/databases/{id}'
GET_PATH_PARAMS = ['id']
GET_QUERY_PARAMS = []
UPDATE_METHOD = None
UPDATE_PATH = None
UPDATE_PATH_PARAMS = []
UPDATE_QUERY_PARAMS = []
DELETE_METHOD = 'DELETE'
DELETE_PATH = '/databases/{id}'
DELETE_PATH_PARAMS = ['id']
DELETE_QUERY_PARAMS = []
BODY_SCHEMA = {
    'health_status': {'api': 'healthStatus', 'type': 'str'},
    'id': {'api': 'id', 'type': 'str'},
    'last_backup_error_message': {'api': 'lastBackupErrorMessage', 'type': 'str'},
    'last_backup_time': {'api': 'lastBackupTime', 'type': 'str'},
    'mariadb': {
        'api': 'mariadb',
        'type': 'dict',
        'nested': {
            'database': {'api': 'database', 'type': 'str'},
            'database_id': {'api': 'databaseId', 'type': 'str'},
            'exclude_tables': {'api': 'excludeTables', 'type': 'list'},
            'host': {'api': 'host', 'type': 'str'},
            'id': {'api': 'id', 'type': 'str'},
            'is_exclude_events': {'api': 'isExcludeEvents', 'type': 'bool'},
            'is_https': {'api': 'isHttps', 'type': 'bool'},
            'is_skip_galera_disable': {'api': 'isSkipGaleraDisable', 'type': 'bool'},
            'is_use_extended_insert': {'api': 'isUseExtendedInsert', 'type': 'bool'},
            'password': {'api': 'password', 'type': 'str'},
            'port': {'api': 'port', 'type': 'int'},
            'privileges': {'api': 'privileges', 'type': 'str'},
            'username': {'api': 'username', 'type': 'str'},
            'version': {'api': 'version', 'type': 'str'},
        },
    },
    'mongodb': {
        'api': 'mongodb',
        'type': 'dict',
        'nested': {
            'auth_database': {'api': 'authDatabase', 'type': 'str'},
            'cpu_count': {'api': 'cpuCount', 'type': 'int'},
            'database': {'api': 'database', 'type': 'str'},
            'database_id': {'api': 'databaseId', 'type': 'str'},
            'exclude_collections': {'api': 'excludeCollections', 'type': 'list'},
            'host': {'api': 'host', 'type': 'str'},
            'id': {'api': 'id', 'type': 'str'},
            'is_direct_connection': {'api': 'isDirectConnection', 'type': 'bool'},
            'is_https': {'api': 'isHttps', 'type': 'bool'},
            'is_srv': {'api': 'isSrv', 'type': 'bool'},
            'password': {'api': 'password', 'type': 'str'},
            'port': {'api': 'port', 'type': 'int'},
            'username': {'api': 'username', 'type': 'str'},
            'version': {'api': 'version', 'type': 'str'},
        },
    },
    'mysql': {
        'api': 'mysql',
        'type': 'dict',
        'nested': {
            'database': {'api': 'database', 'type': 'str'},
            'database_id': {'api': 'databaseId', 'type': 'str'},
            'exclude_tables': {'api': 'excludeTables', 'type': 'list'},
            'host': {'api': 'host', 'type': 'str'},
            'id': {'api': 'id', 'type': 'str'},
            'is_https': {'api': 'isHttps', 'type': 'bool'},
            'is_use_extended_insert': {'api': 'isUseExtendedInsert', 'type': 'bool'},
            'is_zstd_supported': {'api': 'isZstdSupported', 'type': 'bool'},
            'password': {'api': 'password', 'type': 'str'},
            'port': {'api': 'port', 'type': 'int'},
            'privileges': {'api': 'privileges', 'type': 'str'},
            'username': {'api': 'username', 'type': 'str'},
            'version': {'api': 'version', 'type': 'str'},
        },
    },
    'name': {'api': 'name', 'type': 'str'},
    'notifiers': {
        'api': 'notifiers',
        'type': 'list',
        'nested': {
            'discord_notifier': {
                'api': 'discordNotifier',
                'type': 'dict',
                'nested': {
                    'channel_webhook_url': {'api': 'channelWebhookUrl', 'type': 'str'},
                    'notifier_id': {'api': 'notifierId', 'type': 'str'},
                },
            },
            'email_notifier': {
                'api': 'emailNotifier',
                'type': 'dict',
                'nested': {
                    'from': {'api': 'from', 'type': 'str'},
                    'is_insecure_skip_verify': {'api': 'isInsecureSkipVerify', 'type': 'bool'},
                    'notifier_id': {'api': 'notifierId', 'type': 'str'},
                    'smtp_host': {'api': 'smtpHost', 'type': 'str'},
                    'smtp_password': {'api': 'smtpPassword', 'type': 'str'},
                    'smtp_port': {'api': 'smtpPort', 'type': 'int'},
                    'smtp_user': {'api': 'smtpUser', 'type': 'str'},
                    'target_email': {'api': 'targetEmail', 'type': 'str'},
                },
            },
            'id': {'api': 'id', 'type': 'str'},
            'last_send_error': {'api': 'lastSendError', 'type': 'str'},
            'name': {'api': 'name', 'type': 'str'},
            'notifier_type': {'api': 'notifierType', 'type': 'str'},
            'slack_notifier': {
                'api': 'slackNotifier',
                'type': 'dict',
                'nested': {
                    'bot_token': {'api': 'botToken', 'type': 'str'},
                    'notifier_id': {'api': 'notifierId', 'type': 'str'},
                    'target_chat_id': {'api': 'targetChatId', 'type': 'str'},
                },
            },
            'teams_notifier': {
                'api': 'teamsNotifier',
                'type': 'dict',
                'nested': {
                    'notifier_id': {'api': 'notifierId', 'type': 'str'},
                    'power_automate_url': {'api': 'powerAutomateUrl', 'type': 'str'},
                },
            },
            'telegram_notifier': {
                'api': 'telegramNotifier',
                'type': 'dict',
                'nested': {
                    'bot_token': {'api': 'botToken', 'type': 'str'},
                    'is_proxy_enabled': {'api': 'isProxyEnabled', 'type': 'bool'},
                    'notifier_id': {'api': 'notifierId', 'type': 'str'},
                    'proxy_url': {'api': 'proxyUrl', 'type': 'str'},
                    'target_chat_id': {'api': 'targetChatId', 'type': 'str'},
                    'thread_id': {'api': 'threadId', 'type': 'int'},
                },
            },
            'webhook_notifier': {
                'api': 'webhookNotifier',
                'type': 'dict',
                'nested': {
                    'body_template': {'api': 'bodyTemplate', 'type': 'str'},
                    'headers': {
                        'api': 'headers',
                        'type': 'list',
                        'nested': {
                            'key': {'api': 'key', 'type': 'str'},
                            'value': {'api': 'value', 'type': 'str'},
                        },
                    },
                    'notifier_id': {'api': 'notifierId', 'type': 'str'},
                    'webhook_method': {'api': 'webhookMethod', 'type': 'str'},
                    'webhook_url': {'api': 'webhookUrl', 'type': 'str'},
                },
            },
            'workspace_id': {'api': 'workspaceId', 'type': 'str'},
        },
    },
    'postgresql_logical': {
        'api': 'postgresqlLogical',
        'type': 'dict',
        'nested': {
            'cpu_count': {'api': 'cpuCount', 'type': 'int'},
            'database': {'api': 'database', 'type': 'str'},
            'database_id': {'api': 'databaseId', 'type': 'str'},
            'exclude_tables': {'api': 'excludeTables', 'type': 'list'},
            'host': {'api': 'host', 'type': 'str'},
            'id': {'api': 'id', 'type': 'str'},
            'include_schemas': {'api': 'includeSchemas', 'type': 'list'},
            'is_exclude_extensions': {'api': 'isExcludeExtensions', 'type': 'bool'},
            'is_restore_ownership': {'api': 'isRestoreOwnership', 'type': 'bool'},
            'is_restore_privileges': {'api': 'isRestorePrivileges', 'type': 'bool'},
            'is_skip_user_mappings': {'api': 'isSkipUserMappings', 'type': 'bool'},
            'password': {'api': 'password', 'type': 'str'},
            'port': {'api': 'port', 'type': 'int'},
            'ssl_client_cert': {'api': 'sslClientCert', 'type': 'str'},
            'ssl_client_key': {'api': 'sslClientKey', 'type': 'str'},
            'ssl_mode': {'api': 'sslMode', 'type': 'str'},
            'ssl_root_cert': {'api': 'sslRootCert', 'type': 'str'},
            'username': {'api': 'username', 'type': 'str'},
            'version': {'api': 'version', 'type': 'str'},
        },
    },
    'postgresql_physical': {
        'api': 'postgresqlPhysical',
        'type': 'dict',
        'nested': {
            'backup_type': {'api': 'backupType', 'type': 'str'},
            'database_id': {'api': 'databaseId', 'type': 'str'},
            'host': {'api': 'host', 'type': 'str'},
            'id': {'api': 'id', 'type': 'str'},
            'password': {'api': 'password', 'type': 'str'},
            'port': {'api': 'port', 'type': 'int'},
            'ssl_client_cert': {'api': 'sslClientCert', 'type': 'str'},
            'ssl_client_key': {'api': 'sslClientKey', 'type': 'str'},
            'ssl_mode': {'api': 'sslMode', 'type': 'str'},
            'ssl_root_cert': {'api': 'sslRootCert', 'type': 'str'},
            'system_identifier': {'api': 'systemIdentifier', 'type': 'str'},
            'username': {'api': 'username', 'type': 'str'},
            'version': {'api': 'version', 'type': 'str'},
            'wal_segment_size_bytes': {'api': 'walSegmentSizeBytes', 'type': 'int'},
        },
    },
    'type': {'api': 'type', 'type': 'str'},
    'workspace_id': {'api': 'workspace_id', 'type': 'str'},
}
READ_ONLY = False
API_NAME_MAP = {
    'api_url': 'api_url',
    'api_token': 'api_token',
    'state': 'state',
    'workspace_id': 'workspace_id',
    'health_status': 'healthStatus',
    'id': 'id',
    'last_backup_error_message': 'lastBackupErrorMessage',
    'last_backup_time': 'lastBackupTime',
    'mariadb': 'mariadb',
    'mongodb': 'mongodb',
    'mysql': 'mysql',
    'name': 'name',
    'notifiers': 'notifiers',
    'postgresql_logical': 'postgresqlLogical',
    'postgresql_physical': 'postgresqlPhysical',
    'type': 'type',
}
REQUIRED_DELETE_PATH_PARAMS = ['id']
REQUIRED_GET_PATH_PARAMS = ['id']
REQUIRED_CREATE_PATH_PARAMS = []
REQUIRED_LIST_QUERY_PARAMS = ['workspace_id']
NAME_ADDRESSABLE = True
NAME_FIELD = 'name'
NAME_API = 'name'
ID_FIELD = 'id'
ID_API = 'id'
MATCH_FIELDS = [('workspace_id', 'workspaceId')]
CREATE_IS_UPSERT = False


def _build_url(api_url: str, path_template: str, path_params: Dict[str, Any], query_params: Optional[Dict[str, Any]] = None) -> str:
    encoded = {k: parse.quote(str(v), safe='') for k, v in path_params.items()}
    path = path_template.format(**encoded)
    url = api_url.rstrip('/') + path
    clean_query = {k: v for k, v in (query_params or {}).items() if v is not None}
    if clean_query:
        url += '?' + parse.urlencode(clean_query, doseq=True)
    return url


def _decode_body(raw: str) -> Any:
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {'raw': raw}


def _build_curl(method: str, url: str, headers: Dict[str, Any], data: Optional[bytes]) -> str:
    parts = ['curl', '-sS', '-X', method.upper()]
    for key, value in headers.items():
        header_value = str(value)
        if key.lower() == 'authorization':
            header_value = 'Bearer <REDACTED>'
        parts += ['-H', shlex.quote(f'{key}: {header_value}')]
    if data is not None:
        parts += ['--data', shlex.quote(data.decode('utf-8', errors='replace'))]
    parts.append(shlex.quote(url))
    return ' '.join(parts)


def _request_json(
    module: AnsibleModule,
    method: str,
    url: str,
    token: str,
    payload: Optional[Dict[str, Any]] = None,
    expected_statuses: Optional[List[int]] = None,
    allow_statuses: Optional[List[int]] = None,
) -> Tuple[int, Any]:
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}',
    }
    data = None
    response_headers: Dict[str, Any] = {}
    if payload is not None:
        headers['Content-Type'] = 'application/json'
        data = json.dumps(payload).encode('utf-8')

    try:
        with open_url(
            url,
            data=data,
            headers=headers,
            method=method,
            timeout=30,
        ) as response:
            status = int(response.getcode())
            response_headers = dict(getattr(response, 'headers', {}) or {})
            raw = response.read().decode('utf-8')
    except error.HTTPError as exc:
        status = int(exc.code)
        raw = exc.read().decode('utf-8', errors='replace')
        decoded = _decode_body(raw)
        reason = str(getattr(exc, 'reason', '') or '')
        response_headers = dict(getattr(exc, 'headers', {}) or {})
        if allow_statuses and status in allow_statuses:
            return status, decoded
        equivalent_curl = _build_curl(method, url, headers, data)
        module.fail_json(
            msg=f'HTTP {status} on {method} {url}. Reason: {reason}. Response body: {raw}. Equivalent curl: {equivalent_curl}',
            http_status=status,
            method=method,
            url=url,
            reason=reason,
            response_headers=response_headers,
            response_body=raw,
            response_json=decoded,
            equivalent_curl=equivalent_curl,
        )
    except error.URLError as exc:
        reason = str(getattr(exc, 'reason', exc))
        module.fail_json(
            msg=f'Connection error on {method} {url}: {reason}',
            method=method,
            url=url,
            reason=reason,
        )

    if expected_statuses and status not in expected_statuses:
        decoded = _decode_body(raw)
        equivalent_curl = _build_curl(method, url, headers, data)
        module.fail_json(
            msg=f'Unexpected HTTP {status} on {method} {url}. Response body: {raw}. Equivalent curl: {equivalent_curl}',
            http_status=status,
            expected_statuses=expected_statuses,
            method=method,
            url=url,
            response_headers=response_headers,
            response_body=raw,
            response_json=decoded,
            equivalent_curl=equivalent_curl,
        )

    return status, _decode_body(raw)


def _collect_params(module_params: Dict[str, Any], names: List[str]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for name in names:
        value = module_params.get(name)
        if value is not None:
            out[API_NAME_MAP.get(name, name)] = value
    return out


def _build_payload(values: Dict[str, Any], schema: Dict[str, Any]) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    for field_name, field_info in schema.items():
        val = values.get(field_name)
        if val is None:
            continue
        api_name = field_info['api']
        nested = field_info.get('nested')
        ftype = field_info.get('type', 'str')
        if nested and ftype == 'dict' and isinstance(val, dict):
            inner = _build_payload(val, nested)
            if inner:
                payload[api_name] = inner
        elif nested and ftype == 'list' and isinstance(val, list):
            payload[api_name] = [
                _build_payload(item, nested) for item in val if isinstance(item, dict)
            ]
        else:
            payload[api_name] = val
    return payload


def _desired_payload(module_params: Dict[str, Any]) -> Dict[str, Any]:
    return _build_payload(module_params, BODY_SCHEMA)


def _needs_update(current: Any, desired: Dict[str, Any]) -> bool:
    if not desired:
        return False
    if not isinstance(current, dict):
        return True
    for key, value in desired.items():
        if current.get(key) != value:
            return True
    return False


def _extract_items(listing: Any) -> List[Any]:
    if isinstance(listing, list):
        return listing
    if isinstance(listing, dict):
        for value in listing.values():
            if isinstance(value, list):
                return value
    return []


def _find_by_name(
    listing: Any,
    name_api: str,
    desired_name: str,
    match_fields: List[Tuple[str, Any]],
) -> Optional[Dict[str, Any]]:
    if not name_api or desired_name is None:
        return None
    for item in _extract_items(listing):
        if not isinstance(item, dict) or item.get(name_api) != desired_name:
            continue
        matches_scope = True
        for field_api_name, desired_value in match_fields:
            if desired_value is None:
                continue
            if item.get(field_api_name) != desired_value:
                matches_scope = False
                break
        if matches_scope:
            return item
    return None


def _has_required(module_params: Dict[str, Any], names: List[str]) -> bool:
    return all(module_params.get(name) is not None for name in names)


def _ensure_required(module: AnsibleModule, module_params: Dict[str, Any], names: List[str], context: str) -> None:
    missing = [name for name in names if module_params.get(name) is None]
    if missing:
        module.fail_json(msg=f'Missing required parameters for {context}: {", ".join(missing)}')


def run_module() -> None:
    module_args = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        api_url=dict(type='str', required=True),
        api_token=dict(type='str', required=True, no_log=True),
        health_status=dict(type='str', choices=['AVAILABLE', 'UNAVAILABLE']),
        last_backup_error_message=dict(type='str'),
        last_backup_time=dict(type='str'),
        mariadb=dict(
            type='dict',
            options={
                'database': dict(type='str'),
                'database_id': dict(type='str'),
                'exclude_tables': dict(type='list', elements='str'),
                'host': dict(type='str'),
                'id': dict(type='str'),
                'is_exclude_events': dict(type='bool'),
                'is_https': dict(type='bool'),
                'is_skip_galera_disable': dict(type='bool'),
                'is_use_extended_insert': dict(type='bool'),
                'password': dict(type='str', no_log=True),
                'port': dict(type='int'),
                'privileges': dict(type='str'),
                'username': dict(type='str'),
                'version': dict(
                    type='str',
                    choices=['5.5', '10.1', '10.2', '10.3', '10.4', '10.5', '10.6', '10.11', '11.4', '11.8', '12.0'],
                ),
            },
        ),
        mongodb=dict(
            type='dict',
            options={
                'auth_database': dict(type='str'),
                'cpu_count': dict(type='int'),
                'database': dict(type='str'),
                'database_id': dict(type='str'),
                'exclude_collections': dict(type='list', elements='str'),
                'host': dict(type='str'),
                'id': dict(type='str'),
                'is_direct_connection': dict(type='bool'),
                'is_https': dict(type='bool'),
                'is_srv': dict(type='bool'),
                'password': dict(type='str', no_log=True),
                'port': dict(type='int'),
                'username': dict(type='str'),
                'version': dict(type='str', choices=['4', '5', '6', '7', '8']),
            },
        ),
        mysql=dict(
            type='dict',
            options={
                'database': dict(type='str'),
                'database_id': dict(type='str'),
                'exclude_tables': dict(type='list', elements='str'),
                'host': dict(type='str'),
                'id': dict(type='str'),
                'is_https': dict(type='bool'),
                'is_use_extended_insert': dict(type='bool'),
                'is_zstd_supported': dict(type='bool'),
                'password': dict(type='str', no_log=True),
                'port': dict(type='int'),
                'privileges': dict(type='str'),
                'username': dict(type='str'),
                'version': dict(type='str', choices=['5.7', '8.0', '8.4', '9']),
            },
        ),
        name=dict(type='str', required=True),
        notifiers=dict(
            type='list',
            elements='dict',
            options={
                'discord_notifier': dict(
                    type='dict',
                    options={
                        'channel_webhook_url': dict(type='str'),
                        'notifier_id': dict(type='str'),
                    },
                ),
                'email_notifier': dict(
                    type='dict',
                    options={
                        'from': dict(type='str'),
                        'is_insecure_skip_verify': dict(type='bool'),
                        'notifier_id': dict(type='str'),
                        'smtp_host': dict(type='str'),
                        'smtp_password': dict(type='str', no_log=True),
                        'smtp_port': dict(type='int'),
                        'smtp_user': dict(type='str'),
                        'target_email': dict(type='str'),
                    },
                ),
                'id': dict(type='str'),
                'last_send_error': dict(type='str'),
                'name': dict(type='str'),
                'notifier_type': dict(type='str', choices=['EMAIL', 'TELEGRAM', 'WEBHOOK', 'SLACK', 'DISCORD', 'TEAMS']),
                'slack_notifier': dict(
                    type='dict',
                    options={
                        'bot_token': dict(type='str', no_log=True),
                        'notifier_id': dict(type='str'),
                        'target_chat_id': dict(type='str'),
                    },
                ),
                'teams_notifier': dict(
                    type='dict',
                    options={
                        'notifier_id': dict(type='str'),
                        'power_automate_url': dict(type='str'),
                    },
                ),
                'telegram_notifier': dict(
                    type='dict',
                    options={
                        'bot_token': dict(type='str', no_log=True),
                        'is_proxy_enabled': dict(type='bool'),
                        'notifier_id': dict(type='str'),
                        'proxy_url': dict(type='str'),
                        'target_chat_id': dict(type='str'),
                        'thread_id': dict(type='int'),
                    },
                ),
                'webhook_notifier': dict(
                    type='dict',
                    options={
                        'body_template': dict(type='str'),
                        'headers': dict(
                            type='list',
                            elements='dict',
                            options={
                                'key': dict(type='str', no_log=True),
                                'value': dict(type='str'),
                            },
                        ),
                        'notifier_id': dict(type='str'),
                        'webhook_method': dict(type='str', choices=['POST', 'GET']),
                        'webhook_url': dict(type='str'),
                    },
                ),
                'workspace_id': dict(type='str'),
            },
        ),
        postgresql_logical=dict(
            type='dict',
            options={
                'cpu_count': dict(type='int'),
                'database': dict(type='str'),
                'database_id': dict(type='str'),
                'exclude_tables': dict(type='list', elements='str'),
                'host': dict(type='str'),
                'id': dict(type='str'),
                'include_schemas': dict(type='list', elements='str'),
                'is_exclude_extensions': dict(type='bool'),
                'is_restore_ownership': dict(type='bool'),
                'is_restore_privileges': dict(type='bool'),
                'is_skip_user_mappings': dict(type='bool'),
                'password': dict(type='str', no_log=True),
                'port': dict(type='int'),
                'ssl_client_cert': dict(type='str'),
                'ssl_client_key': dict(type='str', no_log=True),
                'ssl_mode': dict(type='str', choices=['disable', 'require', 'verify-ca', 'verify-full']),
                'ssl_root_cert': dict(type='str'),
                'username': dict(type='str'),
                'version': dict(type='str', choices=['12', '13', '14', '15', '16', '17', '18']),
            },
        ),
        postgresql_physical=dict(
            type='dict',
            options={
                'backup_type': dict(type='str', choices=['FULL', 'FULL_INCREMENTAL', 'FULL_INCREMENTAL_WAL_STREAM']),
                'database_id': dict(type='str'),
                'host': dict(type='str'),
                'id': dict(type='str'),
                'password': dict(type='str', no_log=True),
                'port': dict(type='int'),
                'ssl_client_cert': dict(type='str'),
                'ssl_client_key': dict(type='str', no_log=True),
                'ssl_mode': dict(type='str', choices=['disable', 'require', 'verify-ca', 'verify-full']),
                'ssl_root_cert': dict(type='str'),
                'system_identifier': dict(type='str'),
                'username': dict(type='str'),
                'version': dict(type='str', choices=['12', '13', '14', '15', '16', '17', '18']),
                'wal_segment_size_bytes': dict(type='int'),
            },
        ),
        type=dict(type='str', choices=['POSTGRES_LOGICAL', 'POSTGRES_PHYSICAL', 'MYSQL', 'MARIADB', 'MONGODB']),
        workspace_id=dict(type='str'),
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=not READ_ONLY)
    params = module.params

    api_url = params['api_url']
    api_token = params['api_token']
    state = params.get('state', 'present')

    result: Dict[str, Any] = dict(changed=False, resource={}, msg='No changes')

    if READ_ONLY:
        if GET_PATH and _has_required(params, GET_PATH_PARAMS):
            get_url = _build_url(api_url, GET_PATH, _collect_params(params, GET_PATH_PARAMS), _collect_params(params, GET_QUERY_PARAMS))
            current = _request_json(module, GET_METHOD, get_url, api_token, expected_statuses=[200])[1]
            result['resource'] = current if isinstance(current, dict) else {'value': current}
            result['msg'] = 'Single-resource query completed'
            module.exit_json(**result)

        if LIST_PATH:
            list_url = _build_url(api_url, LIST_PATH, _collect_params(params, LIST_PATH_PARAMS), _collect_params(params, LIST_QUERY_PARAMS))
            listing = _request_json(module, LIST_METHOD, list_url, api_token, expected_statuses=[200])[1]
            result['resource'] = listing if isinstance(listing, dict) else {'items': listing}
            result['msg'] = 'List query completed'
            module.exit_json(**result)

        result['msg'] = 'No usable GET endpoint for this module'
        module.fail_json(**result)

    exists = False
    current: Any = {}

    if NAME_ADDRESSABLE:
        if not LIST_PATH:
            module.fail_json(msg='Name-based idempotency requires a list endpoint')
        _ensure_required(module, params, [NAME_FIELD], 'name-based lookup')
        _ensure_required(module, params, REQUIRED_LIST_QUERY_PARAMS, 'name-based lookup')

        list_url = _build_url(api_url, LIST_PATH, _collect_params(params, LIST_PATH_PARAMS), _collect_params(params, LIST_QUERY_PARAMS))
        listing = _request_json(module, LIST_METHOD, list_url, api_token, expected_statuses=[200])[1]
        scoped_match_fields = [(api_name, params.get(field_name)) for field_name, api_name in MATCH_FIELDS]
        matched = _find_by_name(listing, NAME_API, params.get(NAME_FIELD), scoped_match_fields)
        if matched is not None:
            exists = True
            current = matched
            if ID_FIELD and ID_API and matched.get(ID_API) is not None:
                params[ID_FIELD] = matched.get(ID_API)

    if GET_PATH and _has_required(params, GET_PATH_PARAMS):
        get_url = _build_url(api_url, GET_PATH, _collect_params(params, GET_PATH_PARAMS), _collect_params(params, GET_QUERY_PARAMS))
        status, body = _request_json(module, GET_METHOD, get_url, api_token, expected_statuses=[200], allow_statuses=[404])
        if status == 200:
            exists = True
            current = body

    desired = _desired_payload(params)

    if state == 'absent':
        if not DELETE_PATH:
            result['msg'] = 'Resource does not support delete operation'
            module.fail_json(**result)

        if not exists:
            result['msg'] = 'Resource is already absent'
            module.exit_json(**result)

        _ensure_required(module, params, REQUIRED_DELETE_PATH_PARAMS or DELETE_PATH_PARAMS, 'delete')

        if module.check_mode:
            result['changed'] = True
            result['msg'] = 'Delete planned (check_mode)'
            module.exit_json(**result)

        delete_url = _build_url(api_url, DELETE_PATH, _collect_params(params, DELETE_PATH_PARAMS), _collect_params(params, DELETE_QUERY_PARAMS))
        _request_json(module, DELETE_METHOD, delete_url, api_token, expected_statuses=[200, 202, 204])
        result['changed'] = True
        result['resource'] = {}
        result['msg'] = 'Resource deleted'
        module.exit_json(**result)

    if exists:
        if UPDATE_PATH:
            if not _needs_update(current, desired):
                result['resource'] = current if isinstance(current, dict) else {'value': current}
                result['msg'] = 'Resource already in desired state'
                module.exit_json(**result)

            if module.check_mode:
                result['changed'] = True
                result['resource'] = current if isinstance(current, dict) else {'value': current}
                result['msg'] = 'Update planned (check_mode)'
                module.exit_json(**result)

            _ensure_required(module, params, UPDATE_PATH_PARAMS, 'update')
            update_url = _build_url(api_url, UPDATE_PATH, _collect_params(params, UPDATE_PATH_PARAMS), _collect_params(params, UPDATE_QUERY_PARAMS))
            updated = _request_json(module, UPDATE_METHOD, update_url, api_token, payload=desired, expected_statuses=[200, 201])[1]
            result['changed'] = True
            result['resource'] = updated if isinstance(updated, dict) else {'value': updated}
            result['msg'] = 'Resource updated'
            module.exit_json(**result)

        if CREATE_IS_UPSERT:
            if not _needs_update(current, desired):
                result['resource'] = current if isinstance(current, dict) else {'value': current}
                result['msg'] = 'Resource already in desired state'
                module.exit_json(**result)

            if module.check_mode:
                result['changed'] = True
                result['resource'] = current if isinstance(current, dict) else {'value': current}
                result['msg'] = 'Update planned (check_mode)'
                module.exit_json(**result)

            _ensure_required(module, params, REQUIRED_CREATE_PATH_PARAMS or CREATE_PATH_PARAMS, 'create')
            create_url = _build_url(api_url, CREATE_PATH, _collect_params(params, CREATE_PATH_PARAMS), _collect_params(params, CREATE_QUERY_PARAMS))
            updated = _request_json(module, CREATE_METHOD, create_url, api_token, payload=desired, expected_statuses=[200, 201, 202])[1]
            result['changed'] = True
            result['resource'] = updated if isinstance(updated, dict) else {'value': updated}
            result['msg'] = 'Resource updated'
            module.exit_json(**result)

        result['resource'] = current if isinstance(current, dict) else {'value': current}
        result['msg'] = 'Resource exists; no update endpoint available'
        module.exit_json(**result)

    if not CREATE_PATH:
        result['msg'] = 'Resource does not exist and there is no create endpoint'
        module.fail_json(**result)

    _ensure_required(module, params, REQUIRED_CREATE_PATH_PARAMS or CREATE_PATH_PARAMS, 'create')

    if module.check_mode:
        result['changed'] = True
        result['msg'] = 'Create planned (check_mode)'
        module.exit_json(**result)

    create_url = _build_url(api_url, CREATE_PATH, _collect_params(params, CREATE_PATH_PARAMS), _collect_params(params, CREATE_QUERY_PARAMS))
    created = _request_json(module, CREATE_METHOD, create_url, api_token, payload=desired, expected_statuses=[200, 201, 202])[1]
    result['changed'] = True
    result['resource'] = created if isinstance(created, dict) else {'value': created}
    result['msg'] = 'Resource created'
    module.exit_json(**result)


def main() -> None:
    run_module()


if __name__ == '__main__':
    main()
