---
URL: https://bitwarden.com/help/org-faqs/
---

# Organizations FAQs

This article contains Frequently Asked Questions (FAQs) regarding organizations.

For more high-level information about organizations, refer to the following articles:

- [About Organizations](https://bitwarden.com/help/about-organizations/)
- [About Collections](https://bitwarden.com/help/about-collections/)
- [About Groups](https://bitwarden.com/help/about-groups/)

## Organizations general

### Q: What's the difference between organizations and premium?

**A:** Organizations enable secure sharing from organizations to organization users.

Premium individual plans unlock premium password security and management features, including advanced 2FA options, the Bitwarden authenticator (TOTP), encrypted file attachments, and more. Premium individual does not include secure data sharing.

Paid organizations (Families, Teams, or Enterprise) automatically include premium features (advanced 2FA options, Bitwarden authenticator, and more) for every user enrolled in the organization.

## Organization administration

### Q: My organization's owner is no longer with the company, can a new owner be created?

**A:** Only an owner can create a new owner or assign owner to an existing user. For failover purposes, Bitwarden recommends creating multiple owner users. If your single owner has left the company, [contact us](https://bitwarden.com/contact/).

### Q: I have invited users but they cannot see shared items, what do I do?

**A:** Invited users will receive an email asking them to join the organization. First, make sure they have accepted the invitation. If they have, an admin or owner should navigate to the **Members**screen and use the ⋮ options menu to select **Confirm**.

### Q: What events are audited for my organization?

**A:** For a full list of what's included in Bitwarden event logs, see [Event Logs](https://bitwarden.com/help/event-logs/).

### Q: Can I prevent users from self-registering into my organization?

**A:** If you are self-hosting, [configure the environment variable](https://bitwarden.com/help/environment-variables/) `globalSettings__disableUserRegistration=` to `true` to prevent users from signing up for an account via the registration page. Once configured, organization admins or owners must invite users to signup for an account on the self-hosted instance.

### Q: How do I change the name of my organization?

**A:** To change the name of your organization:

1. In the web app, open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
2. Navigate to the ⚙️ **Settings** → **Organization info** screen.
3. Edit the **Organization name** field and select the **Save** button.

**If you are self-hosting**, you will also need to:

1. Navigate to the ⚙️ **Billing** → **Subscription** page.
2. Select the **Download license** button to download a license with the updated organization name.
3. [Upload the new license](https://bitwarden.com/help/licensing-on-premise/#organization-license/) to your self-hosted server.

### Q: How do I optimize performance for a vault with lots of items?

**A**: Since decryption of vault items is done locally, never in our servers, load times may occasionally be longer for a vault with a large number of items. Our team is always working on performance optimization, however here are a few tips that can help reduce load times:

- Follow the principle of least privilege, for example by using collections to organize your vault items. Reducing the number of items a user can access will reduce the number of items to be decrypted while the app is loading.
- For owners and admins, don't use the **This user can access and modify all items**option. These user roles get access to everything via the organization vault anyway, so selecting this options will only add additional items to their **Vaults**view and increase the number of items to be decrypted while the app is loading.
- If you manage multiple organizations, consider contacting us to become a [Provider](https://bitwarden.com/help/providers/). Accessing organizations from the Provider Portal will slightly reduce the amount of required to decrypt all managed items.

### Q: How do I leave an organization?

**A**: To leave an organization, use the web app to select the ⋮ options menu for the organization you want to leave. From the dropdown, select [sign-in] **Leave**: 

![Leave an organization](https://bitwarden.com/assets/2MP5ZWZbCJe6ArraaEMku9/eda75c81ab46706bd8ef373a395bd78b/2025-04-01_14-59-09.png)

## Sharing with an organization

### Q: How do I "unshare" an item from my organization?

**A:** To unshare an item:

1. Clone the item back to your individual vault by using the ⋮ **Options** menu to select **Clone**. This can be done from the Admin Console or, if you are an Owner, Admin, or have Manage collection access to the collection the item is kept in, it can also be done from your Vaults view.
2. Delete the item from the organization vault by selecting **Delete** from the ⋮ **Options** menu.

Alternatively, you can unshare items by moving them to a different collection with higher access control restrictions.

### Q: How do I hide a password from my organization's users?

**A:** Assign the users you want to hide passwords from either **View items, hidden passwords**or **Edit items, hidden passwords**[permission](https://bitwarden.com/help/user-types-access-control/#permissions/) to relevant collections.

### Q: Does an item I move to the organization stay after I leave?

**A:** It does! When a user shares an item with an organization, the organization takes ownership of the item. Even if the user leaves the organization or deletes their account, that item will remain in the organization vault.

## Organization installations

### Q: Can I silently install the Bitwarden desktop app for my users?

**A:** Yes. When silently installing the desktop app across workstations, please do so as a privileged account like an administrator and use the `/allusers` switch in addition to `/S`. For single-user installation, or if your system supports `Logged on User`, use `/S` without `/allusers`.` `
