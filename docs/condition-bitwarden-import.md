---
URL: https://bitwarden.com/help/condition-bitwarden-import/
---

# Import from a Custom File

This article describes how to format` .csv` and `.json` files for importing into Bitwarden. The formats are identical to [Bitwarden vault exports](https://bitwarden.com/help/export-your-data/). To select a file type and format, determine the destination vault and which item types you need to import:

- Format your file based on whether you're importing to an [individual](https://bitwarden.com/help/import-data/#import-to-your-individual-vault/) or [organization vault](https://bitwarden.com/help/import-to-org/#import-to-an-organization-vault/).
- Bitwarden `.csv` files only include logins and secure notes. If you need to also handle identities and cards, use a `.json` file.

> [!NOTE] Items not imported
> While some item types cannot be imported, you can still add them to a vault:
> 
> - Upload [file attachments](https://bitwarden.com/help/attachments/) to the new vault individually.
> - Re-create [Sends](https://bitwarden.com/help/about-send/) in the new vault.

## Condition a .csv

### .csv for individual vault

⬇️ [Download sample csv](https://bitwarden.com/assets/4j3wYIYVQYW2MZUBogVxM3/2299910bb8fc93f6a8916d870be0458c/bitwarden_export.csv) 

Create a UTF-8 encoded plaintext file with the following header as the first line in the file:

```
folder,favorite,type,name,notes,fields,reprompt,login_uri,login_username,login_password,login_totp
```

For example:

```
folder,favorite,type,name,notes,fields,reprompt,login_uri,login_username,login_password,login_totp
Social,1,login,Twitter,,,0,twitter.com,me@example.com,password123,
,,login,EVGA,,,,https://www.evga.com/support/login.asp,hello@bitwarden.com,fakepassword,TOTPSEED123
,,login,My Bank,Bank PIN is 1234,"PIN: 1234",,https://www.wellsfargo.com/home.jhtml,john.smith,password123456,
,,note,My Note,"This is a secure note.",,,,,
```

When importing this file, select **Bitwarden (csv)** as your file format.

### .csv for organization

⬇️ [Download sample csv](https://bitwarden.com/assets/YYnGrBJO8O5Xv2O0dFW9Z/6de667ded7567da41dcdf4af5186311a/bitwarden_export_org.csv)

Create a UTF-8 encoded plaintext file with the following header as the first line in the file:

```
collections,type,name,notes,fields,reprompt,login_uri,login_username,login_password,login_totp
```

For example,

```
collections,type,name,notes,fields,reprompt,login_uri,login_username,login_password,login_totp
"Social,Marketing",login,Twitter,,,0,twitter.com,me@example.com,password123,
"Finance",login,My Bank,"Bank PIN is 1234","PIN: 1234",0,https://www.wellsfargo.com/home.jhtml,john.smith,password123456,
"Finance",login,EVGA,,,0,https://www.evga.com/support/login.asp,hello@bitwarden.com,fakepassword,TOTPSEED123
"Finance",note,My Note,"This is a secure note.",,0,,,
```

> [!TIP] Conditioning nested collections into a .csv
> If you're conditioning a `.csv` with nested collections, create dedicated entries for **each collection that does not have an an item in it**, for example:
> 
> 
> ```bash
> collections,type,name,notes,fields,reprompt,login_uri,login_username,login_password,login_totp
> Parent Collection,,,,,,,,,,
> Parent Collection/First Child Collection,,,,,,,,,,
> Parent Collection/First Child Collection/Second Child Collection,login,Shared Credential,,,,https://website.com,username,password,,
> ```

When importing this file, select **Bitwarden (csv)** as your file format.

### Minimum required values

You may not have data for all the values shown in the above formats, however most are optional. In order for the Bitwarden `.csv` importer to function properly, you are only required to have the following values for any given object:

```
folder,favorite,type,name,notes,fields,reprompt,login_uri,login_username,login_password,login_totp
,,login,Login Name,,,,,,
,,note,Secure Note Name,,,,,,
```

## Condition a .json

⬇️ [Download sample json](https://bitwarden.com/assets/2iwtn9YFqooYJmw1JWwCXa/8b03a95f1c27240c22a7578aa703f7b1/individual.json)

### .json for individual vault

Create a UTF-8 encoded plaintext file in the following format:

```
{
 "folders": [
 {
 "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
 "name": "Folder Name"
 },
 ],
 "items": [
 {
 "passwordHistory": [
 {
 "lastUsedDate": "YYYY-MM-00T00:00:00.000Z",
 "password": "passwordValue"
 }
 ],
 "id": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy",
 "organizationId": null,
 "folderId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
 "type": 1,
 "reprompt": 0,
 "name": "My Gmail Login",
 "notes": "This is my gmail login for import.",
 "favorite": false,
 "fields": [
 {
 "name": "custom-field-1",
 "value": "custom-field-value",
 "type": 0
 },
 ],
 "login": {
 "uris": [
 {
 "match": null,
 "uri": "https://mail.google.com"
 }
 ],
 "username": "myaccount@gmail.com",
 "password": "myaccountpassword",
 "totp": "otpauth://totp/my-secret-key"
 },
 "collectionIds": null
 },
 ]
}
```

When importing this file, select **Bitwarden (json)** as your file format.

### .json for organization

⬇️ [Download sample json](https://bitwarden.com/assets/2Pui1E5uLs2FSw6GhO6pdU/141c68c6ad63ea8f395067c02592ddbc/organization.json)

Create a UTF-8 encoded plaintext file in the following format:

```
{
 "collections": [
 {
 "id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
 "organizationId": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy",
 "name": "My Collection",
 "externalId": null
 },
 ],
 "items": [
 {
 "passwordHistory": [
 {
 "lastUsedDate": "YYYY-MM-00T00:00:00.000Z",
 "password": "passwordValue"
 }
 ],
 "id": "vvvvvvvv-vvvv-vvvv-vvvv-vvvvvvvvvvvv",
 "organizationId": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy",
 "folderId": "zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzz",
 "type": 1,
 "reprompt": 1,
 "name": "Our Shared Login",
 "notes": "A login for sharing",
 "favorite": false,
 "fields": [
 {
 "name": "custom-field-1",
 "value": "custom-field-value",
 "type": 0
 },
 ],
 "login": {
 "uris": [
 {
 "match": null,
 "uri": "https://mail.google.com"
 }
 ],
 "username": "myaccount@gmail.com",
 "password": "myaccountpassword",
 "totp": "otpauth://totp/my-secret-key"
 },
 "collectionIds": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
 },
 ]
}
```

When importing this file, select **Bitwarden (json)** as your file format.

### Import to existing collections

By conditioning your organization .`json` file appropriately, you can import new login items to pre-existing [collections](https://bitwarden.com/help/about-collections/). 

The following example demonstrates the proper format for importing a single item into a pre-existing collection. Note that you will need to:

- Obtain organization and collection IDs. These can be obtained by navigating to the collection in your web app and pulling them from the address bar (e.g. `https://vault.bitwarden.com/#/organizations/<organizationId>/vault?collectionId=<collectionId>`).
- Define a `"collections": []` array that contains data for the pre-existing collection, including organization and collection IDs (see above) as well as its name. As long as these 3 data points match, a new collection will not be created on import and instead items in the file will be imported to the pre-existing collection.

```
{
 "encrypted": false,
 "collections": [
 {
 "id": "b8e6df17-5143-495e-92b2-aff700f48ecd",
 "organizationId": "55d8fa8c-32bb-47d7-a789-af8710f5eb99",
 "name": "My Existing Collection",
 "externalId": null
 }
 ],
 "folders": [],
 "items": [
 {
 "id": "2f27f8f8-c980-47f4-829a-aff801415845",
 "organizationId": "55d8fa8c-32bb-47d7-a789-af8710f5eb99",
 "folderId": null,
 "type": 1,
 "reprompt": 0,
 "name": "Item to Import",
 "notes": "A login item for sharing.",
 "favorite": false,
 "login": {
 "uris": [
 {
 "match": null,
 "uri": "https://mail.google.com"
 }
 ],
 "username": "my_username",
 "password": "my_password",
 "totp": null
 },
 "collectionIds": ["b8e6df17-5143-495e-92b2-aff700f48ecd"]
 }
 ]
}
```

### Minimum required key-value pairs

You may not have data for all the key-value pairs shown in the above formats, however most are optional. In order for the Bitwarden `.json` importer to function properly, you are only required to have the following key-value pairs for each object:

```
{
 "items": [
 {
 "type": 1,
 "name": "Login Item's Name",
 "login": {} 
 },
 {
 "type": 2,
 "name": "Secure Note Item's Name",
 "secureNote": {} 
 },
 {
 "type": 3,
 "name": "Card Item's Name",
 "card": {} 
 },
 {
 "type": 4,
 "name": "Identity Item's Name",
 "identity": {} 
 }
 ]
}
```

The `"login":`, `"secureNote":`, `"card":`, and `"identity":` objects can be imported as empty objects, however we recommend conditioning files with as much data as you are able.

## Import into Bitwarden

Once your `.csv` or `.json` file is ready, import it to an [individual vault](https://bitwarden.com/help/import-data/#import-to-your-individual-vault/) or [organization vault](https://bitwarden.com/help/import-to-org/#import-to-an-organization-vault/). Select **Bitwarden (csv)** or **Bitwarden (json)** from the **File format** list.
