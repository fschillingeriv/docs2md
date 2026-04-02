---
URL: https://bitwarden.com/help/automatic-confirmation/
---

# Automatic Confirmation

By default, users invited to join a Bitwarden organization must be [confirmed by an administrator](https://bitwarden.com/help/managing-users/#confirm/) once they accept an invitation to join. Confirmation is a crucial step that completes the three-step onboarding process designed to facilitate end-to-end-encrypted sharing of items between organizations and their members.

Enterprise organizations can optionally set up automatic confirmation of users if it is not desired that administrators manually confirm each user joining the organization.

In order to be eligible for automatic confirmation functionality:

- **Added by your Bitwarden team**: In order to gain access to this automation, Bitwarden support will need to add it to your organization. The first step is to [contact us](https://bitwarden.com/contact/).
- **Single organization policy will extend to all roles**: The [Single organization policy](https://bitwarden.com/help/policies/#single-organization/) must be on and all members, including owners and admins who are not typically subject to the policy, must be compliant with it.
- **No emergency access**: To mitigate some risks of using automatic confirmation, [emergency access](https://bitwarden.com/help/emergency-access/) will be removed for all members of your organization. Members using emergency access will receive an email informing them it's been turned off.
- **No provisioned provider accounts**: A member of a [provider](https://bitwarden.com/help/providers/) may not be an provisioned member of in your organization. A provider can still manage your organization, but its members cannot occupy a seat in your organization.
- **Accept potential security risks**: Automatic confirmation could pose a security risk to your organization's data. Before using automatic confirmation, make sure you read about the [risks outlined in this article](https://bitwarden.com/help/automatic-confirmation/#potential-security-risks/) and accept them.

Once activated, automatic confirmation is a background process executed by unlocked browser extensions belonging to [owners, admins, and custom role members](https://bitwarden.com/help/user-types-access-control/) with the **Manage users** permission. Learn how to activate automatic confirmation in the following sections.

> [!NOTE] Events logged for automatic confirmation.
> [Events](https://bitwarden.com/help/event-logs/#organization-events/) are logged when automatic confirmation is turned on or off for the organization, turned on or off by each administrator, and when a member is automatically confirmed.

## Turn on automatic confirmation

In order to turn on automatic confirmation of new members, you must turn it on both at the organization level and for each Bitwarden client that you want executing the process.

### For the organization

To turn on automatic confirmation for your organization, make sure you've met the eligibility requirements described above. Once you've contacted your Bitwarden team, an activation panel will be issued to organization owners the next time they log in. 

Once the functionality is added for your organization by Bitwarden, Automatic confirmation can also be activated [via a policy](https://bitwarden.com/help/policies/#automatic-user-confirmation/) from the **Settings** → **Policies** menu in the Admin Console. Either way, select **Continue** to turn on automatic confirmation for the organization:

![Automatic confirmation of new users](https://bitwarden.com/assets/1ggo2uyCvldAlJcOxAmGdv/eabe1eb2c5a82731268d6b3486fbc3d5/2026-02-05_10-43-27.png)
*Automatic confirmation of new users*

### For each administrator

Once turned on for the organization, each [owner, admin, and custom role member](https://bitwarden.com/help/user-types-access-control/) with the **Manage users** permission will be issued an activation panel **in the browser extension** inviting them to turn automatic confirmation on for that client. 

Administrators that close this dialog can toggle automatic confirmation on or off from the browser extension's **Settings** → **Admin**menu. Either way, select **Turn on** to begin automatic confirmation:

![Turn on automatic confirmation](https://bitwarden.com/assets/18MR4NrPqPFWRW7W5oqFzW/40422afa9db8a695213a80944d427589/2026-02-05_11-02-16.png)
*Turn on automatic confirmation*

In order for members to be automatically confirmed, at least one [owner, admin, or relevant custom role member](https://bitwarden.com/help/user-types-access-control/) must turn this on. The automatic confirmation process runs in the background of each unlocked browser extension client that chooses to turn it on.

## Potential security risks

Before turning on automatic confirmation, **make sure you understand the potential risks associated with its use**.

Decryption of your organization's data requires that a user goes through a three-step (Invite → Accept → Confirm) onboarding workflow in order to [facilitate the secure sharing of encryption keys](https://bitwarden.com/help/bitwarden-security-white-paper/#sharing-data-between-users/) and maintain an end-to-end encrypted environment. In this workflow, manual confirmation operates as a final protection to ensure that only members who are intended to access organization data can do so; if an unintended person or malicious actor has accepted an invitation, they could be caught and denied at the confirmation step to prevent unwanted access.

Actors with unrestricted access to the database used by your Bitwarden server, whether self-hosted or cloud-hosted, could fabricate an invitation to join your organization and accept it. With automatic confirmation running, there would be no manual intervention that would allow administrators to catch and deny access to such an actor.
