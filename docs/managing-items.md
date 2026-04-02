---
URL: https://bitwarden.com/help/managing-items/
---

# Vault Items

## Item types

Bitwarden can securely store more than just usernames and passwords. There are five types of items you can store in your vault:

- **Login**: Store username and password combinations for easy autofill [on browser extensions](https://bitwarden.com/help/auto-fill-browser/), [on iOS apps](https://bitwarden.com/help/auto-fill-ios/) and [on Android apps](https://bitwarden.com/help/auto-fill-android/). Login items can also store [passkeys](https://bitwarden.com/help/storing-passkeys/) and, for Premium users, [verification codes](https://bitwarden.com/help/integrated-authenticator/).
- **Card**: Store credit or debit card information for easy [autofill on browser extensions and Android](https://bitwarden.com/help/auto-fill-card-id/) apps during online checkouts.
- **Identity**: Store identity information, like mailing addresses, for easy [autofill on browser extensions and Android](https://bitwarden.com/help/auto-fill-card-id/) apps during a variety of online form submissions.
- **Secure note**: Store freeform text for any kind of information you want protected.
- **SSH key**: Use Bitwarden [as an SSH agent](https://bitwarden.com/help/ssh-agent/).

## Add items

> [!TIP] This's manual, but you can also import.
> This section will cover manually adding a vault item, but for many users Bitwarden recommends [importing items](https://bitwarden.com/help/import-data/) directly into your vault from most password managers or web browsers.

You can add vault items from any Bitwarden app:

### Web app

Select the + **New** button and choose the item type to create:

![Add an item](https://bitwarden.com/assets/5kGYpHHu4197INxX5kOetu/c1aa36b3847c9824b81466837229ec7d/webappnewtest.png)
*Add an item*

### Browser extension

Select the + **New** button and choose the item type to create:

![Add an item](https://bitwarden.com/assets/3CGG1jYRfgQqi5UlWuwliO/c95b2da5c9e64564c1aa7842207a3a6f/extnew1.png)
*Add an item*

### Mobile

Select the + **New** button and choose the item type to create:

![Add an item](https://bitwarden.com/assets/cMVnILAl9uoih1iTqIHx9/19168711ae327ea490fa51c8d9c27ff3/mobilenew1.png)
*Add an item*

### Desktop

![Add an item](https://bitwarden.com/assets/7xia34eJyx1K8Gy8IXajQ7/2abe25e62c5a34e2b41e503fb119c2d3/2026-01-28_09-55-00.png)
*Add an item*

### CLI

Use the `create` command to add a new item. Refer to the [CLI documentation](https://bitwarden.com/help/cli/) for more information.

## Manage items

You can manage your vault items from any Bitwarden app:

### Edit

To edit an item:

### Web app

Select the ⋮ options menu for the item you want to edit:

> [!TIP] You can right-click on the web app.
> You can also right-click the item to call up the same menu.

![Edit or delete an item](https://bitwarden.com/assets/5FmC9ha8GQ4IKU8UM1ra4x/d470974c62468ba565e58ca1917db0b1/webnew1.png)
*Edit or delete an item*

### Browser extension

Select an item to open it and select **Edit**:

![Edit or delete an item](https://bitwarden.com/assets/2q1EZnISzEG3i8iU4vTKj6/b13c46c27a7fb896f31f81485859459f/extnew4.png)
*Edit or delete an item*

### Mobile

Select the ⋮ options menu for the item you want to edit and select **Edit**:

![Edit an item](https://bitwarden.com/assets/357lJe8JKMXNKEhYKUDn4u/31d5f1f811eb35b8b142f9a6f751dae2/2025-11-10_12-05-53.png)
*Edit an item*

### Desktop

Select an item to open it and select the [pencil] edit icon:

![Edit an item](https://bitwarden.com/assets/6Y4kK7J9aLmo9SDY7Ne8VE/0793598383e76b81433d815db7af9d01/2026-01-28_09-59-02.png)
*Edit an item*

### CLI

Use the `edit` command to add a new item. Refer to the [CLI documentation](https://bitwarden.com/help/cli/) for more information.

### Archive

Archiving is a useful tool for decluttering your vault. Archived items are excluded from search results and autofill suggestions, but included in exports. Archiving:

- Is available for all paid plans, including premium users and members of paid organizations. If that subscription ever lapses, users **will not** lose access to archived items.
- Is available for organization items and individually-owned items. Like [favorites](https://bitwarden.com/help/favorites/), one user's choice to archive an item will not archive that items for any other users that have access to it.
- **Does not** remove items from reporting or exports.

To archive an item:

### Web app

Select the item(s) you want to archive and use the ⋮ options menu to choose **Archive**:

![Archive with the web app](https://bitwarden.com/assets/1aRyGxLdpcvGF3fM2Bbd17/24408086dd8835286d079cb48cd6069a/2026-01-27_10-28-36.png)
*Archive with the web app*

On the web app, select **Archive** from your vault filters in order to view your archived items and use the ⋮ options menu to choose **Unarchive**to restore an item to normal vault behavior.

### Browser extension

Use the ⋮ options menu for the item you want to archive and choose **Archive**:

![Archive with the browser extension](https://bitwarden.com/assets/40gA9zgbeBjx2gw77H61kM/08e93903af859aa75bbdd277b4098a90/2026-01-27_10-40-25.png)
*Archive with the browser extension*

On browser extensions, navigate to **Settings** → **Vault options** → **Archive** to view your archived items and use the ⋮ options menu to choose **Unarchive**to restore an item to normal vault behavior.

### Mobile

Use the ⋯ options menu for the item you want to archive and choose **Archive**:

![Archive with the mobile app](https://bitwarden.com/assets/rrxmgUU3pLqQrYa5wDDb9/fd90c478bacd1c366e59b4be3d07b185/2026-02-23_11-48-54.png)
*Archive with the mobile app*

On mobile apps, select **Archive** from your vault filters in order to view your archived items and use the ⋯ options menu to choose **Unarchive**to restore an item to normal vault behavior.

### Desktop

Open the item you want to archive and select the Archive button:

![Archive with the desktop app](https://bitwarden.com/assets/kOYhUPQwYRL9Rm0SKwxsf/1bb7a48646276475df915a73b5ece014/2026-01-27_10-52-53.png)
*Archive with the desktop app*

On desktop apps, select **Archive** from your vault filters in order to view your archived items use the ⋮ options menu to choose **Unarchive**to restore an item to normal vault behavior.

### CLI

To archive an item, use the command `bw archive item <item-id>` where `<item-id>` represents the unique identifier of the item you want to archive.

To view items in your archive, use the command `bw list --archive`.

### Delete

To delete an item:

### Web app

Select the ⋮ options menu for the item and select 🗑️ **Delete**:

![Item options](https://bitwarden.com/assets/3OYHvfRCDy3OphkbEHIJEA/fa47beb671d6efc34a18d05daf630aff/webappnewtest3.png)
*Item options*

### Browser extension

Select an item to open it and select the 🗑️ Delete icon:

![Edit or delete an item](https://bitwarden.com/assets/2q1EZnISzEG3i8iU4vTKj6/b13c46c27a7fb896f31f81485859459f/extnew4.png)
*Edit or delete an item*

### Mobile

Tap an item to open it and select the ⋮ options menu for the item:

![Item options](https://bitwarden.com/assets/6XFamLqIYX26cUY5LWQbPE/1a6000050526e7f4f9e8bfcad93619fe/2025-11-10_12-06-19.png)
*Item options*

### Desktop

Select an item to open it and select the 🗑️ Delete icon:

![Delete an item](https://bitwarden.com/assets/1E8ieEw6639tLYAxe2HYir/bd8b4f23e967bf522981490d23b6396a/2026-01-28_10-01-38.png)
*Delete an item*

### CLI

Use the `delete` command to add a new item. Refer to the [CLI documentation](https://bitwarden.com/help/cli/) for more information.

#### Vault trash

Deleted items are sent to the trash, where they remain for 30 days after deletion. Once 30 days have elapsed, the item will be permanently deleted and not recoverable. In the trash, you can **Restore** an item to your vault or **Permanently delete** it prior to the 30-day waiting period using the ⋮ menu:

### Web app

Select **Trash**from the Filters menu:

![Trash in the web app](https://bitwarden.com/assets/36mo5LyroRq1BhOcjSsBb7/a05100ab172376caf15b4c454beee321/2024-12-02_14-39-40.png)

### Browser extension

Navigate to **Settings** → **Vault** → **Trash**:

![Trash in browser extensions](https://bitwarden.com/assets/5Q0mgKjaDiIKy5ymlVaUnS/fa72b454697bedd7319da17ba671a9e5/2025-04-15_09-33-59.png)

### Mobile

On the **Vaults** tab, scroll down to **Trash** and select the item:

![Trash in mobile apps](https://bitwarden.com/assets/7HwDVQp0ma6RxU95ILNVtI/52275cc54ff5d789f8825d225edb0ecf/2025-04-15_10-22-16.png)

### Desktop

Select **Trash**from the navigation:

![Trash in the desktop app](https://bitwarden.com/assets/viaKopya1CJ9N6mWKyLV6/20bc3829a37c83e2d3c5a2ce16fdd032/2026-01-28_10-06-55.png)
*Trash in the desktop app*

### Clone

You can clone any item that you have ownership of to create a duplicate item. If an item is owned by an organization, it can only be cloned by a members with [**Can manage**](https://bitwarden.com/help/collection-management/#collection-management-settings/) access to the item's collection and can only be done from the web app:

### Web app

Select the ⋮ options menu for the item you want to duplicate and select [clone] **Clone**:

![Item options](https://bitwarden.com/assets/3OYHvfRCDy3OphkbEHIJEA/fa47beb671d6efc34a18d05daf630aff/webappnewtest3.png)
*Item options*

### Browser extension

Select the ⋮ options menu for the item you want to duplicate and select [clone] **Clone**:

![Item options](https://bitwarden.com/assets/10bowrbDmxxf8SxrMhplmJ/01597fd4926492def941caf556cd9d12/extnew5.png)
*Item options*

### Mobile

Tap an item to open it and select the ⋮ options menu for the item:

![Item options](https://bitwarden.com/assets/6XFamLqIYX26cUY5LWQbPE/1a6000050526e7f4f9e8bfcad93619fe/2025-11-10_12-06-19.png)
*Item options*

### Desktop

Select an item to open it and select the [clone] Clone icon:

![Clone an item](https://bitwarden.com/assets/5KRdegIaIbOHxGkMj64Fs9/b1168078f6eded0673dd7dd96f3739e9/2026-01-28_10-12-51.png)
*Clone an item*

## Share items

If you're a member of an [organization](https://bitwarden.com/help/about-organizations/), you can [assign vault items to your organization's collections](https://bitwarden.com/help/sharing/), transferring ownership of the vault item to the organization. To share with other organization members, use the ⋮ menu:

![Assign to collections](https://bitwarden.com/assets/stm9byteqzZn9dvqonHrc/0da481b0cf1f54457d08ae02fd917377/2024-12-02_14-33-34.png)

## Next steps

Now that you understand the basics of working with vault items, we recommend:

- Learning how to navigate your vault using [search](https://bitwarden.com/help/searching-vault/), [filtering](https://bitwarden.com/help/filter-your-vault/), and organizing them in [favorites](https://bitwarden.com/help/favorites/) and [folders](https://bitwarden.com/help/folders/).
- Learning about what else you can add to items, including [custom fields](https://bitwarden.com/help/custom-fields/), [TOTP seeds](https://bitwarden.com/help/integrated-authenticator/), and [file attachments](https://bitwarden.com/help/attachments/).
