---
URL: https://bitwarden.com/help/ping-identity-oidc-implementation/
---

# Ping Identity OIDC

This article contains Ping Identity specific help for configuring Login with SSO via OpenID Connect (OIDC). For help configuring Login with SSO for another OIDC IdP, or for configuring Ping Identity via SAML 2.0, see [OIDC Configuration](https://bitwarden.com/help/configure-sso-oidc/) or [Ping Identity SAML implementation](https://bitwarden.com/help/ping-identity-saml-implementation/).

Configuration involves working simultaneously within the Bitwarden web app and the Ping Identity Administrator Portal. As you proceed, we recommend having both readily available and completing steps in the order they are documented.

## Open SSO in the web vault

Log in to the Bitwarden [web app](https://bitwarden.com/help/getting-started-webvault/) and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)

Select **Settings** → **Single sign-on** from the navigation:

![OIDC configuration](https://bitwarden.com/assets/51wSToXTHHVmBCrLrE8T0E/85aa432ea19eadf0195317f4f233e973/2024-12-04_09-41-46.png)

If you haven't already, create a unique **SSO identifier**for your organization. Otherwise, you don't need to edit anything on this screen yet, but keep it open for easy reference.

> [!TIP] Self-hosting, use alternative Member Decryption Options.
> There are alternative **Member decryption options**. Learn how to get started using [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/) or [Key Connector](https://bitwarden.com/help/about-key-connector/).

## Create OIDC app

In the Ping Identity Administrator Portal, select **Applications** and the + Icon at the top of the screen to open the **Add Application** screen:

![Ping Identity OIDC App](https://bitwarden.com/assets/3upFJSqFSgStI3FB5hSIDH/0714a45788207aed199dc3f3df78e6dd/2024-07-22_16-14-00.png)

### Add application

1. Enter a Bitwarden Specific name in the **Application Name** field. Optionally, add desired description details as needed.
2. Select the **OIDC Web App** option and select **Save** once you have finished.

### Configure application

On the Application screen, select the **Configuration** tab and then the edit button located on the top right hand of the screen.

![Ping OIDC Configuration Edit](https://bitwarden.com/assets/7JxMu92pW8hFkRV7Mmh5Qr/870237c0d0580c7407973aeef0109d2c/2024-07-25_11-30-30.png)

In the edit screen, fill in the following values retrieved from the Bitwarden Single sign-on screen:

| **Ping Identity Field** | **Description** |
|------|------|
| Redirect URIs | Copy and paste the **Callback path** value retrieved from the Bitwarden Single sign-on page. |
| Signoff URLs | Copy and Paste the **Signed out callback path** value retrieved from the Bitwarden Single sign-on page. |

 Once this step has been completed, select **Save** and return to the **Configuration** tab on the Ping Identity Application screen. No other values on this screen require editing.

## Resources

On the Resources tab of the Ping Identity Application screen, select the **edit** icon and enable the following allowed scopes:

- email
- openid

## Back to the web app

At this point, you have configured everything you need within the context of Ping Identity. Return to the Bitwarden web app to configure the following fields:

| **Field** | **Description** |
|------|------|
| Authority | Enter `https://auth.pingone.eu/<TENANT_ID>`, where `TENANT_ID `is the **Environment ID** on Ping Identity. |
| Client ID | Enter the App's **Client ID**retrieved from the Application's Configuration tab. |
| Client Secret | Enter the Secret Value of the created client secret. Select **Generate New Secret**on the application's Configuration tab. |
| Metadata Address | For Ping Identity implementations as documented, you can leave this field blank. |
| OIDC Redirect Behavior | Select either **Form POST** or **Redirect GET**. |
| Get Claims From User Info Endpoint | Enable this option if you receive URL too long errors (HTTP 414), trusted URLS, and/or failures during SSO. |
| Additional/Custom Scopes | Define custom scopes to be added to the request (comma-delimited). |
| Additional/Custom Email Claim Types | Define custom claim type keys for users' email addresses (comma-delimited). When defined, custom claim types are searched for before falling back on standard types. |
| Additional/Custom Name Claim Types | Define custom claim type keys for users' full names or display names (comma-delimited). When defined, custom claim types are searched for before falling back on standard types. |
| Requested Authentication Context Class Reference values | Define Authentication Context Class Reference identifiers (`acr_values`) (space-delimited). List `acr_values `in preference-order. |
| Expected "acr" Claim Value in Response | Define the `acr `Claim Value for Bitwarden to expect and validate in the response. |

When you are done configuring these fields, **Save** your work.

> [!TIP] Policies for SSO Guides
> You can require users to log in with SSO by activating the single sign-on authentication policy. Please note, this will require activating the single organization policy as well. [Learn more](https://bitwarden.com/help/policies/).

## Test the configuration

Once your configuration is complete, test it by navigating to [https://vault.bitwarden.com](https://vault.bitwarden.com), entering your email address and selecting the **Use single sign-on** button:

![Log in options screen](https://bitwarden.com/assets/3BdlHeogd42LEoG06qROyQ/c68021df4bf45d72e9d37b1fbf5a6040/login.png)

Enter the [configured organization identifier](https://bitwarden.com/help/configure-sso-saml/#step-1-enabling-login-with-sso/) and select **Log In**. If your implementation is successfully configured, you will be redirected to the Ping Identity login screen:

![Ping Identity SSO](https://bitwarden.com/assets/1QwyIzAp4JtyGwNLXZNXFI/6d1cc0ca3f278f46d7ad251ff2898dd4/2024-07-22_12-18-19.png)

After you authenticate with your Ping credentials, enter your Bitwarden master password to decrypt your vault!

> [!NOTE] SSO must be initiated from Bitwarden
> Bitwarden does not support unsolicited responses, so initiating login from your IdP will result in an error. The SSO login flow must be initiated from Bitwarden.

## Next steps

- Educate your organization members on how to [use login with SSO](https://bitwarden.com/help/using-sso/).
