---
URL: https://bitwarden.com/help/storing-passkeys/
---

# Autofill Passkeys

> [!NOTE] Autofill vs. Log in with Passkeys
> Bitwarden offers three passkey features:
> 
> - [Save and autofill passkeys](https://bitwarden.com/help/storing-passkeys/) for other services from your Bitwarden vault.
> - Use [passkeys to log in and unlock](https://bitwarden.com/help/login-with-passkeys/) your Bitwarden account.*
> - Use [passkeys for 2FA](https://bitwarden.com/help/setup-two-step-login-fido/) to protect your Bitwarden account.*
> 
> * Some authenticators, notably Windows Hello, will not allow you to use a passkey for both login and 2FA.

Passkeys are a secure alternative to traditional passwords that let you log in to apps and websites without entering a password. Developed with the standards set by the [<u>FIDO Alliance</u>](https://fidoalliance.org/overview/), passkeys bypass vulnerabilities that come with standard passwords, like phishing. 

Save passkeys in your Bitwarden vault and use the browser extension, mobile apps, or desktop apps to autofill them across the apps and websites you use every day. Stored passkeys are protected with Bitwarden's trusted end-to-end encryption.

## What are passkeys?

A [passkey](https://bitwarden.com/resources/passkeys-faq/) is a pair of extremely large numbers, called keys, that work together to securely verify your identity. The website stores one key, and the other stays private in your password manager or on your device. Because each passkey works only on the website it was created for, fake lookalike sites can’t trick you into using it.

When logging in to a website or app, you choose to sign in with a passkey and then confirm it’s you. Some passkeys replace your username and password entirely, while others add a step after you enter a password. Depending on the site and type of passkey, confirming it's you might mean unlocking Bitwarden or using your device’s PIN, pattern, or biometrics, such as your fingerprint or face.

### Types of passkeys

Passkeys vary based on where they’re stored and how they’re used:

- **Synced or device-bound**: Synced passkeys, like those stored in Bitwarden, are available across devices where you use Bitwarden. Device-bound passkeys live on a single piece of hardware, such as a YubiKey, and can’t be copied.
- **Discoverable or non-discoverable**: Discoverable passkeys let you sign in without entering a username or password. Non-discoverable FIDO2 credentials are typically used for 2FA after entering your password.

Discoverable passkeys and non-discoverable FIDO2 credentials can be stored in Bitwarden and used to log in to websites with passkey capabilities. Passkeys saved in Bitwarden are synced between devices where you use Bitwarden.

> [!NOTE] Only some passkeys support PRF
> Some passkeys support the [PRF extension](https://bitwarden.com/blog/prf-webauthn-and-its-role-in-passkeys/), which lets them generate an encryption key. To [unlock your Bitwarden vault with a passkey](https://bitwarden.com/help/login-with-passkeys/) instead of your master password, you’ll need a passkey that supports PRF.

## Save and autofill passkeys with Bitwarden

Storing and using passkeys is available with the Bitwarden browser extension, mobile apps, and desktop apps.

> [!NOTE] Can't save passkey for Bitwarden in Bitwarden
> Bitwarden will not prompt or allow you to save a passkey in your vault that's used to log in to any Bitwarden account. This prevents the circular problem of needing access to your vault to log in to the very same vault.

### Browser extensions

> [!NOTE] Excluded domains supress passkeys
> The browser extension will not offer to save or use a passkey for any domain included in the [**excluded domains**](https://bitwarden.com/help/exclude-domains/) list.

### Allow passkeys with the browser extension

First, open the Bitwarden browser extension and go to **Settings** → **Notifications**. Verify that the **Ask to save and use passkeys**option is checked.

If there are specific sites you do not wish to use Bitwarden for passkeys with, set [excluded domains](https://bitwarden.com/help/exclude-domains/).

### Create a passkey

When creating a new passkey on a website or app, the browser extension will prompt you to store the passkey:

![Save passkey](https://bitwarden.com/assets/3kj9zFGb1nJgW236SUaBON/4a6fc1892506164f37586fa4a4fc9aa2/2024-10-29_11-33-21.png)
*Save passkey*

 

> [!NOTE] Use your device or hardware key (browser)
> Select **Use your device or hardware key** if you do not wish to store the passkey in Bitwarden.

Only one passkey can be saved per login item. If a passkey already exists for a service, overwrite the existing passkey or select the + **Add icon** to create a new login item to store an additional passkey:

![Save passkey with existing login](https://bitwarden.com/assets/2GnYjzxkUFsYftwOSKz1Fi/e065e2784cd4b1eb21470fdfd64a35e9/2024-10-29_11-37-38.png)
*Save passkey with existing login*

### Sign in using a passkey stored in Bitwarden

First, confirm that the **Ask to save and use passkeys** extension setting is turned on. Then start the passkey login on the website. From the window that appears, select your saved passkey:

![Log in with passkey](https://bitwarden.com/assets/5KeuUZox5shd0zDMxPHKXn/1aab35dfceed0ed9cdb17b143be9a890/2024-10-29_11-39-33.png)
*Log in with passkey*

Alternatively, the [inline autofill menu](https://bitwarden.com/help/auto-fill-browser/#inline-autofill-menu/) can also be used to authenticate with passkeys.

> [!NOTE] Undo use own passkey
> If you previously selected **Use your device or hardware key**, Bitwarden will not offer to enter or save a passkey. If you clicked this by accident or change your mind, remove the website from [blocked domains](https://bitwarden.com/help/blocking-uris/). The next time you go to that service's login screen, Bitwarden will ask to save your passkey.

### iOS

You can save and use passkeys from Bitwarden with iOS version 17.0+.

### Set up Bitwarden for use with passkeys

To allow Bitwarden to store and use passkeys in iOS:

1. Open the iOS **Settings** app.
2. Go to **Passwords** → **View AutoFill Settings**.
3. Tap **AutoFill Passwords and Passkeys**. A list of apps where passkeys can be stored will appear.
4. Tap **Bitwarden**.

### Create a passkey

When creating a new passkey on a website or app, the Bitwarden iOS app will prompt you to store the passkey:

![Create a passkey](https://bitwarden.com/assets/6rccoaRtUBbEnUjQxfSTNi/d033196df75950bae5bd7a20e8a7edd2/passkey-ios-1__1_.png)
*Create a passkey*

Select **Continue**.

> [!NOTE] Don't save passkey (iOS)
> If you don't want to store the passkey in Bitwarden, select **Other Options**.

Only one passkey can be saved per login item. If a passkey already exists for a service, overwrite the existing passkey or select the + **Add icon** to create a new login item to store an additional passkey:

![Save or overwrite a passkey](https://bitwarden.com/assets/6L5s6XBFjvaaEiDZ68m00Q/a130745c2276068fd0be066a47a34684/passkey-ios-2__1_.png)
*Save or overwrite a passkey*

### Sign in using a passkey stored in Bitwarden

To use a passkey stored in Bitwarden, start the passkey login on the website. The mobile app will provide an option to login using the passkey stored in your Bitwarden vault:

![Sign in with passkey](https://bitwarden.com/assets/b6fY5o4CBxhW4ZjDIpanR/56ffdbf1ff93b7387be273bc7df15e6b/passkey-ios-3__1_.png)
*Sign in with passkey*

Select **Continue**.

> [!NOTE] Sign in with non-Bitwarden saved passkey (iOS)
> If you prefer to sign in with a passkey not stored in Bitwarden, select **Other Sign In Options**.

### Android

You can save and use passkeys from Bitwarden with Android version 14.0+.

> [!NOTE] Android passkeys, no passkey-based 2FA
> In Android, Bitwarden-stored passkeys can only be used as a primary login credential. Android does not allow third-party passkey providers like Bitwarden to support passkey-based 2FA, also known as "non-discoverable credentials."

### Set up Bitwarden for use with passkeys

To allow Bitwarden to store and use passkeys in Android:

1. Open the Bitwarden app.
2. Go to **Settings** → **Autofill**.
3. Tap **Passkey management**.
4. Tap **Continue**.
5. This will open your device's **Settings** app. Configure Bitwarden as your passkey provider.

### Create a passkey

When creating a new passkey on a website or app, the Bitwarden Android app will prompt you to store the passkey:

![Create a passkey](https://bitwarden.com/assets/4mBZ6s599BKxzn86CDwBhH/e2a313ab3dc263cd93f5da24e7cad778/passkey-android-1__1_.png)
*Create a passkey*

Select **Create**.

> [!NOTE] Don't save passkey (Android)
> If you don't want to store the passkey in Bitwarden, select **Save another way**.

Only one passkey can be saved per login item. If a passkey already exists for a service, overwrite the existing passkey or select the + **Add icon** to create a new login item to store an additional passkey:

![Save or overwrite a passkey](https://bitwarden.com/assets/m8rHHqT8hmuEY7wB9WKld/573de4ef230d2d9cdbdcd94574b55168/passkey-android-2__1_.png)
*Save or overwrite a passkey*

### Sign in using a passkey stored in Bitwarden

To use a passkey stored in Bitwarden, start the passkey login on the website. The mobile app will provide an option to login using the passkey stored in your Bitwarden vault:

![Sign in with passkey](https://bitwarden.com/assets/2COiWur13OpX1QZ7Fy0tbR/65e2b4d39e2387fdcb0ba380ab52fa04/passkey-android-3__1_.png)
*Sign in with passkey*

Select **Sign in** to use your passkey.

> [!NOTE] Sign in with non-Bitwarden saved passkey (Android)
> If you prefer to sign in with a passkey not stored in Bitwarden, select **More saved sign-ins**.

### Windows

You can save and use passkeys from the Bitwarden desktop app. On Windows, this must be an `appx` or Microsoft Store distribution.

If you're using the desktop app to save and use passkeys, we recommend you turn passkey functions off in the Bitwarden browser extension to prevent collision.

## Allow passkeys with the desktop app

To allow Bitwarden to store and use passkeys in Windows:

1. Open the Bitwarden desktop app.
2. Go to **File** → **Settings**.
3. Below **Passkey provider**, select **Manage in system settings**.
4. A pop-up window will appear that lists your available passkey managers. Select the slider next to **Bitwarden** to turn it **On**.

## Create a passkey

When creating a new passkey on a website or app, you'll be prompted to store the passkey in Bitwarden. Select **Continue** and follow the prompts, which vary depending on the type of passkey:

![Create passkey in Windows desktop](https://bitwarden.com/assets/3baKU5E96m37UaicXW3fyB/ebdf212d2460fa14d0f1d9a21e5a49a0/Create_passkey_in_Windows_desktop.png)
*Create passkey in Windows desktop*

Only one passkey can be saved per login item. If a passkey already exists for a service, overwrite the existing passkey or create a new login item to store an additional passkey.

## Sign in using a passkey stored in Bitwarden

Start the passkey login on the website. From the window that appears, select your saved passkey:

![Sign in with passkey in Windows](https://bitwarden.com/assets/MnwSF40M8vWs1s6diioB7/8abc3b9238525a354a04e72f6049fa1a/Sign_in_with_passkey_in_Windows.png)
*Sign in with passkey in Windows*

### macOS

You can save and use passkeys from the Bitwarden desktop app in macOS.

If you're using the desktop app to save and use passkeys, we recommend you turn passkey functions off in the Bitwarden browser extension to prevent collision.

## Allow passkeys with the desktop app

To allow Bitwarden to store and use passkeys:

1. Open the Bitwarden desktop app.
2. From the menu bar, go to **Bitwarden** → **Preferences**.
3. Below **Passkey provider**, select **Manage in system settings**.
4. A pop-up window will appear, asking if you want to use autofill from Bitwarden. Select **Turn On**.

## Create a passkey

When creating a new passkey on a website or app, you'll be prompted to store the passkey in Bitwarden. Select **Continue** and follow the prompts, which vary depending on the type of passkey:

![Create passkey in macOS desktop](https://bitwarden.com/assets/c1xX5mR7BPK06IHgd9BQd/224aaff724cf6b844d1e9355f110d186/Create_passkey_in_macOS_desktop.png)
*Create passkey in macOS desktop*

Only one passkey can be saved per login item. If a passkey already exists for a service, overwrite the existing passkey or create a new login item to store an additional passkey.

## Sign in using a passkey stored in Bitwarden

Start the passkey login on the website. From the window that appears, select your saved passkey:

![Sign in with passkey in macOS](https://bitwarden.com/assets/w39vqckTJBynB4d4r0SrP/2350605c13065b93456a526eb197e4f7/Sign_in_with_passkey_in_macOS.png)
*Sign in with passkey in macOS*

## View passkeys in Bitwarden

Saved passkeys can be accessed from any Bitwarden app. Within the login item, the **Passkey** field displays the date and time that the passkey was created: 

![Passkey in your vault](https://bitwarden.com/assets/2SofQpuQstpo6gnIg9irwM/5ad0255aa61813dd55a6d4081e7c234d/2024-12-02_16-07-56.png)
*Passkey in your vault*

> [!NOTE] master password reprompt
> If [master password re-prompt](https://bitwarden.com/help/master-password-re-prompt/) is used on the login item, you're required to re-enter your master password to access the passkey.

### Delete passkeys

To delete a passkey from a vault item:

1. Open the item **Edit** screen from the Password Manager web app, browser extension, or desktop app.
2. Select the - **Delete icon** for the **Passkey** field:

![Delete a passkey](https://bitwarden.com/assets/448nZ5ybyis0nUEwWsq6kt/8442776aca2a73eec13d30ce25b08f9a/2024-12-02_16-08-55.png)
*Delete a passkey*
3. Select **Delete** to confirm.
4. Select **Save**.

### Export and import passkeys

Passkeys are included in [JSON exports](https://bitwarden.com/help/export-your-data/) generated by Bitwarden and, once exported, can be [imported to a Bitwarden account](https://bitwarden.com/help/import-data/). 

On mobile, passkeys can also be [imported](https://bitwarden.com/help/import-data/#tab-mobile-5ALQx9afSqWXX9jfXsY5sb/) and [exported](https://bitwarden.com/help/export-your-data/#tab-mobile-1QlXqfleMlF6jWT87Dbn2u/) directly using the FIDO Credential Exchange Protocol (CXP), on iOS 26+ and Android 14+. Both applications must support CXP.
