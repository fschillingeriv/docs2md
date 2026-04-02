---
URL: https://bitwarden.com/help/revoke-users/
---

# Temporarily Revoke Access

Organization [admins and some custom role members](https://bitwarden.com/help/user-types-access-control/) can manage members' access to the organization on a temporary basis through revoking and restoring. Revoking access is:

- Often useful when a member shouldn't have access for a period of time, but will need to have access restored in the future.
- **Automatically** done when users are in violation of some [enterprise policies](https://bitwarden.com/help/policies/).
- **Automatically**done for organizations [using SCIM](https://bitwarden.com/help/about-scim/) when a member is suspended or de-activated in the IdP.

Restoring access to a revoked member does not require that they take any steps to rejoin the organization, meaning they won't need to [be re-invited, accept an invite, or be confirmed](https://bitwarden.com/help/managing-users/#onboard-users/).

## Revoke access

> [!NOTE] Revoke/Restore Owners.
> Only **owners**can revoke and restore access to other **owners**.

To revoke organization access to a member:

1. In the Admin Console, navigate to the **Members** view.
2. Select the members you want to revoke access for and use the ⋮ Options menu to **Revoke access**:

![Revoke access](https://bitwarden.com/assets/6hBUggWWvdttF0RUqU8IZ9/389eb47b90742bb3e3844f5105bc643a/2024-12-03_15-06-01.png)

### Restrictions on revoked members

Members with revoked access are listed in the **Revoked**tab and will:

- Not have access to any organization vault items or collections.
- Not be able to log in to the account using your organization's [SSO](https://bitwarden.com/help/about-sso/).
- Not be subject to your organization's [policies](https://bitwarden.com/help/policies/).
- Not occupy a license seat.

## Restore access

> [!NOTE] Can't restore until policy compliance
> Members who are not compliant with some [policies](https://bitwarden.com/help/policies/) will not be able to have their access restored until they take steps to become compliant.

To restore access to a member:

1. In the Admin Console, navigate to the **Members** view.
2. Open the **Revoked**tab.
3. Select the members you want to restore access for and use the ⋮ Options menu to **Restore access**:

![Restore access](https://bitwarden.com/assets/2xe3Vt7l9CCO85RhhmoVJU/47321af7571e298c697a412c650403d6/2024-12-03_15-11-35.png)
