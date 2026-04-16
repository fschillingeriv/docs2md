---
URL: https://bitwarden.com/help/about-scim/
---

# About SCIM

System for cross-domain identity management (SCIM) can be used to automatically provision members and groups in your Bitwarden organization. Bitwarden servers provide a SCIM endpoint that, with a valid [SCIM API Key](https://bitwarden.com/help/about-scim/#set-up-scim/), will accept requests from your identity provider (IdP) for user and group provisioning and de-provisioning.

Bitwarden supports SCIM v2 using standard attribute mappings and offers integration documentation for:

- [JumpCloud](https://bitwarden.com/help/jumpcloud-scim-integration/)
- [Microsoft Entra ID](https://bitwarden.com/help/microsoft-entra-id-scim-integration/)
- [Okta](https://bitwarden.com/help/okta-scim-integration/)
- [OneLogin](https://bitwarden.com/help/onelogin-scim-integration/)
- [Ping Identity](https://bitwarden.com/help/ping-identity-scim-integration/)

> [!NOTE] Different user provisioning methods
> This article discusses only one of the available methods to invite users and manage your subscription’s seat count:
> 
> - All organizations can [manually invite users](https://bitwarden.com/help/managing-users/) and update the [seat count](https://bitwarden.com/help/manage-subscription-seats-in-your-organization/).
> - Teams and Enterprise organizations can use [SCIM](https://bitwarden.com/help/about-scim/).
> - Teams and Enterprise organizations can use [Directory Connector](https://bitwarden.com/help/directory-sync/).
> - Enterprise organizations can use [just-in-time (JIT)](https://bitwarden.com/help/jit-provisioning/).

## Set up SCIM

To set up SCIM, your IdP will need a SCIM URL and API key to make authorized requests to the Bitwarden server. These values are available from the Admin Console by navigating to **Settings**→ **SCIM provisioning**:

![SCIM provisioning](https://bitwarden.com/assets/6sw1kuK7GuZ3dfQkkbs6rV/a4f4e18e561733297338e4ed44c6ed8c/2024-12-03_15-25-46.png)

> [!TIP] Use SCIM Guides.
> The following section covers some generic information that can be used to set up SCIM, however Bitwarden recommends using one of the integration documents for:
> 
> - [JumpCloud](https://bitwarden.com/help/jumpcloud-scim-integration/)
> - [Microsoft Entra ID](https://bitwarden.com/help/microsoft-entra-id-scim-integration/)
> - [Okta](https://bitwarden.com/help/okta-scim-integration/)
> - [OneLogin](https://bitwarden.com/help/onelogin-scim-integration/)
> - [Ping Identity](https://bitwarden.com/help/ping-identity-scim-integration/)

### Required attributes

Bitwarden uses standard SCIM v2 attribute names, listed here, however each IdP may use alternate names which are mapped to Bitwarden during provisioning.

#### User attributes

For each user, Bitwarden will use the following attributes:

- An indication that the user is `active` (**required**)
- `email`ª or `userName` (**required**)
- `displayName`
- `externalId`

> [!NOTE] Multiple email addresses w/ SCIM
> ª - Because SCIM allows users to have multiple email addresses expressed as an array of objects, Bitwarden will use the `value` of the object which contains `"primary": true`.

#### Group attributes

For each group, Bitwarden will use the following attributes:

- `displayName` (**required**)
- `members`ª
- `externalId`

> [!NOTE] Members & SCIM API
> ª - `members` is an array of objects, each object representing a user in that group. **Group provisioning must be used in order to assign synced users to groups**, however the SCIM API cannot be used to query members in a group. To query group membership, use the [Public API.](https://bitwarden.com/help/api/)

## SCIM event logs

Organizations using SCIM capture [event logs](https://bitwarden.com/help/event-logs/) for actions taken by SCIM integrations, including inviting users and removing users, as well as creating or deleting groups. SCIM-derived events will register `SCIM` in the **Member** column.

## Updates to existing objects

The following sections describe the changes that SCIM provisioning will sync to your organization for members and groups **when a change occurs in the IdP**:

### Member status

When a user is temporarily suspended or de-activated in your IdP, as opposed to being outright removed, their access to your organization will automatically be [revoked](https://bitwarden.com/help/revoke-users/). Users with revoked access are listed in the **Revoked**tab of the organization's**Members**screen and will:

- Not have access to any organization vault items, collections.
- Not have the ability to [use SSO to login](https://bitwarden.com/help/using-sso/), or [organizational Duo](https://bitwarden.com/help/setup-two-step-login-duo/) for two-step login.
- Not be subject to your organization's [policies](https://bitwarden.com/help/policies/).
- Not occupy a license seat.

> [!WARNING] Accounts without MPs & TDE
> For member accounts that do not have master passwords as a result of [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/):
> 
> - [Removing them from your organization](https://bitwarden.com/help/remove-users/#remove-members-from-an-organization/) eliminates all access to their Bitwarden account unless they were previously assigned a master password using [account recovery](https://bitwarden.com/help/account-recovery/) and they log in with that master password at least once before being removed.
> 
> These users will not be able to re-join your organization unless the above steps are taken **before** they are removed from the organization. If they aren't, each removed user will be required to [delete their account](https://bitwarden.com/help/delete-your-account/#delete-an-individual-account/) and be issued a new invitation to create an account and join your organization.
> - [Revoking access to the organization](https://bitwarden.com/help/revoke-users/), but not removing them from the organization, will still allow them to log in to Bitwarden and access **only** their individual vault.

### Member email address

> [!NOTE] Who can change email addresses in organizations.
> Members of organizations using [trusted devices](https://bitwarden.com/help/about-trusted-devices/) cannot change their email address unless issued a master password with [account recovery](https://bitwarden.com/help/account-recovery/).
> 
> Members of organizations using [Key Connector](https://bitwarden.com/help/about-key-connector/) cannot change their email address. Members accounts will need to [deleted](https://bitwarden.com/help/delete-member-accounts/) and re-provisioned to accommodate an email address change. Remind users to export data prior to account deletion and re-import their data once provisioned with their new email address.

Members provisioned using SCIM are able to change their account email address in Bitwarden and their organization's relevant IdP, however in order to do so they must:

1. First change the email address in Bitwarden by navigating to **Settings**→ **My account**([learn more](https://bitwarden.com/help/product-faqs/#q-how-do-i-change-my-email-address/)).
2. Once the email has been changed in Bitwarden, update the user value on the IdP or AD client. This could be the `externalid` or a corresponding value, depending on the organization's choice of IdP.
3. Re-sync the IdP or AD client to implement the changes.

> [!NOTE] Changing the Bitwarden email in SCIM org
> If the user email address is updated and synced on the IdP or AD prior to updating the Bitwarden email, the updated email will be interpreted as a new user.

### Member display name

While requests to the SCIM API can be configured to include member display names, this data is not currently synced to Bitwarden on initial provision or when changes occur in the IdP.

### Member external ID

While SCIM provisioning will assign an external ID to a user when they're initially provisioned, it will not currently sync changes to the external ID from the IdP to Bitwarden. 

## Updates to pre-SCIM objects

> [!NOTE] Turn off BWDC for SCIM
> If you used Directory Connector prior to implementing SCIM, make sure to turn Directory Connector off before turning SCIM provisioning on.

The following sections describe the changes that SCIM provisioning will sync to your organization for members and groups **that existed in your organization prior to the implementation of SCIM**:

### Members added prior to SCIM

SCIM provisioning will treat members that**joined your organization before SCIM was implemented** differently depending on whether they do or do not exist in the IdP:

- Members that **exist in the IdP** and joined before SCIM will not be duplicated, required to re-join the organization, or removed from any groups.
- Members that **do not exist in the IdP** and joined before SCIM will not be removed, or added to or removed from any groups.

### Groups created prior to SCIM

SCIM provisioning will treat groups that**were created in your organization before SCIM was implemented** differently depending on whether they do or do not exist in the IdP:

- Groups that **exist in the IdP** and were created before SCIM will not be duplicated or have any member removed, but will have new members added according to membership assigned in the IdP.
- Groups that **do not exist in the IdP** and were created before SCIM will not be removed or have any members added or removed.
