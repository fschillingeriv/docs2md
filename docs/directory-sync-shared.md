---
URL: https://bitwarden.com/help/directory-sync-shared/
---

# Directory Connector File Storage

The desktop app and CLI [share a database and configurations](https://bitwarden.com/help/directory-sync-shared/), so **simultaneous** use on a single machine is not recommended. The recommended path is to complete configuration and testing using the [desktop app](https://bitwarden.com/help/directory-sync-desktop/), and subsequently using the [CLI](https://bitwarden.com/help/directory-sync-cli/) to [schedule automatic syncing](https://bitwarden.com/help/schedule-directory-sync/) to your production organization.

> [!NOTE] Desktop and CLI configuration
> We recommend using the desktop app or CLI prior to conditioning the Directory Connector configuration file, as **it is not possible to setup the entirety of Directory Connector from this file**. Authentication values, like keys or secrets, must be set from either the [desktop app](https://bitwarden.com/help/directory-sync-desktop/) or [CLI](https://bitwarden.com/help/directory-sync-cli/).

## Config file

The Directory Connector configuration file (`data.json`) contains objects you may directly edit in order to:

- Set the connection to your directory
- Configure sync options

It is not possible to setup the entirety of Directory Connector from `data.json`. Authentication values, like keys or secrets, must be set from either the [desktop app](https://bitwarden.com/help/directory-sync-desktop/) or [CLI](https://bitwarden.com/help/directory-sync-cli/).

⬇️ [Download a sample configuration file](https://bitwarden.com/assets/1Bkzdf50jZRPq0MRJ85FPi/68b92adf2f5399dc50df1b897a0c0729/data.json)

> [!NOTE] Modifying BWDC data.json
> Avoid opening or modifying `data.json` while the Directory Connector desktop app or CLI executable is running.

### Location

The location of `data.json` depends on which platform is in use:

- Windows : `%AppData%\Bitwarden Directory Connector`

 - Portable: `.\bitwarden-connector-appdata`
- macOS: `~/Library/Application Support/Bitwarden Directory Connector`
- Linux: `~/.config/Bitwarden Directory Connector`

> [!NOTE]
> Using the Directory Connector [CLI](https://bitwarden.com/help/directory-sync-cli/), run the `data-file` command to discover the absolute path to the `data.json`.

## Secret storage

By default, the Directory Connector [desktop app](https://bitwarden.com/help/directory-sync-desktop/) and [CLI](https://bitwarden.com/help/directory-sync-desktop/) both use a secure method for persisting sensitive data (such as your directory account password, API keys, and so on).

On Linux systems this requires [GNOME Keyring](https://wiki.archlinux.org/index.php/GNOME/Keyring) and [X11](https://en.wikipedia.org/wiki/X_Window_System), which are usually reserved for desktop environments. If you are using a headless Linux environment you may encounter errors such as:

```
Cannot autolaunch D-Bus without X11 $DISPLAY
```

### Secret storage in headless environments

If a secure storage environment is not available, you can configure the Directory Connector CLI to use plaintext storage of secrets. To do so, set the following environment variable to override secure storage, for example by running `sudo -H gedit /etc/environment`:

```
BITWARDENCLI_CONNECTOR_PLAINTEXT_SECRETS=true
```

With plaintext storage enabled, you can then configure all settings directly, in plaintext, from the `data.json` configuration file.

> [!NOTE] Plaintext storage not compatible with BWDC desktop app
> Plaintext storage of secrets is not compatible with the Directory Connector desktop app. You should only use the Directory Connector CLI with plaintext storage of secrets.
