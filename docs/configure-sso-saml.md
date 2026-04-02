---
URL: https://bitwarden.com/help/configure-sso-saml/
---

# Generic SAML

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

![SAML 2.0 configuration ](https://bitwarden.com/assets/20720mRAluo6crSdTiYJrn/1175889d7f6ab42fe7614f34cdd1dcdd/2024-12-04_09-41-15.png)
2. From the **Type** dropdown menu, select the **SAML 2.0** option. If you intend to use OIDC instead, switch over to the [OIDC Configuration Guide](https://bitwarden.com/help/configure-sso-oidc/).

You can turn off the **Set a unique SP entity ID**option at this stage if you wish. Doing so will remove your organization ID from your SP entity ID value, however in almost all cases it is recommended to leave this option on.

> [!TIP] Self-hosting, use alternative Member Decryption Options.
> There are alternative **Member decryption options**. Learn how to get started using [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/) or [Key Connector](https://bitwarden.com/help/about-key-connector/).

## Step 3: Configuration

From this point on, implementation will vary provider-to-provider. Jump to one of our specific **implementation guides** for help completing the configuration process:

| **Provider** | **Guide** |
|------|------|
| AD FS | [AD FS Implementation Guide](https://bitwarden.com/help/saml-adfs/) |
| Auth0 | [Auth0 Implementation Guide](https://bitwarden.com/help/saml-auth0/) |
| AWS | [AWS Implementation Guide](https://bitwarden.com/help/saml-aws/) |
| Azure | [Azure Implementation Guide](https://bitwarden.com/help/saml-azure/) |
| Duo | [Duo Implementation Guide](https://bitwarden.com/help/saml-duo/) |
| Google | [Google Implementation Guide](https://bitwarden.com/help/saml-google/) |
| JumpCloud | [JumpCloud Implementation Guide](https://bitwarden.com/help/saml-jumpcloud/) |
| Keycloak | [Keycloak Implementation Guide](https://bitwarden.com/help/saml-keycloak/) |
| Okta | [Okta Implementation Guide](https://bitwarden.com/help/saml-okta/) |
| OneLogin | [OneLogin Implementation Guide](https://bitwarden.com/help/saml-onelogin/) |
| PingFederate | [PingFederate Implementation Guide](https://bitwarden.com/help/saml-pingfederate/) |

The following sections will define fields available during single sign-on configuration, agnostic of which IdP you are integration with. Fields that must be configured will be marked (**required**).

> [!NOTE] SAML confidence 
> **Unless you are comfortable with SAML 2.0**, we recommend using one of the [above implementation guides](https://bitwarden.com/help/configure-sso-saml/#step-3-configuration/) instead of the following generic material.

The single sign-on screen separates configuration into two sections:

- **SAML Service Provider Configuration** will determine the format of SAML requests.
- **SAML Identity Provider Configuration** will determine the format to expect for SAML responses.

### Service Provider Configuration

| **Field** | **Description** |
|------|------|
| SP Entity ID | (**Automatically generated**) The Bitwarden endpoint for authentication requests. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |
| SAML 2.0 Metadata URL | (**Automatically generated**) Metadata URL for the Bitwarden endpoint. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |
| Assertion Consumer Service (ACS) URL | (**Automatically generated**) Location where the SAML assertion is sent from the IdP. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |
| Name ID Format | Format Bitwarden will request of the SAML assertion. Must be cast as a string. Options include: -Unspecified (default) -Email address -X.509 Subject name -Windows Domain Qualified Name -Kerberos Principal Name -Entity identifier -Persistent -Transient |
| Outbound Signing Algorithm | The algorithm Bitwarden will use to sign SAML requests. Options include: - `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256` (default) - `http://www.w3.org/2000/09/xmldsig#rsa-sha384` - `http://www.w3.org/2000/09/xmldsig#rsa-sha512` |
| Signing Behavior | Whether/when SAML requests will be signed. Options include: -If IdP wants authn requests signed (default) -Always -Never |
| Minimum Incoming Signing Algorithm | Minimum strength of the algorithm that Bitwarden will accept in SAML responses. |
| Expect signed assertations | Check this checkbox if Bitwarden should expect responses from the IdP to be signed. |
| Validate certificates | Check this box when using trusted and valid certificates from your IdP through a trusted CA. Self-signed certificates may fail unless proper trust chains are configured within the Bitwarden login with SSO docker image. |

### Identity Provider Configuration

| **Field** | **Description** |
|------|------|
| Entity ID | (**Required**) Address or URL of your identity server or the IdP Entity ID. This field is case sensitive and must match the IdP value exactly. |
| Binding Type | Method used by the IdP to respond to Bitwarden SAML requests. Options include: -Redirect (recommended) -HTTP POST |
| Single Sign On Service URL | (**Required if Entity ID is not a URL**) SSO URL issued by your IdP. |
| Single log out service URL | Login with SSO currently **does not**support SLO. This option is planned for future use, however we strongly recommend pre-configuring this field. |
| X509 Public Certificate | (**Required**) The X.509 Base-64 encoded certificate body. Do not include the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines or portions of the CER/PEM formatted certificate. The certificate value is case sensitive, extra spaces, carriage returns, and other extraneous characters inside this field will cause certificate validation failure. Copy **only**the certificate data into this field. |
| Outbound Signing Algorithm | The algorithm your IdP will use to sign SAML responses/assertions. Options include: - `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256` (default) - `http://www.w3.org/2000/09/xmldsig#rsa-sha384` - `http://www.w3.org/2000/09/xmldsig#rsa-sha512` |
| Allow outbound logout requests | Login with SSO currently **does not**support SLO. This option is planned for future use, however we strongly recommend pre-configuring this field. |
| Sign authentication requests | Check this checkbox if your IdP should expect SAML requests from Bitwarden to be signed. |

> [!NOTE] X509 cert expiration
> When completing the X509 certificate, take note of the expiration date. Certificates will have to be renewed in order to prevent any disruptions in service to SSO end users. If a certificate has expired, Admin and Owner accounts will always be able to log in with email address and master password.

### SAML attributes & claims

An **email address is required for account provisioning**, which can be passed as any of the attributes or claims in the following table.

A unique user identifier is also highly recommended. If absent, email will be used in its place to link the user.

Attributes/claims are listed in order of preference for matching, including fallbacks where applicable:

| **Value** | **Claim/Attribute** | **Fallback claim/attribute** |
|------|------|------|
| Unique ID | NameID (when not transient) urn:oid:0.9.2342.19200300.100.1.1 Sub UID UPN EPPN | |
| Email | Email http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress urn:oid:0.9.2342.19200300.100.1.3 Mail EmailAddress | Preferred_Username Urn:oid:0.9.2342.19200300.100.1.1 UID |
| Name | Name http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name urn:oid:2.16.840.1.113730.3.1.241 urn:oid:2.5.4.3 DisplayName CN | First Name + “ “ + Last Name (see below) |
| First Name | urn:oid:2.5.4.42 GivenName FirstName FN FName Nickname | |
| Last Name | urn:oid:2.5.4.4 SN Surname LastName | |
