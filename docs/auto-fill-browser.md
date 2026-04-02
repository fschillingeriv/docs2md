---
URL: https://bitwarden.com/help/auto-fill-browser/
---

# Autofill from Browser Extension

Bitwarden makes logging in quick and secure with autofill. When you visit a website, the browser extension recognizes it and enters matching credentials from your vault into the login fields. Configure the autofill methods that you find most convenient.

> [!NOTE] Autofill for basic auth prompts
> [Basic authentication prompts](https://bitwarden.com/help/basic-auth-autofill/) work differently than the autofill methods described in this article.

## Set up autofill

First, all autofill methods with the browser extension require your login items to have an [assigned website URI](https://bitwarden.com/help/uri-match-detection/). This connects your saved credentials to the correct websites.

Next, the steps to configure and use autofill vary and are outlined in each method's description below.

Within the **Settings** → **Autofill** menu, some options apply to all or most autofill methods:

- For best performance, check **Make Bitwarden your default password manager** and [deactivate your browser's password manager](https://bitwarden.com/help/disable-browser-autofill/). This prevents the browser's password tool from interfering with the Bitwarden autofill.
- If you do not want a TOTP to be automatically copied when autofill is activated, uncheck [**Copy TOTP automatically**](https://bitwarden.com/help/auto-fill-browser/#totp-autofill/).
- From the **Clear clipboard** dropdown menu, select your preferred interval to control how long copied values from your vault remain available.
- Choose your**Default URI match detection**, the logic that Bitwarden uses to pair the website to your saved credential. The default, unless [specified by your organization](https://bitwarden.com/help/policies/#default-uri-match-detection/), is **Base domain**.
- Select and add [**Blocked domains**](https://bitwarden.com/help/blocking-uris/) to prevent autofilling on specific websites.

## Autofill methods in the browser extension

The most basic ways to autofill logins are by interacting with the Bitwarden browser extension. When you're on a website and at least one item's saved URI matches, the number of matching items for that website will appear on top of the Bitwarden extension icon.

> [!TIP] Disable badge counter
> To hide the matching items' total, go to ⚙️ **Settings** → **Appearance** and uncheck **Show number of login autofill suggestions on extension icon**.

Select the [shield] **Bitwarden extension badge** to open your vault, and the matching items will appear in the top **Autofill suggestions** section. If you want cards or identities included, go to **Settings** → **Autofill** and check **Always show cards as Autofill suggestions on Vault view**or **Always show identities as Autofill suggestions on Vault view**.

To find an item, select the 🎚️ **Filters icon** to open and apply filters to the **Autofill suggestions** and **All items** results:

![Browser extension filters and suggestions](https://bitwarden.com/assets/12UsFuA2sxbUCBMIczJsxv/689221013fac56ddb555ed9dabddbdc9/screenshot_6.png)
*Browser extension filters and suggestions*

### Fill button

To autofill a login:

1. When on the website's login page, open the Bitwarden browser extension.
2. Go to the **Vault** tab.
3. Select **Fill** next to the login to enter. It will likely be at the top in the **Autofill suggestions** section:

![Autofill via browser extension](https://bitwarden.com/assets/1pamjhdWn7obh8UBxXcIPF/1841242fa5299a780d53f3ae70e546b3/screenshot_5.png)
*Autofill via browser extension*

Selecting the **Fill**button will enter the credential to the detected input fields. In cases where a web page or service has multiple items with relevant URIs, Bitwarden will always autofill the last-used login.

> [!NOTE] Autofill on untrusted iframes and mismatched SSL
> You may receive a warning before autofilling if the targeted fields are in an [untrusted iframe](https://bitwarden.com/help/auto-fill-browser/#autofill-in-iframes/) or the current site uses HTTP but the [item's saved URI](https://bitwarden.com/help/uri-match-detection/) requires HTTPS.

### Copy credentials

You can also select the [clone] **Copy icon** next to an item. A menu will appear where you select **Copy username** or **Copy password**:

![Standard copy icon](https://bitwarden.com/assets/7y8WE9sWACC2KLASo9yASw/5c5fa1150e5e4f4ded19baf0afecfa6e/Standard_Copy_icon.png)
*Standard copy icon*

Alternatively, you can add three quick-copy action buttons next to items to specifically copy your username, password, or verification code to the clipboard:

![Quick copy actions](https://bitwarden.com/assets/5w7lobEk81aOGfLKFjRp2e/d37711426641f91deb9ea28715901fb0/Quick_copy_icons.png)
*Quick copy actions*

This option is off by default. To turn it on, go to **Settings** → **Appearance** and toggle on **Show quick copy actions on Vault**.

### Click items

Alternatively, you can set up the browser extension to autofill when you click anywhere on an item, as long as it appears in the **Autofill suggestions** section. When this option is used, the **Fill** button is not present:

![Click item to autofill](https://bitwarden.com/assets/3tnagVMjtTufvRCrih3ctQ/b3698262ce7c19baeda6afc87c485167/2025-01-02_11-14-19.png)
*Click item to autofill*

To activate this method, go to **Settings** → **Appearance** and toggle **Click items in autofill suggestion to fill** on.

If you want to open an item within the browser extension when this option is turned on, select the⋮ **Menu icon** → **View**.

### View Login

When the browser is open to a saved URI, click on its corresponding login item in the extension to open the **View Login** page. Then select **Autofill** to enter your information on that page:

![Autofill on View Login](https://bitwarden.com/assets/Y4VkZTrM140OgvjZe5lhc/f1bfffb355ce24ec915283e015fba176/Autofill_on_View_Login.png)
*Autofill on View Login*

If you select **Autofill** and the website you're on does not match the login item's saved URI, you have the choice to **Autofill and add this website** to the login item or use **Autofill without adding the website** to your vault. 

### Drag-and-drop logins

The browser extension and desktop apps include a feature to drag the username and password fields into a login form to fill credentials:

![Browser extension drag and drop](https://bitwarden.com/assets/7m5Ghz2w281MDQXtvWVdAZ/ded43247a3295552fed4690a3431b095/browser_gif.gif)

To drag-and-drop credentials:

1. Hover your cursor over the **Username** or **Password** field on the Bitwarden browser extension or desktop app.

![Hover username or password](https://bitwarden.com/assets/38KJr7zvVSKmYri1WaRXGg/5bab3513a7300ef20f9f55a33ba80c82/2025-02-20_11-07-33.png)
*Hover username or password*
2. Once the icon appears, drag the field into the desired login form.

## Other autofill methods

There are several more ways to autofill your credentials when your vault is unlocked within the browser extension. These options may be even faster because you don't need to interact with the browser extension.

For all of the autofill options described below, there are two instances where you may receive a warning before autofilling:

- If the targeted fields are in an [untrusted iframe](https://bitwarden.com/help/auto-fill-browser/#autofill-in-iframes/).
- The current site uses HTTP but the [item's saved URI](https://bitwarden.com/help/uri-match-detection/) requires HTTPS.

### Inline menu

Use the inline autofill menu to quickly input login credentials, [passkeys](https://bitwarden.com/help/storing-passkeys/), and [TOTP](https://bitwarden.com/help/integrated-authenticator/) codes from your Bitwarden vault.

![Inline autofill menu](https://bitwarden.com/assets/H7DjdJNvQH00yGNLf5gsC/1ec6f0ce9a94862b0cae1d8b8d679fc8/2024-10-29_14-41-02.png)
*Inline autofill menu*

#### Activate the inline autofill menu

To turn on the inline autofill menu:

1. Log in and unlock the Bitwarden [browser extension](https://bitwarden.com/help/getting-started-browserext/).
2. Select ⚙️ **Settings** → **Autofill**.
3. Check **Show autofill suggestions on form fields**, which will open more options:

 - (Optional) Check **Display identities as suggestions** and/or **Display cards as suggestions** if you want the inline autofill menu to [suggest those item types](https://bitwarden.com/help/auto-fill-card-id/#using-the-inline-menu/).
 - (Optional) Check **Display suggestions when icon is selected** to display the matching items available for autofill only when the Bitwarden icon is selected. If this setting is unchecked, the matching item(s) immediately appear below the form field.

We also recommend [turning off your browser's autofill](https://bitwarden.com/help/disable-browser-autofill/) option. If your browser's autofill functionality is enabled, you may experience conflicts with the Bitwarden autofill menu.

#### Use the inline autofill menu

### Log in with inline autofill

To log in to an account using the inline autofill menu:

1. Select the login form's username field. If your vault is locked when you attempt this, the menu will prompt you to unlock the vault.
2. The inline autofill menu will display. When it does, select the login or passkey you wish to use for the website.

> [!NOTE] adding URI to auto-fill menu 
> Don't see the login credentials you would like to use? Edit the vault item and select **Autofill and save**, or manually enter the website in the URI field.
3. If no credentials are saved for this site, select + **New item**. The browser extension will open to a new item where you can save new login credentials. 

![Autofill create item](https://bitwarden.com/assets/1nVpqyl5FuzMPIaKezwZ8c/8a715cb0b1e1423815f0b66b0e8b1b42/web-browser-extension-autofill-newitem.png)
*Autofill create item*

> [!NOTE] Press Esc to close auto-fill menu
> If the inline autofill menu is causing unintended interference with your browser, press the `Esc` key to close it.

### Enter TOTP with inline autofill

To autofill TOTP codes with inline autofill, place your cursor into the TOTP field on the login form. When the inline autofill menu displays, select the TOTP code:

![TOTP inline autofill single login](https://bitwarden.com/assets/3RaBZBRgkfwVF0mQPRZYBJ/840a46c911d09ead87ac09fdb0955493/2025-01-03_09-22-34.png)
*TOTP inline autofill single login*

If you have multiple logins for the website, the inline autofill menu will display each login with a TOTP code:

![Inline TOTP autofill](https://bitwarden.com/assets/1rc2rXC3daH5mcEZNRgbv1/db47ffbb4a3b987ff2e3e7842900ceb6/2025-01-02_17-23-28.png)
*Inline TOTP autofill*

### Create account with inline autofill

To create a new account using the inline autofill menu:

1. Enter a username in the login form's username field.
2. Select the password field. The inline autofill menu will display.
3. Select **Fill generated password** if you're satisfied with the generated password**.**You can also use the [refresh-tab] Generate button to generate a new password until you're satisfied with it:

![Fill generated password](https://bitwarden.com/assets/2JcceqWgFbk4ViLCMe6qm5/ce116e8ff337f90fbbd57b52aa15fdcd/2024-11-05_10-07-08.png)
*Fill generated password*

> [!TIP] Inline uses generator settings
> This option will use the settings you've configured in the browser extension's **Generator**tab. [Learn how to change these settings](https://bitwarden.com/help/generator/#password-types/).
4. **Before submitting the form by clicking 'Sign up' or 'Create account'**, the inline autofill menu will offer the option to **Save to Bitwarden**. Use this option to open Bitwarden in a pop-up, and select the **Save** button to save the generated credential:

![Save login to Bitwarden](https://bitwarden.com/assets/7cMSUQLfvxHNwHS8xMX1j7/b63d716005ec29eef2a4f42286271d29/2025-04-25_10-21-36.png)
*Save login to Bitwarden*
5. Complete the form by selecting Sign up, Create account, or whatever button the website or app offers to complete account creation.

### Context menu

Without opening your browser extension, you can right-click on an input field and use the **Bitwarden** → **Autofill** option. If your vault is locked when you attempt this, a window will open prompting you to unlock. Once unlocked, the browser extension will automatically proceed with autofilling your username, password, card, or identity.

![Browser Extension Context Menu](https://bitwarden.com/assets/6GKKvIe7GwwOBtp9gmh862/4d39f59a8a862bb83d53e50f9f68d107/2024-12-03_09-12-06.png)
*Browser Extension Context Menu*

> [!NOTE] No context-menu in safari extension
> Autofill with a context menu is currently unavailable in the Safari browser extension.

### Keyboard shortcuts

One of the fastest methods is with an autofill keyboard shortcut. This works when username and password fields appear together on one page and separately in split login workflows. 

#### Set up keyboard shortcuts

The default shortcut for login items is: `Ctrl/Cmd` + `Shift` + `L`. If you want to change it or the default doesn't work, [update your browser's shortcut settings](https://bitwarden.com/help/keyboard-shortcuts/#customize-browser-extension-shortcuts/). You can also create [shortcuts for cards and identities](https://bitwarden.com/help/auto-fill-card-id/#using-keyboard-shortcuts/).

If you use Microsoft Edge, make sure you upgrade to the latest Chromium-based version. 

#### Use keyboard shortcuts

To use the shortcut:

1. Place your cursor into the first login field, like username.
2. Press `Ctrl/Cmd` + `Shift` + `L`.
3. (Optional) If there are multiple logins with the detected URI, the last-used login will be used for the autofill operation. Press the same keyboard shortcut again to cycle through multiple logins.

If your vault is locked when you attempt the autofill shortcut, a window will open prompting you to unlock. Once unlocked, the browser extension will automatically proceed with autofilling your credentials.

> [!TIP] Authenticator keyboard shortcut
> If the login uses the [Bitwarden authenticator](https://bitwarden.com/help/integrated-authenticator/) for TOTPs and you use the autofill shortcut, the TOTP is automatically copied to the clipboard after autofill. Press `Cmd/Ctrl` + `V` to paste the TOTP.

### On page load

> [!WARNING] Why auto-fill on page load is "experimental".
> This feature is disabled by default because, while generally safe, compromised or untrusted websites could take advantage of this to steal credentials.
> 
> Browser extensions will not allow autofill on page load for [untrusted iframes](https://bitwarden.com/help/auto-fill-browser/#auto-fill-in-iframes/) and will warn users before auto-filling on an HTTP site when HTTPS is expected based on that [item's saved URI(s)](https://bitwarden.com/help/uri-match-detection/).

Autofill on page load will autofill login information when a web page corresponding to a login's URI value loads. By default, **on page load** is not turned on. Once enabled, you can set the default behavior to on or off for all items.

To enable this feature, navigate to **Settings** → **Autofill** in your browser extension, check on the **Autofill on page load** checkbox, and choose your default behavior. Once enabled and the default behavior is set, you can additionally specify autofill on page load behavior for each individual login:

![On page load options](https://bitwarden.com/assets/5PxR0j79XtzMCrF4R6xUtu/49fca8557bb393247d750e3b3030c0e8/2024-12-03_09-14-59.png)
*On page load options*

Using this convention, you can setup your browser extension to, for example:

- Autofill on page load for only a select few items (**off by default** for all items and **manually turned on** for select items).
- Autofill on page for all but a select few items (**on by default** for all items and **manually turned off** for select items).

## Troubleshoot autofill from the browser extension

If your browser extension is having issues autofilling usernames and passwords for a particular site, you can use [linked custom fields](https://bitwarden.com/help/auto-fill-custom-fields/#using-linked-custom-fields/) to force an autofill.

### Autofill in iframes

Browser extensions will quietly disable [autofill on page load](https://bitwarden.com/help/auto-fill-browser/#on-page-load/) for untrusted iframes and will warn you about the iframe if autofill is triggered manually using a keyboard shortcut, the context menu, or directly from the browser extension.

"Untrusted" iframes are defined as those for which the `src=""` value does not match a URI for the login item, as dictated by a globally-set or item-specific [match detection behavior](https://bitwarden.com/help/uri-match-detection/#match-detection-options/).

## Autofill less common credentials

### TOTP autofill

If you use the [integrated authenticator](https://bitwarden.com/help/integrated-authenticator/), the browser extension will autofill your TOTP code provided that you're using the context menu, keyboard shortcuts, or manual autofill (using the **Fill** button for items without a saved URI). You may also use the inline autofill menu for TOTP codes. Browser extensions **will not autofill your TOTP code if you're using autofill on page load**.

By default, your TOTP will also be copied to the clipboard when a login is autofilled. This is the recommended workflow if you're using autofill on page load.

> [!TIP] Extension TOTP copying
> Automatic TOTP copying is on by default when you use autofill in the browser extension. To turn it off, go to **Settings** → **Autofill** and uncheck **Copy TOTP automatically**. You can also use the nearby **Clear clipboard** dropdown menu to specify when copied values are cleared.

### Log in with passkeys stored in Bitwarden

You can [use passkeys to log in](https://bitwarden.com/help/storing-passkeys/) to websites. When storing a new passkey, the website URI is saved in the login item. To use the passkey, open the website and begin the passkey login workflow. Related passkeys will be displayed in a Bitwarden browser extension dialogue box. Select the passkey you would like to use and press **Confirm**:

![Log in with passkey](https://bitwarden.com/assets/5KeuUZox5shd0zDMxPHKXn/1aab35dfceed0ed9cdb17b143be9a890/2024-10-29_11-39-33.png)
*Log in with passkey*

The [inline autofill menu](https://bitwarden.com/help/auto-fill-browser/#inline-autofill-menu/) can also be used to easily authenticate with passkeys.

> [!NOTE] Excluded domains surpress passkeys
> When a domain is in the [**Excluded Domains**](https://bitwarden.com/help/exclude-domains/)list, Bitwarden browser extensions won't issue passkey prompts.
