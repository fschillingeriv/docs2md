---
URL: https://bitwarden.com/help/my-items/
---

# My Items

**My Items** is a location for organization members to store items that do not need to be shared with other users, while remaining under the ownership of the organization. My Items is available to members when the organization is using the [Centralize organization ownership](https://bitwarden.com/help/policies/#centralize-organization-ownership/) policy. 

Once the policy has been enabled by an owner or admin, **My Items** will be added to each organization member's vault and, depending on the organization’s policy settings, users may be prompted to [transfer items from My Vault to My Items](https://bitwarden.com/help/transfer-ownership/).

> [!WARNING] Phases of My Items
> At this time, Bitwarden recommends only organizations that have not started onboarding members to turn on the [Enforce organization data ownership policy](https://bitwarden.com/help/policies/#centralize-organization-ownership/). If your organization activated the policy before version [2025.11.0](https://bitwarden.com/help/releasenotes/), **My Items** will be created for members confirmed since that release. Preexisting members will not have **My Items** and can continue using their **My vault**.

**My Items** is each organization member's primary location for storing items, specifically those that don't need to be shared with other members:

- Items in **My Items** are owned by the organization. These items are not directly accessible by anyone except that member, but is subject to [event logging](https://bitwarden.com/help/event-logs/) and organization [health reports](https://bitwarden.com/help/reports/).
- Members can't share items in **My Items** with other member without first [assigning them to a collection](https://bitwarden.com/help/sharing/).
- Items shared with a member via a [collection](https://bitwarden.com/help/about-collections/) can't be moved or added to **My Items**.
- When the member account is [removed](https://bitwarden.com/help/remove-users/) or [deleted ](https://bitwarden.com/help/delete-member-accounts/) from the organization, items in **My Items** is transferred to organization administrators.

## Locating My Items

You can filter any Bitwarden app to list **My Items**, for example in the web app:

![My Items in the web app](https://bitwarden.com/assets/7f20Jamu35GDGYF4sOmsgn/5e525f384e09aef4b22c0c7f7cf993cb/2026-01-27_09-27-31.png)
*My Items in the web app*

Note in this screenshot that the **Owner** column indicates the item is owned by the Enterprise organization.

## Using My Items

### Save to My Items

For organization members that have access to it, **My Items** will be the default collection to save new items to:

![Save to My Items](https://bitwarden.com/assets/5Z9lis0vkv5MNSWWIy8XHW/f66a9a878e33a1dc4fc038c3d5bfd3ba/2026-01-27_09-30-50.png)
*Save to My Items*

### Import to My Items

For organization members that have access to it, **My Items** can be selected as the collection to [import data](https://bitwarden.com/help/import-data/) into:

![Import to My Items](https://bitwarden.com/assets/3PO3iAbypeTCIXsWCu2jQ2/a75eff626ca0bf19a12fca8b5cd50a1c/2026-01-27_09-38-30.png)
*Import to My Items*

Organization members may [import items](https://bitwarden.com/help/import-data/) into My Items on any Bitwarden client by selecting **My Items** from the **Collection** dropdown:

> [!NOTE] My items imports ignore folders
> When you import a file to **My items**, any folder references within that file will not carry over. You can organize your imported data into [folders](https://bitwarden.com/help/folders/) after the import is complete.

## After offboarding

When a member is [removed](https://bitwarden.com/help/remove-users/) or [deleted](https://bitwarden.com/help/delete-member-accounts/) from the organization, items in **My Items** is automatically transferred to organization administrators. From there, administrators can decide how to handle these items, for example transferring them to collections for use by other members or purging them from the organization. Learn more about [transferring items after employee offboarding and succession](https://bitwarden.com/help/remove-users/).
