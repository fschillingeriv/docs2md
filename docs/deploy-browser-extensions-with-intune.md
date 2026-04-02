---
URL: https://bitwarden.com/help/deploy-browser-extensions-with-intune/
---

# Deploy Browser Extensions with Intune

When operating Bitwarden in a business setting, administrators may want to automate deployment of Bitwarden browser extensions to users with **Microsoft Intune**. This article will cover how to use Intune to deploy Bitwarden Password Manager browser extensions to your endpoints.

> [!NOTE] Configure server for managed devices
> If your organization uses a self-hosted or EU Bitwarden server, configure managed devices to connect to the correct server URL. For more information, see [Connect managed devices](https://bitwarden.com/help/configure-clients-selfhost/).

## Get extension ID & update URL

In order to deploy Bitwarden browser extensions using Intune, you'll need an extension ID and update URL. This identifier will be different for each browser:

### Chrome

- Extension ID: `nngceckbapebfimnlniiiahkandclblb`
- Update URL: `https://clients2.google.com/service/update2/crx`

### Edge

- Extension ID: `jbkfoedolllekgbhcbcoahefnbanhhlh`
- Update URL: `https://edge.microsoft.com/extensionwebstorebase/v1/crx`

## Create configuration profile

Next, open the Microsoft Intune portal and complete the following steps:

1. In the Intune Portal, navigate to **Devices** → **Configuration** and select **Create** → **New Policy**.
2. In the Create a profile window:

 - Select a **Platform** (for example, **Windows 10 and later**).
 - From the **Profile type** dropdown, select **Settings catalog**.
3. Select **Create**.
4. On the next screen, give your configuration profile a **Name**and **Description** and select **Next**.
5. On the Configuration settings screen, select **Add settings**.
6. In the Settings picker:

 - For Google Chrome, search for **Configure the list of force-installed apps and extensions**, select the **Google Google Chrome Extensions**category, and toggle that option on.
 - For Microsoft Edge, search for Control which extensions are installed silently, select the **Microsoft Edge\Extensions** category, and toggle that option on.

> [!TIP] Disable built-in with Intune
> From the Settings picker, you can also deactivate the built-in password manager that comes available on many web browsers. Typically, for Chrome or a Chromium browser like Microsoft Edge, this setting will be labelled **Enable saving passwords to the password manager** or something similar.
7. Close the Settings picker.
8. Still on the Configuration settings screen, enable whichever option(s) you chose and enter the retrieved extension ID and update URL in the format `<extension_id>;<update_url>`.
9. Select **Next**.
10. On the Scope tags screen, enter any scope you wish to apply to the configuration and select **Next**.
11. On the Assignments screen, add and groups or users to the configuration and select **Next**.
12. On the **Review + create** screen, select **Create**.
