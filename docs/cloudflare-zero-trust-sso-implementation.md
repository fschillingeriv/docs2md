---
URL: https://bitwarden.com/help/cloudflare-zero-trust-sso-implementation/
---

# Cloudflare Zero Trust SSO

This article contains **Cloudflare Zero Trust-specific** help for configuring login with SSO. Cloudflare Zero Trust is a cloud-based identity and access management platform that can integrate with multiple identity providers (IdPs). You can also configure gateways and tunneling for secure access to the platform.

> [!NOTE] CFZT prerequisite information
> Cloudflare Zero Trust can be configured with any IdP that operates using SAML 2.0 or OIDC SSO configurations. If you are not familiar with these configurations, refer to these articles:
> 
> - [SAML 2.0 Configuration](https://bitwarden.com/help/configure-sso-saml/)
> - [OIDC Configuration](https://bitwarden.com/help/configure-sso-oidc/)

## Why use Cloudflare Zero Trust with SSO?

Cloudflare Zero Trust is a cloud-based proxy identity and access management platform that can integrate with multiple identity providers (IdPs). The benefit of using Cloudflare Zero Trust in addition to your standard IdP is its ability to configure multiple IdPs for login. Cloudflare Zero Trust can provide SSO access to Bitwarden from multiple separate directories, or sets of users within a directory.

## Open SSO in the web app

> [!NOTE] Bitwarden requires SAML 2.0
> Cloudflare will only support SAML via the Access Application Gateway. This means that the **SAML 2.0** must be selected in the Bitwarden configuration. OIDC authentication can still be configured from the IdP and Cloudflare.

Log in to the Bitwarden web app and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)

Open your organization's **Settings** → **Single sign-on** screen:

![SAML 2.0 configuration ](https://bitwarden.com/assets/20720mRAluo6crSdTiYJrn/1175889d7f6ab42fe7614f34cdd1dcdd/2024-12-04_09-41-15.png)

If you haven't already, create a unique **SSO identifier**for your organization and select **SAML**from the the **Type**dropdown. Keep this screen open for easy reference.

You can turn off the **Set a unique SP entity ID**option at this stage if you wish. Doing so will remove your organization ID from your SP entity ID value, however in almost all cases it is recommended to leave this option on.

> [!TIP] Self-hosting, use alternative Member Decryption Options.
> There are alternative **Member decryption options**. Learn how to get started using [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/) or [Key Connector](https://bitwarden.com/help/about-key-connector/).

## Create a Cloudflare Zero Trust login method

Create a Cloufdlare Zero Trust login method:

1. Navigate to [Cloudflare Zero Trust](https://dash.cloudflare.com/login) and log in or create an account.
2. Configure a domain, which will act as the URL used by your users to access your applications or **App Launcher**, for example `https://my-business.cloudflareaccess.com/`. From the Cloudflare Zero Trust menu , select **Settings**→**Custom Pages**:

![Team domain setting](https://bitwarden.com/assets/4lN2NFw46RAynArFfiW3kD/6dfd8ef5b844347a60f9e230b9736450/2024-12-16_15-43-43.png)
3. Begin configuring the first login method by navigating to **Settings**→ **Authentication**→ **Add new.**
4. Select the login method to connect to Cloudflare Zero Trust. If the IdP you are using is not present on the IdP list, use the SAML or OIDC generic options. In this article, Okta will be used as an example:

![Cloudflare Zero Trust IdP list ](https://bitwarden.com/assets/5Zk3txh2X9fhcPVpMZVJPC/18ad36aaf277af50df063c96f89804e8/Screen_Shot_2022-10-11_at_4.17.21_PM.png)

> [!NOTE] Google Workspace app cannot be used for login methos
> Google Workspace users should select the generic **SAML** setup during this step. The Google Workspace login method may result in errors.
5. After selecting your chosen IdP login method, follow the in-product guide provided by Cloudflare for integrating your IdP.

> [!NOTE] Disable support groups cfzt
> If the IdP you are using has a **support groups** feature, this option must be **disabled**. Bitwarden does not support group based claims, enabling this option will result in an XML element error on the Bitwarden end.

## Create a Cloudflare Zero Trust application

After an IdP has been configured, you'll have to create a Cloudflare Zero Trust application for Bitwarden. **In this example we'll create a SAML application**:

1. Navigate to **Access**→ **Applications**→ **Add an application**and then select **SaaS**.

![CFZT add an application](https://bitwarden.com/assets/70oK8FUQYXpKEvX00NZ9ai/a065258c17b5b01360a6aed574ce2192/2024-07-08_10-46-37.png)

2. On the following screen, add an Application name such as **Bitwarden**. Then, Select the authentication protocol, **SAML**. Once complete, select **Add application**.

![Add an application Cloufflare Zero Trust](https://bitwarden.com/assets/1zm03fKF8Nqu30YbH7duoo/58e66188a1437c3339daee414d7f9bb3/2024-07-08_10-43-34.png)

3. In the Bitwarden web vault, open your organization and navigate to the **Settings**→ **Single Sign-On** screen. Use information from the web vault to fill-in information on the **Configure app**screen:

| **Key** | **Description** |
|------|------|
| **Application** | Enter `Bitwarden`. |
| **Entity ID** | Copy the **SP entity ID**from the Bitwarden Single Sign-On page into this field. |
| **Assertion Consumer Service URL** | Copy the **Assertion consumer service (ACS) URL**from the Bitwarden Single Sign-On page into this field. |
| **Name ID Format** | Select **Email**from the dropdown menu. |

> [!NOTE] CFZT OIDC
> For the generic OIDC configuration, the Auth URL, Token URL, and Certificate URL can be located with the well-known URL.

4. Scroll down to the **Identity providers** menu. Select the IdP(s) that you configured in the previous section, scroll back to the top, and select **Next.**

5. Next, create access policies for user access to the application. Complete the **Policy name**, **Action**, and **Session duration**fields for each policy.

6. You can choose to assign a group policy (**Access**→ **Groups**) or explicit user policy rules (such as emails, "emails ending in", "country", or "everyone"). In the following example, the group "Anon Users" has been included in the policy. An additional rule has been added as well to include emails ending in the chosen domain:

![CFZT app policy](https://bitwarden.com/assets/2VCZsMzbeUtuO9jx1oh6g7/a1fbe343872934b796ce486cf46835fb/Screen_Shot_2022-10-12_at_10.55.31_AM.png)

> [!NOTE] User access to the app launcher
> You can also apply user access through the **App Launcher**for access to the Bitwarden login with SSO shortcut. This can be managed by navigating to **Authentication**→ **App Launcher**→ **Manage**. The application policies in the above example can be duplicated or generated here.

7. Once access policies have been configured, scroll to the top and select **Next**.

8. While on the **Setup** screen, copy the following values and input them into their respective fields on the Bitwarden **Single Sign-On**page:

| **Key** | **Description** |
|------|------|
| **SSO endpoint** | The SSO endpoint directs where your SaaS application will send login requests. This value will be entered into the **Single Sign On Service URL** field in Bitwarden. |
| **Access Entity ID or Issuer** | The Access Entity ID or Issuer is the unique identifier of your SaaS application. This will value will be entered into the **Entity ID** field on Bitwarden. |
| **Public key** | The Public key is the access public certificate that will be used to verify your identity. This value will be entered into the **X509 Public Certificate** field on Bitwarden. |

9. After the values have been entered into Bitwarden, select **Save**on the Bitwarden Single Sign-On screen and select **Done**on the Cloudflare page to save the application. 

10. To create a bookmark to the Bitwarden login with SSO screen, select **Add an application**→ **Bookmark**. Check that the Bookmark is visible in the **App launcher**.

## Test the configuration

Once your configuration is complete, test it by navigating to [https://vault.bitwarden.com](http://www.vault.bitwarden.com/) or [https://vault.bitwarden.eu](https://vault.bitwarden.eu/), entering your email address and selecting the **Use single sign-on** button:

![Log in options screen](https://bitwarden.com/assets/3BdlHeogd42LEoG06qROyQ/c68021df4bf45d72e9d37b1fbf5a6040/login.png)

Enter the configured organization identifier and select **Log In**. If your implementation is successfully configured, you will be redirected to a Cloudflare Access screen, where you can select the IdP to login with:

![Cloudflare IdP selection](https://bitwarden.com/assets/5SyHu8lc0ZJqjpL4hF53ie/b0d661e6772b58f681c47b7b01ebbaa0/Screen_Shot_2022-10-12_at_5.15.39_PM__2_.png)

After selecting your IdP, you will be directed to your IdP login page. Enter in the information used to login via your IdP:

![CFZT IdP login](https://bitwarden.com/assets/7Avc5GWZaeGSk59v3rZ531/3be901d4f137012ef6d1e3cb13d9a4eb/Screen_Shot_2022-10-13_at_4.45.02_PM.png)

After you authenticate with your IdP credentials, enter your Bitwarden credentials to decrypt your vault!
