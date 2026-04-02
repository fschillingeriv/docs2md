---
URL: https://bitwarden.com/help/product-faqs/
---

# Password Manager FAQs

This article contains frequently asked questions (FAQs) about general Bitwarden Password Manager functionality. 

## Most asked questions

### Q: What do I do if I forgot my master password?

**A:** As a zero-knowledge encryption solution, Bitwarden and its systems have no knowledge of, way to retrieve, or way to reset your master password. If you have already lost your master password, there is unfortunately no way for the team to recover the account. For help understanding what to do next, or what to do proactively to protect yourself from such a scenario, refer to the article on [your master password](https://bitwarden.com/help/master-password/).

### Q: Is there a way for someone to access my vault items in case of emergency?

**A:** There is! Users with a premium subscription can proactively setup trusted emergency contacts who can access your vault in case of emergency. For more information, see [Emergency Access](https://bitwarden.com/help/emergency-access/).

### Q: How do I change my master password hint?

**A:** To change your master password hint:

1. In the web app, navigate to **Settings** → **Security** → **Master password**.
2. To change your hint, you must create a new master password. Enter your **Current master password**, then fill out the **New master password** and **Confirm master password** fields. Enter your new hint in the **Master password hint** box.
3. Select the **Change master password**button.

### Q: How do I change my email address?

> [!NOTE] Changing Email vs. Changing 2FA Email
> Changing your account email address will not change the address that received 2FA codes if you are using [two-step login via email](https://bitwarden.com/help/setup-two-step-login-email/).

**A:** To change the email address attached to your account:

1. In the web app, navigate to **Settings** → **My account**.
2. On the **My Account** page, find the **Change email** section.
3. Enter your current **Master password** to prove you have the authority to take this action, and specify the **New email** you'd like to change to.
4. Select the **Continue** button.

Bitwarden will email a verification code to the specified email address. Check your inbox for the code and enter it into the **Code** text input displayed in your web vault to finalize the change. If you don't receive the verification code, check your spam folder. You can also whitelist `no-reply@bitwarden.com` to help ensure delivery in the future.

When you change your email address, you should immediately logout of all Bitwarden apps you use, and log back in with the new credentials. Sessions using a "stale" email address will eventually be logged out.

### Q: What features are unlocked when I verify my email?

**A**: When you verify your email address, you'll unlock the ability to [create file Sends](https://bitwarden.com/help/create-send/) (provided you also have access to premium features).

### Q: Why is a vault item missing from my mobile app, desktop app, or browser extension?

**A:** Typically, this is because an app's vault data has fallen behind a web vault or other app's. Performing a vault sync should bring everything up to date. For more information, see [Sync your Vault](https://bitwarden.com/help/vault-sync/).

### Q: What's the safest way to make a backup of my vault data?

**A:** You can use [encrypted exports](https://bitwarden.com/help/encrypted-export/#create-an-encrypted-export/) to make secure long-term backups of your vault data that are encrypted with your account encryption key, organization encryption key, or with a password of your choosing.

### Q: Can I set Bitwarden to automatically start when my computer starts?

**A:** Yes, toggle the **Start automatically on login** setting on in the Bitwarden desktop app in order to have it automatically launch when you login to your computer.

### Q: Why am I getting a ‘New Device’ email?

**A:** Typically this occurs for users that have a setting on their browser which clears their local storage and/or cookies whenever they close the browser or while they are using the browser. There are extensions that perform these actions. If this happens, you lose the indicator which tells our servers that it is an existing device. New device notification messages are not contingent on the IP address, only the device itself. We use local storage in the browser or client to label the device with an id. If that id has never logged in before then you will get an email. If a user clears this local storage, a new id is generated for that device and it will get a new email.

You may need to make an exception for Bitwarden or configure your whitelist to keep the cookie or local storage from being cleared for Bitwarden. This could also happen if you have your browser set to never remember history.

## Other questions

### Q: Can I install Bitwarden without Google Play, for instance on F-Droid?

**A:** Yes! You can download directly from GitHub [https://github.com/bitwarden/android/releases](https://github.com/bitwarden/android/releases/) or via F-Droid by adding our repo [https://github.com/bitwarden/f-droid](https://github.com/bitwarden/f-droid), which removes all non-approved libraries.

Unfortunately, F-Droid can not compile our app from source as it is based on Xamarin and it is not supported by F-Droid's current compiler methods, so we must use a separate repo.

### Q: Can I turn off automatic updates for Bitwarden?

**A:** Yes! On Windows, you can add the environment variable `ELECTRON_NO_UPDATER=1` to your desktop app template to prevent automatic update procedures from trying and failing on your end-user workstations.

> [!WARNING] Running older versions.
> Like with any software, running old versions may present a security risk.

### Q: How do I get logs for the desktop app?

**A**: Add the environment variable `ELECTRON_ENABLE_LOGGING=true` to your desktop app template to print logs from the desktop app to the console, or start the desktop app from your console and use command line switches to write logs to a file:

- (Windows) `Bitwarden.exe --enable-logging=file --log-file=bitwarden.log`
- (macOS) `./Bitwarden.app/Contents/MacOS/Bitwarden --enable-logging=file --log-file=bitwarden.log`

### Q: What happens when I purge my vault?

**A:** When you purge an **individual vault**, all vault items and folders will be deleted. When you purge an **organization vault**, all shared (for example owned by the organization) vault items will be deleted however existing users, collections, and groups will remain in place. To purge your vault:

### Individual vault

> [!WARNING] Purging your vault
> Purging your vault is permanent. It cannot be undone.

To purge your individual vault:

1. In the Bitwarden web app, navigate to **Settings** → **My account**.
2. In the Danger zone section, select **Purge vault**. You'll need to confirm your master password to complete a purge.

### Organization vault

> [!WARNING] Purging your vault
> Purging your vault is permanent. It cannot be undone.

To purge an organization vault you must be an [organization owner](https://bitwarden.com/help/user-types-access-control/):

1. In the Bitwarden web app, open the Admin Console and navigate to **Settings** → **Organization info**.
2. In the Danger zone section, select **Purge vault**. You'll need to confirm your master password to complete a purge.

### Q: Can I print my vault data?

**A:** Not directly from Bitwarden, however you can [export your vault data](https://bitwarden.com/help/export-your-data/) as a `.csv` or `.json` file and print it out from your text editor.

### Q: Can I prevent my credentials from being saved to the clipboard? 

**A:** Yes! To automatically clear values copied from Bitwarden from the clipboard:

- In your browser extension, navigate to **Settings** → **Autofill** and set **Clear clipboard**to a value other than **Never**.
- In your mobile app, navigate to **Settings** → **Other** and set **Clear clipboard**to a value other than **Never**.
- In your desktop app, navigate to **Settings**and in the **Preferences**section set **Clear clipboard**to a value other than **Never**.

### Q: Does uninstalling or deleting my Bitwarden app also delete my vault data?

**A:** No, deleting a Bitwarden app/extension will not delete your vault data. Vault data will remain encrypted on the server. If you wish to **permanently** delete your vault data, see [Delete an Account or Organization](https://bitwarden.com/help/delete-your-account/).

### Q: Does Bitwarden manage in-browser browser extensions on Android mobile?

**A:** There are Bitwarden browser extension available in the Firefox and Edge browsers on Android mobile devices. However, these extensions are not officially supported by Bitwarden, and the team is aware that some functionality in this client is known to not work correctly. Android users may prefer to use the Bitwarden [mobile app](https://bitwarden.com/help/getting-started-mobile/) for an officially supported password manager client.

### Q: Does Bitwarden have any settings that can be adjusted for graphics or performance?

**A:** Yes, Bitwarden does include settings in the desktop app to adjust for system performance:

- Graphical (GPU) acceleration can be disabled in two ways on Bitwarden desktop apps:

 - Navigate to **Settings** → **APP SETTINGS (ALL ACCOUNTS)** and uncheck the box labeled **Use hardware acceleration**.
 - From the navigation bar, **Help** → **Troubleshooting** → **Disable hardware acceleration and restart**.

### Q: Can Bitwarden be installed in an Android private space?

**A**: Currently, Bitwarden does not recommend installing the Android application in a private space (15.0+) as private spaces are not suitable for apps that need to run in the background for functions like autofill and syncing.
