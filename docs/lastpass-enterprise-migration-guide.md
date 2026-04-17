---
URL: https://bitwarden.com/help/lastpass-enterprise-migration-guide/
---

# LastPass Enterprise Migration Guide

Secure migration of your organization with Bitwarden is straightforward and secure. Follow the steps in this guide to migrate data and users from LastPass:

1. [Create and configure your Bitwarden organization](https://bitwarden.com/help/lastpass-enterprise-migration-guide/#step-2-setup-your-organization/).
2. [Import your data into Bitwarden](https://bitwarden.com/help/lastpass-enterprise-migration-guide/#step-3-import-to-your-organization/).
3. [Onboard your users](https://bitwarden.com/help/lastpass-enterprise-migration-guide/#step-4-onboard-users/).
4. [Configure access to collections and vault items](https://bitwarden.com/help/lastpass-enterprise-migration-guide/#step-5-configure-access-to-collections-and-items/).

> [!NOTE] Assistance during migration?
> If you need assistance during your migration, our [Customer Success team is here to help](https://bitwarden.com/contact/)!

## Scope

This document describes the best practices for migrating data securely from Lastpass to a Bitwarden [Teams or Enterprise organization](https://bitwarden.com/help/about-organizations/), building an infrastructure for security based on simple and scalable methods.

[Password management](https://bitwarden.com/products/business/) is crucial for organizational security and operational efficiency. Providing insight into the best methods to perform migration and configuration is intended to minimize the trial-and-error approach that is often needed when exchanging enterprise tools.

Steps in this document **are listed in the recommended order**for ease-of-use and smooth onboarding for users

## Step 1: Setup your organization

Bitwarden organizations relate users and vault items together for [secure sharing](https://bitwarden.com/help/sharing/) of logins, notes, cards, and identities.

> [!TIP] Import to org instead of to personal.
> It's important that you create your organization first and [import data to it directly](https://bitwarden.com/help/import-to-org/), rather than importing the data to an individual account and then [moving items](https://bitwarden.com/help/sharing/) to the organization secondarily.

1. **Create your organization**. Start by creating your organization. To learn how, check out [this article](https://bitwarden.com/help/about-organizations/#create-an-organization/).

> [!NOTE] Creating a self-hosted org.
> To self-host Bitwarden, create an organization on the Bitwarden cloud, generate a [license key](https://bitwarden.com/host/), and use the key to [unlock organizations](https://bitwarden.com/help/licensing-on-premise/#organization-license/) on your server.
2. **Onboard administrative users**. With your organization created, further setup procedures can be made easier by onboarding some [administrative users](https://bitwarden.com/help/user-types-access-control/). It's important that you **do not begin end-user onboarding** at this point, as there are a few steps left to prepare your organization. Learn how to invite admins [here](https://bitwarden.com/help/managing-users/#onboard-users/).
3. **Configure identity services**. Enterprise organizations support [logging in with single sign-on](https://bitwarden.com/help/about-sso/) (SSO) using either SAML 2.0 or OpenID Connect (OIDC). To configure SSO, open the organization's **Settings** → **Single Sign-On** screen in the Admin Console, accessible by [organization owners and administrators](https://bitwarden.com/help/user-types-access-control/).
4. **Enable enterprise policies**. [Enterprise policies](https://bitwarden.com/help/policies/) enable organizations to implement rules for users, for example requiring use of two-step login. It is highly recommended that you configure policies before onboarding users.

## Step 2: Import data

Data can be imported directly from LastPass or using an [exported file](https://bitwarden.com/help/import-from-lastpass/#export-from-lastpass/) from LastPass. If you're a member of a team using SSO with LastPass, a LastPass administrator will need to complete a short setup procedure before you can use the **Direct import** option ([learn more](https://bitwarden.com/help/import-from-lastpass/#direct-import-with-sso/)).

To import data to your organization using the **Direct import** method:

1. Log in to the Password Manager browser extension or desktop app.
2. In the browser extension, select the **Settings** tab and choose the **Import items** option**.** Or, in the desktop app, select **File**> **Import data**.
3. Complete the following fields from the drop down menus:

 - **Import destination:**Select the import destination, such as the organizational vault that you have access to.
 - **Folder or Collection:**Select if you would like the imported content moved to a specific collection that you have access to.
 - [**File format**](https://bitwarden.com/help/import-faqs/#q-what-file-formats-does-bitwarden-support-for-import/)**:** Select **LastPass**.
 - In the LastPass Instructions box, choose the **Import directly from LastPass** option.
 - Enter your **LastPass email**.

> [!TIP] LP MFA during import
> If your LastPass account has multi-factor authentication activated, you will be prompted to enter a one-time passcode from your authenticator app. If you use Duo for MFA, only in-app approval is supported to fulfill your MFA requirement.
4. Select the **Import data**button to trigger the import.
5. You will be prompted for your LastPass master password or, if your LastPass account uses SSO, to log in to your IdP. In either case, follow the prompts to log in to your LastPass account.

> [!TIP] Recommend org users import individual data.
> You should also recommend to employees that they export their individually-owned data from your existing password manager and prepare it for import into Bitwarden. Learn more [here](https://bitwarden.com/help/import-from-lastpass/#tab-direct-import-7dsxR2Yah8mdGJAmQdYZea/).

## Step 3: Onboard users

Bitwarden supports manual onboarding via the web vault and automated onboarding through SCIM integrations or syncing from your existing directory service:

### Manual onboarding

To ensure the security of your organization, Bitwarden applies a 3-step process for onboarding a new member, [invite](https://bitwarden.com/help/managing-users/) → [accept](https://bitwarden.com/help/managing-users/) → [confirm](https://bitwarden.com/help/managing-users/). Learn how to invite new users [here](https://bitwarden.com/help/managing-users/#onboard-users/).

> [!TIP] Instruct users to import from LP
> Once users are onboarded, instruct them to import their personal data to Bitwarden using an exported file or, if their LastPass accounts are still active, using the **Direct import**method described [here](https://bitwarden.com/help/import-from-lastpass/#import-to-bitwarden/).

### Automated onboarding

Automated user onboarding is available through SCIM integrations with [Azure AD](https://bitwarden.com/help/microsoft-entra-id-scim-integration/), [Okta](https://bitwarden.com/help/okta-scim-integration/), [OneLogin](https://bitwarden.com/help/onelogin-scim-integration/), and [JumpCloud](https://bitwarden.com/help/jumpcloud-scim-integration/), or using [Directory Connector](https://bitwarden.com/help/directory-sync/), a standalone application available in a [desktop app](https://bitwarden.com/help/directory-sync-desktop/) and [CLI](https://bitwarden.com/help/directory-sync-cli/) tool that will synchronize users and groups from your existing directory service.

Whichever you use, users are automatically invited to join the organization and can be confirmed manually or automatically using the [Bitwarden CLI tool](https://bitwarden.com/help/cli/#confirm/).

> [!TIP] Instruct users to import from LP
> Once users are onboarded, instruct them to import their personal data to Bitwarden using an exported file or, if their LastPass accounts are still active, using the **Direct import**method described [here](https://bitwarden.com/help/import-from-lastpass/#import-to-bitwarden/).

## Step 4: Configure access to collections and items

Share vault items with your end-users by configuring access through collections, groups, and group-level or user-level permissions:

### Collections

Bitwarden empowers organizations to share sensitive data easily, securely, and in a scalable manner. This is accomplished by segmenting shared secrets, items, logins, etc. into **collections**.

Collections can organize secure items in many ways, including by business function, group assignment, application access levels, or even security protocols. Collections function like shared folders, allowing for consistent access control and sharing amongst groups of users.

Shared folders from LastPass can be imported as collections into Bitwarden by using the organization import template found [here](https://bitwarden.com/assets/4DdJLATeuhMYlE581pPErF/ef60b56917b58f59141ae9aa58b5a46d/bitwarden_export_org.csv) and placing the name of the shared folder in the `collections` column.

Collections can be shared with both groups and individual users. Limiting the number of individual users that can access a collection will make management more efficient for admins. Learn more [here](https://bitwarden.com/help/about-collections/).

> [!NOTE] Nested collection permissions
> Nested collections do not inherit the permissions of the top level collection. See [using groups](https://bitwarden.com/help/about-groups/#using-groups/) to designate permissions.

### Groups

Using groups for sharing is the most effective way to provide credential and secret access. Groups, like users, can be synced to your organization using SCIM or Directory Connector.

### Permissions

Permissions for Bitwarden collections can be assigned on the group or user-level. This means that each group or user can be configured with different permissions for the same collection. Collection permissions options include options:

- Can view
- Can view, except passwords
- Can edit
- Can edit, except passwords
- Manage collections

Learn more about permissions [here](https://bitwarden.com/help/collection-permissions/). Bitwarden uses a union of permissions to determine final access permissions for a user and a collection. For example:

- User A is part of the Tier 1 Support group, which has access to the Support collection, with can view permission.
- User A is also a member of the Support Management group, which has access to the Support collection, with can edit access.
- In this scenario, User A will be able to edit to the Collection.

## Migration support

The Bitwarden Customer Success team is available 24/7 with priority support for your organizations. If you need assistance or have questions, please do not hesitate to [contact us](https://bitwarden.com/contact/).
