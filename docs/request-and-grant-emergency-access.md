---
URL: https://bitwarden.com/help/request-and-grant-emergency-access/
---

# Request & Grant Emergency Access

As a trusted emergency contact, you may want to request [emergency access](https://bitwarden.com/help/emergency-access/) to a Bitwarden vault when the account holder is unreachable or [forgets their master password](https://bitwarden.com/help/forgot-master-password/). Once requested, the account holder can [approve or deny access](https://bitwarden.com/help/request-and-grant-emergency-access/#approve-or-deny-an-emergency-access-request/), or it will be granted automatically after your configured wait time passes.

## Get emergency access to an account

There are three steps for a [trusted emergency contact](https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts/) to gain emergency access:

### 1. The trusted emergency contact requests access to the account.

First, request access to the account:

1. In the Bitwarden web app, go to **Settings** → **Emergency access**.
2. In the **Designated as emergency contact** section, select the ⋮ **Menu icon** next to the account you want to access:

![Request emergency access](https://bitwarden.com/assets/6x38VldDaEOAqpuCQ4htRJ/7946735436fd16b660aad5d7969dba8d/2025-12-31_09-54-39.png)
*Request emergency access*
3. Select **Request Access** from the confirmation that appears. This will send an email to the account holder, telling them that access to their account was requested.

### 2. The trusted emergency contact's request is approved or denied.

If the account holder can't log in, your request is automatically approved once the [wait time](https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts/#wait-time/) expires.

If the account holder can log in before then, however, they can manually [approve or reject your request](https://bitwarden.com/help/request-and-grant-emergency-access/#approve-or-deny-an-emergency-access-request/).

### 3. If approved, the trusted emergency contact gets access by viewing the vault or updating the master password to log in to the account.

After your request is approved, you can access the account:

1. In the Bitwarden web app and, go to **Settings** → **Emergency access**.
2. In the **Designated as emergency contact** section, select the ⋮ **Menu icon** and choose the option from the dropdown menu that corresponds with your [assigned access](https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts/#user-access/):

 - **View**: This will display the account holder's vault items.
 - **Takeover**: This will prompt you to enter and confirm a new master password for the account holder's account. Select **Save** and log in with the account holder's email address and the new master password.

## Manage a trusted emergency contact's access

As the account holder, you can control a trusted emergency contact's access to your account at three points:

- [Remove](https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts#remove-a-trusted-emergency-contact/) them from your list of trusted emergency contacts.
- [Approve or deny their pending request](https://bitwarden.com/help/request-and-grant-emergency-access/#approve-or-deny-an-emergency-access-request/) for emergency access.
- Revoke their granted emergency access. The steps depend on whether they were granted [view](https://bitwarden.com/help/request-and-grant-emergency-access/#revoke-view-access/) or [takeover](https://bitwarden.com/help/request-and-grant-emergency-access/#revoke-takeover-access/) access.

### Approve or deny an emergency access request

If you can still log in to your account when a trusted emergency contact requests access, you can approve or deny the request before the [wait time](https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts/#wait-time/) expires. To approve or reject an emergency access request: 

1. In the Bitwarden web app, go to **Settings** → **Emergency access**.
2. In the **Trusted emergency contacts**section, select the ⋮ **Menu icon** next to the account that requested access.
3. Select **Approve** or **Reject:**

![Approve or reject emergency access](https://bitwarden.com/assets/7iPFwb2NfsjeVywrwlZxSx/8ff35e1f5d8e2febf34089528ecea5ff/2025-12-31_09-55-14.png)
*Approve or reject emergency access*

### Revoke view access

When someone is granted [view access](https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts/#user-access/) via emergency access, they can review your vault items until you revoke it.

To revoke someone's view access granted via emergency access:

1. In the Bitwarden web app, go to **Settings** → **Emergency access**.
2. In the **Trusted emergency contacts**section, select the ⋮ **Menu icon** next to the account with active emergency access.
3. Select **Reject**:

![Reject emergency access ](https://bitwarden.com/assets/7dhQEDLZNKCwwspstJnhj0/543dd12da8a8d64952763027678cf15a/2025-12-31_09-55-33.png)
*Reject emergency access *

### Revoke takeover access

When a trusted emergency contact is granted and uses [takeover access](https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts/#user-access/), they change the master password on your account. As a result, the only way to remove their access is to:

1. Obtain the new master password they created for your account.
2. Log in to the [web app](https://bitwarden.com/help/getting-started-webvault/) with the new master password.
3. [Change your master password](https://bitwarden.com/help/master-password/#change-your-master-password/) to one that they do not know.
