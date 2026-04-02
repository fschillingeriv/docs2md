---
URL: https://bitwarden.com/help/master-password/
---

# My Master Password

Your master password is the primary method for accessing Bitwarden. It's important that your master password is:

- **Memorable**: Bitwarden employees and systems have **no** knowledge of, way to retrieve, or way to reset your master password. **Do not forget your master password!**
- **Strong**: A longer, more complex, and less common password is the best way to protect your account. Bitwarden provides a free [**password strength testing tool**](https://bitwarden.com/password-strength/) to test the strength of some memorable passwords you are considering. 

Master passwords made after the [2023.3.0 release](https://bitwarden.com/help/releasenotes/) must be at least 12 characters.

> [!TIP] Tips to mitigate forgetting master password.
> Worried about forgetting your master password? Here is what to do:
> 
> - **Set up a hint**. In case you need a reminder, a master password hint email can be requested on the login screen. Make sure you use a hint that only you will understand.
> - **Designate a**[**trusted emergency contact**](https://bitwarden.com/help/emergency-access/). Users with premium access can grant account access to a friend or family member in the case of emergency.

## Change master password

If you know your current master password, you can change it from the web vault:

> [!TIP] If you don't know your master password.
> If you do not know your current master password, [learn what to do](https://bitwarden.com/help/forgot-master-password/).

1. In the web app, select the **Settings** → **Security** from the navigation:
2. Select the **Master password** tab:

![Master password settings](https://bitwarden.com/assets/2Svv0PwlH9i7SSK73dlv9A/e451afb190346e492110a7bf1bd3a518/Master_password_settings.png)
*Master password settings*
3. Enter your **Current master password**.
4. Enter and confirm your **New master password**.
5. If you want to check your master password through HIBP before submitting it, check the **Check known data breaches for the password** ([learn more](https://bitwarden.com/help/reports/#data-breach-individual-vaults-only/)) box. To run this report, a hash of your master password is sent to HIBP and compared to stored exposed hashes. Your master password itself is never exposed by Bitwarden.

> [!WARNING] Rotate account encryption key.
> Don't check the **rotate account's encryption key** box unless you fully understand the ramifications and required follow-up actions. [Learn more](https://bitwarden.com/help/account-encryption-key/).
6. Select the **Change master password** button.

Changing your master password will automatically log you out of the web vault session. Other logged-in apps may remain active for up to an hour, but will eventually also require you to log back in with your new master password.

## I forgot my master password

Learn what to do if you [forget your master password](https://bitwarden.com/help/forgot-master-password/).

## Additional login options

Your master password is a requirement for setting up your Bitwarden account. Depending on how you or your organization interact with Bitwarden, additional options are available for accessing your Bitwarden account.

| Method | Description |
|------|------|
| Log in with device | Login with device is an option to utilize a trusted secondary device that can send authentication requests to Bitwarden. Learn more about login with device [here](https://bitwarden.com/help/log-in-with-device/). |
| Log in with SSO | Bitwarden users who are part of an organization that utilizes login with single sign-on(SSO) can login leveraging an existing identity provider, that will authenticate the user. Learn more about login with SSO [here](https://bitwarden.com/help/about-sso/). |
| Log in with passkeys (beta) | Passkeys can be used to log in to Bitwarden as an alternative to using your master password and email, and some passkeys can be used for vault encryption and decryption. Learn more [here](https://bitwarden.com/help/login-with-passkeys/). |
| Unlock with biometrics and unlock with PIN | Using unlock with biometrics or PIN is not an alternative login method, however, this feature can allow you to access a locked account with system biometrics or a PIN instead of a master password. Learn more about [unlock with biometrics](https://bitwarden.com/help/biometrics/) and [unlock with PIN](https://bitwarden.com/help/unlock-with-pin/). |

## Next steps

Now that you have created a **memorable** and **strong** master password, we recommend:

- [Further securing your account with two-step login](https://bitwarden.com/help/setup-two-step-login/)
- [Enabling emergency access](https://bitwarden.com/help/emergency-access/) (requires premium)
