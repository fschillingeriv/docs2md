---
URL: https://bitwarden.com/help/create-send/
---

# Create a Send

Anyone can create text Sends, but file Sends can only be created by [premium users](https://bitwarden.com/help/password-manager-plans/) or members of a paid organization (families, teams, or enterprise). 

> [!NOTE] Remove Send policy
> Members of organizations that have enabled the [Remove Send policy](https://bitwarden.com/help/policies/#remove-send/) will be unable to access Send from their Bitwarden client.

Choose the Bitwarden app you want to Send from to get started:

### Web app

To create a new Send from the web app:

1. Select **Send** from the navigation.

> [!NOTE] About the Send View
> This view will list Sends that have not reached their [deletion date](https://bitwarden.com/help/send-lifespan/#deletion-date/). Like the **Vaults** view, you can filter your Sends by selecting one of the available **Types**.

2. Select the + **New Send** button:

![New Send](https://bitwarden.com/assets/9KgYcB25tb8NfYnitr0c0/a874be205a9a09ed66ad33a8d4c95ca9/2026-02-25_10-37-01.png)
*New Send*

3. On the **New Send** dialog, specify the following:

- **What type of Send is this?**: Choose whether this Send will be **Text** or a **File**:

| **Type** | **Steps** |
|------|------|
| **Text** | Type or paste the desired text into the input box. Toggle the **When accessing the Send, hide the text by default**option to require recipients to [toggle visibility](https://bitwarden.com/help/send-privacy/#hide-text/) when they open a Send. Sends may not exceed 1000 characters encrypted. When saved, the character count of a Send's text is increased due to encryption, meaning that an 700-character Send will scale to ~1,000 characters when it comes into contact with Bitwarden, triggering this error. As a rule of thumb, character counts will grow between 30-50% when encrypted. |
| **File** | Select the **Choose File**button and browse for the file to Send. The maximum file size per Send is 500 MB (100 MB on Mobile). (**Requires Premium**& Verified Email) |

- **Name**: Choose an identifiable, meaningful name for this Send.

 - By default, a Send is scheduled for deletion seven days from its creation. You can change this and other options (see step 4), otherwise select **Save** to finish creating your Send.

4. Configure the following options as needed:

| **Option** | **Description** |
|------|------|
| **Hide text by default** | The contents of the send will be hidden by default. |
| **Deletion date** | The Send will be permanently [deleted](https://bitwarden.com/help/send-lifespan/#deletion-behavior/) on the specified date and time. By default, seven days from creation. The **maximum allowed value**is 30 days from creation. |
| **Who can view** | Choose who can view: **Anyone with the link:** Anyone who receives the Send link can view the contents of the Send. **Specific people:** [Specify the email address](https://bitwarden.com/help/send-privacy/#email-verified-recipients/) of recipients who can receive this Send. They will receive a verification code in their email when accessing the Send (**Requires Premium**). **Anyone with a password set by you:**[Require a password](https://bitwarden.com/help/send-privacy/#send-passwords/) to be entered by recipients of this Send in order to gain access. |
| **Limit views** | The Send will be [disabled](https://bitwarden.com/help/send-lifespan/#maximum-access-count-behavior/) after the specified access count is reached. By default, unspecified. |
| **Hide your email address from viewers** | [Hide your email](https://bitwarden.com/help/send-privacy/#hide-email/) from Send recipients. |
| **Private note** | Enter private notes for this Send, which will only be visible to you. |

Once you are happy with your Send, select **Save** to finish.

Once your Send is created, use the ⋮ **Options** menu and select the [clone] **Copy Send link** button to copy the generated link to your clipboard:

![Send options](https://bitwarden.com/assets/1PiQrX748LtTFXChfAIbFP/0ff74124a0d215254c532fe79cff9012/2026-02-25_11-08-25.png)
*Send options*

Once copied, share your Send link with intended recipients however you prefer. Sends are end-to-end encrypted, so you don't need to worry about exposing any data to whatever intermediary communications services you use.

### Browser extension

To create a new Send from a browser extension:

1. Select the [send-f] **Send** tab.

> [!NOTE] About the Send View
> This view will list Sends that have not reached their [deletion date](https://bitwarden.com/help/send-lifespan/#deletion-date/). Like the **Vaults** view, you can filter your Sends by selecting one of the available **Types**.

2. Select the + **New** button and choose **Text** or **File**:

![Send view in a browser extension ](https://bitwarden.com/assets/2qOv6DJYX1is2zurmeVBOd/5d2f0fd435c2534bc3377d651cd4f7f1/2026-02-25_11-11-56.png)
*Send view in a browser extension *

3. On the **New Send** view, specify the following:

- **Name**: Choose an identifiable, meaningful name for this Send.
- Some options will depend on whether you selected **Text** or **File**:

| **Type** | **Steps** |
|------|------|
| **Text** | Type or paste the desired text into the input box. Toggle the **When accessing the Send, hide the text by default**option to require recipients to [toggle visibility](https://bitwarden.com/help/send-privacy/#hide-text/) when they open a Send. Sends may not exceed 1000 characters encrypted. When saved, the character count of a Send's text is increased due to encryption, meaning that an 700-character Send will scale to ~1,000 characters when it comes into contact with Bitwarden, triggering this error. As a rule of thumb, character counts will grow between 30-50% when encrypted. |
| **File** | Select the **Choose File**button and browse for the file to Send. The maximum file size per Send is 500 MB (100 MB on Mobile). (**Requires Premium**& Verified Email). |

By default, a Send is scheduled for deletion seven days from its creation. You can change this and other options (see Step 4), otherwise select **Save** to finish creating your Send.

> [!NOTE] Firefox and Safari browser send
> To create a send while using the Firefox or Safari browser extension, you must open the extension in the side bar or select the popout button:
> 
> 
> ![Browser extension pop-out](https://bitwarden.com/assets/1cbJy0jLBmSQmRumvYzVwp/a9e43f4c154686249056924eb3e56323/pop_out_screenshot.png)
> *Browser extension pop-out*

4. Configure the following options as needed:

| **Option** | **Description** |
|------|------|
| **Hide text by default** | The contents of the send will be hidden by default. |
| **Deletion date** | The Send will be permanently [deleted](https://bitwarden.com/help/send-lifespan/#deletion-behavior/) on the specified date and time. By default, seven days from creation. The **maximum allowed value**is 30 days from creation. |
| **Who can view** | Choose who can view: **Anyone with the link:** Anyone who receives the Send link can view the contents of the Send. **Specific people:** [Specify the email address](https://bitwarden.com/help/send-privacy/#email-verified-recipients/) of recipients who can receive this Send. They will receive a verification code in their email when accessing the Send (**Requires Premium**). **Anyone with a password set by you:**[Require a password](https://bitwarden.com/help/send-privacy/#send-passwords/) to be entered by recipients of this Send in order to gain access. |
| **Limit views** | The Send will be [disabled](https://bitwarden.com/help/send-lifespan/#maximum-access-count-behavior/) after the specified access count is reached. By default, unspecified. |
| **Hide your email address from viewers** | [Hide your email](https://bitwarden.com/help/send-privacy/#hide-email/) from Send recipients. |
| **Private note** | Enter private notes for this Send, which will only be visible to you. |

Once you are happy your Send, select **Save** to finish.

Once your Send is created, you may Copy the link or select the ⋮ and then **Copy Send link**to copy the generated link to your clipboard:

![Copy a Send link ](https://bitwarden.com/assets/1lLksK7QbomKPRueO41c4d/7af290d439cb39056564454b78e52936/2026-02-25_11-18-05.png)
*Copy a Send link *

Once copied, share your Send link with intended recipients however you prefer. Sends are end-to-end encrypted, so you don't need to worry about exposing any data to whatever intermediary communications services you use.

### Desktop

To create a new Send from a desktop app:

1. Select the [send-f] **Send** tab.

> [!NOTE] About the Send View
> This view will list Sends that have not reached their [deletion date](https://bitwarden.com/help/send-lifespan/#deletion-date/). Like the **Vaults** view, you can filter your Sends by selecting one of the available **Types**.

2. Select the **New Send** button:

![Send view in a Desktop App ](https://bitwarden.com/assets/2O01p5FyMpUhlhi5bAq7mH/0c154046969e8028d95fb4bdbaf12b93/2026-02-26_15-40-37.png)
*Send view in a Desktop App *

3. In the right-most column, specify the following:

- **Name**: Choose an identifiable, meaningful name for this Send.
- **Type**: Choose whether this Send will be **Text** or a **File**:

| **Type** | **Steps** |
|------|------|
| **Text** | Type or paste the desired text into the input box. Toggle the **When accessing the Send, hide the text by default**option to require recipients to [toggle visibility](https://bitwarden.com/help/send-privacy/#hide-text/) when they open a Send. Sends may not exceed 1000 characters encrypted. When saved, the character count of a Send's text is increased due to encryption, meaning that an 700-character Send will scale to ~1,000 characters when it comes into contact with Bitwarden, triggering this error. As a rule of thumb, character counts will grow between 30-50% when encrypted. |
| **File** | Select the **Choose File**button and browse for the file to Send. The maximum file size per Send is 500 MB (100 MB on Mobile). (**Requires Premium**& Verified Email). |

By default, a Send is scheduled for deletion seven days from its creation. You can change this and other options (see step 4), otherwise select **Save** to finish creating your Send.

4. Configure the following options as needed:

| **Option** | **Description** |
|------|------|
| **Hide text by default** | The contents of the send will be hidden by default. |
| **Deletion date** | The Send will be permanently [deleted](https://bitwarden.com/help/send-lifespan/#deletion-behavior/) on the specified date and time. By default, seven days from creation. The **maximum allowed value**is 30 days from creation. |
| **Who can view** | Choose who can view: **Anyone with the link:** Anyone who receives the Send link can view the contents of the Send. **Specific people:** [Specify the email address](https://bitwarden.com/help/send-privacy/#email-verified-recipients/) of recipients who can receive this Send. They will receive a verification code in their email when accessing the Send (**Requires Premium**). **Anyone with a password set by you:**[Require a password](https://bitwarden.com/help/send-privacy/#send-passwords/) to be entered by recipients of this Send in order to gain access. |
| **Limit views** | The Send will be [disabled](https://bitwarden.com/help/send-lifespan/#maximum-access-count-behavior/) after the specified access count is reached. By default, unspecified. |
| **Hide your email address from viewers** | [Hide your email](https://bitwarden.com/help/send-privacy/#hide-email/) from Send recipients. |
| **Private note** | Enter private notes for this Send, which will only be visible to you. |

Once you are happy your Send, select **Save** to finish.

Once your Send is created, select the ⋮ and then **Copy Send link**to copy the generated link to your clipboard:

![Copy send link desktop](https://bitwarden.com/assets/4IgMnKAEjk16bJdbuUkVeH/aef61f80bb7426874c937d07eaa58b85/2026-02-25_11-40-24.png)
*Copy send link desktop*

Once copied, share your Send link with intended recipients however you prefer. Sends are end-to-end encrypted, so you don't need to worry about exposing any data to whatever intermediary communications services you use.

### Mobile

To create a new Send from a mobile app:

1. Tap the [send-f] **Send** tab.

> [!NOTE] About the Send View
> This view will list Sends that have not reached their [deletion date](https://bitwarden.com/help/send-lifespan/#deletion-date/). Like the **Vaults** view, you can filter your Sends by selecting one of the available **Types**.

2. Tap the + **New send** button:

![Send on mobile](https://bitwarden.com/assets/5vHsSA3o9O735MitlnOPVr/e2eeb5387bf1358f4aa0aaafbfaa3d5c/new_send_mobile.png)
*Send on mobile*

3. On the **Add Send** view, specify the following:

- **Type**: Choose whether this Send will be **Text** or a **File**:

| **Type** | **Steps** |
|------|------|
| **Text** | Type or paste the desired text into the input box. Toggle the **When accessing the Send, hide the text by default**option to require recipients to [toggle visibility](https://bitwarden.com/help/send-privacy/#hide-text/) when they open a Send. Sends may not exceed 1000 characters encrypted. When saved, the character count of a Send's text is increased due to encryption, meaning that an 700-character Send will scale to ~1,000 characters when it comes into contact with Bitwarden, triggering this error. As a rule of thumb, character counts will grow between 30-50% when encrypted. |
| **File** | Select the **Choose File**button and browse for the file to Send. The maximum file size per Send is 500 MB (100 MB on Mobile). (**Requires Premium**& Verified Email). |

- **Name**: Choose an identifiable, meaningful name for this Send.

 - By default, a Send is scheduled for deletion seven days from its creation. You may change this and other options using the [angle-down] **Additional options** menu (see Step 4), otherwise tap **Save** to finish creating your Send.

4. Configure the following options as needed:

| **Option** | **Description** |
|------|------|
| **Hide text by default** | The contents of the send will be hidden by default. |
| **Deletion date** | The Send will be permanently [deleted](https://bitwarden.com/help/send-lifespan/#deletion-behavior/) on the specified date and time. By default, seven days from creation. The **maximum allowed value**is 30 days from creation. |
| **Who can view** | Choose who can view: **Anyone with the link:** Anyone who receives the Send link can view the contents of the Send. **Specific people:** [Specify the email address](https://bitwarden.com/help/send-privacy/#email-verified-recipients/) of recipients who can receive this Send. They will receive a verification code in their email when accessing the Send (**Requires Premium**). **Anyone with a password set by you:**[Require a password](https://bitwarden.com/help/send-privacy/#send-passwords/) to be entered by recipients of this Send in order to gain access. |
| **Limit views** | The Send will be [disabled](https://bitwarden.com/help/send-lifespan/#maximum-access-count-behavior/) after the specified access count is reached. By default, unspecified. |
| **Hide your email address from viewers** | [Hide your email](https://bitwarden.com/help/send-privacy/#hide-email/) from Send recipients. |
| **Private note** | Enter private notes for this Send, which will only be visible to you. |

Once you are happy your Send, select **Save** to finish.

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
