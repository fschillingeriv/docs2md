---
URL: https://bitwarden.com/help/import-from-safari/
---

# Import from macOS & Safari

Use this article for help exporting data from the following platforms, and importing into Bitwarden.

- Safari (macOS and iOS)
- Passwords app (macOS)

> [!TIP] Safari/macOS Export Version
> Exporting passwords requires **Safari 15.0+** or **macOS Monterey (12.0)+**.

## Export from Safari or macOS

You can export your passwords directly from Safari on your mac computer or from macOS Passwords:

### Safari

## From your desktop

To export your data from Safari:

1. Select **File** → **Export browsing data to file** from the macOS menu bar, choose passwords, and select **Download**:

![Export from Safari](https://bitwarden.com/assets/3j4W80s3G7wqFtVrbzKMO4/36308c2c647912bf204739f2bc5f80f2/2024-12-30_12-58-55.png)
2. Save your export to any location and use Touch ID or your macOS password to complete the export.

## From an iPhone

To export data from Safari:

1. Open the **Settings** app on your iPhone and navigate to **Apps** → **Safari**.
2. Scroll down to the History and Website Data section and tap **Export**.
3. Choose the **Passwords** option and tap **Save to Downloads**.

Your data will be saved without encryption into your iCloud Drive. As always, make sure you delete export files once your data is imported to Bitwarden.

### macOS Passwords app

To export data from the macOS Passwords app:

1. Locate and open the macOS **Passwords** app. You'll be prompted to use Touch ID or your password to continue.
2. Once your app is unlocked, select **File** and then **Export All Passwords to File...**.

![Export macOS Passwords](https://bitwarden.com/assets/6r88eOsL7rY2f6KJj4U79x/3fbfbc41456deaf86a48e85173190405/2025-03-11_09-47-02.png)
3. You will be prompted with a dialog confirming that you want to export saved passwords. Select **Export Passwords...** to continue.
4. Save your export to any location and use Touch ID or your password to complete the export.

## Import to Bitwarden

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

## Troubleshoot import errors

If an “Import error” message appears, no data was added to your vault. [Fix the import file issue](https://bitwarden.com/help/import-data/#troubleshoot-import-errors/) and try again.

### iCloud/Mac Keychain/Safari import issues

As of Safari 15.0, you can export passwords from Safari in a `.csv` file. After downloading the file, [condition your .csv](https://bitwarden.com/help/condition-bitwarden-import/) to match Bitwarden's format and import your data.
