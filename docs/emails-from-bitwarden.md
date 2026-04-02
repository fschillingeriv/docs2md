---
URL: https://bitwarden.com/help/emails-from-bitwarden/
---

# Identify Legitimate Emails from Bitwarden

Like using strong passwords, avoiding suspicious emails is an important tool in your online security toolkit. We recommend familiarizing yourself with these [FTC Guidelines](https://www.consumer.ftc.gov/articles/how-recognize-and-avoid-phishing-scams) for spotting and avoiding phishing. 

Here are some guidelines to help you determine whether an email that looks like it's from Bitwarden is legitimate:

## Automated emails

### Product interaction emails

Emails such as new device alerts, invitations to [join an organization](https://bitwarden.com/help/managing-users/), [request access to Secrets Manager](https://bitwarden.com/help/secrets-manager-quick-start/#getting-to-secrets-manager/), and [two-step login codes](https://bitwarden.com/help/setup-two-step-login-email/), or [Send-verification codes](https://bitwarden.com/help/send-privacy/#email-verified-recipients/) will come from `no-reply@bitwarden.com` or `.eu` or, if you are self-hosting, a [configured domain](https://bitwarden.com/help/install-on-premise-linux/#install-bitwarden/) like `no-reply@my.domain.com`.

> [!NOTE] Email Verification Email
> Email verification requests, which as of 2024.9.2 are sent to cloud users during the account creation, are also issued from `no-reply@bitwarden.com`:
> 
> 
> ![Email verification](https://bitwarden.com/assets/2QR4MYirRuYyMJnkx5ce6e/858d2d1fc23440e31ce87a8ff6efa4f5/2024-09-26_10-01-00.png)
> *Email verification*

These emails will **never contain attachments**. If you are prompted to download a file, please report the email to us.

Some of these emails, such as organization invites, will contain buttons. Always check the validity of the hyperlink **before clicking on it**by confirming that it leads to `https://vault.bitwarden.com` or your organization's self-hosted domain. If you don't know your organization's domain, ask a member of your IT team or an administrator.

![Organization invitation](https://bitwarden.com/assets/4Fe96NuWb7yRe6muKf7UbZ/bcb1a8df0bc2ffdecbcd86b82d16c9a3/2025-09-03_10-41-25.png)

### Payments emails

Automated payments emails for individual premium and paid organizations subscriptions will come from an `invoice+statements@bitwarden.com` address. These emails **will contain**attachments, specifically PDF invoices and receipts. If a payment ever fails, a notification email will come from a `failed-payments@bitwarden.com` address.

### Renewals emails

Paid users will be reminded of upcoming renewals via emails for each Bitwarden subscription that is approaching its renewal date. These emails will come from `no-reply@bitwarden.com` or `.eu` and `upcoming-invoice@bitwarden.com` addresses.

## Opt-in emails

While you will receive [automated emails](https://bitwarden.com/help/emails-from-bitwarden/#automated-emails/) as part of everyday use of Bitwarden, you might also receive emails from the following addresses if you have interacted with various parts of the Bitwarden ecosystem:

- Support requests will be received from `support@bitwarden.com`.
- Product announcements will be received from `productupdates@bitwarden.com`.
- Trial information will be received from `trial@bitwarden.com`.
- Marketing campaigns will be received from `marketing@bitwarden.com` and `care@bitwarden.com`.
- Emails from members of the Bitwarden team will be received from `@bitwarden.com` email addresses.

## Alert emails

Bitwarden will send an email alert for suspicious activities such as logging in from an unknown device, and failed login attempts from an unknown device. 

These emails will **never contain attachments**. If you are prompted to download a file or click an unknown link, please contact us. 

### New device verification

The first time you log in from a device you have not logged in to previously, if your account does not use two-step login, you will receive an email containing a verification code . Learn more [here](https://bitwarden.com/help/new-device-verification/).

### New device logged in

If your account successfully logs in from an unknown device, you will receive an email containing information about the login.

![Login from unknown device email](https://bitwarden.com/assets/3BPGGp6Wvm3NzDopPbkkj2/b8ff436931e2791d366dda3ea8ed078e/Screenshot_2023-03-29_at_4.05.28_PM.png)

The email will contain:

- Date
- IP Address
- Device type

If you do not recognize this login, see [here](https://bitwarden.com/help/security-faqs/#q-what-do-i-do-if-i-dont-recognize-a-new-device-logging-into-bitwarden/) and take immediate steps to protect your account. 

### Trusted device request approved

When a request to an organization administrator to [add a trusted device](https://bitwarden.com/help/add-a-trusted-device/) is approved, the requesting user is sent an email informing them they can continue logging in on that device. **The user must take action by logging in to the new device within 12 hours, or the approval will expire.**

The email will contain:

- Date
- IP address
- Device type

### Failed login attempts detected

If an incorrect two-step login attempt, for example the entering of an incorrect TOTP code, is detected you will receive an email informing you of this:

![Failed login attempt email](https://bitwarden.com/assets/7oGzZ6B0WTuRKeKu7DBmAE/8a7b4517cab6b76fd474e05171be5fba/2025-08-28_11-07-13.png)

If the attempt was you, you can safely ignore the message. If the attempt **was not you**, you should [change your master password](https://bitwarden.com/help/master-password/#change-master-password/) immediately.

## Announcement emails

### Subject: Upcoming login changes (Dec. 2024)

This email, sent in December 2024 from `no-reply@bitwarden.com`, was sent to inform users of upcoming changes to new device verification.
