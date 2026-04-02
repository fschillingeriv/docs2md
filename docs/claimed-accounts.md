---
URL: https://bitwarden.com/help/claimed-accounts/
---

# Claimed Accounts

When an Enterprise organization [claims a domain](https://bitwarden.com/help/claimed-domains/), onboarded organization member accounts that use an email address with a matching domain (e.g. `jdoe@mycompany.com`) will be claimed be the organization. Claimed accounts are functionally **owned by the organization**, resulting in a few key changes to the way the account works.

> [!NOTE] Clarifying claimed member prereqs
> A user must have a matching domain **and** be a [confirmed member](https://bitwarden.com/help/managing-users/#confirm/) of your Bitwarden organization to be considered a claimed account. Claiming a domain **does not** automatically invite any users and therefore will not in and of itself add to your subscription seat count.

## Deletion of claimed accounts

Claimed member accounts can be outright deleted by organization administrators, instead of only being able to be removed from the organization. This includes deleting that user's individual vault, if one is available to them. If you are an organization member with a claimed account, it is especially important that you are not storing any personal credentials in that account. 

> [!NOTE] Learn how to delete claimed accounts
> Claimed accounts can be deleted from the Admin Console's **Members** page using the ⋮ options menu:
> 
> ![Delete claimed accounts](https://bitwarden.com/assets/6HUnGTfMstF4IasZcKBfdi/0d2dbd328ba4a006611576e7d91c70df/2025-01-14_10-45-56.png)
> 
> Members of your organization that do not have claimed accounts can only be **Removed** from the organization instead.

## Restricted access to account actions

If you are an organization member with a claimed account, you are not able to:

- Change your account email address to a domain that is not claimed by your organization. (You can still change the username portion of your email address.)
- Leave the organization.
- Purge your vault.
- Delete your account.
