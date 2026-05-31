---
URL: https://bitwarden.com/help/revoke-users/
---

# Temporarily Revoke Access

Revoking a member is how you temporarily remove someone from your organization. You can later [restore their access](https://bitwarden.com/help/revoke-users/#restore-access/) or [permanently remove](https://bitwarden.com/help/remove-users/) them from your organization. When a member is revoked, they:

- Cannot access any organization vault items or collections.
- Cannot log in with your organization's [SSO](https://bitwarden.com/help/about-sso/).

> [!NOTE] Revoked users without master passwords
> Members who **do not have master passwords**, for example in organizations using [trusted devices](https://bitwarden.com/help/about-trusted-devices/) or [Key Connector](https://bitwarden.com/help/about-key-connector/), will be fully locked out of their account if they are revoked.
- Are not subject to your organization's [policies](https://bitwarden.com/help/policies/).
- Do not occupy a [subscription seat](https://bitwarden.com/help/manage-subscription-seats-in-your-organization/).

## Revoke access

There are a few ways to revoke a member. Members are **automatically** revoked when they violate certain [enterprise policies](https://bitwarden.com/help/policies/) or the member is suspended or deactivated in the IdP used for their organization's [SCIM](https://bitwarden.com/help/about-scim/).

Alternatively, an [owner, admin, or custom role member](https://bitwarden.com/help/user-types-access-control/) with **Manage users** permission can **manually** revoke users:

1. In the Admin Console, select **Members**.
2. Check the member(s) you want to revoke.
3. Select the ⋮ **Options menu**.
4. Select **Revoke access**:

![Revoke access](https://bitwarden.com/assets/6hBUggWWvdttF0RUqU8IZ9/389eb47b90742bb3e3844f5105bc643a/2024-12-03_15-06-01.png)
*Revoke access*
5. Select **Revoke members** to confirm.

> [!TIP] View revoked members
> To view which members are revoked, go to **Members** → **Revoked**. Hover over the ℹ️ **Revoked** **icon** next to a specific user to learn why they were revoked:
> 
> 
> ![Revoke reason tooltip](https://bitwarden.com/assets/4K6UcJtGBxlmEyY0ASKBBs/f4ed8fec1ad67da90dd0f980ef2744a6/Revoke_reason_tooltip.png)
> *Revoke reason tooltip*
> 
> If it says "Unknown reason," then the member was revoked before [release 2026.5.0](https://bitwarden.com/help/releasenotes/#2026-5-0/).

## Restore access

An [owner, admin, or custom role member](https://bitwarden.com/help/user-types-access-control/) with **Manage users** permission can restore members' access quickly. Restoring access to a revoked member does not require that they take any steps to rejoin the organization, meaning they don't need to be [re-invited, accept an invite, or be confirmed](https://bitwarden.com/help/managing-users/#add-new-members/).

> [!NOTE] Can't restore until policy compliance
> Members who are not compliant with some [enterprise policies](https://bitwarden.com/help/policies/) cannot be restored to your organization until they take steps to become compliant with those policies.

To restore access to a member:

1. In the Admin Console, select **Members**.
2. Select **Revoked**.
3. Check the member(s) you want to return to the organization.
4. Select the ⋮ **Options menu**.
5. Select **Restore access**:

![Restore access](https://bitwarden.com/assets/2xe3Vt7l9CCO85RhhmoVJU/47321af7571e298c697a412c650403d6/2024-12-03_15-11-35.png)
*Restore access*
6. Select **Revoke members** to confirm.
