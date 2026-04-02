---
URL: https://bitwarden.com/help/auto-fill-android/
---

# Autofill from Android App

Bitwarden makes your passwords available for autofill so that you can seamlessly log in to websites and apps while also maintaining strong and secure passwords. Autofill cuts the copying and pasting out of your login routine by detecting vault items that match the service you are logging in to.

Custom fields and split login workflows (when username and password fields are displayed on separate screens) are not currently supported in mobile autofill.

> [!WARNING] Android Autofill mechanics
> When it comes to installed applications, it's important to **only install and autofill into applications from trusted sources**, like the Google Play Store or F-Droid, because a malicious application could mimic the package name of a well-known application. [Learn more](https://bitwarden.com/help/uri-match-detection/#tab-android-1MW4Dc3sLFszt1M8GaKqyB/).

## Set up autofill

Depending on the version of Android your device is running, there are a few different ways to enable autofill from Bitwarden. To set up autofill:

1. Navigate to **Settings** → **Autofill**.
2. Tap **Autofill services**to allow Bitwarden to use your saved login information to sign in to apps on your device.
3. When your device asks for your preferred services for passwords, passkeys, & autofill, choose **Bitwarden**.
4. Back on the Bitwarden **Settings** → **Autofill** screen, choose one of the following **Display autofill suggestions**options:

 - **Inline**: This option will suggest credentials to autofill in your keyboard.
 - **Popup**: This option will suggest credentials to autofill in a popup over the input field.
5. If you use Brave or Chrome as your web browser, toggle the **Use Brave autofill integration** or **Use Chrome autofill integration** options on to ensure that autofill will work in these browsers. Learn more [below](https://bitwarden.com/help/auto-fill-android/#browser-integrations/).

> [!NOTE] Adroid autofill HTTP chromium
> Due to the way Brave and Chome Android apps function, autofill will not work on sites using HTTP unless a browser flag is manually turned on. To enable Autofill on for HTTP sites on Brave/Chrome:
> 
> 1. Navigate to `brave://flags`
> 2. seach for **Insecure origins treated as secure**and enable the flag
> 3. Add required HTTP domains/IPs, for example: `http://192.0.2.0/24`, or `http://myserver.local`
> 4. Relaunch Brave.
6. If you want to use Quick-action tiles, toggle **Use accessibility** on. When your device takes you to the **Accessibility** menu, toggle Bitwarden on in that location as well.

> [!TIP] Quick Tile Actions
> Quick-action tiles do not require that the **Autofill service**is toggled on in Bitwarden, meaning you can skip the previous steps if this is your preferred method, however you will need to edit your tiles using the [pencil] icon to put the Bitwarden tile options in a place that makes sense for you.

> [!NOTE] There's a troubleshooting guide
> Having problems? Refer to our guide on [troubleshooting Android Autofill](https://bitwarden.com/help/auto-fill-android-troubleshooting/). If you are still not able to get autofill on Android working, [contact us](https://bitwarden.com/contact/).

## Autofill methods

### Inline

This method suggests credentials to autofill in your keyboard:

![Android inline autofill](https://bitwarden.com/assets/2LxDxR7KcVd68U9UydYxat/e02408654528f4262a293de61e1439bb/2025-07-30_10-56-55.png)

If you're not seeing suggestions:

- Make sure you're using Android 11+ and a compatible IME (input method editor).
- Check that the keyboard IME you're using supports inline.

### Popup

This method overlays a popup menu when the device is focused on an input that has a [matching login item](https://bitwarden.com/help/uri-match-detection/). When your vault is unlocked, you'll be provided the options to immediately autofill or to open your vault:

![Android popup autofill](https://bitwarden.com/assets/1fIoPhOLMcXzvd0Y8aw1pm/642f9f722291f2de3daf93f2fd9a6450/2025-07-30_10-59-13.png)

You'll be presented with two options. The first (above, **My Login Item**) will autofill the first login (above, `my_username`) with a matching URI. The second (above, **Bitwarden**) will allow you to choose from a list of logins with matching URIs.

This method requires Android 8+.

### Browser integrations

If you use Brave, Chrome, or Vivaldi as your web browser, toggle the **Use Brave <browser> integration** option, where **<browser>** is the name of that browser, on to ensure that autofill will work in these browsers. Doing so will take you to that web browser's settings, where you will also need to enable the option to use a third-party service. 

This is required by Chrome so it can securely use Bitwarden to autofill passwords through its protected autofill system, and requires that **Autofill services**is enabled in Bitwarden and that the installed Chrome app is at least version 135. These options will disable the browser's built-in autofill functionality in favor of Bitwarden.

> [!WARNING] Risks of compatibility mode.
> Bitwarden will automatically detect whether you're using **Edge, Opera, or Samsung Internet**, will not require an integration option to be turned on for those browsers, and will use a modified autofill logic within those browsers. 
> 
> On Edge, Opera, or Samsung Internet, take care to only autofill trusted and legitimate websites, as a vulnerability exists that could allow credentials to be autofilled into an embedded or hidden iframe on a malicious website.

![Enable android integrations](https://bitwarden.com/assets/1Qm4g428OlYOBvzAxKwUNU/77106f75d8f5af42bed8bde4db9dc325/2025-07-30_13-14-04.png)

### Quick-action tiles

Quick-action tiles use the Android accessibility service to make autofill actions available from your notifications pull-down's settings menu. Quick-action tiles do not require that the **Autofill service**is toggled on in Bitwarden, however you will need to edit your tiles using the [pencil] icon to put the Bitwarden tile options in a place that makes sense for you:

![Android quick-action autofill](https://bitwarden.com/assets/7MHfjTUrRjdLtBoyL3Ukz2/7980adfc9de7b6b2659f1955d3d987fd/2025-07-30_11-07-51.png)

To use a quick-action tile, navigate to the page or app you want to autofill and, swipe down to access the tiles, and tap the tile you want to use.

## Autofill passkeys

The Bitwarden Android app can be used to store and autofill passkeys. To turn on the ability to autofill passkeys, navigate to **Settings**→ **Autofill** and tap **Passkey management** to access the Android settings used to configure Bitwarden as your passkey provider. Please note that Android does not allow 3rd party passkey providers like Bitwarden to support passkey-based 2FA (a.k.a. "non-discoverable credentials"); Bitwarden-stored passkeys can only be used as a primary login credential. Learn more about [storing and autofilling passkeys on Android](https://bitwarden.com/help/storing-passkeys/#tab-android-3XutklkReT3Gw0l1qHhBem/).

## Switch accounts during autofill

If you are [logged in to more than one account](https://bitwarden.com/help/account-switching/), your mobile app will default to trying to autofill credentials from the currently active account. You can switch from one account to another during autofill by tapping the avatar bubble.
