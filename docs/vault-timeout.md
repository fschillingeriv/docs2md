---
URL: https://bitwarden.com/help/vault-timeout/
---

# Automatic Logout or Lock

Session timeout options determine whether Password Manager vault will automatically log out or lock after a specified period of inactivity. When configuring your vault timeout settings, you can set the [timeout](https://bitwarden.com/help/vault-timeout/#session-timeout/) and [timeout action](https://bitwarden.com/help/vault-timeout/#session-timeout-action/).

To set your timeout behavior:

### Web app

Navigate to **Settings**→ **Security** to choose your session timeout and session timeout action.

### Browser extension

Navigate to **Settings**→ **Account security** to choose your session timeout and session timeout action.

### Mobile

Navigate to **Settings**→ **Account security** to choose your session timeout and session timeout action.

### Desktop

- On macOS, navigate to **Bitwarden**→ **Settings** to choose your session timeout and session timeout action.
- On Windows or Linux, navigate to **File** → **Settings** to choose your session timeout and session timeout action.

> [!NOTE] Closing Desktop will lock/lockout app
> Closing the desktop app will cause the vault to lock or log out, depending on your chosen timeout action.

> [!TIP] Vault Timeout with Account Switching
> If you're [logged in to multiple accounts](https://bitwarden.com/help/account-switching/) in your Bitwarden app, the session timeout and the timeout action are set on an account-by-account basis.

## Session timeout

Session timeout, also called vault timeout, determines how long Bitwarden can be inactive before timing out. Inactivity is measured by time since interacting with Bitwarden—not system idle time.

Timeout options vary by app. If there are fewer timeout options than expected and you're part of an Enterprise organization, they may have turned on the [session timeout policy](https://bitwarden.com/help/policies/#session-timeout/).

### Web app

Select when your Bitwarden session times out:

- **Time passed**: After the time interval you chose, like **5 minutes** or **1 hour**
- **On browser refresh**: When you refresh the browser window where Bitwarden is open
- **Custom**: After the amount of time entered in **Hours** and **Minutes**

> [!NOTE] Unique timeout scenarios web and browser
> Because the web app and browser extensions depend on your web browser, there are unique timeout scenarios to consider:
> 
> - **If you refresh your browser** (`CMD/CTRL + R`), the web app will lock. Refreshing will not affect a browser extension.
> - **If you close your browser tab**, you will be logged out of your web app vault. Closing a single tab will not affect the browser extension.
> - **If you close your browser window**, you will be logged out of your web app and your browser extension will timeout.
> 
> - By default, your browser extension will require you to login or unlock with your master password based on your selected vault timeout action.
> - To instead unlock with a PIN after closing your browser window, uncheck **Lock with master password on browser restart**option when [setting up the PIN](https://bitwarden.com/help/unlock-with-pin/).

### Browser extension

Select when your Bitwarden session times out. Available options may differ by browser and may include:

- **Immediately**: When the user stops interacting with Bitwarden
- **Time passed**: After the time interval you chose, like **5 minutes** or **1 hour**
- **On system lock**: When the device is locked or the screensaver activates
- **On browser restart**: When you first open or restart the browser where Bitwarden is open

> [!NOTE] Timeout on Chromebook, Firefox, and Edge
> Some browsers will treat the **On browser restart** option differently: 
> 
> - On Chromebooks, there is no way to fully close or restart the browser. Therefore, the **On browser restart** option will only lock the extension when you restart your device.
> - In Firefox browsers installed via snap, closing the application does not stop all processes. Therefore, the **On browser restart** option will only lock the extension when you restart your device.
> - For Microsoft Edge users, browser restart does not take place when closing the browser. In order for Bitwarden Vault Timeout to occur On browser restart, two Microsoft Edge settings must be turned off:
> 
> 1. **Startup Boost**
> 2. **Continue to run background extensions and applications after Microsoft Edge is closed**
- **Never**: Your session doesn't time out.

> [!WARNING] Never timeout
> The **Never** timeout option stores your encryption key unencrypted on your device, which may hinder security. To keep your data secure, we strongly recommend choosing a different option.
- **Custom**: After the amount of time entered in **Hours** and **Minutes**

Browser extensions will not observe your chosen time-out settings when popped-out.

> [!NOTE] Unique timeout scenarios web and browser
> Because the web app and browser extensions depend on your web browser, there are unique timeout scenarios to consider:
> 
> - **If you refresh your browser** (`CMD/CTRL + R`), the web app will lock. Refreshing will not affect a browser extension.
> - **If you close your browser tab**, you will be logged out of your web app vault. Closing a single tab will not affect the browser extension.
> - **If you close your browser window**, you will be logged out of your web app and your browser extension will timeout.
> 
> - By default, your browser extension will require you to login or unlock with your master password based on your selected vault timeout action.
> - To instead unlock with a PIN after closing your browser window, uncheck **Lock with master password on browser restart**option when [setting up the PIN](https://bitwarden.com/help/unlock-with-pin/).

### Mobile

Select when your Bitwarden session times out:

- **Immediately**: When the user stops interacting with Bitwarden
- **Time passed**: After the time interval you chose, like **5 minutes** or **1 hour**
- **On app restart**: When you first open or restart the Bitwarden app
- **Never**: Your session doesn't time out.

> [!WARNING] Never timeout
> The **Never** timeout option stores your encryption key unencrypted on your device, which may hinder security. To keep your data secure, we strongly recommend choosing a different option.
- **Custom**: After the amount of time entered in **Hours** and **Minutes**

### Desktop

Select when your Bitwarden session times out:

- **Time passed**: After the time interval you chose, like **5 minutes** or **1 hour**
- **On system idle**: When your device has been inactive for a set time but hasn't entered sleep mode
- **On system sleep**: When your device goes to sleep
- **On system lock**: When the device is locked or the screensaver activates
- **On restart**: When your device is first turned on or restarted
- **Never**: Your session doesn't time out.

> [!WARNING] Never timeout
> The **Never** timeout option stores your encryption key unencrypted on your device, which may hinder security. To keep your data secure, we strongly recommend choosing a different option.
- **Custom**: After the amount of time entered in **Hours** and **Minutes**

## Session timeout action

This option determines what Bitwarden will do once your [session times out](https://bitwarden.com/help/vault-timeout/#session-timeout/). Options include:

- **Lock** (default)

Locking your vault will maintain vault data on the device, so unlocking your vault can be done offline. You will be required to enter your [master password](https://bitwarden.com/help/master-password/) or [PIN](https://bitwarden.com/help/unlock-with-pin/), or use [biometrics](https://bitwarden.com/help/biometrics/), but won't need to use any active two-step login methods.
- **Log out**

Logging out of your vault completely removes all vault data from your device. Logging back in will require you to re-authenticate your identity, so logging in can only be done when online. You will be required to enter your [master password](https://bitwarden.com/help/master-password/) and any active [two-step login](https://bitwarden.com/help/setup-two-step-login/) method.

### Trusted devices

If you use [trusted devices](https://bitwarden.com/help/about-trusted-devices/), you must enable [biometrics](https://bitwarden.com/help/biometrics/) or a [PIN](https://bitwarden.com/help/unlock-with-pin/) to unlock your vault. If biometrics or a PIN is not enabled, a session timeout will always log out instead of locking.

Unlocking and logging in with trusted devices **always**require an internet connection.
