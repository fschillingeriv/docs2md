---
URL: https://bitwarden.com/help/claimed-domains/
---

# Claimed Domains

Enterprise customers can claim domain (eg. `mycompany.com`) ownership for their organizations with a valid and unique-to-Bitwarden DNS TXT record. When you claim a domain, your organization gains additional controls over accounts with matching email addresses:

- **Policy to block undesired account creation**: [Turn on a policy](https://bitwarden.com/help/policies/#block-account-creation-for-claimed-domains/) to prevent email accounts with matching domains (e.g. `jdoe@mycompany.com`) from creating Bitwarden accounts outside the organization. When the policy on, email accounts with matching domains can only be used to create Bitwarden accounts by being invited to join the organization.
- **Claimed member accounts**: Onboarded organization member accounts that use an email address with a matching domain (e.g. `jdoe@mycompany.com`) will automatically be [claimed by your organization](https://bitwarden.com/help/claimed-accounts/), restricting users from taking some account actions and allowing administrators to [delete the accounts](https://bitwarden.com/help/delete-member-accounts/) outright instead of only being able to remove them from the organization.

Onboarded organization member accounts that use an email address with a matching domain (e.g. `jdoe@mycompany.com`), referred to as [claimed accounts](https://bitwarden.com/help/claimed-accounts/), also gain the following benefits:

- **Easier SSO workflow**: During SSO authentication, these members will automatically bypass the step that would require them to enter an [SSO identifier](https://bitwarden.com/help/using-sso/#get-your-organization-identifier/).
- **Automatically verified emails**: These members will have their [email automatically verified](https://bitwarden.com/help/product-faqs/#q-what-features-are-unlocked-when-i-verify-my-email/) when onboarded.

## Claim a domain

In order to claim a domain, Bitwarden must verify that:

- No other organization has verified the domain.
- Your organization has ownership of the domain.

Bitwarden will use a DNS TXT record to validate a domain claim. This DNS TXT record must be kept active and available at all times, as Bitwarden will continually check for it.

To claim a domain, complete the following steps as an [admin or owner](https://bitwarden.com/help/user-types-access-control/#member-roles/): 

1. Log in to the Bitwarden [web app](https://bitwarden.com/help/getting-started-webvault/) and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
2. Navigate to **Settings** → **Claimed domains**:

![Claiming a domain](https://bitwarden.com/assets/6WJAs5AXufz8zSiVjEp5aA/8d9f4576f877ce74d6553430801070a9/2025-01-14_09-56-53.png)
3. On the **Claimed domains**screen you will see a list of active domains, along with status checks and options. If you have no active domains, select **New domain**.

> [!TIP] Claimed a domain for the first time
> When you claim a domain, the [single organization policy](https://bitwarden.com/help/policies/#single-organization/) will automatically be activated during the claiming workflow. Domains that were claimed prior to the 2025.3.0 release will not automatically activate this policy, however any subsequent domains claimed by the organization will.
4. In the pop-up window, enter a **Domain name**.

> [!NOTE] domain format
> The format of the domain name entry **should not** include `https://` or `www.`.
5. Copy the **DNS TXT record** and add it to your domain.
6. Select **Claim domain**.

### Manage your domains

You can manage and view the status of your domains from the **Claimed domains** page. All domains will have a status of **Claimed** or **Not Claimed**:

![Claimed domain](https://bitwarden.com/assets/1sgIhVJzsRce0VyNIvH1ze/9ebaf423a88815e476bf2d81231fbf8e/2025-04-15_09-52-34.png)

> [!TIP] If you need to edit your domain.
> Before updating your claimed domain in Bitwarden, verify that your TXT record is publicly visible using the `dig` command:
> 
> 
> ```bash
> dig your.domain.com TXT
> ```
> 
> **If the wrong TXT record is found**, your DNS changes may need more time to propagate. **If the right TXT record is found but claiming still fails**, your Bitwarden server may be configured to use a internal DNS server than the public one in which the update was made.

Use the ⋮ menu located on the right side of the domain to:

- Edit or delete a domain.
- **Copy DNS TXT record**to provide it to your DNS provider.
- Manually **verify domain** if automatic claiming was not successful.

> [!NOTE] Domain verification attempts 
> Bitwarden will attempt to verify the domain 3 times during the first 72 hours. If the domain has not been verified within 7 days after the 3rd attempt, the domain will be removed from your organization.

Domain claiming activities will be logged in the organization event logs. To view events, navigate to **Reporting** → **Event logs** in the Admin Console.

## Once your domain is claimed

Once your domain is claimed and verified, your organization will gain access to the following:

### Block account creation for claimed domains

Turn on [this policy](https://bitwarden.com/help/policies/#block-account-creation-for-claimed-domains/) to prevent email accounts with matching domains (e.g. `jdoe@mycompany.com`) from creating Bitwarden accounts outside the organization. When the policy on, email accounts with matching domains can only be used to create Bitwarden accounts by being invited to join the organization.

### Claimed member accounts

Onboarded organization member accounts that use an email address with a matching domain (e.g. `jdoe@mycompany.com`) will automatically be [claimed by your organization](https://bitwarden.com/help/claimed-accounts/), resulting in a few key changes to the way the account works:

> [!NOTE] Clarifying claimed member prereqs
> A user must have a matching domain **and** be a [confirmed member](https://bitwarden.com/help/managing-users/#confirm/) of your Bitwarden organization to be considered a claimed account. Claiming a domain **does not** automatically invite any users and therefore will not in and of itself add to your subscription seat count.

#### Org-managed account deletion

Claimed member accounts can be outright deleted by organization administrators, instead of only being able to be removed from the organization. Owners and admins can delete a claimed account from the Admin Console's **Members** page using the ⋮ menu:

![Delete claimed accounts](https://bitwarden.com/assets/6HUnGTfMstF4IasZcKBfdi/0d2dbd328ba4a006611576e7d91c70df/2025-01-14_10-45-56.png)

Members of your organization that do not have claimed accounts can be **Removed** from the organization instead.

> [!NOTE] Claimed accounts with Directory Connector and SCIM
> Directory Connector and SCIM do not have the ability to delete claimed accounts, this action can only be taken by admins and owners from the web app Admin Console.

#### Restricted access to account actions

 Users with member accounts will be restricted from:

- Changing their account email address to a different domain (members can still change the username portion of their email address).
- Leaving the organization.
- Purging their vault.
- Deleting their account.
