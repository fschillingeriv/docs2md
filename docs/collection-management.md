---
URL: https://bitwarden.com/help/collection-management/
---

# Collection Settings

[Collection](https://bitwarden.com/help/about-collections/) management settings are a set of organization-wide rules that interact directly with [member roles](https://bitwarden.com/help/user-types-access-control/) and [collection permissions](https://bitwarden.com/help/collection-permissions/) to allow or limit certain actions for certain user populations. These settings can only be set by an organization owner from the Admin Console's **Settings **→ **Organization info** view.

> [!NOTE] Roles, settings, and permissions overview
> These member permissions work together to determine collection access:
> 
> - [Member roles](https://bitwarden.com/help/user-types-access-control/) define who can do organization-level actions.
> - [Collection settings](https://bitwarden.com/help/collection-management/) specify which member roles can create, manage, or delete collections **across the entire organization**.
> - [Collection permissions](https://bitwarden.com/help/collection-permissions/) control what actions a specific user or group can take **within a single collection**.

## List of settings

### Allow owners and admins to manage all collections and items from the Admin Console

This option interacts with the [owner and admin member roles](https://bitwarden.com/help/user-types-access-control/) to determine whether that user population has automatic access to all collections, and therefore all items, in your organization.

| **On** | When on, owners and admins gain the equivalent of the [Manage collection permission](https://bitwarden.com/help/collection-permissions/) for all collections in your organization. Functionally, this means that owners and admins can alter or remove any collection, alter or remove the items in any collection, alter or remove the groups and members assigned to any collection, and alter the collection permissions assigned to any group or member for any collection. This does not include access to active users' [My Items](https://bitwarden.com/help/my-items/) if your organization uses the[ Centralize organization ownership](https://bitwarden.com/help/policies/#centralize-organization-ownership/) policy. |
|------|------|
| **Off** | When off, collections can only be managed in the above manner by members with the [Manage collection permission](https://bitwarden.com/help/collection-permissions/) specifically assigned to them. Owners and admins will only have access to collections to which they have permissions directly assigned. This does not prevent owners and admins from exporting all organization owned data, excluding organization member's individual [My Items](https://bitwarden.com/help/my-items/) locations. To prevent the possibility of orphaned collections, an **Add Access**badge will be displayed in the Collections view for any collection that does not have a member with [Manage collection](https://bitwarden.com/help/user-types-access-control/) permission. Owners and admins will **temporarily** gain access to these collections until they assign a member that permission. |

> [!TIP] Using flexible collections option 2
> This option is suited for you if, for example, your IT team requires access to all vault items associated with your organization for regular auditing.

### Restrict collection creation to owners and admins

This option interacts with the [owner and admin member roles](https://bitwarden.com/help/user-types-access-control/) to determine whether **only** that user population has the ability to create collections.

| **On** | When on, only owners and admins can create collections. This user population will be required to create your organization's collection structure on behalf of your users, but can assign individual users to manage the items and people in those collections once created. |
|------|------|
| **Off** | When off, members with any role can create collections for themselves and their team. Members who create a collection will automatically have [Manage collection](https://bitwarden.com/help/user-types-access-control/) permission over that collection. |

> [!TIP] Manage collection permission
> Even if turned **on**, any user can still be granted [Manage collection permission](https://bitwarden.com/help/collection-permissions/) for a collection so that they can manage its members and contents once created.

### Restrict collection deletion to owners and admins

This option interacts with the [owner and admin member roles](https://bitwarden.com/help/user-types-access-control/) to determine whether **only** that user population has the ability to delete collections. When on, this option also has downstream impact on the [Manage collection](https://bitwarden.com/help/user-types-access-control/) permission. 

| **On** | When on, only owners and admins can delete collections. Functionally, this option supersedes the ability to delete a collection that would have been granted to members with the [Manage collection](https://bitwarden.com/help/user-types-access-control/) permission. |
|------|------|
| **Off** | When off, members with any role can delete collections provided they have [Manage collection](https://bitwarden.com/help/user-types-access-control/) permission over the collection they'd like to delete. |

### Restrict item deletion to members with the Manage collection permissions

This option interacts with the [Manage collection permission](https://bitwarden.com/help/collection-permissions/) to determine whether **only**that user population has the ability to delete items. When off, this option also has downstream impact on the [Can edit permissions](https://bitwarden.com/help/collection-permissions/). 

| **On** | When on, only users with the [Manage collection](https://bitwarden.com/help/user-types-access-control/) permission will be able to delete collection items. |
|------|------|
| **Off** | When off, users with [Can edit and Can edit, hidden passwords](https://bitwarden.com/help/collection-permissions/) permissions will also have the ability to delete collection items. |
