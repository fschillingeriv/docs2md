---
URL: https://bitwarden.com/help/list-of-emails/
---

# Emails from Bitwarden Servers

This article describes the automated emails that will be sent from `no-reply@bitwarden.com` or `.eu` to organization members, including owners, admins, and end-users, as well as individual users.

Emails in this article are organized by who will receive them as well as by criticality. **Whether an email is considered critical in an organization context may depend on your organization's particular deployment or requirements.**

## Organization emails

### Critical administrative emails

The following emails alert owners and admins of Bitwarden organizations to critical changes or action items related to their organization:

| Subject line | Variable | Description |
|------|------|------|
| Your Subscription Will Renew Soon | n/a | The billing email for an organization receives this email when their organization subscription is [approaching a renewal date](https://bitwarden.com/help/organization-renewal/). |
| {Organization} Seat Count Has Increased | {Organization} = Your organization's display name. | All owners receive this email when their [organization seat count autoscales](https://bitwarden.com/help/managing-users/#user-seats/). |
| {Organization} Seat Limit Reached | {Organization} = Your organization's display name. | All owners receive this email when the number of their organization's members matches their [seat limit](https://bitwarden.com/help/managing-users/#set-a-seat-limit/). |
| Domain not claimed | n/a | All owners and admins receive this email when an [attempt to claim a domain for their organization was not successful](https://bitwarden.com/help/claimed-domains/). |
| Action Required: {User} Needs to be Confirmed | {User} = A user's email address. | All owners and admins receive this email when a user is waiting to be [confirmed to join the organization.](https://bitwarden.com/help/managing-users/#confirm/) |
| Review SSO login request for new device | n/a | All owners and admins receive this email when a user is waiting for a [trusted device to be approved](https://bitwarden.com/help/approve-a-trusted-device/). |
| Request to Delete Your Organization | n/a | An owner receives this email if they have requested deletion of their organization from Bitwarden support. This email will only be sent to a valid owner who has confirmed with Bitwarden support that organization deletion can be initiated. |

### Critical member emails

The following emails alert members of Bitwarden organizations, in all roles, to critical changes or action items related to their account: 

| Subject line | Variable | Description |
|------|------|------|
| {Organization} invited you to their Bitwarden organization. | {Organization} = Your organization's display name. | A user receives this email when they are invited to join an organization, **if** they have an existing Bitwarden account. |
| {Organization} set up a Bitwarden account for you. | {Organization} = Your organization's display name. | A user receives this email when they are invited to join an organization, **if** they do not have an existing Bitwarden account. |
| You have been revoked from {Organization} | {Organization} = Your organization's display name. | A user receives this email when their access is revoked due to violation of the [Require two-step login](https://bitwarden.com/help/policies/#require-two-step-login/) or [Single organization](https://bitwarden.com/help/policies/#single-organization/) policies. |
| Your admin has initiated account recovery | n/a | A user receives this email when an administrator has [initiated account recovery on their account](https://bitwarden.com/help/account-recovery/#recover-an-account/). |
| Login request approved | n/a | A user receives this email when a trusted device [login request is approved by an administrator](https://bitwarden.com/help/add-a-trusted-device/). |
| Important update to your Bitwarden account | n/a | A user receives this email when their account is [claimed by an organization they are a member of](https://bitwarden.com/help/claimed-accounts/). |
| {Organization} has identified 1 at-risk password {Organization} has identified {#) at-risk passwords | {Organization} = Your organization's display name. {#} = The number of at-risk passwords. | A user receives this email when an administrator initiates a [change password request](https://bitwarden.com/help/access-intelligence/#requesting-password-changes/). |

### Critical Secrets Manager emails

The following emails alert owners of Bitwarden organizations to critical changes or action items related to their use of Secrets Manager:

| Subject | Variable | Description |
|------|------|------|
| {Organization} Secrets Manager Seat Limit Reached | {Organization} = Your organization's display name. | All owners receive this email when the number of users in an organization [assigned to Secrets Manager matches its seat limit](https://bitwarden.com/help/secrets-manager-quick-start/#user-seats-and-machine-account-scaling/). |
| {Organization} Secrets Manager Machine Accounts Limit Reached | {Organization} = Your organization's display name. | All owners receive this email when the number of [machine accounts created in an organization matches its machine account limit](https://bitwarden.com/help/secrets-manager-quick-start/#user-seats-and-machine-account-scaling/). |

### Non-critical organization emails

The following emails alert members of Bitwarden organizations, in all roles, to non-critical changes or actions items related to their account or organization:

| Subject line | Variable | Description |
|------|------|------|
| You can now access items from {Organization} | {Organization} = Your organization's display name. | A user receives this email when their access to the organization is confirmed. |
| Access Requested for Secrets Manager | n/a | An admin or owner receives this email when a user has requested access to [Secrets Manager](https://bitwarden.com/help/secrets-manager-overview/). |
| Accept Your Free Families Subscription | n/a | A user receives this email when a member of an organization invited them to [create a sponsored Families organization](https://bitwarden.com/help/families-for-enterprise/). |
| Success! Families Subscription Accepted | n/a | A user receives this email when they've redeemed an invitation to [create a sponsored Families organization](https://bitwarden.com/help/families-for-enterprise/). |
| Your Families Sponsorship was Removed | n/a | A user receives this email when they've manually removed [sponsorship for a Families organization](https://bitwarden.com/help/families-for-enterprise/). |
| Removal of Free Bitwarden Families plan | n/a | A user receives this email when sponsorship for a Families organization has been [removed by an administrator, typically by activating a policy](https://bitwarden.com/help/policies/#remove-free-bitwarden-families-sponsorship/). |

### Free or Families organization emails

The following emails alert members of specifically **Free** or **Families** Bitwarden organizations, in all roles, to critical changes or action items related to their account:

| Subject line | Variable | Description |
|------|------|------|
| {Organization} invited you to their Bitwarden organization. | {Organization} = Your organization's display name. | A user receives this email when they are invited to join an organization, **if** they have an existing Bitwarden account. (FAM) |
| {Organization} set up a Bitwarden account for you. | {Organization} = Your organization's display name. | A user receives this email when they are invited to join an organization, **if** they do not have an existing Bitwarden account. (FAM) |
| You have been invited to a Bitwarden Organization. | n/a | A user receives this email when they are invited to join a **free** organization, **if** they have an existing Bitwarden account. |
| You have been invited to Bitwarden Password Manager. | n/a | A user receives this email when they are invited to join a **free** organization, **if** they do not have an existing Bitwarden account. |

## Provider & business unit emails

The following emails alert provider and business unit admins to any changes or action items relevant to their provider or business unit:

| Subject line | Variable | Description |
|------|------|------|
| Create a Provider | n/a | A provider admin receives this email when they are [registered to create a provider](https://bitwarden.com/help/getting-started-providers/#start-a-provider/). |
| Set Up Business Unit | n/a | A business unit admin receives this email when they are registered to create a [business unit](https://bitwarden.com/help/business-unit-portal/). |
| Join {Provider/Business Unit} | {Provider/Business Unit} = Your provider's display name. | A user receives this email when they are [invited to join a provider](https://bitwarden.com/help/provider-users/#invite/) or business unit. |
| You Have Been Confirmed To {Provider/Business Unit} | {Provider/Business Unit} = Your provider's display name. | A user receives this email when their [access to a provider or business unit is confirmed](https://bitwarden.com/help/provider-users/#confirm/). |
| You Have Been Removed from {Provider/Business Unit} | {Provider/Business Unit} = Your provider's display name. | A user receives this email when their [access to a provider or business unit is removed](https://bitwarden.com/help/provider-users/#deprovision-users/). |
| Update your billing information | n/a | A client organization owner receives this email if their organization is removed from provider management and must add a billing method. |
| Request to Delete Your Provider | n/a | An owner receives this email if they have requested deletion of their organization from Bitwarden support. |

## Self-hosting emails

The following emails alert administrators of self-hosted Bitwarden deployments of changes or action items related to their server:

| Subject line | Variable | Description |
|------|------|------|
| License Expired | n/a | An owner receives this email when the [license file for their self-hosted server](https://bitwarden.com/help/licensing-on-premise/) has exceeded its 60-day [grace period after expiration](https://bitwarden.com/help/organization-renewal/). |
| [Admin] Continue Logging In | n/a | An administrator receives this email while logging in to the [System Administrator Portal](https://bitwarden.com/help/system-administrator-portal/). |

## Widely-applicable emails

The following emails alert Bitwarden users, including members of organizations in any role and individual users, of changes or action items related to their account:

| Subject line | Variable | Description |
|------|------|------|
| Verify Your Email | n/a | A user receives this email during independent account creation. |
| Your Email Change | n/a | A user receives this email when a request to change their account email address is initiated. |
| Your Master Password Hint | n/a | A user receives this email when they've requested a [master password hint](https://bitwarden.com/help/master-password/) during login. |
| Master Password Has Been Changed | n/a | A user receives this email when their master password is changed. |
| Your Bitwarden Verification Code | n/a | A user receives this email when logging in if they need to input [email-based two-step login](https://bitwarden.com/help/setup-two-step-login-email/#use-email-verification/) or [verify a new device](https://bitwarden.com/help/new-device-verification/). |
| New Device Logged In From {Device} | {Device} = Device type, for example "Chrome Extension", "Windows", or "iOS". | A user receives this email when their account is logged into from a new device. |
| Failed login attempts detected | n/a | A user receives this email when several attempts to log in to their Bitwarden account fail. |
| Recover 2FA From {IP} | {IP} = An IP address. | A user receives this email when a two-step login [recovery code is used to deactivate 2FA](https://bitwarden.com/help/two-step-recovery-code/#use-your-recovery-code/). |
| Delete Your Account | n/a | A user receives this email when [deletion of their account has been requested](https://bitwarden.com/help/delete-your-account/#delete-a-personal-account/). |
| Payment Failed | n/a | A user receives this email when the payment method attached to their subscription has failed on renewal. |
| Account Credit Payment Processed | n/a | A user receives this email when account credit is processed toward a subscription renewal. |
| Welcome to Bitwarden! | n/a | A user receives this email when they create a new Bitwarden account. |
| Emergency Access Contact Invite | n/a | A user receives this email when they are [invited to be an emergency contact for another user](https://bitwarden.com/help/emergency-access/#add-trusted-emergency-contacts/). |
| Accepted Emergency Access | n/a | A user receives this email when another user has [accepted an invitation to become an emergency contact](https://bitwarden.com/help/emergency-access/#add-trusted-emergency-contacts/). |
| You Have Been Confirmed as Emergency Access Contact | n/a | A user receives this email when they are [confirmed as an emergency contact for another user](https://bitwarden.com/help/emergency-access/#add-trusted-emergency-contacts/). |
| Emergency Access Initiated | n/a | A user receives this email when a emergency contact [requests access to their account](https://bitwarden.com/help/emergency-access/#use-emergency-access/). |
| Emergency Access Approved | n/a | A user receives this email when their [request for emergency access to another's account is approved](https://bitwarden.com/help/emergency-access/#use-emergency-access/). |
| Emergency Access Rejected | n/a | A user receives this email when their [request for emergency access to another's account is rejected](https://bitwarden.com/help/emergency-access/#use-emergency-access/). |
| Pending Emergency Access Request | n/a | A user receives this email when an [initiated emergency access request is still pending](https://bitwarden.com/help/emergency-access/#use-emergency-access/) after a certain amount of time. |
| Emergency Access Granted | n/a | A user receives this email when access to their account [has been granted to an emergency contact](https://bitwarden.com/help/emergency-access/#use-emergency-access/). |
