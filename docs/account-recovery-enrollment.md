---
URL: https://bitwarden.com/help/account-recovery-enrollment/
---

# Account Recovery Enrollment

In order for members to be eligible for [account recovery](https://bitwarden.com/help/account-recovery/), they must be enrolled in the program. Enrollment triggers the key exchange that makes account recovery secure. There are two ways for members to be enrolled:

- **Automatic enrollment**: When you turn on the [Account recovery administration policy](https://bitwarden.com/help/policies/#account-recovery-administration/), you can also turn on the option **Require new members to be enrolled automatically**. This option will enroll new members in account recovery automatically.
- **Self-enrollment**: Organization members can follow a quick process to enroll themselves in account recovery. 

> [!TIP] When self-enrollment is necessary
> Bitwarden recommends turning on automatic enrollment, however members that are already part of your organization **prior to account recovery being turned on** will be required to self-enroll.

## Automatic enrollment

Turning on the option to **Require new members to be enrolled automatically** will:

- Enroll new members in account recovery automatically when they [enter an accepted status](https://bitwarden.com/help/managing-users/#accept/).
- Prevent them from withdrawing from account recovery.

> [!NOTE] Notify users of admin password reset.
> If you automatically enroll members in account recovery, we recommend notifying them of this feature. Some organization members can choose to store personal credentials under their own ownership and should be made aware that account recovery could allow an administrator to access their personal items.

## Self-enrollment

Members that are already part of your organization **prior to account recovery being turned on** if you're using automatic enrollment, or all users if you're not using automatic enrollment, will be required to self-enroll.

To enroll in account recovery, select the ⋮ **Options**menu next to the organization in the Vaults view and select **Enroll in account recovery**:

![Enroll in account recovery](https://bitwarden.com/assets/4ape19S5L7lf0tAAEyInGR/87fadad707f8c7acb5894e94e758c6c3/2024-12-03_15-33-13.png)

### Withdraw enrollment

Members of organizations that have turned on the automatic enrollment option **will not be allowed to withdraw** from account recovery, however members of organizations that have not turned it on can **Withdraw** from the same dropdown used to enroll:

![Withdraw from account recovery](https://bitwarden.com/assets/4GR176lad9pre4sZN3rA35/642bdef55248fb84ddb24fc316875b11/2024-12-03_15-34-30.png)

Manually changing your master password or [rotating an encryption key](https://bitwarden.com/help/account-encryption-key/) **will not** withdraw a member from account recovery.
