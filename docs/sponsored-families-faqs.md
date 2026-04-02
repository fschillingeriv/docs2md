---
URL: https://bitwarden.com/help/sponsored-families-faqs/
---

# Sponsored Families FAQs

## Employer FAQs

#### Q: Can self-hosted Enterprise organizations issue sponsorships?

**A:**Yes. There's a short setup procedure that must be completed by an administrator which you can learn more about [here](https://bitwarden.com/help/families-for-enterprise-self-hosted/). Please remind your users that their sponsored Families organization can be redeemed through our public cloud (`https://vault.bitwarden.com`).

## Employee FAQs

#### Q: Can I redeem with the account that's a member of the sponsoring Enterprise?

**A:** No. Upon redemption, you will be asked to enter a **personal email address** that you own. If you already have a personal Bitwarden account, enter that account's email address. If you don't, enter a personal email address for which you want to create a personal Bitwarden account.

#### Q: Can I redeem for my existing Families organization?

**A:** Yes! Redeeming a sponsorship for an active Families organization will immediately switch you to a sponsored subscription and add prorated account credit for the time remaining on the subscription you have paid for.

#### Q: Can I add additional storage?

**A:** Yes, however 5 GB is included in your sponsorship. More storage can be added at any time and doing so will charge your payment method on file.

#### Q: What happens if I leave the organization sponsoring me?

**A:** If you leave or are removed from the sponsoring organization, or if you manually end your sponsorship, your payment method on file will be charged at the next billing interval.

#### Q: What do I do if I received a renewal reminder in my email?

**A**: If you're still a member of the Enterprise organization, typically an employer, that's sponsoring your free Families organization, you can safely ignore this email. If you're no longer a member of that Enterprise organization, ensure your organization will renew without interruption by opening your Families organization Admin Console, navigating to **Billing** → **Payment method**, and checking that the payment method is valid.

#### Q: What does `Awaiting Sync` mean?

**A:** The status `Awaiting Sync` indicates your self-hosted Bitwarden server is waiting to sync with the Bitwarden cloud before your sponsorship can be fully redeemed or changed. Sync happens once a day.

If you try to redeem your sponsorship before the sync is complete, you will get an error message in the cloud web vault that reads `Cannot find an outstanding sponsorship offer for this organization.`

#### Q: Can a sponsored Families organization be on a self-hosted server?

**A:** Yes, however there are a few steps to go through:

1. Redeem your sponsorship at `https://vault.bitwarden.com` [as described above](https://bitwarden.com/help/families-for-enterprise/#redeem-a-sponsorship/).
2. Still on `https://vault.bitwarden.com`, retrieve your Families organization's license file [as described here](https://bitwarden.com/help/licensing-on-premise/#organization-license/).
3. Log in to your self-hosted server and apply the license file to an organization [as described here](https://bitwarden.com/help/licensing-on-premise/#organization-license/).

Please note, your self-hosted server will need to be connected to an SMTP mail server in order for invitations to your families organization to be sent to other members.

#### Q: If my organization is on a US server, can I redeem a Families organization on the EU server?

**A:**No, the Families plan sponsorship can only be redeemed on the same cloud server as the sponsoring Enterprise organization. If your Enterprise organization has migrated from one cloud server to another, a new Families organization will have to be sponsored on the correct cloud server. For more information on migrating organizations, see the Bitwarden [migration guide](https://bitwarden.com/help/teams-enterprise-migration-guide/).

#### Q: How do I remove a Families organization?

**A:**To remove a Families organization, log in to the account that is a member of the Enterprise organization and navigate to **Settings** → **Free Bitwarden Families**. Select the ⚙️ cog icon associated with the sponsored Families organization and select **Remove**.
