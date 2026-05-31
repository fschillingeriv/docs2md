---
URL: https://bitwarden.com/help/account-recovery-enrollment/
---

# Set Up Account Recovery

[Account recovery](https://bitwarden.com/help/account-recovery/) helps organization members regain access to their account. After the Enterprise policy is activated, members need to enroll in the program. Enrollment triggers the key exchange that makes account recovery secure. There are two ways for members to be enrolled:

- [Automatic enrollment](https://bitwarden.com/help/account-recovery-enrollment/#automatic-enrollment/) is the quickest option, but only applies to members who join after the policy is turned on.
- [Self-enrollment](https://bitwarden.com/help/account-recovery-enrollment/#self-enrollment/) allows members to manually enroll through the web app.

## Turn on Enterprise policy

First, turn on the [Account recovery administration](https://bitwarden.com/help/policies/#account-recovery-administration/) policy. After it's activated, members must enroll in account recovery.

## Automatic enrollment

When you turn on the **Account recovery administration** policy, you have the option to check **Automatically enroll new members in account recovery**. Turning on this setting will:

- Enroll new members in account recovery automatically when they [enter an accepted status](https://bitwarden.com/help/managing-users/#accept/).
- Prevent them from withdrawing from account recovery.

> [!WARNING] Existing members need to self-enroll account recovery
> Bitwarden recommends turning on automatic enrollment. However, automatic enrollment only applies to members who join **after** the policy was activated. If your organization already had members **before the policy was turned on**, those members must self-enroll to be eligible.

If you automatically enroll members in account recovery, we recommend notifying them. Some organization members can choose to store personal credentials under their own ownership and should be made aware that account recovery could allow an administrator to access their personal items.

## Self-enrollment

Members must opt in proactively if [automatic enrollment](https://bitwarden.com/help/account-recovery-enrollment/#automatic-enrollment/) is off or if they joined before it was turned on. To enroll in account recovery:

1. From the web app, select the ⋮ **Options icon** next to the organization in the Vaults view.
2. Select **Enroll in account recovery**:

![Enroll in account recovery](https://bitwarden.com/assets/4ape19S5L7lf0tAAEyInGR/87fadad707f8c7acb5894e94e758c6c3/2024-12-03_15-33-13.png)
*Enroll in account recovery*
3. Enter your **Master password**.
4. Select **Submit**.
5. Select **Trust**.

### Withdraw enrollment

Members of organizations that turned on the automatic enrollment policy **are not allowed to withdraw** from account recovery. Members of organizations that have not turned it on, however, can select **Withdraw** from the same menu used to enroll:

![Withdraw from account recovery](https://bitwarden.com/assets/4GR176lad9pre4sZN3rA35/642bdef55248fb84ddb24fc316875b11/2024-12-03_15-34-30.png)
*Withdraw from account recovery*

Manually changing your master password or [rotating an encryption key](https://bitwarden.com/help/account-encryption-key/) **will not** withdraw a member from account recovery.
