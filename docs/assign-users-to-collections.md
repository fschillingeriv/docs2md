---
URL: https://bitwarden.com/help/assign-users-to-collections/
---

# Assign Users to Collections

When you [create a collection](https://bitwarden.com/help/about-collections/), you can assign access to existing [groups](https://bitwarden.com/help/about-groups/) or members. You can, at any time, modify who has access to a collection from the Password Manager web app:

1. In the web app, open the collection and select the [angle-down] button to see your options:

![Manage a collection](https://bitwarden.com/assets/m7O6TwNqNzsOCJNp1caor/914bfbf2192a2cccbe6c3fb58c11a73d/2024-12-02_15-40-10.png)
2. Select **Access**.
3. In the collection **Access** view, you can:

 - Grant additional [groups](https://bitwarden.com/help/about-groups/) or members access, including what [level of permission](https://bitwarden.com/help/collection-permissions/) they have.
 - Change the [level of permission](https://bitwarden.com/help/collection-permissions/) associated with a [group](https://bitwarden.com/help/about-groups/) or member that can already access the collection.
4. Select **Save**.

> [!TIP] Bulk collection access management
> **Bulk-management**: Users with access to the Admin Console can bulk-manage access to collections from the Collections view using the options ⋮ menu:
> 
> ![Bulk manage collections](https://bitwarden.com/assets/42edJRnvap8xiBpURskIVI/7ff8006517e9bce50dffa4372fcc2911/2024-12-02_15-41-46.png)

## Assign access to un-managed collections

Collections should always have at least one assigned member with the [Manage collection permission](https://bitwarden.com/help/collection-permissions/). Under certain circumstances, for example when a managing member leaves your organization, collections can end up without a member with that level of permission.

> [!NOTE] Only applies if 'Owner/Admin Manage All' setting is off.
> The following only applies if the [Owners and admins can manage all collections and items](https://bitwarden.com/help/collection-management/#owners-and-admins-can-manage-all-collections-and-items/) collection management setting is **off.** If this setting is **on** in your organization:
> 
> - Owners and admins can always, rather than temporarily, modify access to a collection from the **Collections** view.
> - The **Add Access** badge and tab described below will not appear.

When this occurs, owners and admins will temporarily gain management capabilities for these collections through the **Add Access** tab of the **Collections**view:

![Add access to un-managed collections](https://bitwarden.com/assets/1Nqn29nNIkKtb5HfWkfcWK/64c3875f60d3d292837d0655ad3b146c/2024-12-05_09-56-43.png)

Using the steps described previously in this article, owners and admins should assign a new member with the [Manage collection permission](https://bitwarden.com/help/collection-permissions/). Once done, owners and admins lose management capabilities for that collection and the Add Access label is removed.

## Next steps

- [Learn about collections](https://bitwarden.com/help/about-collections/) at a conceptual level.
- [Create a collection](https://bitwarden.com/help/create-collections/) that you can add shared items to.
- [Share items with organization members](https://bitwarden.com/help/sharing/) through your new collection.
- [Configure the permissions](https://bitwarden.com/help/collection-permissions/) your groups and members have to the collection.
- [Configure collection management settings](https://bitwarden.com/help/collection-management/) for your organization.
