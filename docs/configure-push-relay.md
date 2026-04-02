---
URL: https://bitwarden.com/help/configure-push-relay/
---

# Configure Push Relay

By default, your self-hosted Bitwarden server is configured to communicate with Bitwarden's push relay service (`https://push.bitwarden.com`). You can configure the server with your own push relay service, connect to the EU push relay service (`https://push.bitwarden.eu`) if you're using the [EU cloud](https://bitwarden.com/help/server-geographies/), or disable push relay entirely.

> [!WARNING] Disable Push Relay
> Disabling push relay will prevent **mobile apps** from receiving push notifications, which may impact:
> 
> - The ability for the app to [automatically sync](https://bitwarden.com/help/vault-sync/#automatic-sync/). Users will still be able to [manually sync](https://bitwarden.com/help/vault-sync/#manual-sync/).
> - The ability for the app to automatically log users out, which may be relevant when rotating an encryption key or during offboarding.
> - The ability for the app to automatically register that the user is revoked or removed from an organization, which may cause access to organization items to persist longer than intended.

For each self-hosted server that uses the Bitwarden push relay service, Bitwarden collects a record including a timestamp for the most recent connection to the service and the initiating server's installation ID.

## Disable push relay

To disable push relay for standard server installations:

1. Open `./bwdata/config.yml`.
2. Change the `push_notifications: true` attribute to `false`.
3. Run `./bitwarden.sh rebuild` to apply your changes.

To disable push relay for offline and manual server installations:

1. Open `./bwdata/env/global.override.env`.
2. Add the line `globalSettings__pushRelayBaseUri= `(the variable should be **blank**).
3. Restart Bitwarden to apply the changes.
