---
URL: https://bitwarden.com/help/business-unit-portal-quick-start/
---

# Business Unit Portal Quick Start

> [!NOTE] Sign up for Business Unit Portal
> Interested in managing a Business Unit? [Contact us](https://bitwarden.com/contact-sales/) to learn more about the Business Unit Portal. To get started, you must have at least one Enterprise organization.

## Onboard users

As the Business Unit Portal owner, you will be automatically given admin status, allowing you to fully manage all aspects of Business Unit organizations. Bitwarden strongly recommends that you provision additional admins for failover purposes.

Now, begin adding your employees as service users, which will allow them to administer all Business Unit organizations and create new ones, or manage the unit itself.

1. **Invite users**. From the Business Unit Portal 🎚️ **Manage** → **Members** tab, invite users as service users (or invite additional admins):

![Invite business unit members](https://bitwarden.com/assets/3pFCcxegChJXePdeG6Qku/407a11969d79ea7c58f0845e3072922a/2025-04-23_08-56-22.png)
2. **Instruct users to accept invites**. Invited users will receive an email from Bitwarden inviting them to join the Business Unit. Inform users that they should expect an invitation and that they will need to **Log In** with an existing Bitwarden account or **Create Account** to proceed.

![Business Unit Invite](https://bitwarden.com/assets/4p9XEQjOB8nd1beMrTUo0z/2eef7bcb01b850d8544caea5703f5821/Screenshot_2025-03-27_151609.png)
3. **Confirm accepted invitations**. To complete the secure onboarding of your users, confirm accepted invitations from the Business Unit Portal **Members** tab:

![Confirm business unit invites](https://bitwarden.com/assets/40cMs63Aj1g3xrZ8SwHqMX/615ed6f09ba10c9ef3cba9d858742c3f/2025-04-23_09-08-12.png)

With the assembled team of service users, you're ready to start setting up Business Unit organizations.

## Business Unit organizations

Business Unit organizations are any organization that is attached to or administered by the Business Unit Portal. To your users, there's no difference between a "Business Unit" organization and a "regular" organization, except who is conducting the administration.

Organizations relate Bitwarden users and vault items together for secure sharing of logins, cards, notes, and identities. Organizations have a view, the Admin Console, where service users can manage the organization's collections, manage members and groups, run reporting, import data, and configure organization settings:

![Business Unit Portal](https://bitwarden.com/assets/5nwhryDcaYUXFl72AWBeyO/8a5183b4e34803c173ca0281f641d708/2025-04-24_08-59-33.png)

Members of a Business Unit organization will find shared items in the **Vaults** view alongside individually-owned items, as well as several methods for filtering the item list to only organization items or items in particular collections:

![Organization-enabled vault](https://bitwarden.com/assets/4D2tlh9YKPzDY20SYGVKcG/dff56b66549d29405b1af211860f698e/2024-12-03_14-07-28.png)

## Create a Business Unit organization

 To create a new Business Unit organization, you must be as a Business Unit Admin. Navigate to the [bank] **Clients** tab of the Business Unit Portal and select the + **New** button:

![Add business unit](https://bitwarden.com/assets/3Z2OgnsPU5RUx5J05pPYs8/00f61fb7d980105bce9feb56496143a5/2025-04-24_09-02-23.png)

## Add an existing organization

To add an existing organization to the Business Unit, you must be an active Business Unit admin and owner of the organization you wish to add.

1. Navigate to the **Business Unit Portal** using the product switcher and select the + **Add** button → **Existing organization**:

![Business Unit add Existing Organization](https://bitwarden.com/assets/7xFhBj38LTp1iWJdOadbU7/7f6b2185de459bef885095d8aef0951d/2025-10-02_15-38-46.png)
2. The Add existing organization dialogue will appear. Select the Organization you wish to add:

![Add existing organization to Business Unit](https://bitwarden.com/assets/2j9Zja0U0NJ761L0AzJDJv/843f4135b36ab02c01bf2c1a3f7f17c6/2025-10-02_15-54-06.png)
3. You will be prompted to confirm the subscription and billing changes to your provider subscription. Once complete, select **Add organization**.

## Setup the Business Unit organization

With your newly-created Business Unit organization, start building the perfect solution for your users. Exact setup will be different for each Business Unit organization based on your needs, but will typically involve:

1. **Create collections**. A good first step is to [create a set of collections](https://bitwarden.com/help/about-collections/#create-a-collection/), which provide an organizing structure for the vault items you will add to the vault in the next step.

Common collections patterns include **Collections by Department** (for example, users in the client's Marketing Team are assigned to a **Marketing** collection) or **Collections by Function** (for example, users from the client's Marketing Team are assigned to a **Social Media** collection):

![Collections](https://bitwarden.com/assets/6qodHGqBPABEFv3XJxaOUe/780cd4624a5d0a5fe315677968003e2d/collections-graphic-2.png)
2. **Import data**. Once the structure of how you will store vault items is in place, you can begin i[mporting data to the organization](https://bitwarden.com/help/import-to-org/).

> [!NOTE] Service user permissions
> Note that, as a service user, you will not be able to directly view, create, or manage individual items.
3. **Configure enterprise policies**. Before beginning the user management portion of setup, [configure enterprise policies](https://bitwarden.com/help/policies/) in order to set rules-of-use for things such as [master password complexity](https://bitwarden.com/help/policies/#master-password-requirements/), [use of two-step login](https://bitwarden.com/help/policies/#require-two-step-login/), and [admin password reset](https://bitwarden.com/help/account-recovery/#master-password-reset/).

> [!NOTE] Enterprise policy
> Enterprise policies are **only available to Enterprise organizations**.
4. **Setup login with SSO**. If your business unit uses single sign-on (SSO) to authenticate with other applications, [connect Bitwarden with their IdP](https://bitwarden.com/help/about-sso/) to allow authentication with Bitwarden using end-users' SSO credentials.
5. **Create user groups**. For teams and enterprise organizations, [create a set of groups](https://bitwarden.com/help/about-groups/#create-a-group/) for scalable permissions assignment. When you start adding users, add them to groups to have each user automatically inherit the group's configured permissions (for example, access to which collections). One common group-collection pattern is to create **Groups by Department** and **Collections by Function**, for example:

![Collections](https://bitwarden.com/assets/6qodHGqBPABEFv3XJxaOUe/780cd4624a5d0a5fe315677968003e2d/collections-graphic-2.png)

## Invite client users

With the infrastructure for secure and scalable sharing of credentials in place, you can begin inviting users to the organization. Onboarding users to Bitwarden can be accomplished in three ways, depending on the size of your Business Unit:

1. **For smaller units**, you can send email invitations to users from the Admin Console 🎚️ **Members** view:

![Invite member to an organization](https://bitwarden.com/assets/7AJjR4oqEnCH3A89YYoWpH/498d594fa9703bee9c5f49e2af9f83d0/Invite_member_to_an_organization.png)
2. **For larger units**who leverage an IdP such as Azure AD, Okta, OneLogin, or JumpCloud, use [SCIM](https://bitwarden.com/help/about-scim/) to automatically provision users.
3. **For larger units** who leverage a directory service (Active Directory, LDAP, Okta, and more), use [Directory Connector](https://bitwarden.com/help/directory-sync/) to sync organization users from the source directory and automatically issue invitations.

Regardless of whether you have invited users from the organization vault, using SCIM, or using Directory Connector, the same three-step process (Invite → Accept → Confirm) that you followed when [onboarding service users](https://bitwarden.com/help/getting-started-providers/#onboard-users/) will apply here as well.

## Managing self-hosted organizations

Business Unit Portal access to managed organizations is currently available for cloud-hosted environments only. To provide administrative services for a self-hosted instance, an additional service seat will need to be purchased to manage the self-hosted instance. For more information, see [managing self-hosted organizations](https://bitwarden.com/help/getting-started-providers/#managing-self-hosted-organizations/).

###
