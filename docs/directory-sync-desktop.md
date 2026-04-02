---
URL: https://bitwarden.com/help/directory-sync-desktop/
---

# Directory Connector Desktop App

The Directory Connector desktop app is a standalone desktop application that can be used to sync users, groups, and group associations from a selection of directory services.

![Directory Connector Desktop App ](https://bitwarden.com/assets/7r6eylncijFasEUrKXe2Hk/b6eec60c8a6452a300eeba5272c46ea4/app.png)

Directory Connector is also available as a [CLI tool](https://bitwarden.com/help/directory-sync-cli/). The desktop app and CLI [share a database and configurations](https://bitwarden.com/help/directory-sync-shared/), so **simultaneous** use on a single machine is not recommended. The recommended path is to complete configuration and testing using the [desktop app](https://bitwarden.com/help/directory-sync-desktop/), and subsequently using the [CLI](https://bitwarden.com/help/directory-sync-cli/) to [schedule automatic syncing](https://bitwarden.com/help/schedule-directory-sync/) to your production organization.

## Getting started

To get started using the Directory Connector desktop app:

1. Download the latest version of the app from our [GitHub releases page](https://github.com/bitwarden/directory-connector/releases) or by using one of the following official links:

 - 🪟 [Windows Installer (.exe)](https://bitwarden.com/download/?app=connector&platform=windows/)
 - 🪟 [Windows Portable (.exe)](https://bitwarden.com/download/?app=connector&platform=windows&variant=portable/)
 - 🍎 [macOS (.dmg)](https://bitwarden.com/download/?app=connector&platform=macos/)
 - 🐧 [Linux (.AppImage)](https://bitwarden.com/download/?app=connector&platform=linux/)
2. Set the server URL used by Directory Connector before logging in. This is required if you are self-hosting Bitwarden or using the [EU server](https://bitwarden.com/help/server-geographies/):

 1. On the Login screen, select **Settings**.
 2. In the **Server URL** field, enter the domain name for Bitwarden instance with `https://`. For example, `https://vault.bitwarden.eu` or `https://your.domain.bitwarden.com`.
 3. Select **Save**.
3. Log in to Directory Connector using your [organization API key](https://bitwarden.com/help/public-api/#authentication/). If you don't have the API key, reach out to an [organization owner](https://bitwarden.com/help/user-types-access-control/).
4. On the ⚙️ **Settings** tab, connect to your directory and configure [sync options](https://bitwarden.com/help/user-group-filters/). This procedure will vary based on the directory in use, so refer to one of the following articles for instruction:

 - [Sync with Active Directory or LDAP](https://bitwarden.com/help/ldap-directory/)
 - [Sync with Azure Active Directory](https://bitwarden.com/help/microsoft-entra-id/)
 - [Sync with G Suite (Google)](https://bitwarden.com/help/workspace-directory/)
 - [Sync with Okta](https://bitwarden.com/help/okta-directory/)
 - [Sync with OneLogin](https://bitwarden.com/help/onelogin-directory/)

> [!NOTE] Clear sync cache
> If you are re-configuring sync options, rather than setting them for the first time, navigate to the **More** tab and select the **Clear Sync Cache** button to prevent potential conflicts with prior sync operations ([learn more](https://bitwarden.com/help/clear-sync-cache/)).
5. On the ⚙️ **Settings** tab, select your organization from the organization dropdown.
6. **Perform a Test Sync**. To check that your directory connection and sync options are successfully configured and working as expected:

 1. Open the [dashboard] **Dashboard** tab.
 2. Select the **Test Now** button.

Sync testing will query the directory server and print the results to the dashboard. Results will include:

- A list of users that will be synced from the directory.
- A list of groups that will be synced from the directory.
- A list of users that will be disabled based on their status in the directory.
- A list of users that will be deleted from your organization based on their status in the directory.

![Directory Connector test sync](https://bitwarden.com/assets/6HK5d7qPL22HYTHbgRS1tp/42127d0fde4fea4f645ea7ce807ebadc/Screenshot_2024-08-19_at_1.44.23_PM.png)
*Directory Connector test sync*

If the printed results match your expectations, you're ready to [start syncing](https://bitwarden.com/help/directory-sync-desktop/#sync-with-directory-connector/).

## Sync with Directory Connector

Directory Connector can be used to run a one-time [manual sync](https://bitwarden.com/help/directory-sync-desktop/#manual-sync/) or [automatic sync polling](https://bitwarden.com/help/directory-sync-desktop/#automatic-sync/):

### Manual sync

To run a one-time manual sync from your directory to your Bitwarden organization, open the [dashboard] **Dashboard** tab and select the [generate] **Sync Now** button.

Synced users will be invited to your organization, and groups will be immediately created.

### Automatic sync

Automatic syncing will poll your directory based on the **Interval** specified in your [sync options](https://bitwarden.com/help/user-group-filters/) as long as the application is open. If you exit or close the application, automatic sync polling will stop.

To start automatic sync polling with Directory Connector, open the [dashboard] **Dashboard** tab and select the [play] **Start Sync** button.

> [!NOTE] Teams Starter + BWDC
> If you're on the [Teams Starter](https://bitwarden.com/help/password-manager-plans/#teams-starter-organizations/) plan, you are limited to 10 members. Directory Connector will display an error and stop syncing if you try to sync more than 10 members.
> 
> **This plan is no longer available for purchase**. This error does not apply to Teams plans.
