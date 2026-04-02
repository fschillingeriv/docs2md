---
URL: https://bitwarden.com/help/sso-decryption-options/
---

# SSO Decryption Options

Using SSO with Bitwarden retains our zero-knowledge encryption model. Nobody at Bitwarden has access to your data and, similarly, **neither should your Identity Provider**. That's why SSO **decouples authentication and decryption**. In all implementations, your Identity Provider cannot and will not have access to the decryption key needed to decrypt vault data.

**SSO decryption options** are used to determine what decryption key will be used to decrypt vault data in scenarios where SSO is handling authentication. Options include:

- **Master password**: Once authenticated, organization members will decrypt vault data using their [master passwords](https://bitwarden.com/help/master-password/).
- **Trusted devices**: Allows users to authenticate with SSO and decrypt their vault [using a device-stored encryption key](https://bitwarden.com/help/about-trusted-devices/), eliminating the need to enter a master password.
- **Key Connector**: Connect to a self-hosted decryption key server. Using this option, organization members won't need to use their master passwords to decrypt vault data. Instead, [Key Connector](https://bitwarden.com/help/about-key-connector/) will retrieve a decryption key securely stored in a database owned and managed by you.

> [!NOTE] Key Connector disabled default
> Due to the sensitivity of storing decryption keys, the **Key Connector** option is disabled by default and currently only available to organizations self-hosting Bitwarden.
> 
> If you're interesting in using Key Connector, check out the [About Key Connector](https://bitwarden.com/help/about-key-connector/) and [Deploy Key Connector](https://bitwarden.com/help/deploy-key-connector/) articles and [contact us](https://bitwarden.com/contact/) to setup a time for us to help you get started.
