---
URL: https://bitwarden.com/help/setup-two-step-login-authenticator/
---

# Authenticator Two-Step Login

Two-step login using a third-party authenticator app (for example, the standalone [Bitwarden Authenticator](https://bitwarden.com/help/bitwarden-authenticator/)) is available for free to all Bitwarden users.

> [!NOTE] Authenticator App Backups
> Some authenticator apps do not automatically backup your 2FA tokens for easy migration to a new mobile device. In these cases, you should manually save each token's authenticator recovery codes. See [Recovery codes](https://bitwarden.com/help/two-step-recovery-code/) for additional information to safely store and use recovery codes.
> 
> Some apps, such as Authy, do support backup and sync across devices. In these cases, be sure to set a strong backup password and keep a record of it in your Bitwarden vault.

## Set up an authenticator

To enable two-step login using an authenticator app:

> [!WARNING] Losing 2FA Device (Generic)
> **Losing access to your two-step login device can permanently lock you out of your vault** unless you write down and keep your two-step login recovery code in a safe place or have an alternate two-step login method enabled and available.
> 
> [Get your recovery code](https://bitwarden.com/help/two-step-recovery-code/) from the **Two-step login** screen immediately after enabling any method. Additionally, users may create a Bitwarden [export](https://bitwarden.com/help/export-your-data/) to backup vault data.

1. Log in to the Bitwarden web app.
2. Select **Settings** → **Security**→**Two-step login** from the navigation:

![Two-step login settings](https://bitwarden.com/assets/2IjxRoQwl1powHRhah6Bq/39067a5fe6c53732054f323e4afb431b/Screenshot_2025-12-31_at_1.52.00â__PM.png)
*Two-step login settings*
3. Locate the **Authenticator App** method and select **Manage** on that line. You will be prompted to enter your master password to continue.
4. Scan the QR code or manually enter the key using your authenticator app of choice.

If you don't have an authenticator app on your mobile device yet, download one like [Bitwarden Authenticator](https://bitwarden.com/help/bitwarden-authenticator/) and scan the QR code.
5. Once scanned, your authenticator app will return a six-digit verification code. Enter the code in the dialog box in your web vault and select the **Enable** button.

A green `Enabled` message will indicate that two-step login via authenticator has been enabled.
6. Select the **Close** button and confirm that the **Authenticator App** option now is enabled, as indicated by a green checkbox ( ✓ ).

> [!NOTE] After activating 2FA, logout of sessions.
> We recommend keeping your active web vault tab open before proceeding to test two-step login in case something was misconfigured. Once you have confirmed it's working, logout of all your Bitwarden apps to require two-step login for each. You will eventually be logged out automatically.

### Setup on multiple devices or authenticators

Bitwarden two-step login can be made to work with multiple compatible devices. To add 2FA to an additional device, follow the steps above and scan the QR code with your additional device or manually enter the QR key to enable 2FA on the additional device. This can also be done to setup two-step login for multiple authenticators on a single device.

## Use an authenticator

The following assumes that **Authenticator App** is your [highest-priority enabled method](https://bitwarden.com/help/setup-two-step-login/#using-multiple-methods/). To access your vault using an authenticator:

1. Log in to your Bitwarden vault on any app and enter your email address and master password.

You will be prompted to enter the six-digit verification code from your authenticator app.
2. Open your authenticator app and find the six-digit verification code for your Bitwarden vault. Enter this code on the vault login screen. Typically, verification codes will change every 30 seconds.

> [!TIP] Remember Me for 2FA
> Check the **Remember Me** box for Bitwarden to recognize your device for 30 days. Selecting this option means you won't be required to complete your two-step login step during that time.
3. Select **Continue** to finish logging in.

You will not be required to complete your secondary two-step login step to **Unlock** your vault once logged in. For help configuring log out vs. lock behavior, see [vault timeout options](https://bitwarden.com/help/vault-timeout/).
