---
URL: https://bitwarden.com/help/biometrics/
---

# Unlock With Biometrics

Quickly and securely access your vault with biometrics in the desktop app, browser extension, and mobile app. After logging in with your standard method, like a [master password](https://bitwarden.com/help/master-password/) or [trusted device](https://bitwarden.com/help/add-a-trusted-device/), [unlock your vault](https://bitwarden.com/help/understand-log-in-vs-unlock/) with biometrics.

Biometric features are part of the built-in security in your device and/or operating system. **Bitwarden never receives your biometrics data**, because the feature uses native APIs to perform the validation on your local device.

> [!TIP] Biometric for multiple accounts
> Security settings are set per account. To turn on biometric unlock for [multiple accounts](https://bitwarden.com/help/account-switching/), like individual and organization accounts, repeat these steps for each one.

## Set up biometrics for desktop app

To set up biometrics in the desktop app:

### Windows

Set up unlock with biometrics for Windows via [Windows Hello](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/windows-hello) using PIN, facial recognition, or other hardware that meets [Windows Hello biometric requirements](https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/windows-hello-biometric-requirements). This option is supported in the Windows desktop app when it’s installed from [Bitwarden Downloads](https://bitwarden.com/download/#downloads-desktop-applications/). If the desktop app was installed from the Microsoft Store, biometrics will not work.

To turn on biometric unlock:

1. [Turn on Windows Hello](https://support.microsoft.com/en-us/windows/configure-windows-hello-dae28983-8242-bb2a-d3d1-87c9d265a5f0) in your device’s system settings.

> [!NOTE] Microsoft Visual C++ Redistributable
> If you are unable to turn on Windows Hello in your device settings, install [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170).
2. Download the Bitwarden desktop app from [Bitwarden Downloads](https://bitwarden.com/download/#downloads-desktop-applications/) (if you haven’t already). Bitwarden desktop app installs from the Microsoft Store do not support biometric unlock.
3. Open the Bitwarden desktop app and go to **File** → **Settings**.
4. Under **Security**, check **Unlock with Windows Hello**.
5. (Optional) If you want to use biometrics to unlock your vault when the desktop app restarts, uncheck **Require master password or PIN on app restart**. You will be prompted to confirm your biometric in a pop-up window. If this setting remains checked, you will need to enter your master password or PIN every time the desktop app restarts.

### macOS

Set up unlock with biometrics for macOS via [Touch ID](https://support.apple.com/en-us/HT207054). This option is supported in the macOS desktop app when it’s installed from the [Mac App Store](https://apps.apple.com/us/app/bitwarden/id1352778147?mt=12), but not from the Bitwarden downloads page.

To turn on biometric unlock:

1. [Turn on Touch ID](https://support.apple.com/guide/mac-help/use-touch-id-mchl16fbf90a/mac) in your device’s system settings.
2. Download the Bitwarden desktop app from the [Mac App Store](https://apps.apple.com/us/app/bitwarden/id1352778147?mt=12) (if you haven’t already). Bitwarden desktop app installs from the Bitwarden Download page do not support biometric unlock.
3. Open the Bitwarden desktop and go to **Bitwarden** → **Settings**.
4. Under **Security**, check **Unlock with Touch ID** and confirm the update when prompted.
5. (Optional) Check **Ask for Touch ID on app start** to use Touch ID when the desktop app first opens, skipping the initial unlock screen.

### Linux

Unlocking the Bitwarden desktop app with biometrics is supported in Linux when your system has a polkit agent and secret service daemon, such as GNOME Keyring. All available Linux versions of the [Bitwarden desktop app](https://bitwarden.com/download/#downloads-desktop-applications/) support unlock with biometrics.

> [!NOTE] Linux-biometrics compatibility by package
> We recommend installing the `Snap` or `Flatpak` versions of the Bitwarden desktop app, because they are fully supported with automatic updates. These versions are not, however, compatible with biometrics in the Bitwarden browser extension. The other Linux package types, `AppImage`, `.deb`, and `.rpm`, are compatible with biometrics in the browser extension but do not receive automatic updates.

## AppImage, Snap, .deb, and .rpm

To turn on biometric unlock:

1. Turn on system authentication on your machine.
2. Open the Bitwarden desktop and go to **File** → **Settings**.
3. Under **Security**, check **Unlock with system authentication** and confirm the update when prompted.

> [!NOTE] Log in before biometrics-Linux
> After biometrics are configured for the Linux desktop app, you still need to log in with a master password or PIN. Once logged in, use biometrics to unlock your vault.

## Flatpak

To turn on biometric unlock:

1. Copy [this policy](https://github.com/bitwarden/clients/blob/main/apps/desktop/resources/com.bitwarden.desktop.policy) to `/usr/share/polkit-1/actions/com.Bitwarden.policy` on your machine, for example:

```bash
sudo wget -O /usr/share/polkit-1/actions/com.bitwarden.Bitwarden.policy https://raw.githubusercontent.com/bitwarden/clients/main/apps/desktop/resources/com.bitwarden.desktop.policy
```
2. Change the ownership of the downloaded file:

```bash
sudo chown root:root /usr/share/polkit-1/actions/com.bitwarden.Bitwarden.policy
```
3. Change the security context of the file:

```bash
sudo chcon system_u:object_r:usr_t:s0
```
4. Turn on system authentication on your machine.
5. Open the Bitwarden desktop and go to **File** → **Settings**.
6. Under **Security**, check **Unlock with system authentication** and confirm the update when prompted.

> [!NOTE] Log in before biometrics-Linux
> After biometrics are configured for the Linux desktop app, you still need to log in with a master password or PIN. Once logged in, use biometrics to unlock your vault.

## Set up biometrics for browser extension

The ability to unlock your vault with biometrics is supported on these browsers:

- Chromium-based browsers, including Chrome, Edge, Opera, and Brave
- Firefox 87+ (Firefox ESR is not supported.)
- Safari 14+

To set up biometrics on the browser extension or a mobile device:

### Chromium-based & Firefox

There are two steps to enabling biometrics for browser extensions: [activate the integration](https://bitwarden.com/help/biometrics/#1-activate-the-integration/) and [activate extension biometrics](https://bitwarden.com/help/biometrics/#2-activate-extension-biometrics/).

### Activate the integration

First, open the Bitwarden desktop app and update the settings:

1. Turn on unlock with biometrics in the [Bitwarden desktop app](https://bitwarden.com/help/biometrics/#set-up-biometrics-for-desktop-app/).
2. Open the Bitwarden desktop app **Settings**. (For Windows and Linux, go to **File** → **Settings**. For macOS, go to **Bitwarden** → **Settings**.)
3. Check **Allow browser integration**.

> [!WARNING] macOS username size bug
> On macOS, you may encounter an error if your username directory (e.g. `/Users/your_username/Library/...`) is longer than 104 characters. If you encounter this error, shorten your username.
4. (Optional) Check **Require verification for browser integration** to ask for fingerprint verification every time the integration between the desktop app and browser extension is activated.

### Activate extension biometrics

> [!NOTE] Allow access to file URLs
> Some browsers, notably Chrome and Chromium-based browsers like Edge and Brave, may require an additional permission for biometrics to work properly:
> 
> 1. Using the web browser address bar, navigate to the extensions manager (e.g. `chrome://extensions or brave://extensions`).
> 2. Open the Bitwarden entry on this page and toggle on **Allow access to file URLs**.

Next, remain logged in to the Bitwarden desktop app and open the Bitwarden browser extension. To turn on unlock with biometrics for the browser extension:

1. Select the ⚙️ **Settings** icon.
2. Select **Account security**.
3. Check **Unlock with biometrics**.
4. You may see a prompt asking permission for Bitwarden to “communicate with cooperating native applications.” Select **Allow**.

> [!NOTE] Communicate with cooperating native applications
> This permission is required for the browser extension to unlock with biometrics. If you decline, you can continue using the browser extension, but unlock with biometrics will not work.
5. Go to the desktop app and there:

 1. Select **Approve** to verify the browser connection.
 2. Enter your biometric when prompted.
6. (Optional) If you previously turned on **Require verification for browser integration**, enter your fingerprint when prompted.
7. (Optional) Check **Ask for biometrics on launch** to use biometrics when the browser extension first opens, skipping the initial unlock screen.

### Safari

To turn on biometric unlock:

1. Select the ⚙️ **Settings** icon.
2. Select **Account security**.
3. If a confirmation window appears, enter your device’s password and click **Always Allow**.
4. Check **Unlock with biometrics**.
5. When prompted, enter your Touch ID.
6. (Optional) Check **Ask for biometrics on launch** to use biometrics when the browser extension first opens, skipping the initial unlock screen.

> [!TIP] Require verification for browser integration
> To ask for fingerprint verification every time the integration between the desktop app and browser extension is activated:
> 
> 1. Open the desktop app and go to **Bitwarden** → **Settings**.
> 2. Check **Require verification for browser integration**.
> 3. When turning on biometrics unlock in the browser extension, you’ll be asked to enter your fingerprint during setup.

## Set up biometrics for mobile

Unlock with biometrics is supported on iOS via [Touch ID](https://support.apple.com/en-us/HT201371) and [Face ID](https://support.apple.com/en-us/HT208109) and on Android (Google Play or FDroid) via [fingerprint unlock](https://support.google.com/nexus/answer/6285273?hl=en) or [face unlock](https://support.google.com/pixelphone/answer/9517039?hl=en).

> [!NOTE] Android Class Requirement
> On Android, Bitwarden requires your biometric factor to be [Class 3](https://source.android.com/docs/security/features/biometric). Fingerprint readers will most often be Class 3, however the class of facial recognition systems will vary based on device manufacturer and model

To set up unlock with biometrics for your mobile device:

1. Turn on the biometric method in your device’s system settings, like the **iOS Setting**s app.
2. Open the Bitwarden app and tap the ⚙️ **Settings** icon.
3. Tap **Account security**.
4. Tap **Unlock with Face ID** or **Unlock with Biometrics**. (What’s available is based on your device’s hardware capabilities and what you previously turned on in your device’s system settings.)
5. Enter your biometric when prompted, like your face or fingerprint. The toggle will fill in when unlock with biometrics is successfully set up.

## Use unlock with biometrics

### Windows & Linux Desktop

To access your vault with the Windows or Linux desktop app:

1. Log in with a master password or PIN.
2. Select **Unlock with Windows Hello** or **Unlock with system authentication**:

![Unlock with Windows Hello](https://bitwarden.com/assets/7n73BtZuBKI2lrmTMGJUqk/cf42eacad0651a4cf1b12ba786a2f362/Windows_Hello.png)
3. Enter the biometric you configured.

> [!NOTE] Biometrics greyed out
> When you first open or restart the Windows and Linux desktop apps, the biometrics option will be greyed out. Unlock the vault with your standard method, like the master password or PIN. After that first log in and unlock, you can use biometrics to unlock your vault.

### macOS Desktop

If you checked **Ask for Touch ID on app start** during setup, you’ll immediately be prompted to enter your Touch ID.

If you did not check **Ask for Touch ID** on app start during setup:

1. Log in with a master password or PIN.
2. Select **Unlock with Touch ID**:

![Unlock with Touch ID](https://bitwarden.com/assets/2c5pB6gzPsvqDA46W2cODn/46c5bad230d8a5deb7f31e2861bdae0d/Unlock_with_Touch_ID.png)
3. Enter your Touch ID.

### Browser extension

To access your vault with the browser extension:

1. Log in to the Bitwarden desktop app and unlock your vault.
2. With the desktop app still running in the background, open the Bitwarden browser extension.
3. (Optional) If you previously turned on **Require verification for browser integration** in the desktop app, enter your fingerprint when prompted.
4. Depending on if **Ask for biometrics on launch** was checked in the desktop app during setup:

 - If this setting was checked, you’ll immediately be prompted to enter your biometric.
 - If this setting **was not**checked, select **Unlock with biometrics** and enter the biometric you configured:

![Unlock with biometrics browser](https://bitwarden.com/assets/4UeYGO9saN15Jg3xLQmv5y/bfdb5e552b33009d219b1c1b7accd26b/Unlock_with_Biometrics_Browser.png)

> [!NOTE] "Action was cancelled by the desktop application" browser error
> If an “Action was cancelled by the desktop application” error appears, confirm that:
> 
> - Your [desktop app is compatible](https://bitwarden.com/help/biometrics/#set-up-biometrics-for-desktop-app/), such as installed from the Mac App Store.
> - The desktop app is open and you’re logged in.
> - Biometrics are set up for your desktop app before turning them on in the browser extension.
> - If you’re on macOS, shorten your username if it causes your directory path (e.g.` /Users/your_username/Library/...`) to be over 104 characters.

### Mobile

When the Bitwarden mobile app first opens, enter your fingerprint or face ID when prompted.

## Troubleshooting

If a “Biometric unlock disabled pending verification of your master password” error appears:

1. Temporarily turn off autofill in Bitwarden.
2. Follow the steps above to set up biometrics in Bitwarden.
3. Turn autofill back on within Bitwarden.
