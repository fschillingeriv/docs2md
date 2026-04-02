---
URL: https://bitwarden.com/help/folders/
---

# Folders

Folders are structures used to organize your individual vault by gathering together logins, cards, identities, and secure notes. Using folders is a great way to make your vault items easy to find and are listed in alphabetical order in Bitwarden apps. Any vault item can be added to a folder, including [items shared with you from an organization](https://bitwarden.com/help/sharing/).

> [!NOTE] Folders deleted items 
> Items added to a folder will still appear in your vault when **All vaults** is selected from the filter menu, and deleting a folder **will not** delete the items in that folder. Deleting a folder is permanent, and the folder cannot be recovered once deleted.

## Create a folder

Folders can be created, renamed, and deleted from any Bitwarden client application

### Web vault

To create a folder, select the **New** [angle-down] button and choose **Folder**from the dropdown:

![New folder](https://bitwarden.com/assets/3BvTWidqL4xWQvFqBSiJIR/d68bc851d44df1b571eed16366159e0c/2024-12-02_13-50-55.png)

Once created, you can rename or delete a folder at any time by selecting the folder and clicking the [pencil] **Pencil** icon:

![Edit or Delete a Folder](https://bitwarden.com/assets/1aG4313JkmkBvot45gZvEr/a7dc45d314407131948216acc2b2444d/2024-12-02_16-15-07.png)

### Browser extension

To create a folder, select the **New** [angle-down] button and choose **Folder**from the dropdown:

![Browser extension new folder](https://bitwarden.com/assets/1aPQBd9bT7uUf20Y1fZwSB/506e7010284c1e0d83b75204bac22eaa/2024-12-02_16-13-10.png)

Once created, you can rename or delete a folder at any time from the **Settings** → **Vault** → **Folders** menu.

### Desktop

To create a folder, select **File** → **New Folder** from the menu bar:

![Add a folder on desktop](https://bitwarden.com/assets/5aN4a0qkKkJDJSVAzTy3Ix/14cd1d0f480b018df722d6c07c1aeed7/2026-01-29_08-57-38.png)
*Add a folder on desktop*

Once created, you can rename or delete a folder at any time using the hover-over [pencil] **Pencil** icon:

![Edit a folder on desktop](https://bitwarden.com/assets/6t2aoywIMdBPMuJktnhEqA/7e889e22ecb7ea15bd08eda9c11096b8/2026-01-29_09-05-29.png)
*Edit a folder on desktop*

### Mobile

To create a folder, tap the ⚙️ **Settings** menu, tap the **Vault**option, and tap the **Folders** option. Tap the + **Add** icon to add a folder. Once created, you can rename a folder from the same menu by tapping the folder, or delete the folder using the ⋮ menu:

![Folders on mobile](https://bitwarden.com/assets/6IwzXSJHGmSeU7oIy4z8kZ/95620b58758e50fa0e8e22a65f2bfa15/2025-01-21_15-26-07.png)

### CLI

To create a folder, use the command:

```
bw create folder <foldername>
```

You can edit an existing folder using `bw edit <folderId>` and delete one using `bw delete folder <folderId>`. For more information, please refer the the Bitwarden [CLI documentation](https://bitwarden.com/help/cli/).

Deleting a folder will not delete any vault items included in it and will not delete other folders that are nested into it or their contents.

> [!NOTE] Collections and folders difference
> If you are a member of an organization, collections will be shown below your folders in the **Filters** menu.
> 
> There are similarities between folders and collections. **Folders organize your individual vault** (but can include [shared items](https://bitwarden.com/help/sharing/)) and are unique to you, where collections are shared between members of organizations.

### Nested folders

Folders can be "nested" in order to logically organize them within your vault. There is no limit to the depth with which you can nest folders, but creating too many levels may interfere with your vault's interface.

> [!NOTE] Searching inside folders 
> Searching inside a "parent" folder will not include items in folders nested inside it as potential search results. For more information, see [search your vault](https://bitwarden.com/help/searching-vault/).

![Nested folders ](https://bitwarden.com/assets/5blNMg0hJ9XW3Ts2qPRzF5/7a2bdfb7672c04a1a1fbae1068b8b422/2024-12-02_16-18-48.png)

To create a nested folder, give a new folder a name that includes the "parent" folder following by a forward slash (`/`) delimiter, for example `Socials/Forums`. You can also rename existing folders in the same way to nest them under other existing folders.

If there is no folder with the corresponding "parent" name, the folder won't nest and its title will be displayed in-full.

## Move items to a folder

Once you have created a folder in your vault, there are a few ways to move items to it:

### Web vault

From the web vault, you can either:

- Navigate to the **Add**item or **Edit**item screen, select your new folder from the **Folder** dropdown and **Save** your item:

 

![Move item to a Folder](https://bitwarden.com/assets/4VfciDIbEZZFAG1AXbRf3S/275100f866612da15b4714adea8f1944/2024-12-02_16-20-15.png)
- Navigate to the **Vaults** view, select the items you want to move and use the top-level ⋮ options menu to select the 📁 **Add to folder** button. On the move selected dialog box, choose the folder you want to move the item(s) to:

 

![Move items to a folder ](https://bitwarden.com/assets/7zQPzdrcVIbPeX5E8LqTq/ce8e8bf7188626093a675eb844d5002a/2024-12-02_16-22-24.png)

### Browser extension

Open the vault item you want to move, select the **Edit** button, use the **Folder** dropdown to choose a folder, and select **Save**when you're done:

![Move item to a folder ](https://bitwarden.com/assets/6b8EOCtuuHmulnNQNJmWWk/f24c97777972b15ee5000e575f2b242c/2024-10-29_11-48-18.png)

### Desktop

Open the vault item you want to move, select the **Folders** dropdown, and choose the folder to move the item to:

![Add an item to a folder](https://bitwarden.com/assets/63jzyM75IRzhAbw5nNzMHx/aa66bd79357757c4cff73ff531c459bb/2026-01-29_09-06-16.png)
*Add an item to a folder*

### Mobile

Open the vault item you want to move, tap the **Folders** dropdown, and choose the folder to move the item to:

![Move item to a folder on mobile](https://bitwarden.com/assets/169hAtd0PhW3BcYlSPy6vn/2618596e36941b06dabcb766327b664b/2025-01-22_09-44-03.png)

### CLI

Use the `bw edit` command to manipulate the `folderId` attribute of the vault item JSON object, as in the following example:

```
bw get item 7ac9cae8-5067-4faf-b6ab-acfd00e2c328 <Markdown id="7j5zoKrVKfAeuwXSrKN6Y3" />
 bw edit item 7ac9cae8-5067-4faf-b6ab-acfd00e2c328
```

> [!NOTE] Cli folders tip
> Using `edit` will require you to:
> 
> - Use the `get` command with the exact `id` of the item you want to edit.
> - Know the exact `folderId` of the folder you want to move it to.
> - Manipulate the JSON object (specifically, the `folderId` attribute) with a [command-line JSON processor like jq](https://stedolan.github.io/jq/).
> - Use the `encode` command to encode changes to the JSON object.
> 
> If you are unfamiliar with using any of these parts, please refer to the Bitwarden [CLI documentation](https://bitwarden.com/help/cli/).

> [!NOTE] Organization sharing and folders 
> Items [shared with you from an organization](https://bitwarden.com/help/sharing/) can be added to your folders, and doing so will only impact how the item appears in your individual vault (for example adding an item to a folder won't give anyone access to that folder, or change whether it's in a folder in their individual vaults).
