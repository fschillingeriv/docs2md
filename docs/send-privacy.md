---
URL: https://bitwarden.com/help/send-privacy/
---

# Send Privacy

Protect the contents of your Send by configuring a [password for access](https://bitwarden.com/help/send-privacy/#send-passwords/) so unintended recipients can't see the information, and/or to [hide your email](https://bitwarden.com/help/send-privacy/#hide-email/) from recipients. For text Sends, you can also optionally require recipients to [toggle visibility](https://bitwarden.com/help/send-privacy/#hide-text/) to prevent exposure to unintentional onlookers.

The **Password**, **Hide Email**, and **Hide Text** options can be set while creating a new Send, or from the **Edit Send** view at any time prior to the Send's [deletion](https://bitwarden.com/help/send-lifespan/#deletion-behavior/).

## Email-verified recipients

Paid Bitwarden plan users (Premium, Families, Teams, Enterprise) can require email verification to access a Send. When creating the Send, specify one or more recipient email addresses. After accessing the Send link, recipients must enter their email address. If it matches an address you specified, a verification code is emailed to the recipient. To create an email-verified Send:

1. Select the **Specific people** option in the **Who can view** menu. Then, add the intended recipients to the **Emails**field. Complete the [Send setup](https://bitwarden.com/help/about-send/#using-send/) and share the send link with intended recipients.

![Verified user Send](https://bitwarden.com/assets/9isz2fm2soiJJOau1sq7b/1b9cdff84b482c8698ef6e0a20ebf826/Send_access_list.png)
*Verified user Send*
2. Recipients who access the Send link will be asked to enter their email address. A verification code will be sent to that users email address. Enter the verification code to view the content of the send.

![Enter Send verification code](https://bitwarden.com/assets/7qM22jPeoKCnGE6GS03wz7/4f959a8b1b7b9f13674bdda975af9a5d/2026-02-24_17-04-46.png)
*Enter Send verification code*

## Send passwords

For any Send, you can set a password that recipients will be required to enter in order to access it. Password-protecting a Send is a good way to ensure the information in it is not exposed to unintended recipients:

![Receiving a password-protected Send](https://bitwarden.com/assets/7DyqQ9YHNrAIvmlyDrOCmr/fd237c32480dfd1a5d8c8d911e13abff/send-password.png)
*Receiving a password-protected Send*

Once you password-protect a Send, you won't be able to view the configured password again, however you can [change](https://bitwarden.com/help/send-privacy/#change-send-passwords/) or [remove](https://bitwarden.com/help/send-privacy/#remove-send-passwords/) it at any time.

### Change Send passwords

You can change a Send's password at any time from the **Edit Send** view. Changing a Send's password will not require you to enter the previous password. When changing a Send's password, the **Password** field will change to **New Password.**

### Remove Send passwords

You can remove a Send's password at any time using the [undo] **Remove Password** menu option. Removing a Send's password will not require you to enter the previous password:

![Remove password protection](https://bitwarden.com/assets/GIVACRQbGQyj0fLzLUZOc/b7a14b2ef75eea16f9b9376418cca1e7/remove-password_protection.png)
*Remove password protection*

## Hide email

By default, Sends show the sender's email address to recipients. To remove your email address when creating the Send:

1. Select **Options**.
2. Check **Hide my email address from recipients**.

Recipients can still validate the trustworthiness of Sends by cross-referencing the **Send link** with their sender. Hidden-email send objects will issue a warning to recipients encouraging them to do so:

![Hidden-email text Send](https://bitwarden.com/assets/47RPmr6xOowzjJbG6JxVG3/42ba660b4316b57c4857ed7f7fcd58e3/Hidden_email_send.png)
*Hidden-email text Send*

> [!TIP] Send Options Policy
> For enterprise organizations, the availability of this option can be set using an [enterprise policy](https://bitwarden.com/help/policies/#send-controls/).

## Hide text

For text Sends, toggle the **When accessing the Send, hide the text by default** option to require recipients to [eye] **Toggle Visibility** in order to see its contents. Hiding the text is a good way to ensure the information in it is not exposed to unintentional onlookers:

![Receiving a hidden-text Send](https://bitwarden.com/assets/4KcdIWqSnADnv1TMtsrSIr/f9ab606faf3e7395f25b02ed8a11fc14/hidden_text.png)
*Receiving a hidden-text Send*
