---
URL: https://bitwarden.com/help/delete-member-accounts/
---

# Delete Organization Member Accounts

> [!WARNING] Danger Zone
> Deleting an account is permanent and cannot be undone or restored. To create a backup of your vault data to store in a safe location, [export your vault data](https://bitwarden.com/help/export-your-data/).

Depending on your organization's setup, you may be able to delete member accounts. Deleting an account is different than removing a user.

## Delete an account

You may be able delete a member's account using one of the following methods:

- If you have a [claimed domain](https://bitwarden.com/help/claimed-domains/), any users with account email addresses that have a matching domain (e.g. `jdoe@mycompany.com`) can be outright deleted by organization administrators:

![Delete claimed accounts](https://bitwarden.com/assets/6HUnGTfMstF4IasZcKBfdi/0d2dbd328ba4a006611576e7d91c70df/2025-01-14_10-45-56.png)
- If you are self-hosting Bitwarden, an authorized administrator can delete the account from the [System Administrator Portal](https://bitwarden.com/help/system-administrator-portal/).
- If the account has an `@yourcompany.com` email address that your company controls, you can use [this procedure](https://bitwarden.com/help/delete-your-account/#tab-without-logging-in-4KcOdFa6zVp6H7xo9Ui9vc/) to initiate and confirm deletion within the `@yourcompany.com` inbox.

If none of these methods fit your organization's Bitwarden configuration, [remove the member](https://bitwarden.com/help/remove-users/) from your organization. They can then [delete their personal account](https://bitwarden.com/help/delete-your-account/#delete-a-personal-account/). 

## Remove an account

If you don't want to permanently delete account data, consider [removing the member](https://bitwarden.com/help/remove-users/) from the organization. **Removing a user does not delete their Bitwarden account.** Instead, they lose all access to the organization and its data. If they know their master password, they can still log in to the account and access any personally-owned items.
