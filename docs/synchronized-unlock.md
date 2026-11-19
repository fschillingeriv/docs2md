---
URL: https://bitwarden.com/help/synchronized-unlock/
---

# Synchronized Unlock

Synchronized unlock connects the lock state of the Bitwarden web app, browser extension, and desktop app on the same device. When you lock or unlock one connected app, the others will lock or unlock too.

> [!NOTE] Sync unlock version requirement
> Synchronized unlock requires version 2026.11.0 or later of the browser extension, desktop app, and web app.

## Activate synchronized unlock

Synchronized unlock between the browser extension and the web app is **always on**. To also sync with the desktop app:

1. Make sure the Bitwarden desktop app is installed, running, and logged in to the same account as the browser extension.
2. In the browser extension, select **Settings** → **Account security**.
3. Turn on **Synchronize unlock with desktop**:

![Activate synchronized unlock](https://bitwarden.com/assets/5uoOeDjt0aLoFxbYUEOin2/09a633499b6e43959e63ee6d15170e1c/2026-11-12_15-41-42.png)
*Activate synchronized unlock*
4. If your browser asks for permission for Bitwarden to communicate with cooperating native applications, select **Allow**.

The desktop app must be running for synchronized unlock to work. Open the desktop app's settings and activate the **Start automatically on login** to make this more seamless.

## How it works

### Connecting between apps

Synchronized unlock shares **unlock state**, not login, so you need to log in to each app first. Apps connect in pairs:

- The browser extension and the web app, when open in the same browser.
- The browser extension and the desktop app.

> [!NOTE] Sync unlock applies to the same computer
> Synchronized unlock only applies to apps on the same computer. Mobile apps do not share trust or unlock state with apps on your computer.

The web app and desktop app don't connect directly, but stay in sync through the browser extension. Because connections chain together, every connected app on your computer shares one lock state. 

![Sync unlock flow diagram](https://bitwarden.com/assets/2BKjHAbQMYbRSjudxQSJGu/cf30bf16ad4c23837b36441e514d7cec/shared-unlock-diagram.svg)
*Sync unlock flow diagram*

Sync unlock works between apps logged in to the same account. If you're logged in to multiple accounts, each account syncs separately.

### Supported apps

Synchronized unlock is supported on Windows, macOS, and Linux:

| Browser | Sync with desktop app | Sync with web app |
|------|------|------|
| Chrome | Yes | Yes |
| Edge | Yes | Yes |
| Safari | No | No |

The following platforms are not currently supported:

- Browsers installed as a Snap on Linux
- The desktop app, when installed from the Microsoft Store
- Safari
- The Bitwarden CLI
- Mobile apps

### Impact on other settings

#### Biometrics

Synchronized unlock replaces the browser extension's biometric unlock setting. If **Synchronize unlock with desktop** is on and **Unlock with biometrics** is turned on in the desktop app, you can use biometrics to unlock the browser extension too. For more information, see [Unlock with Biometrics](https://bitwarden.com/help/biometrics/).

#### PIN

PINs are not shared between apps, so each app retains its own PIN. Unlocking any app with its PIN unlocks all connected apps.

#### Session timeout

If synchronized unlock is on, one app's session timeout applies to all connected apps, and the timeout setting in the other apps isn't available:

- When the browser extension and web app are connected, the browser extension's timeout applies.
- When the browser extension and desktop app are connected, the desktop app's timeout applies. This also lets the **On system lock** option apply to the browser extension and web app.

For more information, see [Automatic Logout or Lock](https://bitwarden.com/help/vault-timeout/).
