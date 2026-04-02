---
URL: https://bitwarden.com/help/vault-data/
---

# Encrypted Data

All vault data is encrypted by Bitwarden before being stored anywhere. To learn how, refer to the [Bitwarden Security Whitepaper](https://bitwarden.com/help/bitwarden-security-white-paper/#how-vault-items-are-secured/). Bitwarden is a zero knowledge encryption solution, meaning you are the only party with access to the keys required to decrypt the vault data. 

Listed below are examples of the data that is encrypted, as well as download links demonstrating the encrypted data. 

> [!NOTE] Privacy policy
> We encourage you to review our [privacy policy](https://bitwarden.com/privacy/) for more information.

Vault data that is encrypted:

- For all items:

 - Item names
 - Notes
 - Attachments

 - Attachment name
 - File contents
 - File encryption key
 - Custom field names and values
- For [logins](https://bitwarden.com/assets/yfr02nYyvD0GmjXzXjAu5/7e1091a1f05638807caa3268e3333038/login1__1_.json):

 - Usernames
 - Passwords

 - Password history
 - URIs (i.e. match detection strings)
 - Authenticator keys (i.e. TOTP secrets)
- For [cards](https://bitwarden.com/assets/5HYmBCBzT1qVE4yeqwY1F3/7330978a17d92c36e9765cda6834d8d5/card1.json):

 - Cardholder names
 - Numbers
 - Brands
 - Expiration dates
 - Security codes
- For [identities](https://bitwarden.com/assets/5ltDUVHgqqx1yfHIzv5e4k/40f8ae52b2c74feeab2d19e02ea87310/id1.json):

 - Names (Title/First/Middle/Last)
 - Usernames
 - Companies
 - Social Security numbers, passport numbers, and license numbers
 - Emails and phones
 - Address 1, Address 2, Address 3, City / Town, State / Province, Zip / Postal code, Country
- For [Sends](https://bitwarden.com/assets/5QUNWhFSzC7EIo8CaHjxta/681e78b34a6beba57e0e7e753a3c5ce3/send1.json):

 - Send names
 - Send text
 - Send file
 - Send notes
 - Send encryption key ([learn more](https://bitwarden.com/help/send-encryption/))
- [Folder](https://bitwarden.com/assets/6qRBtIOjOOjDryxVo35sQF/d3412d19a841da5ee13b9c73818f6a4c/folders1.json) names
- [Collection](https://bitwarden.com/assets/3KT79LDVKbIhF5cpNk5tL/5097c78255b6abd435233163085cda58/collection1.json) names

[Secrets Manager](https://bitwarden.com/help/secrets-manager-overview/) data that is encrypted:

- For [secrets](https://bitwarden.com/help/secrets/):

 - Secret names
 - Secret values
 - Secret notes
- [Project](https://bitwarden.com/help/projects/) names
- [Service account](https://bitwarden.com/help/machine-accounts/) names
- [Access token](https://bitwarden.com/help/access-tokens/) names (access token values are never stored by Bitwarden)

Some data, but **never vault or secrets data,**is used to provide the Bitwarden service to you. This is referred to as administrative data and can be accessed by Bitwarden. [Learn more](https://bitwarden.com/help/administrative-data/).
