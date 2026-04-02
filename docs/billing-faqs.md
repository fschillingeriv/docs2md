---
URL: https://bitwarden.com/help/billing-faqs/
---

# Billing FAQs

This article contains frequently asked questions (FAQs) regarding **Plans and Pricing**.

For help selecting the right Bitwarden plan for you, refer to [what plan is right for me?](https://bitwarden.com/help/what-plan-is-right-for-me/) and [about Bitwarden plans](https://bitwarden.com/help/password-manager-plans/).

## Account management

### Q: How do I find out what subscription plan I'm on?

**A:** Log in to the web app:

- For individual subscriptions, navigate to **Settings**→ **Subscription**. If this screen can't be found, this account is on a free plan. If this screen exists, this account is on a premium plan.
- For organization subscriptions, organization owners can open the Admin Console and navigate to the organization's **Billing** → **Subscription** view. The **Plan** section will log this organization's plan.

### Q: How do I view my billing information?

**A:** Viewing billing information is different depending on whether you are viewing it for an individual or organization subscription. Use [Update your Billing Information](https://bitwarden.com/help/update-billing-info/) to guide you through both processes.

### Q: How do I delete my account?

**A:** We're sad to see you go! Use [Delete your Account](https://bitwarden.com/help/delete-your-account/) to guide you through this process.

### Q: How do I upgrade from an individual subscription to an organization?

**A:** Use [Upgrade from Individual to Organization](https://bitwarden.com/help/upgrade-from-individual-to-org/) to guide you through this process.

### Q: How do I add or remove a user seat from my organization?

**A:** For Teams and enterprise organizations, user seats will be automatically added as you invite new users. You can [specify a limit](https://bitwarden.com/help/managing-users/#set-a-seat-limit/) to prevent your seat count from exceeding a specific number.

To remove user seats, navigate to your organization's **Billing** → **Subscription** screen and use the **Subscription Seats** input to remove seats ([learn more](https://bitwarden.com/help/managing-users/#manually-add-or-remove-seats/)).

Adding and removing user seats will adjust your future billing totals. Adding seats will immediately charge your payment method on file at an adjusted rate so that **you will only pay for the remainder of the billing cycle** (month/year). Removing seats will cause your next charge to be adjusted so that you are **credited for time not used** by the already-paid-for seat.

### Q: How do subscriptions work for self-hosting?

**A:** In order to use a subscription on a self-hosted server first create an account and subscription in the Bitwarden cloud via the [web app](https://bitwarden.com/help/getting-started-webvault/). From there, download the [subscription license](https://bitwarden.com/help/licensing-on-premise/#organization-license/), which will flag access to premium or organization features, to apply to your self-hosted server.

Per the Bitwarden terms of service, one organization deployment is permitted per subscription.

### Q: If I have a families organization, do I need premium?

**A:** The current families plan (introduced Sep. 2020) automatically provides premium features for all six members of the organization, so no!

### Q: Why do my license expiration dates on cloud and self-hosted not match?

**A**: To ensure that you don't inadvertently lose organization functionality, we provide a 2 month grace period between the expiration of the license on cloud and expiration of the license on your self-hosted server. Learn more [here](https://bitwarden.com/help/organization-renewal/).

### Q: What is the holder of my organization's billing email allowed to do?

**A**: The holder of your organization's [billing email](https://bitwarden.com/help/about-organizations/#create-an-organization/) may, by contacting us:

- Add or remove a credit card from the subscription.
- Change the billing email for the organization.
- Inquire about invoices and billing information on-file.
- Swap between a monthly and annual billing cycle (if applicable for your organization).
- Request a plan upgrade, downgrade, cancellation, or seat adjustment.

They **may not** for any reason request deletion of an organization, be given the identity of current organization owners, or request the promotion of any user to an owner.

## Payment options

### Q: What payment options do you accept for customers based in the United States?

**A:** We accept credit/debit cards, PayPal, bank account (ACH), and Bitcoin. For business subscriptions, we also accept wire transfers and corporate checks, with a minimum payment of 500 USD. For more information regarding payment options, please [contact support](https://bitwarden.com/contact/).

### Q: What payment options do you accept for customers outside the United States?

**A:** We accept credit/debit Cards, PayPal, and Bitcoin. For business subscriptions, we also accept international wire transfers and corporate checks, with a minimum payment of 500 USD. For more information regarding payment options, please [contact support](https://bitwarden.com/contact/).

### Q: Can I pay with Bitcoin?

**A:** Yes! Please note, you will need to **Add Credit** using Bitcoin on the **Settings** → **Billing** screen before purchasing the subscription.

### Q: Can I use a Bitwarden Free plan for commercial use?

**A**: Users can utilize Bitwarden clients, with either paid or free accounts, for personal or business purposes as long as they comply with our [Terms of Service](https://bitwarden.com/terms/). 

Bitwarden's license grants a limited, non-exclusive, non-transferable, royalty-free license to use the Commercial Modules solely for internal development and testing in a non-production environment. For more information, refer to the [license](https://github.com/bitwarden/server/blob/main/LICENSE.txt) and [license FAQ](https://github.com/bitwarden/server/blob/main/LICENSE_FAQ.md).

If users do not intend to modify, resell, rent, lease, distribute, sublicense, loan, or otherwise transfer the Commercial Modules to any third party, or create a competing product or service, they can use any of the available clients for business or personal use while respecting our terms of service.

## Known issues

### Q: An error occurs when I try to go premium on Firefox. How do I fix this?

**A:** We have observed some users of Firefox get the following error message when submitting payment information for a Premium subscription:

`You passed an empty string for 'payment_method_data[referrer]'. We assume empty values are an attempt to unset a parameter; however 'payment_method_data[referrer]' cannot be unset. You should remove 'payment_method_data[referrer]' from your request or supply a non-empty value.`

This usually occurs when submitting your payment method is impeded by an installed browser Extension or configured Browser option.

**Open Firefox in a Private Window and try resubmitting.**
