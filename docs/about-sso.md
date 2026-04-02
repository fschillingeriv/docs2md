---
URL: https://bitwarden.com/help/about-sso/
---

# About Single Sign-On

Using single sign-on (SSO), [Enterprise organizations](https://bitwarden.com/help/about-organizations/#types-of-organizations/) can leverage their existing Identity Provider (IdP) to authenticate members with Bitwarden. SSO for Enterprise organizations include:

- [SAML 2.0](https://bitwarden.com/help/configure-sso-saml/) and [OIDC](https://bitwarden.com/help/configure-sso-oidc/) configuration options that support integration with a wide variety of IdPs.
- An [enterprise policy](https://bitwarden.com/help/policies/#require-single-sign-on-authentication/) to optionally **require** non-administrative members to log in to Bitwarden with SSO.
- An [enterprise policy](https://bitwarden.com/help/policies/#automatically-log-in-users-for-allowed-applications/) to optionally allow easier auto-fill in non-SSO apps launched from your IdP.
- Several distinct [member decryption options](https://bitwarden.com/help/sso-decryption-options/) for safe data access workflows.
- [Just-In-Time (JIT) provisioning](https://bitwarden.com/help/jit-provisioning/) of members via SSO.

> [!TIP] SSO Decryption Options
> Using SSO with Bitwarden retains our zero-knowledge encryption model. Nobody at Bitwarden has access to your data and, similarly, **neither should your Identity Provider**. That's SSO **decouples authentication and decryption**. In all implementations, your Identity Provider cannot and will not have access to the decryption key needed to decrypt vault data.
> 
> While authentication is handled via your IdP, decryption of your data is controlled by one of several [decryption methods](https://bitwarden.com/help/sso-decryption-options/).

![SSO and master password decryption](https://bitwarden.com/assets/76IOpVRQv886zcUYIM2HF0/36300f14123231d0da18081adcc9962b/sso-workflow-3.png)
*SSO and master password decryption*

If you're new to Bitwarden, [start a 7-day Enterprise free trial](https://bitwarden.com/go/start-enterprise-trial/) to begin testing SSO. We recommend this following steps when testing SSO:

1. Configure your SSO integration using one of the **SSO Guides** for your chosen IdP. If your IdP isn't listed, you can use the [generic SAML](https://bitwarden.com/help/configure-sso-saml/) or [generic OIDC](https://bitwarden.com/help/configure-sso-oidc/) guide.
2. Test the [member login experience](https://bitwarden.com/help/using-sso/) using master password decryption.
3. Assess whether a different [member decryption options](https://bitwarden.com/help/sso-decryption-options/) would fit your implementation, and if so begin configuration of that decryption option.
4. Provide information to members, based on the specifics of your implementation, about how to[ log in with SSO](https://bitwarden.com/help/using-sso/).
