---
URL: https://bitwarden.com/help/twostep-faqs/
---

# Two-Step Login FAQs

This article contains frequently asked questions (FAQs) regarding two-step login.

### Q: Can I use SMS 2FA?

**A:** Bitwarden does not support SMS 2FA due to vulnerabilities, including SIM hijacking. We do not recommend SMS 2FA for other accounts unless it is the only available method. Any second factor is recommended over having none, but most alternatives are safer than SMS 2FA.

### Q: Can I require my organization's users to use two-step login?

**A:** You can require your organization's users to use two-step login by enabling the [two-step login policy](https://bitwarden.com/help/policies/#two-step-login/). Additionally, you can setup [organization-wide Duo 2FA](https://bitwarden.com/help/setup-two-step-login-duo/) to ensure that all of your users have a secure two-step login method at their disposal.

### Q: Is FIDO U2F or FIDO2 WebAuthn supported on my iOS or Android app?

**A:** Yes! Please see [two-step login via FIDO2 WebAuthn](https://bitwarden.com/help/setup-two-step-login-fido/).

### Q: Why is Bitwarden not asking for my enabled two-step login method?

**A:** In most cases, one of two things is happening:

1. You may be already logged in to Bitwarden and only unlocking your vault. Two-step login is required to **log in** but not to **unlock**. For more information on the difference between logging in and unlocking, see [vault timeout action](https://bitwarden.com/help/vault-timeout/#session-timeout-action/).
2. You may have previously checked the **Remember me** checkbox on a device when accessing your vault using two-step login.

![Remember me option ](https://bitwarden.com/assets/6ZKXQZRh1riGuGy44rlebh/7985d990f64c1ee20556aa88b63b591a/2024-12-02_11-26-14.png)

The **Remember me** options is enabled per-device, not globally for the account, and will be active for 30 days once turned on. You will need to **Deauthorize Sessions** from your web vault (**Settings** → **My Account**) to make any/all devices continue asking for your two-step login method.

### Q: Does Log in with Device work with two-step login?

**A:** Yes, Log in with Device will substitute the need to enter your master password but users will still need to complete two-step login if it is enabled on the account and if **Remember me** was not previously selected for that device.
