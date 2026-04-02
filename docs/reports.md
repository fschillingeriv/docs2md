---
URL: https://bitwarden.com/help/reports/
---

# Vault Health Reports

Vault health reports can help you evaluate the security of your Bitwarden individual or organization vault. Reports, for example the Reused Passwords and Weak Passwords report, are run locally on your client. This allows offending items to be identified, without Bitwarden ever having access to unencrypted versions of this data.

> [!NOTE] health report 
> Most vault health reports are only available for premium users, including members of paid organizations (families, teams, or enterprise), but the [Data Breach report](https://bitwarden.com/help/reports/#data-breach-individual-vaults-only/) is free for all users.

## View a report

To run any vault health report for your **individual vault**:

1. Log in to the web app and select **Reports**from the navigation:

![Reports page](https://bitwarden.com/assets/JcoKvP7eLrZHUEKmjTqgc/0213680bf5546cfc7df498d9931c8d2f/2024-12-02_16-29-59.png)
2. Select a report to run.

To run any vault health report for your **organization vault**:

1. Log in to the Bitwarden web app.
2. Open the Admin Console using the product switcher:

![Product switcher](https://bitwarden.com/assets/2uxBDdQa6lu0IgIEfcwMPP/e3de3361749b6496155e25edcfdcf08b/2024-12-02_11-19-56.png)
3. In your organization, select **Reporting** → **Reports** from the navigation:

![Organization reports ](https://bitwarden.com/assets/5POQmt3TrEgfFzRNwHancg/9a67882a07d8894747ebb5bc3bbdcaae/2024-12-02_16-31-14.png)
4. Select a report to run.

## Available reports

### Exposed Passwords

The Exposed Passwords report will identify passwords that have been uncovered in known data breaches that were released publicly or sold on the dark web by hackers.

This report uses a trusted web service to search the first five digits of the hash of all your passwords in a database of known leaked passwords. The returned matching list of hashes is then locally compared with the full hash of your passwords. That comparison is only done locally to preserve your [k-anonymity](https://en.wikipedia.org/wiki/K-anonymity).

Once identified, you should create a new password for offending accounts or services.

> [!NOTE] five digit password hash
> Why use the first five digits of password hashes?
> 
> If the report was performed with your actual passwords, it doesn't matter if they were exposed or not; you would be voluntarily leaking it to the service. This report’s result may not mean your account has been compromised, rather that you are using a password that has been found in these databases of exposed passwords. Nevertheless, we highly recommend not using leaked and non-unique passwords.

### Reused Passwords

The Reused Passwords report identifies non-unique passwords in your vault. Reusing the same password for multiple services can allow hackers to easily gain access to more of your online accounts when one service is breached.

Once identified, you should create a unique password for offending accounts or services.

### Weak Passwords

The Weak Passwords report identifies weak passwords that can easily be guessed by hackers and automated tools that are used to crack passwords, sorted by severity of the weakness. This report uses [zxcvbn](https://dropbox.tech/security/zxcvbn-realistic-password-strength-estimation) for password strength analysis.

Once identified, you should use the Bitwarden password generator to create a strong password for offending accounts or services.

### Unsecured Websites

The Unsecured Websites report identifies login items that use unsecured (`http://`) schemes in URIs. It's much safer to use `https://` to encrypt communications with TLS/SSL. To learn more, see [using URIs](https://bitwarden.com/help/uri-match-detection/).

Once identified, you should change offending URIs from `http://` to `https://`.

### Inactive 2FA

The Inactive 2FA report identifies login items where:

- Two-factor authentication (2FA) via TOTP is available from the service
- You have not stored a TOTP authenticator key

Two-factor authentication (2FA) is an important security step that helps secure your accounts. If any website offers it, you should always enable 2FA. Offending items are identified by cross-referencing URI-data with data from [https://2fa.directory/](https://2fa.directory/).

Once identified, setup 2FA using the `Instructions` hyperlink for each offending item:

![Report Instructions](https://bitwarden.com/assets/3USpBf7beuGcdJvMhDrwNI/570672e3220f09e0398ced33a154b1ea/inactive-2fa.png)

### Member access

The Member access report shows the total number of **Groups**, **Collections**, and **Items** each user can access:

![Member access report](https://bitwarden.com/assets/4oNfzpIcDwn2XjUgG0lPG3/a51bac815082055fdd6f47a40937b72d/2024-09-10_16-13-31.png)

To locate a specific person, enter their email into the **Search members** field. Select the neighboring [sign-in] **Export icon** to download a `.csv` that details per member:

- Basic account details, including their **Name** and if **Two-Step Login** or **Account Recovery** is turned on
- Their **Group** assignments
- Which **Collections** they can access and at what [**Collection Permissions**](https://bitwarden.com/help/collection-permissions/) level
- The sum **Total Items** that the member can access

> [!TIP] Member list export
> You can also download a .`.csv` [list of members](https://bitwarden.com/help/managing-users/#download-list-of-members/) that includes account-specific details, like whether Secrets Manager is activated and their status in the organization.

### Data Breach (individual vaults only)

The Data Breach report identifies compromised data (email addresses, passwords, credit cards, DoB, and more) in known breaches, using a service called Have I Been Pwned (HIBP).

When you create a Bitwarden account, you'll have the option to run this report on your master password before deciding to use it. To run this report, the first five digits of a hash of your master password is sent to HIBP and compared to stored exposed hashes. Your master password itself is never exposed by Bitwarden.

A “breach” is defined by HIBP as "an incident where data is inadvertently exposed in a vulnerable system, usually due to insufficient access controls or security weaknesses in the software". For more information, refer to [HIBP's FAQs documentation](https://haveibeenpwned.com/FAQs).

> [!NOTE] Self-hosting reports 
> If you are self-hosting Bitwarden, in order to run the data breach report in your instance you will need to buy an HIBP subscription key that will authorize you to make calls to the API, obtained [here](https://haveibeenpwned.com/API/Key).
> 
> Once you have the key, open your `./bwdata/env/global.override.env` and REPLACE the placeholders value for `globalSettings__hibpApiKey` with your purchased API key:
> 
> 
> ```
> globalSettings__hibpApiKey=REPLACE
> ```
> 
> For more information, see [configure environment variables](https://bitwarden.com/help/environment-variables/).
