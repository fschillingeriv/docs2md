---
URL: https://bitwarden.com/help/emergency-access/
---

# Log in with Emergency Access

Emergency access allows you to designate and manage trusted emergency contacts, who can request access to your vault in cases of emergency. Contacts can be granted either view or takeover user access, giving you control over what they can do if they ever need to step in:

- **View**: When an emergency access request is granted, this user is granted view/read access to all items in your individual vault, including login items' passwords and attachments.
- **Takeover**: When an emergency access request is granted, this user must create a master password for permanent read/write access to your vault. This will **replace** your previous master password and remove any [two-step login methods](https://bitwarden.com/help/setup-two-step-login/) that were previously set up.

[Embedded content]## Add trusted emergency contacts

Only premium users, including members of paid organizations (Families, Teams, or Enterprise) can appoint trusted emergency contacts. Anyone with a free or premium Bitwarden account on the same [Bitwarden server](https://bitwarden.com/help/server-geographies/) can be designated as a trusted emergency contact. There is no limit to the number of trusted emergency contacts you can have.

Setting up emergency access is a three-step process: 

1. You **invite**another user to become your trusted emergency contact.
2. They **accept** the invitation.
3. You **confirm**them as your trusted emergency contact.

### Invite

As someone who wants to grant emergency access to your vault, invite a trusted emergency contact:

1. In the Bitwarden web app, go to **Settings** → **Emergency access**.
2. Select + **Add emergency contact**:

![Emergency access page](https://bitwarden.com/assets/3gb0Zm4K935RUmzjd62eJq/a3930a8381fe1205b655e7a7bb0eca47/2025-12-31_09-50-39.png)
*Emergency access page*
3. Enter the **Email** of your trusted emergency contact. Trusted emergency contacts must have a Bitwarden account (free or premium) and be on the same [server geography](https://bitwarden.com/help/server-geographies/):

![Invite an emergency contact](https://bitwarden.com/assets/2IEldGj87MY2IMDQpty6Vr/f0e9750c278663903be46f4a5d5a4f8c/2025-12-31_09-52-02.png)
*Invite an emergency contact*
4. Set a **User Access** level for the trusted emergency contact, **View** or **Takeover**.
5. Set a **Wait time**. This is how long your trusted emergency contact must wait after requesting account access before it's granted, unless you [manually approve the request](https://bitwarden.com/help/emergency-access/#use-emergency-access/) earlier. The minimum wait time is one day.
6. Select **Save** to send the invitation.

Your trusted emergency contact **must now accept the invitation**.

> [!NOTE] Emergency contact invite time
> Invitations to become a trusted emergency contact are only valid for five days.

### Accept

As someone who wants to receive emergency access to another vault, accept the invitation:

1. Open the emailed invitation and select **Become emergency contact**:

![Emergency access invitation ](https://bitwarden.com/assets/1S7YBbeECgEdl1v9r4E5BU/37c6c4207cb8c6df7f69a63ea12751fd/Screenshot_2024-02-27_at_9.23.46_AM.png)
*Emergency access invitation *
2. A login page will open in your browser. Depending on if you have an account, select **Log in** or **Create account** to accept the invitation.

After you accept the invitation, the inviting user **must confirm your acceptance** before you can [initiate access requests](https://bitwarden.com/help/emergency-access/#use-emergency-access/).

### Confirm

As someone who wants to grant emergency access to your vault, confirm your new trusted emergency contact after they accept your invitation:

1. In the Bitwarden web app, go to **Settings** → **Emergency access.**
2. When the invited user displays the `Needs Confirmation` status, click the ⋮ **Menu icon**.
3. Select **Confirm** from the dropdown menu:

![Confirm an emergency contact](https://bitwarden.com/assets/jEvLxG2nmFJRnlTbcpwRO/891f14df501abae6c1e93ce57a527ec4/2025-12-31_09-53-35.png)
*Confirm an emergency contact*
4. To ensure the integrity of your encryption keys, verify the displayed [fingerprint phrase](https://bitwarden.com/help/fingerprint-phrase/) with the grantee and then select **Confirm**.

## Use emergency access

Once [set up](https://bitwarden.com/help/emergency-access/#add-trusted-emergency-contacts/), a trusted emergency contact can **request access** to your account. If you can still log in to your account, you can **approve or deny the request** during the specified wait time. When you no longer want a trust contact to be able to **access your account**, you can **revoke their emergency access**.

### Request access

To request access to an account:

1. When logged in to the account that's set up as a trusted emergency contact and in the Bitwarden web app, go to **Settings** → **Emergency access**.
2. In the **Designated as emergency contact** section, select the ⋮ **Menu icon**:

![Request emergency access](https://bitwarden.com/assets/6x38VldDaEOAqpuCQ4htRJ/7946735436fd16b660aad5d7969dba8d/2025-12-31_09-54-39.png)
*Request emergency access*
3. Select **Request Access** from the confirmation that appears. An email is sent to the account holder, telling them that access to their account was requested.

You will be provided access to the grantor's vault after the wait time specified **or** when the grantor manually approves your emergency access request.

### Approve or deny requests

You can manually approve or reject an emergency access request before the set wait time lapses. To approve or reject an emergency access request:

1. In the Bitwarden web app, go to **Settings** → **Emergency access**.
2. In the **Trusted emergency contacts** section, use the ⋮ **Menu icon**.
3. Select **Approve** or **Reject:**

![Approve or reject emergency access](https://bitwarden.com/assets/7iPFwb2NfsjeVywrwlZxSx/8ff35e1f5d8e2febf34089528ecea5ff/2025-12-31_09-55-14.png)
*Approve or reject emergency access*
4. Select **Approve** or **Reject**.

### Access the account

To access the vault after your request is approved or the wait time elapses:

1. In the Bitwarden web app, go to **Settings** → **Emergency access**.
2. In the **Designated as emergency contact** section, select the ⋮ **Menu icon** and choose the option from the dropdown menu that corresponds with your [assigned access](https://bitwarden.com/help/emergency-access/#user-access/):

 - **View**: This will display the grantor's vault items.
 - **Takeover**: This will prompt you to enter and confirm a new master password for the grantor's account. Select **Save** and log in with the grantor's email address and the new master password.

> [!NOTE] Emergency access, takeover an org. member
> When you use emergency access to **takeover an account that is in an organization**, there are a few important considerations:
> 
> - If turned on for the organization, the [master password requirements](https://bitwarden.com/help/policies/#master-password-requirements/) policy will be enforced when you change the master password for the takeover.
> - The account will be automatically removed from any organization(s) that they are not the [owner](https://bitwarden.com/help/user-types-access-control/).
> - If the account is the organization owner, they will not be removed from or lose permissions within their organization(s). As such, policies not enforced on owners will still not be enforced after the takeover.

### Revoke access

You may want to revoke a trusted contact's access to your vault. The steps to remove someone's previously granted emergency access to your account depends on if the user was granted view or takeover access.

## View access

When someone is granted **view** access via emergency access, they can view your vault items until their access is manually revoked.

To revoke someone's view access granted via emergency access:

1. Go to **Settings** → **Emergency access**.
2. Select the ⋮ **Menu icon** on the same line as their email.
3. Select [close] **Reject**:

![Reject emergency access ](https://bitwarden.com/assets/7dhQEDLZNKCwwspstJnhj0/543dd12da8a8d64952763027678cf15a/2025-12-31_09-55-33.png)
*Reject emergency access *

## Takeover access

When a trusted emergency contacts is granted and use **takeover** access, they change the master password on your account. As a result, the only way to remove their access is to:

1. Obtain the new master password they created for your account and use it to log in the [web vault](https://bitwarden.com/help/getting-started-webvault/).
2. [Change your master password](https://bitwarden.com/help/master-password/#change-your-master-password/) to one that they do not know.

## Manage trusted emergency contacts

You can update your trusted emergency access contacts at any time. To change an emergency access contact's user access or wait time:

1. Go to **Settings** → **Emergency access**.
2. Click on the user's email, which will open their details.
3. Update the **User access** or **Wait time** as desired.
4. Select **Save**.

To remove someone as a trusted emergency contact:

1. Go to **Settings** → **Emergency access**.
2. Select the ⋮ **Menu icon**.
3. Select **Remove**.
4. Select **Yes** to confirm.

After access to your account is granted to a trusted contact, you can [revoke their access](https://bitwarden.com/help/emergency-access/#use-emergency-access/).

## How it works

> [!NOTE] WP: See encryption section
> The following information references encryption key names and processes that are discussed in [hashing, key derivation, and encryption](https://bitwarden.com/help/bitwarden-security-white-paper/#hashing-key-derivation-and-encryption/). Consider reading those details first.

Emergency access uses public key exchange and encryption/decryption to allow users to give a trusted emergency contact permission to access vault data in a zero-knowledge encryption environment:

1. A Bitwarden user (the grantor) invites another Bitwarden user to become a trusted emergency contact (the grantee). The invitation specifies a user access level, includes a request for the grantee's **RSA Public Key**, and is valid for only five days.
2. Grantee is notified of the invitation via email and accepts the invitation to become a trusted emergency contact. On acceptance, the grantee's **RSA Public Key** is stored with the user record.
3. Grantor is notified of the invitation's acceptance via email and confirms the grantee as their trusted emergency contact. On confirmation, the grantor's **User Symmetric Key** is encrypted using the grantee's **RSA Public Key** and stored with the invitation. Grantee is notified of confirmation.
4. An emergency occurs, resulting in grantee requiring access to grantor's vault. Grantee submits a request for emergency access.
5. Grantor is notified of the request via email. The grantor may manually approve the request at any time, otherwise the request is bound by a grantor-specified wait time. When the request is approved or the wait time lapses, the **Public Key-encrypted User Symmetric Key** is delivered to the grantee for decryption with the grantee's **RSA Private Key**. 

Alternatively, the grantor may reject the request, which will prevent the grantee gaining access as described in the next step. Rejecting a request will not remove the grantee from being a trusted emergency contact or prevent them from making access requests in the future.
6. Depending on the specified user access level, the grantee will either:

 - **View**: Obtain view/read access to items in the grantor's vault.
 - **Takeover**: Be asked to create a new master password for the grantor's vault.

## Frequently asked questions

### What happens when my trusted emergency contact changes their account email address?

A user's status as a trusted emergency contact is tied to a unique Bitwarden account ID, meaning that if a trusted emergency contact [changes their email address](https://bitwarden.com/help/product-faqs/) there is no reconfiguration required to maintain their emergency access. Likewise, if the emergency access grantor changes their email address, no reconfiguration is required.

### What happens when my trusted emergency contact deletes their account?

If a trusted emergency contact creates a new Bitwarden account and [deletes](https://bitwarden.com/help/delete-your-account/) the old account, they will automatically be removed as a trusted emergency contact and must be [re-invited](https://bitwarden.com/help/emergency-access/#add-trusted-emergency-contacts/).

### Will emergency access still work if my premium features are cancelled or lapse due to a failed payment?

If your premium features are cancelled, your trusted emergency contacts will still be able to request and obtain access to your vault. You will not, however be able to add new or edit existing trusted emergency contacts.
