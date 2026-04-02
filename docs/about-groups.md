---
URL: https://bitwarden.com/help/about-groups/
---

# Groups

## What are groups?

Groups relate together individual members and provide a scalable way to assign access to and [permissions](https://bitwarden.com/help/user-types-access-control/#permissions/) for specific [collections](https://bitwarden.com/help/about-collections/). When [onboarding new members](https://bitwarden.com/help/managing-users/), add them to a group to have them automatically inherit that group's configured permissions.

> [!NOTE] Groups available to teams and enterprise organizations
> Groups are available to [Teams and Enterprise organizations](https://bitwarden.com/help/about-organizations/#types-of-organizations/).

### Using groups

Organizations can designate access to [collections](https://bitwarden.com/help/about-collections/) based on member groups, rather than individual members. Group-collection associations provide a deep level of access control and scalability to sharing resources. One common group-collection methodology is to create **Groups by Department** and **Collections by Function**, for example:

![Using Collections with Groups](https://bitwarden.com/assets/1WzkMkukq1i1mueOQP81JC/e6ba38466c2612b64b15344040fea1dd/collections-graphic-2.png)

Other common methodologies include **Collections by Vendor or System** (for example, members in an **Engineering** group are assigned to a **AWS Credentials** collection) and **Groups by Locality** (for example, members are assigned to a **US Employees** group or **UK Employees** group).

## Create a group

Organization [admins (or higher)](https://bitwarden.com/help/user-types-access-control/) and [provider users](https://bitwarden.com/help/provider-users/#provider-user-types/) can create and manage groups. To create a group:

1. Log in to the Bitwarden [web app](https://bitwarden.com/help/getting-started-webvault/) and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
2. Navigate to **Groups** and select the + **New Group** button:

![New group ](https://bitwarden.com/assets/FefJG4qBRiWkTzsxBKfm6/53093b4dd48e534cdde9f3e249d3c382/2024-12-03_14-22-27.png)
3. On the **Group info** tab, give your group a **Name.**

> [!TIP] External ID (Org Entities)
> The **External Id** field is only relevant if you are using [Directory Connector](https://bitwarden.com/help/directory-sync/) and will be visible in the dialogue when configured using [SCIM](https://bitwarden.com/help/about-scim/), Directory Connector, or the API.
4. On the **Members**tab, assign members to the group.
5. On the **Collections**tab, assign collections to group. For each collection, select the desired [permissions](https://bitwarden.com/help/user-types-access-control/#permissions/):

![Collections permissions](https://bitwarden.com/assets/1NP5OrGCAVOZmkxfGjhU2h/7c0375c7f8f8540863a5391b0062454a/2024-12-03_14-23-45.png)

Permissions can designate that members can either view-only or edit items in the collection, as well as whether they can manage access to the collection and whether [passwords are hidden](https://bitwarden.com/help/user-types-access-control/#permissions/).
6. Select **Save** to finish creating your group.

### Edit members assignments

Once your groups are created and configured, add members to them:

1. In the Admin console, open the **Groups** view.
2. For the group you want to edit, use the ⋮ options menu to select **Members**.
3. Add or remove members from the group and select **Save**

> [!NOTE] Admins require collection access
> If the **Owners and admins can manage all collections and items** option is disabled, administrators are unable to add themselves to a group. However, they can add other administrators to a group. See [Collection management settings](https://bitwarden.com/help/collection-management/#collection-management-settings/) for more information.

### Edit collections assignments

If you want to change the [collections](https://bitwarden.com/help/about-collections/) or [permissions](https://bitwarden.com/help/user-types-access-control/#permissions/) assigned to a group:

1. In the Admin console, open the **Groups** view.
2. For the group you want to edit, use the ⋮ options menu to select **Collections**.
3. Add, remove, or change collections permissions from the group and select **Save.**
