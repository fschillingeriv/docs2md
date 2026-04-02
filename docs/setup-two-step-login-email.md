---
URL: https://bitwarden.com/help/setup-two-step-login-email/
---

# Email Two-Step Login

Two-step login using email is available for free to all Bitwarden users.

> [!WARNING] Email 2FA & SSO
> Two-step login via email is not recommended if you are using [**login with SSO**](https://bitwarden.com/help/using-sso/)**,**as using multiple methods will cause errors. Consider setting up [two-step login via a free authenticator](https://bitwarden.com/help/setup-two-step-login-authenticator/) instead.

## Setup Email Verification

To enable two-step login using email:

> [!WARNING] Losing 2FA Device (Generic)
> **Losing access to your two-step login device can permanently lock you out of your vault** unless you write down and keep your two-step login recovery code in a safe place or have an alternate two-step login method enabled and available.
> 
> [Get your recovery code](https://bitwarden.com/help/two-step-recovery-code/) from the **Two-step login** screen immediately after enabling any method. Additionally, users may create a Bitwarden [export](https://bitwarden.com/help/export-your-data/) to backup vault data.

1. Log in to the Bitwarden web app
2. Select **Settings** → **Security**→**Two-step login** from the navigation:

![Two-step login settings](https://bitwarden.com/assets/2IjxRoQwl1powHRhah6Bq/39067a5fe6c53732054f323e4afb431b/Screenshot_2025-12-31_at_1.52.00â__PM.png)
*Two-step login settings*
3. Locate the **Email** method and select **Manage**. You will be prompted to enter your master password to continue.
4. Enter the email that you wish you receive verification codes and click the **Send Email** button.

> [!TIP] Which email address to use for 2FA
> If you have multiple email addresses, the address you use for two-step login doesn't have to be the same address you used to sign up for Bitwarden.
5. Check your inbox for the six-digit verification code. Enter the code in the dialog box in your web vault and select the **Enable** button.

A green `Enabled` message will indicate that two-step login via email has been enabled.
6. Select the **Close** button and confirm that the **Email** option is enabled, as indicated by a green checkbox ( ✓ ).

> [!NOTE] After activating 2FA, logout of sessions.
> We recommend keeping your active web vault tab open before proceeding to test two-step login in case something was misconfigured. Once you have confirmed it's working, logout of all your Bitwarden apps to require two-step login for each. You will eventually be logged out automatically.

## Use Email verification

The following assumes that **Email** is your [highest-priority enabled method](https://bitwarden.com/help/setup-two-step-login/#using-multiple-methods/). To access your vault using email 2FA:

1. Log in to your Bitwarden vault on any any app and enter your email address and master password.

You will be prompted to enter the six-digit verification code that was emailed to your configured email.
2. Check your inbox for the six-digit verification code. Enter this code on the **Verify your Identity** screen:

![Verify your identity](https://bitwarden.com/assets/ewFBMVRtmfZ3fsEC7LZmG/fcda3ce63380357797c2d41987854318/2026-01-12_15-08-12.png)
*Verify your identity*

> [!TIP] Remember Me for 2FA
> Check the **Remember Me** box for Bitwarden to recognize your device for 30 days. Selecting this option means you won't be required to complete your two-step login step during that time.
3. Select **Continue** to finish logging in.

You will not be required to complete your secondary two-step Login step to **Unlock** your vault once logged in. For help configuring log out vs. Lock behavior, see [vault timeout options](https://bitwarden.com/help/vault-timeout/).
