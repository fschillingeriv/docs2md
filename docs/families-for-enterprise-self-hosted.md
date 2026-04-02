---
URL: https://bitwarden.com/help/families-for-enterprise-self-hosted/
---

# Self-hosting Families Sponsorships

Members of [enterprise organizations](https://bitwarden.com/help/about-organizations/#types-of-organizations/) are offered a **free Families organization** sponsorship that can be applied to a new or pre-existing Families organization and redeemed directly from the web vault.

> [!NOTE] Families License
> If you're looking for information on updating a license for a non-sponsored self-hosted Families organization, see [here](https://bitwarden.com/help/licensing-on-premise/#update-organization-license/).

You will need to enable automatic billing sync to allow your self-hosted enterprise organization to issue sponsorships for cloud Families organizations. To set up automatic sync:

## Step 1: Enable cloud communication

First, you'll need to configure your server to allow communication with our cloud systems. 

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

Once you have set these values, apply your changes by running the `./bitwarden.sh restart `command.

> [!NOTE] Self-hosting communication fire walls
> Enabling automatic sync requires communication with Bitwarden's cloud systems. If your environment uses a firewall to block outbound traffic, you will need to allow `https://api.bitwarden.com` or `.eu` and `https://identity.bitwarden.com` or `.eu`.

## Step 2: Retrieve billing sync token

Once cloud communication is enabled at the server-level, a sync token needs to be passed from the cloud organization you use for billing to your self-hosted organization. To retrieve your sync token from the cloud web vault you must be an organization owner. To retrieve the token:

1. Open the cloud web app and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
2. Navigate to **Billing** → **Subscription**.
3. Scroll down to the Self-hosting section and select the **Set up billing sync **button.
4. Enter your master password and select **Generate token**.
5. Copy the generated token.

## Step 3: Apply billing sync token

To apply the billing sync token to your self-hosted organization:

> [!WARNING] F4E on Old Server Version
> At this stage, if you're upgrading your self-hosted deployment from an earlier version, you may need to [manually update your license file](https://bitwarden.com/help/licensing-on-premise/#organization-license/) before proceeding.

1. Open the self-hosted Admin Console and navigate to **Billing** → **Subscription**.
2. In the License and billing management section, choose the **Automatic sync** option.
3. Select the **Manage billing sync** button.
4. Paste your generated **Billing sync token** and select **Save**.

> [!NOTE] Sync Status `Never`
> Sync for [Families for Enterprise](https://bitwarden.com/help/families-for-enterprise-self-hosted/) will occur once daily once you've triggered your first sync. The **Last sync** field in this section will report **Never** until you trigger your first sync.
> 
> Sync for license updates must always be done manually by selecting the **Sync license** button (see the next section for details).

## Step 4: Trigger sync

Trigger a sync once you've completed setup. Billing sync will occur **once daily**, however you can manually trigger a sync at any time. To trigger a sync:

1. Open the self-hosted [System Administrator Portal](https://bitwarden.com/help/system-administrator-portal/) and navigate to **Organization** and select the enterprise organization.
2. Locate the Connections section and select the **Manually Sync**button.

> [!NOTE] organization license error
> If you receive a `version not supported` error message, update your server and try uploading your license file again. To update your server, make a backup of the `bwdata` directory and follow [these instructions](https://bitwarden.com/help/updating-on-premise/).

In between syncs, users may see the status `Awaiting Sync` after redeeming or changing a sponsorship. This indicates your self-hosted Bitwarden server is waiting to sync with the Bitwarden cloud before a sponsorship can be fully redeemed or changed.
