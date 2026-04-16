---
URL: https://bitwarden.com/help/policies/
---

# Enterprise Policies

Enterprise policies allow Enterprise organizations to enforce security rules and default settings for all members, like mandating the use of a two-step login.

> [!WARNING] Enable policies before invite.
> We recommend setting enterprise policies before inviting users to your organization. Some policies will [revoke](https://bitwarden.com/help/revoke-users/) non-compliant users when turned on, and some are not retroactively enforceable.

## Set Enterprise policies

Organization owners and admins can apply Enterprise policies. To update a policy: 

1. Within the Bitwarden web app, open the Admin Console.
2. Select **Settings**.
3. Select **Policies**.
4. Select the name of the policy you want to change:

![Set Enterprise policies](https://bitwarden.com/assets/2flohk6BsRKvazjztwvzsJ/66bdf4f937a1d37646207c79e6ec24be/Set_Enterprise_policies.png)
*Set Enterprise policies*
5. Check or uncheck **Turn on**.
6. (Optional) If more options appear, configure them.
7. Select **Save**.

## Data Controls

Policies in the **Data Controls**section add guardrails to how data may be shared and dictate who owns vault data.

### Single organization

Turn on the **Single organization** policy to restrict non-owner/non-admin members of your organization from being able to join other organizations or from creating other organizations. This policy is enforced even for users who have only [accepted](https://bitwarden.com/help/managing-users/#accept/) invitation to your organization, however this policy is not enforced for owners and admins.

> [!WARNING] Non-compliance revokation warning
> **Organization members who are not owners or admins and do not comply with this policy will have access revoked when you activate this policy.**Users who have access revoked as a result of this policy will be notified via email, and must take steps to become compliant before their access can be restored.

The **Single organization** policy must be turned on before activating the following policies:

- [Account recovery administration](https://bitwarden.com/help/policies/#account-recovery-administration/)
- [Require single sign-on authentication](https://bitwarden.com/help/policies/#require-single-sign-on-authentication/)
- [Default URI match detection](https://bitwarden.com/help/policies/#default-uri-match-detection/)
- [Session timeout](https://bitwarden.com/help/policies/#session-timeout/)

If you are unable to turn off the **Single organization** policy, verify that all of the above policies are deactivated, that you don't have a [claimed domain](https://bitwarden.com/help/claimed-domains/), and then try again.

### Centralize organization ownership

Turn on the **Centralize organization ownership** policy to prevent private ownership of vault items. This adds [My Items](https://bitwarden.com/help/my-items/), an organization-owned location that can only be accessed by that member. **My Items** replaces the individual's **My vault**, shifting ownership from the user to the organization. While the member is active in the organization, administrators are unable to edit or export the user's My Items.

> [!NOTE] Centralize data ownership doesn't apply to admins and owners
> This policy only affects members who are not organization owners or admins. Organization owners and admins can continue using **My vault**.

Once turned on, all new saved items are placed in that member’s **My Items** by default. When on the Add Item screen, a banner informs users that a policy affects item ownership options.

After a [member is removed](https://bitwarden.com/help/remove-users/), the data in that member’s **My Items** stays with the organization. Owners, admins, and some custom role users can assign other members access to the removed members’ **My Items**.

#### Prompt users to move items to the organization

Turn on this sub-option of the **Centralize organization ownership** policy to prompt users who have items currently stored in **My Vault** to [transfer all such items to organization ownership under the My items location](https://bitwarden.com/help/transfer-ownership/). This transfer procedure is a quick, one-click process. 

Members can **accept** or **decline** the prompt. Accepting transfers all individually-owned items to organization ownership, and declining will immediately revoke that member's access to the organization to allow them time to filter which items should be transferred and which should not. [Events are logged ](https://bitwarden.com/help/event-logs/#organization-events/)for either scenario.

### Send controls

Turn on the **Send controls** policy to specify options for creating and editing [Sends](https://bitwarden.com/help/about-send/). This policy is not enforced for owners and admins. When turning on this policy, you must check one of the listed options:

- **Remove Send** prevents members from creating or editing a Send. If they previously created Sends, they can view and delete them from the **Sends** page in all Bitwarden clients except the web app. Members subject to this policy can still open [received Sends](https://bitwarden.com/help/receive-send/).
- **Always show member's email address with recipients when creating or editing a Send** removes the [hide email option](https://bitwarden.com/help/send-privacy/#hide-email/), providing transparency to those who receive a Send.

> [!NOTE] Send controls, only check one setting
> Make sure you select only one setting. If you check both, members will be subject to the **Remove Send** option.

### Remove export

Turn on the **Remove export**policy to prohibit non-owner and non-admin members of your organization from [exporting their individual vault data](https://bitwarden.com/help/export-your-data/#export-an-individual-vault/). This policy is not enforced for owners and admins.

In the web app and CLI, a message is displayed to users indicating that a policy is affecting their options. In other clients, the option will simply be disabled:

![Vault export removed](https://bitwarden.com/assets/5E2871D2vZBzveBmVyv9lO/b89f979980566dda40928db1ce450507/2024-10-14_08-50-45.png)
*Vault export removed*

## Authentication

Policies in the **Authentication** section help you harden your organization's security by forcing members to have robust authentication standards to access their Bitwarden vault.

### Master password requirements

Turn on the **Master password requirements** policy to enforce a configurable set of minimum requirements for users' master password strength. Organizations can enforce:

- Minimum master password complexity
- Minimum master password length
- Types of characters required

Password complexity is calculated on a scale from 0 (weak) to 4 (strong). Bitwarden calculates password complexity using the [zxcvbn library](https://github.com/dropbox/zxcvbn).

Use the **Require existing members to change their passwords**option to require existing, non-compliant organization members, regardless of role, to update their master password during their next login. Users who create a new account from the organization invite will be prompted to create a master password that meets your requirements.

### Account recovery administration

Turn on the **Account recovery administration** policy to allow owners and admins to help members regain access to their account. With this policy, owners and admins can send members enrolled in [account recovery](https://bitwarden.com/help/account-recovery/) a link to reset their master password. By default, users must [self-enroll in account recovery](https://bitwarden.com/help/account-recovery-enrollment/#self-enrollment/) to be eligible.

To simplify account recovery enrollment, check **Require new members to be enrolled automatically** when activating the policy. This enrolls new members when their [invitation to the organization is accepted](https://bitwarden.com/help/managing-users/#accept/) and prevents them from withdrawing from account recovery. Current organization members are not retroactively added, so they still need to self-enroll.

The **Account recovery administration** policy is required for your organization to use [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/).

> [!NOTE] Single org policy required
> The [**Single organization**](https://bitwarden.com/help/policies/#single-organization/) policy must be turned on before activating this policy.

### Require single sign-on authentication

Turn on the **Require single sign-on authentication** policy to require non-owner/non-admin users to log in with SSO. If you're self-hosting, you can enforce this policy for owners and admins using [an environment variable](https://bitwarden.com/help/environment-variables/). For more information, see [Using Login with SSO](https://bitwarden.com/help/using-sso/). This policy is not enforced for owners and admins.

Members of organizations using this policy will not be able to [log in with passkeys](https://bitwarden.com/help/login-with-passkeys/).

> [!NOTE] Single org policy required
> The [**Single organization**](https://bitwarden.com/help/policies/#single-organization/) policy must be turned on before activating this policy.

### Require two-step login

Turn on the **Require two-step login** policy to require members to use any two-step login method to access their vaults. If you are using an SSO or identity provider's 2FA functionality, you don't need to enable this policy. This policy is enforced even for users who have only [accepted](https://bitwarden.com/help/managing-users/#accept/) invitation to your organization.

> [!WARNING] Non-compliance revokation warning
> **Organization members who are not owners or admins and do not comply with this policy will have access revoked when you activate this policy.**Users who have access revoked as a result of this policy will be notified via email, and must take steps to become compliant before their access can be restored.

### Block account creation for claimed domains

> [!NOTE] Pre-req "Block account creation" policy.
> A [domain must be claimed](https://bitwarden.com/help/claimed-domains/) before you can turn on this policy.

Turn on the **Block account creation for claimed domains** policy to prevent people with email addresses that match your [claimed domain](https://bitwarden.com/help/claimed-domains/) from creating a Bitwarden account outside of the organization. When this policy is on, email addresses that match your claimed domain can only be used to create Bitwarden accounts by being invited to join your organization or when [JIT provisioning using SSO](https://bitwarden.com/help/jit-provisioning/).

### Session timeout

Turn on the **Session timeout** policy to set limits and control members' [session timeout](https://bitwarden.com/help/vault-timeout/#session-timeout/) behavior. When this policy is turned on and users edit their account's **Session timeout** settings, the **Timeout** options will not exceed the maximum you picked for the organization and some, like **On browser restart** and **Never**, will not be available. This policy does not affect organization owners.

You can customize two options:

- From the **Maximum allowed timeout** dropdown menu, set a limit to how long sessions can remain active:

 - **Immediately**: When the user stops interacting with Bitwarden
 - **Custom**: After the amount of time entered in **Hours** and **Minutes**
 - **On system lock**: When the device is locked or the screensaver activates (browser extension and desktop app only)
 - **On app restart**: When the Bitwarden app is closed and reopened
 - **Never**: No maximum session duration is set.

> [!WARNING] Never timeout
> The **Never** timeout option stores your encryption key unencrypted on your device, which may hinder security. To keep your data secure, we strongly recommend choosing a different option.
- From the **Session timeout action** dropdown menu, choose what happens after a session ends. You can specify [**Lock or Log out**](https://bitwarden.com/help/vault-timeout/#session-timeout-action/) or select **User preference** to let members choose in their account settings.

> [!TIP] Log out for trusted devices
> If your organization uses [trusted devices](https://bitwarden.com/help/about-trusted-devices/), consider selecting **Log Out**. After a session times out, this allows members to access their vault without a master password via SSO on a trusted device.

> [!NOTE] Single org policy required
> The [**Single organization**](https://bitwarden.com/help/policies/#single-organization/) policy must be turned on before activating this policy.

### Remove Unlock with PIN

Turn on the **Remove Unlock with PIN** policy to prohibit members from configuring or using [unlock with PIN](https://bitwarden.com/help/unlock-with-pin/) on web apps, browser extensions, and desktop apps. This policy applies to all organization members when turned on, including admins and owners. 

> [!NOTE] Mobile support added in a future release
> Support for enforcing this policy on mobile apps is planned for a future release.

Members who are using unlock with PIN prior to the policy will have it enforced on their next log in, meaning if they have an already logged-in session they will still see the option in the UI and be able to unlock with PIN **until** they log out **or** turn off the unlock with PIN option in the client.

## Vault Management

Policies in the **Vault Management** section allow you to set default and minimum standards for your members' items.

### Password generator

Turn on the **Password generator** policy to enforce a configurable set of minimum requirements for any user-generated passwords for all members, regardless of role. Organizations can enforce:

- Password, passphrase, or user preference

**For passwords:**

- Minimum password length
- Minimum number (0-9) count
- Minimum special character (!@#$%^&*) count
- Types of characters required

**For passphrases:**

- Minimum number of words
- Whether to capitalize
- Whether to include numbers

> [!WARNING] Password generator policy warning.
> Existing non-compliant passwords **will not** be changed when this policy is turned on, nor will the items be removed from the organization. When changing or generating a password after this policy is turn on, configured policy rules will be enforced.
> 
> A banner is displayed to users on the password generator screen to indicate that a policy is affecting their generator settings.

### Default URI match detection

Turn on the **Default URI match detection** policy to set the [default URI match detection](https://bitwarden.com/help/uri-match-detection/#default-match-detection/) for your members. This helps you configure [autofill](https://bitwarden.com/help/auto-fill-browser/) to best meet your organization's security and policy needs. 

When turning on this policy, select your organization's **Default URI match detection** from the dropdown menu:

- Base domain
- Host
- Exact
- Never

> [!NOTE] Default URI policy doesn't include starts with or regex
> Users not subject to this policy have two more options when setting their individual account's default match detection: **Starts with** and **Regular expression**. These options are not offered for an organization's default because they can match unintended pages and expose credentials.

Once the policy is activated, members cannot view or change their account's **Default URI match detection** in ⚙️ **Settings** → **Autofill**. They can, however, still choose a URI match for individual login items. This policy does not affect organization owners or admins.

> [!NOTE] Single org policy required
> The [**Single organization**](https://bitwarden.com/help/policies/#single-organization/) policy must be turned on before activating this policy.

### Automatic login with SSO

Turn on the **Automatically login with SSO** policy to allow login forms to be filled and submitted automatically when accessing non-SSO apps from your identity provider. In order to enable this setting:

1. To enable the **Automatic login with SSO** policy, check the **Turn on** box, and enter your**Identity provider host** URL(s). The URL should include `protocol://domain`.

![Automatically log in users for allowed applications](https://bitwarden.com/assets/2qHW4T4CDwpQJmPK6oDDn8/e25f021aa609e6072ffa664ae757ea7f/2025-11-19_09-34-16.png)
*Automatically log in users for allowed applications*
2. As an Administrator on your IdP, add an application, or app shortcut to your end-user dashboard containing the destination URL with the added parameter `/#autosubmit=1`
3. Once the application has been saved, users may select the application from the IdP dashboard and Bitwarden will autofill and login to the application.

> [!NOTE] Automatically login users browser extension
> Automatic login with SSO will autofill data based on the users current active account on the Bitwarden browser extension. Additionally, the data autofilled will be the most recent credential that user used associated with the target application's URL.

### Activate autofill

Turn on the **Activate auto-fill**policy to automatically turn on the [autofill on page load feature](https://bitwarden.com/help/auto-fill-browser/#on-page-load/) on the browser extension for all existing and new members of the organization. If activated, members will not have the ability to disable autofill on page load.

### Remove card item type

Turn on the **Remove card item type**policy will prevent members from creating or importing credit cards to organization and individual vaults.

Users who are members of multiple organizations will still be able to use cards only in an organization that allows it, even if a different organization has activated this policy.

Existing cards will be automatically hidden, however the data will not be deleted and cards will re-appear should administrators disable the policy. 

### Remove Free Bitwarden Families sponsorship

Turn on the **Remove Free Bitwarden Families sponsorship**policy to prevent members of your organization from having the option to [redeem a free Families plan](https://bitwarden.com/help/families-for-enterprise/) through your organization.

Users who have redeemed a sponsored Families organization prior to the policy being activated will continue to have their organization sponsored until the end of the current billing cycle. Their stored payment method will be charged for the organization when the next billing cycle begins.

![Vault export removed](https://bitwarden.com/assets/5E2871D2vZBzveBmVyv9lO/b89f979980566dda40928db1ce450507/2024-10-14_08-50-45.png)
*Vault export removed*

### Automatic user confirmation

Turn on the **Automatic user confirmation** policy to automatically confirm members that accept invitations to join your organization, rather than the standard manual process. To use this policy:

1. Verify your organization's [eligibility](https://bitwarden.com/help/automatic-confirmation/). In particular, the [**Single organization**](https://bitwarden.com/help/policies/#single-organization/) policy must be turned on and all members—including the owner and admins—must be compliant before activating this policy.
2. [Contact us](https://bitwarden.com/contact/) to add the**Automatic user confirmation** policy to your Enterprise policies settings.
3. Go to **Settings** → **Policies** and turn on the now available**Automatic user confirmation** policy.
4. At least one owner, admin, or relevant custom role member must [activate the automatic confirmation setting](https://bitwarden.com/help/automatic-confirmation/#for-each-administrator/).
