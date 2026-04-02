---
URL: https://bitwarden.com/help/import-to-org/
---

# Import to an Organization

Import data directly to your organization for easy migration to Bitwarden from any password management solution. Bitwarden supports many [import file formats](https://bitwarden.com/help/import-faqs/#q-what-file-formats-does-bitwarden-support-for-import/) and, if your's is not supported, you can manually create a [compatible .csv or .json file](https://bitwarden.com/help/condition-bitwarden-import/). There are two methods for importing data directly to your organization:

- Organization [owners, admins, and custom role users with the correct permission](https://bitwarden.com/help/user-types-access-control/) can import items with the organization Admin Console using the instructions in this article.
- Organization members with the [Manage collection permission](https://bitwarden.com/help/collection-permissions/) can import data directly to any collection for which they have that permission by following [this process](https://bitwarden.com/help/import-data/).

## Import to an organization vault

Data can only be imported to an organization using the web app. Data is [encrypted](https://bitwarden.com/help/what-encryption-is-used/) locally before being sent to the server for storage.

> [!NOTE] Items not imported
> While some item types cannot be imported, you can still add them to a vault:
> 
> - Upload [file attachments](https://bitwarden.com/help/attachments/) to the new vault individually.
> - Re-create [Sends](https://bitwarden.com/help/about-send/) in the new vault.

To import data to an organization:

1. Log in to the Bitwarden web app and open the Admin Console.
2. Go to **Settings** → **Import**:

![Import organization items](https://bitwarden.com/assets/12fA17Iq9LdCXdhPsPYQyq/0adc6c4b7164022c4c3623339e41a662/2025-12-17_11-04-54.png)
*Import organization items*
3. (Optional) To import to a specific collection, select it from the **Collection** dropdown menu. This can be helpful when importing data in batches for one segment of users at a time.
4. From the **File format** dropdown menu, select the [import file format](https://bitwarden.com/help/import-faqs/#q-what-file-formats-does-bitwarden-support-for-import/).

> [!NOTE] Encrypted imports
> If you're importing an [encrypted export](https://bitwarden.com/help/encrypted-export/), there isn't a separate option. Select `.json` and a handler will determine that the file is encrypted and attempt to decrypt the file using your [account's encryption key](https://bitwarden.com/help/account-encryption-key/) or encrypted export password.
5. Select **Choose file** and add the file to import, or copy/paste the contents of your file into the input box.

> [!WARNING] Duplicative Imports
> Importing does not check for duplicates. If you import the same file more than once or import items already in your vault, duplicate items will be created.
6. Select **Import** to trigger the import. If you are importing a password protected `.json `file, enter the password into the **Confirm Vault Import** window that appears.

## Troubleshoot import errors

If an "Import error" message appears, no data was added to your vault. [Fix the import file issue](https://bitwarden.com/help/import-data/#troubleshoot-import-errors/) and try again.

Some import errors are specific to organizations:

- **File contains unassigned items**: Ensure all [items are assigned to at least one collection](https://bitwarden.com/help/import-data/#file-contains-unassigned-items/) before trying to upload the file again.

> [!NOTE] File contains unassigned items error
> To minimize this error, turn on the [Restrict collection creation to owners and admins setting](https://bitwarden.com/help/collection-management/#collection-management-settings/) to prevent users from creating collections.
- **Organization can only have a maximum of two collections**: Free organizations support up to two collections. If your import file exceeds this limit, [reduce the number of collections](https://bitwarden.com/help/import-data/#organization-can-only-have-a-maximum-of-two-collections/) in the file or upgrade to import more.
