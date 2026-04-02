---
URL: https://bitwarden.com/help/versioning/
---

# Server & Client Versioning

Currently Bitwarden clients and server use a `yyyy.mm.r` convention, indicating, for example, that `2022.5.0` is the base release (`.0`) of May (`.5.`) 2022 (`2022.`). If subsequent hotfixes are released, for example, they would be `2022.5.1`, `2022.5.2`, and so on.

Initial monthly releases (those ending in `.0`) are shared across all clients and server, but clients and server may deviate as some get hotfixes (`.1`s, `.2`s, and so on) while others don't.

This hasn't always been the case, though. Prior to May 2022, clients and server each had different versioning systems. If you're using a client or server with a version `1.xx.x` or `2.xx.x`, you're using an old version.

> [!NOTE] Deprecating Versions
> When Bitwarden drops support of a version, the entire release and all previous versions will also no longer be supported.

## Self-hosted server version

To find your self-hosted server's version, log in to the [System Administrator Portal](https://bitwarden.com/help/system-administrator-portal/). **Server**and **Web**versions will be listed on the dashboard. If the **Installed**versions don't match the **Latest** versions, [update your server](https://bitwarden.com/help/updating-on-premise/):

![Self-hosted server version](https://bitwarden.com/assets/2CakVlacGDcaICXzgQEBH6/c474a0bcc99fc4f739cd3766387263a7/Screen_Shot_2022-09-30_at_9.25.41_AM.png)

You can also check the `bitwarden.sh`/`bitwarden.ps1` file to see which versions are installed. Running `updateself` will update these if newer versions are available, and running` update` will update Bitwarden containers based on what's listed in the `.sh`/`.ps1` file.

## Client version

To get a client application's version:

### Browser extension

Navigate to the ⚙️ **Settings**tab and select **About** → **About Bitwarden**:

![Browser extension version](https://bitwarden.com/assets/4EkEPm8QGo6KCPTCnn4Pg5/090ff5cd26b2fddeedcbddf9edf49e7a/2024-12-04_10-10-53.png)

### Desktop app

On Windows, select **Help**[arrow-circle-right]**About Bitwarden**. On macOS, select **Bitwarden**[arrow-circle-right]**About Bitwarden:**

![Desktop app version](https://bitwarden.com/assets/6GOZ3TPKmrnBbol1FWMZSm/8a86c4556ec42170f65538c6598c534e/Screen_Shot_2022-09-29_at_2.52.13_PM.png)

### Mobile app

Navigate to the ⚙️ **Settings**tab and select the **About** option: 

![Mobile app version](https://bitwarden.com/assets/3zYXLGYrfsJZuGwlT7Vq3v/9db9b271b977e94468cdf04b8cab70f2/2025-01-22_10-19-54.png)

### CLI

To print the current version to the console run the following command: 

```
bw -v
```
