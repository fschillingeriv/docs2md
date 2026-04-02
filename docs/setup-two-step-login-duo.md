---
URL: https://bitwarden.com/help/setup-two-step-login-duo/
---

# Duo Two-Step Login

Two-step login using Duo is unique among [available two-step login methods](https://bitwarden.com/help/setup-two-step-login/) in that it can be enabled for a personal account with premium membership or enabled for an entire organization by [teams and enterprise organizations](https://bitwarden.com/help/about-organizations/).

## Setup Duo

This article covers Duo setup for **Personal users**, **Organization users**, and **Organization admins**:

### Personal user

### Retrieve Duo keys

You will need a Duo account in order to obtain some information required by Bitwarden to complete setup. [Sign up for free](https://signup.duo.com/), or log in to your existing [Duo Admin Panel](https://admin.duosecurity.com/login). To configure Duo:

1. In the left menu, navigate to **Applications**.
2. Select the **Add an Application** button.
3. Find or search for **Bitwarden** in the applications catalog, being sure to choose the one tagged **2FA**and **Partner**, and select the **Add** button. You will be redirected to a Bitwarden application page:

![Duo Bitwarden Application](https://bitwarden.com/assets/35CpllTrg8k1IIQrL4Jf5m/d62f04d003eb8e6f6d7ef1da2a9f7e9b/2024-03-01_11-42-32.png)
4. Take note of the **Client ID**, **Client secret**, and **API Hostname**. You will need to reference these values when you setup Duo within Bitwarden.
5. Toggle **User access** to **Enable for all users**.

### Setup Duo in Bitwarden

> [!WARNING] Losing 2FA Device (Generic)
> **Losing access to your two-step login device can permanently lock you out of your vault** unless you write down and keep your two-step login recovery code in a safe place or have an alternate two-step login method enabled and available.
> 
> [Get your recovery code](https://bitwarden.com/help/two-step-recovery-code/) from the **Two-step login** screen immediately after enabling any method. Additionally, users may create a Bitwarden [export](https://bitwarden.com/help/export-your-data/) to backup vault data.

To enable two-step login using Duo as a personal user:

1. Log in to the Bitwarden web app.
2. Select **Settings** → **Security**→**Two-step login** from the navigation:|

![Two-step login settings](https://bitwarden.com/assets/2IjxRoQwl1powHRhah6Bq/39067a5fe6c53732054f323e4afb431b/Screenshot_2025-12-31_at_1.52.00â__PM.png)
*Two-step login settings*
3. Locate the **Duo** option and select **Manage**. You will be prompted to enter your master password to continue.
4. Enter the following values retrieved from the Duo Admin Panel (see the above section in this tab):

 - **Client ID**into the **Integration Key**field
 - **Client Secret**into the**Secret Key**field
 - Enter the **API Hostname**
5. Select the **Enable** button.

A green `Enabled` message should appear to indicate that Duo has been enabled for your vault. You can double-check by selecting the **Close** button and seeing that the **Duo** option has a green checkmark ( ✓ ) on it.

We recommend keeping your active web vault tab open before proceeding to test two-step login in case something was misconfigured. Once you have confirmed it's working, logout of all your Bitwarden apps to require two-step login for each. You will eventually be logged out automatically.

> [!NOTE] Self-hosted Duo Setup
> Self-hosted instances operating on air-gapped networks may require additional setup in order to maintain server communication with Duo.

### Register a device

Once Duo is setup, open the web vault. If Duo is your [highest-priority enabled method](https://bitwarden.com/help/setup-two-step-login/#using-multiple-methods/), you will be prompted to **Launch Duo**the next time you log on:

![Launch Duo](https://bitwarden.com/assets/44SjeVrDTuQPz52cBxGhCX/d8cf66018741b808349e6afbd7f0769b/2025-04-08_14-15-16.png)

You will be asked to register a two-step login device, follow the on-screen prompts to configure a secondary device to use Duo (for example, what type of device to register and whether to send an SMS* *or push notification).

![Duo 2FA setup](https://bitwarden.com/assets/5Mm1G5tjfPmzs5V8obaxl1/8e2a79bbf29d5017147953bddb9e10a2/2025-04-08_14-15-43.png)

If you have not already downloaded the Duo mobile app, we recommend that you do so:

- [Download for iOS](https://itunes.apple.com/us/app/duo-mobile/id422663827?mt=8)
- [Download for Android](https://play.google.com/store/apps/details?id=com.duosecurity.duomobile)

### Organization user

### Register a device

Once your organization admin has setup Duo, you will be prompted to **Launch Duo**the next time you log on:

![Launch Duo](https://bitwarden.com/assets/44SjeVrDTuQPz52cBxGhCX/d8cf66018741b808349e6afbd7f0769b/2025-04-08_14-15-16.png)

You will be asked to register a two-step login device, follow the on-screen prompts to configure a secondary device to use Duo (for example, what type of device to register and whether to send an SMS* *or push notification).

![Duo 2FA setup](https://bitwarden.com/assets/5Mm1G5tjfPmzs5V8obaxl1/8e2a79bbf29d5017147953bddb9e10a2/2025-04-08_14-15-43.png)

> [!TIP] Duo Incognito Mode
> If you don't get asked by Duo to register a device, try logging in using an incognito or private browsing window.

If you haven't already downloaded the Duo mobile app, we recommend that you do so:

- [Download for iOS](https://itunes.apple.com/us/app/duo-mobile/id422663827?mt=8)
- [Download for Android](https://play.google.com/store/apps/details?id=com.duosecurity.duomobile)

### Organization admin

Enabling Duo for an organization will prompt all enrolled members to register a device for Duo two-step login the next time they log in to the web vault.

> [!NOTE] Duo account email
> Bitwarden will only recognize users with email address usernames. Duo users that do not have an email address as their primary username will require one. Please reference [Duo Username Aliases Configuration Guide](https://help.duo.com/s/article/aliases-guide?language=en_US) for additional information and instructions.

### Retrieve Duo keys

You will need a Duo account in order to obtain some information required by Bitwarden to complete setup. [Sign up for free](https://signup.duo.com/), or log in to your existing [Duo Admin Panel](https://admin.duosecurity.com/login). To configure Duo:

1. In the left menu, navigate to **Applications**.
2. Select the **Add an Application** button.
3. Find or search for **Bitwarden** in the applications catalog, being sure to choose the one tagged **2FA**and **Partner**, and select the **Add** button. You will be redirected to a Bitwarden application page:

![Duo Bitwarden Application](https://bitwarden.com/assets/35CpllTrg8k1IIQrL4Jf5m/d62f04d003eb8e6f6d7ef1da2a9f7e9b/2024-03-01_11-42-32.png)
4. Take note of the **Client ID**, **Client secret**, and **API Hostname**. You will need to reference these values when you setup Duo within Bitwarden.
5. Toggle **User access** to **Enable for all users**.

### Setup Duo in Bitwarden

> [!WARNING] Org Duo
> Once you initially configure and setup Duo, it is **critically important** that you disable it for the organization before making any further application configuration changes from the Duo Admin Panel. To make configuration changes; disable Duo in Bitwarden, make the required changes in the Duo Admin Panel, and re-enable Duo in Bitwarden.
> 
> This is because Duo for organizations does not currently support [recovery codes](https://bitwarden.com/help/two-step-recovery-code/). Instead, you will need to rely on the Duo Admin Panel to bypass two-step login for members who lose access to Duo. Altering the application configuration from the Duo Admin Panel while Duo is active risks losing the ability to bypass two-step login for you or your organization's members.

You must be an [organization owner](https://bitwarden.com/help/user-types-access-control/) to setup Duo for your organization. To enable two-step login using Duo for your organization:

1. Log in to the Bitwarden web app.
2. Open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
3. Select **Settings**→**Two-step login** from the navigation:

![Manage Duo for organizations](https://bitwarden.com/assets/4RhAdJgvxpRiLtv0P0XrWT/d8a4e561a5293febfbdefe121dd656ab/2024-12-02_11-21-42.png)
4. Locate the **Duo (Organization)** option and select the **Manage** button.
5. You will be prompted to enter your master password to continue.
6. Enter the following values retrieved from the Duo Admin Panel: 

 - **Client ID**into the **Integration Key**field
 - **Client Secret**into the**Secret Key**field
 - Enter the **API Hostname**
7. Select the **Enable** button.

A green `Enabled` message should appear to indicate that Duo has been enabled for your vault. You can double-check by selecting the **Close** button and seeing that the **Duo** option has a green checkmark ( ✓ ) on it.

> [!NOTE] Self-hosted Duo Setup
> Self-hosted instances operating on air-gapped networks may require additional setup in order to maintain server communication with Duo.

### Register a device

Once Duo is setup, you and your organization members will be prompted to **Launch Duo**the next time you log on:

![Launch Duo](https://bitwarden.com/assets/44SjeVrDTuQPz52cBxGhCX/d8cf66018741b808349e6afbd7f0769b/2025-04-08_14-15-16.png)

You will be asked to register a two-step login device, follow the on-screen prompts to configure a secondary device to use Duo (for example, what type of device to register and whether to send an SMS* *or push notification).

![Duo 2FA setup](https://bitwarden.com/assets/5Mm1G5tjfPmzs5V8obaxl1/8e2a79bbf29d5017147953bddb9e10a2/2025-04-08_14-15-43.png)

If you haven't already downloaded the Duo mobile app, we recommend that you do so:

- [Download for iOS](https://itunes.apple.com/us/app/duo-mobile/id422663827?mt=8)
- [Download for Android](https://play.google.com/store/apps/details?id=com.duosecurity.duomobile)

## Use Duo

The following assumes that **Duo** is your [highest-priority enabled method](https://bitwarden.com/help/setup-two-step-login/#using-multiple-methods/). For organization members, **org-wide Duo is always the highest-priority method**. To access your vault using Duo two-step login:

1. Login to your Bitwarden vault on any app and enter your email address and master password. A prompt will ask you to **Launch Duo**. Once launched, a Duo screen will appear to begin your two-step login verification.
2. Depending on how you have configured Duo, complete the authentication request by:

 - Approving the **Duo Push** request from your registered device.
 - Finding the six-digit verification code in your **Duo Mobile** app or **SMS** messages, and enter the code on the vault login screen.

> [!TIP] Remember Me for 2FA
> Check the **Remember Me** box for Bitwarden to recognize your device for 30 days. Selecting this option means you won't be required to complete your two-step login step during that time.

You will not be required to complete your secondary two-step login step to **unlock** your vault once logged in. For help configuring log out vs. lock behavior, see [vault timeout options](https://bitwarden.com/help/vault-timeout/).
