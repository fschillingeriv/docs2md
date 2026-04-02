---
URL: https://bitwarden.com/help/vault-sync/
---

# Sync your Vault

Adding, editing, or deleting [vault items](https://bitwarden.com/help/managing-items/) from any Bitwarden app will automatically push changes to your Bitwarden server, whether Cloud-hosted or self-hosted.

In order to pull those changes down to another Bitwarden app, your vault will need to sync.

## Automatic sync

Items owned by you in the [web vault](https://bitwarden.com/help/getting-started-webvault/) will always remain in-sync. Items owned by an [organization](https://bitwarden.com/help/about-organizations/) will sync across users and client applications every 30 minutes.

Other Bitwarden apps (browser extensions, mobile apps, desktop apps, and CLI) will sync automatically on login, and regularly when unlocked. You can also [manually sync](https://bitwarden.com/help/vault-sync/#manual-sync/) your vault to pull changes immediately.

> [!NOTE] Logging In to Sync
> When you install Bitwarden on a new device, logging in to your account will automatically pull your most up-to-date vault data.

## Manual sync

To manually sync your vault from a Bitwarden app:

### Browser extensions

In the ⚙️ **Settings** tab, select **Vault options** and use the **Sync vault now** button.

### Mobile

Open the ⚙️ **Settings** tab, tap the **Other** option, and tap **Sync now**.

Toggle the **Allow sync on refresh** option to allow your vault to be synced using a pulldown gesture on the 🔒 **Vaults** tab.

### Desktop

Select **File** → **Sync vault** from the menu bar.

> [!TIP] Sync Account Switching
> Only the [currently active account](https://bitwarden.com/help/account-switching/) will be synced, however the account can be synced even when your vault is locked.

### CLI

Use the `sync` command to manually sync your Vault:

```
bw sync
```

For more information, please refer to the Bitwarden [CLI documentation](https://bitwarden.com/help/cli/).

## Troubleshooting

If your vault isn't syncing properly, investigate the following:

#### Mismatched timestamp

Verify that your device's time is correct, such as your local time zone. Bitwarden uses TLS/SSL, which will fail to connect a Bitwarden app to the server if timestamps are mismatched.

#### VPN or ad blocker interference

In some cases, VPN or ad blocker browser extensions may interfere with the connection between Bitwarden app and server. This issue is typically observed with browser extensions. Try turning off your VPN or ad blocker browser extension and then[ manually sync your vault](https://bitwarden.com/help/vault-sync/#manual-sync/).
