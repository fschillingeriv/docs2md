---
URL: https://bitwarden.com/help/managing-users/
---

# User Management

## User seats

A "user seat" refers to a license for a single user within an organization. A user seat, while occupied by a member of your organization, grants that member access to Bitwarden services under your specific plan. A user seat is not permanently attached to that member; when they leave the organization that user seat is made available for use by a new member.

Bitwarden cloud [Teams and Enterprise organizations](https://bitwarden.com/help/about-organizations/#types-of-organizations/) will **automatically scale up** user seats as you [invite](https://bitwarden.com/help/managing-users/#invite/) new users. You can set a [seat limit](https://bitwarden.com/help/managing-users/#set-a-seat-limit/) on scaling to prevent your seat count from exceeding a specified number, or [manually add seats](https://bitwarden.com/help/managing-users/#manually-add-or-remove-seats/) as desired. Regardless of how you choose to add seats, you will need to [manually remove](https://bitwarden.com/help/managing-users/#manually-add-or-remove-seats/) seats you're no longer using.

Adding and removing user seats will adjust your future billing totals. Adding seats will immediately charge your payment method on file at an adjusted rate so that **you will only pay for the remainder of the billing cycle** (month/year). Removing seats will cause your next charge to be adjusted so that you are **credited for time not used** by the already-paid-for seat.

> [!NOTE] Removing seats 
> Only an an [organization owner](https://bitwarden.com/help/user-types-access-control/#default-roles/) or [provider service user](https://bitwarden.com/help/provider-users/#provider-user-types/) can add or remove seats, as this directly affects billing.

### Set a seat limit

> [!NOTE] Managing seats when you're self-hosted
> The number of seats a self-hosted organization has will always mirror its [counterpart cloud-organization](https://bitwarden.com/help/self-host-an-organization/#step-3-start-your-organization/). You will be required to manage your seat count through the cloud Admin Console, however [billing sync](https://bitwarden.com/help/licensing-on-premise/#tab-automatic-sync-4cDnzGHwlfBQEFs6eqrkut/) can be setup to make these changes reflect for your self-hosted organization without requiring you to re-upload you license.

To set a limit on the number of seats your organization can scale up to:

1. Log in to the Bitwarden [web app](https://bitwarden.com/help/getting-started-webvault/) and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
*Product switcher*
2. Navigate to **Billing** → **Subscription** and check the **Limit subscription**checkbox:

![Set a seat limit ](https://bitwarden.com/assets/5DBnJW1y9welOF6hrDKrrh/a700ae21b6f3dd20b702aa9d172ed707/2024-12-03_14-48-25.png)
*Set a seat limit *
3. In the **Seat limit** input, specify a seat limit.
4. Select **Save**.

> [!NOTE] Can't invite more when limit reached
> Once the specified limit is reached, you will not be able to invite new users unless you increase the limit.

### Manually add or remove seats

> [!NOTE] Managing seats when you're self-hosted
> The number of seats a self-hosted organization has will always mirror its [counterpart cloud-organization](https://bitwarden.com/help/self-host-an-organization/#step-3-start-your-organization/). You will be required to manage your seat count through the cloud Admin Console, however [billing sync](https://bitwarden.com/help/licensing-on-premise/#tab-automatic-sync-4cDnzGHwlfBQEFs6eqrkut/) can be setup to make these changes reflect for your self-hosted organization without requiring you to re-upload you license.

To manually add or remove seats to your organization:

1. Log in to the Bitwarden [web app](https://bitwarden.com/help/getting-started-webvault/) and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
*Product switcher*
2. Navigate to **Billing** → **Subscription.**
3. In the **Subscription seats** input, add or remove seats using the hover-over arrows:

![Add or remove seats ](https://bitwarden.com/assets/6vCLfjhJz8FOGEeAuQmYQN/f6d0bfe07c1f4db8633e735f42f121fe/2024-12-03_14-49-45.png)
*Add or remove seats *
4. Select **Save**.

> [!NOTE] Increasing subscription seats 
> If you increase your **Subscription seats** above a specified **Seat limit**, you must also increase the seat limit so that it's equal to or greater than the desired subscription seat count.

## Onboard users

To ensure the security of your organization, Bitwarden applies a three-step process for onboarding a new member: [invite](https://bitwarden.com/help/managing-users/#invite/) → [accept](https://bitwarden.com/help/managing-users/#accept/) → [confirm](https://bitwarden.com/help/managing-users/#confirm/). This is designed to facilitate secure sharing between organizations and users by maintaining end-to-end encryption.

> [!NOTE] User Management Alternatives
> This page covers the process for manually adding users to organizations. Other methods, however, are available for automatic user and group provisioning:
> 
> - Teams and Enterprise organizations can [use SCIM](https://bitwarden.com/help/about-scim/).
> - Teams and Enterprise organizations can [use Directory Sync](https://bitwarden.com/help/directory-sync/).
> - Enterprise organizations can [use JIT](https://bitwarden.com/help/jit-provisioning/).

### Invite

> [!TIP] Enterprise policy before inviting users
> For Enterprise organizations, Bitwarden recommends configuring [enterprise policies](https://bitwarden.com/help/policies/) prior to inviting members to ensure compliance on entrance to your organization.

To invite users to your organization:

1. Log in to the Bitwarden [web app](https://bitwarden.com/help/getting-started-webvault/) and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
*Product switcher*
2. Navigate to **Members** and select + **Invite User**:

![Invite member to an organization](https://bitwarden.com/assets/7AJjR4oqEnCH3A89YYoWpH/498d594fa9703bee9c5f49e2af9f83d0/Invite_member_to_an_organization.png)
*Invite member to an organization*
3. On the Invite user panel:

 - Enter the **Email** address where new users should receive invites. You can add multiple users at a time by comma-separating email addresses.
 - Select the **Member role** to be applied to new users. [Member role](https://bitwarden.com/help/user-types-access-control/) will determine what permissions these users will have at an organizational level.
 - In the **Groups**tab, select which [groups](https://bitwarden.com/help/about-groups/) to add this user to.
 - In the **Collections**tab, select collects to give this user access to and what [permissions](https://bitwarden.com/help/user-types-access-control/#permissions/) they should have to each collection.
4. Click **Save** to invite the designated users to your organization.

> [!NOTE] Invitations expire
> **Invitations expire after five days**, at which point the member will need to be re-invited. Re-invite members in bulk by selecting each member and using the ⋮ **Options icons**to select **Resend invitations**:
> 
> 
> ![Resend invitations in bulk](https://bitwarden.com/assets/1yj3MLJDTr7zOn5TwP0FGJ/67a16c6ee6ee14a92aa350986244e164/Resend_invitations.png)
> *Resend invitations in bulk*
> 
> If you're self-hosting Bitwarden, you can configure the invitation expiration period [using an environment variable](https://bitwarden.com/help/environment-variables/).

### Accept

Invited users will receive an email from Bitwarden inviting them to join the organization. Clicking the link in the email will open the Bitwarden web app, where the user can log in or create an account to accept the invitation:

![Organization invitation](https://bitwarden.com/assets/4Fe96NuWb7yRe6muKf7UbZ/bcb1a8df0bc2ffdecbcd86b82d16c9a3/2025-09-03_10-41-25.png)
*Organization invitation*

You must **fully log in to the Bitwarden web app** to accept the invitation. When you accept an invitation, an administrator will need to [confirm](https://bitwarden.com/help/managing-users/#confirm/) access. Once confirmed, you'll be notified that you can access the organization. Additionally, organization members will have their [email automatically verified](https://bitwarden.com/help/product-faqs/#q-what-features-are-unlocked-when-i-verify-my-email/) when they accept an invitation.

### Confirm

To confirm accepted invitations into your organization:

1. Log in to the Bitwarden [web app](https://bitwarden.com/help/getting-started-webvault/) and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
*Product switcher*
2. Navigate to **Members**.
3. Select any `Accepted` users and use the ⋮ options menu to ✓ **Confirm selected**:

![Confirm member to an organization](https://bitwarden.com/assets/5eRDRAooRSGqRWJYZB5fgz/f3eac670d95664be963d2b38eddf68b5/Confirm_member_to_an_organization.png)
*Confirm member to an organization*
4. Verify that the [fingerprint phrase](https://bitwarden.com/help/fingerprint-phrase/) on your screen matches the one your new member can find in **Settings** → **My account**:

![Fingerprint phrase ](https://bitwarden.com/assets/6sWPBv5GFAyMcULNxfCCJG/b3115a77e0d8d8d48fcc1f9e24e42d70/fingerprint-phrase.png)
*Fingerprint phrase *

Each fingerprint phrase is unique to its account, and ensures a final layer of oversight in securely adding users. If they match, select **Submit**.

> [!NOTE] Clear cache and cookie to restore fingerprint phrase prompt
> If **Never prompt to verify fingerprint phrases** has been toggled on, fingerprint phrase verification be reactivated by clearing the browser cache and cookies.

## Manage existing members

From the **Members** page, you can also review and update individual members' accounts, like adding them to groups, collections, or the Secrets Manager. Select the ⋮ **Menu icon** for available options per user:

![Update member](https://bitwarden.com/assets/5tspjHKPHunTlRhylIJo5O/c707a3e1780364f8820832c216b5ca64/Update_member.png)
*Update member*

### Review 2FA status

The 2FA status of users can be viewed from the **Members** page. If the user has a 🔒 **Lock icon**, two-step login is used on their Bitwarden account:

![2FA status](https://bitwarden.com/assets/HNlJNX9VJVURxGqrrBdRb/1592f5c29694cf36e973ddac553e95e1/2FA_status.png)
*2FA status*

### Download list of members

If you want to view or share a list of all organization members outside of the Admin Console, owners, admins, and [custom role](https://bitwarden.com/help/user-types-access-control/#custom-roles/) users with **Manage users** permission can export a `.csv`. This is available to all organizations.

To export your member list, go to **Members** and select the ⬇️ **Download icon**:

![Export member list](https://bitwarden.com/assets/6FCI1z0EtjbNAgeK5DZVx6/0e9b448678e95f10249a009d5d7f5aba/Export_member_list.png)
*Export member list*

> [!NOTE] Custom role, account recovery, member export
> Custom role users with **Manage account recovery** permission but not **Manage users** permission can download a `.csv` that only shows members who are enrolled in [account recovery](https://bitwarden.com/help/account-recovery/). All other members are excluded from the file.

#### Included data

The member list export includes the following information about each account:

| Column | Description |
|------|------|
| Email | The email address of the account |
| Name | The name of the user, from **Settings** → **My account** |
| Status | Shows where the account is in [onboarding](https://bitwarden.com/help/managing-users/#onboard-users/) (**Invited**, **Accepted**, or **Confirmed**) or if the account is [**Revoked**](https://bitwarden.com/help/revoke-users/) from the organization |
| Role | The user's [member role](https://bitwarden.com/help/user-types-access-control/) in the organization |
| Two-step login | Shows if the user logs in with any [two-step login method](https://bitwarden.com/help/setup-two-step-login/) |
| Account recovery | Shows if the user is enrolled in [account recovery](https://bitwarden.com/help/account-recovery/) |
| Secrets Manager | Shows if the [Secrets Manager](https://bitwarden.com/help/secrets-manager-overview/) is activated for the member |
| Groups | Lists all groups that include the member |

> [!TIP] Check collection access via Member access report
> Enterprise organizations can review the [Member access report](https://bitwarden.com/help/reports/#member-access/) to learn which collection(s) members have access to, their level of permission within each assigned collection, and more.

### Remove users

The **Members** page is also where you can withdraw someone from an organization. There are three methods:

- [Temporarily revoke access](https://bitwarden.com/help/revoke-users/)
- [Permanently remove access](https://bitwarden.com/help/remove-users/)
- [Delete organization member accounts](https://bitwarden.com/help/delete-member-accounts/)

> [!WARNING] Danger Zone
> Deleting an account is permanent and cannot be undone or restored. To create a backup of your vault data to store in a safe location, [export your vault data](https://bitwarden.com/help/export-your-data/).
