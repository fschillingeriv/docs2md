---
URL: https://bitwarden.com/help/getting-started-providers/
---

# Provider Portal Quick Start

> [!TIP] Provider Requirements
> Interested in becoming a Provider? To get started, we ask that:
> 
> - Your business has an active Enterprise organization.
> - Your business has a client ready to be onboarded under your Provider.
> 
> [Become a partner](https://bitwarden.com/partners/)

## Why Bitwarden Providers?

Managed service providers (MSPs) often need a way to quickly create and easily administer Bitwarden organizations on behalf of business customers. **Providers** are administration entities that allow those businesses to create and manage [client organizations](https://bitwarden.com/help/getting-started-providers/#client-organization/) through the **Provider Portal**. With the Provider Portal:

- View all clients under MSP management, onboard new and existing clients, access client organizations' collections, and administer services for teams and enterprise organizations.
- Add internal staff as members, assign proper user roles, and delegate administrative duties.
- View time-stamped actions made by users in the Provider Portal, including creation of new client organizations, invitation of new provider users, and when provider users access client organizations.

The Provider Portal is an all-in-one management experience that enables Providers to manage customers’ Bitwarden organizations at scale. The Provider Portal streamlines administration tasks by centralizing a dedicated space to access and support each client, or to create a new one:

![Provider Portal](https://bitwarden.com/assets/7AoSHeZgJJTBXQmpZ13UBr/56ca464fe6987c8c5fc8e7099235d640/2025-02-25_15-17-46.png)

### Start a Provider

[Contact us](https://bitwarden.com/contact/) to sign up for the Provider program. After you register, a member of the Bitwarden team will contact you and issue an invitation to start a Provider:

![Provider Invitation ](https://bitwarden.com/assets/3zxOwQqwIYO3hte6htfbiv/7e55c649273467fadb6d87bbd229a209/provider-invitation.png)

Selecting the **Setup Provider Now** button will prompt you to log in to Bitwarden and fill out some Provider details.

### Onboard users

As the creator of the Provider, you will be automatically given [Provider admin](https://bitwarden.com/help/provider-users/#provider-user-types/) status, allowing you to fully manage all aspects of the Provider and all [client organizations](https://bitwarden.com/help/getting-started-providers/#client-organizations/). Bitwarden strongly recommends that you provision a second Provider admin for failover purposes.

Now, begin adding your employees as [service users](https://bitwarden.com/help/provider-users/#provider-user-types/), which will allow them to administer all client organizations and create new ones or manage the Provider itself:

1. **Invite Users**. From the Provider Portal 🎚️ **Manage** → **Members** tab, invite users as service users (or invite additional Provider admins):

![Add a provider user](https://bitwarden.com/assets/6E5GA111xdiHHkA0gb5LtG/5e5b5fddb5911e1b2ed468c1d49134ad/2024-12-05_09-27-45.png)
2. **Instruct users to accept invites**. Invited users will receive an email from Bitwarden inviting them to join the provider. Inform users that they should expect an invitation and that they will need to **Log In** with an existing Bitwarden account or **Create Account** to proceed:

![Provider Invitation](https://bitwarden.com/assets/0FRQnrWufrfnbc8Q2GymX/ffcb260e1d90ff1a25d0f67ac9bc6c7a/provider-accept-invite.png)
3. **Confirm accepted invitations**. To complete the secure onboarding of your provider users, confirm accepted invitations from the Provider Portal **People** tab:

![Confirm invited provider user](https://bitwarden.com/assets/IxUeScxNYYmI4y8jceC5v/ebdf3fa89abbd69fbb028e0cff8c99aa/2024-12-05_09-29-04.png)

With an assembled team of service users, you're ready to start setting up [client organizations](https://bitwarden.com/help/getting-started-providers/#client-organizations/).

## Client organizations

Client organizations are any [organization](https://bitwarden.com/help/about-organizations/) that is attached to or administered by a Provider. To your customers, there's no difference between a "client" organization and a "regular" organization except for who is conducting administration.

Organizations relate Bitwarden users and vault items together for [secure sharing](https://bitwarden.com/help/sharing/) of logins, cards, notes, and identities. Organizations have a view, the Admin Console, where Provider service users can manage the organization's collections, manage members and groups, run reporting, import data, and configure organization settings:

![Client organization vault ](https://bitwarden.com/assets/5fXREt9aHmnVgLLRPBs8yg/dbecd580231e8ea2f4eec2be224a1e64/2025-02-25_15-20-08.png)

Members of a client organization (your customer's end-users) will find shared items in their **Vaults** view alongside individually-owned items, as well as several methods for filtering the item list to only organization items or items in particular [collections](https://bitwarden.com/help/about-collections/):

![Organization-enabled vault](https://bitwarden.com/assets/4D2tlh9YKPzDY20SYGVKcG/dff56b66549d29405b1af211860f698e/2024-12-03_14-07-28.png)

### Create a client organization

To create a new client organization, you must be a [Provider Admin](https://bitwarden.com/help/provider-users/#provider-user-types/). Navigate to the [bank] **Clients** tab of the Provider Portal and select the + **Add** button → [business] **New Client**:

![New client organization](https://bitwarden.com/assets/5WjBETB0YFm7TS1zpIHeSC/a22563b9172036b1c90bfb61d9ab310b/new_client_org_1.png)

### Add an existing organization

To add an existing organization, you must be an active provider user and the owner of the organization you wish to add. 

> [!NOTE] Add existing org subscription seat limit
> A service user can add members to client organizations, or add client organizations to the provider, as long as the number of users added is within the provider's seat minimum. Only provider admins can increase the seat minimum.

1. Navigate to the [bank] **Clients** tab of the Provider Portal and select the + **New** button → [sitemap] **Existing organization**:

![Admin Console add Existing Organization](https://bitwarden.com/assets/mA88mJFGTc9w6MEcisaME/af9d5d7d413cb01d9d18df783fd934fc/Existing_client_org.png)
2. The Add existing organization dialogue will appear. Select the organization you wish to add:

![Select Existing Organization](https://bitwarden.com/assets/19Ugi6eUIMQgcliZvxwuf3/9992b070d0dab4defa04639bef8baf01/2025-02-25_15-45-02.png)
3. You will be prompted to confirm the subscription and billing changes to your provider subscription. Once complete, select **Add organization**.

### Setup the client organization

With your newly-created client organization, start building the perfect solution for your customer. Exact setup will be different for each client organization based on your customers' needs, but will typically involve:

1. **Create collections**. A good first step is to [create a set of collections](https://bitwarden.com/help/about-collections/#create-a-collection/), which provide an organizing structure for the vault items you will add to the vault in the next step.

Common collections patterns include **Collections by Department** (for example, users in the client's Marketing Team are assigned to a **Marketing** collection) or **Collections by Function** (for example, users from the client's Marketing Team are assigned to a **Social Media** collection):

![Collections](https://bitwarden.com/assets/6kJ7wMESirqmkfZ8KlfK09/9210ef5cf3cd2442b429760edb98001f/collections-graphic-1.png)
2. **Import data**. Once the structure of how you will store vault items is in place, you can begin i[mporting data to the organization](https://bitwarden.com/help/import-to-org/).

> [!NOTE] Provider restricted access
> Note that, as a provider user, you will not be able to directly view, create, or manage individual items.
3. **Configure enterprise policies**. Before beginning the user management portion of setup, [configure enterprise policies](https://bitwarden.com/help/policies/) in order to set rules-of-use for things such as [master password complexity](https://bitwarden.com/help/policies/#master-password-requirements/), [use of two-step login](https://bitwarden.com/help/policies/#require-two-step-login/), and [admin password reset](https://bitwarden.com/help/account-recovery/#master-password-reset/).

> [!NOTE] Enterprise policy
> Enterprise policies are **only available to Enterprise organizations**.
4. **Setup login with SSO**. If your customer uses single sign-on (SSO) to authenticate with other applications, [connect Bitwarden with their IdP](https://bitwarden.com/help/about-sso/) to allow authentication with Bitwarden using end-users' SSO credentials.
5. **Create user groups**. For teams and enterprise organizations, [create a set of groups](https://bitwarden.com/help/about-groups/#create-a-group/) for scalable permissions assignment. When you start adding users, add them to groups to have each user automatically inherit the group's configured permissions (for example, access to which collections).

One common group-collection pattern is to create **Groups by Department** and **Collections by Function**, for example:

![Collections](https://bitwarden.com/assets/6qodHGqBPABEFv3XJxaOUe/780cd4624a5d0a5fe315677968003e2d/collections-graphic-2.png)

### Invite client users

With the infrastructure for secure and scalable sharing of credentials in place, you can begin inviting users to the organization. Onboarding users to Bitwarden can be accomplished in three ways, depending on the size of your customer:

1. **For smaller customers**, you can send email invitations to users from the Admin Console 🎚️ **Members** view:

![Invite members as a provider](https://bitwarden.com/assets/4wUO7i6w8y4sqAvwuMVZyd/070a5b36b242b1e4871cc0f58e0b8f83/2024-12-05_09-31-35.png)
2. **For larger customers**who leverage an IdP such as Azure AD, Okta, OneLogin, or JumpCloud, use [SCIM](https://bitwarden.com/help/about-scim/) to automatically provision users.
3. **For larger customers** who leverage a directory service (Active Directory, LDAP, Okta, and more), use [Directory Connector](https://bitwarden.com/help/directory-sync/) to sync organization users from the source directory and automatically issue invitations.

Regardless of whether you have invited users from the organization vault, using SCIM, or using Directory Connector, the same three-step process (Invite → Accept → Confirm) that you followed when [onboarding provider users](https://bitwarden.com/help/getting-started-providers/#onboard-users/) will apply here as well.

## Managing self-hosted organizations

MSPs can provide admin support for Bitwarden self-hosted instances as well. Provider Portal access to managed customers is currently available for cloud-hosted environments only. To provide administrative services for a self-hosted instance, an additional service seat will need to be purchased to manage the self-hosted instance.

### Enabling the self-hosted instances

1. Create a new Bitwarden user as a service account. This user will be granted access to manage a customer as an owner during the initial installation.

> [!NOTE] New Bitwarden user service account
> If your client organizations are hosted on the same server, this service account could be a single user that is granted access to all organizations. Otherwise, create a separate service account for each customer or server.
2. Save the newly created user's credentials in your internal Bitwarden vault.
Next, access the **Provider Portal** located on the main navigation bar. [Create a new enterprise organization](https://bitwarden.com/help/getting-started-providers/#create-a-client-organization/) from the Provider Portal.

> [!NOTE] New credential account
> The purpose of this step is to save the credentials, you are not required to invite the user to your organization.
3. During the creation of the enterprise organization, add the service user account that was created in **step 1.**
4. Access the client via the Provider Portal to download the organization license.
5. Deploy the Bitwarden self-hosted instance and [apply the organization license](https://bitwarden.com/help/licensing-on-premise/#apply-organization-license/).
6. Promote a user as the new owner at your managed customer.

> [!NOTE] provider portal custom user
> Optionally, once the new user has been promoted to manager of the customer organization, your service account user can be downgraded to a custom admin role.
