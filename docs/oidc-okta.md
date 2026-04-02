---
URL: https://bitwarden.com/help/oidc-okta/
---

# Okta OIDC

This article contains **Okta-specific** help for configuring login with SSO via OpenID Connect (OIDC). For help configuring login with SSO for another OIDC IdP, or for configuring Okta via SAML 2.0, see [OIDC Configuration](https://bitwarden.com/help/configure-sso-oidc/) or [Okta SAML Implementation](https://bitwarden.com/help/saml-okta/).

Configuration involves working simultaneously within the Bitwarden web app and the Okta Admin Portal. As you proceed, we recommend having both readily available and completing steps in the order they are documented.

## Open SSO in the web vault

Log in to the Bitwarden [web app](https://bitwarden.com/help/getting-started-webvault/) and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)

Select **Settings** → **Single sign-on** from the navigation:

![OIDC configuration](https://bitwarden.com/assets/51wSToXTHHVmBCrLrE8T0E/85aa432ea19eadf0195317f4f233e973/2024-12-04_09-41-46.png)

If you haven't already, create a unique **SSO identifier**for your organization. Otherwise, you don't need to edit anything on this screen yet, but keep it open for easy reference.

> [!TIP] Self-hosting, use alternative Member Decryption Options.
> There are alternative **Member decryption options**. Learn how to get started using [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/) or [Key Connector](https://bitwarden.com/help/about-key-connector/).

## Create an Okta app

In the Okta Admin Portal, select **Applications** → **Applications** from the navigation. On the Applications screen, select the **Create App Integration** button. For Sign-on method, select **OIDC - OpenID Connect**. For Application type, select **Web Application**:

![Create App Integration](https://bitwarden.com/assets/7fGYbP4aawIh8eorrQF6b7/a52951b16123a3e2f4d7bb293ba22a20/okta-createapp.png)

On the **New Web App Integration** screen, configure the following fields:

| **Field** | **Description** |
|------|------|
| App integration name | Give the app a Bitwarden-specific name. |
| Grant type | Enable the following [grant types](https://developer.okta.com/docs/concepts/oauth-openid/#choosing-an-oauth-2-0-flow): - Client acting on behalf of itself → **Client Credentials** - Client acting on behalf of a user → **Authorization Code** |
| Sign-in redirect URIs | Set this field to your **Callback Path**, which can be retrieved from the Bitwarden SSO Configuration screen. For cloud-hosted customers, this is `https://sso.bitwarden.com/oidc-signin` or `https://sso.bitwarden.eu/oidc-signin`. For self-hosted instances, this is determined by your [configured server URL](https://bitwarden.com/help/install-on-premise/#configure-your-domain/), for example `https://your.domain.com/sso/oidc-signin`. |
| Sign-out redirect URIs | Set this field to your **Signed Out Callback Path**, which can be retrieved from the Bitwarden SSO Configuration screen. |
| Assignments | Use this field to designate whether all or only select groups will be able to use Bitwarden Login with SSO. |

Once configured, select the **Next** button.

### Get client credentials

On the Application screen, copy the **Client ID** and **Client secret** for the newly created Okta app:

![App Client Credentials ](https://bitwarden.com/assets/6Q5iWqSrrXUp4s197bfyRt/d1d85d41c31ce60029d84fa6738372f8/okta-clientcredentials.png)

You will need to use both values [during a later step](https://bitwarden.com/help/oidc-okta/#back-to-the-web-vault/).

### Get authorization server information

Select **Security** → **API** from the navigation. From the **Authorization Servers** list, select the server you would like to use for this implementation. On the **Settings** tab for the server, copy the **Issuer** and **Metadata URI** values:

![Okta Authorization Server Settings ](https://bitwarden.com/assets/7hUKbE9s9HGJUwbqC2W36u/11cee32a7b469a662ae35b9c3cc1a2ba/okta-authserver.png)

You will need to use both values [during the next step](https://bitwarden.com/help/oidc-okta/#back-to-the-web-vault/).

## Back to the web app

At this point, you have configured everything you need within the context of the Okta Admin Portal. Return to the Bitwarden web app to configure the following fields:

| **Field** | **Description** |
|------|------|
| Authority | Enter the [retrieved Issuer URI](https://bitwarden.com/help/oidc-okta/#get-authorization-server-information/) for your Authorization Server. |
| Client ID | Enter the [retrieved Client ID](https://bitwarden.com/help/oidc-okta/#get-client-credentials/) for your Okta app. |
| Client Secret | Enter the [retrieved Client secret](https://bitwarden.com/help/oidc-okta/#get-client-credentials/) for your Okta app. |
| Metadata Address | Enter the [retrieved Metadata URI](https://bitwarden.com/help/oidc-okta/#get-client-authorization-server-information/) for your Authorization Server. |
| OIDC Redirect Behavior | Select **Redirect GET**. Okta currently does not support Form POST. |
| Get Claims From User Info Endpoint | Enable this option if you receive URL too long errors (HTTP 414), truncated URLS, and/or failures during SSO. |
| Additional/Custom Scopes | Define custom scopes to be added to the request (comma-delimited). |
| Additional/Custom User ID Claim Types | Define custom claim type keys for user identification (comma-delimited). When defined, custom claim types are searched for before falling back on standard types. |
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

Enter the [configured organization identifier](https://bitwarden.com/help/oidc-okta/#/) and select **Log In**. If your implementation is successfully configured, you'll be redirected to the Okta login screen:

![Log in with Okta ](https://bitwarden.com/assets/3Rh2Bg17sCE57xJsUKfqwN/4342c56fa656be94ef90dd620251a868/okta-login.png)

After you authenticate with your Okta credentials, enter your Bitwarden master password to decrypt your vault!

> [!NOTE] Okta bookmark app
> Bitwarden does not support unsolicited responses, so initiating login from your IdP will result in an error. The SSO login flow must be initiated from Bitwarden. Okta administrators can create an [Okta Bookmark App](https://support.okta.com/help/s/article/How-do-you-create-a-bookmark-app?language=en_US) that will link directly to the Bitwarden web vault login page.
> 
> 1. As an admin, navigate to the **Applications** drop down located on the main navigation bar and select **Applications**.
> 2. Click **Browse App Catalog**.
> 3. Search for **Bookmark App**and click **Add Integration**.
> 4. Add the following settings to the application:
> 
> 1. Give the application a name such as **Bitwarden Login**.
> 2. In the **URL** field, provide the URL to your Bitwarden client such as `https://vault.bitwarden.com/#/login` or `your-self-hostedURL.com`.
> 5. Select **Done** and return to the applications dashboard and edit the newly created app.
> 6. Assign people and groups to the application. You may also assign a logo to the application for end user recognition. The Bitwarden logo can be obtained [here](https://github.com/bitwarden/brand/tree/master).
> 
> Once this process has been completed, assigned people and groups will have a Bitwarden bookmark application on their Okta dashboard that will link them directly to the Bitwarden web vault login page.
