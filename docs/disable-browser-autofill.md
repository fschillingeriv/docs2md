---
URL: https://bitwarden.com/help/disable-browser-autofill/
---

# Deactivate My Browser's Built-in Password Manager

If you're new to Bitwarden, your web browser likely saves and autofills your passwords. Most web browsers enable this by default, even though experts generally agree that [built-in password managers are more vulnerable](https://www.wired.com/2016/08/browser-password-manager-probably-isnt-enough/) than dedicated solutions like Bitwarden. We recommend making Bitwarden your browser's default password manager to improve your security and prevent interference with Bitwarden.

> [!NOTE] Deploying Browser across organization
> The Bitwarden browser extension can be deployed across managed endpoints. Learn more about [deploying the Bitwarden browser extension to managed devices](https://bitwarden.com/help/browserext-deploy/).

## When you install Bitwarden

When you install Bitwarden for the first time, you'll be prompted to make Bitwarden your default password manager:

![Make Bitwarden your default](https://bitwarden.com/assets/6EXjuiuhxjTCNoxlL9uZRq/513b2d10487c86d0ebed4cc050cbcfba/2026-07-14_14-56-41.png)
*Make Bitwarden your default*

Once you select **Continue**, a dialogue will appear on screen. Select **Allow** to give Bitwarden permission to make changes to your browser settings.

## From the Bitwarden settings menu

If you skipped the prompt during installation, the Bitwarden browser extension on some browsers has a built-in setting to make Bitwarden your default password manager:

1. Navigate to the ⚙️ **Settings** tab in the Bitwarden browser extension and then select **Autofill**.
2. Click to enable the **Make Bitwarden your default password manager**.

![Make Bitwarden your default](https://bitwarden.com/assets/5fyBdu5X6JCLu2UsaqYUO0/5cbd0a186251fe8916b5a01be1f3efb8/2026-07-14_14-59-21.png)
*Make Bitwarden your default*
3. A dialogue will appear on screen, select **Allow** to give Bitwarden permission to make changes to your browser settings.

## Manually from your browser settings

If neither of the above methods worked for you, manually deactivate your browser's built-in password manager from the browser settings menus:

> [!NOTE] Chromium instructions 
> Several modern browsers, like Opera and Brave, use a Google Chrome framework called "Chromium". If you are using one of those browsers, use the **Chrome/Chromium** instructions.

### Chrome/Chromium

In Chrome or any Chromium-based browser (for example, Opera or Brave), navigate to the **Passwords** page by entering `chrome://password-manager/settings` in the address bar, substituting `chrome` for your browser name (for example, `brave://password-manager/settings`). 

On this page, toggle off **Offer to save passwords and passkeys** and **Sign in automatically**:

![Turn off Chrome Password Manager](https://bitwarden.com/assets/278FMIhP9usz83Q8zlSZRs/34fc118d1a52fcba111b22f786ad00bf/Turn_off_Chrome_Password_Manager.png)
*Turn off Chrome Password Manager*

Then select **Passwords** to view any that are stored in the browser:

![Chrome Saved Passwords ](https://bitwarden.com/assets/4P5alfndwwNgCpTYrSCg61/bc1570211deec146aa51aa6f35f9fed2/View_passwords_saved_in_Chrome_Password_Manager.png)
*Chrome Saved Passwords *

If you haven't already saved these passwords in Bitwarden, [export them](https://bitwarden.com/help/import-from-chrome/#export-from-chrome/) to prepare for future import to Bitwarden. Once exported, we recommend deleting these passwords from the browser's storage.

### Edge

While Edge is a Chromium based browser, the steps will slightly differ. Navigate to `edge://wallet/settings`. On this page, select **Microsoft Password Manager**:

![Edge disable password](https://bitwarden.com/assets/6tRRYJbZ2xmQZ0ehL2xbvh/4c9c416b6e52c9bd1b3eaf9b75eaaca7/edge-disable-autosave.png)
*Edge disable password*

Then, set the toggle for **Ask to save password** and **Autofill passwords and passkeys**to **off**:

![Toggle save passwords](https://bitwarden.com/assets/3minVF9zEGs9SuGDSQ9FAE/4c3e66b91f7905a5f65ff164afbb3e01/edge_disable_all.png)
*Toggle save passwords*

### Firefox

In Firefox, navigate to **Settings** → **Passwords and autofill**. Scroll down and uncheck all pre-checked options in the **Passwords**, **Payment methods**, and **Addresses and more**sections:

![Firefox password options ](https://bitwarden.com/assets/72yK5CCMKa9pcfCcdvUZqL/70345d0065b2e093519bcb0dbf74ce86/firefox_update.png)
*Firefox password options *

> [!TIP] Bitwarden has more reporting than Firefox, duh.
> Bitwarden Password Manager offers a variety of [reports](https://bitwarden.com/help/reports/) for premium users, like the Exposed Passwords and Reused Passwords reports, and a **free Data Breach report for all users**.

You may also review any logins Firefox has already saved by selecting the **Saved Passwords** button:

![Firefox Saved Logins ](https://bitwarden.com/assets/5UrQ6bGCjV0VdHvy6rzece/fb1d2fc1bd28f1af3fdf4ad890039c84/firefox_update_2.png)
*Firefox Saved Logins *

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
