---
URL: https://bitwarden.com/help/bitwarden-authenticator/
---

# Bitwarden Authenticator

Bitwarden Authenticator is a standalone app that generates time-based one-time passwords (TOTPs) for logins that support authenticator app two-factor authentication (2FA). It generates 5-10 digit codes, by default using SHA-1 and rotating them every 30 seconds.

Bitwarden offers [two authenticators](https://bitwarden.com/help/bitwarden-authenticator/#whats-the-difference-between-bitwarden-authenticator-and-password-managers/): the Bitwarden Authenticator app and Password Manager [integrated authenticator](https://bitwarden.com/help/integrated-authenticator/). Bitwarden Authenticator is available for everyone, with or without a Bitwarden Password Manager account. If you use both apps, you can [synchronize codes](https://bitwarden.com/help/totp-sync/) between Authenticator and your Bitwarden vault. When synced, your codes will be labelled either **Local Codes** or labelled by your account email address:

![Bitwarden iOS Authenticator app](https://bitwarden.com/assets/4fMWMI0YBJQybhhyOlV0Zb/2bb912b6e9a6f38818cc37d8a0f982b4/2025-05-21_10-13-39.png)
*Bitwarden iOS Authenticator app*

## Install Bitwarden Authenticator

Bitwarden Authenticator is available on iOS and Android devices. To get started, download the app from your device's app store:

- iOS: [App Store](https://apps.apple.com/us/app/bitwarden-authenticator/id6497335175) (iOS 15+)
- Android: [Google Play](https://play.google.com/store/apps/details?id=com.bitwarden.authenticator&pli=1) (Android 9+)

> [!TIP] Authenticator iOS default
> On iOS 16+, you can make [Bitwarden Authenticator](https://bitwarden.com/help/bitwarden-authenticator/) or Password Manager [integrated authentication](https://bitwarden.com/help/integrated-authenticator/) your default verification code app when scanning codes directly from the camera app. To set this up:
> 
> 1. Open the iOS **Settings**app on your device.
> 2. Tap **General**.
> 3. Tap **AutoFill & Passwords**.
> 4. Tap **Password Options**.
> 5. In the **Verification Codes** section, select an app from the **Set Up Codes In** dropdown menu.

## Add codes

You can add codes to Authenticator a few ways. If you already saved verification codes in Password Manager, [sync the apps](https://bitwarden.com/help/totp-sync/#sync-codes-saved-in-your-bitwarden-vault/) to automatically display those codes in Authenticator. For new codes, scan a QR code or manually enter a code key:

### Scan a QR code

In the Bitwarden Authenticator app:

1. Tap the + **Add icon**.
2. Point your camera at the QR code. Scanning will happen automatically.
3. Choose whether to **Save here** (only in Authenticator) or **Save to Bitwarden** (save as a login item in Password Manager).

### Add a code manually

In the Bitwarden Authenticator app:

1. Tap the + **Add icon**.
2. Tap **Enter key manually** at the bottom of the screen.
3. Enter the name of the website or app in the **Name**field.
4. Enter the **Authenticator key**offered by the website or app. Some services refer to this as a "secret key" or "TOTP seed."
5. Choose whether to **Save here** (only in Authenticator) or **Save to Bitwarden** (save as a login item in Password Manager).

> [!TIP] Copy code to BW Authenticator
> If you create a local code in Authenticator and later want to add it to your vault, [copy the code to Password Manager](https://bitwarden.com/help/totp-sync/#move-and-sync-local-codes-to-your-bitwarden-vault/).

## Edit codes

To edit a code that's synced from your vault, [update the login item](https://bitwarden.com/help/managing-items/#manage-items/) in Password Manager. For local codes stored only in Authenticator, long press the code and select **Edit** to access these options:

- Edit the **Name** or **Key**.
- Add a **Username**. Use this field when you have multiple accounts for the same website and require a separate verification code per account.
- Toggle on **Favorite** to move that code to the top of the app's home screen for easy access.
- Change the **Algorithm**used to generate the code. By default, Bitwarden Authenticator uses SHA-1.
- Change the **Refresh period**for the code. By default, Bitwarden Authenticator uses 30 seconds.
- Change the **Number of digits**for the code. By default, Bitwarden Authenticator uses 6 digits.

> [!NOTE] Changing authenticator settings
> **Algorithm**, **Refresh period**, and **Number of digits** are determined by the site you're using the verification code with. Do not change these settings for an item unless that website requires it or allows you to customize verification code behavior.

## Use codes

To use a verification code, open Bitwarden Authenticator and tap an entry to copy it. Then paste the code into the verification prompt where you're logging in.

## Transfer codes to a new mobile device

When you get a new mobile device, you need to transfer your TOTPs for them to appear in Bitwarden Authenticator. Use the method that matches your set-up:

- For local codes, [export your Bitwarden Authenticator data](https://bitwarden.com/help/authenticator-import-export/#export-data/) on your old device. On your new device, [import the file to Authenticator](https://bitwarden.com/help/authenticator-import-export/#import-data/).
- For any codes that synced with Password Manager on the old device, [set up sync](https://bitwarden.com/help/totp-sync/) on your new device. This will pull all verification codes that are attached to saved login items. Alternatively, [export a .json file](https://bitwarden.com/help/export-your-data/) for the TOTPs located in your vault and then [import the file to Authenticator](https://bitwarden.com/help/authenticator-import-export/#import-data/) on your new device.

## Frequently asked questions

### What's the difference between Bitwarden Authenticator and Password Manager's integrated authenticator?

The standalone [Bitwarden Authenticator](https://bitwarden.com/download/#bitwarden-authenticator/) app and Password Manager's [integrated authenticator](https://bitwarden.com/help/integrated-authenticator/) store and generate TOTPs. Based on your security preferences, you can use the apps together, independently, or switch between them. When using both, decide whether to keep your codes connected or managed separately. Key differences include:

| Characteristic | Authenticator | Password Manager's integrated authenticator |
|------|------|------|
| Who can use it | Everyone, no Bitwarden account is required. | Free accounts can store keys. Premium users and members of paid organizations can store keys and generate TOTP codes. |
| Primary use | Anyone who prefers storing 2FA codes separately from their password manager and free Bitwarden accounts that want to generate TOTP codes | Convenient all-in-one password and 2FA management |
| Platforms | Mobile only, iOS and Android | All Bitwarden clients, including mobile, browser extension, desktop app, and web app |
| Default storage | Your local device *If your [Password Manager allows authenticator syncing](https://bitwarden.com/help/totp-sync/) and/or you proactively [copy a local code to your vault](https://bitwarden.com/help/totp-sync/#move-and-sync-local-codes-to-your-bitwarden-vault/), the codes are also stored in your Bitwarden vault. | Your Bitwarden vault |
| Sync between apps | Can manually [copy local codes to Password Manager](https://bitwarden.com/help/totp-sync/#move-and-sync-local-codes-to-your-bitwarden-vault/) to permit syncing and can [automatically sync with codes in Password Manager](https://bitwarden.com/help/totp-sync/#sync-codes-saved-in-your-bitwarden-vault/) | Can automatically [sync with codes in Authenticator](https://bitwarden.com/help/totp-sync/#sync-codes-saved-in-your-bitwarden-vault/) |

### Can I use Bitwarden Authenticator to add 2FA to my Bitwarden account?

Yes! Since Bitwarden Authenticator allows you to store codes outside of your Bitwarden account, this app can be used to [add 2FA to your Bitwarden account](https://bitwarden.com/help/setup-two-step-login-authenticator/).

If you do this, save the code as a **local code** in Authenticator to prevent it from syncing to your vault. Syncing the code to the same vault it's meant to protect could lock you out of it.

### How do I change the Authenticator app's appearance?

Go to **Settings** → **Theme**. You can pick **Light** mode, **Dark** mode, or your device's **Default (System)**.

In Android, you can also toggle on **Use dynamic colors** to match Bitwarden's color scheme to your wallpaper.

### How is my data stored and protected?

Your authentication keys (sometimes referred to as "secret keys" or "TOTP seeds") and all associated metadata are stored in a local unencrypted database on your device. This data is not synced to Bitwarden servers. A backup of your data is made by your device's cloud backup system, for example by iCloud Backup or Google One. To protect the data in your app, you can also set up biometric login.

### How do I back up and restore my TOTP data?

An encrypted backup of your data is made by your device's cloud backup system, for example by iCloud or Google One. To restore your data, restore your device's cloud backup.

You can also [export your authenticator data](https://bitwarden.com/help/authenticator-import-export/#export-data/) and store it securely as a backup.

### Which version of Bitwarden Authenticator am I using?

To learn which version of Bitwarden Authenticator you're using, go to **Settings** and scroll down to the **About** section.
