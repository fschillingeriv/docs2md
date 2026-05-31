---
URL: https://bitwarden.com/help/account-recovery/
---

# About Account Recovery

> [!NOTE] Account recovery plan availability
> Account recovery is available for **Enterprise organizations** and is a more robust alternative to individually managed two-step login [recovery codes](https://bitwarden.com/help/two-step-recovery-code/).

Losing a master password,[ two-step login method](https://bitwarden.com/help/setup-two-step-login/), or [trusted device](https://bitwarden.com/help/about-trusted-devices/) can lock a member out of their vault. Account recovery gives administrators the ability to reset member credentials and restore their access. Once [account recovery is set up](https://bitwarden.com/help/account-recovery-enrollment/) and members are enrolled, there are two steps to regain access to the account:

1. An [administrator](https://bitwarden.com/help/account-recovery/#who-can-recover-accounts/) resets the member's master password, two-step login method, or both. Bitwarden then sends a recovery link to the member's account email.
2. With the [emailed recovery link](https://bitwarden.com/help/my-account-was-recovered/), the member can then reset their master password and/or set up a new two-step login method.

Account recovery only affects credentials configured within Bitwarden. It **does not bypass SSO** or any two-factor authentication configured with your IdP. If your organization [requires SSO authentication](https://bitwarden.com/help/policies/#require-single-sign-on-authentication/), members will still be required to use these methods to access their account after recovery.

> [!WARNING] Account recovery not related to deleted accounts
> Account recovery does not restore deleted accounts. [Deleting an account](https://bitwarden.com/help/delete-member-accounts/) is permanent and cannot be undone.

## Who can recover accounts

[Owners, admins, and permitted custom role members](https://bitwarden.com/help/user-types-access-control/) with the **Manage account recovery** permission can initiate account recovery. Who can reset whose master password or two-step login method depends on their role:

- Any owner, admin, or member with a custom role that includes **Manage account recovery** can recover a user's or custom role member's account.
- Only an admin or owner can recover an admin's account.
- Only an owner can recover another owner's account.

## How it works

When a member of the organization enrolls in account recovery, that user's [encryption key](https://bitwarden.com/help/account-encryption-key/) is encrypted with the organization's public key. The result is stored as the **Account Recovery Key**.

When an recovery action is taken:

1. The organization private key is decrypted with the organization symmetric key.
2. The user's **Account Recovery Key** is decrypted with the decrypted organization private key, resulting in the users's [encryption key](https://bitwarden.com/help/account-encryption-key/).
3. The user’s encryption key is encrypted with a new master key and a new master password hash is seeded from the new master password, both the master key-encrypted encryption key and master password has replace pre-existing server-side values
4. The user's encryption key is encrypted with the organization's public key, replacing the previous **Account Recovery Key** with a new one.

**At no point** will anyone, including the administrator who executes the reset, be able to see the old master password.

## Event logging

[Events](https://bitwarden.com/help/event-logs/) are logged when:

- A user enrolls in or withdraws from account recovery.
- An administrator initiates account recovery by resetting the master password or removing two-step login methods.
- A user updates their master password via account recovery.
- A user saves a new two-step login.

## Next steps

- Turn on the [Account recovery administration policy](https://bitwarden.com/help/policies/).
- Instruct users to [enroll in account recovery](https://bitwarden.com/help/account-recovery-enrollment/) if they joined before the policy was turned on or if you didn't turn on automatic enrollment.
- Learn how to [recover an account](https://bitwarden.com/help/recover-a-member-account/).
