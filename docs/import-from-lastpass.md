---
URL: https://bitwarden.com/help/import-from-lastpass/
---

# Import from LastPass

Use this article for help exporting data from LastPass and importing into Bitwarden.

## Export from LastPass

You can [export your data from LastPass](https://support.lastpass.com/help/export-your-passwords-and-secure-notes-lp040004) from their web vault or from a LastPass browser extension:

> [!TIP] Skip LastPass export for direct
> You can skip this step and immediately start importing to Bitwarden using the [Direct import option](https://bitwarden.com/help/import-from-lastpass/#import-to-bitwarden/), available only on Bitwarden browser extensions and desktop apps.

### LastPass web vault

To export your data from the LastPass web vault:

1. Select the [rocket] **Advanced Options** option on the left sidebar:

![Export from web vault ](https://bitwarden.com/assets/5uCdlKvfGTjYIEJvKtpbQw/14cd0e6bfb36a53b1f1d6f88d3808a90/lastpassadvancedoptions.png)
2. From the Manage your Vault section, select the **Export** option. At this stage, LastPass will send you an email to confirm the export.
3. In your inbox, confirm the export, return to your LastPass web vault, and select the **Export** option again to complete export.

Depending on your browser, your data will either be automatically saved as a `.csv` or printed to the screen in a `.csv` format:

![LastPass export ](https://bitwarden.com/assets/6TIRhpByBC4coLrP58zG8a/fb2da8df01a2e0f56e87f45612182e86/lastpass-copy.png)
4. If your data was printed to the screen, highlight the text and copy and paste it into a new `export.csv` file.

> [!WARNING] Lastpass Export Bug
> Some users have reported a bug which changes special characters in your passwords (`&`, `<`, `>`, and so on) to their HTML-encoded values (for example, `&amp;`) in the printed export.
> 
> If you observe this bug in your exported data, use a text editor to find and replace all altered values before importing into Bitwarden.

### LastPass browser extension

To export your data from a LastPass browser extension:

1. In the browser extension, navigate to **Account** → **Fix a problem yourself** → **Export vault items** → **Export data for use anywhere**.

> [!NOTE] Old LP Export Proc
> If you're using an old version of the LastPass browser extension, you may instead need to navigate to **Account Options** → **Advanced** → **Export** → **LastPass CSV File**.
2. Enter your master password to validate the export attempt.

Depending on your browser, your data will either be automatically saved as a `.csv` or printed to the screen in a `.csv` format:

![LastPass export ](https://bitwarden.com/assets/6TIRhpByBC4coLrP58zG8a/fb2da8df01a2e0f56e87f45612182e86/lastpass-copy.png)
3. If your data was printed to the screen, highlight the text and copy and paste it into a new `export.csv` file.

## Import to Bitwarden

Import directly from LastPass or use an [exported file](https://bitwarden.com/help/import-from-lastpass/#export-from-lastpass/) from LastPass. If you're a member of a team using SSO with LastPass, a LastPass administrator will need to complete a short setup procedure before you can use the [**Direct import**](https://bitwarden.com/help/import-from-lastpass/#direct-import-with-sso/) option to import your personal data. In all cases, data is [encrypted](https://bitwarden.com/help/what-encryption-is-used/) locally before being sent to the server for storage.

> [!NOTE] Items not imported
> While some item types cannot be imported, you can still add them to a vault:
> 
> - Upload [file attachments](https://bitwarden.com/help/attachments/) to the new vault individually.
> - Re-create [Sends](https://bitwarden.com/help/about-send/) in the new vault.

### Direct import

> [!TIP] Setup SSO for LP Direct Import
> If you're a member of a team using SSO with LastPass, a LastPass administrator will need to complete a short setup procedure before you can use the **Direct import** option ([learn more](https://bitwarden.com/help/import-from-lastpass/#direct-import-with-sso/)).

Password Manager **browser extensions and desktop apps** can import individual vault data directly from your LastPass account, without requiring you to upload a file. To do a direct import:

1. Log in to the Bitwarden browser extension or desktop app.
2. In the browser extension, select the **Settings** tab and choose **Vault** and then the **Import items** option**.** Or, in the desktop app, select **Import**from the navigation menu.
3. Complete the following fields from the drop down menus:

 - **Vault** or **Import destination:**Select the import destination such as your individual vault or an organizational vault that you have access to.
 - **Folder** or **Collection:** Select if you would like the imported content moved to a specific folder or organization collection that you have access to.
 - [**File format**](https://bitwarden.com/help/import-faqs/#q-what-file-formats-does-bitwarden-support-for-import/)**:** Select **LastPass**.
 - In the LastPass Instructions box, choose the **Import directly from LastPass** option.
 - Enter your **LastPass email**. If you're importing on behalf of your business, we recommend using the credentials of a LastPass [admin](https://support.lastpass.com/s/document-item?language=en_US&bundleId=lastpass&topicId=LastPass/uac_admin_roles.html&_LANG=enus). Using super admin credentials may cause import to fail.
4. Select the **Import data**button to trigger the import.
5. You will be prompted for your LastPass master password or, if your LastPass account uses SSO, to log in to your IdP. In either case, follow the prompts to log in to your LastPass account.

> [!TIP] Direct import w/ LastPass MFA
> If your LastPass account has multi-factor authentication activated, you will be prompted to enter a one-time passcode from your authenticator app. If you use Duo for MFA, only in-app approval is supported to fulfill your MFA requirement.

Additional items such as [file attachments](https://bitwarden.com/help/attachments/) and trash will need to be manually uploaded to your vault.

### File import

Files can be imported to Bitwarden from most Password Manager apps (learn how to [export a file from LastPass](https://bitwarden.com/help/import-from-lastpass/#export-from-lastpass/)). In this section, we'll focus on importing using the web app:

1. Log in to the web vault at [https://vault.bitwarden.com](https://vault.bitwarden.com), [https://vault.bitwarden.eu](https://vault.bitwarden.eu), or `https://your.bitwarden.domain.com` if self-hosting.
2. Select **Tools** → **Import** from the navigation:

![Import items](https://bitwarden.com/assets/1NbyPb9dN545ZqKGRZYB3x/e6b8f3f31aa82bb05cef12c5a5c4c193/2025-12-17_11-25-08.png)
*Import items*
3. Complete the following fields from the drop down menus:

 - **Import destination:**Select the import destination such as your individual vault or an organizational vault that you have access to.
 - **Folder or Collection:** Select if you would like the imported content moved to a specific folder or organization collection that you have access to.
 - [**File format**](https://bitwarden.com/help/import-faqs/#q-what-file-formats-does-bitwarden-support-for-import/)**:** Select the import file format.
4. Select **Choose File**and add the file to import or copy/paste the contents of your file into the input box.

> [!WARNING] Duplicative Imports
> Importing does not check for duplicates. If you import the same file more than once or import items already in your vault, duplicate items will be created.
5. Select **Import** to trigger the import. If you are importing a password protected `.json `file, enter the password into the **Confirm vault import** window that will appear.
6. After successful import, delete the import source file from your computer. This will protect you in the event your computer is compromised.

Additional items such as [file attachments](https://bitwarden.com/help/attachments/), and trash will need to be manually uploaded to your vault.

### CLI

To import data to your vault from the CLI, use the following command:

```
bw import <format> <path>
```

`bw import` requires a format (use `bw import --formats` to retrieve a list of formats) and a path, for example:

```
bw import <format> /Users/myaccount/Documents/mydata.csv
```

After successful import, delete the import source file from your computer. This will protect you in the event your computer is compromised.

## Direct import with SSO

> [!NOTE] Supported IdP for LastPass direct import
> The following IdPs are not supported for direct import by LastPass accounts using SSO:
> 
> - Google Workspace
> - ADFS

If you're an administrator of a team using SSO with LastPass, you will need to complete the following before your team can use the **Direct import** option:

- Add `bitwarden://sso-callback-lp` and `bitwarden://import-callback-lp` as permitted callback URLs (in some IdPs, "Reply URLs" or "Redirect URLs") in your IdP's LastPass application.

If your users will use the Password Manager browser extension, add:

- Add `https://vault.bitwarden.com/sso-connector.html?lp=1`, `https://vault.bitwarden.eu/sso-connector.html?lp=1`, or `https://your.server.com/sso-connector.html?lp=1` as a permitted callback URL (in some IdPs, "Reply URL" or "Redirect URL") in your IdP's LastPass application.
- Add `chrome-extension://nngceckbapebfimnlniiiahkandclblb` and/or `chrome-extension://jbkfoedolllekgbhcbcoahefnbanhhlh` as a permitted callback URL (in some IdPs, "Reply URL" or "Redirect URL") in your IdP's LastPass application. Firefox extensions do not currently support direct import if your LastPass organization uses SSO.

## Troubleshoot import errors

If an "Import error" message appears, no data was added to your vault. [Fix the import file issue](https://bitwarden.com/help/import-data/#troubleshoot-import-errors/) and try again.

### Organization can only have a maximum of two collections

Free Bitwarden organizations can have up to two [collections](https://bitwarden.com/help/about-collections/) to organize items. When importing data, Bitwarden treats LastPass `grouping` values like collections. If your LastPass export contains three or more `grouping` values and you're part of a [free Bitwarden organization](https://bitwarden.com/help/password-manager-plans/), you'll receive a "This organization can only have a maximum of two collections" import error. The following `.csv`, for example, would cause this error:

```
url,username,password,totp,extra,name,grouping,fav
https://www.facebook.com/login.php,username,password,,,Facebook,Social,0
https://twitter.com/login,username,password,,,Twitter,Social,0
https://asana.com/,login,password,,,Asana,Productivity Tools,0
https://github.com/login,username,password,,,Github,Productivity Tools,0
https://www.paypal.com/login,username,password,,,Paypal,Finance,0
https://www.bankofamerica.com/,username,password,,,Bankofamerica,Finance,0
```

To solve this issue, delete the `grouping` column and the `grouping` datum for each item, including the trailing comma, for example edit:

```
https://github.com/login,username,password,,,Github,Productivity Tools,0
```

down to:

```
https://github.com/login,username,password,,,Github,0
```
