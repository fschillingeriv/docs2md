---
URL: https://bitwarden.com/help/collection-permissions/
---

# Collection Permissions

Collection permissions determine what a [group](https://bitwarden.com/help/about-groups/) or member can do with items in a particular collection, like modifying items or changing who has access to the collection.

> [!NOTE] Roles, settings, and permissions overview
> These member permissions work together to determine collection access:
> 
> - [Member roles](https://bitwarden.com/help/user-types-access-control/) define who can do organization-level actions.
> - [Collection settings](https://bitwarden.com/help/collection-management/) specify which member roles can create, manage, or delete collections **across the entire organization**.
> - [Collection permissions](https://bitwarden.com/help/collection-permissions/) control what actions a specific user or group can take **within a single collection**.

## Assign collection permissions

Collection permissions are set when a member or group is first [assigned to a collection](https://bitwarden.com/help/assign-users-to-collections/). Depending on [member roles](https://bitwarden.com/help/user-types-access-control/) and [collection settings](https://bitwarden.com/help/collection-management/), three types of users can update collection permissions:

- Any member with the **Manage collection** collection permission within a collection can alter the permissions assigned to groups and members for that same collection.
- [Custom role](https://bitwarden.com/help/user-types-access-control/#custom-roles/) members granted the **Edit any collection** permission can alter the collection permissions assigned to groups and members for any collection.
- All owners and admins can alter collection permissions for any collection if the **Owners and admins can manage all collections and items** setting is turned on.

To review or update collection permissions:

1. Open the collection in your vault.
2. Select the [angle-down] **Arrow icon** next to the collection’s name.
3. Select **Access**:

![Edit collection permissions](https://bitwarden.com/assets/6tRILg5xNTKEkrEKBmYrGZ/7bf2c7425a0ee905821e34e5c42fab7e/Edit_collection_permissions.png)
*Edit collection permissions*
4. From the **Permission** dropdown menu, choose a permission level for that group or member.
5. Select **Save**.

> [!TIP] Check collection access via Member access report
> Enterprise organizations can review the [Member access report](https://bitwarden.com/help/reports/#member-access/) to learn which collection(s) members have access to, their level of permission within each assigned collection, and more.

## Permissions

The following table lists what each collection permission allows and when collection settings or member roles may affect them. By default, users and groups receive **View items** permission.

> [!TIP] Breadth of assigning permissions vs. roles
> While [member roles](https://bitwarden.com/help/user-types-access-control/#member-role/) are set at an individual-member level, [permissions](https://bitwarden.com/help/collection-permissions/) can be set for an individual member or an entire group. **Permissions assigned at the member level will override permissions set at a group level.**

| **Action** | **View items** | **View items, hidden passwords** | **Edit items** | **Edit items, hidden passwords** | **Manage collection** |
|------|------|------|------|------|------|
| View shared items in an assigned collections | ✓ | ✓ | ✓ | ✓ | ✓ |
| View shared items’ [hidden fields](https://bitwarden.com/help/custom-fields/) in an assigned collection | ✓ | [close] | ✓ | [close] | ✓ |
| Can autofill shared items, including [hidden fields](https://bitwarden.com/help/custom-fields/) *Hidden fields limit but don't prevent access. Treat hidden passwords as shared credentials. | ✓ | ✓ | ✓ | ✓ | ✓ |
| Add items to an assigned collection | [close] | [close] | ✓ | ✓ | ✓ |
| Add items in an assigned collection to a different collection | [close] | [close] | ✓ | ✓ | ✓ |
| Edit items in an assigned collection | [close] | [close] | ✓ | ✓ | ✓ |
| Edit hidden fields in an assigned collection | [close] | [close] | ✓ | [close] | ✓ |
| Remove items from an assigned collection | [close] | [close] | ✓ | [close] | ✓ |
| Delete items from an assigned collection | [close] | [close] | ✓ if the **Restrict item deletion to members with the Manage collection permission**[setting](https://bitwarden.com/help/collection-management/#restrict-item-deletion-to-members-with-the-manage-collection-permissions/) is turned off | ✓ if the **Restrict item deletion to members with the Manage collection permission**[ setting](https://bitwarden.com/help/collection-management/#restrict-item-deletion-to-members-with-the-manage-collection-permissions/) is turned off | ✓ |
| Delete an assigned collection | [close] | [close] | [close] | [close] | ✓ *The **user** [member role](https://bitwarden.com/help/user-types-access-control/#default-roles/) cannot delete an assigned collection when the **Restrict collection deletion to owners and admins**[setting](https://bitwarden.com/help/collection-management/#restrict-collection-deletion-to-owners-and-admins/) is turned on. |
| Manage member and group access to an assigned collection | [close] | [close] | [close] | [close] | ✓ |
| Export data from an assigned collection | [close] | [close] | [close] | [close] | ✓ |

> [!NOTE] Export org data
> The following [member roles](https://bitwarden.com/help/user-types-access-control/) can [export organization vault data](https://bitwarden.com/help/export-organization-items/) even if they do not have the **Manage collection** permission:
> 
> - Owner
> - Admin
> - Custom role with the **Access import/export** permission

> [!WARNING] Hidden Passwords
> **Hidden passwords permissions**: Users may still use passwords via autofill. While hiding passwords prevents easy copy-and-paste, it does not completely prevent user access to this information. Treat hidden passwords as you would any shared credential.

## Next steps

- [Learn about collections](https://bitwarden.com/help/about-collections/) at a conceptual level.
- [Create a collection](https://bitwarden.com/help/create-collections/) that you can add shared items to.
- [Share items with organization members](https://bitwarden.com/help/sharing/) through your new collection.
- [Assign groups and members](https://bitwarden.com/help/assign-users-to-collections/) access to your new collection.
- [Configure collection management settings](https://bitwarden.com/help/collection-management/) for your organization.
