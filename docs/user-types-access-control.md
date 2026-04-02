---
URL: https://bitwarden.com/help/user-types-access-control/
---

# Member Roles

Member roles control what users can do, like configuring SSO or managing device approvals. Assign a [default role](https://bitwarden.com/help/user-types-access-control/#default-roles/) or [custom role](https://bitwarden.com/help/user-types-access-control/#custom-roles/) when inviting users or anytime after. Admins and owners manage roles and can create custom roles in Enterprise organizations.

## Assign member roles

There are two ways to assign a member role in the Admin Console:

- When [inviting a new member](https://bitwarden.com/help/managing-users/#invite/), select a **Member role**.
- To change an existing member's role, go to **Members** and select the person's name. Choose a **Member role** from the options that appear:

![Edit member role](https://bitwarden.com/assets/73zJ6ZvMNNLU8TyH0Xdhow/a96f23b972fc9e954ac4860d3fb044d6/Edit_member_role.png)
*Edit member role*

## Default roles

There are three default member roles: owner, admin, and user. Each role grants different permissions for managing your organization and accessing shared items.

| **Role** | **Overview** |
|------|------|
| Owner | Owners are the only ones that can access an organization's subscription and billing details. Only a current owner can invite new owners or assign the owner role to existing members. To prevent disruptions to your organization’s subscription [when an owner leaves](https://bitwarden.com/help/managing-access-when-the-organization-owner-leaves/), we highly recommend assigning at least one additional owner. Good candidates include your IT team manager or a project manager. |
| Admin | Admins help manage your organization's unique configuration, like SSO and enterprise policies. They also have permission to manage members, like inviting new users and creating user groups. When picking admins for your team, consider who will help deploy Bitwarden across the organization or need access to organization reporting, like event logs or Access Intelligence. |
| User | Users can access shared items in their assigned collections and manage personal vault items. Based on their collection permissions, they can add, edit, or remove collection items. Assign the user role to teammates who need access to shared passwords but won’t manage organization settings, members, or policies. This is the standard role for most members. |

> [!TIP] Assign more than one owner
> Assign at least one additional owner to maintain access to billing and subscription details if the current owner becomes unavailable.

## Default role permissions

The following tables list the permissions for each member role.

### Items and collections

While every member role can save new items in **My vault** or [My Items](https://bitwarden.com/help/my-items/), access to [collections](https://bitwarden.com/help/about-collections/) is determined by three types of permissions that interact.

> [!NOTE] Roles, settings, and permissions overview
> These member permissions work together to determine collection access:
> 
> - [Member roles](https://bitwarden.com/help/user-types-access-control/) define who can do organization-level actions.
> - [Collection settings](https://bitwarden.com/help/collection-management/) specify which member roles can create, manage, or delete collections **across the entire organization**.
> - [Collection permissions](https://bitwarden.com/help/collection-permissions/) control what actions a specific user or group can take **within a single collection**.

The table below lists what each member role can do by default and when collection settings or collection permissions may affect them. When an organization is first set up, all collection settings are turned off and invited users or groups receive the **View items** collection permission.

| **Action** | **Owner** | **Admin** | **User** |
|------|------|------|------|
| Add, edit, or remove items in **My vault** or **My Items** | ✓ | ✓ | ✓ |
| Create collections | ✓ | ✓ | ✓ if the **Restrict collection creation to owners and admins** [setting](https://bitwarden.com/help/collection-management/#restrict-collection-deletion-to-owners-and-admins/) is turned off |
| Access shared items in assigned collections | ✓ | ✓ | ✓ |
| Add, edit, remove, and export items from assigned collections *A member’s [collection permissions](https://bitwarden.com/help/collection-permissions/#permissions/) determines what they can do within that collection. | ✓ | ✓ | ✓ |
| Delete an assigned collection | ✓ if the **Manage collection** [permission](https://bitwarden.com/help/collection-permissions/) is assigned | ✓ if the **Manage collection** [permission](https://bitwarden.com/help/collection-permissions/) is assigned | ✓ if the **Restrict collection deletion to owners and admins** [setting](https://bitwarden.com/help/collection-management/#restrict-collection-deletion-to-owners-and-admins/) is turned off and the **Manage collection** [permission](https://bitwarden.com/help/collection-permissions/) is assigned |
| Access and manage all collections in the organization | [close] if the **Allow owners and admins to manage all collections and items from the Admin Console** [setting](https://bitwarden.com/help/collection-management/#allow-owners-and-admins-to-manage-all-collections-and-items-from-the-admin-console/) is turned off | [close] if the **Allow owners and admins to manage all collections and items from the Admin Console** [setting](https://bitwarden.com/help/collection-management/#allow-owners-and-admins-to-manage-all-collections-and-items-from-the-admin-console/) is turned off | [close] |
| [Export all organization vault data](https://bitwarden.com/help/export-organization-items/) | ✓ | ✓ | [close] |
| Manage [collection settings](https://bitwarden.com/help/collection-management/) | ✓ | [close] | [close] |

### Members and activity

Owners and admins have enhanced capabilities for managing users and accessing organization-level reporting.

| **Action** | **Owner** | **Admin** | **User** |
|------|------|------|------|
| [Invite and confirm new users](https://bitwarden.com/help/managing-users/#onboard-users/) | ✓ | ✓ | [close] |
| [Revoke](https://bitwarden.com/help/revoke-users/) and [remove](https://bitwarden.com/help/remove-users/) users | ✓ | ✓ | [close] |
| Assign and manage member roles | ✓ | ✓ | [close] |
| Create and delete [groups](https://bitwarden.com/help/about-groups/) | ✓ | ✓ | [close] |
| Add users to groups | ✓ | ✓ | [close] |
| Manage [account recovery](https://bitwarden.com/help/account-recovery/) | ✓ | ✓ | [close] |
| Manage [trusted device](https://bitwarden.com/help/about-trusted-devices/) approvals | ✓ | ✓ | [close] |
| View [vault health reports](https://bitwarden.com/help/reports/) | ✓ | ✓ | [close] *All users can access the [Data breach report](https://bitwarden.com/help/reports/#data-breach-individual-vaults-only/). |
| View [event logs](https://bitwarden.com/help/event-logs/) | ✓ | ✓ | [close] |
| View [Access Intelligence](https://bitwarden.com/help/access-intelligence/) | ✓ | ✓ | [close] |

### Organization billing and settings

Access to most organization configuration settings is limited to owners.

| **Action** | **Owner** | **Admin** | **User** |
|------|------|------|------|
| [Manage billing](https://bitwarden.com/help/update-billing-info/), including subscription, payment method, and billing history | ✓ | [close] | [close] |
| Change organization name | ✓ | [close] | [close] |
| Manage [enterprise policies](https://bitwarden.com/help/policies/) | ✓ | ✓ | [close] |
| Manage [claimed domains](https://bitwarden.com/help/claimed-domains/) | ✓ | ✓ | [close] |
| Manage SSO configuration | ✓ | ✓ | [close] |
| Manage organization two-step login | ✓ | [close] | [close] |
| Manage [API](https://bitwarden.com/help/bitwarden-apis/) key | ✓ | [close] | [close] |
| Manage [SCIM](https://bitwarden.com/help/about-scim/) configuration | ✓ | [close] | [close] |

## Custom roles

Enterprise teams can build custom roles tailored to their needs, ideal for least-privileged security models. Use custom roles to delegate organization management tasks or give users access to specific features. Common custom roles include:

| **Use case** | **Custom role permissions** |
|------|------|
| **IT help desk** who handles login issues and trusted device requests | Manage account recovery |
| **Auditor** who reviews security events and compliance | Access event logs and Access reports |
| **Team manager** who tracks password health and manages [group-based collection access](https://bitwarden.com/help/assign-users-to-collections/) | Access reports and Manage groups |

> [!TIP] No billing permission via custom roles
> If someone needs to manage subscription information or update payment details, assign the **owner** role. Access to organization billing cannot be granted through a custom role.

By default, custom roles include the same permissions as the **user** member role. When assigning a custom role to a new or existing member, check the additional permissions you want to grant:

- Access event logs
- Access import/export

 - This permission implicitly provides the custom role member read access to all vault items in order to facilitate exporting, however the member will not automatically be able to view all vault items from within Bitwarden.
- Access reports

 - This permission implicitly provides the custom role member read access to all vault items in order to facilitate report generation, however the member will not automatically be able to view all vault items from within Bitwarden.
- Manage all collections

 - This includes the ability to create, edit, and delete any collection.
- Create new collections
- Delete any collection
- Edit any collection

 - This permission allows the member to change [collection permissions](https://bitwarden.com/help/collection-permissions/) for any collection, which could be used to provide provide full access to vault items to a member of the organization who is not intended to have that level of access.
- Manage groups
- Manage SSO
- Manage [policies](https://bitwarden.com/help/policies/)
- Manage users

 - Custom users with the **Manage users**permission can only grant permissions they already have. For example, a custom user with only **Manage users**and **Access reports** cannot grant **Manage SSO** to someone else.
- Manage account recovery

 - The custom user can [reset master passwords](https://bitwarden.com/help/recover-a-member-account/) for members enrolled in account recovery. Without the additional **Manage users** permission, the **Members** page only lists enrolled members and displays the **Recover account** action.
 - This permission also allows the custom user to manage [trusted device requests](https://bitwarden.com/help/approve-a-trusted-device/).
