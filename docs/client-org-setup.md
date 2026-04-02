---
URL: https://bitwarden.com/help/client-org-setup/
---

# Start a Client Organization

This article will walk you through the [creation of a client organization](https://bitwarden.com/help/client-org-setup/#create-a-client-organization/) and outline a typical [setup procedure](https://bitwarden.com/help/client-org-setup/#initial-setup-procedure/) for getting started administering a customer's organization.

## Create a client organization

To create a client organization you must be a [Provider admin](https://bitwarden.com/help/provider-users/#provider-user-types/):

1. Open the Provider Portal using the product switcher:

![Product switcher - Provider Portal](https://bitwarden.com/assets/4xn04Sj9u8n73TPxZUWi5f/dac0d56f47a05e2d8b28754e997a1391/2025-02-25_15-16-00.png)
2. Navigate to the [bank] **Clients** tab of the Provider Portal and select + **Add** → [business]**New client**:

![New client organization](https://bitwarden.com/assets/5WjBETB0YFm7TS1zpIHeSC/a22563b9172036b1c90bfb61d9ab310b/new_client_org_1.png)
3. On the New client organization screen

 - Select whether to create a **Teams** or **Enterprise**organization.
 - Enter an **Organization name**, **Client owner email**, and **Seats**.

The amount of available unassigned seats, that is seats that you have paid for but aren't utilizing, will be shown on this screen. Should you go above this number, a number of additional seats purchased will be shown. [Learn more](https://bitwarden.com/help/provider-billing/).

> [!NOTE] Owner invitation
> An invitation will automatically be sent to the **Client owner email** to join the organization as an [owner](https://bitwarden.com/help/user-types-access-control/).
4. Once you are happy with the organization, select **Add organization**.

Once created, navigating to the client organization from the Provider Portal will bring you to the organization vault, from which you can fully complete [initial setup](https://bitwarden.com/help/client-org-setup/#initial-setup-procedure/) and engage in [ongoing administration](https://bitwarden.com/help/manage-client-orgs/):

![Client organization vault ](https://bitwarden.com/assets/5fXREt9aHmnVgLLRPBs8yg/dbecd580231e8ea2f4eec2be224a1e64/2025-02-25_15-20-08.png)

## Initial setup procedure

With your newly-created client organization, you are ready to start building the perfect solution for your customer. Exact setup will be different for each client organization depending on your customers' needs, but typically will involve the following steps:

1. **Create collections**. A good first step is to [create a set of collections](https://bitwarden.com/help/about-collections/#create-a-collection/), which provide an organizing structure for the vault items you will add to the vault in the next step.

Common collections patterns include **Collections by Department** (for example, users in the client's Marketing Team are assigned to a **Marketing** collection) or **Collections by Function** (such as users from the client's Marketing Team are assigned to a **Social Media** collection):

![Collections](https://bitwarden.com/assets/6kJ7wMESirqmkfZ8KlfK09/9210ef5cf3cd2442b429760edb98001f/collections-graphic-1.png)
2. **Import data**. Once the structure of how you will store vault items is in place, you can begin i[mporting data to the organization](https://bitwarden.com/help/import-to-org/).

> [!NOTE] Provider restricted access
> Note that, as a provider user, you will not be able to directly view, create, or manage individual items.
3. **Configure enterprise policies**. Before beginning the user management portion of setup, [configure enterprise policies](https://bitwarden.com/help/policies/) in order to set rules-of-use for things such as [master password complexity](https://bitwarden.com/help/policies/#master-password-requirements/), [use of two-step login](https://bitwarden.com/help/policies/#require-two-step-login/), and [admin password reset](https://bitwarden.com/help/account-recovery/#master-password-reset/).

> [!NOTE] Enterprise policies availability
> Enterprise Policies are **only available to Enterprise organizations**.
4. **Setup login with SSO**. If your customer uses single sign-on (SSO) to authenticate with other applications, [connect Bitwarden with their IdP](https://bitwarden.com/help/about-sso/) to allow authentication with Bitwarden using end-users' SSO credentials.
5. **Create user groups**. For Teams and Enterprise organizations, [create a set of groups](https://bitwarden.com/help/about-groups/#create-a-group/) for scalable permissions assignment. When you start adding users, add them to groups to have each user automatically inherit the group's configured permissions (such as access to specific collections).

One common group-collection pattern is to create **Groups by Department** and **Collections by Function**, for example:

![Collections](https://bitwarden.com/assets/6qodHGqBPABEFv3XJxaOUe/780cd4624a5d0a5fe315677968003e2d/collections-graphic-2.png)
6. **Start inviting users**. Now that the infrastructure for the secure and scalable sharing of credentials is in place for your client, you can begin [inviting users to the organization](https://bitwarden.com/help/managing-users/#onboard-users/). To ensure the security of the organization, Bitwarden applies a three-step process for onboarding new users, **Invite** → **Accept**→ **Confirm**.

> [!TIP] SCIM & BWDC for Providers.
> **If your customer uses directory service** or IdP (active directory, an LDAP, Okta, and more), use [SCIM](https://bitwarden.com/help/about-scim/) or [Directory Connector](https://bitwarden.com/help/directory-sync/) to automatically sync organization users from the source directory and automatically issue invitations.
