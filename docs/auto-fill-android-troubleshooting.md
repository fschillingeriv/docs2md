---
URL: https://bitwarden.com/help/auto-fill-android-troubleshooting/
---

# Troubleshoot Android Autofill

If you're having trouble with [autofill on Android](https://bitwarden.com/help/auto-fill-android/), first verify that your Android version is compatible with your chosen autofill method. Bitwarden supports a few different autofill methods depending on your Android version:

| **Option** | **Requires version...** | **Requires you to also enable...** |
|------|------|------|
| Autofill Service | Android 8+ | - |
| Inline Autofill | Android 11+ | Autofill service, IME that supports inline |
| Accessibility | All Android versions | - |

Next, confirm that the login item has the correct URI format saved. On Android, Password Manager uses a website (e.g. `https://gmail.com`) to autofill in web browsers and a package name (e.g. `com.google.android.gm`) to autofill in installed applications. 

> [!WARNING] Android Autofill mechanics
> When it comes to installed applications, it's important to **only install and autofill into applications from trusted sources**, like the Google Play Store or F-Droid, because a malicious application could mimic the package name of a well-known application. [Learn more](https://bitwarden.com/help/uri-match-detection/#tab-android-1MW4Dc3sLFszt1M8GaKqyB/).

### Troubleshooting the autofill service

If the Bitwarden autofill service overlay isn't visible when your device is focusing on a username or password input field, your device may require a device-specific setting to be enabled.

**For Huawei/Honor devices**, enable Dropzone:

1. Open the Huawei/Honor Optimizer app (also known as "Phone Manager").
2. Tap **Dropzone** in the middle of the bottom row.
3. Slide the toggle to the right to allow Dropzone.

**For Oppo and other devices**, enable Floating Window:

1. Open the Android Settings app.
2. Navigate to Privacy/Security.
3. Locate **Floating Windows** or **App Management** and tap to open.
4. Slide the toggle to the right to allow Floating Windows.

### Troubleshooting the accessibility service

The most common issue encountered using the accessibility service is that **Android battery optimization** settings will automatically turn off services (like the Accessibility Service) in order to preserve battery. To resolve this, **turn off battery optimization for Bitwarden**.

If you continue to experience issues with the Accessibility Service:

1. Double-check your battery optimization settings. If battery optimization is on for Bitwarden, turn it off.
2. If you use a battery saver or Task Manager app, try disabling to see if that makes a difference. If it does, add Bitwarden to the exception list.
3. Check the built-in Task Manager. You'll need to bring up the running apps view and then hold down the app icon or swipe up on the Bitwarden app and then select **Lock**.

Please note, the service can also halt if you ever "Force stop" the Bitwarden app.

> [!TIP] Default battery optimization configurations
> The site [https://dontkillmyapp.com/](https://dontkillmyapp.com/) might help you determine the default battery optimization configurations for your device.

> [!NOTE] Android autofill help
> If you are still not able to get Android autofill working, [Contact Us](https://bitwarden.com/contact/).
