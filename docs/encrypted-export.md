---
URL: https://bitwarden.com/help/encrypted-export/
---

# Encrypted Exports

Vault data can be exported in an encrypted `.json` file [for individuals](https://bitwarden.com/help/export-your-data/) and [for organizations](https://bitwarden.com/help/export-organization-items/). Two encrypted export types are available: 

- **Account restricted:** Export an encrypted file that can only be re-imported to the Bitwarden account or organization that generated the encrypted export file. This process utilizes the relative [account ](https://bitwarden.com/help/account-encryption-key/)or organization encryption key specific to the restricted export.
- **Password protected:** Export an encrypted file protected with a password of your choosing. This file can be decrypted with the password and can be imported to any Bitwarden account. The specified password is salted, used to derive an encryption key using [your configured KDF settings](https://bitwarden.com/help/kdf-algorithms/#changing-kdf-algorithms/), and finally stretched with HDKF into a new encryption key, which encrypts your data, and message authentication code (MAC).

> [!WARNING] Encryption Key Impact on Encrypted Exports
> **Account restricted**exports can not be imported to a different account. Additionally, [rotating your account's encryption key](https://bitwarden.com/help/account-encryption-key/) will render an account restricted export impossible to decrypt. **If you rotate your account encryption key, replace any old files with new ones that use the new encryption key.**
> 
> If you wish to import an encrypted `.json` file onto a different Bitwarden account, select the **Password protected**export type when creating an export.

Encrypted exports will include items like logins, cards, secure notes, and identities. An encrypted export of the following plaintext login item:

```
{
 ...
 "login": {
 "username": "mylogin",
 "password": "mypassword",
 "totp": "otpauth://totp/my-secret-key"
 },
 ...
```

Will look something like:

```
{
 ...
 "login": {
 "username": "9.dZwQ+b9Zasp98dnfp[g|dHZZ1p19783bn1KzkEsA=l52bcWB/w9unvCt2zE/kCwdpiubAOf104os}",
 "password": "1o8y3oqsp8n8986HmW7qA=oiCZo872b3dbp0nzT/Pw=|A2lgso87bfDBCys049ano278ebdmTe4:",
 "totp": "2CIUxtpo870B)*^GW2ta/xb0IYyepO(*&G(&BB84LZ5ByZxu0E9hTTs6PHg0=8q5DHEPU&bp9&*bns3EYgETXpiu9898sxO78l"
 },
 ...
```

## Next steps

- Create an encrypted export [as an individual user](https://bitwarden.com/help/export-your-data/).
- Create an encrypted export [of your organization data](https://bitwarden.com/help/export-organization-items/).
- Re-import an encrypted export [as an individual user](https://bitwarden.com/help/import-data/).
- Re-import an encrypted export [as an organization](https://bitwarden.com/help/import-to-org/).
