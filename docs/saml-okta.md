---
URL: https://bitwarden.com/help/saml-okta/
---

# Okta SAML

This article contains **Okta-specific** help for configuring Login with SSO via SAML 2.0. For help configuring login with SSO for another IdP, refer to [SAML 2.0 Configuration](https://bitwarden.com/help/configure-sso-saml/).

Configuration involves working simultaneously within the Bitwarden web app and the Okta Admin Portal. As you proceed, we recommend having both readily available and completing steps in the order they are documented.

> [!TIP] Okta settings screenshot
> **Already an SSO expert?** Skip the instructions in this article and download screenshots of sample configurations to compare against your own.
> 
> ⬇️ [Download Sample](https://bitwarden.com/assets/3tQfArvZQ1vigzlnjdBxr1/364da08e7280662e743b6f6b75eb225f/saml-okta.zip.zip)

## Open SSO in the web app

Log in to the Bitwarden web app and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
*Product switcher*

Open your organization's **Settings** → **Single sign-on** screen:

![SAML 2.0 configuration ](https://bitwarden.com/assets/20720mRAluo6crSdTiYJrn/1175889d7f6ab42fe7614f34cdd1dcdd/2024-12-04_09-41-15.png)
*SAML 2.0 configuration *

If you haven't already, create a unique **SSO identifier**for your organization and select **SAML**from the the **Type**dropdown. Keep this screen open for easy reference.

You can uncheck **Set a unique SP entity ID**. If you do, this will remove your organization ID from your SP entity ID value. We recommend leaving this setting checked in almost all cases.

> [!TIP] Self-hosting, use alternative Member Decryption Options.
> There are alternative **Member decryption options**. Learn how to get started using [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/) or [Key Connector](https://bitwarden.com/help/about-key-connector/).

## Create an Okta application

Next, create a new Okta application:

1. From the Okta Admin Portal, go to **Applications** → **Applications**.
2. Select **Create App Integration.**
3. Select **SAML 2.0**:

![Create new app for SAML 2.0](https://bitwarden.com/assets/6QTVpxi659XVt11Azdtoz/38f8eb0cb2d003de0bba59bf4a6fa3be/Create_new_app_for_SAML_2.0.png)
*Create new app for SAML 2.0*
4. Select **Next**, which will open the app's general settings.
5. Enter a unique, Bitwarden-specific name in **App name**.
6. Select **Next**.

### Configure SAML

This will open the **Configure SAML** page. Configure the following fields:

| **Field** | **Description** |
|------|------|
| Single sign on URL | Set this field to the pre-generated **Assertion Consumer Service (ACS) URL**. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |
| Audience URI (SP Entity ID) | Set this field to the pre-generated **SP Entity ID**. This automatically-generated value can be copied from the organization's **Settings** → **Single sign-on** screen and will vary based on your setup. |
| Name ID format | Select the [SAML NameID format](https://docs.oracle.com/cd/E19316-01/820-3886/ggwbz/index.html) to use in SAML assertions. By default, **Unspecified**. |
| Application username | Select the Okta attribute users will use to login to Bitwarden, typically **Email**. |

### Advanced settings

Next, select **Show Advanced Settings**:

![Show Advanced Settings](https://bitwarden.com/assets/7vxaIVnLCCTyb55hOpkctS/13481c873198fca937f2c92045bbc8c3/Show_Advanced_Settings.png)
*Show Advanced Settings*

Set up these fields:

| **Field** | **Description** |
|------|------|
| Response | Whether the SAML response is signed by Okta. |
| Assertion Signature | Whether the SAML assertion is signed by Okta. |
| Signature Algorithm | The signing algorithm used to sign the response and/or assertion, depending on which is set to **Signed**. By default, `rsa-sha256`. |
| Digest Algorithm | The digest algorithm used to sign the response and/or assertion, depending on which is set to **Signed**. This field must match the selected **Signature Algorithm**. |

Once configured, select **Next** and then **Finish**.

### Attribute statements

To define attribute statements in your new Bitwarden app:

1. Go to the **Sign On** tab.
2. Within the **Attribute statements** section, select **Show legacy configuration**.
3. Select **Edit**:

![Create attribute statements](https://bitwarden.com/assets/6zV8VlsjIKhynmkq6p1xpW/a85a7d67ba233cfeeb569c5861d0203b/Create_attribute_statements.png)
*Create attribute statements*
4. By default, one line will appear below to build an attribute statement. Select **Add Another** twice so you can build these three SP → IdP attribute mappings. Then select **Save**:

| **Name** | **Name format** | **Value** |
|------|------|------|
| email | Unspecified | user.email |
| firstname | Unspecified | user.firstName |
| lastname | Unspecified | user.lastName |

### Get IdP values

While still on the **Sign On** tab, select **View Setup Instructions** on the right:

![View SAML setup instructions](https://bitwarden.com/assets/20AjFNFk4VoBt2HrDtB9Zt/86bb2b1181f09d03b1ac7ac05844c46e/View_SAML_setup_instructions.png)
*View SAML setup instructions*

Leave this page open for [next steps](https://bitwarden.com/help/saml-okta/#saml-identity-provider-configuration/), or copy the **Identity Provider Single Sign-On URL** and **Identity Provider issuer** and download the **X.509 Certificate**:

![IdP values](https://bitwarden.com/assets/3oc8QKbmtLzkZctLDxCCes/356c439aca47a5d0bca3c14ce0126ab2/IdP_values_.png)
*IdP values*

### Assignments

Return to your Bitwarden app configuration in Okta and go to **Assignments**. Select **Assign**:

![Assign to People or Groups](https://bitwarden.com/assets/1XoCbTbrAZV37R3wBTHgVl/0030e828cc635e1a70a719c94885f5ac/Assign_to_People_or_Groups.png)
*Assign to People or Groups*

You can assign access to the application on a user-by-user basis using the **Assign to People** option or in-bulk using the **Assign to Groups** option.

## Back to the web app

At this point, you've configured everything needed within the Okta Admin Portal. Open the Bitwarden web app and go to **Settings** → **Single sign-on** to complete your SSO setup.

### SAML service provider configuration

The first section is **SAML service provider configuration** and determine the format of SAML requests. Configure the following fields according to the choices selected in the Okta Admin Portal [during app creation](https://bitwarden.com/help/saml-okta/#create-an-okta-application/):

| **Field** | **Description** |
|------|------|
| Name ID format | Set this to whatever the Name ID format [specified in Okta](https://bitwarden.com/help/saml-okta/#configure-saml/), otherwise leave **Unspecified**. |
| Outbound signing algorithm | The algorithm Bitwarden will use to sign SAML requests. |
| Signing behavior | Whether/when SAML requests will be signed. |
| Minimum incoming signing algorithm | Set this to the Signature Algorithm [specified in Okta](https://bitwarden.com/help/saml-okta/#advanced-settings/). |
| Expect signed assertions | Check this box if you set the Assertion Signature field to **Signed**[in Okta](https://bitwarden.com/help/saml-okta/#advanced-settings/). |
| Validate certificates | Check this box when using trusted and valid certificates from your IdP through a trusted CA. Self-signed certificates may fail unless proper trust chains are configure within the Bitwarden login with SSO docker image. |

When you're done with the service provider configuration, select **Save**.

### SAML identity provider configuration

The second section on this page is **SAML identity provider configuration** and determines the format to expect for SAML responses. Refer back to the Okta Admin Portal to retrieve some of these values:

| **Field** | **Description** |
|------|------|
| Entity ID | Enter your **Identity Provider Issuer**, retrieved from the Okta [Sign On Settings](https://bitwarden.com/help/saml-okta/#get-idp-values/) screen by selecting the **View Setup Instructions**button. This field is case sensitive. |
| Binding type | Set to **Redirect**. Okta currently does not support HTTP POST. |
| Single sign-on service URL | Enter your **Identity Provider Single Sign-On URL**, retrieved from the Okta [Sign On Settings](https://bitwarden.com/help/saml-okta/#get-idp-values/) screen. |
| Single log-out service URL | Login with SSO currently **does not**support SLO. |
| X509 public certificate | Paste the [downloaded certificate](https://bitwarden.com/help/saml-okta/#get-idp-values/), removing `-----BEGIN CERTIFICATE-----` and  `-----END CERTIFICATE-----` The certificate value is case sensitive, extra spaces, carriage returns, and other extraneous characters **will cause certification validation to fail**. |
| Outbound signing algorithm | Select the Signature Algorithm selected [during Okta app configuration](https://bitwarden.com/help/saml-okta/#advanced-settings/). If you didn't change the Signature Algorithm, leave the default (`rsa-sha256`). |
| Allow outbound logout requests | Login with SSO currently **does not**support SLO. |
| Sign authentication requests | Whether Okta expects SAML requests to be signed. |

> [!NOTE] X509 cert expiration
> When completing the X509 certificate, take note of the expiration date. Certificates will need to be renewed to prevent any disruptions in service to SSO end-users. If a certificate expires, Admin and Owner accounts can still log in with their email address and master password.

When you're done with the identity provider configuration, select **Save**.

> [!TIP] Policies for SSO Guides
> You can require users to log in with SSO by activating the [single sign-on authentication policy](https://bitwarden.com/help/policies/#require-single-sign-on-authentication/).

## Test the configuration

Once your configuration is complete, test it. Go to [https://vault.bitwarden.com](https://vault.bitwarden.com), enter your email address, and select **Use single sign-on**:

![Log in options screen](https://bitwarden.com/assets/3BdlHeogd42LEoG06qROyQ/c68021df4bf45d72e9d37b1fbf5a6040/login.png)
*Log in options screen*

Enter the [configured organization identifier](https://bitwarden.com/help/configure-sso-saml/#step-1-enabling-login-with-sso/) and select **Continue**. If your implementation is successfully configured, you will be redirected to the Okta login screen:

![Log in with Okta ](https://bitwarden.com/assets/3Rh2Bg17sCE57xJsUKfqwN/8f6e1d8555c9e1b60d2e145d0f0bb565/Log_in_with_Okta.png)
*Log in with Okta *

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
