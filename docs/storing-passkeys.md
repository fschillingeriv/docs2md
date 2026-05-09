---
URL: https://bitwarden.com/help/storing-passkeys/
---

# Autofill Passkeys

> [!NOTE] Autofill vs. Log in with Passkeys
> Bitwarden offers three passkey features:
> 
> - Use [passkeys to log in and unlock](https://bitwarden.com/help/login-with-passkeys/) your Bitwarden account.
> - Use [2FA with passkeys](https://bitwarden.com/help/setup-two-step-login-fido/) to log in to your Bitwarden account.
> - [Save and autofill passkeys](https://bitwarden.com/help/storing-passkeys/) for other services from your Bitwarden vault

Passkeys can be stored and used by Bitwarden Password Manager. Using browser extensions and mobile apps, users can log in to their favorite apps and websites that have passkey login capability. Passkeys are a safe, passwordless alternative for users to log into services across their devices.

Developed with the standards set by the [<u>FIDO Alliance</u>](https://fidoalliance.org/overview/), passkeys allow a user to secure their accounts and bypass the vulnerabilities that come with standard password authentication, such as phishing. Stored passkeys are protected with Bitwarden's trusted end-to-end encryption.

## What are passkeys?

[Passkeys](https://bitwarden.com/resources/passkeys-faq/) are a replacement for passwords that provide fast, easy, and secure sign-ins to websites and apps. Passkeys are a discoverable FIDO credential that can be synced to allow secure passwordless sign-ins across devices, or dedicated to a single piece of hardware as a device-bound passkey. 

Apps and services can request that passkeys created with them are verified with a PIN, password, pattern, or biometric factor when you save or access them.

### Types of passkey

Passkeys are stored and invoked via the Bitwarden browser extension and mobile apps. Discoverable passkeys and non-discoverable FIDO2 credentials can be stored in Bitwarden and used to log in to websites with passkey capabilities.

## Save and autofill passkeys with Bitwarden

Storing and using passkeys is available with the Bitwarden browser extension and mobile apps.

### Browser extensions

> [!NOTE] Excluded domains supress passkeys
> The browser extension will not offer to save or use a passkey for any domain included in the [**excluded domains**](https://bitwarden.com/help/exclude-domains/) list.

### Allow passkeys with the browser extension

First, open the Bitwarden browser extension and go to **Settings** → **Notifications**. Verify that the **Ask to save and use passkeys**option is checked.

If there are specific sites you do not wish to use Bitwarden for passkeys with, set [excluded domains](https://bitwarden.com/help/exclude-domains/).

### Create a passkey

When creating a new passkey on a website or app, the browser extension will prompt you to store the passkey: 

![Save passkey](https://bitwarden.com/assets/3kj9zFGb1nJgW236SUaBON/4a6fc1892506164f37586fa4a4fc9aa2/2024-10-29_11-33-21.png)

> [!NOTE] Use your device or hardware key (browser)
> Select **Use your device or hardware key** if you do not wish to store the passkey in Bitwarden.

Only one passkey can be saved per login item. If a passkey already exists for a service, overwrite the existing passkey or select the + **Add icon** to create a new login item to store an additional passkey:

![Save passkey with existing login](https://bitwarden.com/assets/2GnYjzxkUFsYftwOSKz1Fi/e065e2784cd4b1eb21470fdfd64a35e9/2024-10-29_11-37-38.png)

### Sign in using a passkey stored in Bitwarden

First, confirm that the **Ask to save and use passkeys** extension setting is turned on. Then start the passkey login on the website. From the window that appears, select your saved passkey:

![Log in with passkey](https://bitwarden.com/assets/5KeuUZox5shd0zDMxPHKXn/1aab35dfceed0ed9cdb17b143be9a890/2024-10-29_11-39-33.png)

If you prefer to use an existing passkey stored outside of Bitwarden, select **Use your device or hardware key**. This will close the pop-up window and not enter any passkey from Bitwarden.

> [!TIP] Inline autofill menu for passkeys
> The [inline autofill menu](https://bitwarden.com/help/auto-fill-browser/#inline-autofill-menu/) can also be used to easily authenticate with passkeys.

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

## View passkeys in Bitwarden

Saved passkeys can be accessed from any Bitwarden app. Within the login item, the **Passkey** field displays the date and time that the passkey was created: 

![Passkey in your vault](https://bitwarden.com/assets/2SofQpuQstpo6gnIg9irwM/5ad0255aa61813dd55a6d4081e7c234d/2024-12-02_16-07-56.png)

> [!NOTE] master password reprompt
> If [master password re-prompt](https://bitwarden.com/help/master-password-re-prompt/) is used on the login item, you're required to re-enter your master password to access the passkey.

### Delete passkeys

To delete a passkey from a vault item:

1. Open the item **Edit** screen from the Password Manager web app, browser extension, or desktop app.
2. Select the - **Delete icon** for the **Passkey** field:

![Delete a passkey](https://bitwarden.com/assets/448nZ5ybyis0nUEwWsq6kt/8442776aca2a73eec13d30ce25b08f9a/2024-12-02_16-08-55.png)

### Export and import passkeys

Passkeys are included in [JSON exports](https://bitwarden.com/help/export-your-data/) generated by Bitwarden and, once exported, can be [imported to a Bitwarden account](https://bitwarden.com/help/import-data/).
