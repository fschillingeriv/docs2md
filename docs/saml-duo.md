---
URL: https://bitwarden.com/help/saml-duo/
---

# Duo SAML

This article contains **Duo-specific** help for configuring login with SSO via SAML 2.0 For help configuring login with SSO for another IdP, refer to [SAML 2.0 Configuration](https://bitwarden.com/help/configure-sso-saml/).

Configuration involves working simultaneously between the Bitwarden web app and the Duo Admin Portal. As you proceed, we recommend having both readily available and completing steps in the order they are documented.

> [!NOTE]
> **Already an SSO expert?** Skip the instructions in this article and download screenshots of sample configurations to compare against your own.
> 
> ⬇️ [Download Sample](https://bitwarden.com/assets/5zTphwdGyxRww5UaF3COLP/67104e859f8fcaad2aa4b185292971eb/saml-duo-sample.zip)

## Open SSO in the web app

> [!NOTE]
> This article assumes that you have already set up Duo with an Identity Provider. If you haven't, see [Duo's documentation](https://duo.com/docs/sso#saml) for details.

Log in to the Bitwarden web app and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)

Open your organization's **Settings** → **Single sign-on** screen:

![SAML 2.0 configuration ](https://bitwarden.com/assets/20720mRAluo6crSdTiYJrn/1175889d7f6ab42fe7614f34cdd1dcdd/2024-12-04_09-41-15.png)

If you haven't already, create a unique **SSO identifier**for your organization and select **SAML**from the the **Type**dropdown. Keep this screen open for easy reference.

You can turn off the **Set a unique SP entity ID**option at this stage if you wish. Doing so will remove your organization ID from your SP entity ID value, however in almost all cases it is recommended to leave this option on.

> [!TIP] Self-hosting, use alternative Member Decryption Options.
> There are alternative **Member decryption options**. Learn how to get started using [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/) or [Key Connector](https://bitwarden.com/help/about-key-connector/).

## Protect an application

Before continuing, please refer to [Duo's documentation](https://duo.com/docs/sso#saml) to verify that Duo Single Sign-On has been configured with your SAML identity provider for authentication.

In the Duo Admin Portal, navigate to the **Applications** screen and select **Protect an Application**. Enter **Bitwarden** into the search bar and select **Configure**for the **Bitwarden 2FA with SSO hosted by Duo** application:

![Duo Bitwarden Application](https://bitwarden.com/assets/trkKdfpokzVAwdGxg6wa6/02ae03583eae5f96e4a6fbe90e70af14/2023-12-11_15-58-21.png)

Select **Activate and Start Setup**for the newly created application:

![Duo Activation and Setup](https://bitwarden.com/assets/38UnzJq3P4zVvB8wHpK62W/ff109380215fc7d82c25c960eecd3ec3/2023-12-11_16-00-38.png)

Complete the following steps and configurations on the Application configuration screen, some of which you will need to retrieve from the Bitwarden single sign-on screen:

![DUO SAML Identity Provider Configuration](https://bitwarden.com/assets/5OMLBklde4cADIvmgypSxe/64f00b2c483c471a9a5ead8da8f982e5/2023-12-11_16-09-16.png)

### Metadata

You don't need to edit anything in the **Metadata** section, but you will need to [use these values later](https://bitwarden.com/help/saml-duo/#identity-provider-configuration/):

![URLs for Configuration ](https://bitwarden.com/assets/3ob9jp2RJRhMaxOkRrWHKa/8a9b7c3cc3aa077e323353c8c0cab0ed/duo-urls.png)

### Downloads

Select the **Download certificate** button to download your X.509 Certificate, as you will need to use it [later in the configuration](https://bitwarden.com/help/saml-duo/#identity-provider/).

### Service provider

| **Field** | **Description** |
|------|------|
| Entity ID | Set this field to the pre-generated **SP Entity ID**. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |
| Assertion Consumer Service (ACS) URL | Set this field to the pre-generated **Assertion Consumer Service (ACS) URL**. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |
| Service Provider Login URL | Set this field to the login URL from which users will access Bitwarden. For cloud-hosted customers, this is `https://vault.bitwarden.com/#/sso `or` https://vault.bitwarden.eu/#/sso.` For self-hosted instances, this is determined by your [configured server URL](https://bitwarden.com/help/install-on-premise/#configure-your-domain/), for example `https://your.domain.com/#/sso`. |

### SAML response

| **Field** | **Description** |
|------|------|
| NameID format | Set this field to the [SAML NameID format](https://docs.oracle.com/cd/E19316-01/820-3886/ggwbz/index.html) for Duo to send in SAML responses. |
| NameID attribute | Set this field to the Duo attribute that will populate the NameID in responses. |
| Signature algorithm | Set this field to the encryption algorithm to use for SAML assertions and responses. |
| Signing options | Select whether to **Sign response**, **Sign assertion**, or both. |
| Map attributes | Use these fields to map IdP attributes to SAML response attributes. Regardless of which NameID attribute you configured, map the IdP `Email Address `attribute to `Email`, as in the following screenshot: |

![Required Attribute Mapping ](https://bitwarden.com/assets/2MQbtzmGaflBaCf0FIa2r9/914b2dec377d122deee4a65439689e2a/duo-mapping.png)

Once you have finished configuring these fields, **Save** your changes.

## Back to the web app

At this point, you have configured everything you need within the context of the Duo Portal. return to the Bitwarden web app to complete configuration.

The Single sign-on screen separates configuration into two sections:

- **SAML service provider configuration** will determine the format of SAML requests.
- **SAML identity provider configuration** will determine the format to expect for SAML responses.

### Service provider configuration

Configure the following fields according to the choices selected in the Duo Admin Portal [during application setup](https://bitwarden.com/help/saml-duo/#protect-an-application/):

| **Field** | **Description** |
|------|------|
| Name ID Format | [NameID Format](https://docs.oracle.com/cd/E19316-01/820-3886/ggvxx/index.html) to use in the SAML request (`NameIDPolicy`). Set this field to [the selected NameID format](https://bitwarden.com/help/saml-duo/#saml-response/). |
| Outbound Signing Algorithm | Algorithm used to sign SAML requests, by default `rsa-sha256`. |
| Signing Behavior | Whether/when SAML requests will be signed. By default, Duo will not require requests to be signed. |
| Minimum Incoming Signing Algorithm | The minimum signing algorithm Bitwarden will accept in SAML responses. By default, Duo will sign with `rsa-sha256`, so choose that option from the dropdown unless you have [selected a different option](https://bitwarden.com/help/saml-duo/#saml-response/). |
| Want Assertions Signed | Whether Bitwarden wants SAML assertions signed. Check this box if you [selected the **Sign assertion** signing option](https://bitwarden.com/help/saml-duo/#saml-response/). |
| Validate Certificates | Check this box when using trusted and valid certificates from your IdP through a trusted CA. Self-signed certificates may fail unless proper trust chains are configured within the Bitwarden Login with SSO docker image. |

When you are done with the service provider configuration, **Save** your work.

### Identity provider configuration

Identity provider configuration will often require you to refer back to the Duo Admin Portal to retrieve application values:

| **Field** | **Description** |
|------|------|
| Entity ID | Enter the **Entity ID**value of your Duo application, which can be retrieved from the Duo app [Metadata section](https://bitwarden.com/help/saml-duo/#metadata/). This field is case sensitive. |
| Binding Type | Set this field to **HTTP Post**. |
| Single Sign On Service URL | Enter the **Single Sign-On URL**value of your Duo application, which can be retrieved from the Duo app [Metadata section](https://bitwarden.com/help/saml-duo/#metadata/). |
| Single Log Out Service URL | Login with SSO currently **does not**support SLO. This option is planned for future development, however you may pre-configure with the **Single Log-Out URL**value of your Duo application. |
| X509 Public Certificate | Paste the downloaded [certificate](https://bitwarden.com/help/saml-duo/#downloads/), removing `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` The certificate value is case sensitive, extra spaces, carriage returns, and other extraneous characters **will cause certification validation to fail**. |
| Outbound Signing Algorithm | Set this field to the [selected SAML Response signature algorithm](https://bitwarden.com/help/saml-duo/#saml-response/). |
| Disable Outbound Logout Requests | Login with SSO currently **does not**support SLO. This option is planned for future development. |
| Want Authentication Requests Signed | Whether Duo expects SAML requests to be signed. |

> [!NOTE] X509 cert expiration
> When completing the X509 certificate, take note of the expiration date. Certificates will have to be renewed in order to prevent any disruptions in service to SSO end users. If a certificate has expired, Admin and Owner accounts will always be able to log in with email address and master password.

When you are done with the identity provider configuration, **Save** your work.

> [!TIP] Policies for SSO Guides
> You can require users to log in with SSO by activating the single sign-on authentication policy. Please note, this will require activating the single organization policy as well. [Learn more](https://bitwarden.com/help/policies/).

## Test the Configuration

Once your configuration is complete, test it by navigating to [https://vault.bitwarden.com](https://vault.bitwarden.com), entering your email address and select the **Use single sign-on** button:

![Log in options screen](https://bitwarden.com/assets/3BdlHeogd42LEoG06qROyQ/c68021df4bf45d72e9d37b1fbf5a6040/login.png)

Enter the [configured organization identifier](https://bitwarden.com/help/saml-duo/#/) and select **Log In**. If your implementation is successfully configured, you will be redirected to your source IdP's login screen.

After you authenticate with your IdP login and Duo Two-factor, enter your Bitwarden master password to decrypt your vault!

> [!NOTE] SSO must be initiated from Bitwarden
> Bitwarden does not support unsolicited responses, so initiating login from your IdP will result in an error. The SSO login flow must be initiated from Bitwarden.
