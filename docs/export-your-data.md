---
URL: https://bitwarden.com/help/export-your-data/
---

# Export Vault Data

Export your vault data, including logins and notes, to back up important information or [transfer to a new Bitwarden vault](https://bitwarden.com/help/import-data/). No unencrypted data is transferred over the internet, because data is decrypted locally by the client before exporting.

> [!TIP] Cloud-stored, no need for export
> If you’re adding Bitwarden to a new device and your account is hosted on our cloud servers, you don’t need to create an export. Instead, [download Bitwarden](https://bitwarden.com/download/) on your new device and log in with your existing account.

> [!WARNING] Careful w/ Exports
> Unless you are using an [encrypted export](https://bitwarden.com/help/encrypted-export/), do not store or send the exported file over insecure channels, like email, and delete the file immediately after use.

## Export file types

Exports can be downloaded in a few formats:

- `.json` (plaintext)
- `.csv` (plaintext)
- [.json (Encrypted)](https://bitwarden.com/help/encrypted-export/)
- `.zip (with attachments)` (includes a `.json` file and your attachments)

> [!NOTE] .zip exports
> `.zip` exports are currently only available for individual vault data.
- (**iOS 26 only**) export directly to another app

> [!NOTE] What is CXP
> Exporting directly to another app requires that the target app supports the [Fido Credential Exchange Protocol (CXP)](https://fidoalliance.org/specifications-credential-exchange-specifications).

Review [example .csv and .json files](https://bitwarden.com/help/condition-bitwarden-import/) to decide which format is best for you. We recommend the encrypted `.json` option for best security and most complete export. Only `.json` exports include:

- Cards
- Identities
- [Stored passkeys](https://bitwarden.com/help/storing-passkeys/)
- [SSH keys](https://bitwarden.com/help/ssh-agent/)

No export formats include trash items or [Sends](https://bitwarden.com/help/about-send/). For a complete list of all items and fields included in an individual vault export, check out this ⬇️ [.json sample](https://bitwarden.com/assets/3klSoZBBd57skEvwFkcMJc/9dfe5d696c102cd32da88dc325706738/Individual_vault_export.json).

## Export an individual vault

> [!NOTE] Exporting personal data; no org data
> Individual vault exports do not include organization-owned data. Only admins, owners, and some custom roles can [export organization items](https://bitwarden.com/help/export-organization-items/) via the web app or CLI. Members with **Manage collection** [permission](https://bitwarden.com/help/collection-permissions/) can, however, export data from collections they can access.

### Web app

To export vault data:

1. Select **Tools**.
2. Select **Export**:

![Export items](https://bitwarden.com/assets/5PUGzasNsQnABG9gtso4o3/4e4880193ff45c22f0474c129e68e4e3/2025-12-17_11-43-59.png)
*Export items*
3. From the **Export from** dropdown menu, select which data to download:

 - Select **My vault** for your individual vault’s items.
 - Select an organization vault’s name, which will include data from collections where you have [**Manage collection**](https://bitwarden.com/help/collection-permissions/) permission.
4. Select a **File Format**: `.json`, `.csv`, `.json (Encrypted)`, or `.zip (with attachments)`).
5. (Optional) If you choose `.json (Encrypted)`, select an **Export type**for the [encrypted file](https://bitwarden.com/help/encrypted-export/):

 - **Account restricted:** This file can only be imported to the current Bitwarden account that generated the encrypted export file. 

> [!WARNING] Encryption Key Impact on Encrypted Exports
> **Account restricted**exports can not be imported to a different account. Additionally, [rotating your account's encryption key](https://bitwarden.com/help/account-encryption-key/) will render an account restricted export impossible to decrypt. **If you rotate your account encryption key, replace any old files with new ones that use the new encryption key.**
> 
> If you wish to import an encrypted `.json` file onto a different Bitwarden account, select the **Password protected**export type when creating an export.
 - **Password protected:**This file can be imported to any Bitwarden account by utilizing the password set during the encrypted export process.

> [!TIP] Password generator for export
> Select [generate] to securely generate a unique password for the export. If you do, be sure to save that password in a safe place.
6. Select **Export**.
7. Enter your master password or an email verification code to confirm.

Export files will be saved **to the location set by your browser**. By default this is typically a Downloads folder, but you can change it within the web browser.

### Browser extension

To export vault data:

1. Select the ⚙️ **Settings** icon.
2. Select **Vault options**.
3. Select **Export vault**.
4. From the **Export from** dropdown menu, select which data to download:

 - Select **My vault** for your individual vault’s items.
 - Select an organization vault’s name, which will include data from collections where you have [**Manage collection**](https://bitwarden.com/help/collection-permissions/) permission.
5. Select a **File Format**: `.json`, `.csv`, `.json (Encrypted)`, or `.zip (with attachments)`).
6. (Optional) If you choose `.json (Encrypted)`, select an **Export type**for the [encrypted file](https://bitwarden.com/help/encrypted-export/):

 - **Account restricted:** This file can only be imported to the current Bitwarden account that generated the encrypted export file. 

> [!WARNING] Encryption Key Impact on Encrypted Exports
> **Account restricted**exports can not be imported to a different account. Additionally, [rotating your account's encryption key](https://bitwarden.com/help/account-encryption-key/) will render an account restricted export impossible to decrypt. **If you rotate your account encryption key, replace any old files with new ones that use the new encryption key.**
> 
> If you wish to import an encrypted `.json` file onto a different Bitwarden account, select the **Password protected**export type when creating an export.
 - **Password protected:**This file can be imported to any Bitwarden account by utilizing the password set during the encrypted export process.

> [!TIP] Password generator for export
> Select [generate] to securely generate a unique password for the export. If you do, be sure to save that password in a safe place.
7. Select **Export vault**.
8. Enter your master password or an email verification code to confirm.
9. Select **Export vault**.

Export files will be saved **to the location set by your browser**. By default this is typically a Downloads folder, but you can change it within the web browser.

### Desktop

To export vault data:

1. Select **Export** from the navigation menu.
2. From the **Export from** dropdown menu, select which data to download:

 - Select **My vault** for your individual vault’s items.
 - Select an organization vault’s name, which will include data from collections where you have [**Manage collection**](https://bitwarden.com/help/collection-permissions/) permission.
3. Select a **File Format**: `.json`, `.csv`, `.json (Encrypted)`, or `.zip (with attachments)`).
4. (Optional) If you choose `.json (Encrypted)`, select an **Export type**for the [encrypted file](https://bitwarden.com/help/encrypted-export/):

 - **Account restricted:** This file can only be imported to the current Bitwarden account that generated the encrypted export file. 

> [!WARNING] Encryption Key Impact on Encrypted Exports
> **Account restricted**exports can not be imported to a different account. Additionally, [rotating your account's encryption key](https://bitwarden.com/help/account-encryption-key/) will render an account restricted export impossible to decrypt. **If you rotate your account encryption key, replace any old files with new ones that use the new encryption key.**
> 
> If you wish to import an encrypted `.json` file onto a different Bitwarden account, select the **Password protected**export type when creating an export.
 - **Password protected:**This file can be imported to any Bitwarden account by utilizing the password set during the encrypted export process.

> [!TIP] Password generator for export
> Select [generate] to securely generate a unique password for the export. If you do, be sure to save that password in a safe place.
5. Select **Export vault**.
6. Enter your master password or an email verification code to confirm.
7. Select **Export vault**.

Export files will be saved **to the location set by your device**. By default this is typically a Downloads folder, but you can change it within the device settings.

### Mobile

To export vault data:

1. Tap the ⚙️ **Settings** icon.
2. Tap **Vault**.
3. Tap **Export vault**.

> [!NOTE] CXP on iOS
> On iOS 26, you can choose between **Export vault to a file**and **Export vault to another app**. 
> 
> If you choose **Export vault to a file**, continue with these instructions. If you choose **Export vault to another app**, follow the simple on-screen process to export data directly to any other app that supports the [FIDO Credential Exchange Protocol](https://fidoalliance.org/specifications-credential-exchange-specifications).
4. Select a **File Format**: `.json`, `.csv`, or `.json (Password protected)`.

![Export vault on mobile](https://bitwarden.com/assets/6IvRA9oYfTvO9GxylX2MMh/528b65ca6d83f0f28c469b62078570d5/2025-01-22_09-51-29.png)
5. (Optional) If you choose `json (Password protected)`, enter a new password. If you import this file back into Bitwarden, you'll need to enter that password.
6. Enter your master password.
7. Select **Export**.

Export files will be saved **to the location set by your device**. By default this is typically a Downloads folder, but you can change it within the device settings.

### CLI

> [!TIP] Sync before export on CLI
> Sync your vault with `bw sync` before exporting to ensure the most up-to-date information is included.

To export your individual vault data from the [CLI](https://bitwarden.com/help/cli/), use the `export` command. By default, `export` will export your vault as a `.csv` and save the file to the working directory. This behavior can be altered using options:

```
bw export --output /users/me/documents/ --format json --password mYP@ssw0rd
```

The `--password` option can be used to specify a password to use to encrypt `encrypted_json` exports instead of your [account encryption key](https://bitwarden.com/help/account-encryption-key/).
