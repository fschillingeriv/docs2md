---
URL: https://bitwarden.com/help/create-send/
---

# Create & Edit a Send

[Bitwarden Send](https://bitwarden.com/help/about-send/) lets you share encrypted text or files with anyone via a secure, generated link. Create a Send from any Bitwarden app and configure access and privacy options to fit your sharing needs.

> [!NOTE] Remove Send policy
> If you're a member of an organization that has turned off Send under the [Manage Send policy](https://bitwarden.com/help/policies/#manage-send/), your access to Sends is limited:
> 
> - You cannot create new Sends or edit existing ones.
> - You can view and delete Sends from the **Sends** page in all Bitwarden clients, except the web app.
> - You cannot access the Sends page with the Bitwarden web app.
> 
> Using the Manage Send policy, organization owners and admins can also control which fields are unavailable when creating a new Send.

## Create a Send

There are two types of Sends:

- A **text Send** shares encrypted text content, such as a message or note. All Bitwarden users can create and edit a text Send.
- A **file Send** contains an encrypted file, such as a document or image. Only [premium users](https://bitwarden.com/help/password-manager-plans/) or members of a paid organization (Families, Teams, or Enterprise) can make a file Send. To create a file Send, your account's email address must also be verified.

> [!NOTE] Older accounts may need to verify an email
> If your account is older, you may need to proactively verify your email. Log in to the [web app](https://vault.bitwarden.com/) and select **Verify Email**. If your account email is not verified, then you cannot create [Sends](https://bitwarden.com/help/about-send/).

Choose the Bitwarden app you want to Send from to get started:

### Web app

To create a new Send from the web app:

1. Select [send] **Send**.

> [!NOTE] About the Send View
> This page lists all Sends you created that have not reached their [deletion date](https://bitwarden.com/help/send-lifespan/#deletion-date/). You can filter your Sends by selecting one of the available **Types**.
2. Select + **New**:

![New Send](https://bitwarden.com/assets/9KgYcB25tb8NfYnitr0c0/a874be205a9a09ed66ad33a8d4c95ca9/2026-02-25_10-37-01.png)
*New Send*
3. Select which Send type you want to create, **Text** or **File**.
4. Enter a **Name**. This will be visible to anyone who opens the Send.
5. Depending on the type of Send:

 - For a **text Send**, enter the **Text to share**. If you don't want the Send to display this text when the link is first opened in a browser, check **Hide text by default**. This will require recipients to [toggle visibility](https://bitwarden.com/help/send-privacy/#hide-text/) to read your message.

> [!NOTE] Note; Create Send, text character limits
> Text Sends can include up to 1,000 characters encrypted. When saved, the character count of a Send's text is increased due to encryption, meaning that an 700-character Send will scale to ~1,000 characters when it comes into contact with Bitwarden, triggering this error. As a rule of thumb, character counts will grow between 30-50% when encrypted.
 - For a **file Send**, select **Choose file** and pick your file.

> [!NOTE] Create Send, file Send size limit
> The maximum file size per file Send is 500 MB (100 MB on mobile).
6. Pick a **Deletion date** from the dropdown menu, which is when the Send will be permanently [deleted](https://bitwarden.com/help/send-lifespan/#deletion-behavior/). The default is seven days and the maximum allowed time is 30 days from creation.
7. (Optional) Adjust the remaining options as needed:

 - Pick **Who can view** from the dropdown menu:

 - Choose **Anyone with the link** to allow anybody to open the Send link and view its contents. This is the default.
 - Choose **Specific people** and enter their email addresses (up to 2,500 characters) to require [Send email verification](https://bitwarden.com/help/send-privacy/#email-verified-recipients/) before the Send can be opened.
 - Choose **Anyone with a password set by you** to require recipients to enter a [password to open the Send](https://bitwarden.com/help/send-privacy/#send-passwords/).
 - Enter a number in **Limit views** to control how many times the Send can be opened before it's [deactivated](https://bitwarden.com/help/send-lifespan/#maximum-access-count-behavior/). No limit is set by default.
 - Check **Hide your email address from viewers** to remove your account's email from the opened Send.

> [!NOTE] Send, hide email from viewers
> When a Send is restricted to **Specific people** or **Anyone with a password set by you**, your email address is always hidden until the recipient enters the emailed verification code or password. The **Hide your email address from viewers** setting only applies after that point.
 - Enter a **Private note** that's visible only to you, the creator of the Send. This note does not appear on the opened Send.
8. Select **Save**.

Once your Send is created, use the ⋮ **Options** menu and select the [clone] **Copy Send link** button to copy the generated link to your clipboard:

![Send options](https://bitwarden.com/assets/1PiQrX748LtTFXChfAIbFP/0ff74124a0d215254c532fe79cff9012/2026-02-25_11-08-25.png)
*Send options*

Once copied, share your Send link with intended recipients however you prefer. Sends are end-to-end encrypted, so you don't need to worry about exposing any data to whatever intermediary communications services you use.

### Browser extension

> [!NOTE] Firefox and Safari browser send
> To create a send while using the Firefox or Safari browser extension, you must open the extension in the side bar or select the popout button:
> 
> 
> ![Browser extension pop-out](https://bitwarden.com/assets/1cbJy0jLBmSQmRumvYzVwp/a9e43f4c154686249056924eb3e56323/pop_out_screenshot.png)
> *Browser extension pop-out*

To create a new Send from the browser extension:

1. Select [send]**Send** .

> [!NOTE] About the Send View
> This page lists all Sends you created that have not reached their [deletion date](https://bitwarden.com/help/send-lifespan/#deletion-date/). You can filter your Sends by selecting one of the available **Types**.
2. Select + **New**:

![Send view in a browser extension ](https://bitwarden.com/assets/2qOv6DJYX1is2zurmeVBOd/5d2f0fd435c2534bc3377d651cd4f7f1/2026-02-25_11-11-56.png)
*Send view in a browser extension *
3. Select which Send type you want to create, **Text** or **File**.
4. Enter a **Name**. This will be visible to anyone who opens the Send.
5. Depending on the type of Send:

 - For a **text Send**, enter the **Text to share**. If you don't want the Send to display this text when the link is first opened in a browser, check **Hide text by default**. This will require recipients to [toggle visibility](https://bitwarden.com/help/send-privacy/#hide-text/) to read your message.

> [!NOTE] Note; Create Send, text character limits
> Text Sends can include up to 1,000 characters encrypted. When saved, the character count of a Send's text is increased due to encryption, meaning that an 700-character Send will scale to ~1,000 characters when it comes into contact with Bitwarden, triggering this error. As a rule of thumb, character counts will grow between 30-50% when encrypted.
 - For a **file Send**, select **Choose file** and pick your file.

> [!NOTE] Create Send, file Send size limit
> The maximum file size per file Send is 500 MB (100 MB on mobile).
6. Pick a **Deletion date** from the dropdown menu, which is when the Send will be permanently [deleted](https://bitwarden.com/help/send-lifespan/#deletion-behavior/). The default is seven days and the maximum allowed time is 30 days from creation.
7. (Optional) Adjust the remaining options as needed:

 - Pick **Who can view** from the dropdown menu:

 - Choose **Anyone with the link** to allow anybody to open the Send link and view its contents. This is the default.
 - Choose **Specific people** and enter their email addresses (up to 2,500 characters) to require [Send email verification](https://bitwarden.com/help/send-privacy/#email-verified-recipients/) before the Send can be opened.
 - Choose **Anyone with a password set by you** to require recipients to enter a [password to open the Send](https://bitwarden.com/help/send-privacy/#send-passwords/).
 - Enter a number in **Limit views** to control how many times the Send can be opened before it's [deactivated](https://bitwarden.com/help/send-lifespan/#maximum-access-count-behavior/). No limit is set by default.
 - Check **Hide your email address from viewers** to remove your account's email from the opened Send.

> [!NOTE] Send, hide email from viewers
> When a Send is restricted to **Specific people** or **Anyone with a password set by you**, your email address is always hidden until the recipient enters the emailed verification code or password. The **Hide your email address from viewers** setting only applies after that point.
 - Enter a **Private note** that's visible only to you, the creator of the Send. This note does not appear on the opened Send.
8. Select **Save**.

Once your Send is created, you may Copy the link or select the ⋮ and then **Copy Send link**to copy the generated link to your clipboard:

![Copy a Send link ](https://bitwarden.com/assets/1lLksK7QbomKPRueO41c4d/7af290d439cb39056564454b78e52936/2026-02-25_11-18-05.png)
*Copy a Send link *

Once copied, share your Send link with intended recipients however you prefer. Sends are end-to-end encrypted, so you don't need to worry about exposing any data to whatever intermediary communications services you use.

### Desktop

To create a new Send from the desktop app:

1. Select [send] **Send**.

> [!NOTE] About the Send View
> This page lists all Sends you created that have not reached their [deletion date](https://bitwarden.com/help/send-lifespan/#deletion-date/). You can filter your Sends by selecting one of the available **Types**.
2. Select + **New**:

![Send view in a Desktop App ](https://bitwarden.com/assets/2O01p5FyMpUhlhi5bAq7mH/3135d39e953c52bb0d843ee6afeb1121/2026-04-23_11-48-19.png)
*Send view in a Desktop App *
3. Select which Send type you want to create, **Text** or **File**.
4. Enter a **Name**. This will be visible to anyone who opens the Send.
5. Depending on the type of Send:

 - For a **text Send**, enter the **Text to share**. If you don't want the Send to display this text when the link is first opened in a browser, check **Hide text by default**. This will require recipients to [toggle visibility](https://bitwarden.com/help/send-privacy/#hide-text/) to read your message.

> [!NOTE] Note; Create Send, text character limits
> Text Sends can include up to 1,000 characters encrypted. When saved, the character count of a Send's text is increased due to encryption, meaning that an 700-character Send will scale to ~1,000 characters when it comes into contact with Bitwarden, triggering this error. As a rule of thumb, character counts will grow between 30-50% when encrypted.
 - For a **file Send**, select **Choose file** and pick your file.

> [!NOTE] Create Send, file Send size limit
> The maximum file size per file Send is 500 MB (100 MB on mobile).
6. Pick a **Deletion date** from the dropdown menu, which is when the Send will be permanently [deleted](https://bitwarden.com/help/send-lifespan/#deletion-behavior/). The default is seven days and the maximum allowed time is 30 days from creation.
7. (Optional) Adjust the remaining options as needed:

 - Pick **Who can view** from the dropdown menu:

 - Choose **Anyone with the link** to allow anybody to open the Send link and view its contents. This is the default.
 - Choose **Specific people** and enter their email addresses (up to 2,500 characters) to require [Send email verification](https://bitwarden.com/help/send-privacy/#email-verified-recipients/) before the Send can be opened.
 - Choose **Anyone with a password set by you** to require recipients to enter a [password to open the Send](https://bitwarden.com/help/send-privacy/#send-passwords/).
 - Enter a number in **Limit views** to control how many times the Send can be opened before it's [deactivated](https://bitwarden.com/help/send-lifespan/#maximum-access-count-behavior/). No limit is set by default.
 - Check **Hide your email address from viewers** to remove your account's email from the opened Send.

> [!NOTE] Send, hide email from viewers
> When a Send is restricted to **Specific people** or **Anyone with a password set by you**, your email address is always hidden until the recipient enters the emailed verification code or password. The **Hide your email address from viewers** setting only applies after that point.
 - Enter a **Private note** that's visible only to you, the creator of the Send. This note does not appear on the opened Send.
8. Select **Save**.

Once your Send is created, select the ⋮ and then **Copy Send link**to copy the generated link to your clipboard:

![Send options on desktop](https://bitwarden.com/assets/4IgMnKAEjk16bJdbuUkVeH/fb20d049505d8a69dce6f39e4e4a9c4c/2026-04-23_11-49-34.png)
*Send options on desktop*

Once copied, share your Send link with intended recipients however you prefer. Sends are end-to-end encrypted, so you don't need to worry about exposing any data to whatever intermediary communications services you use.

### Mobile

To create a new Send from a mobile app:

1. Tap [send] **Send**.

> [!NOTE] About the Send View
> This page lists all Sends you created that have not reached their [deletion date](https://bitwarden.com/help/send-lifespan/#deletion-date/). You can filter your Sends by selecting one of the available **Types**.
2. Tap the + **New icon**:

![Send on mobile](https://bitwarden.com/assets/5vHsSA3o9O735MitlnOPVr/e2eeb5387bf1358f4aa0aaafbfaa3d5c/new_send_mobile.png)
*Send on mobile*
3. Select which Send type you want to create, **Text** or **File**.
4. Enter a **Send name**. This will be visible to anyone who opens the Send.
5. Depending on the type of Send:

 - For a **text Send**, enter the **Text to share**. If you don't want the Send to display this text when the link is first opened in a browser, toggle on **When accessing the Send, hide the text by default**. This will require recipients to [toggle visibility](https://bitwarden.com/help/send-privacy/#hide-text/) to read your message.

> [!NOTE] Note; Create Send, text character limits
> Text Sends can include up to 1,000 characters encrypted. When saved, the character count of a Send's text is increased due to encryption, meaning that an 700-character Send will scale to ~1,000 characters when it comes into contact with Bitwarden, triggering this error. As a rule of thumb, character counts will grow between 30-50% when encrypted.
 - For a **file Send**, select **Choose file** and pick your file.

> [!NOTE] Create Send, file Send size limit
> The maximum file size per file Send is 500 MB (100 MB on mobile).
6. Pick a **Deletion date** from the dropdown menu, which is when the Send will be permanently [deleted](https://bitwarden.com/help/send-lifespan/#deletion-behavior/). The default is seven days and the maximum allowed time is 30 days from creation.
7. (Optional) Adjust the remaining options as needed:

 - Pick **Who can view** from the dropdown menu:

 - Choose **Anyone with the link** to allow anybody to open the Send link and view its contents. This is the default.
 - Choose **Specific people** and enter their email addresses (up to 2,500 characters) to require [Send email verification](https://bitwarden.com/help/send-privacy/#email-verified-recipients/) before the Send can be opened.
 - Choose **Anyone with a password set by you** to require recipients to enter a [password to open the Send](https://bitwarden.com/help/send-privacy/#send-passwords/).
 - Enter a number in **Maximum access count** to control how many times the Send can be opened before it's [deactivated](https://bitwarden.com/help/send-lifespan/#maximum-access-count-behavior/). No limit is set by default.
 - Toggle on **Hide my email address from recipients** to remove your account's email from the opened Send.

> [!NOTE] Send, hide email from viewers
> When a Send is restricted to **Specific people** or **Anyone with a password set by you**, your email address is always hidden until the recipient enters the emailed verification code or password. The **Hide your email address from viewers** setting only applies after that point.
 - Enter a **Private note** that's visible only to you, the creator of the Send. This note does not appear on the opened Send.
8. Tap **Save**.

Once your Send is created, select the ⋯ and then choose the **Share link** option:

![Share a send on mobile](https://bitwarden.com/assets/6WZTQUop3KXnQKoGqgVzgu/8bf9c1b068a97856c5d13b09449a1fdf/shore-mobile-send.png)
*Share a send on mobile*

> [!TIP] Send via iOS Share Menu
> If you are using iOS, you can also share your send directly from the iOS [Share Menu](https://developer.apple.com/design/human-interface-guidelines/ios/extensions/sharing-and-actions/).

Share your Send link with intended recipients however you prefer. Sends are end-to-end encrypted, so you don't need to worry about exposing any data to whatever intermediary communications services you use.

### CLI

The following are sample commands to help you get started using Send from the CLI. For more examples and help writing your own send command, we recommend reading [Send from CLI](https://bitwarden.com/help/send-cli/).

To create a simple text Send with a [deletion date](https://bitwarden.com/help/send-lifespan/#deletion-date/) set to 14 days from creation:

```
bw send -n "My Text Send" -d 14 "My first secret message."
```

To create a simple file Send with a [deletion date](https://bitwarden.com/help/send-lifespan/#deletion-date/) set to 14 days from creation:

```
bw send -n "My File Send" - d 14 -f /Users/myaccount/Documents/my_file.pdf
```

## Edit a Send

You may want to update a Send after creating it.

### Web app

To edit a Send:

1. Go to **Send**.
2. Select the name of the **Send**.
3. Select **Edit**.
4. Make your desired changes and then select **Save**.

### Browser extension

To edit a Send:

1. Go to **Send**.
2. Select the name of the **Send**.
3. Make your desired changes and then select **Save**.

### Desktop

To edit a Send:

1. Go to **Send**.
2. Select the name of the **Send**.
3. Make your desired changes and then select **Save**.

### Mobile

To edit a Send:

1. Tap **Send**.
2. Tap the name of the **Send**.
3. Tap the ⋯ **Menu icon**.
4. Tap **Edit**.
5. Make your desired changes and then tap the ✓ **Check icon**.

### CLI

Use the `edit` command to [update a Send with the CLI](https://bitwarden.com/help/send-cli/#edit/).
