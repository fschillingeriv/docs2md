---
URL: https://bitwarden.com/help/storing-passkeys/
---

# Autofill Passkeys

> [!NOTE] Autofill vs. Log in with Passkeys
> Bitwarden offers three passkey features: use [passkeys to log in and unlock](https://bitwarden.com/help/login-with-passkeys/) your Bitwarden account, use [passkeys for 2FA](https://bitwarden.com/help/setup-two-step-login-fido/) on your Bitwarden account, and [autofill stored passkeys](https://bitwarden.com/help/storing-passkeys/) for other websites and services.

Passkeys can be stored and used by Bitwarden Password Manager. Using browser extensions and mobile apps, users can log in to their favorite apps and websites that have passkey login capability. Passkeys are a safe, passwordless alternative for users to log into services across their devices.

Developed with the standards set by the [<u>FIDO Alliance</u>](https://fidoalliance.org/overview/), passkeys allow a user to secure their accounts and bypass the vulnerabilities that come with standard password authentication, such as phishing. Stored passkeys are protected with Bitwarden's trusted end-to-end encryption.

> [!NOTE] Passkeys availability (mobile)
> On iOS, version 17.0 or higher is required for storing and using passkeys. [Learn more](https://bitwarden.com/help/auto-fill-ios/).
> 
> On Android, version 14.0 or higher is required for storing and using passkeys. There may be additional setup steps required. [Learn more](https://bitwarden.com/help/auto-fill-android/).

## What are passkeys?

Passkeys are a replacement for passwords that provide fast, easy, and secure sign-ins to websites and apps across a user's devices. More precisely, "passkey" is a consumer-friendly term for a discoverable FIDO credential that can be synced to allow secure passwordless sign-ins across devices, or dedicated to a single piece of hardware as a device-bound passkey. 

Apps and services can request that passkeys created with them are verified with a PIN, password, pattern, or biometric factor when you save or access them. For more general information about passkeys, see [Passkey FAQs](https://bitwarden.com/resources/passkeys-faq/).

### Types of passkeys

Passkeys are stored and invoked via Bitwarden browser extensions and mobile apps. This means that both discoverable passkeys and non-discoverable FIDO2 credentials can be stored in Bitwarden and used to log in to websites with passkey capabilities.

## Using passkeys with Bitwarden

> [!NOTE] Passkey storage only available in browser ext & moile
> Saving and using passkeys are a feature of Bitwarden browser extensions and mobile apps. Please note:
> 
> - On iOS, version 17.0 or higher is required for storing and using passkeys. [Learn more](https://bitwarden.com/help/auto-fill-ios/).
> - On Android, version 14.0 or higher is required for storing and using passkeys. There may be additional setup steps required. [Learn more](https://bitwarden.com/help/auto-fill-android/).

### Browser extensions

> [!NOTE] Excluded domains surpress passkeys
> When a domain is in the [**Excluded Domains**](https://bitwarden.com/help/exclude-domains/)list, Bitwarden browser extensions won't issue passkey prompts.

### Ask to save and use passkeys

To use the functionality described below, make sure that the **Ask to save and use passkeys**option, located in the browser extensions **Settings** → **Notifications** menu, is toggled on.

You can set [excluded domains](https://bitwarden.com/help/exclude-domains/) if there are specific sites you do not wish to use Bitwarden for passkeys with.

### Create a passkey

When creating a new passkey on a website or app, the browser extension will prompt you to store the passkey: 

![Save passkey](https://bitwarden.com/assets/3kj9zFGb1nJgW236SUaBON/4a6fc1892506164f37586fa4a4fc9aa2/2024-10-29_11-33-21.png)

> [!NOTE] Use your device or hardware key (browser)
> Select **Use your device or hardware key** if you do not wish to store the passkey in Bitwarden.

If a passkey already exists for this service, Bitwarden will allow you to save a new passkey by selecting the + icon to create a new item, or by overwriting an existing passkey:

![Save passkey with existing login](https://bitwarden.com/assets/2GnYjzxkUFsYftwOSKz1Fi/e065e2784cd4b1eb21470fdfd64a35e9/2024-10-29_11-37-38.png)

Duplicate passkeys cannot be saved for the same username and service. You may edit or overwrite an existing cipher if you wish to save a new passkey with the username and service.

> [!NOTE] One passkey per login
> Only one passkey can be saved per login item. If a credential is saved in multiple places, for instance as two separate login items in the individual vault and organization vault respectively, a different passkey can be be stored with each login item.

### Sign in using a passkey stored in Bitwarden

To use a passkey stored in Bitwarden, initiate the passkey login on the website. When the **Ask to save and use passkeys**option is on, the browser extension will provide an option to login using the passkey stored in your Bitwarden vault:

> [!TIP] Inline autofill menu for passkeys
> The [inline autofill menu](https://bitwarden.com/help/auto-fill-browser/#inline-autofill-menu/) can also be used to easily authenticate with passkeys.

![Log in with passkey](https://bitwarden.com/assets/5KeuUZox5shd0zDMxPHKXn/1aab35dfceed0ed9cdb17b143be9a890/2024-10-29_11-39-33.png)

Select the passkey you would like to use.

> [!NOTE] Other options for passkeys (browser extension)
> Select **Use your device or hardware key** if you do not wish to store the passkey in Bitwarden, or to use an existing passkey that is not stored in Bitwarden.

### iOS

### Setup Bitwarden for use with passkeys

To use the functionality described below, open your iOS **Settings** app and navigate to **Passwords** → **Password Options**. Toggle the following options on:

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

Duplicate passkeys cannot be saved for the same username and service. You may edit or overwrite an existing cipher if you wish to save a new passkey with the username and service.

> [!NOTE] One passkey per login
> Only one passkey can be saved per login item. If a credential is saved in multiple places, for instance as two separate login items in the individual vault and organization vault respectively, a different passkey can be be stored with each login item.

### Sign in using a passkey stored in Bitwarden

To use a passkey stored in Bitwarden, initiate the passkey login on the website. The mobile app will provide an option to login using the passkey stored in your Bitwarden vault:

![Sign in with passkey](https://bitwarden.com/assets/b6fY5o4CBxhW4ZjDIpanR/56ffdbf1ff93b7387be273bc7df15e6b/passkey-ios-3__1_.png)
*Sign in with passkey*

Select **Continue**.

> [!NOTE] Other options for passkeys (iOS)
> Select **Other Options** if you do not wish to store the passkey in Bitwarden or **Other Sign In Options** to sign in with a passkey not stored in Bitwarden.

### Android

### Setup Bitwarden for use with passkeys

Once the Bitwarden application is updated to the latest version, go to **Settings**→ **Auto-fill** and tap **Passkey management** to access the Android settings to configure Bitwarden as your passkey provider. Please note that Android does not allow 3rd party passkey providers like Bitwarden to support passkey-based 2FA (a.k.a. "non-discoverable credentials"); Bitwarden-stored passkeys can only be used as a primary login credential.

### Create a passkey

When creating a new passkey on a website or app, the Android application will prompt you to store the passkey:

![Create a passkey](https://bitwarden.com/assets/4mBZ6s599BKxzn86CDwBhH/e2a313ab3dc263cd93f5da24e7cad778/passkey-android-1__1_.png)
*Create a passkey*

Select **Create**.

> [!NOTE] Other options for passkeys (Android)
> Select **Save another way**if you do not wish to store the passkey in Bitwarden or **More saved sign-ins**to sign in with a passkey not stored in Bitwarden.

If a passkey already exists for this service, Bitwarden will allow you to save a new passkey by selecting the + icon to create a new item, or by overwriting an existing passkey:

![Save or overwrite a passkey](https://bitwarden.com/assets/m8rHHqT8hmuEY7wB9WKld/573de4ef230d2d9cdbdcd94574b55168/passkey-android-2__1_.png)
*Save or overwrite a passkey*

Duplicate passkeys cannot be saved for the same username and service. You may edit or overwrite an existing cipher if you wish to save a new passkey with the username and service.

> [!NOTE] One passkey per login
> Only one passkey can be saved per login item. If a credential is saved in multiple places, for instance as two separate login items in the individual vault and organization vault respectively, a different passkey can be be stored with each login item.

### Sign in using a passkey stored in Bitwarden

To use a passkey stored in Bitwarden, initiate the passkey login on the website. The mobile app will provide an option to login using the passkey stored in your Bitwarden vault:

![Sign in with passkey](https://bitwarden.com/assets/2COiWur13OpX1QZ7Fy0tbR/65e2b4d39e2387fdcb0ba380ab52fa04/passkey-android-3__1_.png)
*Sign in with passkey*

Select **Sign in** to use your passkey.

> [!NOTE] Other options for passkeys (Android)
> Select **Save another way**if you do not wish to store the passkey in Bitwarden or **More saved sign-ins**to sign in with a passkey not stored in Bitwarden.

## Viewing passkeys in Bitwarden

Once a passkey has been saved, it can be viewed from any Bitwarden app and is located in the **Passkey** field:

![Passkey in your vault](https://bitwarden.com/assets/2SofQpuQstpo6gnIg9irwM/5ad0255aa61813dd55a6d4081e7c234d/2024-12-02_16-07-56.png)

> [!NOTE] master password reprompt
> If master password re-prompt has been enabled on the login item, you will be required to re-enter your master password in order to access the passkey.

### Deleting passkeys

To delete a passkey from a vault item:

1. Open the item **Edit** screen from the Password Manager web app, browser extension or desktop app.
2. Select the - delete icon for the **Passkey** field.

![Delete a passkey](https://bitwarden.com/assets/448nZ5ybyis0nUEwWsq6kt/8442776aca2a73eec13d30ce25b08f9a/2024-12-02_16-08-55.png)

## Passkey Management FAQ

The following FAQ items are in reference to Bitwarden passkey storage. For general passkey information, see [Passkey FAQs](https://bitwarden.com/resources/passkeys-faq/).

#### **Q:**Will passkeys be included if you [clone](https://bitwarden.com/help/managing-items/#clone/) a vault item?

**A:**Bitwarden will not copy a passkey when completing a clone action.

#### **Q:** Are stored passkeys included in Bitwarden imports and exports?

**A:**Passkeys are included in [.json exports](https://bitwarden.com/help/export-your-data/) from Bitwarden and, once exported, can be [imported to a Bitwarden account](https://bitwarden.com/help/import-data/). The ability to transfer your passkeys to or from another passkey provider is planned for a future release.

#### **Q:** Can I store passkeys in the mobile app?

**A:**Passkeys support for mobile applications is available for iOS ([learn more](https://bitwarden.com/help/auto-fill-ios/)) and for Android ([learn more](https://bitwarden.com/help/auto-fill-android/)).
