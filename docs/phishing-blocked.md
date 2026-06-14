---
URL: https://bitwarden.com/help/phishing-blocked/
---

# Phishing Blocker

Bitwarden phishing blocker detects known phishing websites and redirects Bitwarden users to a secure notification page, helping to ensure that credentials are not mistakenly entered or compromised. Phishing blocker identifies phishing websites using the regularly updated, open source [Phishing.Database](https://github.com/Phishing-Database/Phishing.Database).

Phishing blocker is available for Bitwarden individual Premium and Families plans on browser clients `2026.1.1` and newer.

> [!NOTE] Phishing blocker unavailable for Safari
> At this time, phishing blocker is not available on the Bitwarden browser extension for Safari.

## Phishing blocker

Phishing blocker operates using the browser extension. When phishing blocker identifies a known phishing website: 

1. Instead of loading a known phishing website, Bitwarden will redirect the user to a warning page, indicating that the site has been blocked.

![Phishing blocker](https://bitwarden.com/assets/7IDSIId3ZA7nRT1T8gdX1T/3382ba87ffa5a38d8fa68b03d4ea0dcc/Phiishing-blocker-cropped.png)
2. Select the appropriate option:

 - **Close tab**: Selecting this option will close out the malicious tab that Bitwarden has blocked.
 - **Continue**: Selecting this option will allow you to continue to the website and close the Bitwarden phishing blocker.

> [!NOTE] Continue to phishing website warning
> Selecting **Continue** will proceed to the website that was identified for previous phishing activity. This action could result in your credentials being compromised. Caution is recommended if selecting this option.

## Toggle phishing blocker

By default, phishing blocker will be enabled for individual premium and families users. You may toggle the feature **on**or **off** in the browser extension by navigating to **Settings** → **Account security** and selecting the toggle:

![Toggle phishing blocker](https://bitwarden.com/assets/4jeEBHYQeUpsZNOoKKUeW1/d19fe64cfed2edba32983f45c5434490/phishing_setting.png)
*Toggle phishing blocker*

## How it works

Bitwarden phishing blocker uses the Phishing.Database to reference known phishing sites. This open source tool is updated daily by users to identify harmful URLs.

> [!NOTE] Phishing blocker performs checks local
> All website checks are performed locally by the Bitwarden browser extension. No data is ever shared with Bitwarden or third parties.

1. The Bitwarden browser extension fetches the list from Phishing.Database directly.
2. The Bitwarden API uses the SHA-256 checksum to identify changes in the list and fetch updated lists.
3. Using the browser extension, Bitwarden will check URLS against the phishing list on page load.
4. If the site is a match with a known threat on the phishing database, Bitwarden will take you to a blocked screen, providing the options to leave the site or continue.
