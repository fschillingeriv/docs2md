---
URL: https://bitwarden.com/help/releasenotes/
---

# Release Notes

> [!TIP] Subscribe to Release Notes
> Want Release Announcements delivered straight to your inbox? Sign up to receive an email update with the latest Bitwarden release notes.
> 
> [Contact form]
> 
> You can also subscribe to the [Bitwarden Status RSS Feed](https://status.bitwarden.com/) for service updates, including announcements of release windows.

## Overview

The releases labelled in this document represent releases of the Bitwarden server. Client applications (browser extensions, mobile apps, desktop apps, and the CLI) that are released within the same window will be listed with their specific version number, which may vary from the associated server version number. Learn more about [software release support at Bitwarden](https://bitwarden.com/help/bitwarden-software-release-support/)*.*

### Client apps and self-hosted servers

Client applications and self-hosted servers are released in the days following a server release to ensure stability. Apps distributed through app stores go through an additional approval process by the distributor. As a result, client **applications and self-hosted servers should expect to receive new features following their announcement** on this page.

### Progressive feature rollout

Some features are rolled out progressively to users over time. Features that are being rolled out in this manner may be available for some users before others.

> [!TIP] Progressive rollout star
> Features marked with a ⭐ **Star icon** are part of a progressive rollout.

### Links to GitHub

Bitwarden believes source code transparency is an absolute requirement for security solutions like ours. View full, detailed Release Notes in GitHub using any of the following links:

- [Server Releases](https://github.com/bitwarden/server/releases)
- [Web Releases](https://github.com/bitwarden/clients/releases/)
- [Desktop Releases](https://github.com/bitwarden/clients/releases)
- [Browser Extension Releases](https://github.com/bitwarden/clients/releases)
- [Android Releases](https://github.com/bitwarden/android/releases)
- [iOS Releases](https://github.com/bitwarden/ios/releases)
- [CLI Releases](https://github.com/bitwarden/clients/releases)
- [Directory Connector Releases](https://github.com/bitwarden/directory-connector/releases)

## Release Announcements

## 2026.4.0

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2026.4.0 and Mobile 2026.4.0.)*

#### Password Manager

- **Preview image attachments on Android**: You can now [preview image attachments](https://bitwarden.com/help/attachments/#view-an-attachment/) from within the Password Manager Android app, without having to download the file to your device. Previewing image attachments will be available on iOS in a future release.

#### Admin Console

- **Send controls Enterprise policy**: Two Enterprise policies, Send Options and Remove Send, were merged into the newly titled [Send controls policy](https://bitwarden.com/help/policies/#send-controls/). If either policy was previously turned on, the chosen options will transfer and remain unchanged.
- **Updated Enterprise Policies page**: On the Policies page, the [Enterprise Policies](https://bitwarden.com/help/policies/) are now organized into three categories: Data Controls, Authentication, and Vault Management. You can also review at a glance which policies are turned on or off.
- **Access Intelligence dashboard update**: Visualize [how at-risk applications, passwords, and members have changed over time](https://bitwarden.com/help/access-intelligence/#activity/) relative to absolute changes in application, password, and member counts with new graphs on the Access Intelligence Activity view.

## 2026.3.2

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2026.3.1, Browser Extension 2026.3.0, Mobile 2026.3.1, Desktop 2026.3.1, and CLI 2026.3.0.)*

#### Password Manager

- ⭐ **Autofill button on View Login**: Autofill credentials directly from the [View Login](https://bitwarden.com/help/auto-fill-browser/#view-login/) page in the browser extension.
- **Generator options for password protected Sends**: All password generator features are now available when creating password protected [Sends](https://bitwarden.com/help/about-send/).
- **Arm64 builds available for Linux**: Arm64 desktop builds are now available for Linux users on Snapcraft and Flathub. See [downloads](https://bitwarden.com/download/#downloads-desktop-applications/) for additional information.

#### Admin Console

- ⭐ **Automatic confirmation policy**: A new policy allows for [automatic confirmation of new members joining the organization](https://bitwarden.com/help/automatic-confirmation/). Using this policy requires an understanding of how it works and Bitwarden support must be contacted to activate it in your organization.
- ⭐ **Policy name update**: The Enforce organization data ownership policy has been renamed to [Centralize organization ownership](https://bitwarden.com/help/policies/#centralize-organization-ownership/).
- ⭐ **Transfer items from My Vault to My Items**: Organizations using the Centralize organization ownership policy can now [opt to prompt](https://bitwarden.com/help/policies/#centralize-organization-ownership/) users to [transfer items from My Vault to My Items](https://bitwarden.com/help/transfer-ownership/) using the browser extension.

## 2026.3.0

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2026.3.0, Browser Extension 2026.3.0, and Mobile 2026.3.0.)*

#### Password Manager

- **Email verification for Bitwarden Send**: Protect Sends with email verification is now available on mobile clients. Learn more about [Bitwarden Send](https://bitwarden.com/help/about-send/).

#### Authenticator

- **Session timeout for Android**: The [Bitwarden Authenticator](https://bitwarden.com/help/bitwarden-authenticator/) Android app can now be set to lock after a period of time that you can set. Unlock with your device’s chosen method, like a pin or biometric.
- **New app icon for iOS**: The [Bitwarden Authenticator](https://bitwarden.com/help/bitwarden-authenticator/) iOS app has a new app icon.

#### Admin Console

- ⭐ **Bulk invite improvements**: Several improvements have been added to the [organization user invite process](https://bitwarden.com/help/managing-users/), such as a visual status indicator and bulk-action warnings.

## 2026.2.1

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2026.2.1, Browser Extension 2026.2.0, Mobile 2026.2.1, Desktop 2026.2.1, and CLI 2026.2.0.)*

#### Password Manager

- **Email verification for Bitwarden Send**: When users create a Send, they can choose to protect it with email verification for recipients. Learn more about [Bitwarden Send](https://bitwarden.com/help/about-send/).
- **Item archiving**: Users on paid subscriptions can now [archive vault items](https://bitwarden.com/help/managing-items/#archive/) to exclude them from search and from autofill without removing them from the vault.
- **Biometric unlock for Flatpak**: Flatpak-installed desktop apps now support [unlock with biometrics](https://bitwarden.com/help/biometrics/#tab-linux-2vCWb5iFg4OqKS0B2xXpqW/).
- **Increase minimum KDF iterations**: If your PBKDF2 KDF iterations are below 600,000, the default level since [release 2023.2.0](https://bitwarden.com/help/releasenotes/#2023-2-0/), you'll be [asked to update](https://bitwarden.com/help/kdf-algorithms/#low-pbkdf2-kdf-iterations/) the setting or the increase will apply automatically when you next log in or unlock with your master password.

#### Admin Console

- **Huntress SIEM integration**: Bitwarden Teams and Enterprise organizations can now [integrate with Huntress](https://bitwarden.com/help/huntress-siem/) for security information and event management (SIEM).

#### Secrets Manager

- **Jenkins integration:**The Bitwarden Secrets Manager CLI can now be used to [inject secrets into Jenkins Pipelines](https://bitwarden.com/help/jenkins-integration/).

## 2026.2.0

*(This listed release number is for the Bitwarden Server, other version numbers released in this cycle include Web 2026.2.0, Browser Extension 2026.1.1, and Mobile 2026.2.0.)*

#### Password Manager

- **Import SSH keys from 1Password**: [SSH keys](https://bitwarden.com/help/ssh-agent/) can now be [imported directly to Bitwarden](https://bitwarden.com/help/import-from-1password/) using the `.1pux` export format offered by 1Password.
- **Import passkeys from a Bitwarden .json**: [Passkeys](https://bitwarden.com/help/storing-passkeys/) that are [exported from Bitwarden](https://bitwarden.com/help/export-your-data/) in a .json file can now be [imported](https://bitwarden.com/help/import-data/) to a new Bitwarden account or used as a short-term backup.

#### Admin Console

- **API - New member management endpoints**: The [Public API](https://bitwarden.com/help/api/) now includes endpoints for [revoking and restoring access](https://bitwarden.com/help/revoke-users/) to organization members.

## 2026.1.1

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2026.1.1, Browser Extension 2026.1.0, Mobile 2026.1.0, Desktop 2026.1.0, and CLI 2026.1.0.)*

#### Password Manager

- **Unlock with passkeys**: Passkeys can now [unlock your web app or browser extension](https://bitwarden.com/help/login-with-passkeys/#set-up-encryption-for-unlock/). This grows existing passkey support beyond logging in, letting you access your vault without entering the master password.
- **Desktop app UI update**: The desktop app UI has been updated, and more updates will follow.
- **New default width for extensions**: Browser extensions have a new, wider default width. You can change back to the narrow version interface or to an extra wide one [from the Appearance menu](https://bitwarden.com/help/change-theme/#tab-browser-extension-1yAVQbGXha0iO7CioSiFvm/).

> [!NOTE] 2025.1.1 Desktop Announcement
> This release includes an update of our Linux desktop to Electron 39. Users of the Bitwarden Flatpak application on Fedora-based Linux distributions with KDE may experience issues with the clipboard when importing SSH keys. This is a known issue that Bitwarden is investigating.

#### Self-host

- **Enhanced error log redaction**: Error logs created for authentication tokens that are invalid, expired, or have an incorrect issuer, audience, or signature, now redact all personally identifiable information (PII) and authentication data.

## 2026.1.0

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2026.1.0.)*

#### Password Manager

- **More 2FA security keys for Premium**: Bitwarden Premium users may now use up to 10 security keys for [two-step login](https://bitwarden.com/help/setup-two-step-login/), including [passkeys](https://bitwarden.com/help/setup-two-step-login-fido/).

#### Admin Console

- **Export list of members**: All organizations can [download a .csv list of members](https://bitwarden.com/help/managing-users/#download-list-of-members/), which details when someone uses two-step login, if they can access the Secrets Manager, and more.

## 2025.12.2

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2025.12.2, Browser Extension 2025.12.1, Mobile 2025.12.1, Desktop 2025.12.1, and CLI 2025.12.1)*

#### Password Manager

> [!NOTE] 2025.12.2 Desktop App Announcements
> **Desktop App Announcement**
> 
> An issue has been fixed for the Windows portable desktop app, the result of which will automatically log users out when the app is updated to this version. Once logged back in, the Windows portable desktop app will resume working as normal.

- **Subscription storage increase**: Premium subscriptions and paid organizations now offer 5GB of storage for [attachments](https://bitwarden.com/help/attachments/) and [Sends](https://bitwarden.com/help/about-send/).
- **Updating PINs on legacy clients**: Updating Bitwarden clients from version 2025.9.0 or older to this version will require users to set their PIN again in order to continue using [unlock with PIN](https://bitwarden.com/help/unlock-with-pin/). No changes have been made to PIN requirements themselves.

#### Admin Console

- **Block account creation for claimed domains policy**: This [new policy](https://bitwarden.com/help/policies/#block-account-creation-for-claimed-domains/) will allow administrators to prevent people with email addresses that match your [claimed domain](https://bitwarden.com/help/claimed-domains/) from creating a Bitwarden account outside of the organization.
- **Optimized bulk re-inviting**: The ability to re-send organization invitations in bulk from the Admin Console, previously limited to 500 invitations per action, now supports up to 8,000 invitations per action.
- **Session timeout policy**: You can now pick from more options in the [session timeout Enterprise policy](https://bitwarden.com/help/policies/#session-timeout/): On system lock, On app restart, and Never. All of the new timeout options are enforced across all Bitwarden clients when selected.

## 2025.12.1

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2025.12.1)*

#### Password Manager

- **Import and export pages renamed**: To improve the user experience, the "Import data" and "Export vault" pages have been renamed simply "Import" and "Export" on the web app. These pages will be renamed in other clients in a future release.

#### Admin Console

- **Enterprise policy name updated**: The "Remove individual vault export" policy is now called [Remove export](https://bitwarden.com/help/policies/#remove-export/). This is a name change only; what the policy does remains the same.

#### Self-host

- **Key Connector confirmations**: To increase security, an additional organization confirmation dialogue has been added to the [Key Connector login process](https://bitwarden.com/help/about-key-connector/#log-in-using-key-connector/) for new users.

## 2025.12.0

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2025.12.0, Browser Extension 2025.12.0, Mobile 2025.12.0, Desktop 2025.12.0, and CLI 2025.12.0)*

#### Password Manager

- **Vault health alerts and password coaching**: As a new feature for Premium plans, Password Manager will now [alert users that they should update a password](https://bitwarden.com/help/change-at-risk-passwords/) when it's detected that the password is weak, re-used, or exposed and recommend that they be updated.
- **Direct import for Chrome and Brave**: Transfer your data from Chrome and Brave browsers into Bitwarden quicker than ever with [direct import](https://bitwarden.com/help/import-from-chrome/#import-directly-from-browser/).
- **Autofill and save URI**: In the browser extension, the option to **Fill & save** has been rolled into the normal **Autofill** option. Now, when selecting Autofill for an item without a matching URI, an option to [save the current website URI to the login item](https://bitwarden.com/help/uri-match-detection/#save-uri-to-existing-login-item/) will appear.

#### Admin Console

- **Prevent SSO login for revoked users**: Users that have been revoked from an organization will no longer be able to use SSO to log in to their SSO-linked account.

## 2025.11.1

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2025.11.2, iOS 2025.11.0, and Android 2025.11.1)*

#### Password Manager

- **Log in with passkeys**: Now generally available in the browser extension and web app, log in to your Bitwarden account faster and more securely using [passkeys](https://bitwarden.com/help/login-with-passkeys/).
- **Android autofill update**: Password manager on Android uses an updated [autofill match logic for Opera, Edge, and Samsung Internet](https://bitwarden.com/help/auto-fill-android/#browser-integrations/) by default. Prior to this version, this logic used only when the Compatibility Mode option was turned on.

#### Admin Console

- **Access Intelligence**: Enterprise organizations can use [Access Intelligence](https://bitwarden.com/help/access-intelligence/) to review at-risk credentials and notify members they need to [take action on those credentials](https://bitwarden.com/help/change-at-risk-passwords/).
- **Policy name update**: The Automatically log in users for allowed applications policy has been renamed to [Automatic login with SSO](https://bitwarden.com/help/policies/#automatic-login-with-sso/).

#### Self-host

- **Bitwarden lite general availability**: [Bitwarden lite](https://bitwarden.com/help/install-and-deploy-lite/), formerly Bitwarden Unified, is now generally available.
- **Environment variable update**: The self-host environment variable `globalSettings__syslog__destination` has been deprecated. Learn more about Self-hosted [environment variables](https://bitwarden.com/help/environment-variables/).

#### Security

- **No logout on KDF change**: [Changing KDF algorithm](https://bitwarden.com/help/kdf-algorithms/) will no longer log you out of client applications.

## 2025.11.0

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2025.11.0, Browser Extension 2025.11.0, Mobile 2025.11.0, Desktop 2025.11.0, and CLI 2025.11.0)*

#### Password Manager

- **Log in with passkey support on browser extensions**: Users can now log in to browser extensions [with a passkey](https://bitwarden.com/help/login-with-passkeys/). Currently, Chrome and Chromium-based browsers like Edge are supported.
- **Windows Hello update**: You can now unlock your vault with biometrics immediately after the Windows desktop app restarts, rather than entering a master password or PIN. When setting up [biometrics in the Windows desktop app](https://bitwarden.com/help/biometrics/#set-up-biometrics-for-desktop-app/), uncheck **Require master password or PIN on app restart**.
- **Right-click in web app**: In the web app Vaults view, you can now right-click to call up the same menu you'd access using the ⋮ options menu.
- **Improved sign-up flow for premium subscription**: Users seeking the benefits of a paid Bitwarden plan will find it easier to upgrade their account. Select the **Upgrade your plan** button within the web app navigation to learn more about and select a paid plan.

#### Admin Console

- **Default URI match detection for organizations**: Organization owners and admins can now choose the [default URI match detection method](https://bitwarden.com/help/policies/#default-uri-match-detection/) for their members. Members can still edit the URI match detection method for individual login items.
- **My items**: When the [Enforce organization data ownership](https://bitwarden.com/help/policies/#centralize-organization-ownership/) policy is turned on, the organization owns new members’ items by default. Members subject to this policy can now save items in a new [My items](https://bitwarden.com/help/my-items/) location, providing members with privacy while ensuring admins can transfer data after a member leaves the organization.

#### Self-host

> [!NOTE] Helm Version Update
> **Helm Charts Versioning Update**: For Bitwarden self-host Helm charts, the CalVer versioning scheme (2025.8.0) will be deprecated on November 13, 2025. Moving forward, only SemVer versions will be supported and released.

- **Backup script update**: Docker deployments utilizing the packaged [backup-db.sh script](https://bitwarden.com/help/backup-on-premise/) have been updated to the [Simple recovery model](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server?view=sql-server-ver17) to prevent transaction log file sizes from compounding.
- **Web clients require https configuration:**Self-hosted server connections will now require `https://` configuration. Server URLs without https:// will receive an error message.

## 2025.10.1

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2025.10.1 and Mobile 2025.10.1)*

#### Password Manager

- **Android Chrome integration version requirement**: To continue using the [Chrome browser integration on Android](https://bitwarden.com/help/auto-fill-android/#browser-integrations/), upgrade the Chrome app to at least version 135. This is required due structural changes in Chrome and Bitwarden autofill integration processes.

#### Admin Console

- **Sumo Logic SIEM integration**: A new integration is available for security information and event management (SIEM) [with Sumo Logic](https://bitwarden.com/help/sumo-logic-siem/). The integration offers comprehensive event coverage across authentication, organizational activities, and vault items.

## 2025.10.0

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2025.10.0, Browser Extension 2025.10.0, Mobile 2025.10.0, Desktop 2025.10.0, and CLI 2025.10.0)*

#### Password Manager

- **Direct importer for Edge, Opera, and Vivaldi browsers**: Move your data into Bitwarden quickly and securely with [direct import](https://bitwarden.com/help/import-from-chrome/#import-directly-from-browser/) for Edge, Opera, and Vivaldi browsers.
- **Simplified login screen for SSO users**: Members of organizations using the [Require single sign-on policy](https://bitwarden.com/help/policies/#require-single-sign-on-authentication/) will now have other authentication options greyed-out on the login screen, provided they've authenticated at least once on that device.

#### Secrets Manager

- **New event logs**: Secrets Manager will now [log events](https://bitwarden.com/help/event-logs/#secrets-manager-events/) when machine accounts are created, deleted, have users or groups assigned to them, and have users or groups removed from them.

#### Self-host

- **New environment variables**: New [environment variables](https://bitwarden.com/help/environment-variables/#refresh-token-variables/) are available for configuring the handling of refresh tokens, allowing users to determine the lifetime and timeout of authentication tokens on self-hosted servers.

## 2025.9.2

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2025.9.1)*

#### Admin Console

- **Member invitation subject line update**: The [email subject line](https://bitwarden.com/http://bitwarden.com/help/list-of-emails/#critical-member-emails/) for invitations to join an organization was updated.
- **Tax ID reminder**: If you're a business owner or provider admin in a country that collects [value added tax (VAT)](https://bitwarden.com/help/tax-calculation/#value-added-tax-vat/) and haven't added your tax ID yet, you'll see a banner on the Admin Console, Payment Details, and Provider Portal pages. Click **Add a Tax ID** to update the billing details with your organization's tax ID.

#### Secrets Manager

- **Terraform Provider**: Bitwarden Secrets Manager now offers a Terraform provider, capable of fetching, creating, and managing Secrets Manager secrets for your Terraform infrastructure. Learn more about the Terraform provider [here](https://bitwarden.com/help/terraform-provider/).

## Secrets Manager Kubernetes Operator 1.0.0

- **Update to default mapped secrets behavior:** The new default behavior of the Kubernetes operator will only sync secrets that been mapped in the `BitwardenSecret` object, unless otherwise specified with `onlyMappedSecrets: false`. Learn more about the Secrets Manager Kubernetes operator [here](https://bitwarden.com/help/secrets-manager-kubernetes-operator/).

## 2025.9.0

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2025.9.0, Browser Extension 2025.9.0, Mobile 2025.9.0, Desktop 2025.9.0, and CLI 2025.9.0)*

#### Password Manager

- **Device approval using browser extensions**: Approve new [trusted devices](https://bitwarden.com/help/add-a-trusted-device/) and [login with device](https://bitwarden.com/help/log-in-with-device/) requests using the browser extension.
- **CXP for iOS 26**: Users on iOS 26 can now import directly to or export directly from Bitwarden and any other iOS app that supports [FIDO's Credential Exchange Protocol](https://fidoalliance.org/specifications-credential-exchange-specifications). Learn more about [importing](https://bitwarden.com/help/import-data/) and [exporting](https://bitwarden.com/help/export-your-data/).

#### Admin Console

- **Collection settings updates**: Some collection management settings have been renamed and more granular events will now be logged when they're turned on or off. Learn more [here](https://bitwarden.com/help/collection-management/).
- **Organization SSH keys**: SSH keys created with the Bitwarden SSH agent can now be stored and shared in organization collections. Learn more about the Bitwarden SSH agent [here](https://bitwarden.com/help/ssh-agent/).

## 2025.8.1

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2025.8.2 and Mobile 2025.8.1)*

#### Password Manager

- **Card autofill for Android**: The Bitwarden Android app can now autofill cards, such as debit or credit cards, in Chrome and Chromium-based browsers. Learn more [here](https://bitwarden.com/help/auto-fill-card-id/).
- **Failed 2FA emails**: Users will now receive an email notifying them of failed login attempts that were prevented by two-step login. If you receive these emails, update your master password immediately to one that is strong, unique, and has never been used before. Learn more [here](https://bitwarden.com/help/emails-from-bitwarden/).

#### Secrets Manager

- **New event logs**: Secrets Manager will now log events when projects are accessed, created, edited, or deleted. Learn more [here](https://bitwarden.com/help/event-logs/).

## 2025.8.2

(*This listed release includes ****only Browser Extensions & Desktop Apps****. The next release to include Server updates will resume the typical version progression (2025.8.1))*

- To further protect against malicious websites, the inline autofill menu is now always displayed above other content on a web page.

## 2025.8.0

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2025.8.0, Browser Extension 2025.8.0, Mobile 2025.8.0, Desktop 2025.8.0, and CLI 2025.8.0)*

> [!NOTE] Selfhost version support
> To ensure compatibility with the latest Bitwarden release, please update both your clients and self-hosted server. Keeping your software current in accordance with the [Bitwarden software release support](https://bitwarden.com/help/bitwarden-software-release-support/) policy will help to maintain full compatibility, support, and unlock the latest Bitwarden features.

#### Admin Console

- **Remove card item type policy**: An enterprise policy was added that allows enterprise organizations to restrict the use of the card item type. Learn more [here](https://bitwarden.com/help/policies/#remove-card-item-type/).

#### Password Manager

- **Inline autofill** **password generator improvements**: The inline autofill password generator will now immediately offer to save the generated password as a new login item. Learn more about the inline autofill [here](https://bitwarden.com/help/auto-fill-browser/#inline-autofill-menu/).
- **Improved Item view**: New improvements to viewing vault items have been added. Updates include favicons and other important information presented at the top of the vault item. Learn more about vault items [here](https://bitwarden.com/help/managing-items/).
- **HTTPS now required on Android**: The Android Password Manager app now requires connection to a server using HTTPS. This change will only affect users who are self-hosting a Bitwarden server without a SSL/TLS certificate. Learn more about certificates [here](https://bitwarden.com/help/certificates/).
- **Unlock with biometrics updates**: Desktop apps must now first be unlocked with a method other than biometrics, such as PIN or master password, after application restart. Following this, biometrics can be used to unlock. Learn more about unlock with biometrics [here](https://bitwarden.com/help/biometrics/).

## 2025.7.3

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2025.7.2)*

#### Admin Console

- **Members view performance improvements**: Loading times for the Members view, particularly for organizations with large numbers of members, have been optimized.

#### Provider Portal

- **Billing update**: Providers that have not added a payment method on the **Billing** → **Subscription** page should do so as soon as possible. Providers with unpaid invoices will now be suspended 30 days after an unpaid invoice is due, including suspension of client organizations. Adding a valid payment method, for those that have not already, will ensure seamless continuation of service.

#### Self-host

- **Deprecated logging methods**: For self-hosted users, the direct integration with `syslog` in Bitwarden - enabled by overriding `enabledglobalSettings__syslog__destination` - has been deprecated in favor of integrating with Docker's `syslog` drivers. Users with the deprecated method will receive warning logs to notify them of the change. Learn more [here.](https://bitwarden.com/help/hosting-faqs/#q-how-do-i-enable-logging-to-syslog/)

## 2025.7.1

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2025.7.1, Browser Extension 2025.7.0, Desktop 2025.7.1, and CLI 2025.7.0)*

#### Password Manager

- **URI Match Detection warning update**: Users who choose to setup URI match detection with the advanced options **Starts with** and **Regular expression** will see a warning dialogue to confirm they understand the potential security risks associated with these autofill options. Learn more [here](https://bitwarden.com/help/uri-match-detection/#match-detection-options/).
- **Onscreen tips for new users - Browser extension**: To assist new users, onscreen tips have been added to the browser extension. These tips will help introduce new users to the features and components of the browser extension. Learn more [here](https://bitwarden.com/help/getting-started-browserext/).
- **Browser extension permission update**: Browser extensions on Firefox and Safari will now require the notifications permission to support [log in with device](https://bitwarden.com/help/log-in-with-device/).
- **Chromium integrations on Android**: If you use Brave or Chrome as your web browser, toggle the new **Use Brave autofill integration** or **Use Chrome autofill integration** options. Learn more [here](https://bitwarden.com/help/auto-fill-android/).

#### Secrets Manager

- **New secrets events**: Event Logs will now log when secrets are created, edited, or deleted. Learn more [here](https://bitwarden.com/help/event-logs/#secrets-manager-events/).

## 2025.7.0

(*The listed release number is for the Bitwarden Server, other version numbers released in this cycle also include Web 2025.7.0)*

#### Password Manager

- **Password Depot 17** **import**: Password Depot 17 has been added to the list of formats available for direct import into Bitwarden Password Manager. Learn more [here](https://bitwarden.com/help/import-faqs/#q-what-file-formats-does-bitwarden-support-for-import/).

#### Admin Console

- **Policy rename**: The Remove individual vault policy has been renamed to the Enforce organization data ownership policy. Learn more [here](https://bitwarden.com/help/policies/#centralize-organization-ownership/).
- **Member permissions update**: Organization members with the **Manage account recovery** permission can reset organization member's master passwords. This permission can be granted separately from the Manage users permission. Learn more [here](https://bitwarden.com/help/user-types-access-control/#permissions/).

## 2025.6.2

(*The listed release number is for the Bitwarden server, other version numbers released in this cycle also include Web 2025.6.1, Browser Extension 2025.6.0, Desktop 2025.6.0, and CLI 2025.6.0)*

> [!WARNING] Legacy Users
> Accounts using a legacy encryption scheme are no longer supported. Older accounts that were created before 2017 and have not logged into the web app since 2023 are using a legacy encryption scheme that is no longer supported. Only inactive accounts without user activity for two years may be impacted. Learn more [here](https://bitwarden.com/help/legacy-user-support/).

> [!WARNING] Kerberos is broken
> **Kerberos authentication support notice for Self-host**: In some deployment modes, self-host server versions 2025.6.0 through 2025.6.2 have had an interruption in their support for **Kerberos** external database authentication. This will be fixed in an upcoming release of the self-host server. Customers using Kerberos authentication should wait to upgrade their self-host deployments until the next release unless instructed otherwise by Bitwarden support.

#### Password Manager

- **Persistence in browser extensions when adding & editing items:** Browser extensions will now cache changes to item data for up to two minutes even if you click out of or minimize the extension window.
- **Browser extension notification redesign**: Browser extension notifications have a new look and feel. Learn more [here](https://bitwarden.com/help/autosave-from-browser-extensions/).
- **Advanced troubleshooting for mobile apps**: In mobile apps, users now have the option to to locally and temporarily log app events to help troubleshoot unexpected behaviors in the Bitwarden app. Learn more [here](https://bitwarden.com/help/flight-recorder/).

#### Bitwarden Authenticator

- **Sync TOTPs with Password Manager**: Users now have the option to seamlessly sync verification code data between Bitwarden Authenticator and Password Manager. Learn more [here](https://bitwarden.com/help/totp-sync/).

## 2025.6.1

(The listed release number is for the Bitwarden server, other version numbers released in this cycle include Web 2025.6.0 and Self-host 2025.6.1)

> [!WARNING] Kerberos is broken
> **Kerberos authentication support notice for Self-host**: In some deployment modes, self-host server versions 2025.6.0 through 2025.6.2 have had an interruption in their support for **Kerberos** external database authentication. This will be fixed in an upcoming release of the self-host server. Customers using Kerberos authentication should wait to upgrade their self-host deployments until the next release unless instructed otherwise by Bitwarden support.

#### Self-host

- **Rootless Containers for Helm**: Helm deployments can now run Bitwarden in rootless mode. Learn more [here](https://bitwarden.com/help/self-host-with-helm/#rootless-requirements/).

## 2025.5.3

#### Self-host

- **SQL version support**: Release 2025.5.3 will be the last Bitwarden release that will maintain support for SQL Server 2019. Bitwarden fully supports SQL Server 2022.

## 2025.5.2

(*The listed release number is for the Bitwarden server, other version numbers released in this cycle also include Web 2025.5.1, Browser Extension 2025.5.1, Desktop 2025.5.0, iOS 2025.5.0, Android 2025.5.0, and CLI 2025.5.0*)

> [!NOTE] 2025.5.2 Announcement
> Important changes are coming to the Bitwarden clients! To help improve security and maintainability, please note that significantly older versions will cease to function if not kept up to date. This is especially important for users of our CLI. Please ensure that you have upgraded to the latest version of any installed clients.

#### Password Manager

- **Export attachments from desktop and CLI**: On the desktop app and CLI, you can now create a `.zip` export your individual vault file attachments. Learn more [here](https://bitwarden.com/help/attachments/).
- **Support for dynamic colors on Android**: You can now apply color schemes to your Bitwarden Android app based on your wallpaper. Learn more [here](https://bitwarden.com/help/change-theme/#tab-mobile-1yAVQbGXha0iO7CioSiFvm/).
- **SSH approval settings**: A new setting is available for users who have enabled the SSH agent on the desktop app. You may specify when Bitwarden will require you to authorize access to an SSH credential stored in the vault. Learn more about SSH agent settings [here](https://bitwarden.com/help/ssh-agent/).

#### Admin Console

- **Organization sponsored Families plan**: Organizations can issue sponsored Families plans directly to employees personal email accounts, including employees that aren't members of the current organization. Learn more about sponsored Families plans [here](https://bitwarden.com/help/organization-sponsored-families-plans/).
- **Collection permissions update**: The **Can edit** and **Can edit, hidden passwords** permissions will now grant users the ability to delete collection items, unless the new **Limit item deletion to members with the Manage collection permission** has been enabled. Learn more about collection permissions [here](https://bitwarden.com/help/about-collections/#collections-permissions/).
- **New collection management setting**: To increase privilege customization, a new collection management setting has been added, **Limit item deletion to members with the Manage collection permissions**. Learn more about collection management settings [here](https://bitwarden.com/help/collection-management/).

## 2025.5.0

(*The listed release number is for the Bitwarden server, other version numbers released in this cycle also include Web 2025.5.0 and Browser Extension 2025.5.0*)

#### Password Manager

- **Enhanced PIN requirements**: On browser extensions, PINs used for unlock must now be at least 4 characters. This will be updated in other clients in future releases.
- **Export attachments from web and browser**: On the web app and browser extension, you can now create a `.zip` export that includes file attachments. This will be added to other clients in future releases. Learn more [here](https://bitwarden.com/help/attachments/).
- **Nested collections in search results**: Nested collections are now included in search results, making it easier to find relevant items. Learn more about collections [here](https://bitwarden.com/help/about-collections/).

#### Admin Console

- **Organization features previews**: The Admin Console for Teams, Families, and Free organizations will now show previews of features included in higher subscription tiers.

## 2025.4.3

(*The listed release number is for the Bitwarden server, other version numbers released in this cycle also include Web 2025.4.1, Browser Extension 2025.4.0, Desktop 2025.4.2, and CLI 2025.4.0*)

This release includes:

#### Password Manager

- **Persistence in browser extensions when approving devices:** Browser extensions will now wait for up to two minutes for approval even if you click out of or minimize the extension window in order to approve the request using the web app.
- **Master password re-prompt desktop update**: When the master password re-prompt option is active for an item, desktop apps will now gate all fields behind successful verification instead of only hidden fields. Learn more [here](https://bitwarden.com/help/managing-items/#protect-individual-items/).

#### Admin Console

- **External ID display update**: External ID will now only be displayed for the group, collection, and member dialogue if configured using SCIM, Bitwarden Directory Connector or the API. Learn more about Directory Connector [here](https://bitwarden.com/help/directory-connector/).
- **Member SSO external ID**: Member SSO external ID will be displayed in the member dialogue for members configured using SSO.

## 2025.4.0

This release includes:

#### Password Manager

- **Edge export (csv)**: Edge (csv) export has been added to the list of formats available for import into Bitwarden Password Manager. Learn more [here](https://bitwarden.com/help/import-data/).

## 2025.3.3

(*The listed release number is for the Bitwarden server, other version numbers released in this cycle also include Web 2025.3.1, Browser Extension 2025.3.2, Desktop 2025.3.2, and CLI 2025.3.0*)

This release includes:

#### Password Manager

- **Browser extension filter persistence**: For an improved experience when navigating between the browser extension and a web page, search terms and filters will now persist for up to two minutes, or until you change the active tab in your browser extension.
- **Browser extension loading times**: We have made several changes to improve the browser extension loading times. Learn more about the Bitwarden browser extension [here](https://bitwarden.com/help/getting-started-browserext/).
- **Re-order website URIs**: On the web app and browser extensions Edit Login view, you can now re-order website URIs for better visual organization using the drag-and-drop (☰ ) button.
- **FIDO2 two-step login support for Linux desktop**: Linux desktop apps now support two-step login using a FIDO2 passkey. Learn more [here](https://bitwarden.com/help/setup-two-step-login-fido/).
- **SSH agent forwarding**: Support for SSH agent forwarding has been improved on the Bitwarden Desktop app. Learn more about the Bitwarden SSH agent [here](https://bitwarden.com/help/ssh-agent/).

## 2025.3.0

This release includes:

#### My Account

- **Verification of new devices, grace period for new accounts**: Newly created accounts will be exempt from new device login protection for the first 24 hours after account creation. Learn more [here](https://bitwarden.com/help/new-device-verification/).

#### Password Manager

- **Login request banner notifications**: Login with device requests will now prompt a banner notification to appear in the web app while pending approval. Learn more about login with device [here](https://bitwarden.com/help/log-in-with-device/).

#### Admin Console

- **Domain verification renamed**: Domain verification, available for Enterprise organizations, has been renamed to "claimed domains". Learn more [here](https://bitwarden.com/help/claimed-domains/).
- **Claimed accounts**: When an Enterprise organization claims a domain, any member accounts with emails that match the domain will now be claimed by the organization, allowing account deletion by administrators. Claimed accounts also have a few other restrictions on account actions. Learn more [here](https://bitwarden.com/help/claimed-accounts/).
- **Unassigned items in reports**: Organization-owned items not assigned to a collection are now listed with interactive links for further review in organization vault health reports.

#### Self-hosting

- **Move to GitHub Container Registry**: Container images have been moved from Docker Hub to GitHub Container Registry. If you're deploying with a method that doesn't use the `bitwarden.sh` or `bitwarden.ps1` scripts, update image references to GitHub Container Registry URLs (e.g. `ghcr.io/bitwarden/image_name:version`).

## 2025.2.1

(*The listed release number is for the Bitwarden server, other versions numbers released in this cycle also include Web 2025.2.2, Browser Extension 2025.2.2, Desktop 2025.2.1, and CLI 2025.2.0*)

This release includes:

#### My Account

- **New device login protection**: To keep your account safe and secure, Bitwarden will gradually begin requiring additional verification for users who do not use two-step login or SSO. Learn more [here](https://bitwarden.com/help/new-device-verification/).
- **Update to recovery code use**: Using a recovery code, while still requiring your email address and master password, will now automatically log you into your vault and deactivate two-step login, instead of only deactivating two-step login. Learn more [here](https://bitwarden.com/help/two-step-recovery-code/#use-your-recovery-code/).
- **FIDO2 two-step login for macOS desktop**: macOS desktop apps now support two-step login using a FIDO2 passkey. Learn more [here](https://bitwarden.com/help/setup-two-step-login-fido/).

#### Password Manager

- **Click to autofill setting moved**: The Click to autofill setting on the browser extension has been moved to the **Settings** → **Appearance** tab. Learn more [here](https://bitwarden.com/help/auto-fill-browser/#customizing-autofill-behavior/).
- **Prevent duplicate passkeys on iOS**: Duplicate passkeys cannot be saved on iOS that match an existing username and service already stored in the Bitwarden vault. The existing passkey may be modified or overwritten instead. Learn more about creating passkeys [here](https://bitwarden.com/help/storing-passkeys/#using-passkeys-with-bitwarden/).
- **Enterprise single sign-on login update**: The "Use single sign-on" button has been added to the first step of the SSO login workflow in order to streamline Enterprise SSO login. Learn more [here](https://bitwarden.com/help/using-sso/#login-using-sso/).

#### Admin Console

- **Remove Unlock with PIN policy**: Enterprise organizations can now set a policy to prohibit members from using unlock with PIN in clients apps. Learn more [here](https://bitwarden.com/help/policies/#remove-unlock-with-pin/).
- **Policy non-compliance change**: Policies that previously removed members from an organization for non-compliance will now revoke those members instead. Learn more [here](https://bitwarden.com/help/managing-users/#revoke-access/).
- **Email notification for device approval requests**: Admins will now receive an email whenever a member of their organization submits a trusted device approval request. Learn more [here](https://bitwarden.com/help/approve-a-trusted-device/).

#### Provider Portal

- **Add existing organizations to Provider Portal**: Existing organizations may now be added to the Provider Portal by provider users if they are also the owner of the organization. Learn more [here](https://bitwarden.com/help/getting-started-providers/#add-an-existing-organization/).

## 2025.2.0

(*The listed release number is for the Bitwarden server, other versions numbers released in this cycle also include Web 2025.2.1*)

> [!NOTE] New device verification release note
> To keep your account safe and secure, in an upcoming release, Bitwarden will require additional verification **for users who do not use two-step login**. Users who want to avoid new device verification workflows can:
> 
> - Preemptively set up two-step login by following any of the guides on [this page](https://bitwarden.com/help/setup-two-step-login/).
> - Opt-out of this feature from the Settings → My account screen in the Danger Zone section.
> 
> Learn more [here](https://bitwarden.com/help/new-device-verification/).

This release includes:

#### Password Manager

- **Increased import item limit**: The limit to the number of items that can be in a Password Manager import has been increased. Learn more [here](https://bitwarden.com/help/import-data/).

#### Admin Console

- **Collection permissions updates:**

 - **Collection permission names updated**: Collection permission names have been updated to provide additional clarity. Learn more [here](https://bitwarden.com/help/user-types-access-control/#permissions/).
 - **Update to "Edit items, hidden passwords" permission**: To increase security, the "Edit items, hidden passwords" permission will no longer allow users to assign items within the collection to another collection.

## 2025.1.2

(*The listed release number is for the Bitwarden web app, other versions numbers released in this cycle are Server 2025.1.4, Desktop 2025.1.4, Browser Extension 2025.1.3, CLI 2025.1.3, iOS 2025.1.2, and Android 2025.1.1*)

This release includes:

#### Password Manager

- **Change vault item owner**: On the web app, you can now share a vault item directly from the Edit window by changing its owner to any organization you're a member of. Learn more [here](https://bitwarden.com/help/sharing/).
- **Block autofill for browser extensions**: Browser extensions can now specifically be instructed not to allow autofill on certain domains. Learn more [here](https://bitwarden.com/help/blocking-uris/).
- **Bitwarden Send updates on mobile**: Bitwarden Send options on mobile apps have discontinued support for setting an expiration date and deactivating the Send, in accordance with what is currently available on browser extensions. Support for these options will be discontinued in other clients in future releases. Learn more [here](https://bitwarden.com/help/send-lifespan/).

#### Plans and Pricing

- **Restart organization subscription**: Bitwarden subscriptions that have ended or lapsed will now have a 7 day grace period in which users can reactivate their subscription. Learn more about organization renewal [here](https://bitwarden.com/help/organization-renewal/).

## 2025.1.1

This release includes:

#### Password Manager

- **SSH agent**: Bitwarden users can now securely store and generate SSH keys directly with Bitwarden Password Manager. Learn more about the Bitwarden SSH agent [here](https://bitwarden.com/help/ssh-agent/).
- **Use web device approval**: Use the web app to approve new trusted devices and login with device requests. Learn more [here](https://bitwarden.com/help/log-in-with-device/).
- **Updated generator for desktop**: The password and username generator on desktop apps has had its UI refreshed to mirror newer designs from other Bitwarden apps. Learn more [here](https://bitwarden.com/help/generator/).

#### Admin Console

- **SSO external ID added to Public API responses**: Public API responses that return data on organization members will now include their SSO external identifiers when applicable. Learn more [here](https://bitwarden.com/help/api/).

#### Self-hosting

- **Legacy user encryption key migration**: When updated to server version `2025.1.3`, self-hosted servers will require users with extant legacy encryption keys, typically accounts created prior to 2021 who do not frequently use the web app, to log in to the web app to migrate legacy encryption keys.

> [!NOTE] Extant legacy security keys
> Impacted users will be logged out of, and prevented from logging in to, non-web Bitwarden clients until they have completed migration by logging into the Bitwarden web app. **To ensure there is no loss of service for your users, Bitwarden recommends**:
> 
> 1. Upgrading your self-hosted server to `2025.1.0` as soon as possible.
> 2. Notifying users that they should log in on the web app following this update to ensure extant legacy keys are migrated **before being enforced**by `2025.1.3`.
> 3. Scheduling the upgrade of your hosted server to `2025.1.3` some period of time following the notification to allow users to migrate extant legacy keys.

## 2025.1.0

This release includes:

#### Password Manager

- **More autofill customization options**: Browser extensions now have more options for customizing your autofill experience, including the ability to select the item card to autofill instead of the **Fill** button, and several quick copy actions. Learn more [here](https://bitwarden.com/help/auto-fill-browser/#customizing-autofill-behavior/).
- **Biometric unlock for Snap Store desktop app**: Password Managed desktop apps downloaded via the Snap Store now support biometric unlock. Learn more [here](https://bitwarden.com/help/biometrics/#tab-desktop-2vCWb5iFg4OqKS0B2xXpqW/).
- **Inline autofill for TOTP codes**: The inline autofill menu can now be used to select TOTP codes. Learn more about the inline autofill menu [here](https://bitwarden.com/help/auto-fill-browser/#use-the-inline-autofill-menu/).
- **Long-press to autofill on iOS**: Long-press any text field on iOS 18+ to autofill from Bitwarden. Learn more [here](https://bitwarden.com/help/auto-fill-ios/).
- **New Public API operation**: A GET operation has been added to the` /public/organization/subscription` endpoint. Learn more about the Bitwarden Public API [here](https://bitwarden.com/help/public-api/).

#### Admin Console

- **Remove Free Bitwarden Families sponsorship policy**: This policy will allow Enterprise organizations to prevent users from redeeming a sponsored Families plan through their organization. Learn more [here](https://bitwarden.com/help/families-for-enterprise/).
- **Integrations page**: An Integrations page has been added to the Admin Console navigation menu. The integrations page provides Help Center links to popular Bitwarden integrations for SSO, event management and more!

#### Provider Portal

- **Provider members can no longer export client vaults**: In order to increase security and privacy for client organizations, provider members will no longer have access to export client vaults.

## 2024.12.0

> [!NOTE] U2F Support in 2025
> In 2025, Bitwarden will begin phasing out support for FIDO Universal 2nd Factor (U2F) keys, which can be identifies as those marked **(Migrated from FIDO)** in the Two-step Login → Manage FIDO2 WebAuthn view of the web app. If you currently use a migrated U2F key, remove and re-register the key to automatically [set it up with WebAuthn](https://bitwarden.com/help/setup-two-step-login-fido/).

This release includes:

#### Password Manager

- **Browser extension & web app UI refresh:** The Bitwarden Password Manager browser extension UI has been redesigned. Some included styling changes also enhance the web app's UI. Learn more [here](https://bitwarden.com/blog/bringing-intuitive-workflows-and-visual-updates-to-the-bitwarden-browser/).
- **Web app view item panel**: The web app will now open items to a View panel, rather than directly to an Edit panel. Only users with edit access to items will be able to use the Edit button to change a vault item. Learn more [here](https://bitwarden.com/help/managing-items/).
- **Autofill TOTP codes iOS 18.0+**: Bitwarden keyboard autofill feature on iOS 18.0 (or newer) will now autofill TOTP codes in login forms. Learn more about iOS autofill [here](https://bitwarden.com/help/auto-fill-ios/).
- **PasswordXP .csv importer**: PasswordXP .csv has been added to the list of formats available for import into Bitwarden Password Manager. Learn more [here](https://bitwarden.com/help/import-data/).
- **Netwrix Password Secure .csv importer**: Netwrix Password Secure .csv has been added to the list of formats available for import into Bitwarden Password Manager. Learn more [here](https://bitwarden.com/help/import-data/).

#### Admin Console

- **SCIM for Teams organizations**: Teams organizations can now use System of Cross-domain Identity Management (SCIM) to automatically provision members and groups from a source directory. This was previously only available for Enterprise organizations. Learn more [here](https://bitwarden.com/help/about-scim/).

## 2024.11.0

This release includes:

#### My Account

- **Email verification during sign up for all clients**: Users who create a new Bitwarden account using any Bitwarden client will now be asked to verify their email before creating a master password. Learn more [here](https://bitwarden.com/help/create-bitwarden-account/).

#### Password Manager

- **Inline autofill menu password generation**: The inline autofill menu can now be used to easily generate passwords when filling out account creation or password update fields. Learn more [here](https://bitwarden.com/help/auto-fill-browser/#use-the-inline-autofill-menu/).
- **Inline autofill menu options for cards and identities**: You can now turn on and off the option to include cards and identities as suggestions in the inline autofill menu. Learn more [here](https://bitwarden.com/help/auto-fill-card-id/#using-the-inline-menu/).
- **iOS copy & paste updates**: Several updates have been added to Bitwarden on iOS copy & paste functionality for ease of use.
- **Improved error handling for non-official servers**: To help users who are using non-official Bitwarden servers, new error messaging has been added to help identify errors when connecting to a non-official server.
- **Temporarily remove 'Allow screen capture' toggle on desktop apps:**To improve the experience with this feature, it has been temporarily removed from macOS and Windows desktop apps. Desktops apps will, for now, be captured by screenshots and screen sharing.
- **Increase min number of words for passphrases**: The passphrase generator will now require that generated passphrases include at least 6 words, except on mobile clients. Learn more [here](https://bitwarden.com/help/generator/#password-types/).

#### Admin Console

- **Collection management settings update**: The limit collection creation and deletion to owners and admins setting has been separated into two individual settings for each action respectively. Learn more about collection management [here](https://bitwarden.com/help/collection-management/#collection-management-settings/).
- **Can manage permission required for deleting collection items**: The **Can manage** permission is now required in order to delete collection items. Users with **Can edit** will not longer have the capability. Learn more about member permissions [here](https://bitwarden.com/help/user-types-access-control/#permissions/).

## 2024.10.4

This release includes:

#### Admin Console

- **Restrict access to**`**bw list org-members**`**command**: This command, and the equivalent endpoint in the Vault Management API, is now restricted to owners, admins, and custom users with the "Manage users" permission.

#### Provider Portal

- **Billing system migration**: Starting this month, existing providers will begin to be migrated to the updated client organization billing system. Learn more [here](https://bitwarden.com/help/provider-billing/).

## 2024.10.2

This release includes:

#### My Account

- **Email verification during sign up**: Users who create Bitwarden accounts through the web app will now be asked to verify their email before they create a master password. Learn more [here](https://bitwarden.com/help/create-bitwarden-account/).

#### Password Manager

- **Unlock with biometrics - Linux browser extension**: Unlock with biometrics for the Bitwarden browser extension is now available for Linux users on Chromium-based browsers. Learn more [here](https://bitwarden.com/help/biometrics/#enable-unlock-with-biometrics/).
- **Desktop apps prevent screen capture:**By default, desktop apps for Windows and macOS will now prevent screen capture and recording. Learn more [here](https://bitwarden.com/help/getting-started-desktop/#next-steps/).
- **Sync a locked vault on desktop**: Desktop apps can now manually sync even when the active account is locked. Learn more [here](https://bitwarden.com/help/vault-sync/#manual-sync/).

#### Admin Console

- **Microsoft Sentinel integration:** A new native integration is available for security information and event management (SIEM) with Microsoft Sentinel. The integration offers comprehensive event coverage across authentication, organizational activities, and vault items. Learn more [here](https://bitwarden.com/help/microsoft-sentinel-siem/).
- **Ping Identity SCIM support**: System for cross-domain identity management (SCIM) with Ping Identity is now officially supported for Bitwarden organizations. Use the Ping Identity SCIM integration to automatically provision members and groups in your Bitwarden organization. Learn more [here](https://bitwarden.com/help/ping-identity-scim-integration/).
- **Upgrade plan UI improvements**: Improvements have been made to streamline the process for upgrading your organization to another plan. Learn more [here](https://bitwarden.com/help/about-organizations/#upgrade-an-organization/).
- **Automatically log in users for allowed applications policy**: This new policy will allow IdP administrators to enable non-SSO applications to automatically log in users when launched from their IdP dashboard. Learn more [here](https://bitwarden.com/help/policies/#automatically-log-in-users-for-allowed-applications/).

## 2024.9.2

This release includes:

#### Password Manager

- **PDF attachments now downloaded by default on web app**: PDFs stored as item attachments will be downloaded to your device for viewing, rather than opening in a new browser tab. Learn more [here](https://bitwarden.com/help/attachments/).

#### Secrets Manager

- **New Machine account view**: Machine accounts have a new **Config**tab, which provides a quick view of information that might be required when configuring an application to use a machine account. Learn more [here](https://bitwarden.com/help/machine-accounts/#configuration-information/).

## 2024.9.1

This release includes: 

#### Password Manager

- **Inline autofill menu for passkeys**: Use the inline autofill menu to authenticate with passkeys. Learn more [here](https://bitwarden.com/help/auto-fill-browser/#use-the-inline-autofill-menu/).

#### Admin Console

- **Member access report**: Enterprise organizations can use the member access report to monitor organization member's access to groups, collections and items. Learn more [here](https://bitwarden.com/help/reports/#member-access/).
- **Fix for removed user events**: Events are now properly logged for users removed via the Public API or Directory Connector.

## 2024.8.2

This release includes:

#### Password Manager

- **Native mobile app for iOS**: Password Manager mobile apps downloaded via the Apple App Store have been upgraded to native mobile applications. Learn more [here](https://bitwarden.com/help/native-mobile-apps-release/).
- **Password generator for password-protected exports**: Bitwarden can now generate unique passwords for password-protected exports. Learn more about password-protected exports [here](https://bitwarden.com/help/encrypted-export/#create-an-encrypted-export/).

#### Admin Console

- **Rapid7 SIEM integration:**Bitwarden organizations can now use Rapid7 for security information and event management (SIEM). Learn more [here](https://bitwarden.com/help/rapid7-siem/).

## 2024.8.0

> [!NOTE] Native mobile apps coming soon
> In a **future** release, Password Manager mobile apps downloaded via the Apple App Store and Google Play Store will be upgraded to native mobile applications. Learn more [here](https://bitwarden.com/help/native-mobile-apps-release/).

This release includes:

#### Password Manager

- **Autofill cards and identities**: Additional autofill methods can now fill cards and identities:

 - Autofill cards and identities using keyboard shortcuts. Learn more [here](https://bitwarden.com/help/auto-fill-card-id/#using-keyboard-shortcuts/).
 - Use the inline autofill menu for cards and identities. Learn more [here](https://bitwarden.com/help/auto-fill-card-id/#using-the-inline-menu/).
- **Unlock with biometrics Linux desktop app**: Unlock with biometrics on the Bitwarden desktop app is now available for Linux users using Polkit. Learn more [here](https://bitwarden.com/help/getting-started-desktop/#tab-3-6vQUhrVotSKFarA3cqyESG/).

#### Secrets Manager

- **Display total amount of machine accounts, projects and secrets**: The Secrets Manager navigation bar will now display the total number of machine accounts, projects, and secrets that you have access to.

#### Admin Console

- **Additional supported options when changing member decryption options**: If your organization moves from SSO with trusted devices to master password decryption, users will be prompted on next log in to create a master password instead of requiring administrators to issue one beforehand. Learn more [here](https://bitwarden.com/help/about-trusted-devices/#impact-on-master-passwords/).

#### Provider Portal

- **UI improvements**: The "People" page has been renamed to the "Members" page and the color scheme of the Provider Portal has been changed to match the Admin Console.

## 2024.7.3

This release includes:

#### Secrets Manager

- **New Secrets Manager landing page**: Quickly learn more about Secrets Manager and sign up for the product directly from the web app. Learn more [here.](https://bitwarden.com/help/secrets-manager-quick-start/#getting-to-secrets-manager/)

#### Provider Portal

- **Limiting provider access to vault items**: For added security and privacy for clients, provider users may no longer directly view, manage, or create items in client organizations' vaults. Provider users may, however, import vault data directly to client organizations.

## 2024.7.2

This release includes:

#### Provider Portal

- **Consolidated billing for new providers**: Billing procedures for providers that join Bitwarden after this release are now streamlined and managed exclusively from the Provider Portal. Existing providers will be migrated to the new billing system in a future release. Learn more [here](https://bitwarden.com/help/provider-billing/).

## 2024.7.1

This release includes:

#### Password Manager

- **Remove user verification for passkeys**: The recent update requiring user verification for using a passkey on the browser extension has been temporarily rolled back.
- **PRF-Enabled Passkeys will persist through account encryption key rotation**: PRF keys used when logging into Bitwarden with a passkey will now persist if users rotate their account encryption key. Learn more [here](https://bitwarden.com/help/account-encryption-key/#rotate-your-encryption-key/).
- **Invite clarification for emergency contacts and Providers**: Trusted emergency contacts and Provider users will now move to a "Needs confirmation" state after they've accepted an invitation to make your next steps clearer.
- **Bulk assign items to collections**: From the Vaults view, you can now bulk assign items to an organization's collections. A previous version of this feature was called "Move to organization". Learn more [here](https://bitwarden.com/help/managing-items/#assign-to-collections/).
- **Renamed adding items to folders**: From the Vaults view, the option to add item to a folder has been renamed from "Move selected" to "Add to folder". Learn more [here](https://bitwarden.com/help/folders/#move-items-to-a-folder/).
- **Deprecate desktop app setting**: The desktop app can now approve device logins by default. Learn more [here](https://bitwarden.com/help/log-in-with-device/).
- **Improved SSO identifier workflow**: Admins can now distribute the URL of the **Enterprise single sign-on** screen with their SSO identifier included as a query parameter to automatically redirect organizations members to the IdP for a more streamlined SSO experience. Learn more [here](https://bitwarden.com/help/sso-faqs/#q-do-i-need-to-enter-my-sso-identifier-every-time-i-login/).

#### Secrets Manager

- **Add direct access to a secret**: People and machine accounts can now be directly granted access to a secret rather than requiring a project as an intermediary. Learn more [here](https://bitwarden.com/help/secrets/).

#### Self-hosting

> [!NOTE] Individual item encryption server version notice
> Users should upgrade self-hosted servers to at least this version prior to the 2024.10.x release to ensure compatibility with clients using vault item keys.

- **Support for bulk device approval**: Self-hosted Bitwarden servers now support bulk device approval for SSO with trusted devices. Learn more [here](https://bitwarden.com/help/approve-a-trusted-device/#bulk-approve-requests/).

#### Security

- **Vault item keys**: An extra layer of encryption in the form of a new encryption key generated for each individual vault item has been added. Learn more [here](https://bitwarden.com/help/bitwarden-security-white-paper/#how-vault-data-is-encrypted/).

#### Plans and Pricing

- **Invoicing update, monthly-billed organizations**: Teams and Enterprise organizations billed monthly will see any prorated seat count adjustments included in their next occurring monthly invoice, rather than in a newly generated invoice per seat count change.
- **Invoicing update, annually-billed organizations**: Teams and Enterprise organizations billed annually will see any prorated seat count adjustments included in a once-a-month adjustment invoice, rather than in an immediately-generated separate invoice per seat count change.

## 2024.6.3

This release includes:

#### Password Manager

- **SSO with trusted device bulk approval**: Admins and owners may now approve trusted device requests in bulk using the [web app](https://bitwarden.com/help/approve-a-trusted-device/#bulk-approve-requests/) or [CLI](https://bitwarden.com/help/cli/#device-approval/).
- **Legacy user encryption key migration**: Bitwarden accounts created prior to 2021 will have their account encryption keys migrated to Bitwarden's modern user symmetric key. These users will be logged out of non-web Bitwarden clients until they have completed the migration by logging into the Bitwarden web client. Learn more about Bitwarden encryption [here](https://bitwarden.com/help/what-encryption-is-used/).

#### Self-hosting

- **Support for more collection management options**: Self-hosted Bitwarden servers now support the **Owners and admins can manage all collections and items** collection management option. Learn more [here](https://bitwarden.com/help/collection-management/).

## 2024.6.1

This release includes:

#### Password Manager

- **Collections management update**: A collection management option has been added that allows you to determine whether admins and owners are automatically provided management permissions to all collections, and the items therein, in your organization. Learn more [here](https://bitwarden.com/help/collection-management/).

## 2024.6.0

This release includes:

#### Password Manager

- **User verification for passkeys**: Browser extensions may now prompt users to verify with biometrics, PIN, or master password when using a stored passkey to login. Learn more [here](https://bitwarden.com/help/storing-passkeys/#tab-browser-extensions-3XutklkReT3Gw0l1qHhBem/).
- **In-product getting started**: Users that are new to Password Manager will now be shown a getting started module to help them get started protecting credentials quickly.
- **Browser extension settings reorganization**: Use the newly reorganized settings screen on browser extensions to quickly locate and modify browser extension settings.
- **Firefox extension gains full functionality in private windows**: Bitwarden browser extensions used in Firefox private windows no longer have any limitations. Learn more [here](https://bitwarden.com/help/private-mode/).
- **Additional location for product switcher**: The product switcher, used to move between Password Manager, Admin Console, Secrets Manager, and Provider Portal can now also be found in the bottom left of your navigation.
- **Password-protected export for browser extensions and desktop**: Browser extensions and desktop apps can now export password protected encrypted exports. Learn more [here](https://bitwarden.com/help/encrypted-export/#create-an-encrypted-export/).

#### Bitwarden Authenticator

- **Import to Bitwarden Authenticator**: Import data directly to Bitwarden Authenticator from a variety of other authenticator apps, including Google Authenticator, LastPass Authenticator, Raivo, and 2FAS. Learn more [here](https://bitwarden.com/help/authenticator-import-export/).

#### Secrets Manager

- **Start a Secrets Manager trial**: Start a Secrets Manager enterprise trial to test a proof-of-concept and gain access to enterprise features like SSO and SCIM integrations, enterprise policies, self-hosting, event logs, and priority support. [Sign-up for a free 7-day trial of Secrets Manager today](https://bitwarden.com/go/start-secrets-enterprise-trial/).
- **Secrets Manager Kubernetes Operator (beta)**: Use the Bitwarden Secrets Manager Kubernetes Operator to securely and efficiently integrate Secrets Manager into Kubernetes workflows. Learn more [here](https://bitwarden.com/help/secrets-manager-kubernetes-operator/).

#### Admin Console

- **Configure custom users via API**: Organization members' custom role permissions can now be configured via the Public API. Learn more [here](https://bitwarden.com/help/api/).

## 2024.5.0

This release includes:

#### Password Manager

- **Clone organization items from My vault**: Users with Can manage permission can now clone organization-owned items from their Vaults view. Learn more [here](https://bitwarden.com/help/managing-items/#clone/).
- **Browser extension platform upgrade**: Starting this week, Password Manager browser extensions will begin a gradual upgrade to a new extension platform called Manifest V3, beginning with 1% of users and increasing incrementally throughout the month of May. You do not need to take action either to initiate this upgrade or once it’s completed.

#### Admin Console

- **Splunk Cloud integration**: The Bitwarden Event Logs app is available for information and event management on Splunk Cloud Classic and Splunk Cloud Victoria. Learn more [here](https://bitwarden.com/help/splunk-siem/).

#### Self-hosting

- **Collection management and deprecation of manager role**: Self-hosted servers can now access collections management functionality and will have users with the Manager role migrated to the User role with a new Can manage permission. Learn more [here](https://bitwarden.com/help/collection-management/).

> [!TIP] Update license after FC migration
> If you're self-hosting, set your [collection management settings in your cloud organization](https://bitwarden.com/help/collection-management/) and then [update your self-hosted server's license](https://bitwarden.com/help/licensing-on-premise/#update-organization-license/) to carry those settings over to your self-hosted organization.

## 2024.4.2

This release includes:

#### Password Manager

- **Use passkeys on mobile apps**: Password Manager mobile apps can now be used to create and sign in with passkeys. This feature is available for iOS and as a beta for Android. Learn more [here](https://bitwarden.com/help/storing-passkeys/).
- **Delete stored passkeys**: Passkeys that have been stored with Bitwarden login items can now be deleted using the Bitwarden browser extension and desktop app. Learn more [here](https://bitwarden.com/help/storing-passkeys/).
- **Additional permission for browser extensions**: Browser extensions in this version require a new permission from Manifest V2 browsers to better manage content script injection. Learn more [here](https://github.com/bitwarden/clients/pull/8222).

#### Secrets Manager

- **New integrations page**: Get quick access to Secrets Manager integrations through the new page available from the Secrets Manager web app.
- **Secrets Manager CLI Docker image**: The Bitwarden Secrets Manager CLI is now available as a Docker image. Learn more [here](https://bitwarden.com/help/secrets-manager-cli/).

## Bitwarden Authenticator

Introducing the new Bitwarden Authenticator standalone mobile app. Use Bitwarden Authenticator to generate verification codes for two factor authentication for apps and websites. Download from app stores or [learn more](https://bitwarden.com/help/bitwarden-authenticator/).

## 2024.4.1

This release includes:

#### Password Manager

- **Delete stored passkeys**: Passkeys that have been stored on Bitwarden login items can now be deleted from the **Vault item** → **Edit**screen of the Bitwarden web app. Learn more [here](https://bitwarden.com/help/storing-passkeys/#delete-vault-item-passkey/).

#### Secrets Manager

- **"Service accounts" now "Machine accounts"**: Service accounts have been renamed to machine accounts.

## 2024.3.1

> [!TIP] Unassigned curfuffle
> With [recent migrations to a new permissions structure](https://bitwarden.com/help/collection-management/#collection-management-settings/) that brings greater collections management flexibility to your organization, vault items that are not assigned to a specific [collection](https://bitwarden.com/help/about-collections/) are now no longer displayed in your Password Manager **All vaults** view. [Learn how to access these items](https://bitwarden.com/help/unassigned-vault-items-moved-to-admin-console/).

This release includes:

#### Password Manager

- **New languages available for Bitwarden apps**: With the contributions of community translators, new language options are now available across Bitwarden apps! See a complete list of languages [here](https://bitwarden.com/help/localization/). Learn more about contributing to Bitwarden localization [here](https://contributing.bitwarden.com/contributing/#localization-l10n).
- **Desktop app hardware acceleration**: Bitwarden desktop apps now have an option to turn on or off hardware acceleration to optimize performance. This setting is enabled by default.

#### Admin Console

- **Bulk assign items to collections**: Organization items can be assigned to collections in bulk from the Admin Console. Learn more [here](https://bitwarden.com/help/about-collections/#bulk-assign-items-to-collections/).

## 2024.3.0

This release includes:

#### Self-hosting

- **New logs functionality for Linux deployments**: Linux deployments using the standard `bitwarden.sh` shell script can now use a new option to download compressed log files (see [here](https://bitwarden.com/help/install-on-premise-linux/#script-commands-reference/)).

## 2024.2.3

This release includes:

#### Password Manager

- **Web app navigation update:** The Bitwarden web app has been totally redesigned! We hope you enjoy the new experience ([learn more](https://bitwarden.com/blog/bitwarden-design-updating-the-navigation-in-the-web-app/)).
- **Duo 2FA login update:**Duo has introduced Universal Prompt for users and admins. Duo admins who have enabled the service will see slight changes to the Duo 2FA login process. See [here](https://bitwarden.com/help/setup-two-step-login-duo/).

#### Self-hosting

- **Support for log in with passkeys (beta)**: Self-hosted Bitwarden servers now support the log in with passkeys feature (see [here](https://bitwarden.com/help/login-with-passkeys/)).

## 2024.2.2

This release includes:

#### Admin Console

- **Collection management for end-users**: Organizations now have the option to allow all users to create and manage their own collections. This option, located on the **Organization info** screen, is opt-in for existing organizations and opt-out for organizations created after 2024.2.2 (see [here](https://bitwarden.com/help/collection-management/)).
- **Deprecation of Manager role**: When you turn on collection management, organization users with the Manager role will be migrated to the User role with a new Can manage permission over their assigned collections (see [here](https://bitwarden.com/help/user-types-access-control/)).

#### Secrets Manager

- **Ansible integration**: Use Bitwarden Secrets Manager to retrieve secrets and inject them into your Ansible playbook (see [here](https://bitwarden.com/help/ansible-integration/)).

## 2024.2.0

This release includes:

#### Password Manager

- **Browser extension TOTP capture**: Use the Bitwarden browser extension to scan a webpage and save TOTP authenticator QR codes (see [here](https://bitwarden.com/help/authenticator-keys/#scan-a-qr-code/)).
- **Increased import item quantity maximum**: Imports made to Bitwarden Password Manager can now contain roughly double the amount of data (see [here](https://bitwarden.com/help/import-data/)).

#### Admin Console

- **Unique SP entity IDs per organization**: Organizations using SAML for SSO can now upgrade their entity IDs to be unique for their organization. Doing so will require re-configuring on the IdP (see [here](https://bitwarden.com/help/configure-sso-saml/)).

#### Plans & Pricing

- **Automatic tax calculation**: Tax rates for subscriptions will now be automatically calculated based on geography by our payments sub-processor. The subtotal charged by Bitwarden will remain the same, however you may notice a change in your tax-inclusive monthly invoice.

## 2024.1.2

This release includes:

#### Password Manager

- **Passkey storage for self-hosted**: Passkeys can now be stored in self-hosted Bitwarden servers (see [here](https://bitwarden.com/help/storing-passkeys/)).

#### Admin Console

- **More collections permissions via Public API**: You can now use the Public API to hide passwords from users for any collection (see [here](https://bitwarden.com/help/api/)).

## 2024.1.0

This release includes:

#### My Account

- **Log in with passkeys (beta)**: Passkeys can be used to log in to the Bitwarden web app as an alternative to using your master password and email (see [here](https://bitwarden.com/help/login-with-passkeys/)).

#### Password Manager

- **Account switching for browser extensions**: Log in to up to 5 accounts and switch seamlessly between them when using Bitwarden browser extensions (see [here](https://bitwarden.com/help/account-switching/)).

#### Admin Console

- **Configure subscription via Public API**: Use new Public API endpoints to configure subscription information like seat count, maximum auto-scaling, and storage (see [here](https://bitwarden.com/help/api/)).
- **More organization upgrade paths**: More Bitwarden organizations can now upgrade to a different subscription without needing to contact support.

## Self-host with Helm GA

Bitwarden can now be self-hosted in Kubernetes deployments using a Helm Chart (see [here](https://bitwarden.com/help/self-host-with-helm/)).

## 2023.12.1

This release includes:

#### Password Manager

- **Auto-fill menu**: Auto-fill credentials while browsing the web by turning on the new inline auto-fill menu (see [here](https://bitwarden.com/help/auto-fill-browser/#inline-auto-fill-menu/)).

## 2023.12.0

This release includes:

#### Password Manager

- **Option to turn off prompt to use passkeys**: You can now choose whether or not your browser extension will ask to save and use passkeys. (see [here](https://bitwarden.com/help/storing-passkeys/#turn-off-passkey-prompt/)).
- **Forward Email support on mobile**: Forward Email can now be used on mobile apps as a forwarded email alias provider for the username generator (see [here](https://bitwarden.com/help/generator/#generate-a-username/)).
- **Vault health reports update**: Organization members will now see organization-owned items which they have **Can edit**access to in their individual vault health reports.

#### Admin Console

- **Elastic integration**: Bitwarden organizations can now use Elastic for security information and event management (SIEM) (see [here](https://bitwarden.com/help/elastic-siem/)).
- **CLI event logs**: Event logs viewed from the web app will now specify which events were logged by the Bitwarden CLI.

#### Secrets Manager

- **Secrets manager CLI output**: A new format has been added to output secrets as key-value pairs in the Secrets Manager CLI (v0.4.0) (see [here](https://bitwarden.com/help/secrets-manager-cli/#o-output/)).

## 2023.10.0

This release includes:

#### Password Manager

- **Save passkeys to your vault**: Passkeys can now be stored in your Bitwarden vault! Store and log in with passkeys using the Bitwarden browser extension (see [here](https://bitwarden.com/help/storing-passkeys/)).
- **Direct LastPass importer**: Import data from LastPass directly to Bitwarden using browser extensions or desktop apps, including if you're a member of a team using SSO with LastPass (see [here](https://bitwarden.com/help/import-from-lastpass/#import-to-bitwarden/)).
- **Import from browser extensions and desktop apps**: Data can now be imported to Bitwarden from browser extensions and desktop apps (see [here](https://bitwarden.com/help/import-data/)).
- **Mobile settings reorganization**: The Settings tab on mobile apps has been reorganized into more intuitive categories.
- **Support for self-hosted alias providers**: The username generator on Password Manager clients can now be connected to self-hosted Addy.io and SimpleLogin instances (see [here](https://bitwarden.com/help/generator/#tab-simplelogin-3Uj911RtQsJD9OAhUuoKrz/)).
- **Auto-fill cards and identities via context menu**: Cards and identities can now be auto-filled by browser extensions using the context menu (see [here](https://bitwarden.com/help/auto-fill-card-id/#using-the-context-menu/)).

#### Secrets Manager

- **Support for self-hosting**: Enterprise organizations can now self-host Secrets Manager (see [here](https://bitwarden.com/help/manage-your-secrets-org/#self-hosting/)).
- **New event logs view**: Service account event logs can now be accessed directly from the service accounts view (see [here](https://bitwarden.com/help/service-accounts/#service-account-events/)).

## 2023.9.0

This release includes:

- **FIDO2 WebAuthn now a free two-step login option**: The FIDO2 WebAuthn method for two-step login has been expanded to free accounts. Now every Bitwarden user can improve login security using compatible FIDO2 WebAuthn credentials, such as those device-bound to hardware security keys (see [here](https://bitwarden.com/help/setup-two-step-login-fido/)).
- **Organization member email verification**: Organization members will have their email automatically verified when they [accept an invitation](https://bitwarden.com/help/managing-users/#accept/) to join or if they are a member of an organization using [domain verification](https://bitwarden.com/help/claimed-domains/).
- **Export update**: JSON exports of vault data will now include the password history for applicable items (see [here](https://bitwarden.com/help/export-your-data/)).
- **CLI password generator options:** Generating a password using the CLI has additional option flags for customizing password complexity (see [here](https://bitwarden.com/help/generator/#generate-a-password/)).
- **ProtonPass JSON importer**: ProtonPass JSON has been added to the list of formats available for direct import into Bitwarden Password Manager (see [here](https://bitwarden.com/help/import-faqs/#q-what-file-formats-does-bitwarden-support-for-import/)).
- **Desktop app theme update**: The desktop app's dark theme has been updated!

## 2023.8.2

This release includes:

- **SSO with trusted devices:**SSO with trusted devices allows users to authenticate using SSO and decrypt their vault-stored encryption key without entering a master password (see [here](https://bitwarden.com/help/about-trusted-devices/)).
- **Manager collection access:**To reduce visibility to non-essential data, managers can now only see collections that they are assigned to.

## 2023.8.0

This release includes:

- **Secrets Manager - General availability**: Bitwarden Secrets Manager is now generally available for empowering developers, DevOps, and cybersecurity teams to centrally store, manage, automate, and deploy secrets at scale. Learn more about [Secrets Manager plans](https://bitwarden.com/help/secrets-manager-plans/) and [sign up today](https://bitwarden.com/help/sign-up-for-secrets-manager/).
- **Import to a folder or collection:**Import data directly to an existing folder, or if you're a member of an organization directly to a collection, from the **Tools** → **Import data** screen.

## 2023.7.1

This release includes:

- **Secrets Manager - CLI updates**: New commands were added for editing and creating projects and secrets, and the syntax used by the CLI has been restructured (see [here](https://bitwarden.com/help/secrets-manager-cli/)).
- **EU Cloud**: Bitwarden cloud servers are now available with vault data storage in the European Union (see [here](https://bitwarden.com/help/server-geographies/)).

## 2023.7.0

This release includes:

- **Login with device for self-hosted:**Bitwarden applications connected to self-hosted servers can now log in by sending an authentication request to a registered device instead of using a master password (see [here](https://bitwarden.com/help/log-in-with-device/)).
- **Forward Email alias integration**: Connect the Bitwarden username generator to [Forward Email](https://forwardemail.net/) for easy creation of email aliases (see [here](https://bitwarden.com/help/generator/#username-types/)).
- **Browser extension TOTP auto-fill:**Browser extensions will now auto-fill TOTP codes automatically unless you're using auto-fill on page load (see [here](https://bitwarden.com/help/auto-fill-browser/#totp-auto-fill/)).
- **Policies - Renamed Admin password reset**: The Admin password reset policy is now named Account recovery administration (see [here](https://bitwarden.com/help/account-recovery/)).
- **Use auto-fill in <textarea>s**: Bitwarden apps can now auto-fill credentials into HTML `<textarea>` elements.
- **Create folders and collections from Vaults page**: Folders and collections can now be created from the main **Vaults** page using the **New** button.

### Secrets Manager beta

This release includes:

- **Secrets Manager - Service account write access**: Service accounts can now be granted write access to projects and secrets (see [here](https://bitwarden.com/help/machine-accounts/)).

> [!TIP] SM 07/25 dependency
> Fully utilizing write access for machine accounts is dependent on a forthcoming [CLI](https://bitwarden.com/help/secrets-manager-cli/) release. For now, this simply makes the option available in the UI. Stay tuned to the [Release Notes](https://bitwarden.com/help/releasenotes/) for more information.
- **Secrets Manager - Bulk user management**: Organization members can now be added to Secrets Manager in bulk (see [here](https://bitwarden.com/help/secrets-manager-quick-start/#give-members-access/)).

## 2023.5.0

> [!WARNING] Windows 8.1 deprecation
> Beginning with the **2023.5.0** release, Password Manager desktop apps will no longer support Windows 8.1 and older or Windows Server 2012 and older.
> 
> Users of these operating systems may download a 2023.4.0 desktop app [here](https://github.com/bitwarden/clients/releases) and must disable automatic updates (learn more [here](https://bitwarden.com/help/product-faqs/#q-can-i-turn-off-automatic-updates-for-bitwarden/)). We recommend upgrading to a supported operating system, as old client versions are not guaranteed to be supported by Bitwarden cloud servers long-term and may present security risks to you in the future.

This release includes: 

- **Environment selector**: The workflow for connecting Bitwarden apps to self-hosted servers was improved. See [here](https://bitwarden.com/help/change-client-environment/).
- **Password Manager - Improved auto-fill for German HTML**: German-language HTML fields are now available for auto-fill. See [here](https://github.com/bitwarden/clients/pull/4210).
- **Self-hosting - Clarification to language around server licensing**: There is a grace period of 60 days to upload a new license to replace an expired one. See [here](https://bitwarden.com/help/licensing-on-premise/#update-organization-license/).
- **Low KDF alert**: A new alert will appear in the web app when a user's KDF iterations are lower than industry recommendations, currently 600,000 iterations. See [here](https://bitwarden.com/help/kdf-algorithms/#low-pbkdf2-kdf-iterations/).

### Secrets Manager beta

This release includes:

- **Secrets Manager - Create project during secret creation**: You can now create a new project in the secret creation menu. See [here](https://bitwarden.com/help/secrets/).

## 2023.4.0

This release includes:

- **Splunk integration:**Bitwarden organizations can now use self-hosted Splunk Enterprise for security information and event management (SIEM). Learn how to get started with Splunk [here](https://bitwarden.com/help/splunk-siem/).
- **Improved reseller billing:**Bitwarden resellers will now be the only entities with access to see billing, subscription, or payment information for their customer organizations. See [here](https://bitwarden.com/help/bitwarden-resellers/).
- **Master password requirements policy update:**If enabled, the master password requirements policy can now be set to prompt pre-existing non-compliant users to update their master passwords. See [here](https://bitwarden.com/help/policies/#master-password-requirements/).
- **Vault timeout policy update:**The vault timeout policy now provides the option to designate vault timeout actions. See [here](https://bitwarden.com/help/policies/#session-timeout/).
- **Desktop - New biometrics options**: You can now choose whether to require a master password on app start or allow biometrics on launch. See [here](https://bitwarden.com/help/biometrics/).
- **Desktop - Windows Hello security improvements**: A vulnerability related to Windows Hello and Windows Credential Manager has been addressed. As an additional measure, we recommend using the new option to require a master password on app start. See [here](https://bitwarden.com/help/biometrics/).
- **Browser extension - Improved form detection**: The logic for form detection has been improved and bug reports addressed for the browser extension’s notification bar. For a technical breakdown, see [here](https://github.com/bitwarden/clients/pull/4798).

## 2023.3.0

This release includes:

- **Domain verification:**Organizations can verify ownership of domains (e.g. `mycompany.com`), allowing users to skip the organization identifier step when using login with SSO. See [here](https://bitwarden.com/help/claimed-domains/).
- **Browser Extension - Improved auto-fill security**: Browser extensions will now disallow auto-fill on page load for untrusted iframes. Browser extensions will also warn users about untrusted iframes when manually auto-filling, using the context menu, or using keyboard shortcuts, and will warn users when auto-filling HTTP sites that expect HTTPS based on that item's saved URI(s). See [here](https://bitwarden.com/help/auto-fill-browser/).
- **Master password security checks**: Users can now check known data breaches for their prospective master password via Have I Been Pwned when creating an account or changing their master password on the web vault. See [here](https://bitwarden.com/help/reports/#data-breach-individual-vaults-only/).
- **Master password length requirement**: Master passwords must now be at least 12 characters long. This rule will be enforced for new Bitwarden accounts and for any users that [change their master password](https://bitwarden.com/help/master-password/#change-master-password/).
- **Activate auto-fill policy**: For Enterprise organizations, the Activate auto-fill policy will automatically turn on auto-fill on page load for new and existing members of your organization. See [here](https://bitwarden.com/help/policies/#activate-auto-fill/).
- **Browser Extension - Improved notification bars**: Notification bars for adding undetected items to your vault now have more intuitive workflows for users subject to the Remove individual vault policy. See [here](https://bitwarden.com/help/getting-started-browserext/#auto-save-a-login/).
- **iOS - Choose Bitwarden for verification codes**: Users on iOS 16+ can now set Bitwarden as their default application for storing verification codes when scanned codes directly from the camera app. See [here](https://bitwarden.com/help/authenticator-keys/#bitwarden-authenticator-on-ios/).
- **Mobile - Change language in-app:** Users can change the language in the Bitwarden mobile app to differ from the language set on their device OS. See [here](https://bitwarden.com/help/localization/#change-app-language/).

### Secrets Manager beta

Bitwarden Secrets Manager is now available as an open beta. Learn how to get started [here](https://bitwarden.com/help/secrets-manager-overview/).

## 2023.2.0

This release includes:

> [!NOTE] 2023.2.0 SH Announcement
> **Self-host Announcement**
> 
> In this release, we've migrated to a new [SQL client](https://devblogs.microsoft.com/dotnet/introducing-the-new-microsoftdatasqlclient/) which expects either a valid certificate or the presence of `TrustServerCertificate=True` in the [connection string](https://bitwarden.com/help/environment-variables/#included-variables/) set in `global.override.env`. Please check for one of these before updating your server.

- **Argon2:** You can now change the algorithm used to derive your account's master key to Argon2id from the **Account settings** → **Security** → **Keys** page. See [here](https://bitwarden.com/help/kdf-algorithms/). 

> [!NOTE] Switching to Argon2
> **2023-02-14**: Argon2 is supported by Bitwarden clients version 2023.2.0 and later, and switching to Argon2 via the web vault could mean other clients will not be able to load your vault until they’re updated, typically within a week after release.
- **Increased default KDF iterations for PBKDF2**: New Bitwarden accounts will use 600,000 KDF iterations for PBKDF2, as recommended by OWASP. Existing accounts can manually increase this number. See [here](https://bitwarden.com/help/what-encryption-is-used/#changing-kdf-iterations/).
- **Master password security checks**: New users who create their accounts on mobile apps, browser extensions, and desktop apps can now check known data breaches for their prospective master password via HIBP. This will be brought to the web vault in a future release. See [here](https://bitwarden.com/help/reports/#data-breach-individual-vaults-only/).
- **Organization vault updates**: As part of an ongoing effort to improve the web vault UI, some organization administration functions were redesigned, for example a consolidated **Vault**view for item and collection management as well as dedicated **Members**and **Groups** views.
- **Log in with device on additional clients:**Log in with device is now available on additional clients. Login requests can now also be initiated from browser extensions, desktop apps, and mobile apps and can now also be approved from desktop apps. See [here](https://bitwarden.com/help/log-in-with-device/).
- **Automatic license sync for self-hosted organizations:** Self-hosted organizations can enable automatic license sync in order to automatically update billing and subscription changes instead of having to manually re-upload licenses. See [here](https://bitwarden.com/help/licensing-on-premise/#update-a-renewed-organization-license/).
- **SQLite DB option for Bitwarden unified:**SQLite is now an available database option for Bitwarden unified self-hosted deployments. See [here](https://bitwarden.com/help/install-and-deploy-lite/).
- **Updated self-hosted installer URLs:** The URLs for downloading self-hosted server installers have changed. See [here](https://bitwarden.com/help/install-on-premise-linux/#install-bitwarden/) for Linux and [here](https://bitwarden.com/help/install-on-premise-windows/#install-bitwarden/) for Windows.
- **Psono importer (json)**: A new import option is available for Psono (json) exports. See [here](https://bitwarden.com/help/import-faqs/#q-what-file-formats-does-bitwarden-support-for-import/).

## 2023.1.0

This release includes:

- **Bitwarden on Apple Watch**: Bitwarden has added Apple Watch support to provide an additional option for accessing TOTP login codes. See [here](https://bitwarden.com/help/apple-watch-totp/).
- **New environment variable:**An environment variable to enforce the Require SSO authentication policy for owners and admins is now available for self-hosted servers. See [here](https://bitwarden.com/help/environment-variables/#optional-variables/).
- **Bitwarden unified - Support for custom database ports:** Unified deployments now support running the database on a custom port using a new environment variable. See [here](https://bitwarden.com/help/install-and-deploy-unified-beta/#environment-variables/).
- **Passky importer (json):**A new import option is available for unencrypted Passky (json) exports. See [here](https://bitwarden.com/help/import-faqs/#q-what-file-formats-does-bitwarden-support-for-import/).
- **Custom avatar colors:** Change the color of your avatar from the web vault **Account settings** → **My account** page.

## 2022.12.0

This release includes:

- **Browser Extension - Themed notification bars:**Themed notification bars have been added to the Bitwarden browser extension to match the popular color themes.
- **Browser Extension - UI update:** UI updates have been made to the Bitwarden browser extensions.
- **Bitwarden on Apple Watch (beta)**: Bitwarden on the Apple Watch will be available in beta to users who sign up through TestFlight and will provide an additional option for accessing TOTP login codes. Learn more [<u>here</u>](https://bitwarden.com/help/apple-watch-totp/).

### Bitwarden unified self-host deployment (beta)

Bitwarden is excited to announce the beta release for a new option available to self-host users. The Bitwarden unified deployment is light weight and flexible option for users who wish to control and deploy Bitwarden on their own server. For more information on the beta, see [here](https://bitwarden.com/help/install-and-deploy-lite/). 

## 2022.11.2

This release includes:

- **Log in with device:**Log in to the web vault by sending an authentication request to your registered mobile device instead of using your master password (see [here](https://bitwarden.com/help/log-in-with-device/)).

## 2022.11.0

> [!NOTE] 2022.11.0 Release
> This release does not include updates to the browser extension, which will remain at version 2022.10.1.

This release includes:

- **Organization vault updates:** As part of an ongoing effort to improve the web vault UI, some organization administration functions have been moved, for example into dedicated **Billing** and **Reporting**tabs.
- **Login flow updates**: To accommodate new log in options, the log in process has been separated into two screens.
- **SCIM updates**: SCIM-triggered events will now log from `SCIM` instead of `Unknown`, and the SCIM API key will now be obfuscated by default.
- **Generate username & password from iOS app extension:** "On-the-fly" generation of usernames and passwords can now be done from the iOS app extension, accessible from the Share menu while using apps like browsers.
- **New theme for mobile:**The popular Solarized Dark theme has been brought to mobile.
- **Directory Connector - Group filter queries for Google Workspace:**Query parameters can be used in group filters for Google Workspace (see [here](https://bitwarden.com/help/gsuite-directory/#specify-sync-filters/)).
- **Performance Optimization**: We've improved web vault load times and experience for accounts with access to thousands of vault items.

## 2022.10.0

This release includes:

- **Password protected encrypted export:**Encrypted `.json` exports can now be encrypted with a password of your choosing. Password protected exports can be imported to any Bitwarden account (see [here](https://bitwarden.com/help/encrypted-export/)).
- **Mobile username generator:**The username generator is now available for use on Bitwarden mobile apps (see [here](https://bitwarden.com/help/generator/#generate-a-username/)).
- **DuckDuckGo email alias integration**: Connect the Bitwarden username generator to DuckDuckGo for easy creation of email aliases (see [here](https://bitwarden.com/help/generator/#username-types/)).
- **DuckDuckGo macOS browser integration**: We've partnered with DuckDuckGo to create an integration with their [forthcoming macOS browser](https://spreadprivacy.com/introducing-duckduckgo-for-mac/)! Stay tuned for more information on when they'll launch this feature.
- **SCIM update:**Revoked users will no longer occupy licensed seats in your organization (see [here](https://bitwarden.com/help/about-scim/#revoking-&-restoring-access/)).

## 2022.9.0

This release includes:

- **Fastmail email alias integration**: Connect the Bitwarden username generator to Fastmail for easy creation of email aliases (see [here](https://bitwarden.com/help/generator/#username-types/)).
- **Provider Portal update**: The main Provider Portal screen now has at-a-glance seat and plan reporting for each client organization.
- **Organization vault export event:**When an owner or admin performs a vault export, the action will now be recorded on the organization's event logs (see [here](https://bitwarden.com/help/event-logs/)).
- **Browser Extension - Support for pre-configured environment URLs:** Self-hosting customers can now pre-configure environment URLs for browser extensions, streamlining rollout for end users by using endpoint management to deploy your configuration (see [here](https://bitwarden.com/help/deploy-clients/#browser-extensions/)).
- **Mobile - Update to Bitwarden Authenticator:** Mobile apps now have a Verification Codes screen that provides quick and easy access to your TOTPs (see [here](https://bitwarden.com/help/authenticator-keys/#viewing-totp-codes/)). We've also improved the process for adding TOTP codes to vault items through the mobile app (see [here](https://bitwarden.com/help/authenticator-keys/#scan-a-qr-code/)).
- **CLI -**`**serve**`**Origin protection**: The `serve` command will now block any requests made with an `Origin` header by default (see [here](https://bitwarden.com/help/cli/#serve/)).

## 2022.8.1

This release includes:

- **SCIM for Enterprise Organizations:**Enterprise Organizations can now use System of Cross-domain Identity Management (SCIM) to automatically provision members and groups from a source directory (see [here](https://bitwarden.com/help/about-scim/)).
- **hCaptcha for Failed Login Attempts**: You'll now receive an email and be required to complete hCaptcha validation if we detect 9 consecutive failed login attempts.

## 2022.8.0

This release includes:

- **User Revocation**: Organizations can now temporarily revoke user access to an Organization without fully removing them (see [here](https://bitwarden.com/help/managing-users/#revoke-access/)).
- **Enterprise Policies Updates**: Enterprise policy names and descriptions have been updated to better describe their impact on your Organization (see [here](https://bitwarden.com/help/policies/)).
- **Settings and Preferences Updates**: The names and descriptions of some app settings and preferences have been updated to be more intuitive.

## 2022.6.0

This release includes key features and usability improvements that make Bitwarden even better on-the-go:

- **Account Switch during Auto-fill (iOS)**: Quickly switch to another account during auto-fill by tapping the avatar button, now available on Android and iOS (see [here](https://bitwarden.com/help/auto-fill-ios/)).
- **Vault Filter for Mobile**: On mobile apps, you can now filter items by vault.
- **Org Member Premium Status**: Organization members can now use premium features like advanced 2FA methods as soon as they're invited, rather than confirmed.
- **Accessibility Improvements**: This release includes a few changes that will improve the performance of Bitwarden with assistive technologies, including the ability for users with [hCaptcha Accessibility Access](https://dashboard.hcaptcha.com/signup?type=accessibility) to use their Accessibility Cookie to skip hCaptcha challenges (now available for desktop and mobile apps).

## 2022.5.0

> [!TIP] New Versioning Schema
> **We've got new version numbering!**
> 
> To make it easier to track versions of the *many *Bitwarden apps as we move to a near-monthly release cycle, we've adopted a new version numbering system that will be**shared by all clients**. This release is `2022.5.0` because it's the base release (`.0`) of May (`.5.`) 2022 (`2022.`).

This release includes:

- **Web Vault UI Updates**: The Web Vault has received design updates, some of which improve filtering between individual and Organization vault items. This is the first phase of a multi-part project to update the Web Vault for both individual users and Organizations.
- **Families Sponsorships for Self-hosted Enterprise Orgs:**Families Organization Sponsorships can now be issued for members of self-hosted Enterprise Organizations (see [here](https://bitwarden.com/help/families-for-enterprise-self-hosted/)).
- **Username Generator - Forwarded Email Alias Type:** Integrate the username generator with SimpleLogin, Addy.io, or Firefox Relay to automate simultaneous creation of usernames and corresponding email aliases (see [here](https://bitwarden.com/help/generator/#username-types/)).
- **Item Linking:** Copy the URL of an item for use as a direct link to provide to Organization members or in documentation (see [here](https://bitwarden.com/help/link-to-an-item/)).
- **Account Switch during Auto-fill:** On Android, quickly switch to another account during auto-fill by tapping the avatar bubble (see [here](https://bitwarden.com/help/auto-fill-android/#auto-fill-while-account-switching/)).
- **Changes to Client Organization Billing:** As of this release, only [Provider](https://bitwarden.com/help/providers/) users can view billing information for [Client Organizations](https://bitwarden.com/help/providers/#client-organizations/).

## 2022-04-26

*Desktop 1.330, Browser Extension 1.58.0, Mobile 2.18.0, CLI 1.22.1, Directory Connector 2.10.1*

> [!NOTE] 2022-04-19 Announcement
> **Supportability Announcement**
> 
> As of this release, macOS desktop apps downloaded from the App Store will require macOS Mojave (10.14) or greater. `.dmg` installers, available from [bitwarden.com/download](https://bitwarden.com/download/) and Github, are not subject to the same restriction.

- **Username Generator for Browser and Desktop**: Generate usernames for new credentials using email-based conventions like plus addressing or using random words (see [here](https://bitwarden.com/help/generator/)).
- **CLI - New**`**serve**`**Option**: Use the `—hostname` option to securely bind your API web server to a host (see [here](https://bitwarden.com/help/cli/#serve/)).

## 2022-04-19

*Server 1.48.0, Web 2.28.0*

The latest release includes community-requested features and the beginning of a multi-part effort to update the web vault UI. Updates to client apps (browser extension, mobile, desktop, and CLI) will come in a follow-on release:

- **Username Generator for Web Vault**: Generate usernames for new credentials using email-based conventions like plus addressing or using random words. A follow-on release will include the username generator for browser extensions and desktop apps (see [here](https://bitwarden.com/help/generator/)).
- **Web Vault - Reports Page**: We've updated the location and feel of the Reports page to make it easier to find and take action on report results (see [here](https://bitwarden.com/help/reports/)).
- **Improvements to macOS & Safari Importer**: We've fixed some issues that resulted in the macOS and Safari importer failing to import URLs and notes properly.
- **Accessibility Improvements**: This release includes a few changes that will improve the performance of Bitwarden with assistive technologies like screen readers.

## 2022-03-22

*Browser Extension 1.57.0, Mobile 2.17.0*

Following last week's release, the following has been released for mobile apps and browser extensions:

- **Account Switching added to Mobile:**Log in to up to 5 accounts and switch seamlessly between them when using Bitwarden on Android and iOS (see [here](https://bitwarden.com/help/account-switching/)).
- **Support for Firefox Private Mode:** This release includes more robust support for Firefox Private Windows (see [here](https://bitwarden.com/help/private-mode/)).

## 2022-03-15

*Server 1.47.0, Web 2.27.0, Desktop 1.32.0, CLI 1.22.0, Directory Connector 2.9.11*

The latest release focuses on improvements to individual applications so that you can use Bitwarden exactly the way you need to. Updates to mobile apps and browser extensions will come in a follow-on release:

- **Vault Management API via CLI:**Using the new `serve` CLI command, you can make API calls to a full suite of Vault Management endpoints (see [here](https://bitwarden.com/help/cli/#serve/)).
- **Changes to export CLI Command:** `export` no longer requires a master password, however you can now use a `--password` argument to set a custom encryption/decryption password for encrypted exports (see [here](https://bitwarden.com/help/cli/#export/)).
- **New Importers:** We've added custom importers for Dashlane `.csv` files and 1Password `.1pux` files (requires 1Password v8.5+).
- **Improvements to Myki Importer:** [Learn more](https://github.com/bitwarden/jslib/pull/707).
- **Deprecation of Artifact Binding:** Due to security concerns, Artifact binding for SAML SSO configurations has been removed (learn [more](https://github.com/bitwarden/server/pull/1885)).
- **Support for Docker Compose v2**

## 2022-02-08

*Server 1.46.0, Web 2.26.0, Desktop 1.31.0, Browser Extension 1.56.0, Mobile 2.16.0, CLI 1.21.0, Directory Connector 2.9.9*

To kickoff 2022, Bitwarden is pleased to release:

- **Account Switching for Desktop:** Log in to up to 5 accounts at once in the Bitwarden desktop app. This is the beginning of a phased rollout of this feature across Bitwarden apps, with more to come soon (see [here](https://bitwarden.com/help/account-switching/)).
- **Send on iOS:** You can now share a Bitwarden Send directly from the iOS share menu (see [here](https://bitwarden.com/help/create-send/)).
- **Delete Account from Mobile:** You can now delete your Bitwarden account from the mobile app, but why would you (see [here](https://bitwarden.com/help/delete-your-account/))?
- **New Icons:** We've updated the look and feel of all Bitwarden apps with all-new icons. Feast your eyes!
- **Directory Connector - Azure AD Sync Performance:** Performance for Directory Connector syncs against Azure Active Directory has been improved. Organizations syncing with Azure AD *will not* need to change their sync configuration.
- **Back End Improvements:** We've been hard at work improving the general performance and stability of the Bitwarden platform, which will springboard some great new features in the future.

## 2021-12-07

*Server 1.45.0, Web 2.25.0, Desktop 1.30.0, Browser Extension 1.55.0, Mobile 2.15.0, CLI 1.20.0*

Bitwarden is proud to announce new enterprise features in the December release that add flexibility and value to the enterprise plans:

- **Key Connector**: (*Only available to Self-hosted Organizations*) When using Login with SSO with customer-managed encryption, the self-hosted Key Connector application serves cryptographic keys to Bitwarden clients as an alternative to requiring a Master Password for Vault decryption (see [here](https://bitwarden.com/help/about-key-connector/)).
- **Families for Enterprise**: (*Only available to Cloud-hosted Organizations, self-hosted in a future release*) Starting with this release, members of Enterprise Organizations can redeem a free [Bitwarden Families Organization](https://bitwarden.com/help/password-manager-plans/#families-organizations/) for sharing with up to 5 friends or family members. Families Organizations include all premium features for all 6 users and unlimited secure data sharing (see [here](https://bitwarden.com/help/families-for-enterprise/) for details).
- **MacOS and Safari Importer**: We've added a custom importer for passwords exported from Safari and macOS (see [here](https://bitwarden.com/help/import-from-safari/) for details).
- **New Custom Field Type**: Linked custom fields can be used to solve issues where your Browser Extension has trouble auto-filling usernames and passwords for a particular site by linking usernames and passwords to bespoke form elements (see [here](https://bitwarden.com/help/auto-fill-custom-fields/#using-linked-custom-fields/) for details).
- **Browser Extension - Unlock Vault while Auto-filling**: Trying to auto-fill with the context menu or keyboard shortcut when your Vault is locked will now prompt you to unlock your Vault and automatically auto-fill your credentials once it's unlocked.

## 2021-10-26

*Server 1.44.0, Web 2.24.0, Desktop 1.29.0, Browser Extension 1.54.0, Mobile 2.14.0, CLI 1.19.0*

The Bitwarden team is pleased to release a set of features and updates continuing our mission of making password management easy and accessible for individuals and businesses:

> [!NOTE]
> **Deprecation Announcement**: The Business Portal has been deprecated. Enterprise Organizations can configure [Policies](https://bitwarden.com/help/policies/) and [Login with SSO](https://bitwarden.com/help/about-sso/) from the Organization **Manage** tab.

- **Vault Timeout Policy**: The Vault Timeout policy will apply a maximum [Vault timeout duration](https://bitwarden.com/help/vault-timeout/) for all members of your Organization (see [here](https://bitwarden.com/help/policies/#session-timeout/) for details).
- **Disable Personal Vault Export Policy**: The Disable Personal Vault Export policy will prohibit non-Owner/non-Admin members of your Organization from exporting private Vault data (see [here](https://bitwarden.com/help/policies/#disable-personal-vault-export/) for details).
- **Auto-scale Organization Seats**: Teams and Enterprise Organizations will automatically scale up user seats as new users are invited. Organizations can set a limit on scaling to prevent the seat count from exceeding a specified number (see [here](https://bitwarden.com/help/managing-users/) for details).
- **Custom Vault Timeout**: You can now specify a custom timeframe (Hours and Minutes) for Vault Timeout (see [here](https://bitwarden.com/help/vault-timeout/#session-timeout/) for details).
- **Custom Role - Improved Collection Permissions**: Collection-management permissions for the Custom role have been expanded to include granular controls over whether the user can create, edit, or delete assigned or all Collections (see [here](https://bitwarden.com/help/user-types-access-control/#custom-role/) for details).
- **Admin Password Reset - Update Password after Reset**: Passwords reset by an Admin must now be updated by the user they belong to immediately when they log in to Bitwarden (see [here](https://bitwarden.com/help/account-recovery/#after-a-password-reset/) for details).
- **Browser Extension - Autofill Span Elements**: The Browser Extension can now auto-fill [custom fields](https://bitwarden.com/help/custom-fields/) in the innerText of HTML `<span>` elements (see [here](https://bitwarden.com/help/auto-fill-custom-fields/#html-span-elements/) for details).
- **Browser Extension - Automatic Biometrics Prompt**: The Browser Extension can now automatically prompt for your biometric input when opened. You can toggle this behavior from the ⚙️ **Settings** menu (see [here](https://bitwarden.com/help/biometrics/) for details).
- **Web Vault - Dark Mode**: The Web Vault now has dark mode (see [here](https://bitwarden.com/help/change-theme/) for details)!
- **CLI -**`**generate**`**Passphrase Options**: The `bw generate --passphrase` command now includes the options `--capitalize` and `--includeNumber` (see [here](https://bitwarden.com/help/cli/#generate/) for details).

## 2021-09-21

*Server 1.43.0, Web 2.23.0, Desktop 1.28.3, Browser Extension 1.53.0, Mobile 2.13.0, CLI 1.18.1*

The latest release of Bitwarden focuses on often requested improvements to existing functionality:

- **FIDO2 WebAuthn on Mobile**: Two-step Login via FIDO2 WebAuthn is now supported on iOS and Android (see [here](https://bitwarden.com/help/setup-two-step-login-fido/) for details).
- **Admin Password Reset - Automatic Enrollment Improvement**: The Automatic Enrollment policy option will now prevent users from withdrawing from Admin Password Reset (see [here](https://bitwarden.com/help/account-recovery/#automatic-enrollment/) for details).
- **Browser Extension - Select Folder from Save Bar**: You can now select which [Folder](https://bitwarden.com/help/folders/) to save an item to directly from the Browser Extension's save prompt (see [here](https://bitwarden.com/help/getting-started-browserext/#add-a-login/) for details).
- **Browser Extension - Custom Field Context Menu Item**: You can now copy an HTML element name directly from the Browser Extension's context menu for easy custom field creation (see [here](https://bitwarden.com/help/custom-fields/#custom-field-names/) for details).
- **Web Vault - Policies Relocation**: [Enterprise Policies](https://bitwarden.com/help/policies/) can now only be configured from your Organization's **Manage** → **Policies** screen, rather than from the Business Portal.
- **CAPTCHA Validation**: Starting with this release, we're turning on [hCaptcha](https://www.hcaptcha.com/about) validation to protect against bot attacks like credential stuffing. Please note, challenges in the CLI are delivered differently than in other client applications (see [here](https://bitwarden.com/help/cli-auth-challenges/) for CLI details).

## 2021-08-18

> [!TIP] Get Started with Provider Portal
> Interested in becoming a Provider? To get started, we ask that:
> 
> - Your business has an active Enterprise Organization.
> - Your business has a client ready to be onboarded under your Provider.
> 
> [Contact Us](https://bitwarden.com/contact/)

The latest release of Bitwarden is focused on enabling Managed Service Providers (MSPs) to support their customers' password management needs:

- **Provider Portal**: The Provider Portal allows Managed Service Providers (MSPs) and Resellers to create and administer Organizations on behalf of customers. Using the Portal, Providers can seamlessly support credential management across multiple customers (see [here](https://bitwarden.com/help/getting-started-providers/) for details).
- **Share Verbiage Change**: We've updated the [share] **Share** button to [arrow-circle-right] **Move to Organization** to make it cleared that shared items are owned by the Organization. Additionally, we've updated the "shared item" indicator ([share]) to match the Collections indicator ([collection]).
- **CLI**`**move**`**Command**: In keeping with the above item, the CLI `share` command has been changed to `move` (see [here](https://bitwarden.com/help/cli/#move/) for details).

## 2021-06-29

The Bitwarden team is happy to announce the rollout of Admin Password Reset, the latest feature purpose-built to help enterprises seeking to ensure password security at scale. This release includes:

- **Admin Password Reset**: Enterprise Organizations can enroll in Admin Password Reset to allow designated administrators to reset the Master Password of Organization users (see [here](https://bitwarden.com/help/account-recovery/) for details).
- **Master Password Re-prompt**: Use the new Master Password re-prompt option to require verification of your Master Password to access sensitive Vault items as designated by the user (see [here](https://bitwarden.com/help/managing-items/#protect-individual-items/) for details).
- **Bulk User Management**: Organization Owners and Admins can now re-send invitations, confirm accepted users, and remove users from an Organization in-bulk (see [here](https://bitwarden.com/help/managing-users/#onboard-users/) for details).
- **Event Log Export**: Export event logs directly from the Web Vault (see [here](https://bitwarden.com/help/event-logs/#export-events/) for details).
- **Directory Connector API Key Authentication**: Starting with this release, users of Directory Connector will need to use the [Organization API Key](https://bitwarden.com/help/public-api/#authentication/) to login.
- **Directory Connector Sync Limit Increase**: Directory Connector can now sync an unlimited number of users or groups, where previously the limit was set at 2000 of either. To sync more than 2000 users or groups, toggle the new Sync Option (see [here](https://bitwarden.com/help/user-group-filters/#large-syncs/) for details).
- **Autofill On Page Load Enhancements**: The Browser Extension's Auto-fill on page load feature has been upgraded to more flexibly fit users' unique needs (see [here](https://bitwarden.com/help/auto-fill-browser/#on-page-load/) for details).
- **More CLI Options**: We've added a few new CLI options, including easy retrieval of Vault item notes (`bw get notes <id>`) and the ability to set maximum access count for Sends (`bw send create --maxAccessCount <#>`).
- **Web Developer Autofill Exclusion**: Web Development contributors can now prevent the Browser Extension from auto-filling a given form element by adding a `data-bwignore` attribute (e.g. `data-bwignore="true"`) to an `<input>` element.

## 2021-05-11

The Bitwarden team is pleased to release a set of features and updates continuing our mission of making password management easy and accessible for individuals and businesses:

- **Privacy & Security Options for Send**: Use a new Send Privacy option to hide your email from recipients (see [here](https://bitwarden.com/help/send-privacy/#hide-email/) for details). To prevent abuse, File Sends will now require a verified email address. Additionally, Enterprise Organizations can implement a new policy to set the availability of the Hide Email option (see [here](https://bitwarden.com/help/policies/#send-controls/) for details).
- **FIDO Updates & Expanded Support**: Our FIDO implementation has been upgraded from FIDO U2F to FIDO2 WebAuthn, but existing FIDO U2F keys will retain their integrity. FIDO support has been expanded to more Browser Extensions and the Windows Desktop App (see [here](https://bitwarden.com/help/setup-two-step-login-fido/) for details).
- **Custom Fields for Keys**: Custom Field values have been upgraded to support up to 5000 characters, allowing storage of keys like RSA 4096-bit SSH keys (see [here](https://bitwarden.com/help/custom-fields/#custom-fields-for-keys/) for details).
- **File Size Increases**: You can now create File Attachments or File Sends that are up to 500 MB each. Due to device restrictions, the old 100 MB limit is still in place for Mobile Apps.

> [!NOTE]
> As a result of the Attachment upgrade, Attachments uploaded on the newest clients cannot be opened on older client versions. If you find you're unable to access a recently-created Attachment, upgrade your client to the newest version. (**Hint:** The Cloud Web Vault is *always* on the newest version.) **Frozen or legacy client versions**, including the Safari 13 (or earlier) macOS Desktop App & App Extension, will not support accessing these attachments.
- **Disable Browser Extension Counter**: Disable the Browser Extension badge counter using a new toggle in the ⚙️ **Settings** → **Options** menu (see [here](https://bitwarden.com/help/auto-fill-browser/) for details).
- **Biometrics for Safari**: The Safari Web Extension now includes support for Unlock with Biometrics for Safari 14+ (see [here](https://bitwarden.com/help/biometrics/) for details).
- **Search Internationalization**: Vaults can now be searched against 1 character, improving the experience for languages with 1-character words like Simplified and Traditional Chinese.
- **Sorted Weak Passwords Report**: The Weak Passwords Report is now sorted by the severity of the password's weakness (see [here](https://bitwarden.com/help/reports/#weak-passwords-report/) for details)

> [!NOTE]
> Since implementing [Soft Delete](https://bitwarden.com/help/managing-items/#items-in-the-trash/) back in 2020, we've been patient to take out the Trash. **Starting 5/15/2021**, we'll activate the nightly job that will permanently delete items that have been in your trash for 30 days or more.
> 
> Prior to 5/15/2021, we recommend digging through your Trash for anything you might want to Restore!

## 2021-03-11

Bitwarden is proud to announce the release of Bitwarden Send, and end-to-end encrypted solution for ephemeral sharing. This release includes:

- **Bitwarden Send**: Bitwarden Send is end-to-end encrypted solution for ephemeral sharing. There's lot of material about Send on our website and Help Center, but you can start [here](https://bitwarden.com/products/send/) or [here](https://bitwarden.com/help/about-send/).
- **FIDO U2F Support for Edge**: Two-step Login via FIDO U2F is now available for the Web Vault and Browser Extensions in Microsoft Edge (see [here](https://bitwarden.com/help/setup-two-step-login-fido/) for details).
- **Domain Exclusion in Browser Extensions**: Bitwarden Browser Extensions can now be configured with domains to explicitly not offer to remember passwords for (see [here](https://bitwarden.com/help/exclude-domains/) for details).
- **Improved Import Error Messages**: We've had lots of folks migrating to Bitwarden recently, so we cleaned up an import error message to help you reconcile issues faster (see [here](https://bitwarden.com/help/import-data/#length-related-import-errors/) for details).
- **Safari Web Extension Port**: Our Safari App Extension has officially been ported to a Web Extension for use with Safari 14+. Due to changes to Safari, Web Extension use is now limited to only those obtained through Mac App Store downloads (see [here](https://bitwarden.com/help/install-safari-app-extension/) for details).

## 2021-01-19 Post-Release Update

> [!NOTE]
> Biometric Unlock for Browser Extensions is available for **only Chromium-based browsers** (e.g. Chrome, Edge) with v1.48.0 of the Browser Extension, provided you have the latest version (2021-01-19) of the Desktop App.
> 
> When your Browser Extension updates to this version, you may be asked to accept a new permission for Bitwarden to `Communicate with cooperating native applications`. This permission is safe, but **optional**, and will enable the Browser Extension to communicate with the Bitwarden Desktop App, which is required to enable Biometric Unlock (see [here](https://bitwarden.com/help/biometrics/#browser-extensions/) for details). Declining this permission will allow you to use v1.48.0 without Biometric Unlock functionality.
> 
> **Biometric Unlock is currently not available for:**
> 
> - Firefox Browser Extensions below version 87.
> - Microsoft App Store Desktop Apps (a side-loaded Windows Desktop App, available at [bitwarden.com/download/](https://bitwarden.com/download/) will work fine).
> - Side-loaded MacOS Desktop Apps (an App Store Desktop app will work fine).
> 
> The Bitwarden team is investigating these and will provide updates as things progress.

## 2021-01-19

For the first major release of 2021, the Bitwarden team combined multiple major enhancements to address the critical needs of all users, including:

- **Emergency Access**: Bitwarden's new Emergency Access feature enables users to designate and manage trusted emergency contacts, who may request access to their Vault in a zero knowledge encryption environment (see [here](https://bitwarden.com/help/emergency-access/) for details).[here](https://bitwarden.com/help/emergency-access/)
- **Encrypted Exports**: Personal users and Organizations can now export Vault data in an encrypted `.json` file (see [here](https://bitwarden.com/help/encrypted-export/) for details).
- **New Role**: A Custom role is now available to allow for granular control over user permissions (see [here](https://bitwarden.com/help/user-types-access-control/#custom-role/) for details).
- **New Enterprise Policy**: The Personal Ownership policy is now available for use by Enterprise Organization (see [here](https://bitwarden.com/help/policies/#personal-ownership/) for details).
- **Biometric Unlock for Browser Extensions**: Using an integration with a native Desktop application, you can now use Biometric input to unlock Chromium-based Browser Extensions (see [here](https://bitwarden.com/help/biometrics/#browser-extensions/) for details).

## 2020-11-12

The latest release of Bitwarden adds SSO-related enhancements to all client applications, including:

- **New Enterprise Policies:** The Single Organization and Single Sign-On Authentication polices are now available for use by Enterprise Organizations (see [here](https://bitwarden.com/help/policies/) for details).
- **API Key for CLI:** Authenticate into the Bitwarden CLI using an API Key newly available from your Web Vault (see [here](https://bitwarden.com/help/personal-api-key/) for details).
- **Improvements to SSO Onboarding:** We've made some improvements to the way users are onboarded via SSO to prevent potential security risks (see [here](https://github.com/bitwarden/server/pull/945) for details).
- **GDPR Acknowledgement:** From now on, new users of Bitwarden will be asked to acknowledge a Privacy Policy on registration.
- **Android 11 Inline Auto-fill**: For devices using Android 11+, enabling the Auto-fill Service will display suggestions inline for IMEs that also support [this feature](https://developer.android.com/guide/topics/text/ime-autofill#workflow) (see [here](https://github.com/bitwarden/mobile/pull/1145) for details).

## 2020-9-30

The latest release of Bitwarden adds much-anticipated **Login with SSO** functionality for all client applications, and the Business Portal for Web Vaults. Read this [blog post](https://bitwarden.com/blog/bitwarden-launches-sso-authentication/) for more information about Login with SSO, and refer to our [documentation](https://bitwarden.com/help/about-sso/).

## Early 2020 releases

The following items were released between March and September of 2020.

- [Enterprise Policies](https://bitwarden.com/help/policies/)
- [Vault Timeout Options](https://bitwarden.com/help/vault-timeout/)
- [Trash functionality](https://bitwarden.com/help/managing-items/#deleting-an-item/)
- [Password View Permissions - "Hide Passwords"](https://bitwarden.com/help/user-types-access-control/#granular-access-control/)
- [Touch ID / Windows Hello for Desktop Applications](https://bitwarden.com/help/biometrics/#desktop-applications/)
