---
URL: https://bitwarden.com/help/disable-browser-autofill/
---

# Deactivate My Browser's Built-in Password Manager

If you're new to Bitwarden, your web browser likely saves and autofills your passwords. Most web browsers enable this by default, even though experts generally agree that [built-in password managers are more vulnerable](https://www.wired.com/2016/08/browser-password-manager-probably-isnt-enough/) than dedicated solutions like Bitwarden. We recommend turning off your browser's built-in password manager to improve your security and prevent interference with Bitwarden.

> [!NOTE] Deploying Browser across organization
> The Bitwarden browser extension can be deployed across managed endpoints. Learn more about [deploying the Bitwarden browser extension to managed devices](https://bitwarden.com/help/browserext-deploy/).

## Manually disable a browser's built-in password manager

Learn how to disable the built-in password manager for major browsers.

> [!NOTE] Chromium instructions 
> Several modern browsers, including Edge, Opera, and Brave, use a Google Chrome framework called "Chromium". If you are using one of those browsers, use the **Chrome/Chromium** instructions.

### Chrome/Chromium

In Chrome or any Chromium-based browser (Opera, and Brave), navigate to the **Passwords** page by entering `chrome://password-manager/settings` in the address bar, substituting `chrome` for your browser name (for example, `brave://password-manager/settings`). 

On this page, toggle off both the **Offer to save passwords** option and the **Auto Sign-in** option:

![Chrome Password Options ](https://bitwarden.com/assets/6bpi4fkyZhnkhW5RBtugDW/d8e2de4536d6a34f092fd9d5975fd04a/chrome-disable-autofill.png)
*Chrome Password Options *

This page will also list any **Saved Passwords** that are being stored by the browser:

![Chrome Saved Passwords ](https://bitwarden.com/assets/4P5alfndwwNgCpTYrSCg61/b3545839a8429f28ee7b6ac66559c3ce/chrome-delete-passwords.png)
*Chrome Saved Passwords *

If you haven't already saved these passwords in Bitwarden, [export them](https://bitwarden.com/help/import-from-chrome/#export-from-chrome/) to prepare for future import to Bitwarden. Once exported, you should delete these passwords from the browser's storage.

### Edge

While Edge is a Chromium based browser, the steps will slightly differ. Navigate to `edge://wallet/settings`. On this page, select **Microsoft Password Manager**:

![Edge disable password](https://bitwarden.com/assets/6tRRYJbZ2xmQZ0ehL2xbvh/4c9c416b6e52c9bd1b3eaf9b75eaaca7/edge-disable-autosave.png)
*Edge disable password*

Then, set the toggle for **Ask to save password** and **Autofill passwords and passkeys**to **off**:

![Toggle save passwords](https://bitwarden.com/assets/3minVF9zEGs9SuGDSQ9FAE/4c3e66b91f7905a5f65ff164afbb3e01/edge_disable_all.png)
*Toggle save passwords*

### Firefox

In Firefox, navigate to **Settings** → **Privacy & Security**. Scroll down and uncheck all pre-checked options in the **Passwords**, **Payment methods**, and **Addresses and more**sections:

![Firefox password options ](https://bitwarden.com/assets/72yK5CCMKa9pcfCcdvUZqL/95494d5079e32ae509ea62347ccc9ee8/Firefox_settings.png)
*Firefox password options *

> [!TIP] Bitwarden has more reporting than Firefox, duh.
> Bitwarden Password Manager offers a variety of [reports](https://bitwarden.com/help/reports/) for premium users, like the Exposed Passwords and Reused Passwords reports, and a **free Data Breach report for all users**.

You may also review any logins Firefox has already saved by selecting the **Saved Passwords** button:

![Firefox Saved Logins ](https://bitwarden.com/assets/5UrQ6bGCjV0VdHvy6rzece/a2148eaa8dcaaf4f7158e8d806dcb97b/2025-08-06_16-53-15.png)
*Firefox Saved Logins *

![Firefox Saved Logins ](https://bitwarden.com/assets/5UrQ6bGCjV0VdHvy6rzece/a2148eaa8dcaaf4f7158e8d806dcb97b/2025-08-06_16-53-15.png)

If you haven't already saved these passwords in Bitwarden, [export them](https://bitwarden.com/help/import-from-firefox/) for future import to Bitwarden. Once exported, you should 🗑️ **Remove** these passwords from Firefox.

### Safari

In Safari, open **Settings** from the menu bar and navigate to the **AutoFill** tab. On this tab, uncheck all the pre-checked options:

![Safari Password Options ](https://bitwarden.com/assets/4nuEz911vsIAUegHVL0Zec/7d663935c4f9e65297c14598f1037b72/safari-disable.png)
*Safari Password Options *

You should also find out which passwords Safari has already saved by navigating to the **Passwords** tab. If you have passwords saved, this tab will lead you to the Apple Passwords app.

![Safari Saved Passwords ](https://bitwarden.com/assets/6eZMZC98Grc7sbdHbBfXtK/4c72d19c26e56ad7dfb3267f466bd119/safari-delete.png)
*Safari Saved Passwords *

If you haven't already saved these passwords in Bitwarden, create login items in Bitwarden for these passwords. Once all saved passwords are in Bitwarden, **Remove** these passwords from Safari.

### Vivaldi

In Vivaldi, open the ⚙️ **Vivaldi Settings** window and select [eye] **Privacy** from the left-hand navigation. Scroll down to the Passwords section and uncheck the **Save Webpage Passwords** option:

![Vivaldi Password Options ](https://bitwarden.com/assets/6nk9FVDeg8XaUz22Xahr8T/ee0f597cc264da5a30853588d541f074/vivaldi-disable.png)
*Vivaldi Password Options *

You should also find out which passwords Vivaldi has already saved by selecting the **Show Saved Passwords** button:

![Vivaldi Saved Passwords ](https://bitwarden.com/assets/1j5qvcTAVsXficByKFewec/fd6f86731a9e15d38e0cbc39f4f64197/vivaldi-delete.png)
*Vivaldi Saved Passwords *

If you haven't already saved these passwords in Bitwarden, create login items in Bitwarden for these passwords. Once all saved passwords are in Bitwarden, remove these passwords from Vivaldi. [Learn how](https://help.vivaldi.com/desktop/privacy/password-management/#Deleting_passwords).

### Tor

Despite sharing roots with Firefox, Tor is unique in that it doesn't save your logins by default. If you haven't manually configured Tor to save and autofill logins, you are already all set.

If you did, navigate to the **Passwords** page by entering `about:preferences#privacy` in the address bar, and scroll down to the Logins and Passwords section. Toggle off all the options that you had checked:

![Tor Password Option ](https://bitwarden.com/assets/4FcJnbhCUhDNITJjiy9ciD/d0f83af69188afaf619788c7e60c9a1b/tor-disable.png)
*Tor Password Option *

You should also find out which logins Tor has already saved by selecting the **Saved Logins...** button:

![Tor Saved Passwords ](https://bitwarden.com/assets/3NHOIo5RIwTjVecqRPeT5Y/6c1e26dc5385006a498b77c48e1048c2/tor-delete.png)
*Tor Saved Passwords *

If you haven't already saved these passwords in Bitwarden, create login items in Bitwarden for these passwords. Once all saved passwords are in Bitwarden, 🗑️ **Remove** these passwords from Tor.

### DuckDuckGo

In DuckDuckGo, navigate to **Settings → Autofill**. From this screen, uncheck the box for **Usernames and passwords**.

![Disable DuckDuckGo Password Manager](https://bitwarden.com/assets/6kAbV4w8EiJX20O9VZOQyl/c6df545c4bc464122b250527b80494d3/Screenshot_2023-11-03_at_11.06.54_AM.png)
*Disable DuckDuckGo Password Manager*

You can create a backup of your existing data by selecting **Export Passwords**. Once you have created a backup file, select **View Autofill Content...**and delete the stored autofill data to remove previously saved suggestions. 

In the Password Manager section, macOS users can choose to use Bitwarden. Learn more about the Bitwarden DuckDuckGo macOS browser integration [here](https://bitwarden.com/help/duckduckgo-macos-browser-integration/).

## Make Bitwarden your default password manager in Chrome

> [!NOTE] Make Bitwarden default is exclusive to chrome
> The **Make Bitwarden your default password manager** option is only available for the Chrome and Edge browser extensions. For other browsers, [manually disable their built-in password manager](https://bitwarden.com/help/disable-browser-autofill/#manually-disable-a-browsers-built-in-password-manager/).

The Bitwarden browser extension on Chrome and Edge has a built-in setting to disable your browser's default password manager. To use this setting:

1. Navigate to the ⚙️ **settings** tab in the Bitwarden browser extension and then select **Autofill**.
2. Click to enable the **Make Bitwarden your default password manager**.

![Make Bitwarden default password manager](https://bitwarden.com/assets/5fyBdu5X6JCLu2UsaqYUO0/abfb44cb460314112805bfd0312c1f8f/2025-10-14_12-44-35.png)
*Make Bitwarden default password manager*
3. A dialogue will appear on screen, select **allow** to give Bitwarden permission to make changes to your browser settings.
