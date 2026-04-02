---
URL: https://bitwarden.com/help/change-client-environment/
---

# Connect Individual Clients

By default, Bitwarden clients will connect to Bitwarden-hosted servers, but any client application can be configured to connect to your self-hosted Bitwarden instance instead. 

> [!NOTE] If you do not wish to connect to a self-hosted instance
> If you are trying to connect to a Bitwarden-hosted server, but your client is attempting to connect to a self-hosted instance, select **bitwarden.com** or **bitwarden.eu** from the **Logging in on** menu.

### Browser extension

To connect a browser extension to your self-hosted server:

1. On the login or registration screen, select the **Logging in on**dropdown and choose the **Self-hosted**option.

![Self-hosted server selection](https://bitwarden.com/assets/1Pq95ZZLLySxwjLr7eul5W/326732e7943499236adf16e6a16378b6/2024-12-04_10-05-14.png)
2. In the **Server URL**field, enter the domain name for your server with `https://` (for example, `https://my.bitwarden.domain.com`).
3. Select **Save**.

> [!TIP] Advanced Client-Server Specification
> Users with unique setups can specify the URL of each service independently in the **Custom Environment**section.

### Mobile app

To connect a mobile app to your self-hosted server:

1. On the login or registration screen, select the **Logging in on**dropdown and choose the **Self-hosted**option.

![Server selection on mobile](https://bitwarden.com/assets/0mBtygWpIfx8MLtcPwxwD/0041c5a129a88b9fb5dd021a07a6da4e/2025-01-22_10-17-39.png)
2. In the **Server URL**field, enter the domain name for your server with `https://` (for example, `https://my.bitwarden.domain.com`).
3. Select **Save**.

> [!TIP] Advanced Client-Server Specification
> Users with unique setups can specify the URL of each service independently in the **Custom Environment**section.

### Desktop app

[Each account](https://bitwarden.com/help/account-switching/) that's logged in to your desktop app can be connected to a different server. To connect an account to your self-hosted server:

1. On the login or registration screen, select the **Logging in on**dropdown and choose the **Self-hosted**option.

![Server selection desktop](https://bitwarden.com/assets/4KVc44Osl3K38W0dxdCl3M/53ad13b8f456e8d92594c29c54091bd0/desktop.png)
2. In the **Server URL**field, enter the domain name for your server with `https://` (for example, `https://my.bitwarden.domain.com`).
3. Select **Save**.

> [!TIP] Advanced Client-Server Specification
> Users with unique setups can specify the URL of each service independently in the **Custom Environment**section.

### CLI

To connect the CLI to your self-hosted server:

1. Logout using the `bw logout` command.
2. Use the following command to connect the CLI to your self-hosted server:

```
bw config server https://your.bw.domain.com
```

Users with unique setups can specify the URL of each service independently using the following commands:

```
bw config server --web-vault <url>
bw config server --api <url>
bw config server --identity <url>
bw config server --icons <url>
bw config server --notifications <url>
bw config server --events <url>
bw config server --key-connector <url>
```
