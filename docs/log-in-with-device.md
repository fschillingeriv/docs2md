---
URL: https://bitwarden.com/help/log-in-with-device/
---

# Log In with Device

Set up log in with a device for faster, more convenient Bitwarden access. This login method, called passwordless authentication, eliminates the need to enter your master password every time you log in. Using **Log in with device**, any time you log into Bitwarden on one device, you can opt to use a different Bitwarden app you're logged in to to approve the authentication request instead of typing your master password.

[Learn about our zero-knowledge encryption implementation](https://bitwarden.com/help/log-in-with-device/#how-it-works/).

## Prepare to log in with a device

To set up logging in with a device:

- Log in normally to the initiating app (web app, browser extension, desktop, or mobile app) at least once so that Bitwarden can recognize your device.

> [!NOTE] Passwordless + Private Browsing
> Using Incognito mode or Private Browsing prevents Bitwarden from registering your browser, so you won't be able to log in with a device in a private browser window.

- Have a recognized account on an approving app (web app, browser extension, mobile or desktop app). Recognizing an account requires you to have successfully logged on to that device at any time.

> [!NOTE] Passwordless + Require SSO
> If, as a member of an Enterprise organization, you are subject to the [require SSO policy](https://bitwarden.com/help/policies/#require-single-sign-on-authentication/), you won't be able to use the **Log in with device** option. You'll need to [use SSO to log in](https://bitwarden.com/help/using-sso/#login-using-sso/) instead.

## Log in with a device

On the login screen of the initiating app, enter your email address and select **Continue**. Then, select the **Log in with device**option:

![Log in with a device](https://bitwarden.com/assets/7owqaTEe9Bo05wfLRZPhn8/38f1d0334964bb3d98a430b80b9d6b95/2025-09-09_10-03-52.png)

### Approve a log in request

Using **Log in with device**will send authentication requests to any Bitwarden app that you're currently logged in to for approval:

### Mobile app

To approve a request with the mobile app:

1. In the mobile app, navigate to **Settings** → **Account** **security**→ **Pending login requests**:

![Pending login requests on mobile](https://bitwarden.com/assets/1ZB3Pc8T0mlP96W3IZefrR/a22c8efe63a88941bad11a278b1d113d/2025-09-09_09-39-13.png)
*Pending login requests on mobile*
2. Locate and tap the pending device request.
3. Verify that fingerprint phrase matches and select **Confirm access**:

![Approve a login on mobile](https://bitwarden.com/assets/6xeP36n7g2dbwLI9YWjNg4/2aa9fdc96e765e963ee07f38ad0b6c06/2025-09-09_09-39-44.png)
*Approve a login on mobile*

### Browser extension

To approve a request with the browser extension:

1. In the browser extension, wait for a device approval request to be received or navigate to **Settings**→ **Account** **security**→ **Devices**:

![Devices view on browser extensions](https://bitwarden.com/assets/6OZfQt2jDDqa9F0MaUdBUq/1460f0ec04c63ab55da1f5eaf37ca469/2025-09-09_09-49-23.png)
*Devices view on browser extensions*
2. In the **Devices**view, locate and select the pending device request:

![Devices list on browser extensions](https://bitwarden.com/assets/64f1jZ30In2BbWDEUZVtxO/9de965d59fedca2bad4e325f4181f69a/2025-09-09_09-49-42.png)
*Devices list on browser extensions*
3. Verify that fingerprint phrase matches and select **Confirm access**:

![Approve a device on browser extensions](https://bitwarden.com/assets/2LFY10MMpI9G0ZcojcXveg/0a891ec5fa8f6052e5804841e7ec7724/2025-09-09_09-48-55.png)
*Approve a device on browser extensions*

### Web app

To approve a request with the web app:

> [!NOTE] Browser extensions & web app approval
> When requesting approval for a login of the browser extension, the extension will wait for up to two minutes for approval even if you click out of or minimize the extension window in order to approve the request using the web app.

1. In the web app, select the **Review login request**link in the banner notification or navigate to **Settings** → **Security**→ **Devices**:

![Approval request on web](https://bitwarden.com/assets/1K9FeC1OVOwyu0T8DMiwOp/cc88b5f47f0f243f5a655e77086871c9/2025-12-31_11-10-23.png)
*Approval request on web*
2. On the **Devices** tab, locate and select the pending device request:

![Device list on web app](https://bitwarden.com/assets/7GLmOwtReFuUD3uxPQ0LB8/ed5dbce83b2c428b9c2369270be1d959/2025-12-31_11-08-26.png)
*Device list on web app*
3. Verify that fingerprint phrase matches and select **Confirm access**:

![Confirm access with web app](https://bitwarden.com/assets/6s6Hdn9L1EyeRfBsmOcfgX/f6a13a34fdc59f815f7e4d51e981af47/2025-12-31_11-08-37.png)
*Confirm access with web app*

### Desktop app

To approve a request with the desktop app:

1. In the desktop app, wait for a device approval request to be received:

![Approve on desktop](https://bitwarden.com/assets/5cpkevhyuiSg82yfopvmc1/abd4d9949f342ff7efb3c289ec1942f5/2026-01-29_10-13-52.png)
*Approve on desktop*
2. Verify that fingerprint phrase matches and select **Confirm access**.

Note that this is a unique fingerprint that isn't the same as your [account fingerprint phrase](https://bitwarden.com/help/fingerprint-phrase/).

Requests expire after 15 minutes if they aren't approved or denied. If you are not receiving login requests, try refreshing the web app, or [manually syncing your vault](https://bitwarden.com/help/vault-sync/) from the mobile app. 

> [!NOTE] Passwordless & 2FA
> If you use the **Login with device**option, you'll still need to use any currently active [two-step login method](https://bitwarden.com/help/setup-two-step-login/).

## How it works

When logging in with a device is initiated:

1. The initiating client sends a request which includes the account email address, a unique **Auth-request Public Key**ª, and an access code, to an Authentication Request table in the Bitwarden database. Registered devices, meaning clients that are logged in and have a [device-specific GUID](https://bitwarden.com/help/administrative-data/) stored in the Bitwarden database, are provided the request.
2. When the request is approved, the approving client encrypts the account's **User Encryption key** using the **Auth-request public key** enclosed in the request.
3. The approving client then sends the **User Encryption key** to the Authentication Request record and marks the request fulfilled.
4. The initiating client requests the encrypted **User Encryption key**.
5. The initiating client then **locally**decrypts the **User Encryption key** using the **Auth-request private key.**
6. The initiating client then uses the access code to authenticate the user with the Bitwarden Identity service.
7. The initiating client can then retrieve the user's vault data and use the **User Encryption key** to decrypt it.

ª - **Auth-request Public and Private Keys** are uniquely generated for each passwordless login request and only exist for as long as the request does. Requests expire and are purged periodically if they aren't approved or denied.
