---
URL: https://bitwarden.com/help/remove-users/
---

# Permanently Remove Access

Organization [admins, owners, and some custom role members](https://bitwarden.com/help/user-types-access-control/) can remove members from an organization. Removing a member:

- **Eliminates** their access to the organization and its data. Removed members need to [re-join the organization](https://bitwarden.com/help/managing-users/#onboard-users/) to re-gain access.
- **Does not delete** their Bitwarden account in most cases. Removed members are still able to access their personally-owned vault items unless you [delete their account](https://bitwarden.com/help/delete-member-accounts/).
- Is **automatically** done for organizations using [directory sync](https://bitwarden.com/help/directory-sync/) if the **Remove disabled users during sync option** is turned on.

## Remove members from an organization

To remove members from your organization:

1. In the Admin Console, go to **Members**.
2. Select the users you want to remove and select the ⋮ **Options icon**.
3. Select **Remove**:

![Remove members ](https://bitwarden.com/assets/5hTYQXah4C90KJcZnWwnqs/83372c5f7e37a9ea27cb14cc78b3b93e/2024-12-03_15-06-01.png)
4. Select **Remove members** to confirm.

> [!TIP] Remove is Delete, if you're a Claimed Domain
> If your organization has a [claimed domain](https://bitwarden.com/help/claimed-domains/) and the user's account email address matches your claimed domain, **Remove** is not listed. Instead, you can select **Delete** to [delete the account permanently](https://bitwarden.com/help/delete-member-accounts/), effectively removing the user’s access to the organization:
> 
> ![Delete claimed accounts](https://bitwarden.com/assets/6HUnGTfMstF4IasZcKBfdi/0d2dbd328ba4a006611576e7d91c70df/2025-01-14_10-45-56.png)

Offline devices cache a read-only copy of data, including organization items. Some clients may retain access to this read-only data for a short time after a member is removed. If you anticipate malicious exploitation of this, update credentials the member had access to when you remove them from the organization.

> [!WARNING] Accounts without MPs & TDE
> For member accounts that do not have master passwords as a result of [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/):
> 
> - [Removing them from your organization](https://bitwarden.com/help/remove-users/#remove-members-from-an-organization/) eliminates all access to their Bitwarden account unless they were previously assigned a master password using [account recovery](https://bitwarden.com/help/account-recovery/) and they log in with that master password at least once before being removed.
> 
> These users will not be able to re-join your organization unless the above steps are taken **before** they are removed from the organization. If they aren't, each removed user will be required to [delete their account](https://bitwarden.com/help/delete-your-account/#delete-an-individual-account/) and be issued a new invitation to create an account and join your organization.
> - [Revoking access to the organization](https://bitwarden.com/help/revoke-users/), but not removing them from the organization, will still allow them to log in to Bitwarden and access **only** their individual vault.

## What happens to removed members' data

Organizations own all [collections](https://bitwarden.com/help/about-collections/). When you remove the only member with full [Manage collection permission](https://bitwarden.com/help/collection-permissions/) to a collection, owners and admins can grant a current member [access to the collection](https://bitwarden.com/help/assign-users-to-collections/#assign-access-to-un-managed-collections/).

Items saved in My vault are owned by the individual user. When a member is removed from an organization, the user keeps all items in their My vault.

In contrast, organizations using the [Centralize organization ownership](https://bitwarden.com/help/policies/#centralize-organization-ownership/) policy retain access to data when members are removed. This policy replaces the individually-owned My vault with the organization-owned [My Items](https://bitwarden.com/help/my-items/). When a member with data in My Items is removed, their My Items automatically converts into a collection named with the user's email address. Owners and admins can then [assign access to the collection](https://bitwarden.com/help/assign-users-to-collections/#assign-access-to-un-managed-collections/). After a current member is granted [Manage collection permission](https://bitwarden.com/help/collection-permissions/), they can access, edit, and reassign items the same way as a standard Bitwarden collection.
