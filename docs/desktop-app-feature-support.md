---
URL: https://bitwarden.com/help/desktop-app-feature-support/
---

# Desktop App Feature Support

The Bitwarden desktop app is available for Windows, macOS, and Linux through a variety of channels, or installation methods, however each channel may offer different functionality. This article defines which features are available through which channels, and can be used to help you decide which method you'd like to use to install the desktop app:

> [!TIP] Features descriptions are below.
> Jump to the bottom of this page for [descriptions of each of the features](https://bitwarden.com/help/desktop-app-feature-support/#feature-descriptions/) listed in these tables.

## Operating systems

### Windows

| Feature | [Installer (.exe)](https://bitwarden.com/download/#downloads-desktop-applications/) | [Microsoft Store](https://apps.microsoft.com/detail/9pjsdv0vpk04?hl=en-US&gl=US) | [Portable App (.exe)](https://bitwarden.com/download/#downloads-desktop-applications/) |
|------|------|------|------|
| Automatic Updates | ✓ | ✓ | |
| Desktop Biometrics | ✓ | | ✓ |
| Extension Biometrics | ✓ | | ✓ |
| Integration with OS | ✓ | ✓ | ✓ |
| Startup on Launch | ✓ | | ✓ |
| Direct Importer | ✓ | | |
| Secure Storage | ✓ | ✓ | |
| Process Isolation | ✓ | ✓ | |

### macOS

| Feature | [Installer (.dmg)](https://bitwarden.com/download/#downloads-desktop-applications/) | [App Store](https://apps.apple.com/us/app/bitwarden/id1352778147?mt=12) |
|------|------|------|
| Automatic Updates | ✓ | ✓ |
| Desktop Biometrics | | ✓ |
| Extension Biometrics | | ✓ |
| Integration with OS | ✓ | ✓ |
| Startup on Launch | ✓ | ✓ |
| Direct Importer | ✓ | |
| Secure Storage | ✓ | ✓ |
| Process Isolation | ✓ | ✓ |

### Linux

| Feature | [AppImage](https://bitwarden.com/download/#downloads-desktop-applications/) | [Snap](https://snapcraft.io/bitwarden) | [Flatpak](https://flathub.org/apps/com.bitwarden.desktop) | [.deb](https://bitwarden.com/download/#downloads-desktop-applications/) | [.rpm](https://bitwarden.com/download/#downloads-desktop-applications/) |
|------|------|------|------|------|------|
| Automatic Updates | * | ✓ | ✓ | | |
| Desktop Biometrics | ✓ | ✓ | ** | ✓ | ✓ |
| Extension Biometrics | ✓ | | | ✓ | ✓ |
| Integration with OS | * | ✓ | ✓ | ✓ | ✓ |
| Startup on Launch | | ✓ | ✓ | ✓ | ✓ |
| Direct Importer | ✓ | | | | |
| Secure Storage | ✓ | *** | *** | *** | *** |
| Process Isolation | **** | | ✓ | **** | **** |

* - Can be set up with applications like AppImageLauncher.

** - Requires manual installation of [this policy](https://github.com/bitwarden/clients/blob/main/apps/desktop/resources/com.bitwarden.desktop.policy) via Polkit.

*** - Requires `libsecret` to be installed.

**** - Only the `main` process is isolated.

## Feature descriptions

| Feature | Description |
|------|------|
| Automatic Updates | The desktop app will automatically update to the newest version when one is available. |
| Desktop Biometrics | The desktop app can be unlocked with biometrics. |
| Integration with OS | The desktop app will automatically integrate with your desktop for features like desktop shortcuts and application shortcuts. |
| Startup on Launch | The desktop app can be set to automatically startup on the launch of your device. |
| Extension Biometrics | The desktop app can be used to unlock a browser extension with biometrics. |
| Direct Importer | The desktop app can be used to directly import data from a supported web browser's credential manager (e.g. Google Password Manager). |
| Secure Storage | The desktop app will store access tokens and biometric unlock data securely according to OS methodologies: - On Windows, Windows Credential Manager. - On macOS, Keychain. - On Linux, `libsecret`. |
| Process Isolation | The desktop app separates components into different sandboxed processes, so that if one component is compromised, attackers cannot easily access sensitive data like encryption keys or system resources in the other processes. |
