---
URL: https://bitwarden.com/help/saml-keycloak/
---

# Keycloak SAML

This article contains **Keycloak-specific** help for configuring login with SSO via SAML 2.0. For help configuring login with SSO for another IdP, refer to [SAML 2.0 Configuration](https://bitwarden.com/help/configure-sso-saml/).

Configuration involves working simultaneously with the Bitwarden web app and the Keycloak Portal. As you proceed, we recommend having both readily available and completing steps in the order they are documented.

> [!NOTE]
> **Already an SSO expert?** Skip the instructions in this article and download screenshots of sample configurations to compare against your own.
> 
> ⬇️ [Download Sample](https://bitwarden.com/assets/6SVuB4OSxNq6QzGkuqGUd8/5ac1881e660cb456a60ca0da8433e814/saml-keycloak-sample.zip)

## Open SSO in the web app

Log in to the Bitwarden web app and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
*Product switcher*

Open your organization's **Settings** → **Single sign-on** screen:

![SAML 2.0 configuration ](https://bitwarden.com/assets/20720mRAluo6crSdTiYJrn/1175889d7f6ab42fe7614f34cdd1dcdd/2024-12-04_09-41-15.png)
*SAML 2.0 configuration *

If you haven't already, create a unique **SSO identifier**for your organization and select **SAML**from the the **Type**dropdown. Keep this screen open for easy reference.

You can turn off the **Set a unique SP entity ID**option at this stage if you wish. Doing so will remove your organization ID from your SP entity ID value, however in almost all cases it is recommended to leave this option on.

> [!TIP] Self-hosting, use alternative Member Decryption Options.
> There are alternative **Member decryption options**. Learn how to get started using [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/) or [Key Connector](https://bitwarden.com/help/about-key-connector/).

## Keycloak setup

Login to Keycloak and select **Clients** → **Create Client**. 

![Create a Client ](https://bitwarden.com/assets/2bBUv6v2343MxtsXC09lvm/1d3c30e4fbe95941ed0d8303f888a885/create_client.png)
*Create a Client *

On the Create client screen fill in the following fields:

| **Field** | **Description** |
|------|------|
| Client type | Select SAML. |
| Client ID | Set this field to the pre-generated **SP Entity ID**. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |
| Name | Enter a name of your choice for the Keycloak client. |

Once you have filled in the required fields on the **General Settings** page, click **Next**.

On the **Login settings** screen, fill in the following field:

| **Field** | **Description** |
|------|------|
| Valid redirect URIs | Set this field to the pre-generated **Assertion Consumer Service (ACS) URL**. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |

Select **Save**. 

Select the Keys tab and toggle the **Client signature required** option to **Off**.

![Keycloak Keys Config](https://bitwarden.com/assets/RZd8WRbn45BIbiyqN7UzR/1337005dbd6c68e1d8b68ee99b1dcdc9/keys_confifg.png)
*Keycloak Keys Config*

Return to the settings tab and scroll down to **SAML capabilities**, and then turn off **Force POST binding**.

![Force Post binding disabled](https://bitwarden.com/assets/63FPnC5EAZ2vRnBFL4hUxe/996d021e902c9f575ca7036de8654dfe/Force_Post_binding_disabled.png)
*Force Post binding disabled*

Lastly, on the Keycloak main navigation, select **Realm settings** and then the **Keys** tab. Locate the **RS256** 
Certificate and select **Certificate**. 

![Keycloak RS256 Certificate](https://bitwarden.com/assets/2Codsw3P2MWiMHRctDckTF/fc55404f24ceade2663cdef01caa7528/2023-09-25_16-33-13.png)
*Keycloak RS256 Certificate*

The value for the certificate will be required for the following [section](https://bitwarden.com/help/saml-keycloak/#back-to-the-web-vault/). 

## Back to the web app

At this point, you have configured everything you need within the context of the Keycloak Portal. Return to the Bitwarden web app **Single sign-on**screen.

The Single sign-on screen separates configuration into two sections:

- **SAML service provider configuration** will determine the format of SAML requests.
- **SAML identity provider configuration** will determine the format to expect for SAML responses.

Complete the following fields in the **SAML service provider configuration** section:

| **Field** | **Description** |
|------|------|
| Name ID format | Select **Email** **Address**. |
| Outbound Signing Algorithm | The algorithm Bitwarden will use to sign SAML requests. |
| Signing Behavior | Whether/when SAML requests will be signed. |
| Minimum Incoming Signing Algorithm | Select the algorithm the Keycloak client is [configured to use](https://bitwarden.com/help/saml-keycloak/#settings/) to sign SAML documents or assertions. |
| Want Assertions Signed | Whether Bitwarden expects SAML assertions to be signed. If toggled on, make sure you configure the Keycloak client to [sign assertions](https://bitwarden.com/help/saml-keycloak/#settings/). |
| Validate Certificates | Check this box when using trusted and valid certificates from your IdP through a trusted CA. Self-signed certificates may fail unless proper trust chains are configured with the Bitwarden login with SSO docker image. |

Complete the following fields in the **SAML identity provider configuration** section:

| **Field** | **Description** |
|------|------|
| Entity ID | Enter the URL of the Keycloak realm on which the client was created, for example `https://<keycloak_domain>/realms/<realm_name>`. This field is case sensitive. |
| Binding type | Select **Redirect**. |
| Single sign-on service URL | Enter your master SAML processing URL, for example `https://<keycloak_domain>/realms/<realm_name>/protocol/saml`. |
| Single Log Out Service URL | Login with SSO currently **does not **support SLO. This option is planned for future development, however you may preconfigure it with your **Logout URL **if you wish. |
| X509 public certificate | Enter the **RS256 certificate** that was copied in the previous step. The certificate value is case sensitive, extra spaces, carriage returns, and other extraneous characters **will cause certificate validation to fail**. |
| Outbound Signing Algorithm | Select the algorithm the Keycloak client is [configured to use](https://bitwarden.com/help/saml-keycloak/#settings/) to sign SAML documents or assertions. |
| Disable Outbound Logout Requests | Login with SSO currently **does not **support SLO. This option is planned for future development. |
| Want Authentication Requests Signed | Whether Keycloak expects SAML requests to be signed. |

> [!NOTE] X509 cert expiration
> When completing the X509 certificate, take note of the expiration date. Certificates will have to be renewed in order to prevent any disruptions in service to SSO end users. If a certificate has expired, Admin and Owner accounts will always be able to log in with email address and master password.

When you're done with the identity provider configuration, **Save** your work.

> [!TIP] Policies for SSO Guides
> You can require users to log in with SSO by activating the single sign-on authentication policy. Please note, this will require activating the single organization policy as well. [Learn more](https://bitwarden.com/help/policies/).

## Additional Keycloak settings

On the Keycloak Client **Settings tab**, additional configuration options are available:

| **Field** | **Description** |
|------|------|
| Sign Documents | Bitwarden expects SAML documents to be signed. Be sure this setting remains **on**. |
| Sign Assertions | Specify whether SAML assertions should be signed by the Keycloak realm. |
| Signature Algorithm | If **Sign Assertions**is enabled, select what algorithm to sign with (`sha-256` by default). |
| Name ID Format | Select the Name ID Format for Keycloak to use in SAML responses. |

Once you have completed the forum, select **Save**.

## Test the configuration

Once your configuration is complete, test it by navigating to [https://vault.bitwarden.com](https://vault.bitwarden.com), entering your email address and selecting the **Use single sign-on** button:

![Log in options screen](https://bitwarden.com/assets/3BdlHeogd42LEoG06qROyQ/c68021df4bf45d72e9d37b1fbf5a6040/login.png)
*Log in options screen*

Enter the [configured organization identifier](https://bitwarden.com/help/configure-sso-saml/#step-1-enabling-login-with-sso/) and select **Log In**. If your implementation is successfully configured, you will be redirected to the Keycloak login screen:

![Keycloak Login Screen ](https://bitwarden.com/assets/1FOJPAvRf0NCpJleOtMA8e/cc981e5933250dcab63a3f518370a24f/keycloak-login.png)
*Keycloak Login Screen *

After you authenticate with your Keycloak credentials, enter your Bitwarden master password to decrypt your vault!

> [!NOTE] SSO must be initiated from Bitwarden
> Bitwarden does not support unsolicited responses, so initiating login from your IdP will result in an error. The SSO login flow must be initiated from Bitwarden.
