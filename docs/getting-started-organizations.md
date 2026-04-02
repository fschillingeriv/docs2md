---
URL: https://bitwarden.com/help/getting-started-organizations/
---

# Organizations Quick Start

Password managers such as Bitwarden make it easy to store and access unique and secure passwords across all of your devices, keeping your online accounts safer than ever! Using Bitwarden, you won't need to dangerously repeat simple passwords or leave them exposed in unencrypted formats such as spreadsheets, documents, or sticky notes.

Bitwarden organizations will add a layer of collaboration and sharing to password management for your family, team, or enterprise, allowing you to securely share common information such as office wifi passwords, online credentials, or shared company credit cards. Secure sharing of organization-owned credentials is **safe** and **easy**.

This article will help you get started with a **free two-person organization** so you can experience secure sharing in no time.

## What are organizations?

Bitwarden organizations relate users and vault items together for [secure sharing](https://bitwarden.com/help/sharing/) of logins, notes, cards, and identities owned by the organization. Organizations could be a family, team, company or any group of people that requires secure shared data. Organizations have a unique view, the Admin Console, where [administrators](https://bitwarden.com/help/user-types-access-control/) can manage the organization's items and users, run reports, and configure organization settings:

![Free organization Admin Console](https://bitwarden.com/assets/hzBuypc5ISzqC3jUmYbea/edcb03ce3d3071cea4f9afb6c7f8eca9/2024-12-03_13-46-09.png)

Unless an organization you're a member of uses [policies](https://bitwarden.com/help/policies/#single-organization/) to restrict you to membership in a single organization, you can be a member of as many as you'd like.

#### Comparing organizations with premium

The key feature to know is that organizations enables **secure sharing from organizations to users**. [Premium individual](https://bitwarden.com/help/password-manager-plans/#premium-individual/) accounts unlock premium password security and management features, including advanced two-factor authentication (2FA) options, the Bitwarden Authenticator (TOTP), encrypted file attachments, and more, but Premium **doesn't include secure data sharing**itself**.**However, every Bitwarden account comes with the option to launch a free two-person organization for secure sharing.

Paid organizations (Families, Teams, or Enterprise) automatically include these premium features (advanced 2FA options, Bitwarden Authenticator (TOTP), and more) for **every** user enrolled in the organization.

## Setup Bitwarden accounts

Free Bitwarden organizations allow for two users to securely share organization-owned credentials. You might use a free organization to share with friend or partner, or to test organizations before [upgrading to a different plan](https://bitwarden.com/help/password-manager-plans/).

Bitwarden provides applications on a variety of devices, including browser extensions, mobile apps, desktop apps, and a CLI, but for the purposes of this guide we'll focus on the [web app](https://bitwarden.com/help/getting-started-webvault/). The web app provides the richest Bitwarden experience for administering your organization.

### Sign up for Bitwarden

[Create a Bitwarden account](https://bitwarden.com/go/start-free/), and make sure that you pick a strong and memorable [master password](https://bitwarden.com/help/master-password/). We even recommend writing down your master password and storing it in a safe location.

> [!NOTE] Master password reminder 
> **Don't forget your Master Password!** Bitwarden is a zero-knowledge encryption solution, meaning that the team at Bitwarden, as well as Bitwarden systems themselves, have no knowledge of, way to retrieve, or way to reset your master password.

Once your account is created, log in to the [web app](https://bitwarden.com/help/getting-started-webvault/) and verify your account's email address to unlock access to all features:

![Send verification email](https://bitwarden.com/assets/7bJkgn3Qjoon9c1h68WmgW/035a83d213860b7c5b92a29502fc315f/2024-12-03_13-54-17.png)

### Sign up for Bitwarden again

In order to use your free two-person organization for secure sharing, you'll need to have two Bitwarden accounts. Once your first Bitwarden account is setup, follow the same procedure (or help your friend or partner to do so) to setup the other account.

> [!NOTE] Organization owner setup
> Bitwarden organizations have a deep level of [member-level permissions customization](https://bitwarden.com/help/user-types-access-control/). Whichever member you proceed to [setup your organization](https://bitwarden.com/help/getting-started-organizations/#setup-your-organization/) with will be the **Owner**.

## Setup your organization

To setup your organization:

1. In the Bitwarden [web app](https://bitwarden.com/help/getting-started-webvault/), select the + **New organization** button:

![New organization](https://bitwarden.com/assets/3eSqWiTIuPSFxXdo5AAjT9/248b0fa7bb381add0d71682acd244a63/2024-12-03_13-57-58.png)
2. Enter an **Organization name** and a **Billing email** we can reach you at. In this guide we are setting up a free organization, so you won't be billed for anything!
3. **Choose your plan**. Bitwarden offers organizations suited to any need, but in this case select **Free**.
4. Scroll down and select **Submit** to finish creating your organization.

### Get to know your organization

Once created, you'll land in the Admin Console, which is the central hub for all things sharing and organization administration. As the [organization owner](https://bitwarden.com/help/user-types-access-control/), you'll be able to see your **Vault**items and [collections](https://bitwarden.com/help/getting-started-organizations/#get-to-know-collections/), to manage **Members,** run **Reports**, change **Billing**settings, and configure other organization **Settings**:

![Free organization Admin Console](https://bitwarden.com/assets/hzBuypc5ISzqC3jUmYbea/edcb03ce3d3071cea4f9afb6c7f8eca9/2024-12-03_13-46-09.png)

Users with access to the Admin Console can get to it from any time in the web app using the left-hand navigation:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)

### Get to know collections

Collections are an important part of a Bitwarden organization, they represent the logical grouping of organization-owned vault items that [belong to your organization](https://bitwarden.com/help/getting-started-organizations/#shared-items/). Your organization comes pre-loaded with a **Default Collection** and an **Unassigned** tag. With a free organization, you can create up to two collections from the Vaults view or from the Admin Console:

![Create new collection](https://bitwarden.com/assets/3rq5lVSQlvNT9gu2M2bCbk/8741dc155e8f2fa83d2caeb69218ce64/2024-12-02_15-35-48.png)

> [!NOTE] Organizations require collections 
> In a lot of ways, collections are like the [folders](https://bitwarden.com/help/folders/) you might use to organize your individual vault. A key difference is that items that [belong to your organization](https://bitwarden.com/help/getting-started-organizations/#shared-items/) **must be included in at least one collection**.

## Add a user to your organization

Now that you are familiar with your organization, it's a good time to add the other organization member you'll be sharing with. To ensure the security of your organization, Bitwarden applies a three-step process for onboarding a new member, [Invite](https://bitwarden.com/help/getting-started-organizations/#invite/) → [Accept](https://bitwarden.com/help/getting-started-organizations/#accept/) → [Confirm](https://bitwarden.com/help/getting-started-organizations/#confirm/).

> [!NOTE] invite accept confirm workflow req
> Completing the full [Invite](https://bitwarden.com/help/getting-started-organizations/#invite/) → [Accept](https://bitwarden.com/help/getting-started-organizations/#accept/) → [Confirm](https://bitwarden.com/help/getting-started-organizations/#confirm/) process is required to ensure that members receive full access to shared organization items.

### Invite

As the organization owner, invite a new member:

1. In the Admin Console, select **Members** from the navigation and use the + **Invite member** button:

![Invite member to an organization](https://bitwarden.com/assets/7AJjR4oqEnCH3A89YYoWpH/498d594fa9703bee9c5f49e2af9f83d0/Invite_member_to_an_organization.png)
2. In the **Role**tab, enter the **Email** of your second member, which should match the email they [signed up for Bitwarden](https://bitwarden.com/help/getting-started-organizations/#sign-up-for-bitwarden-again/) with. Then, select a [Member role](https://bitwarden.com/help/user-types-access-control/#user-types/). In many cases, it's a good idea to add a second user with the **Owner** role to the organization.
3. In the **Collections**tab, select which collections to allow this user access to, as well as what the level of [permission](https://bitwarden.com/help/user-types-access-control/#access-control/) for each to give them.
4. Select **Save** to send the invitation to the designated email address.

Once your invitation is sent, inform your new member and help them [accept the invitation](https://bitwarden.com/help/getting-started-organizations/#accept/).

### Accept

As the newly invited member, open your email inbox and look for an email from Bitwarden inviting you to join an organization. Clicking the link in the email will open an invitation window:

![Bitwarden Invitation ](https://bitwarden.com/assets/6ZzHPswxQoqTbjkSWodwxw/9381e27fdee50d5cfe062473633ef7ed/Screen_Shot_2023-04-28_at_10.40.35_AM.png)

Since you have already [signed up for Bitwarden](https://bitwarden.com/help/getting-started-organizations/#sign-up-for-bitwarden-again/), simply log in. Fully logging in to Bitwarden will accept the invitation.

> [!NOTE] Invitations expiration 
> Invitations expire after five days. Make sure you accept the invitation within that window, otherwise the organization Owner will have to [re-invite you](https://bitwarden.com/help/getting-started-organizations/#invite/).

### Confirm

Confirming accepted members to your organization is the last step to grant members access to shared items. To complete the loop:

1. In the Admin Console, select **Members** from the navigation.
2. Select any `Accepted` users and use the ⋮ Options menu to ✓ **Confirm selected**:

![Confirm member to an organization](https://bitwarden.com/assets/5eRDRAooRSGqRWJYZB5fgz/f3eac670d95664be963d2b38eddf68b5/Confirm_member_to_an_organization.png)
3. Verify that the [fingerprint phrase](https://bitwarden.com/help/fingerprint-phrase/) on your screen matches the one your new member can find in **Settings** → **My account**:

![Fingerprint phrase ](https://bitwarden.com/assets/6sWPBv5GFAyMcULNxfCCJG/b3115a77e0d8d8d48fcc1f9e24e42d70/fingerprint-phrase.png)

Each fingerprint phrase is unique to its account, and ensures a final layer of oversight in securely adding users. If they match, select **Submit**.

## Get to know your vault

Part of the magic of Bitwarden organizations is that items that belong to you and items that [belong to the organization](https://bitwarden.com/help/getting-started-organizations/#shared-items/) are accessible side-by-side from your **Vaults** view. You can filter between your individual items (**My vault**) and organization items (**My Organization**):

![Organization-enabled vault](https://bitwarden.com/assets/4D2tlh9YKPzDY20SYGVKcG/dff56b66549d29405b1af211860f698e/2024-12-03_14-07-28.png)

### Items shared from an organization

You might not have a [item shared from an organization](https://bitwarden.com/help/getting-started-organizations/#share-a-login/) yet, but when you do it will be displayed in your vault with a card indicating where the item is from:

![Shared item badge](https://bitwarden.com/assets/6tnBV4hUxUNtWvGNAp8eua/215f54e0a26f5a1b2d41e18119fdcd71/2024-12-02_15-31-38.png)

Shared items are **owned** by the organization. This means that anyone with permission can alter the item or delete it, which would remove it from your vault as well.

## Move an item to the organization

The last step on the road to secure sharing is to create an item and move it to the organization so it can be shared. An existing [vault item](https://bitwarden.com/help/managing-items/#add-a-vault-item/) can be moved to the organization after it's created, but for this guide, we'll focus on creating a new login from your individual vault:

1. On the **Vaults** page, select the + **New** button and select **Login**.
2. Fill in all the relevant information for your new login item (for example, username and password). The item can be anything you want both yourself and the other organization user to have access to, for example a family streaming account.
3. In the **Ownership** section at the top of the **Add item**panel, select your organization to designate the item for sharing.
4. Select one or more collections to put this item into. Generally, users of two-person organizations setup access for both users for all collections. In larger or more complex organizations, which collection you put the item into will determine who can access it.
5. Select the **Save** button to finishing creating the organization-owned item.

This new item will be accessible to both yourself and the other organization user! As long as both users can access the collection it's in, it will appear for both in the organization vault and in the **All vaults** view alongside other vault items.

## Unshare an item from an organization

If you have shared an item with an organization, there are two options to unshare the item with the organization.

1. Clone the item back to your individual vault by using the product switcher to open the Admin Console and selecting **Clone** from the Options menu for the item you want to clone. Only users with user type admin or higher can clone items into their individual vault by changing the **Ownership** setting.
2. Delete the item from the organization vault by selecting **Delete** from the same menu.

Alternatively, you can unshare items by moving them to a different collection with higher access control restrictions.

## Congratulations!

You have setup your new Bitwarden accounts, created an organization, learned a bit about your vaults, and shared an item! Nice work! If you want to upgrade to a paid organization to unlock [lots of additional features](https://bitwarden.com/help/password-manager-plans/), navigate to your organization's **Billing** → **Subscription** view and select the **Upgrade plan** button:

![Upgrade a free org](https://bitwarden.com/assets/c7MRk3qA3cxcVZHC2gBBs/4128a414a194af6e446ac39d9c250990/2024-12-03_14-09-22.png)
