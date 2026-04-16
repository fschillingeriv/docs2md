---
URL: https://bitwarden.com/help/receive-send/
---

# Receive a Send

Sends can be received and opened by anyone with the link, including those who do not have Bitwarden accounts—unlike regular vault items. Send links are randomly generated, and will look something like this:

- `https://send.bitwarden.com/#...`, which will automatically resolve to `https://vault.bitwarden/com/#/send/...`
- `https://your.selfhosted.domain.com/#/send/....` if you're self-hosting

![A received Send](https://bitwarden.com/assets/LLnrgZwyr6IAJ0GImXLnj/da3e363db0474f4cd6a57a44a6f1bd8f/Receive_a_send.png)
*A received Send*

Depending on the [options configured](https://bitwarden.com/help/create-send/) by the sender, the recipient of a Send may be required to:

- Enter a password to access the contents of the send
- Enter an [emailed verification code](https://bitwarden.com/help/receive-send/#email-verified-sends/)
- Manually toggle visibility on a hidden-text send

## Email-verified Sends

Premium Bitwarden users may create a Send with required email-verification to view. If you receive a Send link that requires email-verification, you will be prompted to enter a verification code after opening the Send link. To open an email-verified Send:

1. Open the Send link you received from the sender and enter your email address:

![Enter email Send](https://bitwarden.com/assets/6guff4hS04wXAcGp7DUMDo/5ba4409fd5fcf3171f665896fa17ca9f/2026-02-24_16-06-03.png)
*Enter email Send*
2. If the entered email matches the email address specified by the sender, you will receive an authorization code in your email inbox:

![Send verification code](https://bitwarden.com/assets/3f6f5IfMdXDqrR3cMwgoWN/65f8d6ffe2b3239049e7f76dfca33253/2026-02-24_16-06-56.png)
*Send verification code*
3. Enter the authorization code to view the Send.

![Enter Send verification code](https://bitwarden.com/assets/7qM22jPeoKCnGE6GS03wz7/4f959a8b1b7b9f13674bdda975af9a5d/2026-02-24_17-04-46.png)
*Enter Send verification code*

## Hidden-email Sends

By default, Sends will display the email address of the sender to recipients, as in the above screenshot. Senders can optionally hide their email address, which will substitute in a warning message:

![Hidden-email text Send](https://bitwarden.com/assets/47RPmr6xOowzjJbG6JxVG3/42ba660b4316b57c4857ed7f7fcd58e3/Hidden_email_send.png)
*Hidden-email text Send*

If you receive a Send with this warning, here's what you should do:

- **Was this Send expected?**

 If this Send was expected, get in touch with the sender. Validate with this person that the link you received (`https://vault.bitwarden.com/#/send/xxx/yyy`) matches the one they created.
- **Was this Send unexpected?**

 If this Send was unexpected, identify the sender before interacting with it. Ask your colleagues, managers, or friends whether they might have sent you something. If you do identify the sender, validate with this person that the link you received (`https://vault.bitwarden.com/#/send/xxx/yyy`) matches the one they created. **If you can't identify the sender**, don't interact with the Send.

> [!WARNING] Trusting unexpected File Sends.
> Taking the above measures to ensure the trustworthiness of a Send are particularly important in the case of file downloads. **Don't download mysterious files.**

## Deleted, expired, and disabled Sends

When a Send is [deleted, expired, or disabled](https://bitwarden.com/help/send-lifespan/) and you try using the Send link, the page will state that the Send does not exist or is no longer available:

![A deleted, expired, or disabled Send ](https://bitwarden.com/assets/6sveEP7CK57cGvSa9zpdwe/8da52464833e2dbfab7ef228f38f77e6/A_deleted__expired__or_disabled_Send.png)
*A deleted, expired, or disabled Send *
