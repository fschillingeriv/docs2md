---
URL: https://bitwarden.com/help/integrated-authenticator/
---

# Integrated Authenticator

Password Manager includes an integrated authenticator that generates verification codes for [two-step login](https://bitwarden.com/help/bitwarden-field-guide-two-step-login/#securing-important-websites/) directly in your vault. Instead of opening a separate app and manually typing codes, it automatically produces the [time-based one-time passwords](https://en.wikipedia.org/wiki/Time-based_One-time_Password_algorithm) (TOTPs), six-digit codes using SHA-1 that rotate every 30 seconds.

> [!NOTE] TOTP account requirements 
> Storing keys in Password Manager integrated authenticator is available to all accounts. Generating TOTP codes is available with Premium or membership to a paid organization (Families, Teams, or Enterprise).

Bitwarden offers two authenticators: Password Manager integrated authenticator and the [Bitwarden Authenticator](https://bitwarden.com/help/bitwarden-authenticator/) app. Learn more about [when to use the different authenticators](https://bitwarden.com/help/bitwarden-authenticator/#whats-the-difference-between-bitwarden-authenticator-and-password-managers/).

## Generate TOTP codes

There are three ways to set up TOTP generation in Password Manager for your vault's login items:

- [Scan a QR code](https://bitwarden.com/help/authenticator-keys/#scan-a-qr-code/) from the Bitwarden mobile app or browser extension.
- [Manually enter a secret](https://bitwarden.com/help/authenticator-keys/#manually-enter-a-secret/) from any Bitwarden app.
- [Sync codes](https://bitwarden.com/help/totp-sync/) with the Bitwarden Authenticator app so the TOTPs also appear in Password Manager.

Once set up, integrated authentication will continuously generate six-digit TOTPs rotated every 30 seconds, which you can use as a secondary step for two-step login to connected websites or apps. You can update the TOTP seed at any time using the [camera]**Camera icon** on the **Edit item** screen.

### Scan a QR code

To set up integrated authentication for a login item using a QR code:

### Mobile

1. **Edit** the vault item for which you want to generate TOTPs.
2. Tap [camera] **Set up TOTP**:

![Set up TOTP on mobile](https://bitwarden.com/assets/1cjF7IObqGhZL2ETA6XhTU/10641831c6fb690b85c3c99f39f1b1b1/2025-01-21_16-46-53.png)
*Set up TOTP on mobile*
3. Scan the QR code.
4. Tap **Save** to begin generating TOTPs.

### Browser extension

1. **Edit** the vault item for which you want to generate TOTPs.
2. Select [camera]**TOTP**, which will scan the authenticator QR code from the current webpage. The full QR code must be visible on-screen.

![Browser extension TOTP scan](https://bitwarden.com/assets/7vTPBRNX8Q1xxOZsqFxWBQ/3a91391f5c233743b8f6be509086f895/2024-10-29_11-04-36.png)
*Browser extension TOTP scan*
3. Tap **Save** once the code has been entered to begin generating TOTPs.

### Manually add a secret

To manually add a secret key to a login item:

1. **Edit** the vault item for which you want to generate TOTPs.
2. Select the **Authenticator key**field. (On mobile apps, you can alternatively select the [camera] **Set up authenticator key** → **Enter key manually** from the **Edit** view.)
3. Paste the secret key into the **Authenticator Key**field.
4. Save the item.

## Use generated codes

After you add a secret key to a login item, there are two ways to retrieve the TOTP: autofilling or copying the code.

> [!NOTE] TOTP & Time
> TOTPs rely on time-based code generation. If your device has an incorrect time compared to the server, it will generate codes that don't work. If you're having trouble with your TOTP codes, set your device's time zone to and [**time to Automatic**](https://bitwarden.com/help/integrated-authenticator/#troubleshooting/).

### Autofill TOTP codes

Bitwarden browser extensions and iOS (version 18.0+) will autofill your TOTP code, unless the [**autofill on page load**](https://bitwarden.com/help/auto-fill-browser/#on-page-load/) setting is active. In that case, the browser extension also copies the TOTP code to your clipboard for easy pasting into the form. 

On browser extensions, you can also copy the TOTP code from the context menu:

![Browser Extension context menu ](https://bitwarden.com/assets/5YmvBLK63g2xMnUewNVjOg/a63aec8b36ac65d6d91acf666fc8406f/2024-10-29_11-11-51.png)
*Browser Extension context menu *

> [!TIP] Extension TOTP copying
> Automatic TOTP copying is on by default when you use autofill in the browser extension. To turn it off, go to **Settings** → **Autofill** and uncheck **Copy TOTP automatically**. You can also use the nearby **Clear clipboard** dropdown menu to specify when copied values are cleared.

### View and copy TOTP codes

All Bitwarden apps display your rotating TOTP code inside the vault item, which can be copied and pasted like a username or password:

![Copy a TOTP code ](https://bitwarden.com/assets/41IqtUVMLh7MLxwwNU2ZpD/b9fc56ddc82ab78130305c0751aac0ca/2024-12-02_14-55-24.png)
*Copy a TOTP code *

When you first open the Bitwarden mobile app, select **Verification codes** to display all active TOTPs in your vault:

![Verification codes on mobile](https://bitwarden.com/assets/3MRb58qhCFvVHVjPaxMk6R/227fae64af8e1a13e6c86a74412929eb/2025-01-21_17-13-12.png)
*Verification codes on mobile*

> [!TIP] Viewing codes when offline
> As long as you're logged in to your Bitwarden vault, your generated codes are available—even when your device is offline.

### Troubleshooting

TOTP codes are generated based on your device's system clock. If your generated codes are not working or invalid, the most likely reason is that your device clock has become out-of-step from the Bitwarden server. To re-sync the clock on your device:

### Windows

Navigate to **Start** → **Settings** → **Time & language** → **Date & time**, and turn the **Set time automatically** option off and back on.

If this doesn't work, use the following PowerShell commands to set your timezone, being sure to replace the timezone name with the right one from [this list](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/default-time-zones?view=windows-11#time-zones), and restart your computer:

```plain text
Set-TimeZone -Id "Central Standard Time"
```

```plain text
Restart-Computer
```

### macOS

Navigate to **System Settings** → **General** → **Date & Time**, and turn the **Set time and date automatically** and **Set time zone automatically using your currently location** options off and back on.

### Android

Navigate to **Settings** → **System** → **Date & time**, and turn the **Set time automatically** option off and back on.

### iOS

Navigate to **Settings** → **General** → **Date & Time**, and turn the **Set Automatically** option off and back on.

## Support for more parameters

By default, Bitwarden will generate six-digit TOTPs using SHA-1 and rotate them every 30 seconds, however some websites or services will expect different parameters. Parameters can be customized in Bitwarden by manually editing the `otpauth://totp/` URI for your vault item.

| **Parameter** | **Description** | **Values** | **Sample** **Query** |
|------|------|------|------|
| Algorithm | Cryptographic algorithm used to generate TOTPs. | -sha1 -sha256 -sha512 -otpauth | `algorithm=sha256` |
| Digits | Number of digits in the generated TOTP. | 1-10 | `digits=8` |
| Period | Number of seconds with which to rotate the TOTP. | Must be > 0 | `period=60` |

For example:

```
otpauth://totp/Test:me?secret=JBSWY3DPEHPK3PXP&algorithm=sha256&digits=8&period=60
```

Learn more about using [otpauth:// URIs](https://github.com/google/google-authenticator/wiki/Key-Uri-Format).

## Set as default on iOS

iOS users running iOS 16+ can set any application as the default for storing verification codes when scanning codes directly from the camera app, including [Bitwarden Authenticator](https://bitwarden.com/help/bitwarden-authenticator/) and Password Manager [integrated authentication](https://bitwarden.com/help/integrated-authenticator/). To set this up:

1. Open the iOS **Settings**app on your device.
2. Tap **General**.
3. Tap **AutoFill & Passwords**.
4. In the **Verification Codes** section, choose an app from the **Set Up Codes In** dropdown.

## Azure and Office 365

By default, Microsoft Azure and Office 365 accounts expect the use of Microsoft Authenticator for TOTPs. To instead use the integrated authenticator in Bitwarden for your Microsoft Azure or Office 365 account(s):

1. In Microsoft, navigate to your account settings page. Depending on whether yours is a personal or business account, this may be `account.microsoft.com` or `myaccount.microsoft.com`.
2. Depending on whether yours is a personal or business account, open your **Security dashboard** or select **Security info**. If you're going through the **Security dashboard**, you'll need to also select **Two-step verification** from that screen.

![Turn on 2FA](https://bitwarden.com/assets/4x8LX6bcktyPDnQhPvSLOz/7903ba57aeb75b15e83562841136a16b/Screen_Shot_2023-02-23_at_10.24.27_AM.png)
*Turn on 2FA*
3. Select either the Two-step verification**Turn on** button or **Add sign-in method** button and choose Authenticator app from the dropdown.
4. During the setup procedure, you'll see a dropdown menu for the verification method. Select **Authenticator App**or **An app**.
5. Proceed until you see a blue "different authenticator app" hyperlink. Select the hyperlink when you see it.
6. Continue until you see a QR code, at which point you can follow the standard [QR code steps](https://bitwarden.com/help/integrated-authenticator/#scan-a-qr-code/).

## Steam Guard TOTPs

You can use the Bitwarden integrated authenticator for your Steam account's 2FA. Once you locate the secret key, enter it in the **Authenticator key** field with this format: `steam://your_secret_key_here`.

> [!NOTE] Steam app auth
> To use this functionality, you will need to manually extract your Steam account's secret using a third-party tool. There are tools such as [SteamTimeIdler](https://github.com/SteamTimeIdler/stidler/wiki/Getting-your-%27shared_secret%27-code-for-use-with-Auto-Restarter-on-Mobile-Authentication#getting-shared-secret-from-ios-windows) that can help you accomplish this, however such **extraction tools are not officially supported by Bitwarden or Steam**. Use these tools at your own risk.

Generated codes for Steam are five digits and alphanumeric, unlike traditional six-digit numeric TOTPs.
