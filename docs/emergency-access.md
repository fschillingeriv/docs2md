---
URL: https://bitwarden.com/help/emergency-access/
---

# About Emergency Access

Emergency access lets you prepare for the unexpected by appointing trusted emergency contacts who can request access to your Bitwarden vault if needed. Trusted emergency contacts can be granted either view or takeover access, giving you control over what they can do if they ever need to step in:

- **View**: When an emergency access request is granted, this user is granted view/read access to all items in your individual vault, including login items' passwords and attachments.
- **Takeover**: When an emergency access request is granted, this user must create a master password for permanent read/write access to your vault. This will **replace** your previous master password and remove any [two-step login methods](https://bitwarden.com/help/setup-two-step-login/) that were previously set up.

## Set up and use emergency access

There are a few steps to grant someone emergency access to an account:

1. The account holder [adds a trusted contact](https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts/) for their account before an emergency arises.
2. When needed, the trusted contact [requests access](https://bitwarden.com/help/request-and-grant-emergency-access/#1-the-trusted-contact-requests-access-to-the-account/) to the account.
3. The [request is approved ](https://bitwarden.com/help/request-and-grant-emergency-access/#2-the-trusted-contacts-request-is-approved-or-denied/)by the account holder or after the wait time expires.
4. The [trusted contact accesses the account](https://bitwarden.com/help/request-and-grant-emergency-access/#3-if-approved-the-trusted-contact-gets-access-by-viewing-the-vault-or-updating-the-master-password-to-log-in-to-the-account/).
5. (Optional) The account holder [revokes the trusted contact's access](https://bitwarden.com/help/request-and-grant-emergency-access/#manage-a-trusted-emergency-contacts-access/) to their account.

## Who can use emergency access

[Adding a trusted contact](https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts/) for emergency access is available to premium users, including members of paid organizations (Families, Teams, and Enterprise). If your organization turned on the [Automatic confirmation policy](https://bitwarden.com/help/policies/#automatic-user-confirmation/), emergency access is **not** available for your account.

Anyone with a free or premium Bitwarden account on the same [Bitwarden server](https://bitwarden.com/help/server-geographies/) can be designated as a trusted emergency contact. There is no limit to the number of trusted emergency contacts a premium user can have.

> [!TIP] Account recovery instead of emergency access
> If you're an organization administrator, [account recovery](https://bitwarden.com/help/account-recovery/) may be a better fit for managing employee account access during offboarding or succession planning.

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

## Next steps

- [Add trusted emergency contacts](https://bitwarden.com/help/add-and-manage-trusted-emergency-contacts/) to your account.
- Share with your trusted contacts [how to request access](https://bitwarden.com/help/request-and-grant-emergency-access/#1-the-trusted-contact-requests-access-to-the-account/), should the need arise.
- Learn how to [handle emergency access requests](https://bitwarden.com/help/request-and-grant-emergency-access/#approve-or-deny-an-emergency-access-request/) to your account.
