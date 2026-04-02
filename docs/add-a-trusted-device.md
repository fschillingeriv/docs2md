---
URL: https://bitwarden.com/help/add-a-trusted-device/
---

# Add a Trusted Device

When you become a member of an organization, the device you log in with for the first time will automatically be registered as a trusted device. Once this occurs, all you'll need to do to log in to Bitwarden and decrypt your data is complete your company's established single sign-on flow.

> [!TIP] TDE Remember Me?
> Devices will be trusted by default when you log in on them. It is highly recommended that you uncheck the **Remember this device** option when logging in on a public or shared device.

When you log into a new device however, you'll need to approve, or trust, that device. There are a few methods for doing so:

- **Approve from another device**: If you're already logged into Bitwarden on another device, you can approve the new device from there:

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
- **Use master password**: If you are an admin or owner, or joined your organization before SSO with trusted devices was implemented, and therefore still have a master password associated with your account, you can enter it to approve the device.

![Request admin approval](https://bitwarden.com/assets/5IMJBQOrklcOuLVEpaR6gX/60ead8f10e34f7acd2467eaaa34ff93d/2025-06-16_15-22-15.png)
- **Request admin approval**: You can send a device approval request to admins and owners within your organization for approval. You **must** be [enrolled in account recovery](https://bitwarden.com/help/account-recovery/#self-enroll-in-account-recovery/) to request admin approval, though you may have been [automatically enrolled](https://bitwarden.com/help/account-recovery/#automatic-enrollment/) when you joined the organization. In many cases, this will be the only option available to you ([learn more](https://bitwarden.com/help/approve-a-trusted-device/)).

> [!TIP] If you used admin approval for TDE
> If you use this option, you'll get an email informing you to continue logging in on the new device when you're approved. You must take action by logging in to the new device within 12 hours, or the approval will expire.

Once the new device becomes trusted, all you'll need to do to log in to Bitwarden and decrypt your vault data is complete your company's established single sign-on flow.

## Adding your first trusted device

The initial client used to access Bitwarden for users who were invited with Just in Time (JIT) provisioning using [login with SSO](https://bitwarden.com/help/about-sso/) will become their first trusted device. If the initial client accessed is the Bitwarden desktop or mobile app, this device can be used to approve additional devices.

For the desktop or mobile app to become the first trusted device, the user should not use the organization invite link. Instead, open the mobile or desktop app and select the **Enterprise single sign-on** option to begin the JIT process.

## Remove a trusted device

Devices will remain trusted until:

- The application or extension is uninstalled.
- The web browser's memory is cleared (web app only).

## Troubleshooting

If you're having trouble establishing device trust:

- On Chrome, check that **Allow sites to save data on your device** is turned on (**Settings** → **Privacy and security** → **Site settings** → **Additional content settings** → **On-device site data** → **Allow sites to save data on your device**).
