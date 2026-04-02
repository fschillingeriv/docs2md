---
URL: https://bitwarden.com/help/account-encryption-key/
---

# Encryption Key Rotation

Each unique Bitwarden account has an encryption key which is used to encrypt all vault data.

> [!NOTE] Rotating encryption key
> **Rotating your encryption key is a potentially dangerous operation.** Please read this section thoroughly to understand the full ramifications of doing so.

Rotating your account’s encryption key generates a new encryption key that is used to re-encrypt all vault data. You should consider rotating your encryption key if your account has been compromised in such a way that someone has obtained your encryption key.

## Before rotating

Before rotating, you should take the following actions to protect against potential data loss or corruption.

#### Re-create any account restricted exports

If you are using Account restricted [encrypted exports](https://bitwarden.com/help/encrypted-export/) to store long-term secure backups, you should preemptively re-create the encrypted export of your vault data using the Password protected option

Account restricted encrypted exports use your encryption key to encrypt **and decrypt** your vault data, meaning that a rotated encryption key will not be able to decrypt an export created with the "stale" (prior-to-rotation) key. Replacing your Account restricted export with a Password protected export ensures you'll be able, if you need to, to re-import your data after rotating your account encryption key.

#### Log out of client applications

Before you rotate an encryption key, we recommend you log out of any logged-in sessions on Bitwarden client applications (desktop app, browser extension, mobile app, and so on). Logging out of client applications in this way will prevent sessions from using the "stale" (prior-to-rotation) encryption key. After doing so, logging back in as normal will use the new encryption key.

**Making changes in a session with a "stale" encryption key will cause data corruption that will make your data unrecoverable.**

## How to rotate an encryption key

> [!NOTE] Backup prior to key rotation
> Bitwarden recommends creating a backup of your items prior to rotating your account encryption key. Password protected `.json` exports are the recommended format for this scenario, however any format **except Account restricted** `.json` exports can be re-imported after your key is rotated. To learn more about vault exports and what items are included, see [Export Vault Data](https://bitwarden.com/help/export-your-data/).

To rotate your account encryption key:

1. In the web app, navigate to**Settings** → **Security** → **Master password**:

![Master password settings](https://bitwarden.com/assets/2Svv0PwlH9i7SSK73dlv9A/e451afb190346e492110a7bf1bd3a518/Master_password_settings.png)
*Master password settings*
2. Enter your **Current master password** and create/confirm a **New master password**.
3. Check the **Also rotate my account's encryption key** checkbox and accept the dialog.
4. Select **Change master password**.
