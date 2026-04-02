---
URL: https://bitwarden.com/help/getting-started-browserext/
---

# Password Manager Browser Extensions

Bitwarden browser extensions integrate password management directly into your favorite browser. Download a Bitwarden browser extension from your browser's marketplace or app store, or from the [Bitwarden Downloads](https://bitwarden.com/download/) page.

> [!TIP] Safari Extension
> The Safari browser extension is packaged with the desktop app, available for download from the macOS App Store. [Learn more](https://bitwarden.com/help/install-safari-app-extension/).

## First steps

Let's start your Bitwarden browser extension journey by adding a new login item to your vault:

### Add a login

To create a new login item:

1. Navigate to the 🔒 **Vault**tab and select the + **New**icon.
2. Choose which type of item to create (in this case, select **Login**).
3. Enter the basic information for this login. For now, give the item:

 - An **Item name**to help you easily recognize it (for example, Instagram `Account`).
 - Your **Username**.
 - Your current **Password**(we will replace this with a stronger password soon).
4. You may select a folder from the [Folders](https://bitwarden.com/help/folders/) dropdown. 

> [!TIP] Selecting Owner if creating an item for an org (browser extension).
> If you're using Bitwarden in your workplace, you can use the **Owner**dropdown to create this item within your [organization](https://bitwarden.com/help/about-organizations/) instead of in your individual vault.
5. In the **Website (URI)**field, enter the URL where you log in to the account (for example, `https://instagram.com/login`).
6. Nice work! Select **Save**to continue.

### Generate a strong password

Now that you have saved a new login, let's improve its security by replacing your password with a stronger one:

1. In your web browser, login to the account with your existing username and password. We're going to be replacing your existing password with a stronger one, but this is a great opportunity to practice autofill!

To autofill, open the Bitwarden browser extension while you're on the website's login page and, in the 🔒 **Vault**tab, select the **Fill** button for the suggested item:

![Autofill via browser extension](https://bitwarden.com/assets/1pamjhdWn7obh8UBxXcIPF/1841242fa5299a780d53f3ae70e546b3/screenshot_5.png)
*Autofill via browser extension*
2. Once logged in, find where you can change your password.
3. On the website's change password form, enter your **Current Password**, which you can copy and paste from Bitwarden using the [clone] **Copy**icon:

![Copy a password](https://bitwarden.com/assets/40l7cU1a0jzaTNUJXd5jPD/97b9ed67c0b255384ce84fa53fad2015/screenshot_2.png)
*Copy a password*
4. Once your old password is filled in, open the login item in Bitwarden and select **Edit**.
5. In the **Password** box, select [generate] **Generate**and tweak your password settings to your liking. You can use to [generate] icon until you get a password you like and, once you do, select **Use this password**. Moving from `Fido1234` to `X@Ln@x9J@&u@5n##B` can stop a hacker in their tracks.
6. Select **Save**.
7. Copy your new password and paste it into the New Password and Confirm Password fields back on the website.

Congratulations! Your login is now saved in Bitwarden for secure and easy use!

### Pin the extension

Pinning the browser extension will ensure that it's easily accessible each time you open your browser. The procedure differs based on which browser you are using:

### Chrome

Select the [puzzle] **Extensions**icon next to the address bar and select the **Pin**icon next to Bitwarden:

![Pin in Chrome](https://bitwarden.com/assets/4cwP0QDHWh01v1K8nMV0ma/88b4b36c5b3e9d1fccffe7552880c485/chrome_pin.png)
*Pin in Chrome*

### Firefox

Select the [puzzle] **Extensions**icon next to the address bar , right-click the Bitwarden browser extension, and choose **Pin to Toolbar:**

![Pin on Firefox](https://bitwarden.com/assets/2O0RQxs4fr6tTKBAMOQcGy/a54ea16b59f933a209db9458c92358e6/firefox_pin.png)
*Pin on Firefox*

You can also activate a persistent Bitwarden sidebar by selecting **View** → **Sidebar** → **Bitwarden** from the Firefox menu.

> [!NOTE] Disable Bitwarden sidebar
> If you do not want the Bitwarden sidebar to open on browser startup, select **Close Sidebar** from the Bitwarden tab on the Firefox sidebar. Users may be required to select **Close Sidebar** on each active Firefox tab and restart Firefox.

### Safari

Right-click anywhere in the tool bar and select **Customize Toolbar**to open a drag-and-drop interface that lets you move or remove icons in your toolbar:

![Pin in Safari](https://bitwarden.com/assets/3mD3G3rNMEUu24XBh6a3Kt/5217730380fe6ee6cd49f7c3820574ee/safari_pin.png)
*Pin in Safari*

## Add a second account

Do you have multiple Bitwarden accounts, perhaps one for personal use and one for work? The browser extension can be logged in to five accounts at once!

To login to an additional account, select the currently logged-in account from the top-right corner of the browser extension:

![Browser extension account switching](https://bitwarden.com/assets/7xbbMZ89zcTHz6ee0cA1MK/8d8972a6b995b3fd7367f248c9c60d69/screenshot_3.png)
*Browser extension account switching*

Once you have opened the account switching menu, select + **Add account**:

![Browser extension Add account](https://bitwarden.com/assets/343trVk3zLCF7Z12uA5wjO/ac2f56fc907372335f30d1dbf68116a1/screenshot_4.png)
*Browser extension Add account*

Once you log in to your second account, you can quickly swap between them from the same menu, which will also show the current status of each account's vault (*locked or unlocked*). If you log out of one of these accounts, it will be removed from this list. 

> [!NOTE] Account switching not available on Safari
> Account switching on the browser extension is not available on Safari at this time.

## Next steps

Now that you have mastered the basics let's dig into one more action that you will take regularly, **Autofill** and **Auto-save**, and three recommended setup steps; easier vault **unlocking**, **pinning** the extension to your browser, and **disabling the browser's built-in** password manager:

### Disable a built-in password manager

Most web browsers will automatically save your passwords by default, but experts generally agree that [built-in password managers are more vulnerable](https://www.wired.com/2016/08/browser-password-manager-probably-isnt-enough/) than dedicated solutions such as Bitwarden. Learn more about [manually disabling a browser's built-in password manager](https://bitwarden.com/help/disable-browser-autofill/#manually-disable-a-browsers-built-in-password-manager/).

### Autofill a login

There are lots of ways to autofill credentials with Bitwarden browser extensions! The basic method is to open the Bitwarden browser extension while you're on the website's login page and, in the 🔒 **Vault**tab, select the **Fill** button for the suggested item:

![Autofill via browser extension](https://bitwarden.com/assets/1pamjhdWn7obh8UBxXcIPF/1841242fa5299a780d53f3ae70e546b3/screenshot_5.png)
*Autofill via browser extension*

Note that, when you have logins saved for a website you're trying to log in to, Bitwarden browser extensions will overlay a notification bubble reporting the number of logins you have for that website. Those items will appear at the top of your **Autofill suggestions.** You can filter what will appear in the suggestions and what's displayed in the **All items** list using the filter dropdown menus, which can be shown or hidden using the 🎚️ button:

![Browser extension filters and suggestions](https://bitwarden.com/assets/12UsFuA2sxbUCBMIczJsxv/689221013fac56ddb555ed9dabddbdc9/screenshot_6.png)
*Browser extension filters and suggestions*

There are plenty of other methods and ways of customizing autofill from your browser extension, including [context menus and keyboard shortcuts](https://bitwarden.com/help/auto-fill-browser/). Learn more.

### Autosave a login

Bitwarden browser extensions offer an array of [in-browser notifications](https://bitwarden.com/help/autosave-from-browser-extensions/) that compare your decrypted data with data that you enter into login, registration, and similar web forms.

When you see this banner, select **Save** to add a new or updated login item with the username, password, and URI. You can also choose to **Select folder...** for the item if it's new, or **Edit** the item before saving:

![Ask to add login](https://bitwarden.com/assets/4vsurEuH5deik26BWn4n1p/82757186b081890fbe92b4d73baeae53/screenshot_7.png)
*Ask to add login*

Learn more about [Autosave with the browser extension](https://bitwarden.com/help/autosave-from-browser-extensions/).

> [!NOTE] Passkeys on browser ext
> Did you know that you can save and autofill passkeys with the Bitwarden browser extension? Learn more about passkeys [here](https://bitwarden.com/help/storing-passkeys/).

### Unlock with PIN or biometrics

For fast access to your credentials, setup a [PIN](https://bitwarden.com/help/unlock-with-pin/) or [biometrics](https://bitwarden.com/help/biometrics/) to unlock your vault. To setup a PIN, for example:

1. Open the ⚙️ **Settings** tab.
2. In the **Account security** section, check the **Unlock with PIN** checkbox.
3. Enter the desired PIN code in the input box. PIN codes can be any combination of characters (a-z, 0-9, $, #, etc.)

> [!TIP] Ask for biometrics on launch
> **Optional:** The pre-checked option **Ask for biometrics on launch** will require you to enter your master password instead of a PIN when your browser restarts. If you want to be able to unlock with a PIN when you browser restarts, uncheck this option.

### Browser Pop-out

The Bitwarden browser extension has a pop-out feature that will allow you to reposition the client while using your internet browser. To pop-out the browser extension, select the icon shown in the following screenshot:

![Browser extension pop-out](https://bitwarden.com/assets/1cbJy0jLBmSQmRumvYzVwp/a9e43f4c154686249056924eb3e56323/pop_out_screenshot.png)
*Browser extension pop-out*

The browser extension will not observe your chosen [vault timeout](https://bitwarden.com/help/vault-timeout/) settings when popped-out.

#### Make Bitwarden your default password manager

The Bitwarden browser extension has a built-in setting to disable your browser's default password manager. To use this setting:

1. Navigate to the ⚙️ **settings** tab in the Bitwarden browser extension and then select **Autofill**.
2. Click to enable the **Make Bitwarden your default password manager**.

![Make Bitwarden default password manager](https://bitwarden.com/assets/5fyBdu5X6JCLu2UsaqYUO0/abfb44cb460314112805bfd0312c1f8f/2025-10-14_12-44-35.png)
*Make Bitwarden default password manager*
3. A dialogue will appear on screen, select **allow** to give Bitwarden permission to make changes to your browser settings.
