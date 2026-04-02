---
URL: https://bitwarden.com/help/using-bitwarden-offline/
---

# Using Bitwarden Offline

Any [unlocked](https://bitwarden.com/help/vault-timeout/#session-timeout-action/) Bitwarden app can be used offline in **read-only mode**, for example when using airplane mode on a mobile device or when not connected to your self-hosted server.

Most functions of Bitwarden are accessible in offline mode, however you won't be able to make edits to or add vault items, attachments, or sends or import new vault items.

## Installing Bitwarden offline

Customers occasionally wish to install Bitwarden on offline machines, for example in air-gapped environments. To install the Bitwarden desktop app on an offline machine:

> [!TIP] Portable App for Offline Install
> **For Windows only**, you can download and transfer `Bitwarden-Portable-x.xx.x.exe` to an offline machine as an alternative to the following procedure. The portable app does not require installation.

1. On a machine with internet access, navigate to [https://github.com/bitwarden/clients/releases](https://github.com/bitwarden/clients/releases) and download the latest release installer (for example, `Bitwarden-Installer-1.32.1.exe`) and the correlated release asset bundle (for example, `Bitwarden-1.32.1-x64.nsis.7z`).
2. Transfer the downloaded files to the offline machine and **place them in the same directory**.
3. Run the installer (for example, `Bitwarden-Installer-1.32.1.exe`). If the required asset bundle is in the same directory, Bitwarden will be installed without requiring internet access.

Please note that following the offline installation procedures will mean that your desktop app **will not automatically update** when new features or patches are released.
