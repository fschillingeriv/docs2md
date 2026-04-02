---
URL: https://bitwarden.com/help/directory-sync/
---

# About Directory Connector

The Bitwarden Directory Connector app automatically provisions users, groups, and group associations in your Bitwarden organization by pulling from a selection of source directory services. Provisioned users will be issued invitations to join the organization, and can subsequently complete the normal [onboarding procedure](https://bitwarden.com/help/managing-users/#onboard-users/).

Directory Connector can be configured to remove users from your Bitwarden organization when they are disabled from the source directory. This won't delete their Bitwarden accounts, but they will lose all access to your organization. 

> [!NOTE] Directory connector teams and enterprises
> Directory Connector functionality is available to **Teams** and **Enterprise** organizations. To use Directory Connector, you must have access to your [organization API key](https://bitwarden.com/help/public-api/#authentication/) which can only be retrieved by an [organization owner](https://bitwarden.com/help/user-types-access-control/) and securely shared using [Bitwarden Send](https://bitwarden.com/help/about-send/).

![Directory Connector Diagram](https://bitwarden.com/assets/6RFsU5sJGDLMPawg64sBqM/85c9e9f6e7758944d76c8ecb79ca4af9/Marketing_Diagram_2024__1_.png)

A Directory Connector sync operation can be run on-demand or automatically on a configured interval. Directory Connector applications can be installed as an agent on the server that hosts your directory, an administrator's workstation, or any other desktop device that can access the source directory.

Directory Connector supports sync from the following sources:

- [Active Directory](https://bitwarden.com/help/ldap-directory/)
- [Any LDAP-based directory](https://bitwarden.com/help/ldap-directory/)
- [Microsoft Entra ID](https://bitwarden.com/help/microsoft-entra-id/)
- [Google Workspace](https://bitwarden.com/help/workspace-directory/)
- [Okta](https://bitwarden.com/help/okta-directory/)
- [OneLogin](https://bitwarden.com/help/onelogin-directory/)

## Directory Connector applications

Directory Connector is available as a cross-platform [desktop app](https://bitwarden.com/help/directory-sync-desktop/) and as a [command line interface (CLI)](https://bitwarden.com/help/directory-sync-cli/). The desktop app and CLI [share a database and configurations](https://bitwarden.com/help/directory-sync-shared/), so **simultaneous** use on a single machine is not recommended. The recommended path is to complete configuration and testing using the [desktop app](https://bitwarden.com/help/directory-sync-desktop/), and subsequently using the [CLI](https://bitwarden.com/help/directory-sync-cli/) to [schedule automatic syncing](https://bitwarden.com/help/schedule-directory-sync/) to your production organization.

![Directory Connector Desktop App ](https://bitwarden.com/assets/7r6eylncijFasEUrKXe2Hk/b6eec60c8a6452a300eeba5272c46ea4/app.png)

### Download Directory Connector

Use the following links to download Directory Connector:

### Desktop app

Download the latest version of the Directory Connector desktop app from our [GitHub releases page](https://github.com/bitwarden/directory-connector/releases) or by using one of the following official links:

- 🪟 [Windows Installer (.exe)](https://bitwarden.com/download/?app=connector&platform=windows/)
- 🪟 [Windows Portable (.exe)](https://bitwarden.com/download/?app=connector&platform=windows&variant=portable/)
- 🍎 [macOS (.dmg)](https://bitwarden.com/download/?app=connector&platform=macos/)
- 🐧 [Linux (.AppImage)](https://bitwarden.com/download/?app=connector&platform=linux/)

### CLI

Download the latest version of the Directory Connector CLI from one of the following links:

- 🪟 [Windows CLI (.exe)](https://bitwarden.com/download/?app=connector&platform=windows&variant=cli-zip/)
- 🍎 [macOS CLI](https://bitwarden.com/download/?app=connector&platform=macos&variant=cli-zip/)
- 🐧 [Linux CLI](https://bitwarden.com/download/?app=connector&platform=linux&variant=cli-zip/)

## Source code

As with everything at Bitwarden, Directory Connector is open source and hosted on GitHub at [github.com/bitwarden/directory-connector](https://github.com/bitwarden/directory-connector).
