---
URL: https://bitwarden.com/help/authenticator-import-export/
---

# Import & Export Authenticator Data

You can import verification codes into Bitwarden Authenticator from supported applications, allowing you to quickly migrate existing codes without manually re-adding each one. You can also export your codes at any time to create backups.

## Import data

To import time-based one-time passwords (TOTPs) into Bitwarden Authenticator:

1. Tap the ⚙️ **Settings** **icon**.
2. Tap **Import**.
3. From the **File format** dropdown menu, choose the import file's source:

 - **Authenticator Export (JSON)**: Import a Bitwarden Authenticator or Bitwarden Password Manager `.json` export. Use the instructions in the following section for information on how to create a `.json` export with Bitwarden Authenticator. Importing a [Bitwarden Password Manager .json export](https://bitwarden.com/help/export-your-data/) will parse the file and import TOTP seeds.
 - **Google Authenticator (QR code)**: Import from Google Authenticator using a QR code, which can be made from the **Transfer accounts** screen in Google Authenticator. Scan the generated QR code with Bitwarden Authenticator to complete the import.

> [!TIP] Google Import Authenticator Android
> On Android, use the + **Add** icon on the home screen to scan a Google Authenticator QR code rather than navigating to **Settings**→ **Import**.
 - **LastPass (JSON)**: Import a LastPass Authenticator account export, which can be made from the LastPass Authenticator **Settings** → **Transfer accounts**screen.
 - **2FAS (.2fas)**: Import a 2FAS backup file, which can be made from the 2FAS **Settings** → **2FAS Backup** screen. Only backup files that are not password protected can be imported to Bitwarden Authenticator.
 - **Raivo (JSON) (iOS only)**: Import a Raivo OTP export, which can be made from the Raivo **Settings** screen using the **Export OTPs to ZIP archive option**. You will need to decrypt the `.zip` file using your master password and import the enclosed `raivo-otp-export.json` file to Bitwarden Authenticator.
 - **Aegis (Android only)**: Import an unencrypted Aegis .json export, which can be made from the Aegis **Import & Export** screen.

## Export data

You can export data that's stored locally in the Bitwarden Authenticator app. Any TOTPs synced from your Bitwarden vault, however, will need to be [exported through your vault](https://bitwarden.com/help/export-your-data/) separately, because they're not included in Bitwarden Authenticator exports.

To export data from Bitwarden Authenticator:

1. Open the ⚙️ **Settings**tab.
2. Tap **Export**.
3. Select your export's **File format** from the dropdown menu, `.json` or `.csv`.
4. Tap **Export items**.

> [!NOTE] Exporting from authenticator
> Exported data includes the `otpauth://totp/?secret=` string for each entry. If you want to store this data elsewhere or set up a second authenticator app, this is the most important data to save.

### Example exports

Bitwarden Authenticator exports data in the following formats. You may also use this section to condition your own import file if you're importing from a currently-unsupported provider:

### .json

```plain text
{
 "encrypted": false,
 "items": [
 {
 "favorite": false,
 "id": "52A4DFB0-F19E-4C9D-82A1-BBEE95BBEF81",
 "login": {
 "totp": "otpauth://totp/Amazon:alice@bitwarden.com?secret=IIO5SCP3766LMSAB5HJCQPNDCCNAZ532&issuer=Amazon&algorithm=SHA1&digits=6&period=30",
 "username": "alice@bitwarden.com"
 },
 "name": "Amazon",
 "type": 1
 },
 {
 "favorite": false,
 "id": "DC81A830-ED98-4F45-9B73-B147E40134AB",
 "login": {
 "totp": "otpauth://totp/Apple:alice@bitwarden.com?secret=IIO5SCQ3766LMSBB5HJCQPNDCCNAZ532&issuer=Apple&algorithm=SHA1&digits=6&period=30",
 "username": "alice@bitwarden.com"
 },
 "name": "Apple",
 "type": 1
 },
 {
 "favorite": false,
 "id": "4EF44090-4B6A-4E98-A94C-CF7B0F2CC35D",
 "login": {
 "totp": "otpauth://totp/Bitwarden:alice@bitwarden.com?secret=IIO5SCP3766LMSBB5HJCQPNDCCNAZ532&issuer=Bitwarden&algorithm=SHA1&digits=6&period=30",
 "username": "alice@bitwarden.com"
 },
 "name": "Bitwarden",
 "type": 1
 },
 {
 "favorite": false,
 "id": "59B09168-502A-4D38-B218-FACF66E6A365",
 "login": {
 "totp": "otpauth://totp/Microsoft:alice@bitwarden.com?secret=IIO5SCP3766LMSBB5HJCHPNDCCNAZ532&issuer=Microsoft&algorithm=SHA1&digits=6&period=30",
 "username": "alice@bitwarden.com"
 },
 "name": "Microsoft",
 "type": 1
 },
 {
 "favorite": false,
 "id": "789F095B-95B2-4816-A5F7-01095116C10E",
 "login": {
 "totp": "otpauth://totp/Reddit:alice@bitwarden.com?secret=IIO5SCP3766LNSBB5HJCQPNDCCNAZ532&issuer=Reddit&algorithm=SHA1&digits=6&period=30",
 "username": "alice@bitwarden.com"
 },
 "name": "Reddit",
 "type": 1
 }
 ]
}
```

### .csv

```plain text
folder,favorite,type,name,notes,fields,reprompt,login_uri,login_username,login_password,login_totp
,,login,Amazon,,,0,,alice@bitwarden.com,,otpauth://totp/Amazon:alice@bitwarden.com?secret=IIO5SCP3766LMSAB5HJCQPNDCCNAZ532&issuer=Amazon&algorithm=SHA1&digits=6&period=30
,,login,Apple,,,0,,alice@bitwarden.com,,otpauth://totp/Apple:alice@bitwarden.com?secret=IIO5SCQ3766LMSBB5HJCQPNDCCNAZ532&issuer=Apple&algorithm=SHA1&digits=6&period=30
,,login,Bitwarden,,,0,,alice@bitwarden.com,,otpauth://totp/Bitwarden:alice@bitwarden.com?secret=IIO5SCP3766LMSBB5HJCQPNDCCNAZ532&issuer=Bitwarden&algorithm=SHA1&digits=6&period=30
,,login,Microsoft,,,0,,alice@bitwarden.com,,otpauth://totp/Microsoft:alice@bitwarden.com?secret=IIO5SCP3766LMSBB5HJCHPNDCCNAZ532&issuer=Microsoft&algorithm=SHA1&digits=6&period=30
,,login,Reddit,,,0,,alice@bitwarden.com,,otpauth://totp/Reddit:alice@bitwarden.com?secret=IIO5SCP3766LNSBB5HJCQPNDCCNAZ532&issuer=Reddit&algorithm=SHA1&digits=6&period=30
```
