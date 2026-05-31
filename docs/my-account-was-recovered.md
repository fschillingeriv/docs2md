---
URL: https://bitwarden.com/help/my-account-was-recovered/
---

# My Account Was Recovered

If your organization administrator [resets your master password or two-step login method](https://bitwarden.com/help/recover-a-member-account/), Bitwarden will send you an email. This message is meant to keep you informed and help you regain access to your account.

> [!NOTE] Account recovery doesn't bypass SSO
> Account recovery only affects credentials configured within Bitwarden. It **does not bypass SSO** or any two-factor authentication configured with your IdP. If your organization [requires SSO authentication](https://bitwarden.com/help/policies/#require-single-sign-on-authentication/), you are still required to use those methods to access your account after recovery.

## Reset master password

After you receive the account recovery email, ask your administrator for the temporary master password. Use a secure channel to receive it, such as [Bitwarden Send](https://bitwarden.com/help/create-send/). To then reset your master password:

1. Within the email, select **Recover your account** to open the recovery web page.
2. Enter your email and select **Continue**.
3. Enter your temporary master password and select **Log in with master password**.
4. Create a new master password and select **Change master password**.
5. Log in to your Bitwarden account with your email and new master password.
6. (Optional) Go to **Settings** -> **Security** to set up a new [two-step login method](https://bitwarden.com/help/setup-two-step-login/).

You are required to update your master password after a reset because a master password should be **strong**, **memorable**, and something **only you** know.

## Reset two-step login

Your administrator may instead leave your master password as-in and only remove the two-step login configured for your Bitwarden account. To add a new two-step login method in this scenario:

1. Within the email, select **Recover your account** to open the recovery web page.
2. Enter your email and select **Continue**.
3. Enter your existing master password and select **Log in with master password**.
4. The page to set up [two-step login methods](https://bitwarden.com/help/setup-two-step-login/) will open. Set up the method of your choice.

> [!NOTE] Need to restore account after account recovery if two-step policy enabled
> If you're unable to access your organization's data after connecting a new two-step login method, contact your administrator. They may need to [restore](https://bitwarden.com/help/revoke-users/#restore-access/) your account.
