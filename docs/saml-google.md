---
URL: https://bitwarden.com/help/saml-google/
---

# Google SAML

This article contains **Google Workspace-specific** help for configuring login with SSO via SAML 2.0. For help configuring login with SSO for another IdP, refer to [SAML 2.0 Configuration](https://bitwarden.com/help/configure-sso-saml/).

Configuration involves working simultaneously with the Bitwarden web app and the Google Workspace Admin console. As you proceed, we recommend having both readily available and completing steps in the order they are documented.

> [!NOTE]
> **Already an SSO expert?** Skip the instructions in this article and download screenshots of sample configurations to compare against your own.
> 
> ⬇️ [Download Sample](https://bitwarden.com/assets/2qc3QwfnmHhjJ5RCwL5hQN/aedad77e918df194f3033a34a141fcec/saml-google-sample.zip)

## Open SSO in the web app

Log in to the Bitwarden web app and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)

Open your organization's **Settings** → **Single sign-on** screen:

![SAML 2.0 configuration ](https://bitwarden.com/assets/20720mRAluo6crSdTiYJrn/1175889d7f6ab42fe7614f34cdd1dcdd/2024-12-04_09-41-15.png)

If you haven't already, create a unique **SSO identifier**for your organization and select **SAML**from the the **Type**dropdown. Keep this screen open for easy reference.

You can turn off the **Set a unique SP entity ID**option at this stage if you wish. Doing so will remove your organization ID from your SP entity ID value, however in almost all cases it is recommended to leave this option on.

> [!TIP] Self-hosting, use alternative Member Decryption Options.
> There are alternative **Member decryption options**. Learn how to get started using [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/) or [Key Connector](https://bitwarden.com/help/about-key-connector/).

## Create a SAML app

In the Google Workspace Admin console, select **Apps** → **Web and mobile apps** from the navigation. On the Web and mobile apps screen, select **Add App** → **Add custom SAML app**:

![Create a SAML App ](https://bitwarden.com/assets/C9jyVEQXkiBxRwU82ix0U/c9cda4568d3a7f43170e4b3ef0aebab4/g-addapp.png)

### App details

On the app details screen, give the application a unique Bitwarden-specific name and select the **Continue** button.

### Google identity provider details

On the Google Identity Provider details screen, copy your **SSO URL**, **Entity ID**, and **Certificate** for [use during a later step](https://bitwarden.com/help/saml-google/#identity-provider-configuration/):

![IdP Details ](https://bitwarden.com/assets/6YxeYEY4VdrJNYO0zYkPqd/bbe5b99b54570ef14f7a4ff5a1bcb7a6/g-details.png)

Select **Continue** when you are finished.

### Service provider details

On the Service provider details screen, configure the following fields:

| **Field** | **Description** |
|------|------|
| ACS URL | Set this field to the pre-generated **Assertion Consumer Service (ACS) URL**. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |
| Entity ID | Set this field to the pre-generated **SP Entity ID**. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |
| Start URL | Optionally, set this field to the login URL from which users will access Bitwarden. For cloud-hosted customers, this is `https://vault.bitwarden.com/#/sso` or `https://vault.bitwarden.eu/#/sso`. For self-hosted instances, this is determined by your [configured server URL](https://bitwarden.com/help/install-on-premise/#configure-your-domain/), for example `https://your.domain.com/#/sso`. |
| Signed response | Check this box if you want Workspace to sign SAML responses. If not checked, Workspace will sign only the SAML assertion. |
| Name ID format | Set this field to **Persistent**. |
| Name ID | Select the Workspace user attribute to populate NameID. |

Select **Continue** when you are finished.

### Attribute mapping

On the Attribute mapping screen, select the **Add Mapping** button and construct the following mapping:

| **Google Directory attributes** | **App attributes** |
|------|------|
| Primary email | email |

Select **Finish**.

### Turn on the app

By default, Workspace SAML apps will be **OFF for everyone**. Open the User access section for the SAML app and set to **ON for everyone** or for specific Groups, depending on your needs:

![User Access ](https://bitwarden.com/assets/1cFjmvCmDIAMy6zy4e9x0a/03a1613a1186da2f014c40add256047e/g-activate.png)

**Save** your changes. Please note that it can take up to 24 hours for a new Workspace app to propagate to users existing sessions.

## Back to the web app

At this point, you have configured everything you need within the context of the Google Workspace Admin console. Return to the Bitwarden web app to complete configuration.

The Single sign-on screen separates configuration into two sections:

- **SAML service provider configuration** will determine the format of SAML requests.
- **SAML identity provider configuration** will determine the format to expect for SAML responses.

### Service provider configuration

Configure the following fields according to the choices selected in the Workspace Admin console [during setup](https://bitwarden.com/help/saml-google/#service-provider-details/):

| **Field** | **Description** |
|------|------|
| Name ID Format | Set this field to the Name ID format [selected in Workspace](https://bitwarden.com/help/saml-google/#service-provider-details/). |
| Outbound Signing Algorithm | The algorithm Bitwarden will use to sign SAML requests. |
| Signing Behavior | Whether/when SAML requests will be signed. |
| Minimum Incoming Signing Algorithm | By default, Google Workspace will sign with RSA SHA-256. Select `sha-256 `from the dropdown. |
| Expect signed assertions | Whether Bitwarden expects SAML assertions to be signed. This setting should be **unchecked**. |
| Validate Certificates | Check this box when using trusted and valid certificates from your IdP through a trusted CA. Self-signed certificates may fail unless proper trust chains are configured with the Bitwarden Login with SSO docker image. |

When you are done with the service provider configuration, **Save** your work.

### Identity provider configuration

Identity provider configuration will often require you to refer back to the Workspace Admin console to retrieve application values:

| **Field** | **Description** |
|------|------|
| Entity ID | Set this field to Workspace's **Entity ID**, retrieved from the [Google Identity Provider details section](https://bitwarden.com/help/saml-google/#google-identity-provider-details/) or using the **Download Metadata**button. This field is case sensitive. |
| Binding Type | Set to **HTTP POST**or **Redirect**. |
| Single Sign On Service URL | Set this field to Workspace's **SSO URL**, retrieved from the [Google Identity Provider details section](https://bitwarden.com/help/saml-google/#identity-provider-details/) or using the **Download Metadata**button. |
| Single Log Out URL | Login with SSO currently **does not**support SLO. This option is planned for future development, however you may pre-configure it if you wish. |
| X509 Public Certificate | Paste the [retrieved certificate](https://bitwarden.com/help/saml-google/#identity-provider-details/), removing `-----BEGIN CERTIFICATE-----`  and  `-----END CERTIFICATE-----` The certificate value is case sensitive, extra spaces, carriage returns, and other extraneous characters **will cause certification validation to fail**. |
| Outbound Signing Algorithm | By default, Google Workspace will sign with RSA SHA-256. Select `sha-256 `from the dropdown. |
| Disable Outbound Logout Requests | Login with SSO currently **does not**support SLO. This option is planned for future development. |
| Want Authentication Requests Signed | Whether Google Workspace expects SAML requests to be signed. |

> [!NOTE] X509 cert expiration
> When completing the X509 certificate, take note of the expiration date. Certificates will have to be renewed in order to prevent any disruptions in service to SSO end users. If a certificate has expired, Admin and Owner accounts will always be able to log in with email address and master password.

When you are done with the identity provider configuration, **Save** your work.

> [!TIP] Policies for SSO Guides
> You can require users to log in with SSO by activating the single sign-on authentication policy. Please note, this will require activating the single organization policy as well. [Learn more](https://bitwarden.com/help/policies/).

## Test the configuration

Once your configuration is complete, test it by navigating to [https://vault.bitwarden.com](https://vault.bitwarden.com), entering your email address and selecting the **Enterprise Single-On** button:

![Log in options screen](https://bitwarden.com/assets/3BdlHeogd42LEoG06qROyQ/c68021df4bf45d72e9d37b1fbf5a6040/login.png)

Enter the [configured organization identifier](https://bitwarden.com/help/configure-sso-saml/#step-1-enabling-login-with-sso/) and select **Log In**. If your implementation is successfully configured, you will be redirected to the Google Workspace login screen:

![Login ](https://bitwarden.com/assets/1hJ5ERnbj5UA7QriG0UPTb/95f36b9cb7573b1a966fe1331bf02fcd/g-login.png)

After you authenticate with your Workspace credentials, enter your Bitwarden master password to decrypt your vault!

> [!NOTE] SSO must be initiated from Bitwarden
> Bitwarden does not support unsolicited responses, so initiating login from your IdP will result in an error. The SSO login flow must be initiated from Bitwarden.
