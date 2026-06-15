---
URL: https://bitwarden.com/help/directory-sync/
---

# About Directory Connector

> [!NOTE] Different user provisioning methods
> This article discusses only one of the available methods to invite users and manage your subscription’s seat count:
> 
> - All organizations can [manually invite users](https://bitwarden.com/help/managing-users/) and update the [seat count](https://bitwarden.com/help/manage-subscription-seats-in-your-organization/).
> - Teams and Enterprise organizations can use [SCIM](https://bitwarden.com/help/about-scim/).
> - Teams and Enterprise organizations can use [Directory Connector](https://bitwarden.com/help/directory-sync/).
> - Enterprise organizations can use [just-in-time (JIT)](https://bitwarden.com/help/jit-provisioning/).

The Bitwarden Directory Connector app:

- **Automatically provisions users, groups, and group associations** in your Bitwarden organization by pulling from a selection of source directory services. Provisioned users will be issued invitations to join the organization, and can subsequently complete the acceptance and confirmation steps of the normal [onboarding procedure](https://bitwarden.com/help/managing-users/#add-new-members/).
- **Can be configured to remove users** from your Bitwarden organization when they are disabled from the source directory. This won't delete their Bitwarden accounts, but they will lose all access to your organization.
- **Can be run on-demand or automatically** on a configured interval.

## Applications

Directory Connector is available as a cross-platform [desktop app](https://bitwarden.com/help/directory-sync-desktop/) and as a [command line interface (CLI)](https://bitwarden.com/help/directory-sync-cli/). The desktop app and CLI [share a database and configurations](https://bitwarden.com/help/directory-sync-shared/), so **simultaneous** use on a single machine is not recommended. 

The recommended path is to complete configuration and testing using the [desktop app](https://bitwarden.com/help/directory-sync-desktop/), and subsequently using the [CLI](https://bitwarden.com/help/directory-sync-cli/) to [schedule automatic syncing](https://bitwarden.com/help/schedule-directory-sync/) to your production organization.

Directory Connector can be **installed on any desktop device that can access the source directory**, including as an agent on the server that hosts your directory or on an administrator's workstation. 

> [!NOTE] Directory connector teams and enterprises
> To use Directory Connector, you must have access to your [organization API key](https://bitwarden.com/help/public-api/#authentication/) which can only be retrieved by an [organization owner](https://bitwarden.com/help/user-types-access-control/) and securely shared using [Bitwarden Send](https://bitwarden.com/help/about-send/).

### Download

Download Directory Connector now:

### Desktop app

Download the latest version of the Directory Connector desktop app from [GitHub](https://github.com/bitwarden/directory-connector/releases) or using one of the following links:

- 🪟 [Windows Installer (.exe)](https://bitwarden.com/download/?app=connector&platform=windows)
- 🪟 [Windows Portable (.exe)](https://bitwarden.com/download/?app=connector&platform=windows&variant=portable)
- 🍎 [macOS (.dmg)](https://bitwarden.com/download/?app=connector&platform=macos)
- 🐧 [Linux (.AppImage)](https://bitwarden.com/download/?app=connector&platform=linux)

### CLI

Download the latest version of the Directory Connector CLI from [GitHub](https://github.com/bitwarden/directory-connector/releases) or using one of the following links:

- 🪟 [Windows CLI (.exe)](https://bitwarden.com/download/?app=connector&platform=windows&variant=cli-zip)
- 🍎 [macOS CLI](https://bitwarden.com/download/?app=connector&platform=macos&variant=cli-zip) (ARM64-only)
- 🐧 [Linux CLI](https://bitwarden.com/download/?app=connector&platform=linux&variant=cli-zip)

As with everything at Bitwarden, Directory Connector is open source and hosted on GitHub at [github.com/bitwarden/directory-connector](https://github.com/bitwarden/directory-connector).

## Source directories

Directory Connector supports sync from the following sources:

- [Active Directory](https://bitwarden.com/help/ldap-directory/)
- [Any LDAP-based directory](https://bitwarden.com/help/ldap-directory/)
- [Microsoft Entra ID](https://bitwarden.com/help/microsoft-entra-id/)
- [Google Workspace](https://bitwarden.com/help/workspace-directory/)
- [Okta](https://bitwarden.com/help/okta-directory/)
- [OneLogin](https://bitwarden.com/help/onelogin-directory/)

### Changing email addresses 

> [!NOTE] Who can change email addresses in organizations.
> Members of organizations using [trusted devices](https://bitwarden.com/help/about-trusted-devices/) cannot change their email address unless issued a master password with [account recovery](https://bitwarden.com/help/account-recovery/).
> 
> Members of organizations using [Key Connector](https://bitwarden.com/help/about-key-connector/) cannot change their email address. Members accounts will need to [deleted](https://bitwarden.com/help/delete-member-accounts/) and re-provisioned to accommodate an email address change. Remind users to export data prior to account deletion and re-import their data once provisioned with their new email address.

Members provisioned using Directory Connector are able to change their account email address in Bitwarden and in the source directory, however in order to do so:

1. First change the email address in Bitwarden by navigating to **Settings**→ **My account**([learn more](https://bitwarden.com/help/product-faqs/#q-how-do-i-change-my-email-address/)).
2. Once the email has been changed in Bitwarden, an administrator can change the user value on the directory.
3. Re-sync the directory to implement the changes.

> [!NOTE] Changing the Bitwarden email in SCIM org
> If the user email address is updated and synced on the IdP or AD prior to updating the Bitwarden email, the updated email will be interpreted as a new user.
