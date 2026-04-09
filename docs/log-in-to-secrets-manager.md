---
URL: https://bitwarden.com/help/log-in-to-secrets-manager/
---

# Log in to Secrets Manager

The end-to-end zero-knowledge encrypted Bitwarden account you use to log into Password Manager will be the same as what you use to log into Secrets Manager.

> [!TIP] Not SM CLI
> This article pertains to logging in to the Secrets Manager web vault. The [Secrets Manager CLI](https://bitwarden.com/help/secrets-manager-cli/), which is primarily used to script secrets injection into your applications and infrastructure, requires logging in with an [access token](https://bitwarden.com/help/access-tokens/).

## Master password

Your master password is the primary method for accessing your Bitwarden account. It's important that your master password is:

- **Memorable**: Bitwarden employees and systems have no knowledge of, way to retrieve, or way to reset your master password. **Do not forget your master password!**
- **Strong**: A longer, more complex, and less common master password is the best way to protect your account. Bitwarden provides a free password strength testing tool to test the strength of some memorable pass words you are considering.

> [!TIP] Tips to mitigate forgetting master password.
> Worried about forgetting your master password? Here's what to do:
> 
> - **Set up a hint**. In case you need a reminder, a master password hint email can be requested on the login screen. Make sure you use a hint that only you will understand.
> - **Designate a**[**trusted emergency contact**](https://bitwarden.com/help/emergency-access/). Users with premium access can grant account access to a friend or family member in the case of emergency.

Learn how to [change your master password](https://bitwarden.com/help/master-password/#change-master-password/), or what to do if you've [forgotten your master password](https://bitwarden.com/help/forgot-master-password/).

## Two-step login

Using [two-step login](https://bitwarden.com/help/bitwarden-field-guide-two-step-login/) (also called two-factor authentication or 2FA) to protect your Bitwarden account prevents a malicious actor from accessing your data even if they discover your master password by requiring authentication from a secondary device when you log in.

There are lots of different methods for two-step login, ranging from dedicated authenticator apps to hardware security keys. Whatever you choose, Bitwarden highly recommends that you secure your vault using two-step login.

### Free methods

Bitwarden offers several two-step login methods for free, including:

| **Method** | **Setup instructions** |
|------|------|
| via an authenticator app (for example, [Authy](https://authy.com/) or [Google Authenticator](https://support.google.com/accounts/answer/1066447?hl=en)) | Click [**here**](https://bitwarden.com/help/setup-two-step-login-authenticator/). |
| via email | Click [**here**](https://bitwarden.com/help/setup-two-step-login-email/). |
| via a FIDO WebAuthn Authenticator | Click [**here**](https://bitwarden.com/help/setup-two-step-login-fido/). |

### Premium methods

For premium users (including members of paid organizations), Bitwarden offers several advanced two-step login methods:

| **Method** | **Setup instructions** |
|------|------|
| via Duo Security with Duo Push, SMS, phone call, and security keys | Click [**here**](https://bitwarden.com/help/setup-two-step-login-duo/). |
| via YubiKey (any 4/5 series device or YubiKey NEO/NFC) | Click [**here**](https://bitwarden.com/help/setup-two-step-login-yubikey/). |

## Log in with device

Did you know you can log in to the Bitwarden web app using a secondary device instead of your master password? Logging in with a device is a passwordless approach to authentication, removing the need to enter your master password by sending authentication requests to any certain devices you're currently logged in to for approval. [Learn more](https://bitwarden.com/help/log-in-with-device/).

## Single sign-on

If your organization uses [login with SSO](https://bitwarden.com/help/about-sso/), you can access your Bitwarden web app [using your federated SSO credentials](https://bitwarden.com/help/using-sso/).
