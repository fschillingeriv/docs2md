---
URL: https://bitwarden.com/help/server-geographies/
---

# Server Geographies

The Bitwarden cloud is available globally with data storage in both **United States** and **European Union** regions. The practices used by Bitwarden for securing your sensitive data are the same, regardless of which server region you use. Learn more [about how Bitwarden secures your data](https://bitwarden.com/help/data-storage/).

## Choose your cloud server

To choose which Bitwarden server geography to create your account or organization on, select the **Server** or **Logging in on:**dropdown on the login or registration screen and select your desired region:

### Web app

![Region selector on web app](https://bitwarden.com/assets/30W3B0aJy0dzO0pKTaBr7h/ed4fa669856dc3b13dbd80a1e0b237b5/2024-12-04_10-09-00.png)

### Browser extension

![Region selector on browser extensions](https://bitwarden.com/assets/4Kas8J6TjKZWMdaTo7pZMX/7d33be1c411bcf7eaf0816842beb824b/2025-02-18_14-09-00.png)

### Mobile app

![Region selector on mobile apps](https://bitwarden.com/assets/753jtQ6dg9u6Rln2A7TF4R/01b3d12d193d8f00432b925c29999d91/2025-02-18_14-18-33.png)

### Desktop app

![Region selector on desktop apps](https://bitwarden.com/assets/3FlU02971dqGGkp86WJJc5/43aeb8ee7de20a3cc0156fbf2c766432/choose-my-service-1.png)

Bitwarden data regions are separate, and your account or organization only exists in the region where it was first created.

### Connect your self-hosted server

Self-hosting a Bitwarden organization or individual premium plan requires first starting a subscription on a cloud server and subsequently [uploading a license file](https://bitwarden.com/help/licensing-on-premise/) to your self-hosted instance. If you create your subscription on an EU server, add the following [environment variables](https://bitwarden.com/help/environment-variables/) to your server's `./bwdata/env/global.override.env` file to ensure you're communicating with the correct server:

```
globalSettings__installation__identityUri=https://identity.bitwarden.eu
globalSettings__installation__apiUri=https://api.bitwarden.eu
globalSettings__pushRelayBaseUri=https://push.bitwarden.eu
```

> [!NOTE] Installation id region
> Make sure before proceeding that your configuration correctly correlates to the data region selected when retrieving your [installation ID & key](https://bitwarden.com/host/) as described above.

## Migrate to another cloud

To migrate from one Bitwarden cloud server to another, for example, from a US server to an EU server:

1. [Export your organization vault](https://bitwarden.com/help/export-your-data/#export-an-organization-vault/) and instruct all organization members to [export their individual vaults](https://bitwarden.com/help/export-your-data/#export-an-individual-vault/).

> [!TIP] For C2C migration, download attachments
> Individually download any file attachments for vault items and note which items they belong to.
2. Create a new Bitwarden account in the desired region and start a trial organization. Bitwarden support will be able to migrate your subscription to the new region (see **Step 4**).
3. Set up your new organization, configuring things like enterprise policies, login with SSO, constructing group-collection relationships, and inviting users with Directory Connector or SCIM. For help, refer to the [Proof-of-Concept Checklist](https://bitwarden.com/help/proof-of-concept/).
4. [Contact Bitwarden support](https://bitwarden.com/contact/) to move your new organization off of trial and resume your subscription in your new region.
5. Import your organization vault data obtained in **Step 1**, and instruct organization members to import their individual vaults as well.

### Migration FAQs

**Q:** **Do I need to migrate?**

**A:** Migrating regions is not required. The region selector allows organizations to specify the geographic location of vault data. Features and functions are identical across regions.

**Q: Is there a process for migrating?**

**A:** Bitwarden regions are distinct cloud environments. Bitwarden cannot migrate accounts from one region to another for customers. A script is available for organizations to help facilitate migrations. Subscriptions can be transferred from one region to another region by [contacting us](https://bitwarden.com/contact/).

**Q: Can an account created in one server geography join an organization in another server geography?**

**A:**No, vault data and user data are completely separate between server geographies. If a user is on a different server than an organization, the user cannot access or interact with that organization. This separation includes organizations that have migrated and are no longer on the same cloud server as the organization members.

**Q: What does the migration script do?**

**A:** The script works with the Bitwarden CLI to move data from one installation to another. Instructions are available in [this article](https://bitwarden.com/help/migration-script/). This script migrates all organization vault data, including attachments, as well as member roles (excluding the custom role), and collections permissions assigned both to members and groups. The script also automatically recreates your groups in the new organization if you’re not using directory integration for automatic provisioning. Note that this does not include the migration of individual user vaults.

**Q: What does a manual migration look like?**

A: A complete manual migration involves creating a new account in the preferred region and beginning the new organization creation process. Once the new organization is configured, re-invite users, and then export vault data from your old organization and import into the new one. Users will need to manually export/import their individual vaults.

**Q: What happens to my sponsored families plan if we migrate our enterprise plan?**

A: Complimentary families plan for enterprise employees must be based in the same region as the sponsoring plan. If your enterprise plan migrates to another region, it will end your families plan sponsorship. You will need to migrate your families plan and then sponsor the new plan following the steps in the [Redeem Families Sponsorship](https://bitwarden.com/help/families-for-enterprise/) article.
