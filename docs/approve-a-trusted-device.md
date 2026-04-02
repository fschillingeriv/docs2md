---
URL: https://bitwarden.com/help/approve-a-trusted-device/
---

# Approve a Trusted Device

When a member of your organization logs into a new device, they'll need to [approve, or trust, that device](https://bitwarden.com/help/add-a-trusted-device/). One method for doing so, done by selecting the **Request admin approval**option, involves sending a device approval request to admins and owners within the organization for approval.

![Request admin approval](https://bitwarden.com/assets/5IMJBQOrklcOuLVEpaR6gX/60ead8f10e34f7acd2467eaaa34ff93d/2025-06-16_15-22-15.png)

As an admin, you'll receive an email any time an organization member submits a device approval request. To approve a request, as an organization admin, or owner, or [custom user](https://bitwarden.com/help/user-types-access-control/#custom-role/) with the **Manage account recovery** permission:

1. Log in to the Bitwarden web app and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
2. Select **Settings**→ **Device approvals** from the navigation.
3. Using the options ⋮ menu, select ✓ **Approve request**.

![Approve device request](https://bitwarden.com/assets/1iPurecgskOyt0NGDRidBM/3a85c233b2a208dc2c939c8e79fd9b4f/Screenshot_2024-02-29_at_10.52.50_AM.png)

> [!NOTE] Verify fingerprint
> When a member requests device approval, a fingerprint phrase is displayed on the member's device. Additional verification can be performed by checking that this fingerprint phrase matches the one shown in the member column. This method is optional and **requires synchronous communication** between the requesting member and the administrator.

## Bulk approve requests

Multiple device requests may be approved at one time using the top level options ⋮ menu and selecting ✓ **Approve all requests**.

![Approve or bulk approve device](https://bitwarden.com/assets/4ozBvrFFLPYcRmuCWNCuCz/504a206008a06c4e98d0058478f21d26/TDE_Bulk_Device_sc3.png)

> [!NOTE] Bulk device approval web app warning
> Bulk device approval using the **Approve all requests** option may neglect verification steps that administrators can perform to ensure a request is legitimate, such as checking the user's reported fingerprint phrase.
> 
> Bitwarden recommends that significant security controls such as IdP credential standards, IdP MFA, and IdP device registration and trust be reviewed before enabling and using bulk device approval.

When a device request is approved, the requesting user is sent an email informing them they can continue logging in on that device. The user must take action by logging in to the new device within 12 hours, or the approval will expire.

Unapproved requests will expire after 1 week. You can deny a login attempt by instead selecting [close] **Deny request**, or deny all existing requests by selecting the top-most options ⋮ menu and selecting [close] **Deny all requests**.

[Events](https://bitwarden.com/help/event-logs/) are logged when:

- A user requests a device approval.
- A device request is approved.
- A device request is denied.
