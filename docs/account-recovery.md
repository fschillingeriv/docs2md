---
URL: https://bitwarden.com/help/account-recovery/
---

# About Account Recovery

> [!NOTE] Account recovery plan availability
> Account recovery is available for **Enterprise organizations**.

Account recovery allows [owners, admins, and some custom role members](https://bitwarden.com/help/user-types-access-control/) to help organization members regain access when they forget their [master password](https://bitwarden.com/help/master-password/) or lose their [trusted devices](https://bitwarden.com/help/about-trusted-devices/). Account recovery:

- Can be activated for an organization by turning on the [Account recovery administration policy](https://bitwarden.com/help/policies/#account-recovery-administration/).
- Requires that members [enroll](https://bitwarden.com/help/account-recovery-enrollment/), using automatic enrollment or through self-enrollment, to be eligible for account recovery. Enrollment triggers the key exchange that makes account recovery secure.
- **Does not bypass members' two-step login or SSO**. If a [two-step login method](https://bitwarden.com/help/setup-two-step-login/) is enabled for the account or if the organization [requires SSO authentication](https://bitwarden.com/help/policies/#require-single-sign-on-authentication/), members will still be required to use these methods to access their account after recovery.

> [!WARNING] Account recovery not related to deleted accounts
> Account recovery does not restore deleted accounts. [Deleting an account](https://bitwarden.com/help/delete-member-accounts/) is permanent and cannot be undone.

## Who can recover accounts

Account recovery can be executed by [owners, admins, and permitted custom users](https://bitwarden.com/help/user-types-access-control/). Account recovery uses a hierarchical permission structure to determine who can reset whose master password, meaning:

- Any owner, admin, or member with a custom role that includes **Manage account recovery** can reset a user's or custom role member's master password.
- Only an admin or owner can reset an admin's master password.
- Only an owner can reset another owner's master password.

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

- A user's master password is reset using account recovery.
- A user updates a password issued through account recovery.
- A user enrolls in account recovery.
- A user withdraws from account recovery.

## Next steps

- Set up account recovery by turning on the [Account recovery administration policy](https://bitwarden.com/help/policies/) .
- Instruct users to [enroll in account recovery](https://bitwarden.com/help/account-recovery-enrollment/) if they joined before the policy was turned on or if you didn't turn on automatic enrollment.
- Learn how to [recover the account of an enrolled member](https://bitwarden.com/help/recover-a-member-account/).
- Provide members with [instructions on what to do when their account is recovered](https://bitwarden.com/help/my-account-was-recovered/).
