---
URL: https://bitwarden.com/help/saml-auth0/
---

# Auth0 SAML

This article contains **Auth0-specific** help for configuring Login with SSO via SAML 2.0. For help configuring login with SSO for another IdP, refer to [SAML 2.0 Configuration](https://bitwarden.com/help/configure-sso-saml/).

Configuration involves working simultaneously within the Bitwarden web app and the Auth0 Portal. As you proceed, we recommend having both readily available and completing steps in the order they are documented.

> [!NOTE]
> **Already an SSO expert?** Skip the instructions in this article and download screenshots of sample configurations to compare against your own.
> 
> ⬇️ [Download Sample](https://bitwarden.com/assets/20UMzdVJ0bPm0ggsNF1QE5/e88a1f1e2ffbaddcf42c65d404916c23/saml-auth0-sample.zip)

## Open SSO in the web app

Log in to the Bitwarden web app and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)

Open your organization's **Settings** → **Single sign-on** screen:

![SAML 2.0 configuration ](https://bitwarden.com/assets/20720mRAluo6crSdTiYJrn/1175889d7f6ab42fe7614f34cdd1dcdd/2024-12-04_09-41-15.png)

If you haven't already, create a unique **SSO identifier**for your organization and select **SAML**from the the **Type**dropdown. Keep this screen open for easy reference.

You can turn off the **Set a unique SP entity ID**option at this stage if you wish. Doing so will remove your organization ID from your SP entity ID value, however in almost all cases it is recommended to leave this option on.

> [!TIP] Self-hosting, use alternative Member Decryption Options.
> There are alternative **Member decryption options**. Learn how to get started using [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/) or [Key Connector](https://bitwarden.com/help/about-key-connector/).

## Create an Auth0 application

In the Auth0 Portal, use the Applications menu to create a **Regular Web Application**:

![Auth0 Create Application ](https://bitwarden.com/assets/3EsE3HTVqocRvC1f2XSWbt/9077b5bc7801de7270372594e62b7aad/auth0-createapp.png)

Click the **Settings** tab and configure the following information, some of which you will need to retrieve from the Bitwarden Single Sign-On screen:

![Auth0 Settings ](https://bitwarden.com/assets/6MMUA6fh1HBgeEa1lCWXc5/4dc49064bcd846f5973595fed3f525e9/auth0-appsettings.png)

| **Auth0 Setting** | **Description** |
|------|------|
| Name | Give the application a Bitwarden-specific name. |
| Domain | Take note of this value. You will need it [during a later step](https://bitwarden.com/help/saml-auth0/#identity-provider-configuration/). |
| Application Type | Select **Regular Web Application**. |
| Token Endpoint Authentication Method | Select **Client Secret**(**Post)**, which will map to a **Binding Type**attribute you will [configure later](https://bitwarden.com/help/saml-auth0/#identity-provider-configuration/). |
| Application Login URI | Set this field to the pre-generated **SP Entity ID**. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |
| Allowed Callback URLS | Set this field to the pre-generated **Assertion Consumer Service (ACS) URL**. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |

#### Grant Types

In the **Advanced Settings** → **Grant Types** section, ensure that the following Grant Types are selected (they may be pre-selected):

![Application Grant Types ](https://bitwarden.com/assets/6Pl6X2GbNJmgIN0xQgJcoV/f1af38c91fa568b99c77b3b21e78d017/auth0-advancedsettings.png)

#### Certificates

In the **Advanced Settings** → **Certificates** section, copy or download up your signing certificate. You won't need to do anything with it just yet, but you will need to [reference it later](https://bitwarden.com/help/saml-auth0/#identity-provider-configuration/).

![Auth0 Certificate ](https://bitwarden.com/assets/1VeE8trhYRSDBVBpmdlJDA/4bc9ed89e8e8b539f3d2c2791f2f42eb/auth0-certificate.png)

#### Endpoints

You don't need to edit anything in the **Advanced Settings** → **Endpoints** section, but you will need the SAML endpoints to [reference later](https://bitwarden.com/help/saml-auth0/#identity-provider-configuration/).

> [!NOTE]
> In smaller windows, the **Endpoints** tab can disappear behind the edge of the browser. If you're having trouble finding it, click the **Certificates** tab and hit the Right Arrow key (→).

![Auth0 Endpoints ](https://bitwarden.com/assets/6eUrnDaSf3W67POfR0IKgq/6d120ea3b1ffc7a194ccbefd31e047d9/auth0-endpoints.png)

## Configure Auth0 actions

Create actions to customize the logic that Auth0 will use during the post-login flow and dictate the parameters of the exchange with Bitwarden. To create the necessary action:

1. Navigate to **Actions**→ **Library** and select **Create Action** → **Build from scratch**.
2. Give you action a name like `Bitwarden SSO`, chose the **Login / Post Login** Trigger, choose the **Node 18 (Recommended)** Runtime option, and select **Create**.
3. In the integrated code editor, add the following rule:

```javascript
exports.onExecutePostLogin = async (event, api) => {
 // Modify SAML configuration settings
 if (event.request.protocol === 'samlp') {
 api.saml.updateConfiguration({
 signatureAlgorithm: "rsa-sha256",
 digestAlgorithm: "sha256",
 signResponse: true,
 nameIdentifierFormat: "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
 binding: "urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect"
 });
 }
};
```
4. Select **Deploy**.
5. Navigate to **Actions**→ **Triggers**and select the `post-login` trigger.
6. Drag and drop your new action into the **Post Login** flow and select **Apply**.

When configuring the above action, you can customize any of the following attributes to fit your needs:

| **Key** | **Description** |
|------|------|
| `signatureAlgorithm` | Algorithm Auth0 will use to sign the SAML assertion or response. This value should be set to `rsa-sha256`. You must also set: -Set `digestAlgorithm `to `sha256`. -Set (in Bitwarden) the **Minimum Incoming Signing Algorithm**to `rsa-sha256`. |
| `digestAlgorithm` | Algorithm used to calculate digest of SAML assertion or response. Set to `sha-256`. |
| `signResponse` | By default, Auth0 will sign only the SAML assertion. Set this to `true `to sign the SAML response instead of the assertion. |
| `nameIdentifierFormat` | By default, `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`. You can set this value to [any SAML NameID format](https://docs.oracle.com/cd/E19316-01/820-3886/ggwbz/index.html). If you do, change the SP **Name ID Format**field to the corresponding option (see [here](https://bitwarden.com/help/saml-auth0/#service-provider-configuration/)). |

### Migrate from rules to actions

On November 18, 2024 Auth0 will deprecate rules. If you are currently using a rule as described in a previous version of this document, you can use a **Migrate to Action** button on the Auth0 Rules screen to make this process easier. If you do this:

- Do not toggle the pre-existing rule off.
- Do add the new action to your `post-login` trigger as described above in steps 5 & 6.

## Back to the web app

At this point, you have configured everything you need within the context of the Auth0 Portal. Return to the Bitwarden web app to complete configuration.

The Single sign-on screen separates configuration into two sections:

- **SAML service provider configuration** will determine the format of SAML requests.
- **SAML identity provider configuration** will determine the format to expect for SAML responses.

### Service provider configuration

Unless you have configured [custom rules](https://bitwarden.com/help/saml-auth0/#configure-auth0-rules/), your service provider configuration will already be complete. If you configured custom rules or want to make further changes to your implementation, edit the relevant fields:

| **Field** | **Description** |
|------|------|
| Name ID Format | [NameID Format](https://docs.oracle.com/cd/E19316-01/820-3886/ggvxx/index.html) to specify in the SAML request (`NameIDPolicy`). To omit, set to **Not Configured**. |
| Outbound Signing Algorithm | Algorithm used to sign SAML requests, by default `rsa-sha256`. |
| Signing Behavior | Whether/when Bitwarden SAML requests will be signed. By default, Auth0 will not require requests to be signed. |
| Minimum Incoming Signing Algorithm | The minimum signing algorithm Bitwarden will accept in SAML responses. Select `rsa-sha256 `from the dropdown unless you have configured a [custom signing rule](https://bitwarden.com/help/saml-auth0/#configure-auth0-rules/). |
| Want Assertions Signed | Whether Bitwarden wants SAML assertions signed. By default, Auth0 will sign SAML assertions, so check this box unless you've configured a [custom signing rule](https://bitwarden.com/help/saml-auth0/#configure-auth0-rules/). |
| Validate Certificates | Check this box when using trusted and valid certificates from your IdP through a trusted CA. Self-signed certificates may fail unless proper trust chains are configured within the Bitwarden Login with SSO docker image. |

When you are done with the service provider configuration, **Save** your work.

### Identity provider configuration

Identity provider configuration will often require you to refer back to the Auth0 Portal to retrieve application values:

| **Field** | **Description** |
|------|------|
| Entity ID | Enter the **Domain**value of your Auth0 application (see [here](https://bitwarden.com/help/saml-auth0/#create-an-auth0-application/)), prefixed by `urn:`, for example `urn:bw-help.us.auth0.com`. This field is case sensitive. |
| Binding Type | Select **HTTP POST**to match the [Token Endpoint Authentication Method](https://bitwarden.com/help/saml-auth0/#create-an-auth0-application/) value specified in your Auth0 application. |
| Single Sign On Service URL | Enter the **SAML Protocol URL**(see [Endpoints](https://bitwarden.com/help/saml-auth0/#endpoints/)) of your Auth0 application. For example, `https://bw-help.us.auth0.com/samlp/HcpxD63h7Qzl420u8qachPWoZEG0Hho2`. |
| Single Log Out Service URL | Login with SSO currently **does not**support SLO. This option is planned for future development, however you may pre-configure it if you wish. |
| X509 Public Certificate | Paste the retrieved [signing certificate](https://bitwarden.com/help/saml-auth0/#certificates/), removing `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` The certificate value is case sensitive, extra spaces, carriage returns, and other extraneous characters **will cause certification validation to fail**. |
| Outbound Signing Algorithm | Select `rsa-sha256 `unless you've configured a [custom signing rule](https://bitwarden.com/help/saml-auth0/#configure-auth0-rules/). |
| Disable Outbound Logout Requests | Login with SSO currently **does not**support SLO. This option is planned for future development. |
| Want Authentication Requests Signed | Whether Auth0 expects SAML requests to be signed. |

> [!NOTE] X509 cert expiration
> When completing the X509 certificate, take note of the expiration date. Certificates will have to be renewed in order to prevent any disruptions in service to SSO end users. If a certificate has expired, Admin and Owner accounts will always be able to log in with email address and master password.

When you are done with the identity provider configuration, **Save** your work.

> [!TIP] Policies for SSO Guides
> You can require users to log in with SSO by activating the single sign-on authentication policy. Please note, this will require activating the single organization policy as well. [Learn more](https://bitwarden.com/help/policies/).

## Test the configuration

Once your configuration is complete, test it by navigating to [https://vault.bitwarden.com](https://vault.bitwarden.com), entering your email address and selecting the **Use single sign-on** button:

![Log in options screen](https://bitwarden.com/assets/3BdlHeogd42LEoG06qROyQ/c68021df4bf45d72e9d37b1fbf5a6040/login.png)

Enter the [configured organization identifier](https://bitwarden.com/help/saml-auth0/#/) and select **Log In**. If your implementation is successfully configured, you will be redirected to the Auth0 login screen:

![Auth0 Login ](https://bitwarden.com/assets/h2jxKn7KCsKPE3qYqvt3y/657246df1424b743436b3f9ec1d8c559/auth0-login.png)

After you authenticate with your Auth0 credentials, enter your Bitwarden master password to decrypt your vault!

> [!NOTE] SSO must be initiated from Bitwarden
> Bitwarden does not support unsolicited responses, so initiating login from your IdP will result in an error. The SSO login flow must be initiated from Bitwarden.
