---
URL: https://bitwarden.com/help/sharing/
---

# Share Items

Bitwarden provides two methods for sharing a vault item: add it to an organization collection to give members ongoing access, or create a link that gives anyone temporary access to a copy of the item's contents. This article covers both methods so you can choose which option will best meet the recipient's needs.

- Share with [organization collections](https://bitwarden.com/help/sharing/#organization-sharing/)

 - Sharing with a collection gives members of an organization ongoing access to an item through shared permissions.
- Share [via link](https://bitwarden.com/help/sharing/#share-via-link/)

 - Share via link creates a Send containing a copy of a vault item. Recipients can view the copy until the link expires, but they can't access or change the original item. Share via link is available on the browser extension, desktop app, and web app.

## Organization sharing

Sharing using collections requires membership in an [organization](https://bitwarden.com/help/about-organizations/). Using Bitwarden, sharing an item means two things:

- Adding the item to an [organization](https://bitwarden.com/help/about-organizations/). This transfers ownership of the item to the organization you're sharing it with.
- Adding the item to one or more [collections](https://bitwarden.com/help/about-collections/). The **Access** settings set on those collections determine who will have access to it.

Sharing with collections requires organization membership.

### Share new items

Whether you're **Adding items** to your organization or **Importing items** to your organization, you can specify who they should be shared with right from the start. You can add or import items to any collection that you have the right [permissions](https://bitwarden.com/help/collection-permissions/) for:

### Adding items

To add a new shared item from the web app, browser extension, mobile, or desktop:

1. On the **Vault** view of any Bitwarden app, select the + **Add** button and select the desired item type.

> [!TIP] Can also be done from Admin Console
> Organization [owners, admins, and some custom users](https://bitwarden.com/help/user-types-access-control/) can also take this step directly from the **Admin Console** to skip some of the steps in this process.
2. Using the **Owner** dropdown, choose the organization you want this item to be owned by.
3. Using the **Collections** dropdown, choose the collection(s) to share this item with. The **Access** settings set on those collections determine who will have access to it.
4. Fill in the rest of the relevant information for the item and select **Save** to complete sharing.

> [!NOTE] Reminder, sharing means org ownership
> **Reminder**: Sharing an item involves giving ownership of it to the organization. [Permissions for a collection](https://bitwarden.com/help/collection-permissions/) should be well managed by the administrative team because members with the right level of permission have the ability to alter or delete a shared item. You can tell that an item is owned by the organization by the badge next to its name:
> 
> 
> 
> ![Shared item badge](https://bitwarden.com/assets/6tnBV4hUxUNtWvGNAp8eua/215f54e0a26f5a1b2d41e18119fdcd71/2024-12-02_15-31-38.png)
> *Shared item badge*

### Importing items

When importing items to Password Manager, you can import them directly to a shared context. If you're importing more than just a few items, we recommend referring to the [Import to an organization](https://bitwarden.com/help/import-to-org/) article.

1. Navigate to **Tools**→ **Import data**.

> [!TIP] Can also be done from Admin Console
> Organization [owners, admins, and some custom users](https://bitwarden.com/help/user-types-access-control/) can also take this step directly from the **Admin Console** to skip some of the steps in this process.
2. Using the **Vault** dropdown, choose the organization you want this item to be owned by.
3. Using the **Collection** dropdown, choose the collection to share this item with. The **Access** settings set on those collections determine who will have access to it.
4. Choose the **File format** and **Select the import file**.
5. Select **Import data** to complete sharing.

> [!NOTE] Reminder, sharing means org ownership
> **Reminder**: Sharing an item involves giving ownership of it to the organization. [Permissions for a collection](https://bitwarden.com/help/collection-permissions/) should be well managed by the administrative team because members with the right level of permission have the ability to alter or delete a shared item. You can tell that an item is owned by the organization by the badge next to its name:
> 
> 
> 
> ![Shared item badge](https://bitwarden.com/assets/6tnBV4hUxUNtWvGNAp8eua/215f54e0a26f5a1b2d41e18119fdcd71/2024-12-02_15-31-38.png)
> *Shared item badge*

### Share existing items

You might find that an item currently owned by you needs to be shared with other members of your organization. Items can be shared with any collection that you have the right [permissions](https://bitwarden.com/help/collection-permissions/) for, from any Bitwarden app:

### Web app

The most universal method for sharing existing items using the web app can be used to share items that will be brand new to your organization, or to simply add more collections to the list it's shared with:

1. In the **Vaults** view, select the item(s) to share using the checkbox(es).

> [!TIP] Can also be done from Admin Console
> Organization [owners, admins, and some custom users](https://bitwarden.com/help/user-types-access-control/) can also take this step directly from the **Admin Console** to skip some of the steps in this process.
2. Using the action bar, select **Assign to collections**:

![Assign to collections](https://bitwarden.com/assets/stm9byteqzZn9dvqonHrc/000099fa7e49dffd712f1c94b966fa09/assign_to_collections.png)
*Assign to collections*
3. On the **Assign to collections** pop-up:

 - Use the **Move to organization** dropdown to choose the organization you want this item to be owned by.
 - Use the **Select collections to assign** dropdown to choose the collection(s) to share this item with. The **Access** settings set on those collections determine who will have access to it.
4. Select **Assign** to complete sharing.

### More methods for sharing

The previously described method is the most universal and simplified, however there are a few other methods for sharing you may have access to:

- **Share from the Admin Console**: As mentioned previously, organization [owners, admins, and some custom users](https://bitwarden.com/help/user-types-access-control/) can streamline sharing by doing so directly from the Admin Console:

![Assign to collections in bulk](https://bitwarden.com/assets/1u6EPNgAlCnvC9DcmUIosQ/e403afa9610a8fc26176d9f4223d8392/Assign_to_collections_in_bulk_edited.png)
*Assign to collections in bulk*
- **Edit an item directly**: If you need to make changes to an individual item prior to sharing it, open the item and, in the **Edit** view, use the **Owner**and **Collections** dropdowns to choose who to share it with while you're making the necessary changes:

![Change item ownership](https://bitwarden.com/assets/34zUaUOVRSXEv90fQiq5mD/e1e41fb5b40e3efcd974c770b101ad55/2025-01-28_10-40-03.png)
*Change item ownership*

### Browser extension

To share an existing item from the browser extension:

1. In the **Vault**view, use the ⋮ options menu for the item you want to share and select **Assign to collections**:

![Browser extension assign to collections](https://bitwarden.com/assets/7t3FoxPnpWGQAEzH1ERVDi/6c5622df8525848c0b4eb9bba330b70f/2024-12-02_15-32-47.png)
*Browser extension assign to collections*
2. On the **Assign to collections** pop-up:

 - Use the **Move to organization** dropdown to choose the organization you want this item to be owned by.
 - Use the **Select collections to assign** dropdown to choose the collection(s) to share this item with. The **Access** settings set on those collections determine who will have access to it.
3. Select **Assign** to complete sharing.

### More methods for sharing

There are a few other ways to share an item:

- **Edit an item directly**: If you need to make changes to an individual item prior to sharing it, open the item and, in the **Edit** view, use the **Owner**and **Collections** dropdowns to choose who to share it with while you're making the necessary changes:

![Share while editing on browser](https://bitwarden.com/assets/X73xPwnn5yKQtHhAC8U0H/480609793077866d21105593767d7448/2025-07-29_09-33-57.png)
*Share while editing on browser*

### Mobile

To share an existing item from the mobile app:

1. Tap the vault item you want to share so that the **View item**panel is displayed.
2. Tap the ⋮ options menu and choose the **Move to Organization** option.
3. On the **Move to Organization** panel:

 - Use the **Organization** dropdown to choose the organization you want this item to be owned by.
 - Use the **Collections**selectors to choose the collection(s) to share this item with. The **Access** settings set on those collections determine who will have access to it.
4. Tap **Move**to complete sharing.

### More methods for sharing

There are a few other ways to share an item:

- **Edit an item directly**: If you need to make changes to an individual item prior to sharing it, open the item and, in the **Edit** view, use the **Owner**and **Collections** dropdowns to choose who to share it with while you're making the necessary changes.

### Desktop

To share an existing item from the desktop app:

1. In the **Vault**view, select the item(s) you want to share and then select **Assign to collections** on the action bar:

![Assign to collection on desktop](https://bitwarden.com/assets/1xswcoVXzvNiKuWhkRSSkS/b654f435182377846e35c4865bea2b68/Assign_to_collection_desktop.png)
*Assign to collection on desktop*
2. On the **Assign to collections** pop-up:

 - Use the **Move to organization** dropdown to choose the organization you want this item to be owned by.
 - Use the **Select collections to assign** dropdown to choose the collection(s) to share this item with. The **Access** settings set on those collections determine who will have access to it.
3. Select **Assign** to complete sharing.

### More methods for sharing

There are a few other ways to share an item:

- **Edit an item directly**: If you need to make changes to an individual item prior to sharing it, open the item and, in the **Edit** view, use the **Owner**and **Collections** dropdowns to choose who to share it with while you're making the necessary changes:

![Share while editing on desktop](https://bitwarden.com/assets/4U6pHkqLgt3miuwFLJ9tkH/caeb931f14a8a6b10ba7e299a705e083/2026-04-23_11-41-17.png)
*Share while editing on desktop*

### CLI

To move an item, use the command:

```
bw move <itemid> <organizationid> [encodedJson]
```

Where:

- `itemid `represents the item's unique identifier.
- `organizationid` represents the unique identifier of the organization to move the item to.

For more information, please refer to the Bitwarden [CLI documentation](https://bitwarden.com/help/cli/#move/). 

### After items are shared

> [!NOTE] Reminder, sharing means org ownership
> **Reminder**: Sharing an item involves giving ownership of it to the organization. [Permissions for a collection](https://bitwarden.com/help/collection-permissions/) should be well managed by the administrative team because members with the right level of permission have the ability to alter or delete a shared item. You can tell that an item is owned by the organization by the badge next to its name:
> 
> 
> 
> ![Shared item badge](https://bitwarden.com/assets/6tnBV4hUxUNtWvGNAp8eua/215f54e0a26f5a1b2d41e18119fdcd71/2024-12-02_15-31-38.png)
> *Shared item badge*

### Reclaim shared item ownership

Users with the [Manage collection permission](https://bitwarden.com/help/collection-permissions/) for the collection(s) an item is stored in can choose to stop sharing an item with an organization:

1. Clone the item by using the ⋮ options menu for the item and selecting **Clone**.
2. On the **Add item** panel, use the **Owner**dropdown to select your account email. This will ensure the item is cloned into a non-shared context.
3. **Save** the cloned item.
4. Delete the original item by using the ⋮ options menu for the item and selecting **Delete**.

Note that in some cases moving the item to a collection with higher access control restrictions, or to a collection that only you have access to, can be more effective than outright removing it from the organization.

## Share via link

Use **Share via link** to give someone temporary access to a copy of a vault item, while the original item remains in your vault. Share via link creates a [Send](https://bitwarden.com/help/about-send/) containing the item's contents, which you can share through any channel. Share via link is available for [premium users](https://bitwarden.com/help/password-manager-plans/) or members of a paid organization (Families, Teams, or Enterprise). Additionally, organization admins can configure access to this feature using the [Manage Send and share policy](https://bitwarden.com/help/policies/#manage-send-and-share/). 

> [!NOTE] Items you can't share via link
> **Share via link** is not available for SSH key items or for items in your archive or trash. To share an archived or deleted item, unarchive it or restore it from the trash first. To share an item in one or more collections, you need edit permission for at least one of them.

To share a vault item with one or more people who do not need ongoing access to an organization collection:

1. Select the ⋮ menu for the item you wish to share, and then choose **Share via link**:

![Share with link](https://bitwarden.com/assets/7LURUsVmunZxNFPjWwXAJn/fc31a656e4ec94b6fa6f7aa37648b1fa/web_share_link.png)
*Share with link*
2. Enter the recipient's email address. Use commas to separate emails if sending to more than one recipient:

![Share with link menu](https://bitwarden.com/assets/3vTrnas77a2ZHgWOBu65Xc/ecf1b5c7761351eb9adf207805c00f43/share_link_menu_web_app.png)
*Share with link menu*
3. Configure the share rules:

 - **Link expires after**: Choose how long the link stays valid.

> [!NOTE] Recipient keeps anything they copy
> The expiration date only affects the share link itself. If the recipient saved the shared vault item while the link was valid, they will still have it after the link expires.
 - **One time share**: Allow the link to be opened only once.
4. Once you are ready to share the link, select **Copy** **link** and paste it into your preferred channel of communication. Previously generated links will appear in the **Active links** list.

### Edit a vault item share

After you create a link, you can edit it to change its settings or add options:

1. Navigate to the **Send** page and select the shared vault item:

[Embedded content]
2. Select **Edit**.

When editing a vault item share, you may configure additional settings for the share link:

- **Maximum access count**: Configure the number of times the link can be accessed.
- **Hide my email address from recipients**: Selecting this option will hide the sender's email address when the recipient opens the share link.
- **Private note**: Add any additional private notes to the Send.

> [!NOTE] Shared copies don't update
> **Share via link** sends a copy of the item as it existed when the link was created. Later edits to the original won't update the recipient's copy.

### Receive an item from a shared link

When you receive a shared item link:

1. Open the link, enter your email, and select **Send code**. Your email must match one the sender entered in order to receive a code.

![Enter email to verify](https://bitwarden.com/assets/4TYGXZJtn13F7PZzULJ5IY/d3fc9be6b3c299f7ffa002c2472b8685/enter_email_receive_send.png)
*Enter email to verify*
2. After you receive the code, enter it into the **Verification code** field.
3. After your code is verified, you can copy the item's contents to use, or paste them into a new item in your vault for long-term storage.

![Share with link content](https://bitwarden.com/assets/7g7mG243hYSCQDrmUMP6dv/7d7f8594e7cdd233b30920af1d8a9eba/Share_with_link_content.png)
*Share with link content*
