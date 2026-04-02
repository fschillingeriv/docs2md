---
URL: https://bitwarden.com/help/saml-onelogin/
---

# OneLogin SAML

This article contains **OneLogin-specific** help for configuring login with SSO via SAML 2.0. For help configuring login with SSO for another IdP, refer to [SAML 2.0 Configuration](https://bitwarden.com/help/configure-sso-saml/).

Configuration involves working simultaneously within the Bitwarden web app and the OneLogin Portal. As you proceed, we recommend having both readily available and completing steps in the order they are documented.

> [!NOTE]
> **Already an SSO expert?** Skip the instructions in this article and download screenshots of sample configurations to compare against your own.
> 
> ⬇️ [Download Sample](https://bitwarden.com/assets/mQMTlMcvpyBPzgAkgqDvg/ace51cc7a46379048140042282e6b24f/saml-onelogin-sample.zip)

## Open SSO in the web app

Log in to the Bitwarden web app and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)

Open your organization's **Settings** → **Single sign-on** screen:

![SAML 2.0 configuration ](https://bitwarden.com/assets/20720mRAluo6crSdTiYJrn/1175889d7f6ab42fe7614f34cdd1dcdd/2024-12-04_09-41-15.png)

If you haven't already, create a unique **SSO identifier**for your organization and select **SAML**from the the **Type**dropdown. Keep this screen open for easy reference.

You can turn off the **Set a unique SP entity ID**option at this stage if you wish. Doing so will remove your organization ID from your SP entity ID value, however in almost all cases it is recommended to leave this option on.

> [!TIP] Self-hosting, use alternative Member Decryption Options.
> There are alternative **Member decryption options**. Learn how to get started using [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/) or [Key Connector](https://bitwarden.com/help/about-key-connector/).

## Create a OneLogin app

In the OneLogin Portal, navigate to the the **Applications** screen and select the **Add App** button:

![Add an Application ](https://bitwarden.com/assets/37OSt7e5j969j9ikvH8buI/3bf9fa6b57a45b357a9d2bc012d8a6af/ol-addapp.png)

In the search bar, type `saml custom connector` and select the **SAML Custom Connector (Advanced)** app:

![SAML Test Connector App ](https://bitwarden.com/assets/hTfoABj2iirzB1X7UT69x/520891ab503ad773178fef291d49e198/2026-03-02_09-22-12.png)

Give your application a Bitwarden-specific **Display Name** and select the **Save** button.

### Configuration

Select **Configuration** from the left-hand navigation and configure the following information, some of which you will need to retrieve from the Single Sign-On screen:

![App Configuration](https://bitwarden.com/assets/12yP5ohPGhqcCZZdpwVDQd/7fc5661e4fb4954ad00246deae2fd9b1/ol-appconfig.png)

| **Application Setting** | **Description** |
|------|------|
| Audience (EntityID) | Set this field to the pre-generated **SP Entity ID**. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |
| Recipient | Set this field to the same pre-generated **SP Entity ID**used for the **Audience (Entity ID)**setting. |
| ACS (Consumer) URL Validator | Despite being marked **Required**by OneLogin, you don't actually need to enter information into this field to integrate with Bitwarden. Skip to the next field, **ACS (Consumer) URL**. |
| ACS (Consumer) URL | Set this field to the pre-generated **Assertion Consumer Service (ACS) URL**. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |
| SAML initiator | Select **Service Provider**. Login with SSO does not currently support IdP-initiated SAML assertions. |
| SAML nameID Format | Set this field to the [SAML NameID Format](https://docs.oracle.com/cd/E19316-01/820-3886/ggwbz/index.html) you want to use for SAML assertions. |
| SAML signature element | By default, OneLogin will sign the SAML Response. You can set this to **Assertion**or **Both** |

Select the **Save** button to finish your configuration settings.

### Parameters

Select **Parameters** from the left-hand navigation and use the + **Add** icon to create the following custom parameters:

| **Field Name** | **Value** |
|------|------|
| email | Email |
| firstname | First Name |
| lastname | Last Name |

Select the **Save** button to finish your custom parameters.

### SSO

Select **SSO** from the left-hand navigation and complete the following:

1. Select the **View Details** link under your X.509 Certificate:

![View your Cert ](https://bitwarden.com/assets/7emKbivWUWKO1ufVC9Rkgu/0039e55d93ba69fadc8c39e0be3d8a07/Screen_Shot_2022-12-29_at_9.42.14_AM.png)

On the Certificate screen, download or copy your X.509 PEM Certificate, as you will need to [use it later](https://bitwarden.com/help/saml-onelogin/#identity-provider-configuration/). Once copied, return to the main SSO screen.
2. Set your **SAML Signature Algorithm**.
3. Take note of your **Issuer URL** and **SAML 2.0 Endpoint (HTTP)**. You will need to [use these values shortly](https://bitwarden.com/help/saml-onelogin/#identity-provider-configuration/).

### Access

Select **Access** from the left-hand navigation. In the **Roles** section, assign application access to all the roles you would like to be able to use Bitwarden. Most implementations create a Bitwarden-specific role and instead opt to assign based on a catch-all (for example, **Default**) or based on pre-existing roles.

![Role Assignment ](https://bitwarden.com/assets/6D4j0WofpBcvSCMB0rN4Db/5303beacbc3ce331dfddc6dc6b19d6ea/ol-roles.png)

## Back to the web app

At this point, you have configured everything you need within the context of the OneLogin Portal. Return to the Bitwarden web app to complete configuration.

The Single sign-on screen separates configuration into two sections:

- **SAML service provider configuration** will determine the format of SAML requests.
- **SAML identity provider configuration** will determine the format to expect for SAML responses.

### Service provider configuration

Configure the following fields according to the choices selected in the OneLogin Portal [during app creation](https://bitwarden.com/help/saml-onelogin/#create-a-onelogin-app/):

| **Field** | **Description** |
|------|------|
| Name ID Format | Set this field to whatever you selected for the OneLogin **SAML nameID Format**field [during app configuration](https://bitwarden.com/help/saml-onelogin/#configuration/). |
| Outbound Signing Algorithm | Algorithm used to sign SAML requests, by default `sha-256`. |
| Signing Behavior | Whether/when SAML requests will be signed. By default, OneLogin will not require requests to be signed. |
| Minimum Incoming Signing Algorithm | Set this field to whatever you selected for the **SAML Signature Algorithm**[during app configuration](https://bitwarden.com/help/saml-onelogin/#configuration/) |
| Expect Signed Assertions | Check this box if you set the **SAML signature element**in OneLogin to **Assertion**or **Both**[during app configuration](https://bitwarden.com/help/saml-onelogin/#configuration/). |
| Validate Certificates | Check this box when using trusted and valid certificates from your IdP through a trusted CA. Self-signed certificates may fail unless proper trust chains are configured within the Bitwarden login with SSO docker image. |

When you are done with the service provider configuration, **Save** your work.

### Identity provider configuration

Identity provider configuration will often require you to refer back to the OneLogin Portal to retrieve application values:

| **Field** | **Description** |
|------|------|
| Entity ID | Enter your OneLogin **Issuer URL**, which can be retrieved from the [OneLogin app SSO screen](https://bitwarden.com/help/saml-onelogin/#sso/). This field is case sensitive. |
| Binding Type | Set to **HTTP Post**(as indicated in the SAML 2.0 Endpoint (HTTP)). |
| Single Sign On Service URL | Enter your OneLogin **SAML 2.0 Endpoint (HTTP)**, which can be retrieved from the [OneLogin app SSO screen](https://bitwarden.com/help/saml-onelogin/#sso/). |
| Single Log Out Service URL | Login with SSO currently **does not**support SLO. This option is planned for future development, however you may pre-configure it if you wish. |
| X509 Public Certificate | Paste the [retrieved X.509 Certificate](https://bitwarden.com/help/saml-onelogin/#sso/), removing `-----BEGIN CERTIFICATE-----`  and  `-----END CERTIFICATE-----` The certificate value is case sensitive, extra spaces, carriage returns, and other extraneous characters **will cause certification validation to fail**. |
| Outbound Signing Algorithm | Select the SAML Signature Algorithm selected in the [OneLogin SSO](https://bitwarden.com/help/saml-onelogin/#sso/) configuration section. |
| Allow outbound logout request | Login with SSO currently **does not**support SLO. This option is planned for future development. |
| Sign authentication requests | Whether OneLogin expects SAML requests to be signed. |

> [!NOTE] X509 cert expiration
> When completing the X509 certificate, take note of the expiration date. Certificates will have to be renewed in order to prevent any disruptions in service to SSO end users. If a certificate has expired, Admin and Owner accounts will always be able to log in with email address and master password.

When you are done with the identity provider configuration, **Save** your work.

> [!TIP] Policies for SSO Guides
> You can require users to log in with SSO by activating the single sign-on authentication policy. Please note, this will require activating the single organization policy as well. [Learn more](https://bitwarden.com/help/policies/).

## Test the configuration

Once your configuration is complete, test it by navigating to [https://vault.bitwarden.com](https://vault.bitwarden.com), entering your email address and selecting the **Use single sign-on** button:

![Log in options screen](https://bitwarden.com/assets/3BdlHeogd42LEoG06qROyQ/c68021df4bf45d72e9d37b1fbf5a6040/login.png)

Enter the [configured organization identifier](https://bitwarden.com/help/saml-onelogin/#/) and select **Log In**. If your implementation is successfully configured, you will be redirected to the OneLogin login screen:

![OneLogin Login ](https://bitwarden.com/assets/58dRC3pPEm0bO8xtd2Tqzq/415b83d361b49c73550d0932ddca8576/ol-login.png)

After you authenticate with your OneLogin credentials, enter your Bitwarden master password to decrypt your vault!

> [!NOTE] SSO must be initiated from Bitwarden
> Bitwarden does not support unsolicited responses, so initiating login from your IdP will result in an error. The SSO login flow must be initiated from Bitwarden.
