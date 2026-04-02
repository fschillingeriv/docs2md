---
URL: https://bitwarden.com/help/deploy-desktop-apps-with-intune/
---

# Deploy Desktop Apps with Intune

When operating Bitwarden in a business setting, administrators may want to automate deployment of Bitwarden desktop apps to users with **Microsoft Intune**. This article will cover how to use Intune to deploy Bitwarden Password Manager desktop apps to your endpoints.

> [!NOTE] Configure server for managed devices
> If your organization uses a self-hosted or EU Bitwarden server, configure managed devices to connect to the correct server URL. For more information, see [Connect managed devices](https://bitwarden.com/help/configure-clients-selfhost/).

Bitwarden desktop apps can be deployed to endpoints using either a Win32 application (*recommended*) or via the Microsoft App Store:

### Win32 App

To deploy the Win32 version of Bitwarden Password Manager, complete the following steps:

1. Download the latest Bitwarden Windows desktop app installer from [bitwarden.com/download/](https://bitwarden.com/download/).
2. Use the [Microsoft Win32 Content Prep Tool](https://github.com/Microsoft/Microsoft-Win32-Content-Prep-Tool) to convert the installer into the required `.intunewin` format ([learn more](https://learn.microsoft.com/en-us/mem/intune/apps/apps-win32-prepare)).
3. Open the Intune Portal, navigate to **Apps** → **Windows** and select + **Add**.
4. In the Select app type window, use the **App type** dropdown to select **Windows app (Win32)**.
5. Hit **Select**.
6. On the App information screen, select **Select app package file.**
7. On the App package file window, use the file explorer to select your converted `.intunewin` installer and select **OK**.
8. Take note of the **Name** of your app before proceeding, particularly the version number in the executable.
9. Select **Next**.
10. On the Program screen:

 - Specify the following **Install command**: `Bitwarden-installer-{version}.exe /allusers /S`. Make sure to replace `{version}` with the correct version of the application, for example `2024.8.0`, as seen in the App name (Step 8).
 - Specify the following **Uninstall command**: `C:\Program Files\Bitwarden\Uninstall Bitwarden.exe /allusers /S`.
 - Choose an **Install behavior**, more information can be found by hovering over the ℹ️ icon on that page.
11. Select **Next**.
12. On the Requirements screen:

 - Specify an **Operating system architecture** of **64-bit / 32-bit.**
 - Specify a **Minimum operating system**of **Windows 10 1607**.
13. Select **Next**.
14. On the Detection rules screen:

 - From the **Rules** dropdown, select **Manually configure detection rules**.
 - Select **Add**.
 - From the **Rule type**dropdown, select **File**.
 - Specify a **Path** of `C:\Program Files\Bitwarden`.
 - Specify a **File or folder** of `Bitwarden.exe`.
 - From the **Detection method** dropdown, select **File or folder exists**.
 - For **Associated with a 32-bit app on 64-bit clients**, choose **No**.
15. Select **Next**.
16. On the Dependencies screen, select **Next**.
17. On the Assignments screen, add and groups or users to the configuration and select **Next**.
18. On the **Review + create** screen, select **Create**.

### App Store

> [!TIP] Endpoints must qualify for app store method
> In order for this method to work, endpoint devices must have access to the Microsoft App Store and must support the Intune Management Extension (IME).
> 
> Please note that Bitwarden desktop apps from the Microsoft App Store do not currently support biometric integration with browser extensions ([learn more](https://bitwarden.com/help/biometrics/)).

To deploy the Microsoft App Store version of Bitwarden Password Manager, open the Microsoft Intune portal and complete the following steps:

1. In the Intune Portal, navigate to **Apps** → **Windows** and select + **Add**.
2. In the Select app type window, use the **App type** dropdown to select **Microsoft Store app (new)**.
3. Hit **Select**.
4. On the App information screen, select **Search the Microsoft Store app (new**).
5. Search for Bitwarden and hit **Select** once you've found and highlighted it.
6. Choose an **Install behavior**, more information can be found by hovering over the ℹ️ icon on that page.
7. Select **Next**.
8. On the Assignments screen, add and groups or users to the configuration and select **Next**.
9. On the **Review + create** screen, select **Create**.
