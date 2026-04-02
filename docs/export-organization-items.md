---
URL: https://bitwarden.com/help/export-organization-items/
---

# Export Organization Items

For organizations, exporting data and storing it in a secure location is a great way of ensuring access to a backup. Organizations can export data from the web app and CLI. Vault data is decrypted locally by the client before export, meaning no unencrypted data is transported over the internet when you create an export. There are two ways to export organization data:

- Organization members with the [Manage collection permission](https://bitwarden.com/help/collection-permissions/) can export item data from collections for which they have that permission by following [this process](https://bitwarden.com/help/export-your-data/).
- Organization [admins, owners, and custom users with the correct permissions](https://bitwarden.com/help/user-types-access-control/) can export all organization item data by using this instructions in this article.
- Organizations that have enabled the [Centralize organization ownership policy](https://bitwarden.com/help/policies/#centralize-organization-ownership/) cannot export organization members' [My Items](https://bitwarden.com/help/my-items/) while the user is active in the organization.

Exports can be made in a few different formats, however Bitwarden recommends using an [encrypted .json option](https://bitwarden.com/help/encrypted-export/) for best security and a more complete export, as `.csv` files won't currently export cards or identities, and only `.json` exports include [stored passkeys](https://bitwarden.com/help/storing-passkeys/) and [SSH keys](https://bitwarden.com/help/ssh-agent/). For a complete list of all the items and fields included in an organizations vault export, see this ⬇️ [JSON sample](https://bitwarden.com/assets/2oQPd5ZsY1N0hph4N6pBrY/b5fc7c05ac238d71d9a1902a58559cc6/Organization_vault_export.json).

### Web app

To export your organization data from the web app:

1. Open the **Admin Console** using the product switcher.
2. Select **Settings** → **Export** from the navigation:

![Export organization items](https://bitwarden.com/assets/2UQyeVwsMcc1f7vcJOnnUO/92b2bb7eee6bcf9e183f9b039aec5d33/2025-12-17_11-08-49.png)
*Export organization items*
3. On the vault export page, choose a **File format** (`.json`, `.csv`, or `.json (Encrypted)`) and select the **Confirm format**button.

> [!WARNING] Careful w/ Exports
> Unless you are using an [encrypted export](https://bitwarden.com/help/encrypted-export/), do not store or send the exported file over insecure channels, like email, and delete the file immediately after use.
4. Enter your master password and select the **Export** button.

> [!NOTE] Exported Org data event
> Exporting an organization's vault data will be captured by event logs. [Learn more](https://bitwarden.com/help/event-logs/).

### CLI

> [!TIP] Sync before export on CLI
> Sync your vault with `bw sync` before exporting to ensure the most up-to-date information is included.

To export your organization data from the CLI, use the `export` command with the `--organizationid` option. By default, `export` will export your vault as a `.csv` and save the file to the working directory, however this behavior can be altered using options:

```
bw export my-master-password --organizationid 7063feab-4b10-472e-b64c-785e2b870b92 --output /users/me/documents/ --format json --session my-session-key
```

> [!TIP] Getting organizationid with bw list
> If you don't know your `organizationid` value off-hand, you can access it at the command-line using `bw list organizations`.

For more detail, see our [CLI documentation](https://bitwarden.com/help/cli/).

> [!NOTE] Exported Org data event
> Exporting an organization's vault data will be captured by event logs. [Learn more](https://bitwarden.com/help/event-logs/).
