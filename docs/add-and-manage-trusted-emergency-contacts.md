---
URL: https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts/
---

# Add & Manage Trusted Emergency Contacts

Trusted emergency contacts are the people who you allow to log in to your Bitwarden account with [emergency access](https://bitwarden.com/help/emergency-access/). You can add or update your trusted emergency contacts at any time.

## Add a trusted emergency contact

[Adding a trusted emergency contact](https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts/) for emergency access is available to premium users, including members of paid organizations (Families, Teams, and Enterprise). If your organization turned on the [Automatic confirmation policy](https://bitwarden.com/help/policies/#automatic-user-confirmation/), emergency access is **not** available for your account.

To designate a trusted emergency contact for emergency access:

### 1. You invite another user to become your trusted emergency contact.

As someone who wants to grant emergency access to your vault, invite a trusted emergency contact:

1. In the Bitwarden web app, go to **Settings** → **Emergency access**.
2. Select + **Add emergency contact**:

![Emergency access page](https://bitwarden.com/assets/3gb0Zm4K935RUmzjd62eJq/a3930a8381fe1205b655e7a7bb0eca47/2025-12-31_09-50-39.png)
*Emergency access page*
3. Enter the **Email** of your trusted emergency contact. Trusted emergency contacts must have a Bitwarden account (free or premium) and be on the same [server geography](https://bitwarden.com/help/server-geographies/):

![Invite an emergency contact](https://bitwarden.com/assets/2IEldGj87MY2IMDQpty6Vr/f0e9750c278663903be46f4a5d5a4f8c/2025-12-31_09-52-02.png)
*Invite an emergency contact*
4. Set a [**User Access**](https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts/#user-access/) level for the trusted emergency contact, **View** or **Takeover**.
5. Set a [**Wait time**](https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts/#wait-time/).
6. Select **Save** to send the invitation.

Your trusted emergency contact **must now accept the invitation**.

> [!NOTE] Emergency contact invite time
> Invitations to become a trusted emergency contact are only valid for five days.

### 2. They accept the invitation.

As someone who wants to receive emergency access to another vault, accept the invitation:

1. Open the emailed invitation and select **Become emergency contact**:

![Emergency access invitation ](https://bitwarden.com/assets/1S7YBbeECgEdl1v9r4E5BU/37c6c4207cb8c6df7f69a63ea12751fd/Screenshot_2024-02-27_at_9.23.46_AM.png)
*Emergency access invitation *
2. A login page will open in your browser. Depending on if you have an account, select **Log in** or **Create account** to accept the invitation.

After you accept the invitation, the inviting user **must confirm your acceptance as their trusted contact** before they can [initiate access requests](https://bitwarden.com/help/request-and-grant-emergency-access/).

### 3. You confirm them as your trusted emergency contact.

As someone who wants to grant emergency access to your vault, confirm your new trusted contact after they accept your invitation:

1. In the Bitwarden web app, go to **Settings** → **Emergency access.**
2. When the invited user displays the `Needs Confirmation` status, select the ⋮ **Menu icon**.
3. Select **Confirm** from the dropdown menu:

![Confirm an emergency contact](https://bitwarden.com/assets/jEvLxG2nmFJRnlTbcpwRO/891f14df501abae6c1e93ce57a527ec4/2025-12-31_09-53-35.png)
*Confirm an emergency contact*
4. To verify the identity of the invited user, confirm the displayed [fingerprint phrase](https://bitwarden.com/help/fingerprint-phrase/) with the invited user and then select **Confirm**.

## Trusted emergency contact settings

For each trusted emergency contact, pick the wait time before access is granted automatically and the level of access they receive.

### User access

Trusted emergency contacts can be granted either view or takeover access, giving you control over what they can do if they ever need to step in:

- **View**: When an emergency access request is granted, this user is granted view/read access to all items in your individual vault, including login items' passwords and attachments.
- **Takeover**: When an emergency access request is granted, this user must create a master password for permanent read/write access to your vault. This will **replace** your previous master password and remove any [two-step login methods](https://bitwarden.com/help/setup-two-step-login/) that were previously set up.

### Wait time

When a trusted emergency contact [requests access](https://bitwarden.com/help/request-and-grant-emergency-access/#1-the-trusted-contact-requests-access-to-the-account/), you can manually approve or deny it. If you don't respond, access is automatically approved after the wait time you specified when adding that specific trusted emergency contact. The minimum wait time is one day.

## Change trusted emergency contact settings

To change an emergency contact's user access or wait time:

1. Go to **Settings** → **Emergency access**.
2. Select the user's email, which will open their details.
3. Update the **User access** or **Wait time** as desired.
4. Select **Save**.

> [!TIP] Emergency access, manage trusted contact
> You can also manage [pending or granted emergency access requests](https://bitwarden.com/help/request-and-grant-emergency-access/#approve-or-deny-an-emergency-access-request/) from **Settings** → **Emergency access**.

## Remove a trusted emergency contact

To remove a trusted emergency contact from your account:

1. Go to **Settings** → **Emergency access**.
2. Select the ⋮ **Menu icon**.
3. Select **Remove**.
4. Select **Yes** to confirm.

## Frequently asked questions

### Will emergency access still work if my premium features are cancelled or lapse due to a failed payment?

If your premium features are cancelled, your trusted emergency contacts will still be able to request and obtain access to your vault. You will not, however be able to add new or edit existing trusted emergency contacts.

### What happens when my trusted emergency contact changes their account email address?

A user's status as a trusted emergency contact is tied to a unique Bitwarden account ID, meaning that if a trusted emergency contact [changes their email address](https://bitwarden.com/help/product-faqs/) there is no reconfiguration required to maintain their emergency access. Likewise, if the emergency access grantor changes their email address, no reconfiguration is required.

### What happens when my trusted emergency contact deletes their account?

If a trusted emergency contact creates a new Bitwarden account and [deletes](https://bitwarden.com/help/delete-your-account/) the old account, they will automatically be removed as a trusted emergency contact and must be [re-invited](https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts/).

## Next steps

- Share with your trusted emergency contacts [how to request access](https://bitwarden.com/help/request-and-grant-emergency-access/#1-the-trusted-contact-requests-access-to-the-account/), should the need arise.
- Learn how to [handle emergency access requests](https://bitwarden.com/help/request-and-grant-emergency-access/#approve-or-deny-an-emergency-access-request/) to your account.
