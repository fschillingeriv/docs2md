---
URL: https://bitwarden.com/help/login-with-passkeys/
---

# Log In & Unlock with Passkeys

> [!NOTE] Autofill vs. Log in with Passkeys
> Bitwarden offers three passkey features: use [passkeys to log in and unlock](https://bitwarden.com/help/login-with-passkeys/) your Bitwarden account, use [passkeys for 2FA](https://bitwarden.com/help/setup-two-step-login-fido/) on your Bitwarden account, and [autofill stored passkeys](https://bitwarden.com/help/storing-passkeys/) for other websites and services.

Passkeys offer secure authentication for your Bitwarden account. Use them to log in and, with a [PRF-capable setup](https://bitwarden.com/help/login-with-passkeys/#unlock-vault-requirements/), automatically [unlock your vault](https://bitwarden.com/help/understand-log-in-vs-unlock/) without entering your master password. Passkeys bypass two-step login, offering a streamlined alternative to traditional password-based authentication.

## Requirements

Using passkeys to log in and unlock your Bitwarden account is currently supported in these Bitwarden apps:

- Browser extension in Chromium-based browsers
- Web app

> [!NOTE] macOS passkey bug
> On macOS, creating and using PRF-capable passkeys to unlock your vault requires a Chromium-based browser.

Passkeys used to log in to Bitwarden require user verification, such as biometrics or a security key to authenticate and use your passkey.

### Unlock vault requirements

To decrypt and unlock your vault with a passkey, you need to [set up encryption](https://bitwarden.com/help/login-with-passkeys/#set-up-encryption-for-unlock/) for that specific passkey. Your browser (like Google Chrome) and authenticator (like YubiKey 5) must both be [PRF-capable](https://bitwarden.com/blog/prf-webauthn-and-its-role-in-passkeys/) to use this unlock method. If either is not PRF-capable, you'll need to use a different unlock method, such as your master password or [PIN](https://bitwarden.com/help/unlock-with-pin/).

**PRF capability varies by equipment and environment.** For example, Google Chrome is PRF-capable, but Chrome profiles are not. YubiKey 5 is a PRF-capable authenticator. Additionally, Windows 10 is known to have issues with PRF-capable passkeys.

### Passkey restrictions

You cannot use passkeys with Bitwarden if you’re in an organization that uses the [Require SSO policy](https://bitwarden.com/help/policies/#require-single-sign-on-authentication/), SSO with [trusted devices](https://bitwarden.com/help/about-trusted-devices/), or [Key Connector](https://bitwarden.com/help/about-key-connector/).

Bitwarden will not prompt or allow you to save a passkey for logging in to any Bitwarden account. This prevents the circular problem of needing access to your vault to log in to the very same vault.

## Manage passkeys

Use the web app to create, update, and remove passkeys that are used to access your Bitwarden account.

### Create a passkey

You can add up to five passkeys to your Bitwarden account. To create a passkey for logging in to Bitwarden:

1. In the web app, go to **Settings** → **Security**.
2. Select **Master password**.
3. Within the **Log in with passkey**section, select **Turn on** or, if you've already setup a passkey, **New passkey**. You'll be prompted to enter your master password.
4. Follow prompts from your browser to create a FIDO2 passkey. You can complete user verification using a factor like a biometric or by creating a PIN.

> [!TIP] Browser might have default passkey prompt.
> You may need to cancel out of a default authenticator your browser will want you to use, for example if you want to use a hardware security key on a macOS device that will prioritize Touch ID.
5. Enter a **Name** for your passkey.
6. (Optional) If your [browser and authenticator are PRF-capable](https://bitwarden.com/help/login-with-passkeys/#unlock-vault-requirements/), the **Use for vault encryption** setting will be checked by default. This allows your passkey to decrypt and unlock your vault. Uncheck this option if you do not want the passkey to unlock your vault:

![Use passkey for vault encryption](https://bitwarden.com/assets/2gsO1o5tDU7s7LXvcpaL7w/56a8a797155760fe6fbd1d2e2d92b59b/2025-12-31_11-19-58.png)
*Use passkey for vault encryption*
7. Select **Turn on**.

### Set up encryption for unlock

If your [browser and authenticator are PRF-capable](https://bitwarden.com/help/login-with-passkeys/#unlock-vault-requirements/), you can decrypt and unlock your vault with a passkey. There are two ways to do this:

- When creating a passkey, keep the **Use for vault encryption** setting checked ([step 6](https://bitwarden.com/help/login-with-passkeys/#create-a-passkey/)).
- For an existing passkey, go to **Settings** → **Security** → **Master Password** and select **Set up encryption** next to the passkey:

![Passkeys list](https://bitwarden.com/assets/TpXTFNlF2hzRaUaLmxAXr/6710e5ab7c98efcb11547dc6038fdf7d/Passkeys_list.png)
*Passkeys list*

Your passkeys list shows the encryption status for each passkey: **Used for encryption**, supported but not active (**Set up encryption**), or **Encryption not supported**.

### Remove a passkey

To delete a passkey from your Bitwarden account, go to **Settings** → **Security** → **Master Password** and select **Remove** next to the passkey. This disconnects the passkey from Bitwarden, but the private key will remain in your FIDO2 authenticator.

### Lost or deleted passkey

If you lose or delete a passkey, such as from a security key, Windows Hello, or Apple Passwords, it can no longer be used to access your vault. Should that happen, your master password is required to unlock your vault, so it must be strong and memorable. Consider creating and securely storing a [security readiness kit](https://bitwarden.com/resources/bitwarden-security-readiness-kit/) so your critical account details are always within reach, even when a passkey is lost.

## Log in and unlock with your passkey

After you create a passkey, you can use it with the Bitwarden web app and Chromium-based browser extensions. For PRF-capable passkeys on macOS, you'll need a Chromium-based browser for the web app.

> [!NOTE] Known Linux defect for login with passkey.
> If you're logging in to the browser extension on **Linux**, you need to pop out the extension before attempting to log in or unlock with a passkey:
> 
> 
> ![Browser extension pop-out](https://bitwarden.com/assets/1cbJy0jLBmSQmRumvYzVwp/a9e43f4c154686249056924eb3e56323/pop_out_screenshot.png)
> *Browser extension pop-out*

To log in with a passkey and unlock your vault:

1. On the Bitwarden login screen, select **Log in with passkey** where you'd usually enter your email address.
2. Follow prompts from your browser to read the passkey. This will authenticate you with Bitwarden.
3. What happens next depends on if your passkey is [set up for vault encryption](https://bitwarden.com/help/login-with-passkeys/#set-up-encryption-for-unlock/):

 - If your passkey is set up for vault encryption, you're done! The passkey is used to decrypt and unlock your vault.
 - If your passkey is not set up for vault encryption, enter your master password and select **Unlock**, or use another unlock method you previously configured.

To unlock your vault when you're already logged in, select **Unlock with Passkey** on the locked vault screen. Follow prompts from your browser to read the passkey. This will unlock your account, opening your vault.

## How it works

The mechanics of logging in with passkeys differ based on whether your passkey is [set up with encryption](https://bitwarden.com/help/login-with-passkeys/#set-up-encryption-for-unlock/).

### Passkeys with encryption

#### Create a passkey

When a PRF-compatible passkey is registered for log in to Bitwarden and encryption is turned on:

1. A **passkey public and private key pair** is generated by the authenticator via the WebAuthn API. This key pair, by definition, is what constitutes your passkey.
2. A **PRF symmetric key** is generated by the authenticator via the WebAuthn API's PRF extension. This key is derived from an **internal secret** unique to your passkey and a **salt** provided by Bitwarden.
3. A **PRF public and private key pair** is generated by the Bitwarden client. The PRF public key encrypts your **account encryption key**, which your client will have access to by virtue of being logged in and unlocked, and the resulting **PRF-encrypted account encryption key** is sent to the server.
4. The **PRF private key** is encrypted with the **PRF symmetric key** (see Step 2) and the resulting **PRF-encrypted private key** is sent to the server.
5. Your client sends data to Bitwarden servers to create a new passkey credential record for your account. If your passkey is registered with support for vault encryption and decryption, this record includes:

 - The passkey name
 - The passkey public key
 - The PRF public key
 - The PRF-encrypted account encryption key
 - The PRF-encrypted private key

Your passkey private key, which is required to accomplish authentication, only ever leaves the client in an encrypted format.

#### Log in with your passkey

When a passkey is used to log in and, specifically, to decrypt your vault data:

1. Using WebAuthn API public key cryptography, your authentication request is asserted and affirmed.
2. Your **PRF-encrypted account encryption key** and **PRF-encrypted private key** are sent from the server to your client.
3. Using the same **salt** provided by Bitwarden and the **internal secret** unique to your passkey, the **PRF symmetric key** is re-created locally.
4. The **PRF symmetric key** is used to decrypt your **PRF-encrypted private key**, resulting in your **PRF private key**.
5. The **PRF private key** is used to decrypt your **PRF-encrypted account encryption key**, resulting in your **account encryption key**. Your account encryption key is used to decrypt your vault data.

If you're already logged in and then use a passkey to unlock your vault, your encrypted keys are already on your device from login, so the authentication and key retrieval steps are skipped.

### Passkeys without encryption

#### Create a passkey

When a passkey is registered for log in to Bitwarden and encryption remains turned off:

1. A **passkey public and private key pair** is created. This key pair, by definition, is what constitutes your passkey.
2. Your client sends data to Bitwarden servers to create a new passkey credential record for your account. If your passkey is not registered with support for vault encryption and decryption, this record includes:

 - The passkey's name
 - The passkey's public key

Your passkey's private key, which is required to accomplish authentication, only ever leaves the client in an encrypted format.

#### Log in with your passkey

When a passkey is used to log in, your authentication request is asserted and affirmed using WebAuthn API public key cryptography. You will then be required to decrypt your vault using your master password.
