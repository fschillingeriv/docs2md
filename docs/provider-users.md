---
URL: https://bitwarden.com/help/provider-users/
---

# Provider Users

## Onboard provider users

To ensure the secure administration of your client organizations, Bitwarden applies a three-step process for onboarding a new Provider member, [Invite](https://bitwarden.com/help/provider-users/#invite/) → [Accept](https://bitwarden.com/help/provider-users/#accept/) → [Confirm](https://bitwarden.com/help/provider-users/#confirm/).

### Invite

To invite users to your Provider:

1. Log in to Bitwarden and and open the Provider Portal using the product switcher:

![Product switcher - Provider Portal](https://bitwarden.com/assets/4xn04Sj9u8n73TPxZUWi5f/dac0d56f47a05e2d8b28754e997a1391/2025-02-25_15-16-00.png)
2. Open the **Manage** → **Members** view and select the + **Invite member** button:

![Add a provider user](https://bitwarden.com/assets/6E5GA111xdiHHkA0gb5LtG/5e5b5fddb5911e1b2ed468c1d49134ad/2024-12-05_09-27-45.png)
3. On the Invite member panel:

 - Enter the **Email** address where new users should receive their invites. You can add up to 20 members at a time by comma-separating email addresses.
 - Select the **User type** to be applied to this batch of users. [User type](https://bitwarden.com/help/provider-users/#provider-user-types/) will determine what access these users will have to the provider. **Both user types** will be able to fully administer any [client organization](https://bitwarden.com/help/client-org-setup/).
4. Click **Save** to invite the designated users to join the Provider.

> [!NOTE] Resend Provider Invitations
> **Invitations expire after five days**, at which point the user will need to be re-invited. Re-invite users in bulk by selecting each user and using the ⋮ option menu to **Resend invitations**:
> 
> ![Resend provider invitation ](https://bitwarden.com/assets/6Sx6YxDzCYoaw7qFGgMvvv/77c341b80fd47aa6865821c30a887a8c/2024-12-05_09-34-07.png)

### Accept

Invited users will receive an email from Bitwarden inviting them to join the Provider. Clicking the link in the email will open a Bitwarden invitations window. **Log In** with an existing Bitwarden account or **Create Account** to accept the invitation:

![Email Invitation ](https://bitwarden.com/assets/1DlzjKAmxR82fsAMFqIBwB/ed0e704ccdea7785609b562e79310e0b/provider-accept-invite.png)

### Confirm

To confirm accepted invitations to your Provider:

1. In the Provider Portal, navigate to the **Manage**→**Members** view.
2. Select any `Accepted` users and use the ⋮ options menu to ✓ **Confirm selected**:

![Confirm invited provider user](https://bitwarden.com/assets/IxUeScxNYYmI4y8jceC5v/ebdf3fa89abbd69fbb028e0cff8c99aa/2024-12-05_09-29-04.png)
3. On the panel that appears, verify that the [fingerprint phrases](https://bitwarden.com/help/fingerprint-phrase/) for new users match those they can find in their **Settings** → **My account**screen. Each fingerprint phrase is unique to its account, and ensures a final layer of oversight in securely adding users. If they match, select **Confirm**.

## Deprovision users

To remove users from your Provider:

1. In the Provider Portal, navigate to the **Manage**→**Members** view.
2. Select the members you want to remove from the provider and use the ⋮ options menu to [close] **Remove**:

![Remove provider users ](https://bitwarden.com/assets/DC18TP9xNK1V8768meTDT/bfedb940285677f78e408294aadf5e0f/2024-12-05_09-36-46.png)

## Provider user types

> [!NOTE] Managing distinct user types
> **Managing a client organization's users?** Organizations have a set of [member roles and access controls](https://bitwarden.com/help/user-types-access-control/) that are distinct from Provider user types.

Bitwarden Provider users can be granted one of two user types to manage their access to the Provider. **Both user types will be able to fully administer any client organization.** Bitwarden strongly recommends that you provision a second user with a Provider admin role for failover purposes.

You can set user types when you [invite](https://bitwarden.com/help/provider-users/#invite/) provider users, or at any time from the **Manage** → **Members** screen in your Provider Portal. User types include:

| **Role** | **Description** |
|------|------|
| Service user | Service users can access and manage all [client organizations](https://bitwarden.com/help/client-orgs/), including: - Create or delete collections - Assign users and user groups to collections - Assign users to user groups - Create or delete user groups - Invite and confirm new users - Manage enterprise policies - View event logs - Export organization vault data - Manage password reset - Add or remove seats from a client organization, as long as they're within the [total seats available to the provider](https://bitwarden.com/help/provider-billing/#about-provider-billing/) |
| Provider admin | Provider admins manage all aspects of the provider and all client organizations. Provider admins can do all of the above, plus: - Create new client organizations - Invite and confirm new service users and provider admins - View provider event logs - Edit provider settings - Manage billing, subscription, and [total seats available to the provider](https://bitwarden.com/help/provider-billing/#about-provider-billing/) |
