---
URL: https://bitwarden.com/help/import-data/
---

# Import to your Vault or Collections

Import logins and data from different password managers, other Bitwarden vaults, or [encrypted exports](https://bitwarden.com/help/encrypted-export/) to instantly transfer your information and skip manual entry. You can import data from any password management solution that allows exports.

> [!TIP] Import to org instead of individual
> This article covers importing to your own vault or [to a collection](https://bitwarden.com/help/import-data/#import-to-a-collection/) that you have access to. If you're administering an organization, you may need to [import to an organization](https://bitwarden.com/help/import-to-org/) instead.

## Common password manager & file type imports

Bitwarden supports data imports from many common password management solutions, including:

- [Import from LastPass](https://bitwarden.com/help/import-from-lastpass/)
- [Import from 1Password](https://bitwarden.com/help/import-from-1password/)
- [Import from Firefox](https://bitwarden.com/help/import-from-firefox/)
- [Import from Google Chrome, Edge, or Chromium](https://bitwarden.com/help/import-from-chrome/)
- [Import from Password Safe](https://bitwarden.com/help/import-from-passwordsafe/)
- [Import from another Bitwarden vault](https://bitwarden.com/help/export-your-data/)

[Additional file types](https://bitwarden.com/help/import-faqs/#q-what-file-formats-does-bitwarden-support-for-import/) from other password managers are compatible with Bitwarden. If your solution isn’t listed but can export data, edit the file to match a [supported format](https://bitwarden.com/help/condition-bitwarden-import/).

## Import to your individual vault

Data can be imported to Bitwarden from the web app, browser extension, desktop app, and CLI. Data is [encrypted](https://bitwarden.com/help/what-encryption-is-used/) locally before being sent to the server for storage.

> [!NOTE] Items not imported
> While some item types cannot be imported, you can still add them to a vault:
> 
> - Upload [file attachments](https://bitwarden.com/help/attachments/) to the new vault individually.
> - Re-create [Sends](https://bitwarden.com/help/about-send/) in the new vault.

### Web app

To import data to your Bitwarden vault:

1. Select **Tools**.
2. Select **Import**:

![Import items](https://bitwarden.com/assets/1NbyPb9dN545ZqKGRZYB3x/e6b8f3f31aa82bb05cef12c5a5c4c193/2025-12-17_11-25-08.png)
*Import items*
3. From the **Vault** dropdown menu, select where to save the data:

 - To save data in your personal vault, select **My vault**. (Optional) Choose an existing [**Folder**](https://bitwarden.com/help/folders/) to organize the imported items.

> [!NOTE] Choosing a folder with a folder defined in the import.
> If your data file contains folders from your previous password manager and you select a destination folder from the dropdown menu, the imported folders will be nested inside the folder you selected.
 - To save data in an organization's vault, select the organization's name. (Optional) Choose a [Collection](https://bitwarden.com/help/create-collections/) to organize the imported items and share with other members. (You can only choose a collection where you have [**can manage**](https://bitwarden.com/help/about-collections/#collections-permissions/) permission.)
4. From the **File format** dropdown menu, select the [file format](https://bitwarden.com/help/import-faqs/#q-what-file-formats-does-bitwarden-support-for-import/) of your exported data.
5. To enter your data, do one of the following:

 - Select **Choose File** and pick the exported file from your computer.
 - Copy and paste the contents of your exported file into the text box.

> [!WARNING] Duplicative Imports
> Importing does not check for duplicates. If you import the same file more than once or import items already in your vault, duplicate items will be created.
6. Select **Import**. If you're importing a password-protected `.json `file, enter the password into the **Confirm vault import** window that appears.
7. After your data is imported, delete the exported data file from your computer. This will protect you in the event your computer is compromised. If you're importing to Bitwarden from another password manager or browser, you may also want to delete data from that tool.

### Browser extension

To import data to your vault:

1. Select **Settings**.
2. Select **Vault options.**
3. Select **Import items**. A new window will appear**.**
4. From the **Vault** dropdown menu, select where to save the data:

 - To save data in your personal vault, select **My vault**. (Optional) Choose an existing [**Folder**](https://bitwarden.com/help/folders/) to organize the imported items.

> [!NOTE] Choosing a folder with a folder defined in the import.
> If your data file contains folders from your previous password manager and you select a destination folder from the dropdown menu, the imported folders will be nested inside the folder you selected.
 - To save data in an organization's vault, select the organization's name. (Optional) Choose a [Collection](https://bitwarden.com/help/create-collections/) to organize the imported items and share with other members. (You can only choose a collection where you have [**can manage**](https://bitwarden.com/help/about-collections/#collections-permissions/) permission.)
5. From the **File format** dropdown menu, select the [import file format](https://bitwarden.com/help/import-faqs/#q-what-file-formats-does-bitwarden-support-for-import/).
6. Select **Choose File** and pick the file or copy and paste your file’s contents into the text box.

> [!WARNING] Duplicative Imports
> Importing does not check for duplicates. If you import the same file more than once or import items already in your vault, duplicate items will be created.
7. Select **Import data**. If you are importing a password protected `.json `file, enter the password into the **Confirm vault import** window that appears.
8. After your data is imported, delete the exported data file from your device. This will protect you in the event your computer is compromised. If you're importing to Bitwarden from another password manager or browser, you may also want to delete data from that tool.

### Mobile

In most cases, importing data on a mobile device requires you to do so via the web app, opened in a mobile browser. You can reach this location from Password Manager by navigating to **Settings** → **Vault** → **Import items**.

On iOS 26, Bitwarden supports import using the [Fido Credential Exchange Protocol (CXP)](https://fidoalliance.org/specifications-credential-exchange-specifications) for direct and easy migration of passwords, passkeys, credit cards, and personal identity information into your vault. The app you're importing from must also support CXP and steps will vary by application.

For example, on the iOS Passwords app, use the ⋯ options menu to select **Export Data to Another App** and choose Bitwarden. 

### Desktop

To import data to your vault:

1. Select **Import** from the navigation menu.
2. From the **Vault** dropdown menu, select where to save the data:

 - To save data in your personal vault, select **My vault**. (Optional) Choose an existing [**Folder**](https://bitwarden.com/help/folders/) to organize the imported items.

> [!NOTE] Choosing a folder with a folder defined in the import.
> If your data file contains folders from your previous password manager and you select a destination folder from the dropdown menu, the imported folders will be nested inside the folder you selected.
 - To save data in an organization's vault, select the organization's name. (Optional) Choose a [Collection](https://bitwarden.com/help/create-collections/) to organize the imported items and share with other members. (You can only choose a collection where you have [**can manage**](https://bitwarden.com/help/about-collections/#collections-permissions/) permission.)
3. From the **File format** dropdown menu, select the [import file format](https://bitwarden.com/help/import-faqs/#q-what-file-formats-does-bitwarden-support-for-import/).
4. Select **Choose File** and pick the file or copy and paste your file’s contents into the text box.

> [!WARNING] Duplicative Imports
> Importing does not check for duplicates. If you import the same file more than once or import items already in your vault, duplicate items will be created.
5. Select **Import data**. If you are importing a password protected `.json `file, enter the password into the **Confirm vault import** window that appears.
6. After your data is imported, delete the exported data file from your computer. This will protect you in the event your computer is compromised. If you're importing to Bitwarden from another password manager or browser, you may also want to delete data from that tool.

### CLI

To import data to your vault, use the following [CLI](https://bitwarden.com/help/cli/) command:

```
bw import <format> <path>
```

`bw import` requires a format (use `bw import --formats` to retrieve a list of formats) and a path, for example:

```
bw import <format> /Users/myaccount/Documents/mydata.csv
```

After your data is imported, delete the exported data file from your computer. This will protect you in the event your computer is compromised. If you're importing to Bitwarden from another password manager or browser, you may also want to delete data from that tool.

## Import to a collection

Import data to a [collection](https://bitwarden.com/help/create-collections/) to organize and share items with like your immediate teammates or family. If you're administering a Bitwarden organization, consider [importing data to an organization](https://bitwarden.com/help/import-to-org/) instead.

When on the **Import** page, select your organization’s **Vault** and the **Collection**:

![Import to a collection](https://bitwarden.com/assets/5i5K8TyWXdbpJLNlsfyd3v/ff5bd0dedb26341e355c8537faafee2e/2025-12-17_11-28-45.png)
*Import to a collection*

## Troubleshoot import errors

If a limit is exceeded or the file contains unassigned items, you will see an “Import error” message. No data is added to your vault when an import is rejected.

### File limits

Imported files can contain up to:

- 40,000 items
- 2,000 folders
- 2,000 collections
- 7,000 item-folder relationships (For example, a single item in three folders is counted as three item-folder relationships.)
- 80,000 item-collection relationships (For example, a single item in three collections is counted as three item-collection relationships.)

If your file is too large, split it into smaller ones and import each separately.

### Field length limits

If an item in your file (typically a `.csv`) exceeds a field’s **encrypted** character limit, Bitwarden will not import any of its contents. The “Import error” message will appear with details identifying the specific issue(s).

> [!TIP] Character counts when encryption
> Bitwarden's encryption process expands text 30-50% during import, which may push your field(s) beyond the character limit. For example, a `Notes `field—the most common offender—can increase from 8,000 to over 10,000 characters, exceeding the limit and triggering the error.

To fix this error and upload your data:

1. Open your `.csv` file in a text editor or spreadsheet program.
2. Review the error message details to find the item(s) causing the issue. For example, here’s how to interpret the following error:
`[2] [Login] “My New Item”: The field Notes exceeds the maximum encrypted value length of 10000 characters.`

 - `[2]` is the index number where the offending item is located, adjusted to match row numbering in most spreadsheet programs.
 - `[Login]` is the vault item `type` of the offending item.
 - `"My New Item"` is the name of the offending item.
 - `Notes` is the specific field that exceeds the character limit.
 - `10000` is the character limit allowed for that field.
3. Reduce the character count or delete the offending item(s).
4. Save the file.
5. Go back to Bitwarden and [import the updated file](https://bitwarden.com/help/import-data/#import-to-your-individual-vault/).

### File contains unassigned items

Organization users (not [admins or owners](https://bitwarden.com/help/user-types-access-control/#member-roles/)) must assign all imported credentials to at least one collection. There are two ways to fix this import error:

- Assign an existing collection where you have the **Manage collection** permission.
- Create a new collection for the unassigned items. [Customize your import file](https://bitwarden.com/help/condition-bitwarden-import/) by entering a new collection name. This will automatically create that collection and add the items to it.

> [!NOTE] File contains unassigned items error
> To minimize this error, turn on the [Restrict collection creation to owners and admins setting](https://bitwarden.com/help/collection-management/#collection-management-settings/) to prevent users from creating collections.

### Organization can only have a maximum of two collections

Free organizations can have up to two [collections](https://bitwarden.com/help/about-collections/). If you try importing a file that specifies more than two collections, an import error will appear. There are a few options to correct this:

- If you are trying to import a `.csv` or `.json`, [edit the file](https://bitwarden.com/help/condition-bitwarden-import/) to remove the additional collections.
- Upgrade your plan so you can create more collections and import your file as-is.
