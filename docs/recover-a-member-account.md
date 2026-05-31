---
URL: https://bitwarden.com/help/recover-a-member-account/
---

# Recover a Member Account

To [recover](https://bitwarden.com/help/account-recovery/) the account of a member who lost their master password, two-step login method, or trusted devices:

- You must be an [owner, admin, or permitted custom role](https://bitwarden.com/help/account-recovery/#who-can-recover-accounts/) member.
- Your organization must have the [Account recovery administration policy](https://bitwarden.com/help/policies/#account-recovery-administration/) turned on.
- The member whose account you want to recover must be [enrolled](https://bitwarden.com/help/account-recovery-enrollment/).

> [!TIP] See who is enrolled in account recovery
> You can view which members are enrolled in account recovery on the **Members** page. A 🔑 **Key icon** will be present in the **Policies** column.

To help your organization member regain access via account recovery:

1. In the Admin Console, go to **Members**.
2. (Optional) If the account is revoked, select **Revoked**.
3. For the member whose account you want to recover, select the ⋮ **Menu icon**on the same line as their account.
4. Select 🔑 **Recover account**:

![Recover account](https://bitwarden.com/assets/26oD8iqDY15SNJXCJlQE71/22e66b7e11a56d99c13ac41a1236c4e7/2024-12-03_15-35-51.png)
*Recover account*
5. In the **Recover account** window that appears, check which credential(s) you want to reset:

 - Check **Reset master password** to create a new temporary password, which must meet your organizations' requirements if the [Master password requirements policy](https://bitwarden.com/help/policies/#master-password-requirements/) is on. Copy the new master password and share it securely with the member, such as with [Bitwarden Send](https://bitwarden.com/help/create-send/).
 - Check **Reset two-step login** to remove two-factor authentication set up for Bitwarden (not your IdP). If the member hasn't set up any two-step login method, this option cannot be checked.

> [!NOTE] Account recovery, revoked if 2FA policy
> If the [Require two-step login policy](https://bitwarden.com/help/policies/#require-two-step-login/) is on, resetting a member's two-step login method will automatically [revoke](https://bitwarden.com/help/revoke-users/) them because they'll no longer be compliant. Ask them to notify you after they set up a new two-step login method to [restore access](https://bitwarden.com/help/revoke-users/#restore-access/).
6. Select **Save**. This will send an email to the member's account email with [next steps](https://bitwarden.com/help/my-account-was-recovered/) and log the user out of their current sessions. Active sessions on some client applications, like mobile apps, may remain active for up to one hour.
