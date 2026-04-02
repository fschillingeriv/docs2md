---
URL: https://bitwarden.com/help/recover-a-member-account/
---

# Recover a Member Account

To recover the account of a member who has forgotten their master password or lost their trusted devices:

- You must be an [owner, admin, or permitted custom role](https://bitwarden.com/help/user-types-access-control/) member.
- Your organization must have the [Account recovery administration policy](https://bitwarden.com/help/policies/#account-recovery-administration/) turned on.
- The member whose account you want to recover must [be enrolled](https://bitwarden.com/help/account-recovery-enrollment/).

> [!TIP] Seeing who is enrolled
> A member that is enrolled in account recovery will have a key icon ( 🔑 ) displayed in the **Policies** column.

Complete the following steps to recover an organization member's account:

1. In the Admin Console, navigate to the **Members** view.
2. For the member whose account you want to recover, use the ⋮ Options menu to select 🔑 **Recover account**:

![Recover account](https://bitwarden.com/assets/26oD8iqDY15SNJXCJlQE71/22e66b7e11a56d99c13ac41a1236c4e7/2024-12-03_15-35-51.png)
3. In the Recover account window, create a **New password** for the user. If your organization has enabled the [master password requirements policy](https://bitwarden.com/help/policies/#master-password-requirements/), you will need to create a password that meets the implemented requirements (for example, min. eight characters or contains numbers):

![Create new password](https://bitwarden.com/assets/28qKke9XJLj6nTZJjg4mK4/7b1c2c5cb2c139bf08ea4c5f65c9a02a/2024-12-03_15-38-52.png)
4. Copy the new master password and contact the member to coordinate secure communication of it, for example by using [Bitwarden Send](https://bitwarden.com/help/create-send/).
5. Select **Save** to proceed with account recovery. Doing so will log the user out of their current sessions. Active sessions on some client applications, like mobile apps, may remain active for up to one hour.
