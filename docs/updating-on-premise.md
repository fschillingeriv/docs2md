---
URL: https://bitwarden.com/help/updating-on-premise/
---

# Update a Server

> [!TIP] Self-hosted Server Release Lag
> Self-hosted server releases lag several days behind cloud server releases. Please note that the [System Administrator Portal](https://bitwarden.com/help/system-administrator-portal/) may report an available update **before** it is available for self-hosted servers.
> 
> Additionally, please review Bitwarden [software release support](https://bitwarden.com/help/bitwarden-software-release-support/#release-support-at-bitwarden/) documentation.

**It is critically important to keep your self-hosted Bitwarden instance up to date.** Updates may include fixes that are important for the security of your Bitwarden instance, including patches to any vulnerabilities. Data stored in your Bitwarden vault, including passwords, should be considered critical data and therefore protected with up-to-date software.

 Additionally, newer versions of client applications may not support older versions of your self-hosted instance.

You can subscribe to email notifications for self-hosted server releases by navigating to [this repository](https://github.com/bitwarden/self-host) and selecting **Watch** → **Custom** → **Releases**.

> [!NOTE]
> We highly recommend backing up your data before updating your self-hosted instance. For more information, see [Backup your Hosted Data](https://bitwarden.com/help/backup-on-premise/).

If you're running a standard installation, update your Bitwarden instance using the same Bash (Linux or macOS) or PowerShell (Windows) script (`bitwarden.sh`) used to install Bitwarden. Run the following sequence of commands:

🐧 🍎 Bash

```
./bitwarden.sh updateself
./bitwarden.sh update
```

🪟 PowerShell

```
.\bitwarden.ps1 -updateself
.\bitwarden.ps1 -update
```

### Update offline deployment

If you're running a [manually-installed](https://bitwarden.com/help/install-on-premise-manual/#update-your-server/) or an [offline Linux](https://bitwarden.com/help/install-and-deploy-offline/#update-your-server/) or [offline Windows](https://bitwarden.com/help/install-and-deploy-offline-windows/#update-your-server/) installation, follow the procedures in the linked articles.

Your Bitwarden installation should now be fully up to date and running.
