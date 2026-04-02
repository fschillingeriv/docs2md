---
URL: https://bitwarden.com/help/deactivate-browser-password-managers/
---

# Deactivate Browser Password Managers Using Device Management

This article will direct you on how to disable various web browser's built-in password managers using group policy. These steps will help prevent corporate logins from being saved and synchronized to personal accounts. You may also consider deploying the [Bitwarden browser extension to all browsers](https://bitwarden.com/help/browserext-deploy/) as part of this same policy.

## Disable with Windows GPO

### Disable Edge

1. Open Group Policy Management Editor on your managing Windows server.
2. [Download the appropriate Edge Policy Template](https://www.microsoft.com/en-us/edge/business/download?form=MA13FJ).
3. In Group Policy Editor, create a new GPO for Edge and provide an appropriate name.
4. Choose your desired scope.
5. Right-click the new Group Policy **Object** → **Edit**.
6. On the Group Policy Management Editor, go to **User Configuration** → **Policies** → **Administrative Templates**→**Microsoft Edge**.
7. Set the following policies:

 - Open "Password manager and protection," disable the policy **Enable saving passwords to the password manager**.
 - Disable the policy **Enable AutoFill for addresses**.
 - Disable the policy **Enable AutoFill for payment instruments**.
 - Optionally, you can enable the policy **Disable synchronization of data using Microsoft sync services**.

Once complete, the GPO **settings** should show the following:

![Edge Settings](https://bitwarden.com/assets/7JYNg4j0ETWUYqxvC1aA35/b2330512b7ccfd0c2371d14349f6f91d/image.png)
8. Ensure the GPO link is enabled.

### Disable Chrome

1. Open Group Policy Management Editor on your managing Windows server.
2. [Download the Google Chrome Administrative Templates.](https://support.google.com/chrome/a/answer/187202?hl)
3. In the `ADMX` file, copy the following:
`policy_templates\windows\admx\chrome.admx 
`and`
policy_templates\windows\admx\google.admx

`**TO** `C:\Windows\PolicyDefinitions`
4. In the `ADML` file, copy the following:
`policy_templates\windows\admx\en-us\chrome.adml 
`and`
policy_templates\windows\admx\en-us\google.adml
`
**TO** `C:\Windows \PolicyDefinitions\en-us`
5. In Group Policy Editor, create a new GPO for Chrome and provide an appropriate name.
6. Choose your desired scope.
7. Right-click the **Group Policy Object** → **Edit**.
8. Go to **User Configuration** → **Policies** → **Administrative Templates** → **Google** → **Google Chrome**.
9. Edit the following settings:

 - Under "Password Manager," disable the policy **Enable saving passwords to the password manager**.
 - Disable the policy **Enable AutoFill for Addresses**.
 - Disable the policy**Enable AutoFill for credit cards**.
10. Once complete, the GPO **settings** should show the following:

![Chrome Settings](https://bitwarden.com/assets/4g4UFkO53OhzFhZlnSPoKY/000e4a638d423783c6e1c94c10b13395/chrome_gpo.png)
11. Ensure the GPO link is enabled.

### Disable Firefox

1. Open Group Policy Editor on your managing Windows server.
2. [Download the latest Firefox Policy Templates .zip file.](https://github.com/mozilla/policy-templates/releases)
3. Copy the **ADMX** file:
**FROM** the downloaded folder `policy_templates_v1.##\windows\firefox.admx & mozilla.admx`
**TO** `C:\Windows\PolicyDefinitions`
4. Copy the **ADML** file
**FROM** `policy_templates\windows\en-us\firefox.adml & mozilla.adml`
**TO** `C:\Windows \PolicyDefinitions\en-us`
5. In Group Policy Editor, create a new GPO for FireFox and provide an appropriate name.
6. Choose your desired scope.
7. Right-click the **new group policy** → **Edit**.
8. Open **User Configuration** → **Policies** → **Administrative Templates** → **Mozilla**→ **Firefox**.
9. Locate and edit the following policies:

 - Enable the policy **Disable Firefox Accounts**.
 - Disable the policy **Offer to save logins**.
 - Disable the policy **Offer to save logins (default)**.
 - Disable the policy **Password Manager**.
10. Once complete, the GPO **settings** should show the following:

![Firefox Settings](https://bitwarden.com/assets/75Do1uQgOThyyIfdXU3ti7/5ab03c79118217b0fdd6485ad8c71527/image.png)
11. Ensure the GPO link is enabled.

### How to check if it worked?

Check that the previous steps worked correctly for your setup:

### Edge

1. On a user's computer, Open the command line, and run:
 `gpupdate /force`.
2. Open Edge, then click the three dots for settings **...** → **Settings** → **Passwords**.
3. Ensure "Offer to save passwords" is turned off and managed by the organization.

> [!NOTE] Disable Edge GPO
> **Sign-in automatically** is still checked because there is no policy setting to turn this off.
> 
> Any logins previously saved in Edge will not be removed and will continue to be displayed to the user, despite autofill being disabled. Be sure to instruct the user to [import any saved logins](https://bitwarden.com/help/import-from-chrome/) into Bitwarden before deleting them from Edge.

### Chrome

1. On a user's computer, Open the command line, and run:
 `gpupdate /force`.
2. Open Chrome and click the **profile** **icon** on the top right. See that the user is not signed in.
3. Open Chrome, then click the three dots **...** → **Settings** → **Passwords**. See that **Offer to save passwords** is unchecked and managed by the organization.

### Firefox

1. On a user's computer, Open the command line, and run:
 `gpupdate /force`.
2. Open Firefox and select **Logins and Passwords** from the menu bar.
3. Ensure that a "Blocked Page" message is displayed.

## Disable on Linux

### Chrome

To disable the Chrome Password Manager via group policy:

1. Download the [Google Chrome .deb or .rpm](https://www.google.com/chrome/?platform=linux) for Linux.
2. Download the [Chrome Enterprise Bundle](https://chromeenterprise.google/browser/download/#windows-tab).
3. Unzip the Enterprise Bundle (`GoogleChromeEnterpriseBundle64.zip` or `GoogleChromeEnterpriseBundle32.zip`) and open the `/Configuration` folder.
4. Make a copy of the `master_preferences.json` (in Chrome 91+, `initial_preferences.json`) and rename it `managed_preferences.json`.
5. To [disable](https://chromeenterprise.google/policies/#PasswordManagerEnabled) Chrome's built-in password manager, add the following to `managed_preferences.json` inside of `"policies": { }`:

```plain text
{
 "PasswordManagerEnabled": false
}
```
6. Create the following directories if they do not already exist:

```plain text
mkdir /etc/opt/chrome/policies
mkdir /etc/opt/chrome/policies/managed
```
7. Move `managed_preferences.json` into `/etc/opt/chrome/policies/managed`.
8. As you will need to deploy these files to users' machines, we recommend making sure only admins can write files in the `/managed` directory.

```plain text
chmod -R 755 /etc/opt/chrome/policies
```
9. Additionally, we recommend admins should add the following to files to prevent modifications to the files themselves:

```plain text
chmod 644 /etc/opt/chrome/policies/managed/managed_preferences.json
```
10. Using your preferred software distribution or MDM tool, deploy the following to users' machines:

 1. Google Chrome Browser
 2. `/etc/opt/chrome/policies/managed/managed_preferences.json`

> [!NOTE] Refer to Google's guide to chome for linux
> For more help, refer to Google's [Chrome Browser Quick Start for Linux](https://support.google.com/chrome/a/answer/9025926?hl=en&ref_topic=9025817) guide.

### Firefox

To disable the Firefox Manager via group policy:

1. Download [Firefox for Linux](https://www.mozilla.org/en-US/firefox/linux/).
2. Open a terminal and navigate to the directory your download has been saved to. For example:` 
cd ~/Downloads `
3. `Extract to contents of the downloaded file:
`

```plain text
tar xjf firefox-*.tar.bz2
```

The following commands must be executed as root, or preceded by `sudo`.
4. Move the uncompressed Firefox folder to `/opt`:

```plain text
mv firefox /opt
```
5. Create a symlink to the Firefox executable:

```plain text
ln -s /opt/firefox /usr/local/bin/firefox
```
6. Download a copy of the desktop file:

```plain text
wget https://raw.githubusercontent.com/mozilla/sumo-kb/main/install-firefox-linux/firefox.desktop -P /usr/local/share/applications
```
7. To disable Firefox's built-in password manager, add the following to `policies.json` inside of `"policies": {}`:

```plain text
{
 "PasswordManagerEnabled": false
}
```
8. Create the following directory if it does not already exist:

```plain text
mkdir /opt/firefox/distribution
```
9. Modify the directory with the following:

```plain text
chmod 755 /opt/firefox/distribution
```
10. Additionally, we recommend admins should add the following to files to prevent modifications to the files themselves:

```plain text
chmod 644 /opt/firefox/distribution/policies.json
```
11. Using your preferred software distribution or MDM tool, deploy the following to users' machines:
12. Firefox Browser
13. `/distribution/policies.json`

> [!NOTE] disable firefox group policy
> For more help, refer to Firefox's [policies.json Overview](https://support.mozilla.org/en-US/kb/customizing-firefox-macos-using-configuration-prof) or [Policies README](https://github.com/mozilla/policy-templates/blob/master/README.md) on Github.

## Disable on MacOS

### Chrome

1. Download the [Google Chrome .dmg or .pkg](https://chromeenterprise.google/browser/download/#mac-tab) for macOS.
2. Download the [Chrome Enterprise Bundle](https://support.google.com/chrome/a/answer/7650032?hl=en&sjid=15647115866896992845-NA).
3. Unzip the Enterprise Bundle (`GoogleChromeEnterpriseBundle64.zip` or `GoogleChromeEnterpriseBundle32.zip`).
4. Open the `/Configuration/com.Google.Chrome.plist` file with any text editor.
5. To [disable](https://chromeenterprise.google/policies/#PasswordManagerEnabled) Chrome's built-in password manager, add the following to `com.Google.Chrome.plist`:

```plain text
<key>PasswordManagerEnabled</key>
<false />
```
6. Convert the `com.Google.Chrome.plist` file to a configuration profile using a conversion tool of your choice.
7. Deploy the Chrome `.dmg` or `.pkg` and the configuration profile using your software distribution or MDM tool to all managed computers.

> [!NOTE] disable google chrome mac
> For more help, refer to Google's [Chrome Browser Quick Start for Mac](https://support.google.com/chrome/a/answer/9020580?hl=en&ref_topic=7650028) guide.

For additional information, see [Chrome's documentation](https://support.google.com/chrome/a/answer/7550274?hl=en) for setting up Chrome browser on Mac.

### Firefox

1. Download and install [Firefox for Enterprise](https://www.mozilla.org/en-US/firefox/enterprise/#download) for macOS.
2. Create a `distribution` directory in `Firefox.app/Contents/Resources/`.
3. In the created `/distribution` directory, create a new file `org.mozilla.firefox.plist`.

> [!NOTE]
> Use the [Firefox .plist template](https://github.com/mozilla/policy-templates/blob/master/mac/org.mozilla.firefox.plist) and [Policy README](https://github.com/mozilla/policy-templates/blob/master/README.md) for reference.
4. To [disable](https://github.com/mozilla/policy-templates/blob/master/README.md#passwordmanagerenabled) Firefox's built-in password manager, add the following to `org.mozilla.firefox.plist`:

```plain text
<dict>
 <key>PasswordManagerEnabled</key>
 <false/>
</dict>
```
5. Convert the `org.mozilla.firefox.plist` file to a configuration profile using a conversion tool of your choice.
6. Deploy the Firefox `.dmg` and the configuration profile using your software distribution or MDM tool to all managed computers.

For additional information, see [Firefox's documentation ](https://support.mozilla.org/en-US/kb/customizing-firefox-macos-using-configuration-prof)for MacOS configuration profiles.

### Edge

1. Download the [Microsoft Edge for macOS .pkg](https://www.microsoft.com/en-us/edge) file.
2. In Terminal, use the following command to create a `.plist` file for Microsoft Edge:

```plain text
/usr/bin/defaults write ~/Desktop/com.microsoft.Edge.plist RestoreOnStartup -int 1
```
3. Use the following command to convert the `.plist` from binary to plain text:

```plain text
/usr/bin/plutil -convert xml1 ~/Desktop/com.microsoft.Edge.plist
```
4. To [disable](https://docs.microsoft.com/en-us/deployedge/microsoft-edge-policies#passwordmanagerenabled) Edge's built-in password manager, add the following to `com.microsoft.Edge.plist`:

```plain text
<key>PasswordManagerEnabled</key>
<false/>
```
5. Deploy the Edge `.pkg` and the configuration profile using your software distribution or MDM tool to all managed computers.

> [!NOTE]
> **For Jamf-specific** help, refer to Microsoft's documentation on [Configuring Microsoft Edge policy settings on macOS with Jamf](https://docs.microsoft.com/en-us/deployedge/configure-microsoft-edge-on-mac-jamf).

For additional information, see [Edge's documentation](https://learn.microsoft.com/en-us/deployedge/configure-microsoft-edge-on-mac#configure-microsoft-edge-policies-on-macos) for configuration profiles.
