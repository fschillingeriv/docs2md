---
URL: https://bitwarden.com/help/getting-started-mobile/
---

# Password Manager Mobile Apps

Bitwarden mobile apps let you take your password manager on the go. Download Bitwarden from the [iOS App Store](https://bitwarden.com/download/apple-iphone-password-manager/) or Google Play Store, or by navigating to [get.bitwarden.com](https://get.bitwarden.com) on any device.

![Bitwarden on iOS and Android](https://bitwarden.com/assets/53OzJZ4klYWemxUepHMtq4/5ab47331f033259bd2e82817a99e992f/2025-01-21_15-22-10.png)

> [!TIP] Protect your master password
> Your Bitwarden master password is the single key to your vault. Bitwarden has no way to retrieve or reset it if you forget it. Before going further, make sure you have your master password stored somewhere safe outside of the app — a written note in a secure location, for example. Setting up biometrics or a PIN (covered below) means you'll rarely need to type it on your phone, but you'll need it when you log in for the first time on a new device.

## Step 1: Bring your existing passwords in

Most new users arrive with passwords already saved somewhere — a browser like Chrome or Safari, Apple's Passwords app, or a previous password manager like LastPass or 1Password. **Getting those into Bitwarden is the single most important first step.** Once your passwords are in Bitwarden and synced to your phone, the rest of this guide will make much more sense.

Importing is done through the Bitwarden web app or desktop app, not from the mobile app directly. Once imported, your vault will sync to your phone automatically the next time you open the mobile app.

For step-by-step import instructions, see:

- [Import from Chrome or Edge](https://bitwarden.com/help/import-from-chrome/)
- [Import from Safari / Apple Passwords](https://bitwarden.com/help/import-from-safari/)
- [Import from LastPass](https://bitwarden.com/help/import-from-lastpass/)
- [Import from 1Password](https://bitwarden.com/help/import-from-1password/)
- [Import from all other sources](https://bitwarden.com/help/import-data/)

> [!NOTE] Don't see your passwords on your phone yet?
> After importing on desktop or the web app, open your Bitwarden mobile app and go to **Settings** → **Other** → **Sync now** to pull down your latest vault data immediately.

## Step 2: Understand how Bitwarden locks and logs out

Bitwarden has two secured states — **locked** and **logged out** — that behave differently. Understanding this distinction will save you a lot of confusion.

**Locked** means your vault data is stored encrypted on your device. You don't need an internet connection to unlock, and you can use biometrics or a PIN instead of your master password. This is the state you want your vault to return to when it times out.

**Logged out** means all vault data has been removed from your device. Getting back in requires your master password, an internet connection, and any two-step login method you have enabled. Logging out is the right move on a device you no longer trust, but not ideal for day-to-day use.

### Configure your vault timeout

To set your vault timeout behavior:

1. In the Bitwarden mobile app, tap the ⚙️ **Settings** tab.
2. Tap **Account security**.
3. Set your **Vault timeout** (how long before the app times out after inactivity). A setting of **15 minutes** is a reasonable starting point for most people.
4. Set your **Vault timeout action** to **Lock** — this keeps your vault data on the device so biometrics can unlock it without an internet connection.

> [!TIP] Why this matters for biometrics
> If your vault timeout action is set to **Log out** instead of **Lock**, biometrics won't work the next time you open the app — you'll need your full master password. Make sure **Lock** is selected to get the most out of biometric unlock.

For more detail, see [Automatic Logout or Lock](https://bitwarden.com/help/vault-timeout/).

## Step 3: Set up biometrics or a PIN

Unlocking Bitwarden with biometrics (Face ID, Touch ID, fingerprint) or a PIN means you'll rarely have to type your master password on your phone. Set this up before your vault locks for the first time.

### 🍎 iOS

If you haven't set up Face ID or Touch ID on your device yet, do that first in the iOS ⚙️ **Settings** app.

1. In Bitwarden, tap the ⚙️ **Settings** tab.
2. Tap **Account security**.
3. Tap **Unlock with Face ID** or **Unlock with Touch ID**, depending on your device.
4. Verify with your face or fingerprint when prompted. The toggle will fill to show it's active.

### 🤖 Android

If you haven't set up fingerprint unlock or face unlock on your Android device, do that first in the Android ⚙️ **Settings** app.

1. In Bitwarden, tap the ⚙️ **Settings** tab.
2. Tap **Account security**.
3. Tap **Unlock with biometrics**.

![Biometric unlock on mobile](https://bitwarden.com/assets/7FDRtrf7LkC22dzf3ErsR4/3c176fd1ddb2a3d188817d7e1f795adf/2025-01-21_15-16-44.png)

4. Verify with your fingerprint or face when prompted.

### Set up a PIN as an alternative

A PIN is a good backup to biometrics. To enable one:

1. Tap the ⚙️ **Settings** tab → **Account security** → **Unlock with PIN code**.
2. Choose a PIN. You'll be asked whether you want to require your master password when the app restarts — choose the option that makes sense for your security needs.

For more information, see [Unlock with PIN](https://bitwarden.com/help/unlock-with-pin/).

## Step 4: Set up autofill

Autofill lets Bitwarden automatically enter your username and password into apps and websites so you don't have to copy and paste. This is the most powerful feature of the mobile app.

> [!NOTE] Before you start
> Autofill uses the **URI** field on each vault item to match passwords to the right app or website. If you imported your passwords (Step 1), most items already have URIs. Items you add manually will need a URI for autofill to work with them.

### 🍎 iOS: Set up AutoFill

1. On the iOS home screen, tap the ⚙️ **Settings** app.
2. Tap **General** → **AutoFill & Passwords**.
3. Toggle **AutoFill Passwords and Passkeys** on (green = active).
4. In the **AutoFill From:** list, tap **Bitwarden** to select it.

> [!TIP] One autofill source works best
> If Apple's own **Passwords** app is also toggled on in the AutoFill From list, iOS will show both options every time you tap a login field, which can be confusing. We recommend deactivating other autofill sources and using Bitwarden only.

For more information, see [Autofill Logins on iOS](https://bitwarden.com/help/auto-fill-ios/).

### 🤖 Android: Set up autofill

1. Open your Bitwarden Android app and tap the ⚙️ **Settings** tab.
2. Tap **Autofill**.
3. Toggle **Autofill service** on. You'll be redirected to an Android settings screen.
4. From the autofill provider list, tap **Bitwarden**.
5. Confirm you trust Bitwarden when prompted.

![Android autofill options](https://bitwarden.com/assets/5Othw4YuSWmQbV1pmkvVxd/1d8fcf282bee1d729abe88570e7e650f/2025-01-21_15-29-52.png)

> [!TIP] Using Chrome on Android?
> Chrome requires a separate step. In Bitwarden's **Settings** → **Autofill** screen, also toggle **Use Chrome autofill integration** on. Without this, autofill may not appear when you're logging in through Chrome.

> [!NOTE] Check your preferred autofill provider
> On some Android devices (especially Pixels and Samsung phones running newer Android versions), Bitwarden may appear under "Additional services" rather than "Preferred service." If autofill isn't working, go to your Android **Settings** → **Passwords, passkeys & autofill**, tap the currently preferred service, and switch it to Bitwarden. Google Password Manager should then move to "Additional services" — turn it off there to avoid conflicts.

For more information, see [Autofill Logins on Android](https://bitwarden.com/help/auto-fill-android/).

### Using autofill once it's set up

Once autofill is configured, logging in to an app or website works like this:

1. Tap the email/username or password field in any app or website.

**On iOS:** Tap **Passwords** above the keyboard, or select Bitwarden from the autofill bar that appears.

**On Android:** Tap the Bitwarden overlay that appears near the input field, or use the popup that appears above the keyboard.

2. Bitwarden will prompt you for Face ID, Touch ID, fingerprint, or your PIN.
3. If a matching login is found for that app or website, tap it to fill your credentials automatically. If no match appears, tap 🔍 **Search** to find it manually.

> [!TIP] Autofill not appearing?
> The most common reason autofill doesn't show up is that the vault item doesn't have a URI that matches the current app or website. Open the item in Bitwarden, tap **Edit**, and add the correct URL or app URI. See [Using URIs](https://bitwarden.com/help/uri-match-detection/) for more information.

### Troubleshooting autofill

If you followed the steps above and autofill still isn't working:

- **On Android**, confirm your vault is unlocked (not logged out) before trying to autofill. A logged-out vault won't respond to autofill prompts.
- **On Android**, battery optimization settings can disable Bitwarden's accessibility service in the background. Go to your device's battery settings and turn off battery optimization for Bitwarden. See [Troubleshoot Android Autofill](https://bitwarden.com/help/auto-fill-android-troubleshooting/) for device-specific steps.
- **On iOS**, if you get a loop asking for your master password but nothing fills, check that biometrics is properly enabled in Bitwarden's Account security settings, and that iOS Settings → AutoFill & Passwords still shows Bitwarden as selected.
- On both platforms, make sure the login item has a URI that corresponds to the app or website you're trying to fill.

## Step 5: Add and manage logins

### Add a new login manually

You'll often need to add a login for an app that Bitwarden doesn't automatically prompt you to save. To add one:

1. Navigate to the 🔒 **My Vault** tab and tap the + **Add** icon.
2. Select **Login** as the item type.
3. Enter a **Name** (e.g., `Netflix`), your **Username**, and your **Password**.
4. Tap **+ New URI** and enter the URL for the website or the app package name. This is what Bitwarden uses to match this login during autofill.
5. Tap **Save**.

![Add a login on mobile](https://bitwarden.com/assets/4QMufMJAsQn5qN9XY3syyL/decdef6cfc89e8af57c30e17ddeae864/2025-01-21_15-27-28.png)

### Save new logins as you create them

When you create a new account on an app or website, Bitwarden on mobile may or may not prompt you to save the new credentials automatically — this behavior is less consistent on mobile than on desktop. The most reliable approach is to:

1. Generate a strong password in Bitwarden **before** signing up (see below).
2. Copy it, complete the sign-up form in the other app or browser, then go back to Bitwarden and save the new login manually using the steps above.

This ensures the credential is captured immediately and won't be lost.

### Generate a strong password

When creating or updating a password for an account:

1. Open the vault item and tap **Edit** (iOS) or the ✏️ pencil icon (Android).
2. In the **Password** field, tap the 🔄 **Generate** icon.
3. Confirm **Yes** to replace the existing password with a randomly generated strong one.
4. Tap **Save**, then copy the new password and paste it into the account you're updating.

### Organize with folders

Folders help you find items quickly. To create a folder:

1. Tap the ⚙️ **Settings** tab → **Vault** → **Folders**.
2. Tap the + **Add** icon.
3. Give the folder a name (e.g., `Finance`, `Work`) and tap **Save**.

When adding or editing a vault item, you can assign it to a folder using the **Folder** dropdown.

### Launch directly from Bitwarden

Any vault item with a valid URI has a 🔗 **Launch** button. Tapping it opens the website or app directly. If you're unfamiliar with URIs, see [Using URIs](https://bitwarden.com/help/uri-match-detection/).

![Launch from mobile](https://bitwarden.com/assets/2PsCaLjOAe6WEfnwMkYG0P/be1fde317404835cba1e600244922d98/2025-01-21_15-32-37.png)

## Keeping your vault in sync

Bitwarden syncs your vault automatically when you log in and at regular intervals while the app is open. If you add or change something on another device and don't see it on your phone yet:

1. Tap the ⚙️ **Settings** tab.
2. Tap **Other** → **Sync now**.

You can also enable the **Allow sync on refresh** option to pull down updates by dragging down on the 🔒 **Vaults** tab, similar to refreshing a list in other apps. For more information, see [Sync your Vault](https://bitwarden.com/help/vault-sync/).

## Next steps

Now that the essentials are in place, here are some features worth exploring:

### Add a second account

The mobile app can be logged in to up to five accounts at once. This is useful if you have separate personal and work vaults.

To add a second account, tap the currently logged-in account from the top menu bar and select + **Add Account**:

![Account switching on mobile](https://bitwarden.com/assets/56xAZhiS6wZqKktMlFwbVn/9af5d0ce782af44fc48ebfd8057ddc4c/2025-01-21_14-58-15.png)

Once logged in to a second account, you can switch between them from the same menu, which shows the current status of each vault (locked or unlocked). Logging out of one account removes it from this list.

### Set up two-step login

Two-step login (2FA) adds a second layer of protection to your Bitwarden account so that even if your master password is ever exposed, an attacker still can't get into your vault. We strongly recommend setting this up.

You can enable two-step login from the [Bitwarden web app](https://vault.bitwarden.com) under **Settings** → **Security** → **Two-step login**. Options include authenticator apps, email, and hardware security keys.

For more information, see [Two-Step Login Methods](https://bitwarden.com/help/setup-two-step-login/).

> [!IMPORTANT] Save your recovery code
> When you enable two-step login, Bitwarden gives you a recovery code. **Save this code somewhere safe outside of Bitwarden.** If you lose access to your two-step login device, this code is the only way to get back into your vault. See [Can't Access Two-Step Login](https://bitwarden.com/help/lost-two-step-device/) for more information.

### Explore the Bitwarden Authenticator

Bitwarden can also store TOTP (time-based one-time password) codes for your accounts — the 6-digit codes that many services require as a second login step. This is available on Premium accounts and paid organization memberships.

For more information, see [Integrated Authenticator](https://bitwarden.com/help/integrated-authenticator/).
