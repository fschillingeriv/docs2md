---
URL: https://bitwarden.com/help/import-from-keeper/
---

# Import from Keeper

Use this article for help exporting data from Keeper and importing into Bitwarden. Bitwarden supports import of Keeper data that is exported as a `.csv` or `.json` file.

## Export from Keeper

To export data from the Keeper web app:

1. Select your account email in the top corner of the web app and select **Settings** from the dropdown:

![Export from Keeper](https://bitwarden.com/assets/37IrIjwTCvp8aeNOYgVINt/b5520f293391b24fa825eaa2e944788b/2025-01-06_09-30-34.png)
*Export from Keeper*
2. Select **Export** from the pop-up window.
3. Choose the **CSV** or **JSON**export file type.
4. Select **Export**.
5. Enter your master password.
6. Select **Export Now**.

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

There are two ways to import data when using a mobile device. Direct import with CXP is often the easiest, but is only supported by a limited number of password manager apps at this time.

### Most common method for mobile

For most devices, open a mobile browser. Log in to Bitwarden there and follow the [web app import steps](https://bitwarden.com/help/import-data/#tab-web-app-5ALQx9afSqWXX9jfXsY5sb/).

### Direct import with the Credential Exchange Protocol (CXP)

Bitwarden supports the [FIDO Credential Exchange Protocol (CXP)](https://fidoalliance.org/specifications-credential-exchange-specifications). This facilitates an alternate, often faster import path by removing the need to manually download and handle a data file. The password manager app that currently stores your data must also support CXP, and the steps vary by application.

#### CXP with iOS devices

To import data using a mobile device with **iOS 26+**:

1. Open the other CXP-compatible password manager app where your data is saved.
2. Depending on the app, find the export data option and choose which items to import. You may need to complete extra steps, like logging in or confirming you want to move data.

> [!NOTE] Apple Passwords CXP steps
> In the **Apple Passwords** app, for example:
> 
> 1. Tap the ⋯ **Options icon**.
> 2. Tap **Export Data to Another App**.
> 3. Check which passwords and passkeys you want to transfer from the list that appears. When done, tap **Continue**.
3. On the **Export Passwords** screen, tap **Continue**.
4. Select **Bitwarden** for the destination and then tap **Continue**.
5. Tap **Continue in "Bitwarden"**.
6. The Bitwarden app will open. Tap **Continue** to confirm the import.
7. Once complete, a message confirming that your data was imported will appear.

#### CXP with Android devices

To import data using a mobile device with **Android 10+**:

1. Open the Bitwarden app.
2. Tap **Settings**.
3. Tap **Vault**.
4. Tap **Import items**.
5. Tap **Import from another app**.
6. Select the other CXP-compatible password manager app where your data is saved and tap **Continue**.
7. Depending on the app, choose which items to import. You may need to complete extra steps, like logging in or confirming you want to move data.
8. Once complete, a message confirming that your data was imported will appear.

> [!NOTE] Android CXP doesn't support Dashlane.
> At this time, importing Dashlane data via CXP isn't supported on Android.

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

If an “Import error” message appears, no data was added to your vault. [Fix the import file issue](https://bitwarden.com/help/import-data/#troubleshoot-import-errors/) and try again.
