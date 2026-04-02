---
URL: https://bitwarden.com/help/lost-two-step-device/
---

# Can't Access Two-Step Login

[Two-step login methods](https://bitwarden.com/help/setup-two-step-login/) protect your account, but losing your authentication device, like a phone with an authenticator app or linked email inbox, can lock you out of your Bitwarden vault. If you lose your two-step authentication method, recovery options are limited. Regaining access largely depends on if you or your company administrator previously prepared for this potential situation.

## Possible recovery methods

Try the following options to see if you can reset your two-step login method or [export your vault](https://bitwarden.com/help/export-your-data/) before creating a new account.

> [!NOTE] Account recovery doesn't remove 2FA
> [Account recovery](https://bitwarden.com/help/account-recovery/) does not bypass or turn off two-step authentication.

### Alternate two-step login method

If you set up more than one two-step login method, try another one. When on the login screen, select **Use another two-step login method**.

### Recovery code

You can [use your recovery code](https://bitwarden.com/help/two-step-recovery-code/#use-your-recovery-code/) to access your account if you saved it before being locked out. Recovery codes are generated when you set up any two-step login method, and you must proactively save the code somewhere that you can find it outside of your vault. Bitwarden is unable to retrieve the recovery code on your behalf.

A recovery code looks like this when you retrieve it from your account’s security settings:

![Example recovery code](https://bitwarden.com/assets/64piqJsX7vN25To16iRFIp/09e977fae9485c0764f832c6bb4b4b04/2024-12-02_11-24-35.png)
*Example recovery code*

> [!NOTE] Recovery Codes + Duo for Orgs
> Recovery codes will not deactivate Duo for organizations. If you are locked out of your vault by an organizational Duo prompt, reach out to the Duo administrator at your company for help bypassing the prompt.
> 
> If you're not sure whether the Duo prompt is setup personally or by your organization, try selecting **Use another two-step login method**.

### Trusted emergency contact

If you designated a [trusted emergency contact](https://bitwarden.com/help/emergency-access/) with takeover access, ask them to [initiate emergency access](https://bitwarden.com/help/emergency-access/#use-emergency-access/). After the **Wait time** set for that emergency contact passes, all two-step login methods are turned off and the emergency contact can change the master password.

### Duo bypass code

If your Bitwarden account is connected to Duo, ask your company's Duo administrator to generate a [bypass code](https://duo.com/docs/administration-users#generating-a-bypass-code). This temporary code will authenticate your Duo credentials, allowing you to log in to Bitwarden.

### Other device or Bitwarden app

Check all your devices to see if you're already logged in to any Bitwarden client, like the mobile app, browser extension, or desktop app.

- If you’re logged in to the web app, retrieve and then [use your recovery code](https://bitwarden.com/help/two-step-recovery-code/#use-your-recovery-code/) to disconnect all two-step login methods.
- If you’re logged in to any other Bitwarden app, [export your vault](https://bitwarden.com/help/export-your-data/), create a new account, and [import your data](https://bitwarden.com/help/import-data/) there. After confirming that your data was imported correctly, log out of the old account and consider [deleting](https://bitwarden.com/help/delete-your-account/) it.

## When recovery methods don’t work

We recommend double-checking all your devices and browsers for any logged in Bitwarden sessions. If you find one, that’s your last opportunity to [export vault data](https://bitwarden.com/help/export-your-data/). 

If none of these options grant you access to your account, there is no way for Bitwarden to recover the account or its data. You will need to [delete your account](https://bitwarden.com/help/delete-your-account/#tab-without-logging-in-4KcOdFa6zVp6H7xo9Ui9vc/) and create a new one. If you delete a Bitwarden account that has a premium subscription, [contact us](https://bitwarden.com/contact/) and we'll apply your existing subscription to the new account.
