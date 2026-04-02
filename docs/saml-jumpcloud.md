---
URL: https://bitwarden.com/help/saml-jumpcloud/
---

# JumpCloud SAML

This article contains **JumpCloud-specific** help for configuring login with SSO via SAML 2.0. For help configuring login with SSO for another IdP, refer to [SAML 2.0 Configuration](https://bitwarden.com/help/configure-sso-saml/).

Configuration involves working simultaneously within the Bitwarden web app and the JumpCloud Portal. As you proceed, we recommend having both readily available and completing steps in the order they are documented.

> [!NOTE]
> **Already an SSO expert?** Skip the instructions in this article and download screenshots of sample configurations to compare against your own.
> 
> ⬇️ [Download Sample](https://bitwarden.com/assets/2jY7iejfs0KgdWBnwhGMHF/4bdd393ef26aac504ac2dd5b38cd283f/saml-jumpcloud-sample.zip)

## Open SSO in the web app

Log in to the Bitwarden web app and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)

Open your organization's **Settings** → **Single sign-on** screen:

![SAML 2.0 configuration ](https://bitwarden.com/assets/20720mRAluo6crSdTiYJrn/1175889d7f6ab42fe7614f34cdd1dcdd/2024-12-04_09-41-15.png)

If you haven't already, create a unique **SSO identifier**for your organization and select **SAML**from the the **Type**dropdown. Keep this screen open for easy reference.

You can turn off the **Set a unique SP entity ID**option at this stage if you wish. Doing so will remove your organization ID from your SP entity ID value, however in almost all cases it is recommended to leave this option on.

> [!TIP] Self-hosting, use alternative Member Decryption Options.
> There are alternative **Member decryption options**. Learn how to get started using [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/) or [Key Connector](https://bitwarden.com/help/about-key-connector/).

## Create a JumpCloud SAML application

In the JumpCloud Portal, select **Applications** from the menu and select the **Get Started** button:

![Create Bitwarden app Jumpcloud](https://bitwarden.com/assets/63S5F953fjQN6V4xYKZR3h/515abac11c991e20cf8d5286e1b80a1d/Screen_Shot_2023-02-07_at_10.49.15_AM__2_.png)

Enter `Bitwarden` in the search box and select the **configure** button:

![Configure Bitwarden ](https://bitwarden.com/assets/2pFRcBTjlIjBhMbqlKMhxb/b80b23ecfd660d5c314028297c606879/jc-bw.png)

> [!NOTE] Custom SAML App 
> If you are more comfortable with SAML, or want more control over things like NameID Format and Signing Algorithms, create a **Custom SAML Application** instead.

### General info

In the **General Info** section, configure the following information:

| **Field** | **Description** |
|------|------|
| Display Label | Give the Application a Bitwarden-specific name. |

### Single sign-on configuration

In the **Single Sign-On Configuration** section, configure the following information:

![Jumpcloud SSO configuration ](https://bitwarden.com/assets/29XSIA5254JE0flwlFEGBf/5f078dec5b873be5568b2485c221c645/Screen_Shot_2023-02-07_at_3.20.29_PM__2_.png)

| **Field** | **Description** |
|------|------|
| IdP Entity ID | Set this field to a unique, Bitwarden-specific value, for example, `bitwardensso_yourcompany`. |
| SP Entity ID | Set this field to the pre-generated **SP Entity ID**. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |
| ACS URL | Set this field to the pre-generated **Assertion Consumer Service (ACS) URL**. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |

#### Custom SAML app only

If you created a Custom SAML Application, you will also need to configure the following **Single Sign-On Configuration** fields:

| **Field** | **Description** |
|------|------|
| SAMLSubject NameID | Specify the JumpCloud attribute that will be sent in SAML responses as the NameID. |
| SAMLSubject NameID Format | Specify the format of the NameID sent in SAML responses. |
| Signature Algoritm | Select the algorithm to use to sign SAML assertions or reponses. |
| Sign Assertion | By default, JumpCloud will sign the SAML response. Check this box the sign the SAML assertion. |
| Login URL | Specify the URL from which your users will login to Bitwarden via SSO. For cloud-hosted customers, this is `https://vault.bitwarden.com/#/sso` or `https://vault.bitwarden.eu/#/sso`. For self-hosted instances, this is determined by your [configured server URL](https://bitwarden.com/help/install-on-premise/#configure-your-domain/), for example `https://your.domain.com/#/sso`. |

### Attributes

In the **Single Sign-On Configuration** → **Attributes** section, construct the following SP → IdP attribute mappings. If you selected the Bitwarden Application in JumpCloud, these should already be constructed:

![Attribute Mapping ](https://bitwarden.com/assets/5vRaXPal1HJsXhJZX8MdTL/b7c71fb6d4156d104f0f2b826f78a247/jc-attr.png)

Once you are finished, select the **activate** button.

### Download the certificate

Once the application is activated, use the **SSO** menu option again to open the created Bitwarden application. Select the **IDP Certificate** dropdown and **Download certificate**:

![Download Certificate ](https://bitwarden.com/assets/6Y2DUGlm3LxBK6Ws44SjRg/a032010b5c0df73cccf7418892c9c00f/jc-cert.png)

### Bind user groups

In the JumpCloud Portal, select **User Groups** from the menu:

![User Groups ](https://bitwarden.com/assets/3nIOyl4xedMgTRTNobFqwG/35151b1af8594d15fd9d69531c5e4e04/jc-groups.png)

Either create a Bitwarden-specific user group, or open the All Users default user group. In either case, select the **Applications** tab and enable access to the created Bitwarden SSO application for that user group:

![Bind App Access ](https://bitwarden.com/assets/7BUUQUi79zmEy8xm64qwog/7d5537c45423a87f92485e7b6cad5d5e/jc-group-app.png)

> [!NOTE]
> Alternatively, you can bind access to user groups directly from the **SSO** → **Bitwarden Application** screen.

## Back to the web app

At this point, you have configured everything you need within the context of the JumpCloud Portal. Return to the Bitwarden web vault to complete configuration.

The Single sign-on screen separates configuration into two sections:

- **SAML service provider configuration** will determine the format of SAML requests.
- **SAML identity provider configuration** will determine the format to expect for SAML responses.

### Service provider configuration

Configure the following fields according to the choices selected in the JumpCloud Portal [during app creation](https://bitwarden.com/help/saml-jumpcloud/#create-a-jumpcloud-saml-app/):

| **Field** | **Description** |
|------|------|
| Name ID Format | If you created a Custom SAML Application, set this to whatever the specified SAMLSubject NameID Format is. Otherwise, leave **Unspecified**. |
| Outbound Signing Algorithm | The algorithm Bitwarden will use to sign SAML requests. |
| Signing Behavior | Whether/when SAML requests will be signed. By default, JumpCloud will not require requests to be signed. |
| Minimum Incoming Signing Algorithm | If you created a Custom SAML Application, set this to whichever Signature Algorithm you selected. Otherwise, leave as `rsa-sha256`. |
| Want Assertions Signed | If you created a Custom SAML Application, check this box if you set the **Sign Assertion**option in JumpCloud. Otherwise, leave unchecked. |
| Validate Certificates | Check this box when using trusted and valid certificates from your IdP through a trusted CA. Self-signed certificates may fail unless proper trust chains are configured within the Bitwarden login with SSO docker image. |

When you are done with the service provider configuration, **Save** your work.

### Identity provider configuration

Identity provider configuration will often require you to refer back to the JumpCloud Portal to retrieve application values:

| **Field** | **Description** |
|------|------|
| Entity ID | Enter your JumpCloud **IdP Entity ID**, which can be retrieved from the JumpCloud [Single Sign-On Configuration screen](https://bitwarden.com/help/saml-jumpcloud/#single-sign-on-configuration/). This field is case sensitive. |
| Binding Type | Set to **Redirect**. |
| Single Sign On Service URL | Enter your JumpCloud **IdP URL**, which can be retrieved from the JumpCloud [Single Sign-On Configuration screen](https://bitwarden.com/help/saml-jumpcloud/##single-sign-on-configuration/). |
| Single Log Out Service URL | Login with SSO currently **does not**support SLO. This option is planned for future development. |
| X509 Public Certificate | Paste the [retrieved certificate](https://bitwarden.com/help/saml-jumpcloud/##download-the-certificate/), removing `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` The certificate value is case sensitive, extra spaces, carriage returns, and other extraneous characters **will cause certification validation to fail**. |
| Outbound Signing Algorithm | If you created a Custom SAML Application, set this to whichever Signature Algorithm you selected. Otherwise, leave as `rsa-sha256`. |
| Disable Outbound Logout Requests | Login with SSO currently **does not**support SLO. This option is planned for future development. |
| Want Authentication Requests Signed | Whether JumpCloud expects SAML requests to be signed. |

> [!NOTE] X509 cert expiration
> When completing the X509 certificate, take note of the expiration date. Certificates will have to be renewed in order to prevent any disruptions in service to SSO end users. If a certificate has expired, Admin and Owner accounts will always be able to log in with email address and master password.

When you are done with the identity provider configuration, **Save** your work.

> [!TIP] Policies for SSO Guides
> You can require users to log in with SSO by activating the single sign-on authentication policy. Please note, this will require activating the single organization policy as well. [Learn more](https://bitwarden.com/help/policies/).

## Test the configuration

Once your configuration is complete, test it by navigating to [https://vault.bitwarden.com](https://vault.bitwarden.com), entering your email address and selecting the **Use single sign-on** button:

![Log in options screen](https://bitwarden.com/assets/3BdlHeogd42LEoG06qROyQ/c68021df4bf45d72e9d37b1fbf5a6040/login.png)

Enter the [configured organization identifier](https://bitwarden.com/help/saml-jumpcloud/#/) and select **Log In**. If your implementation is successfully configured, you will be redirected to the JumpCloud login screen:

![JumpCloud Login ](https://bitwarden.com/assets/678vDfFuKfH8FBZkhJdt5J/df1e8bad4f88f013ca194d9c9c82fccc/jc-login.png)

After you authenticate with your JumpCloud credentials, enter your Bitwarden master password to decrypt your vault!

> [!NOTE] SSO must be initiated from Bitwarden
> Bitwarden does not support unsolicited responses, so initiating login from your IdP will result in an error. The SSO login flow must be initiated from Bitwarden.
