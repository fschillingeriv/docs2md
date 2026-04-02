---
URL: https://bitwarden.com/help/november-deprecation-notice/
---

# November Deprecation Notice

With the next release of Bitwarden (2022.11.0), planned for 11-16-2022, two endpoints of the Bitwarden server's API service will be deprecated. The function of the endpoints that will be deprecated will be taken over by endpoints in the Identity service.

The new endpoints, which will be used by Bitwarden clients of version 2022.11.0 and above, were added in server version 1.46.0. **This means that self-hosted servers running version 1.45.4 or any earlier version will not be compatible with 2022.11.0 clients.**[ Learn how to check your server version.](https://bitwarden.com/help/versioning/)

We recommend [updating your self-hosted server](https://bitwarden.com/help/updating-on-premise/) prior to the release of 2022.11.0. If for any reason you cannot, [contact us](https://bitwarden.com/contact/).

> [!NOTE] Non-updated Server & Web Vault
> As the web vault is packaged with server, the web vault will continue to work normally if you do not update your server.
