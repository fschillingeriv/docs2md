---
URL: https://bitwarden.com/help/auto-fill-ios/
---

# Autofill from iOS App

Bitwarden makes your passwords and passkeys available for autofill so that you can seamlessly log in to websites and apps while also maintaining strong and secure passwords. Autofill cuts the copying and pasting out of your login routine by detecting vault items that match the service you are logging in to.

Custom fields and split login workflows (when username and password fields are displayed on separate screens) are not currently supported in mobile autofill.

## Set up autofill

> [!NOTE] autofill URI
> Most autofill methods require login items to have an [assigned website URI](https://bitwarden.com/help/uri-match-detection/).

There are a few different ways to autofill on iOS:

- **Keyboard autofill**: (Recommended) Use this option to make Bitwarden autofill accessible in any iOS app—including web browsers—through a keyboard button or slide-up prompt.
- **Browser app extension**: Use this option to make Bitwarden autofill accessible only in web browser apps, like Safari, through the Share menu.
- **Long-press a text field**: Use this option to autofill from Bitwarden in a larger variety of locations.

> [!NOTE] iOS AutoFill
> It is currently not possible to use auto-fill on iOS if your [vault timeout action](https://bitwarden.com/help/vault-timeout/#session-timeout-action/) is set to **Log Out** and your only enabled [two-step login method](https://bitwarden.com/help/setup-two-step-login/) requires NFC (for example, an NFC YubiKey), as iOS will not allow NFC inputs to interrupt autofill workflows.
> 
> Either change your vault timeout action to **Lock**, or enable another two-step login method.

> [!NOTE] iOS autofill Argon2id
> If you are using Argon2id with a KDF memory value higher than 64 MB, a warning dialogue will be displayed every time iOS autofill is initiated or a new Send is created through the Share sheet. To avoid this message, adjust Argon2id settings [here](https://bitwarden.com/help/kdf-algorithms/#argon2id/) or enable [unlock with biometrics](https://bitwarden.com/help/biometrics/#enable-unlock-with-biometrics/).

### Keyboard autofill

To activate keyboard autofill on iOS for passwords, complete the following steps. This will also activate the slide-up menu for passkey autofill:

1. Open iOS ⚙️ **Settings** and then **General** on your device.
2. Tap **AutoFill & Passwords**.
3. Toggle **AutoFill Passwords and Passkeys** on and tap **Bitwarden** in the **Autofill From** list:

![Setup autofill on iOS](https://bitwarden.com/assets/5jxVP3WslH4ppIdFq9viqX/613fbbb9eacbb14f56c0fbcee17bc9a1/2025-01-22_11-00-15.png)

> [!NOTE] Disable other autofill providers on iOS
> We highly recommend deactivating any other autofill service, like Keychain, in the **Autofill From** list.

Next, test autofill to make sure it works properly:

1. Open an app or website that you aren't currently signed in to.
2. Tap the username or password field on the login screen. A keyboard will slide up with a matching login (`my_username`), or with a 🔑 **Passwords** button:

![AutoFill on iOS ](https://bitwarden.com/assets/vQG8BTWlHg2AQxBlXe4S3/63f2a5e9c32c2f38b29ec0ab0af24d57/autofill-ios.jpeg)
3. If a [matching login](https://bitwarden.com/help/uri-match-detection/) is displayed, tap it to autofill. If the 🔑 **Passwords** button is displayed, tap it to browse your vault for the login to use. In cases where the 🔑 **Passwords** button is displayed, it's probably because there isn't an item in your vault with a [matching URI](https://bitwarden.com/help/uri-match-detection/).

> [!NOTE] iOS biometric unlock disabled with autofill
> Are you getting a `Biometric unlock disabled pending verification of master password` message? [Learn what to do](https://bitwarden.com/help/autofill-faqs/#q-what-do-i-do-about-biometric-unlock-disabled-pending-verification-of-master-password/).

### Browser app extension autofill

To enable browser app extension autofill on iOS:

1. Open your Bitwarden app and tap ⚙️ **Settings**.
2. Tap **Autofill**.
3. Tap the **App extension** option in the Autofill section.
4. Tap the **Activate app extension** button.
5. From the share menu that slides up, tap **Bitwarden**.

A green `Extension Activated!` message will indicate success.

Then test that the app extension is working correctly:

1. Open your device's web browser and navigate to a website that you aren't currently signed in to.
2. Tap the **Share** icon.
3. Scroll down and tap the **Bitwarden** option:

![Bitwarden in the Share menu ](https://bitwarden.com/assets/3Icxd3YqcXjBrjHVAeluwm/8be732b1ed2adebfd0a7af00f7150a97/extension.png)

> [!NOTE]
> If you have [unlock with biometrics](https://bitwarden.com/help/biometrics/) enabled, the first time you tap this option you will be prompted to verify your master password.
4. A Bitwarden screen will slide up on your device and will list [matching logins](https://bitwarden.com/help/uri-match-detection/) for the website. Tap the item to autofill.

> [!NOTE]
> If there are no logins listed, it's probably because there isn't a login in your vault with a [matching URI](https://bitwarden.com/help/uri-match-detection/).

### Long-press a text field

By long-pressing any text field, you can autofill data from Bitwarden and long as it's active as the keyboard auto-fill option:

![Long-press a text field on iOS](https://bitwarden.com/assets/77glhnjH87Z6PKscElWtZy/f9229264859577c0490cf423237f8502/2025-01-22_11-05-33.png)

## Switch accounts during autofill

If you are [logged in to more than one account](https://bitwarden.com/help/account-switching/), your [mobile app ](https://bitwarden.com/download/apple-iphone-password-manager/)will default to trying to autofill credentials from the currently active account. You can switch from one account to another during autofill by tapping the avatar bubble.

## Use passkeys

### Set up Bitwarden for use with passkeys

Autofilling passkeys, including being prompted by Bitwarden when you create a new passkey, requires iOS 17.0 or higher.

To use the functionality described below:

1. Open your iOS **Settings** app.
2. Go to **Passwords** → **Password Options**.
3. Toggle the following options on:

 - Toggle **AutoFill Passwords and Passkeys**on.
 - Toggle **Bitwarden**on in the **Use passwords and passkeys from:**list.

### Create a passkey

When creating a new passkey on a website or app, the iOS application will prompt you to store the passkey:

![Create a passkey](https://bitwarden.com/assets/6rccoaRtUBbEnUjQxfSTNi/d033196df75950bae5bd7a20e8a7edd2/passkey-ios-1__1_.png)
*Create a passkey*

Select **Continue**.

> [!NOTE] Other options for passkeys (iOS)
> Select **Other Options** if you do not wish to store the passkey in Bitwarden or **Other Sign In Options** to sign in with a passkey not stored in Bitwarden.

If a passkey already exists for this service, Bitwarden will allow you to save a new passkey by selecting the + icon to create a new item, or by overwriting an existing passkey:

![Save or overwrite a passkey](https://bitwarden.com/assets/6L5s6XBFjvaaEiDZ68m00Q/a130745c2276068fd0be066a47a34684/passkey-ios-2__1_.png)
*Save or overwrite a passkey*

> [!NOTE] One passkey per login
> Only one passkey can be saved per login item. If a credential is saved in multiple places, for instance as two separate login items in the individual vault and organization vault respectively, a different passkey can be be stored with each login item.

### Sign in using a passkey stored in Bitwarden

To use a passkey stored in Bitwarden, initiate the passkey login on the website. The mobile app will provide an option to login using the passkey stored in your Bitwarden vault:

![Sign in with passkey](https://bitwarden.com/assets/b6fY5o4CBxhW4ZjDIpanR/56ffdbf1ff93b7387be273bc7df15e6b/passkey-ios-3__1_.png)
*Sign in with passkey*

Select **Continue**.

> [!NOTE] Other options for passkeys (iOS)
> Select **Other Options** if you do not wish to store the passkey in Bitwarden or **Other Sign In Options** to sign in with a passkey not stored in Bitwarden.
