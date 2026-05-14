---
URL: https://bitwarden.com/help/billing-faqs/
---

# Billing FAQs

This article contains frequently asked questions (FAQs) regarding **Plans and Pricing**.

For help selecting the right Bitwarden plan for you, refer to [what plan is right for me?](https://bitwarden.com/help/what-plan-is-right-for-me/) and [about Bitwarden plans](https://bitwarden.com/help/password-manager-plans/).

## Account management

### Q: How do I upgrade from an individual subscription to an organization?

**A:** Use [Upgrade from Individual to Organization](https://bitwarden.com/help/upgrade-from-individual-to-org/) to guide you through this process.

### Q: How do subscriptions work for self-hosting?

**A:** In order to use a subscription on a self-hosted server first create an account and subscription in the Bitwarden cloud via the [web app](https://bitwarden.com/help/getting-started-webvault/). From there, download the [subscription license](https://bitwarden.com/help/licensing-on-premise/#organization-license/), which will flag access to premium or organization features, to apply to your self-hosted server.

Per the Bitwarden terms of service, one organization deployment is permitted per subscription.

### Q: If I have a families organization, do I need premium?

**A:** The current families plan (introduced Sep. 2020) automatically provides premium features for all six members of the organization, so no!

### Q: Why do my license expiration dates on cloud and self-hosted not match?

**A**: To ensure that you don't inadvertently lose organization functionality, we provide a 2 month grace period between the expiration of the license on cloud and expiration of the license on your self-hosted server. Learn more [here](https://bitwarden.com/help/organization-renewal/).

## Payment options

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
