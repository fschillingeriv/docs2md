---
URL: https://bitwarden.com/help/duckduckgo-m%61cos-browser-integration/
---

# DuckDuckGo macOS Browser Integration

> [!TIP] Use DDG download, not app store
> In order to use the DuckDuckGo macOS app integration with Bitwarden, you'll need to download the DuckDuckGo macOS browser from [https://duckduckgo.com/mac](https://duckduckgo.com/mac) instead of from the macOS App Store.

Bitwarden and DuckDuckGo have partnered to offer Bitwarden functionality inside the DuckDuckGo macOS browser! The integration allows for seamless autofilling, creating, and updating of credentials in your Bitwarden vault while using login forms in DuckDuckGo:

![Bitwarden in DuckDuckGo](https://bitwarden.com/assets/4bfRWX1qSH0NK9HG2bBDTb/bfe35d198efed114e64ef1b97d6f9508/ddg_macos.png)

The integration requires the Bitwarden [desktop app](https://bitwarden.com/help/getting-started-desktop/) to be installed on your machine and unlocked in order to access vault items from DuckDuckGo. 

## Set up the integration

To set up the integration between the DuckDuckGo macOS browser and Bitwarden:

1. Open DuckDuckGo's **Settings**screen and select **Passwords & Autofill**from the menu.
2. In the Password Manager section, select **Bitwarden**. A wizard will help you through integration setup, but we'll outline the remaining steps here as well.
3. Install the Bitwarden desktop app if it isn't already on your machine.
4. Open the Bitwarden desktop app and log in or unlock your vault.
5. Select **Bitwarden > Settings**from the macOS menu bar.
6. Scroll to find the **App Settings (All Accounts)** section.
7. Check **Allow DuckDuckGo browser integration**.
8. In DuckDuckGo select **Connect** when the browser detects Bitwarden is ready.
9. In Bitwarden, select **Yes**to approve DuckDuckGo's request to connect.

> [!TIP] DDG Integration Vault Status
> Once Bitwarden is connected, you can return to the **Settings** > **Autofill** page in DuckDuckGo to see the current status of the integration (for example, whether you need to unlock Bitwarden to autofill, create, or update credentials).

## Use the integration

### Autofill credentials

To autofill credentials from Bitwarden, select login form input boxes. If credentials are detected, they'll be offered for autofill:

![DuckDuckGo Auto-fill](https://bitwarden.com/assets/34RVEdeI6m5IiMXxEBmYJb/5fa66cccef09aed7ef03011a522ad3a3/Screen_Shot_2022-11-14_at_9.25.24_AM.png)

### Add or update credentials

If a set of credentials you use is not detected in or different from what's stored in Bitwarden, you'll be prompted to add or update:

![DuckDuckGo Add or Update](https://bitwarden.com/assets/4YmcbgoaQ92Lhj2wBS8g0R/f74b7ead6f4711cf6a3dac46d73b3f71/ddg_macos_copy.png)
