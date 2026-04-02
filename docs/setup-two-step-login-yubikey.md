---
URL: https://bitwarden.com/help/setup-two-step-login-yubikey/
---

# YubiKey OTP Two-Step Login

Two-step login using YubiKey OTP (one-time password) is available for Premium users, including members of paid organizations (Families, Teams, and Enterprise). Any [YubiKey that supports OTP](https://www.yubico.com/products/yubikey-hardware/compare-yubikeys/) can be used. This includes all YubiKey 4 and 5 series devices, as well as YubiKey NEO and YubiKey NFC. You can add up to five YubiKeys to your account. Bitwarden also supports other [passkeys for two-step login](https://bitwarden.com/help/setup-two-step-login-fido/).

> [!TIP] YubiKey with FIDO2 WebAuthn
> Most modern YubiKeys, including 5 series keys, support the FIDO2 WebAuthn protocol. If your key supports it, which you can determine using the [Yubico Authenticator](https://www.yubico.com/products/yubico-authenticator/) desktop application, we recommend setting up your key as a FIDO2 WebAuthn device by following [these instructions](https://bitwarden.com/help/setup-two-step-login-fido/).

## Set up YubiKey

To enable two-step login using Yubikey:

> [!WARNING] Losing 2FA Device (Generic)
> **Losing access to your two-step login device can permanently lock you out of your vault** unless you write down and keep your two-step login recovery code in a safe place or have an alternate two-step login method enabled and available.
> 
> [Get your recovery code](https://bitwarden.com/help/two-step-recovery-code/) from the **Two-step login** screen immediately after enabling any method. Additionally, users may create a Bitwarden [export](https://bitwarden.com/help/export-your-data/) to backup vault data.

1. Log in to the Bitwarden web app.
2. Go to **Account Settings** → **Security**→**Two-step login**:

![Two-step login settings](https://bitwarden.com/assets/2IjxRoQwl1powHRhah6Bq/39067a5fe6c53732054f323e4afb431b/Screenshot_2025-12-31_at_1.52.00â__PM.png)
*Two-step login settings*
3. Next to **YubiKey OTP Security Key**, select **Manage**. You will be prompted to enter your master password to continue.
4. Plug the YubiKey into your computer's USB port.
5. Select the first empty YubiKey input field in the dialog in your web vault.
6. Touch the Yubikey's button.
7. (Optional) If you will be using the YubiKey for a NFC-enabled mobile device, check **One of my keys supports NFC**.
8. Select **Save**. A green `Enabled` message will indicate that two-step login with YubiKey is enabled.
9. Select **Close** and confirm that the **YubiKey OTP Security Key** option is now enabled, as indicated by a green checkbox ( ✓ ).

Repeat this process to add up to five YubiKeys to your account.

> [!NOTE] After activating 2FA, logout of sessions.
> We recommend keeping your active web vault tab open before proceeding to test two-step login in case something was misconfigured. Once you have confirmed it's working, logout of all your Bitwarden apps to require two-step login for each. You will eventually be logged out automatically.

## Self-hosted setup

If you're an organization administrator, you'll need to configure a pair of environment variables in `global.override.env` in order to allow calls to be made to the YubiKey OTP API:

| **Variable** | **Description** |
|------|------|
| globalSettings__yubico__clientId | Replace value with ID received from your Yubico Key. Sign up for Yubico Key [here](https://upgrade.yubico.com/getapikey/). |
| globalSettings__yubico__key | Input the key value received from Yubico. |

## Use YubiKey

The following assumes that **YubiKey** is your [highest-priority enabled method](https://bitwarden.com/help/setup-two-step-login/#using-multiple-methods/). To access your vault using a YubiKey:

1. Log in to your Bitwarden vault with your email address and master password.
2. When prompted, insert your YubiKey into your computer's USB port or hold your YubiKey against the back of your NFC-enabled device:

![YubiKey prompt](https://bitwarden.com/assets/7jikprFVd3XRhOGRCLrEYT/82b0a7332797a1c6ee6add081ea40ab9/2025-03-25_10-15-37.png)

> [!TIP] Remember Me for 2FA
> Check the **Remember Me** box for Bitwarden to recognize your device for 30 days. Selecting this option means you won't be required to complete your two-step login step during that time.
3. If you are using a **non-NFC** YubiKey on a mobile device:

 1. Plug your YubiKey into the device.
 2. Tap **Cancel** to end the NFC prompt:

![Cancel NFC](https://bitwarden.com/assets/0SakpfPW6yFdTU34AHxNu/7b9167ccdccd05cdaa87f748041be031/nonfc.webp)
 3. Tap the text input field, denoted by a gray underline.
 4. Tap or press your YubiKey button to insert your code.
4. Select or tap **Continue** to finish logging in.

You are not required to complete your secondary two-step login step to **unlock** your vault once logged in. For help configuring log out vs. lock behavior, see [vault timeout options](https://bitwarden.com/help/vault-timeout/).

## NFC troubleshooting

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
