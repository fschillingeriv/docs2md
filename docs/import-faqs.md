---
URL: https://bitwarden.com/help/import-faqs/
---

# Import & Export FAQs

This article contains frequently asked questions (FAQs) regarding import & export.

### Q: How do I import my data if I don’t see my service on the import options list?

**A:** If we don't have official support for the service you are using, manually condition a `.csv` or `.json` for import into Bitwarden. For more information about how to do this, see [Condition a Bitwarden .csv or .json](https://bitwarden.com/help/condition-bitwarden-import/).

### Q: How do I import items directly to collections?

**A:** You can import items into existing collections by appropriately conditioning a `.json` before before importing, or you can define new collections within your import file in order to create new collections when you upload the file. [Learn how](https://bitwarden.com/help/condition-bitwarden-import/).

### Q: Why did importing create duplicate vault items?

**A:** Every import operation creates every new record as an item in your vault, regardless of whether matching vault items already exist in your vault. Prior to import, we recommend either:

- Editing your import file to only include net-new vault Items.
- Purging your vault before an import operation.

Individual vaults can be purged from the **Settings** → **My account** page. Organization vaults can be purged from the Organization**Settings** → **Organization info** page.

### Q: What file formats does Bitwarden support for import?

 **A:** The following formats are supported out-of-the-box:

> [!TIP] If import format isn't listed.
> If your format is not listed below, manually [create a Bitwarden .csv or .json](https://bitwarden.com/help/condition-bitwarden-import/).

- [1Password (1pif)](https://bitwarden.com/help/import-from-1password/)
- [1Password 6 & 7 Windows (.sv)](https://bitwarden.com/help/import-from-1password/)
- [1Password 6 & 7 Mac (csv)](https://bitwarden.com/help/import-from-1password/)
- 1Password (1pux)
- Ascendo DataVault (csv)
- Avast Passwords (csv)
- Avast Passwords (json)
- Avira (json)
- BlackBerry Password Keeper (csv)
- Blur (csv)
- [Brave (csv)](https://bitwarden.com/help/import-from-chrome/)(select **Chrome**)
- Buttercup (csv)
- [Chrome (csv)](https://bitwarden.com/help/import-from-chrome/)
- Clipperz (html)
- Codebook (csv)
- Dashlane (json)
- Dashlane (csv)
- Edge (csv)
- Encryptr (csv)
- Enpass (csv)
- Enpass (json)
- [Firefox (csv)](https://bitwarden.com/help/import-from-firefox/)
- F-Secure KEY (fsk)
- GNOME Passwords and Keys/Seahorse (json)
- Kaspersky Password Manager (txt)
- KeePass 2 (xml)
- KeePassX (csv)
- Keeper (csv)
- [LastPass (csv)](https://bitwarden.com/help/import-from-lastpass/)
- LogMeOnce (csv)
- Meldium (csv)
- mSecure (csv)
- Myki (csv)
- [Microsoft Edge (csv)](https://bitwarden.com/help/import-from-chrome/)(select **Chrome**)
- Netwrix Password Secure (csv)
- Nordpass (csv)
- [Opera (csv)](https://bitwarden.com/help/import-from-chrome/)(select **Chrome**)
- Padlock (csv)
- Passbolt (csv)
- PassKeep (csv)
- Passky (json)
- Passman (json)
- Passpack (csv)
- Password Agent (csv)
- Password Boss (json)
- Password Dragon (xml)
- Password Depot 17 (xml)
- Password Safe (xml)
- PasswordWallet (txt)
- PasswordXP (csv)
- ProtonPass (json)
- Psono (json)
- RememBear (csv)
- RoboForm (csv)
- Safari and macOS (csv)
- SafeInCloud (xml)
- SaferPass (csv)
- SecureSafe (csv)
- SplashID (csv)
- Sticky Password (xml)
- True Key (csv)
- Universal Password Manager (csv)
- [Vivaldi (csv)](https://bitwarden.com/help/import-from-chrome/)
- Yoti (csv)
- Zoho Vault (csv)
