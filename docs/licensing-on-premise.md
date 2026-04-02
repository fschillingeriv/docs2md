---
URL: https://bitwarden.com/help/licensing-on-premise/
---

# License Organizations or Premium

Self-hosting Bitwarden is free, however some features must be unlocked in your self-hosted instance with a registered license file. A license file can be obtained from the Bitwarden-hosted web app by either an account with a premium individual subscription or by the owner of an organization.

The steps are different when working with an [individual license](https://bitwarden.com/help/licensing-on-premise/#individual-license/) versus an [organization license](https://bitwarden.com/help/licensing-on-premise/#organization-license/).

> [!NOTE] licensing paid features 
> The procedures in this article assume that you have already started a paid subscription to Bitwarden. If you haven't, refer to [About Bitwarden Plans](https://bitwarden.com/help/password-manager-plans/) and [What Plan is Right for Me?](https://bitwarden.com/help/what-plan-is-right-for-me/)

## Individual license

Follow these procedures when working with an individual license for a premium subscription. You'll be working in both the cloud web vault and your self-hosted web vault, and your account email addresses should match.

### Retrieve individual license

After you create an account on your self-hosted server, retrieve your license from the cloud web app:

1. Log in and select **Settings** → **Subscription** from the navigation.
2. Select the **Download license**button:

![Download personal license](https://bitwarden.com/assets/bXoVGOMEI1d8iCVoy5fmI/af545e3c083aeebaf12c751fc38a59ea/2024-12-04_10-02-56.png)

### Apply individual license

Next, log in to your self-hosted Bitwarden server to apply the downloaded license:

1. If you haven't already, verify your email address. You will need to have [configured SMTP-related environment variables](https://bitwarden.com/help/environment-variables/) to do so.
2. Select **Settings** → **Subscription** from the navigation.
3. In the License file section, select the **Browse...** or **Choose file** button button and add the downloaded license file.
4. Select the **Submit** button to apply your premium license.

### Update individual license

If for any reason you need to update your individual license file, for example when it expires:

1. Follow the steps to **Retrieve your license**again.
2. Follow the steps to **Apply your license**again, only this time you will see an **Update license**button rather than a button to browse for a new license.

## Organization license

Follow these procedures when working with an organization license for a Families or Enterprise organization. You must be an [organization owner](https://bitwarden.com/help/user-types-access-control/) to retrieve, apply, and update a license.

### Retrieve organization license

Before starting an organization on your self-hosted server, retrieve your organization license from the cloud web app.

1. In the Bitwarden web app, open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
2. Navigate to **Billing** → **Subscription**.
3. Scroll down and select the **Download license** button.
4. When prompted, enter the installation ID that was used to install your self-hosted server and select **Submit**. If you don't know the installation ID off-hand, you can retrieve it from `./bwdata/env/global.override.env`.

> [!NOTE] Installation ID & Region
> Make sure that the installation ID you retrieved from [bitwarden.com/host](https://bitwarden.com/host/) uses the same [data region](https://bitwarden.com/help/server-geographies/) as where your organization exists.

### Apply organization license

Applying your license in a self-hosted server is the means by which you'll create a self-hosted organization. From your self-hosted web vault:

1. Start a new organization by selecting the + **Add organization** button.
2. Select the **Browse...** or **Choose file** button, add the downloaded license file, and select **Submit**.

> [!NOTE] organization license error
> If you receive a `version not supported` error message, update your server and try uploading your license file again. To update your server, make a backup of the `bwdata` directory and follow [these instructions](https://bitwarden.com/help/updating-on-premise/).

### Update organization license

Organizations will need to update the license file used by their self-hosted server in several different scenarios, for example:

- To **add user seats** to a self-hosted organization. Self-hosted organizations' seat count is dictated by the license, so to add seats they must first be added to the associated cloud organization and then the license used by your self-hosted organization must be updated.
- To continue operation of the self-hosted organization **w****hen the license renews**. You have 60 days, from the date of renewal, to update the license file to you self-hosted server before your self-hosted [organization is disabled](https://bitwarden.com/help/organization-renewal/).

There are two methods for updating a self-hosted organization's license, however **Families organizations may only update manually**:

### Automatic sync

Automatic sync:

- Eliminates the need for organization admins to manually re-upload licenses. Once setup, admins will only need to trigger a sync from the **Organization** → **Billing** when an update to the license used by the self-hosted organization is required.
- Makes [Families sponsorships](https://bitwarden.com/help/families-for-enterprise/) possible for members of self-hosted organizations. Sync for these sponsorships will automatically occur per day.
- Cannot be setup by organizations still in a free trial period.

To set up automatic sync:

#### Step 1: Enable cloud communication

> [!TIP] Who can Enable Cloud Comms
> This step must be completed by someone with access to your self-hosted instance's configuration files.

Configure your server to allow communication with Bitwarden cloud systems by setting the following lines in `bwdata/env/global.override.env`:

```
globalSettings__enableCloudCommunication=true
globalSettings__baseServiceUri__cloudRegion=US
```

If your cloud organization was created on EU servers, you'll need make the following changes to configure for communication with EU cloud servers:

- Change the second of these lines to `globalSettings__baseServiceUri__cloudRegion=EU`.
- Set the following 3 additional values:

```
globalSettings__installation__identityUri=https://identity.bitwarden.eu
globalSettings__installation__apiUri=https://api.bitwarden.eu
globalSettings__pushRelayBaseUri=https://push.bitwarden.eu
```

> [!NOTE] Installation id region
> Make sure before proceeding that your configuration correctly correlates to the data region selected when retrieving your [installation ID & key](https://bitwarden.com/host/) as described above.

Once you have set these value, apply your change by running the `./bitwarden.sh rebuild `command. Start your server again with the `./bitwarden.sh start` command.

> [!NOTE] Self-hosting communication fire walls
> Enabling automatic sync requires communication with Bitwarden's cloud systems. If your environment uses a firewall to block outbound traffic, you will need to allow `https://api.bitwarden.com` or `.eu` and `https://identity.bitwarden.com` or `.eu`.

#### Step 2: Retrieve billing sync token

Once cloud communication is enabled at the server-level, a sync token needs to be passed from the cloud organization that is associated with your self-hosted organization. To retrieve your sync token from the cloud web app:

1. Open the **cloud** Admin Console and navigate to **Billing** → **Subscription**.
2. In the self-hosting section, select **Set up billing sync**.
3. Enter your master password and select **Generate token**.
4. Copy the generated token.

#### Step 3: Apply billing sync token

To apply the billing sync token to your self-hosted organization:

1. Open the **self-hosted** Admin Console and navigate to **Billing** → **Subscription**.
2. In the License and billing management section, choose the **Automatic sync** option.
3. Select the **Manage billing sync** button.
4. Paste your generated **Billing Sync Token** and select **Save**.

> [!NOTE] Sync Status `Never`
> Sync for [Families for Enterprise](https://bitwarden.com/help/families-for-enterprise-self-hosted/) will occur once daily once you've triggered your first sync. The **Last sync** field in this section will report **Never** until you trigger your first sync.
> 
> Sync for license updates must always be done manually by selecting the **Sync license** button (see the next section for details).

#### Step 4: Trigger sync

Trigger a sync once you've completed setup and **each time you need to update your license**. Sync for Familes for Enterprise will occur **once daily**. To trigger a sync:

1. Open the **self-hosted** Admin Console and navigate to **Organization** → **Billing**.
2. Select the **Sync license**button.

> [!NOTE] organization license error
> If you receive a `version not supported` error message, update your server and try uploading your license file again. To update your server, make a backup of the `bwdata` directory and follow [these instructions](https://bitwarden.com/help/updating-on-premise/).

### Manual update

To manually re-upload a license file:

1. Follow the steps to **Retrieve your license**again.
2. Open the self-hosted Admin Console and navigate to **Billing** → **Subscription**.
3. In the License and billing management section, choose the **Manual upload** option.
4. Select the **Browse...** or **Choose file** button to add your license file.
5. Select **Submit**.

> [!NOTE] organization license error
> If you receive a `version not supported` error message, update your server and try uploading your license file again. To update your server, make a backup of the `bwdata` directory and follow [these instructions](https://bitwarden.com/help/updating-on-premise/).
