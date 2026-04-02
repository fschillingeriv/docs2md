---
URL: https://bitwarden.com/help/setup-two-step-login-fido/
---

# Passkey Two-Step Login

> [!NOTE] Autofill vs. Log in with Passkeys
> Bitwarden offers three passkey features: use [passkeys to log in and unlock](https://bitwarden.com/help/login-with-passkeys/) your Bitwarden account, use [passkeys for 2FA](https://bitwarden.com/help/setup-two-step-login-fido/) on your Bitwarden account, and [autofill stored passkeys](https://bitwarden.com/help/storing-passkeys/) for other websites and services.

Two-step login using FIDO2 WebAuthn credentials is available for free to all Bitwarden users. Any FIDO2 WebAuthn Certified credentials can be used, including security keys such as YubiKeys, SoloKeys, and Nitrokeys, as well as native biometrics options like Windows Hello. On macOS, non-security keys like TouchID are not currently supported.

> [!TIP] U2F to WebAuthn
> All new FIDO keys set up with Bitwarden are registered as WebAuthn keys. If you have a registered FIDO key that is marked **(Migrated from FIDO)** in the Two-step Login → Manage FIDO2 WebAuthn view of the web app, it is a U2F key and should be removed and re-registered to automatically set the key up with WebAuthn. Bitwarden will begin phasing out support for **(Migrated from FIDO)** U2F keys in 2025.

FIDO2 WebAuthn is compatible with most Bitwarden applications. If you wish to use a version that doesn’t support it, ensure you turn on an alternative two-step login method. Supported applications include:

- **Web vault** on a device with a [FIDO2-supported browser](https://fidoalliance.org/fido2/fido2-web-authentication-webauthn/).
- **Browser extensions** for a [FIDO2-supported browser](https://fidoalliance.org/fido2/fido2-web-authentication-webauthn/).
- **Mobile apps** for Android and iOS 13.3+ with a [FIDO2-supported browser](https://fidoalliance.org/fido2/fido2-web-authentication-webauthn/).
- **Desktop apps** on macOS, Windows 10+, and Linux.

## Set up FIDO2 WebAuthn

To enable two-step login using FIDO2 WebAuthn:

> [!WARNING] Losing 2FA Device (Generic)
> **Losing access to your two-step login device can permanently lock you out of your vault** unless you write down and keep your two-step login recovery code in a safe place or have an alternate two-step login method enabled and available.
> 
> [Get your recovery code](https://bitwarden.com/help/two-step-recovery-code/) from the **Two-step login** screen immediately after enabling any method. Additionally, users may create a Bitwarden [export](https://bitwarden.com/help/export-your-data/) to backup vault data.

1. Log in to the Bitwarden web app.
2. Select **Settings** → **Security**→**Two-step login** from the navigation:

![Two-step login settings](https://bitwarden.com/assets/2IjxRoQwl1powHRhah6Bq/39067a5fe6c53732054f323e4afb431b/Screenshot_2025-12-31_at_1.52.00â__PM.png)
*Two-step login settings*
3. Locate the **Passkey** option and select **Manage**. You will be prompted to enter your master password to continue.
4. Give your security key a friendly **Name**.
5. Plug the security key into your device's USB port and select **Read Key**. If your security key has a button, touch it.

> [!NOTE] Windows Hello is FIDO2
> Some devices, including those with Windows Hello or macOS devices that support passkeys, are native FIDO2 authenticators that will offer these options as defaults. If you want to register a security key or other authenticator, you may need to select a **Try another way**, **Other Options**, or **Cancel** button to open up your other options.
6. Select **Save**. A green `Enabled` message will indicate that two-step login using FIDO2 WebAuthn has been successfully enabled and your key will appear with a green checkbox ( ✓ ).
7. Select the **Close** button and confirm that the **FIDO2 WebAuthn** option is now enabled, as indicated by a green checkbox ( ✓ ).

Repeat this process to add up to 5 FIDO2 WebAuthn security keys to your account. Bitwarden Premium accounts may add up to 10 FIDO2 WebAuthn security keys to an account. Learn more about [password manager plans](https://bitwarden.com/help/password-manager-plans/).

> [!NOTE] After activating 2FA, logout of sessions.
> We recommend keeping your active web vault tab open before proceeding to test two-step login in case something was misconfigured. Once you have confirmed it's working, logout of all your Bitwarden apps to require two-step login for each. You will eventually be logged out automatically.

## Use FIDO2 WebAuthn

The following assumes that **FIDO2 WebAuthn** is your [highest-priority enabled method](https://bitwarden.com/help/setup-two-step-login/#using-multiple-methods/). To access your vault using a FIDO2 WebAuthn device:

1. Log in to your Bitwarden vault and enter your email address and master password.

You will be prompted to read your security key, for example by inserting your security key into your device's USB port and tapping the button:

![FIDO2 prompt](https://bitwarden.com/assets/3RuttlEwwfVX3UJKA8GTFg/ab7e0ba835a7f42ea3f10369cb66c008/2025-03-25_10-28-20.png)

> [!TIP] Remember Me for 2FA
> Check the **Remember Me** box for Bitwarden to recognize your device for 30 days. Selecting this option means you won't be required to complete your two-step login step during that time.

You will not be required to complete your secondary two-step login setup to **unlock** your vault once logged in. For help configuring log out vs. lock behavior, see [vault timeout options](https://bitwarden.com/help/vault-timeout/).

## NFC troubleshooting

> [!TIP] 2FA, Use a physical plug
> Hardware security keys typically have a physical plug, which will work more reliably in cases where NFC is difficult.

If your YubiKey's NFC functionality isn't working properly:

##### Check that NFC is enabled:

1. Download [Yubico Authenticator](https://www.yubico.com/products/yubico-authenticator/).
2. Plug the YubiKey into your device.
3. Open the key in Yubico Authenticator and select **Toggle applications**.
4. Enable all NFC options that are available for your key. If there are no NFC options listed, your key may not support NFC.

##### Check that NFC is configured properly:

1. Download the [YubiKey personalization tool](https://www.yubico.com/products/services-software/download/yubikey-personalization-tools/).
2. Plug the YubiKey into your device.
3. Select the **Tools** tab.
4. Select the **NDEF Programming** button.
5. Select the the configuration slot you would like the YubiKey to use over NFC.
6. Select the **Program** button.

##### (Android-only) Check the following:

- That you checked the **One of my keys supports NFC** checkbox during setup.
- That your Android device supports [NFC](https://en.wikipedia.org/wiki/List_of_NFC-enabled_mobile_devices) and is [known to work properly](https://forum.yubico.com/viewtopic1c5f.html?f=26&t=1302) with YubiKey NEO or YubiKey 5 NFC.
- That you have NFC enabled on your Android device (**Settings** → **More**).
- That your keyboard layout/format/mode is set to QWERTY.
