---
URL: https://bitwarden.com/help/import-from-keepass/
---

# Import from KeePass

When migrating from KeePass, you can choose which file type to import in to Bitwarden:

- Import an encrypted KeePass `.kdbx` file, secured with a password and an optional key file.
- Import a `.csv` or `.xml` file from KeePass2 or KeePassX.

> [!NOTE] Items not imported
> While some item types cannot be imported, you can still add them to a vault:
> 
> - Upload [file attachments](https://bitwarden.com/help/attachments/) to the new vault individually.
> - Re-create [Sends](https://bitwarden.com/help/about-send/) in the new vault.

## Export from KeePass

The steps to [export from KeePass](https://keepass.info/help/base/importexport.html) may differ based on your version. To export data from KeePassXC on macOS, for example:

- `.kdbx`: Go to **Database** → **Save Database As**. Enter a file name and select **Save**.
- `.csv` or `.xml`: Go to **Database** → **Export**. Select **Yes** to confirm the export, enter your password, and select **Unlock**.

## Import to Bitwarden

After exporting your KeePass data, follow the steps that match your file type.

### KDBX

This option may be preferred because it creates an encrypted file, which you can protect with a password or key file. You can use the Bitwarden web app, browser extension, desktop app, or CLI.

> [!NOTE] Import CLI, KeePass KDBX
> When using the [CLI to import](https://bitwarden.com/help/import-data/#tab-cli-5ALQx9afSqWXX9jfXsY5sb/) a `.kdbx` file, you will be prompted to enter your KeePass password and, if added to your KeePass database, its key file path.

To import a `.kdbx` file to your Bitwarden vault:

1. In the Bitwarden web app, browser extension, or desktop app, open the **Import** page:

 - Web app: Go to **Tools** → **Import**.
 - Browser extensions: Go to **Settings** → **Vault options** → **Import**.
 - Desktop apps: Select **Import** from the navigation.
2. From the **Vault** dropdown menu, select where to save the data:

 - To save data in your personal vault, select **My vault**. (Optional) Choose an existing [**Folder**](https://bitwarden.com/help/folders/) to organize the imported items.

> [!NOTE] KeePass groups become Bitwarden folders in My vault
> When you import KeePass data to My vault, any KeePass groups you may have set up will be migrated as Bitwarden [folders](https://bitwarden.com/help/folders/). If you also choose a **Folder** when importing the file, the imported folders will be nested inside the folder you selected.
 - To save data in an organization's vault, select the organization's name. (Optional) Choose a [Collection](https://bitwarden.com/help/create-collections/) to organize the imported items and share with other members. (You can only choose a collection where you have [**can manage**](https://bitwarden.com/help/about-collections/#collections-permissions/) permission.)

> [!NOTE] Import KeePass groups as collections, org-vault
> When you import KeePass data to an organization vault, any KeePass groups you may have set up will be migrated as Bitwarden [collections](https://bitwarden.com/help/about-collections/), nested within the collection you chose as a destination for the import.
3. From the **File format** dropdown menu, select **KeePass (kdbx)**.
4. Enter your **KeePass master password**.
5. If you added a key file within your KeePass database security settings:

 1. Select **Add key file**.
 2. Within **Key file upload**, select **Choose File** and pick your export's key file. The file name will end with `.keyx`.
6. Within **KDBX file upload**, select **Choose File** and pick your export's file. The file name will end with `.kdbx`.
7. Select **Import**.
8. After your data is imported, delete the exported data file from your computer. This will protect you in the event your computer is compromised. You may want to also delete your data from KeePass.

> [!NOTE] KeePass import, hidden field
> If your file contains any KeePass fields where the advanced setting **Protect value in process memory** was applied, it becomes a [hidden field](https://bitwarden.com/help/custom-fields/) in your Bitwarden vault.

### CSV or XML

If you exported your data as a `.csv` or `.xml` file, you can import that file using the Bitwarden web app, browser extension, desktop app, or [CLI](https://bitwarden.com/help/import-data/#tab-cli-5ALQx9afSqWXX9jfXsY5sb/). Data is [encrypted](https://bitwarden.com/help/what-encryption-is-used/) locally before being sent to the server for storage.

To import your KeePass data:

1. In the Bitwarden web app, browser extension, or desktop app, open the **Import** page:

 - Web app: Go to **Tools** → **Import**.
 - Browser extensions: Go to **Settings** → **Vault options** → **Import**.
 - Desktop apps: Select **Import** from the navigation.
2. From the **Vault** dropdown menu, select where to save the data:

 - To save data in your personal vault, select **My vault**. (Optional) Choose an existing [**Folder**](https://bitwarden.com/help/folders/) to organize the imported items.

> [!NOTE] KeePass groups become Bitwarden folders in My vault
> When you import KeePass data to My vault, any KeePass groups you may have set up will be migrated as Bitwarden [folders](https://bitwarden.com/help/folders/). If you also choose a **Folder** when importing the file, the imported folders will be nested inside the folder you selected.
 - To save data in an organization's vault, select the organization's name. (Optional) Choose a [Collection](https://bitwarden.com/help/create-collections/) to organize the imported items and share with other members. (You can only choose a collection where you have [**can manage**](https://bitwarden.com/help/about-collections/#collections-permissions/) permission.)

> [!NOTE] Import KeePass groups as collections, org-vault
> When you import KeePass data to an organization vault, any KeePass groups you may have set up will be migrated as Bitwarden [collections](https://bitwarden.com/help/about-collections/), nested within the collection you chose as a destination for the import.
3. From the **File format** dropdown menu, select **KeePass (csv)** or **KeePass (xml)**.
4. Select **Choose File** and pick the exported file from your computer.
5. Select **Import**.
6. After your data is imported, delete the exported data file from your computer. This will protect you in the event your computer is compromised. You may want to also delete your data from KeePass.

> [!NOTE] KeePass import, hidden field
> If your file contains any KeePass fields where the advanced setting **Protect value in process memory** was applied, it becomes a [hidden field](https://bitwarden.com/help/custom-fields/) in your Bitwarden vault.

If an “Import error” message appears, no data was added to your vault. [Fix the import file issue](https://bitwarden.com/help/import-data/#troubleshoot-import-errors/) and try again.
