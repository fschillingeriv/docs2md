---
URL: https://bitwarden.com/help/unlock-with-pin/
---

# Unlock With PIN

> [!NOTE] Policy restriction
> If you are a member of an Enterprise organization, a [policy](https://bitwarden.com/help/policies/#remove-unlock-with-pin/) may prohibit you from setting up unlock with PIN.

Bitwarden Password Manager mobile apps, browser extensions, and desktop apps can be unlocked with a PIN. **Unlocking** Password Manager is, importantly, different than **logging in** to it. 

When you log in, you will still be required to use a designated log in method (for example, a [master password](https://bitwarden.com/help/master-password/) or [trusted device](https://bitwarden.com/help/add-a-trusted-device/)) and any active [two-step login method](https://bitwarden.com/help/setup-two-step-login/). Once logged in, you can freely use a PIN to unlock the app. For more information, refer to the article [Understand Unlock vs. Log In](https://bitwarden.com/help/understand-log-in-vs-unlock/).

## Set up a PIN

Complete the following steps to allow your account to be unlocked with a PIN. If you're [logged in to multiple accounts](https://bitwarden.com/help/account-switching/), you'll need to set this up for each:

> [!WARNING] Security Impact of PINs
> Using a PIN can weaken the level of encryption that protects your application's local vault database. If you are worried about attack vectors that involve your device's local data being compromised, you may want to reconsider the convenience of using a PIN.

### Browser extension

To set up a PIN for your browser extension:

1. Open the **Settings** tab, choose the **Account security** menu, and toggle on the **Unlock with PIN** option:

![Toggle unlock with PIN](https://bitwarden.com/assets/6EAFlGeRk9LfFh1GWgowor/0ea284d711e099cf04402ca06869d12a/2025-08-13_10-48-58.png)
2. When prompted, enter the PIN you want to use in the **Set PIN** popup. Your PIN can be any combination of characters (a-z, 0-9, $, #, etc.).

> [!TIP] Choosing a safe PIN
> **Creating a strong PIN**:
> 
> - Avoiding easily guessable digits, like date of birth, especially if you share your device with others.
> - At least 4 characters is required, but using more than the minimum requirement is recommended.
3. The **Require master password on browser restart** option will, by default, require you to enter your master password instead of the PIN when your browser restarts. If you want the ability to unlock with a PIN even when the browser restarts, toggle the option off.

> [!NOTE] Lock w/ MPW on restart
> If you turn off this option, the Bitwarden application may not fully purge sensitive data from application memory when entering a locked state. If you are concerned about your device's local memory being compromised, you should keep this option turned on.

> [!WARNING] Successive failed PINs
> When using a PIN, you will be automatically logged out after **five**failed attempts at entering the PIN.

### Mobile

To set up a PIN for your mobile app:

1. In your Bitwarden app, open the **Settings** tab, choose the **Account security** menu, and tap the **Unlock with PIN Code** option:

![Unlock with PIN on mobile](https://bitwarden.com/assets/7s8JhXJwhOYgmDCuwqEcvd/1451d2e61244617f768f70474ff236a8/2025-01-21_15-07-55.png)
2. When prompted, enter the PIN you want to use in the popup. Your PIN can be any combination of characters (a-z, 0-9, $, #, etc.).

> [!TIP] Choosing a safe PIN
> **Creating a strong PIN**:
> 
> - Avoiding easily guessable digits, like date of birth, especially if you share your device with others.
> - At least 4 characters is required, but using more than the minimum requirement is recommended.
3. When asked whether you want to require unlocking with a biometric or master password when the app is restarted:

 - Choose **Yes** if you want to require a non-PIN unlock method when Password Manager is launched from a closed state.
 - Choose **No** if you want to be able to use your PIN when Password Manager is launched from a closed state.

> [!WARNING] Successive failed PINs
> When using a PIN, you will be automatically logged out after **five**failed attempts at entering the PIN.

### Desktop

To set up a PIN for your desktop app:

1. open your Settings (on Windows or Linux, **File** → **Settings**) (on macOS, **Bitwarden** → **Settings**) and scroll to the **Security** section.
2. Toggle the **Unlock with PIN** option on:

![Unlock with PIN on desktop](https://bitwarden.com/assets/78q1ueLazPoYxUVCqPDjCC/1a614603978a9571eea9c2d33be28333/2026-01-28_09-38-16.png)
*Unlock with PIN on desktop*
3. When prompted, enter the PIN you want to use in the popup. Your PIN can be any combination of characters (a-z, 0-9, $, #, etc.).

> [!TIP] Choosing a safe PIN
> **Creating a strong PIN**:
> 
> - Avoiding easily guessable digits, like date of birth, especially if you share your device with others.
> - At least 4 characters is required, but using more than the minimum requirement is recommended.
4. The **Lock with master password on restart** option will, by default, require you to enter your master password instead of the PIN when your app restarts. If you want the ability to unlock with a PIN even when the browser restarts, toggle the option off.

> [!NOTE] Lock w/ MPW on restart
> If you turn off this option, the Bitwarden application may not fully purge sensitive data from application memory when entering a locked state. If you are concerned about your device's local memory being compromised, you should keep this option turned on.

> [!WARNING] Successive failed PINs
> When using a PIN, you will be automatically logged out after **five**failed attempts at entering the PIN.

### Change a PIN

You can change your PIN at any time toggling the **Unlock with PIN** option off and back on, as described in the directions above. Note that doing so requires that Password Manager is unlocked.

### PINs after a logout

When you log out of your account on any of the above Password Manager apps, your configured PIN and associated settings will be automatically wiped. You can re-activate PIN unlock after logging back in.
