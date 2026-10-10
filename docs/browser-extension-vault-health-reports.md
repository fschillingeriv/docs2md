---
URL: https://bitwarden.com/help/browser-extension-vault-health-reports/
---

# Browser Extension Vault Health Reports

Run vault health reports in the Bitwarden browser extension to find and fix any weak, reused, or exposed logins stored in your Bitwarden vault. Available on Free, Premium, and Families subscriptions, the health reports available in the browser extension check for three types of at-risk passwords:

- [Exposed passwords](https://bitwarden.com/help/reports/#exposed-passwords-report/) have been found in known data breaches.
- [Weak passwords](https://bitwarden.com/help/reports/#weak-passwords-report/) can be easily guessed by hackers or automated tools.
- [Reused passwords](https://bitwarden.com/help/reports/#reused-passwords-report/) are saved in your vault for two or more different login items.

> [!TIP] Access Intelligence instead of health scan
> If you’re a member of a Teams or Enterprise organization, this option will not appear. Instead, learn how [Access Intelligence](https://bitwarden.com/help/access-intelligence/) can help identify at-risk credentials across your organization and notify members to update their passwords.

# Scan vault for password health

Accounts with a Free, Premium, and Families subscription can view how many exposed, weak, and reused passwords are in their vault.

> [!TIP] Password scan, additional vault health reports
> Use the Bitwarden web app to run additional [vault health reports](https://bitwarden.com/help/reports/).

To learn how many passwords saved in your vault are at-risk:

1. Log in to the Bitwarden browser extension.
2. Select **Health**. If this your first time accessing the **Health** tab, select **Scan my vault**:

![Health reports in browser extension](https://bitwarden.com/assets/hjNDZ9phqDhgp0cqCrQdP/0908df3fdaaa5f8bcd5508dc5eed75f2/Health_scan_in_browser_extension.png)
*Health reports in browser extension*

The **Health** tab will display the total number of passwords in your vault that are exposed, weak, or reused:

![Risks identified in health scan](https://bitwarden.com/assets/2N0fLBOMLg1drYnuQlxAbG/f419cccbac162351c10cee9794ad7c3b/Risks_identified_in_health_scan.png)
*Risks identified in health scan*

# View at-risk passwords

If your account is on a Premium or Families subscription, you can review each health report to see which items, if any, need attention.

> [!NOTE] Password scan, Free limitation
> Free subscriptions can only view the total number of at-risk passwords in each report, not which logins are flagged.

To review at-risk passwords:

1. From the **Health** tab, select a vault health report: exposed, weak, or reused.
2. Review the list of at-risk logins:

![At-risk passwords in health reports](https://bitwarden.com/assets/Oye8NAAshoVyyCtrh5KHm/347de476dbbee0ba32916588df670f45/At-risk_passwords_in_health_scan.png)
*At-risk passwords in health reports*
3. (Optional) From this list, you can:

 - Select the item to open the **View login** screen, where you can [edit the item](https://bitwarden.com/help/managing-items/#manage-items/).
 - If the login's website is [saved as a URI](https://bitwarden.com/help/uri-match-detection/#save-uris-in-login-items/), select **Change password** to open the website and update your credentials. Remember to update the login item in your vault with the new password.
 - Select the ⋯ **Options menu** → **Delete item** to [remove the login](https://bitwarden.com/help/managing-items/#delete/) from your vault. Select **Delete** to confirm.

> [!WARNING] Delete login, but account is still at-risk
> Deleting an item only removes it from your vault. It does not change the password on the actual account, so the login remains at-risk if it's still in use.
