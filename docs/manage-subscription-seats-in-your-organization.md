---
URL: https://bitwarden.com/help/manage-subscription-seats-in-your-organization/
---

# Manage Subscription Seats in Your Organization

A user seat is the billed license for one user within a Bitwarden organization. When a user is invited to your organization, they occupy one user seat and are granted access to Bitwarden features under your specific plan. The total number of user seats represents how many users can join your organization. As such, user seats are not permanently attached to a specific member.

> [!NOTE] Different user provisioning methods
> This article discusses only one of the available methods to invite users and manage your subscription’s seat count:
> 
> - All organizations can [manually invite users](https://bitwarden.com/help/managing-users/) and update the [seat count](https://bitwarden.com/help/manage-subscription-seats-in-your-organization/).
> - Teams and Enterprise organizations can use [SCIM](https://bitwarden.com/help/about-scim/).
> - Teams and Enterprise organizations can use [Directory Connector](https://bitwarden.com/help/directory-sync/).
> - Enterprise organizations can use [just-in-time (JIT)](https://bitwarden.com/help/jit-provisioning/).

## User seat billing

Only an [organization owner](https://bitwarden.com/help/user-types-access-control/#default-roles/) or [provider service user](https://bitwarden.com/help/provider-users/#provider-user-types/) can add or remove seats because it directly affects the organization’s billing subscription.

To check how many user seats your team already includes, open the Admin Console and go to **Billing** → **Subscription**. Your organization’s seat total is listed within **Subscription seats**:

![Set Subscription seats](https://bitwarden.com/assets/6IiAvwCX2KbCTUAbAnY4yV/81614bb5a44c64cdc387ba9cee5663eb/Set_Subscription_seats.png)
*Set Subscription seats*

If the number of user seats is higher than your organization’s total [active users](https://bitwarden.com/help/managing-users/#manage-existing-members/), then that means there are unassigned user seats. Unassigned user seats are still billed, so you may want to invite more people or [remove the extra user seats](https://bitwarden.com/help/managing-users/#manually-add-or-remove-seats/) from your subscription.

> [!NOTE] Removing a user different from reducing seat count
> [Removing a user](https://bitwarden.com/help/remove-users/) from your organization does not automatically reduce your organization’s billed subscription seats. You still need to reduce the seat count.

### Billing for new user seats

When new users are [invited](https://bitwarden.com/help/managing-users/#invite/), Bitwarden cloud [Teams and Enterprise organizations](https://bitwarden.com/help/about-organizations/#types-of-organizations/) will **automatically increase** the number of billed user seats. You can set a [seat limit](https://bitwarden.com/help/manage-subscription-seats-in-your-organization/#set-a-seat-limit/) to prevent your seat count from exceeding a specified number or [manually add seats](https://bitwarden.com/help/managing-users/#manually-add-or-remove-seats/) as desired.

When you add seats in the middle of your billing cycle, you are only charged for the remaining time. If you're on a **monthly plan**, that prorated amount is added to your next scheduled renewal.

For **annual subscriptions**, new seats added mid-cycle are billed on a prorated basis. The prorated amount is charged to the payment method on file on the same day of the month as your renewal date. On your next annual renewal date, all of your seats are billed together for the full year.

For example, if your plan renews on July 15th and you add a seat on May 1st, you'll be charged on May 15th for the prorated remainder of the current period (May 1–July 14). When your annual renewal occurs on July 15th, all seats are consolidated into a single yearly charge.

### Credit for removed user seats

Regardless of how you add seats, you must [manually remove](https://bitwarden.com/help/managing-users/#manually-add-or-remove-seats/) user seats you no longer want from your subscription. Removing seats will cause your next charge to be adjusted so that you are **credited for time not used** by the already-paid-for seat.

### Self-hosted billing

The number of seats a self-hosted organization has will always mirror its [counterpart cloud-organization](https://bitwarden.com/help/self-host-an-organization/#step-3-start-your-organization/). This means self-hosted organizations **do not** automatically scale users. Instead, you must use the cloud Admin Console to manage your seat count.

To quickly reflect changes to your seat count made in the cloud Admin Console, you can set up [billing sync](https://bitwarden.com/help/licensing-on-premise/#tab-automatic-sync-4cDnzGHwlfBQEFs6eqrkut/). This will remove the need to [re-upload your license](https://bitwarden.com/help/licensing-on-premise/#tab-manual-update-4cDnzGHwlfBQEFs6eqrkut/).

## Manually add or remove seats

To manually add or remove seats to your organization:

1. Log in to the Bitwarden web app and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
*Product switcher*
2. Go to **Billing** → **Subscription**.
3. Enter the total number of user seats that you want in **Subscription seats**:

![Set Subscription seats](https://bitwarden.com/assets/6IiAvwCX2KbCTUAbAnY4yV/81614bb5a44c64cdc387ba9cee5663eb/Set_Subscription_seats.png)
*Set Subscription seats*
4. Select **Save**.

> [!NOTE] Can't invite more when limit reached
> If **Limit subscription** is checked, then the number in **Subscription seats** must be equal to or lower than your seat limit. If you need to add more user seats, increase the **Seat Limit**.

## Set a seat limit

You have the option to control subscription costs by setting a cap on the number of user seats that can be added to your organization. Once the specified limit is reached, you will not be able to invite new users unless you increase that limit.

To set a limit on the number of seats your organization can automatically scale up to:

1. Log in to the Bitwarden web app and open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
*Product switcher*
2. Go to **Billing** → **Subscription**.
3. Check **Limit subscription (optional)**.
4. Enter the maximum number of user seats you want to allow in **Seat limit (optional)**:

![Set Seat limit ](https://bitwarden.com/assets/5DBnJW1y9welOF6hrDKrrh/06cade0656921a06d5bc43d3b9d26a62/Set_Seat_limit.png)
*Set Seat limit *
5. Select **Save**.
