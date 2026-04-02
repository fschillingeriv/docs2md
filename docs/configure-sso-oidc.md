---
URL: https://bitwarden.com/help/configure-sso-oidc/
---

# Generic OIDC

## Step 1: Set an SSO identifier

Users who [authenticate their identity using SSO](https://bitwarden.com/help/using-sso/#login-using-sso/) will be required to enter an **SSO identifier** that indicates the organization (and therefore, the SSO integration) to authenticate against. To set a unique SSO Identifier:

1. Log in to the Bitwarden [web app](https://bitwarden.com/help/getting-started-webvault/) and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
2. Navigate to **Settings** → **Single sign-on**, and enter a unique **SSO Identifier** for your organization:

![Enter an identifier ](https://bitwarden.com/assets/6pr4tqMnrLCvwDBMlba5x7/7ef7563f7017f58adffff5d15ac68512/2024-12-04_09-39-25.png)
3. Proceed to **Step 2: Enable login with SSO**.

> [!NOTE] Sharing organization identifier
> You will need to share this value with users once the configuration is ready to be used.

## Step 2: Enable login with SSO

Once you have your SSO identifier, you can proceed to enabling and configuring your integration. To enable login with SSO:

1. On the **Settings** → **Single sign-on** view, check the **Allow SSO authentication** checkbox:

![OIDC configuration](https://bitwarden.com/assets/51wSToXTHHVmBCrLrE8T0E/85aa432ea19eadf0195317f4f233e973/2024-12-04_09-41-46.png)
2. From the **Type** dropdown menu, select the **OpenID Connect** option. If you intend to use SAML instead, switch over the the [SAML Configuration guide](https://bitwarden.com/help/configure-sso-saml/).

> [!TIP] Self-hosting, use alternative Member Decryption Options.
> There are alternative **Member decryption options**. Learn how to get started using [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/) or [Key Connector](https://bitwarden.com/help/about-key-connector/).

## Step 3: Configuration

From this point on, implementation will vary provider-to-provider. Jump to one of our specific **implementation guides** for help completing the configuration process:

| Provider | Guide |
|------|------|
| Azure | [Azure Implementation Guide](https://bitwarden.com/help/oidc-azure/) |
| Okta | [Okta Implementation Guide](https://bitwarden.com/help/oidc-okta/) |

### Configuration reference materials

The following sections will define fields available during single sign-on configuration, agnostic of which IdP you are integration with. Fields that must be configured will be marked (**required**).

> [!NOTE] OpenID proficiency 
> **Unless you are comfortable with OpenID Connect**, we recommend using one of the [above implementation guides](https://bitwarden.com/help/configure-sso-oidc/#step-3-configuration/) instead of the following generic material.

| **Field** | **Description** |
|------|------|
| Callback Path | (**Automatically generated**) The URL for authentication automatic redirect. For cloud-hosted customers, this is `https://sso.bitwarden.com/oidc-signin` or `https://sso.bitwarden.eu/oidc-signin.` For self-hosted instances, this is determined by your [configured server URL](https://bitwarden.com/help/install-on-premise/#configure-your-domain/), for example `https://your.domain.com/sso/oidc-signin`. |
| Signed Out Callback Path | (**Automatically generated**) The URL for sign-out automatic redirect. For cloud-hosted customers, this is `https://sso.bitwarden.com/oidc-signedout` or `https://sso.bitwarden.eu/oidc-signedout`. For self-hosted instances, this is determined by your [configured server URL](https://bitwarden.com/help/install-on-premise/#configure-your-domain/), for example `https://your.domain.com/sso/oidc-signedout`. |
| Authority | (**Required**) The URL of your authorization server ("Authority"), which Bitwarden will perform authentication against. For example, `https://your.domain.okta.com/oauth2/default `or `https://login.microsoft.com/<TENANT_ID>/v2.0`. |
| Client ID | (**Required**) An identifier for the OIDC client. This value is typically specific to a constructed IdP app integration, for example an [Azure app registration](https://bitwarden.com/help/oidc-azure/) or [Okta web app](https://bitwarden.com/help/oidc-okta/). |
| Client Secret | (**Required**) The client secret used in conjunction with the client ID to exchange for an access token. This value is typically specific to a constructed IdP app integration, for example an [Azure app registration](https://bitwarden.com/help/oidc-azure/) or [Okta Web App](https://bitwarden.com/help/oidc-okta/). |
| Metadata Address | (**Required if Authority is not valid**) A Metadata URL where Bitwarden can access authorization server metadata as a JSON object. For example, `https://your.domain.okta.com/oauth2/default/.well-known/oauth-authorization-server` |
| OIDC Redirect Behavior | (**Required**) Method used by the IdP to respond to authentication requests from Bitwarden. Options include **Form POST**and **Redirect GET**. |
| Get claims from user info endpoint | Enable this option if you receive URL too long errors (HTTP 414), truncated URLS, and/or failures during SSO. |
| Additional/custom scopes | Define custom scopes to be added to the request (comma-delimited). |
| Additional/custom user id claim types | Define custom claim type keys for user identification (comma-delimited). When defined, custom claim types are searched for before falling back on standard types. |
| Additional/custom email claim types | Define custom claim type keys for users' email addresses (comma-delimited). When defined, custom claim types are searched for before falling back on standard types. |
| Additional/custom name claim types | Define custom claim type keys for users' full names or display names (comma-delimited). When defined, custom claim types are searched for before falling back on standard types. |
| Requested authentication context class reference values | Define authentication context class reference identifiers (`acr_values`) (space-delimited). List `acr_values `in preference-order. |
| Expected "acr" Claim Value in Response | Define the `acr `claim value for Bitwarden to expect and validate in the response. |

### OIDC attributes & claims

An **email address is required for account provisioning**, which can be passed as any of the attributes or claims in the below table.

A unique user identifier is also highly recommended. If absent, email will be used in its place to link the user.

Attributes/claims are listed in order of preference for matching, including fallbacks where applicable:

| **Value** | **Claim/Attribute** | **Fallback claim/attribute** |
|------|------|------|
| Unique ID | Configured Custom User ID Claims NameID (when not transient) urn:oid:0.9.2342.19200300.100.1.1 Sub UID UPN EPPN | |
| Email | Configured Custom Email Claims Email http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress urn:oid:0.9.2342.19200300.100.1.3 Mail EmailAddress | Preferred_Username Urn:oid:0.9.2342.19200300.100.1.1 UID |
| Name | Configured Custom Name Claims Name http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name urn:oid:2.16.840.1.113730.3.1.241 urn:oid:2.5.4.3 DisplayName CN | First Name + “ “ + Last Name (see below) |
| First Name | urn:oid:2.5.4.42 GivenName FirstName FN FName Nickname | |
| Last Name | urn:oid:2.5.4.4 SN Surname LastName | |
