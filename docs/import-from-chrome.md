---
URL: https://bitwarden.com/help/import-from-chrome/
---

# Import from Chrome, Edge, & Chromium Browsers

Quickly transfer your saved passwords in Chromium-based browsers, like Google Chrome, Microsoft Edge, and Opera, to your Bitwarden vault. There are two methods:

- [Export your browser data](https://bitwarden.com/help/import-from-chrome/#export-from-your-browser/) and import it into Bitwarden
- [Import directly from your browser](https://bitwarden.com/help/import-from-chrome/#import-directly-from-browser/) (desktop app only)

## Export & import a file from your browser

### Export from your browser

Export your data from a desktop or mobile browser.

### Desktop browser

To export passwords from Chrome or Edge on your desktop: 

1. Open your browser's settings and navigate to the password settings, for example `chrome://password-manager/settings` or `edge://wallet/passwords`.
2. Locate **Export Passwords** and click **Download file**. You may be prompted to enter your computer's password for authorization. For Microsoft Edge, this may be hidden behind a ⋯ menu in the Saved passwords section.
3. Specify a location to save your export to, and verify that the format is **comma-separated values** (**CSV**).
4. Select **Save** to finish exporting.

### Mobile browser

To export passwords from Chrome or Edge on your mobile device:

1. Tap the ⋯ menu button and tap **Password Manager**.
2. Tap **Settings**.
3. Tap **Export Passwords...**.

You may be prompted to enter your device PIN or a biometric for authorization.
4. Specify a location to save your export to.

### Import to Bitwarden

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

If an “Import error” message appears, no data was added to your vault. Fix the import file issue and try again.

## Import directly from browser

The Bitwarden desktop app can import passwords from these browsers without a manually exported file:

- Chrome
- Edge (Windows and macOS only)
- Opera
- Brave
- Vivaldi (Windows and macOS only)
- Arc (macOS only)

This option is available on Windows and macOS desktop apps when installed from the [downloads page](https://bitwarden.com/download/#downloads-desktop-applications/), and on Linux when installed via AppImage. The direct import method does not work with desktop apps downloaded from app stores at this time.

> [!NOTE] Antivirus may pop-up.
> The **Import directly from browser option**, specifically the process `bitwarden_chromium_import_helper.exe`, is known to be flagged by some EDR software, or on Windows by User Account Controls, when it attempts to pull credentials from browser storage:
> 
> - **As an administrator**, you can proactively set the `bitwarden_chromium_import_helper.exe` to run as an administrator through UAC or your EDR software to prevent it from failing or issuing warnings when your users attempt the import.
> - **As a user**, if you're prompted to allow this app to make changes to your device, select **Yes** to proceed with the import.

To import your data from a browser:

1. Log into the Bitwarden desktop app.
2. Select **File.**
3. Select **Import data**.
4. From the **Vault** dropdown menu, select where to save the data:

 - **Individual vault**: Select **My vault** and (optional) choose a **Folder** to move the items.
 - **Organization vault**: Select the organization vault’s name and choose a **Collection**. (The [**Manage collection**](https://bitwarden.com/help/about-collections/#collections-permissions/) permission is required.)
5. From the **File format** dropdown menu, select your browser. If that browser is compatible and installed on the same device, two options will appear below.
6. Select **Import directly from browser**:

![Import directly from browser](https://bitwarden.com/assets/1dZKYVPQpd1TVDcmUuwLq2/23e9b222768964108ade8c02e52134ee/Directly_import_with_Chromium.png)
7. Select the **Browser Profile** that contains your passwords.
8. Select **Import**.
9. Enter your computer password to confirm.

> [!WARNING] Duplicative Imports
> Importing does not check for duplicates. If you import the same file more than once or import items already in your vault, duplicate items will be created.
