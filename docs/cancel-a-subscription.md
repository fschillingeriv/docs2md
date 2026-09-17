---
URL: https://bitwarden.com/help/cancel-a-subscription/
---

# Cancel a Subscription

Bitwarden subscriptions renew automatically so you don't lose access to paid features. If you cancel automatic renewal, you can continue using your subscription until the end of your current billing cycle. After your subscription ends, you'll lose access to paid features, but your [account or organization won't be deleted](https://bitwarden.com/help/delete-your-account/). If your subscription is less than 30 days old, [contact us](https://bitwarden.com/contact/) for a refund.

> [!NOTE] Self-host cancellation
> If you [self-host Bitwarden](https://bitwarden.com/help/licensing-on-premise/), cancel your subscription from the Bitwarden web app and server where you created the subscription.

## Cancel a personal subscription

To cancel a personal subscription:

1. In the web app, go to **Settings** → **Subscription**:

![Subscription page](https://bitwarden.com/assets/3Ru9TSLguhRNYtLe2TLwXk/bec6794eb58efa8780504720d4acb250/2026-03-03_10-24-17.png)
*Subscription page*
2. Take note of the **Next charge**date. This is when you will lose access to paid features once your subscription is cancelled.
3. Select **Cancel subscription**.

### After personal cancellation

> [!NOTE] Bitwarden refunds 
> If you cancel a premium subscription **within 30 days of the its creation**, contact us for a refund. Subscriptions older than 30 days are not eligible for a refund.

When you confirm cancellation, your account will move into a **Pending cancellation**status until the noted **Next charge**date is reached.

> [!TIP] Reinstate Sub
> If you change your mind before the end of the billing cycle, select **Reinstate subscription**on the same page to turn the renewal back on.

When the **Next charge**date is reached, your account will revert to a free individual plan and you'll lose access to all [paid features](https://bitwarden.com/pricing/). The free plan also changes access to these specific features:

- **Two-step login**: You will **not** be locked out of your vault, however you will not be able to use advanced [two-step login options](https://bitwarden.com/help/setup-two-step-login/) such as Yubikey or Duo for authentication. Your secret keys will remain stored in vault items in the **Authenticator Key (TOTP)** field, however Bitwarden will not generate TOTP codes.

 - If you have a core two-step login option enabled (authenticator app or email), you will be prompted to use the enabled option.
 - If you do not have another two-step login option enabled, you will authenticate into your vault without two-step login.
- **Encrypted file attachments**: [Attachments](https://bitwarden.com/help/attachments/) will **not** be deleted from your vault. You will not, however, be able to download saved attachments or upload new ones.
- **Emergency access**: [Trusted emergency contacts](https://bitwarden.com/help/emergency-access/) will still be able to request and obtain access to your vault. As the account holder, however, you will not be able to add new or edit existing trusted emergency contacts.

## Cancel an organization subscription

To cancel an organization subscription you must be an [organization owner](https://bitwarden.com/help/user-types-access-control/):

1. In the web app, open the Admin Console and go to **Billing**→ **Subscription**:

![Organization subscription ](https://bitwarden.com/assets/7MT9lfZZDTOQOBmnrLGceN/1ac8c615153e35250d15ce3921148cfe/2024-12-04_10-33-12.png)
*Organization subscription *
2. Take note of the **Subscription expiration**date. This is when your organization will lose access to [paid features](https://bitwarden.com/pricing/) once your subscription is cancelled.
3. Scroll down and select **Cancel subscription**.

### After organization cancellation

When you confirm cancellation, your organization will move into a **Pending cancellation**status until the noted **Subscription expiration**date is reached.

> [!TIP] Reinstate Sub
> If you change your mind before the end of the billing cycle, select **Reinstate subscription**on the same page to turn the renewal back on.

When the **Next charge**date is reached, your account will revert to a free individual plan and your organization will move to a **Disabled** state. Your organization will lose access to all [paid features](https://bitwarden.com/pricing/) and a few important things to note are:

- **Organization members**: Existing members and groups **will not** be removed from the organization. If for any reason you'd like to reinstate your subscription, members will not need to take action to regain access.
- **Premium features**: All members of the organization will lose access to premium features while your your organization is disabled, as described in the **After personal cancellation** section of this page.
- **Organization-owned items**: Organization-owned items and collections **will not**be deleted. Organization owners will retain access to organization-owned vault items, but all other members will lose access to shared items while your organization is disabled.
