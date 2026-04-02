---
URL: https://bitwarden.com/help/providers/
---

# Provider Portal Overview

> [!TIP] Provider Requirements
> Interested in becoming a Provider? To get started, we ask that:
> 
> - Your business has an active Enterprise organization.
> - Your business has a client ready to be onboarded under your Provider.
> 
> [Become a partner](https://bitwarden.com/partners/)

## What are Providers?

Providers are administration entities in Bitwarden that allow managed service providers (MSPs) to create and manage any number of [client organizations](https://bitwarden.com/help/providers/#client-organizations/) on behalf of individual business customers. Client organization management is easily accessible through the **Provider Portal**, available through the product switcher:

![Product switcher - Provider Portal](https://bitwarden.com/assets/4xn04Sj9u8n73TPxZUWi5f/dac0d56f47a05e2d8b28754e997a1391/2025-02-25_15-16-00.png)

### What is the Provider Portal?

The Provider Portal is an all-in-one management experience that enables providers to manage customers' Bitwarden organizations at scale. The Provider Portal streamlines administration tasks by centralizing a dedicated space to access and support each client, or to create a new one:

![Provider Portal](https://bitwarden.com/assets/7AoSHeZgJJTBXQmpZ13UBr/56ca464fe6987c8c5fc8e7099235d640/2025-02-25_15-17-46.png)

Providers are built with two distinct [user types](https://bitwarden.com/help/provider-users/#provider-user-types/):

- **Service users** can administer [client organizations](https://bitwarden.com/help/providers/#client-organizations/).
- **Provider admins** can administer [client organizations](https://bitwarden.com/help/providers/#client-organizations/) and administer the Provider itself, including adding new service users to the team.

## Client organizations

Client organizations are any [organization](https://bitwarden.com/help/about-organizations/) that is attached to or administered by a [Provider](https://bitwarden.com/help/providers/#what-are-providers/). To your customers, there's no difference between a "client" organization and a "regular" organization except for who is conducting administration. 

All Provider members have access to all client organizations, however members of a client organization cannot see or access information about the Provider's other client organizations:

![Structure of a Provider ](https://bitwarden.com/assets/28M8mkU03SyVFq70ZgD0Bp/04e3c65eba73892ae3301d366ce97ce1/provider-diagram.png)

> [!NOTE] Provider credentials
> **As denoted in the above diagram**, if Providers want to use an [organization](https://bitwarden.com/help/about-organizations/) to manage their own credentials, they **should not** include it as a client organization that is administered by the Provider.
> 
> Creating an independent organization for this case will ensure users can be given the appropriate [user types and access controls](https://bitwarden.com/help/user-types-access-control/) over credentials.

Organizations relate Bitwarden users and vault items together for [secure sharing](https://bitwarden.com/help/sharing/) of logins, cards, notes, and identities. Organizations have a unique view, the Admin Console, where Provider service users can manage the organization's collections, manage members and groups, run reporting, import data, and configure organization settings:

![Client organization vault ](https://bitwarden.com/assets/5fXREt9aHmnVgLLRPBs8yg/dbecd580231e8ea2f4eec2be224a1e64/2025-02-25_15-20-08.png)

Members of a client organization (such as your customer's end-users) will find shared items in their **Vaults** view alongside individually-owned items, as well as several methods for filtering the item list to only organization items or items in particular [collections](https://bitwarden.com/help/about-collections/):

![Organization-enabled vault](https://bitwarden.com/assets/4D2tlh9YKPzDY20SYGVKcG/dff56b66549d29405b1af211860f698e/2024-12-03_14-07-28.png)

Once you have [contacted us](https://bitwarden.com/contact/) and been setup with a Provider by a member of the Bitwarden team, [start a client organization](https://bitwarden.com/help/client-org-setup/).
