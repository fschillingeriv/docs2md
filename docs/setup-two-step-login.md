---
URL: https://bitwarden.com/help/setup-two-step-login/
---

# Two-Step Login Methods

> [!TIP] New device verification
> **March 4 2025**: To increase account security, Bitwarden will begin requiring additional verification for users **who do not use two-step login** when [logging into your account from a new device or after clearing browser cookies](https://bitwarden.com/help/new-device-verification/). You may have received an email and product notification indicating this.
> 
> After entering your Bitwarden master password, you will be prompted to enter a one-time verification code sent to your account email. Alternatively, you can:
> 
> - Set up two-step login by following any of the guides on this page.
> - Opt-out of this feature (**Turn off new device login protection**) from the Settings → My account screen in the Danger Zone section.

Using two-step login (also called two-factor authentication, or 2FA) protects your Bitwarden vault in case someone gets ahold of your master password. It works by requiring authentication from another source when you log in. If you are unfamiliar with the basics of 2FA, check out our [Field Guide](https://bitwarden.com/help/bitwarden-field-guide-two-step-login/).

[![Vimeo Video](https://vumbnail.com/1060246387.jpg)](https://vimeo.com/1060246387)
*[Watch on Vimeo](https://vimeo.com/1060246387)*

There are many different methods available for two-step login. You can have as many active as you'd like. What's important is that any form of two-step login is active to be sure your account is protected.

## Two-step login for individuals

Anyone can set up two-step login on their individual account by visiting the web app and choosing**Settings**→ **Security**→ **Two-step login**. Set up at least one of the following two-step login methods. Setup instructions are available for each:

| **Method** | **Setup instructions** | **Subscription requirements** |
|------|------|------|
| FIDO2 WebAuthn credentials (for example, hardware keys like YubiKeys and Google Titan) | [**Setup instructions**](https://bitwarden.com/help/setup-two-step-login-fido/) | Free for all |
| Authenticator app (for example, [Bitwarden Authenticator](https://bitwarden.com/help/bitwarden-authenticator/)) | [**Setup instructions**](https://bitwarden.com/help/setup-two-step-login-authenticator/) | Free for all |
| Email | [**Setup instructions**](https://bitwarden.com/help/setup-two-step-login-email/) | Free for all |
| Duo Security with Duo Push, SMS, phone call, and security keys | [**Setup instructions**](https://bitwarden.com/help/setup-two-step-login-duo/) | Requires premium |
| YubiKey OTP (any 4/5 series device or YubiKey NEO/NFC) | [**Setup instructions**](https://bitwarden.com/help/setup-two-step-login-yubikey/) | Requires premium |

## Two-step login for Teams and Enterprise

While each user can activate two-step login on their accounts using the methods on the chart above, Teams and Enterprise organizations have additional options:

| **Method** | **Setup instructions** | Subscription requirements |
|------|------|------|
| Duo Security with Duo Push, SMS, phone call, and security keys | Click [**here**](https://bitwarden.com/help/setup-two-step-login-duo/). | Requires Teams or Enterprise |

Additionally, Enterprise organizations can require two-step login with a [policy](https://bitwarden.com/help/policies/#two-step-login/), and the same protection can be achieved outside of Bitwarden using your Identity Provider when using Single Sign-On (SSO).

## Using multiple methods

You can enable multiple two-step login methods. When you log in to a vault that has multiple enabled methods, Bitwarden will prompt you for the highest-priority method according to the following order of preference:

1. Duo (organizations)
2. FIDO2 WebAuthn
3. YubiKey
4. Duo (individual)
5. Authenticator app
6. Email

> [!WARNING] Email 2FA & SSO
> Two-step login via email is not recommended if you are using [**login with SSO**](https://bitwarden.com/help/using-sso/)**,**as using multiple methods will cause errors. Consider setting up [two-step login via a free authenticator](https://bitwarden.com/help/setup-two-step-login-authenticator/) instead.

Any option will work, though. Authenticate with a lower-preference method by selecting the **Use another two-step login method** button:

### Web app

![Use another two-step login method ](https://bitwarden.com/assets/6pZaDONKwdhsCVDxz4fEoP/16a2053bf3a08a0449a0db1410fa752d/2025-02-28_08-56-53.png)

### Browser extension

![Use another two-step login method](https://bitwarden.com/assets/X0JAzFLcwRr4smlsMYCf7/0aa1f3c0cf56dd8e062e1e89fd99e43d/2025-03-17_10-55-29.png)

### Mobile

![Use another two-step login method](https://bitwarden.com/assets/2iyAQzp5BrmXPbIqKp9aB5/6b7bc9726ade6a5ef79cf4877e5c30ec/2025-03-18_09-30-31.png)

### Desktop

![Use another two-step login method](https://bitwarden.com/assets/36novNT7xJ8ZJSoG66MQXg/774092e3a3361e3a92d3bd84786b260e/setup-two-step-login-1.png)
