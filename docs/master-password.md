---
URL: https://bitwarden.com/help/master-password/
---

# My Master Password

Your master password is the primary method for accessing Bitwarden. It's important that your master password is:

- **Memorable**: Bitwarden employees and systems have **no** knowledge of, way to retrieve, or way to reset your master password. **Do not forget your master password.**
- **Strong**: A longer, more complex, and less common password is the best way to protect your account. Bitwarden provides a free [**password strength testing tool**](https://bitwarden.com/password-strength/) to test the strength of some memorable passwords you are considering. 

Master passwords made after the [2023.3.0 release](https://bitwarden.com/help/releasenotes/) must be at least 12 characters.

> [!TIP] Tips to mitigate forgetting master password.
> Worried about forgetting your master password? Here's what to do:
> 
> - **Set up a hint**. In case you need a reminder, a master password hint email can be requested on the login screen. Make sure you use a hint that only you will understand.
> - **Designate a**[**trusted emergency contact**](https://bitwarden.com/help/emergency-access/). Users with premium access can grant account access to a friend or family member in the case of emergency.

## Change master password

You can change your master password from the web app, browser extension, or desktop app. You'll need to know your current master password in order to do so:

### Web app

In the web app:

1. Select **Settings** → **Security** from the navigation.
2. Select the **Master password** tab:

![Master password settings](https://bitwarden.com/assets/2Svv0PwlH9i7SSK73dlv9A/e451afb190346e492110a7bf1bd3a518/Master_password_settings.png)
*Master password settings*
3. Enter your **Current master password**.
4. Enter and confirm your **New master password**.
5. (Optional) **Enter a Master password hint** that will help you recall your password. When requested, the hint is sent to the account holder's email.
6. (Optional) If you want to check your master password through [HIBP](https://haveibeenpwned.com/) before submitting it, check **Check known data breaches for the password** to run the [Data Breach report](https://bitwarden.com/help/reports/#data-breach-individual-vaults-only/). This will send a hash of your master password to HIBP and compare it to stored exposed hashes. Your master password itself is never exposed by Bitwarden.

> [!WARNING] Rotate account encryption key.
> Don't check the **rotate account's encryption key** box unless you fully understand the ramifications and required follow-up actions. [Learn more](https://bitwarden.com/help/account-encryption-key/).
7. Select the **Change master password** button.

Changing your master password will automatically log you out of the web vault session. Other logged-in apps may remain active for up to an hour, but will eventually also require you to log back in with your new master password.

### Browser extension

In the browser extension:

1. Open the **Settings** tab and select **Account security**.
2. Scroll to the **Other options** section and select **Change master password**:

![Change master password on browser extension](https://bitwarden.com/assets/13NQDBUne0d99ssQlhxnTy/5320be0c494c351f808db48db48105ba/2026-04-21_09-58-31.png)
*Change master password on browser extension*
3. Enter your **Current master password**.
4. Enter and confirm your **New master password**.
5. (Optional) **Enter a Master password hint** that will help you recall your password. When requested, the hint is sent to the account holder's email.
6. (Optional) If you want to check your master password through [HIBP](https://haveibeenpwned.com/) before submitting it, check **Check known data breaches for the password** to run the [Data Breach report](https://bitwarden.com/help/reports/#data-breach-individual-vaults-only/). This will send a hash of your master password to HIBP and compare it to stored exposed hashes. Your master password itself is never exposed by Bitwarden.
7. Select the **Change master password** button.

Changing your master password will automatically log you out of the web vault session. Other logged-in apps may remain active for up to an hour, but will eventually also require you to log back in with your new master password.

### Desktop app

In the desktop app:

1. From the menu bar, select **Account** → **Change master password**:

![Change master password on desktop](https://bitwarden.com/assets/5X1HjOgjvRg0ewMD30zYaY/4d9dfb5f92429b3b42d5111e0b759ca5/2026-04-21_09-00-24.png)
*Change master password on desktop*
2. Enter your **Current master password**.
3. Enter and confirm your **New master password**.
4. (Optional) **Enter a Master password hint** that will help you recall your password. When requested, the hint is sent to the account holder's email.
5. (Optional) If you want to check your master password through [HIBP](https://haveibeenpwned.com/) before submitting it, check **Check known data breaches for the password** to run the [Data Breach report](https://bitwarden.com/help/reports/#data-breach-individual-vaults-only/). This will send a hash of your master password to HIBP and compare it to stored exposed hashes. Your master password itself is never exposed by Bitwarden.
6. Select the **Change master password** button.

Changing your master password will automatically log you out of the web vault session. Other logged-in apps may remain active for up to an hour, but will eventually also require you to log back in with your new master password.

## I forgot my master password

Learn what to do if you [forget your master password](https://bitwarden.com/help/forgot-master-password/).

## Additional login options

Your master password is a requirement for setting up your Bitwarden account. Depending on how you or your organization interact with Bitwarden, additional options are available for accessing your Bitwarden account.

| Method | Description |
|------|------|
| [Log in with device](https://bitwarden.com/help/log-in-with-device/) | Login with device is an option to utilize a trusted secondary device that can send authentication requests to Bitwarden. |
| [Log in with SSO](https://bitwarden.com/help/about-sso/) | Bitwarden users who are part of an organization that utilizes login with single sign-on(SSO) can login leveraging an existing identity provider, that will authenticate the user. |
| [Log in with passkeys](https://bitwarden.com/help/login-with-passkeys/) | Passkeys can be used to log in to Bitwarden as an alternative to using your master password and email, and some passkeys can be used for vault encryption and decryption. |
| [Unlock with biometrics](https://bitwarden.com/help/biometrics/) and [unlock with PIN](https://bitwarden.com/help/unlock-with-pin/) | While using unlock with biometrics or PIN is not an alternative login method, it allows you to access a locked account with system biometrics or a PIN instead of a master password. |

## Next steps

Now that you have created a **memorable** and **strong** master password, we recommend:

- [Further securing your account with two-step login](https://bitwarden.com/help/setup-two-step-login/)
- [Enabling emergency access](https://bitwarden.com/help/emergency-access/) (requires premium)
