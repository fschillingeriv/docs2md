---
URL: https://bitwarden.com/help/forgot-master-password/
---

# Forgot My Master Password

Bitwarden operates with zero-knowledge encryption. This means that **Bitwarden has no way to access, retrieve, or reset your master password**. There are, however, a few steps you can take to try to regain access to your account:

## Check server geography

Check that you have the correct[ server selected](https://bitwarden.com/help/server-geographies/#choose-your-cloud-server/) when you try to log in. Bitwarden data regions are separate, and your account only exists in the region where it was first created. Selecting your server is necessary before trying the following options. 

![Server geography ](https://bitwarden.com/assets/3H5fN6yR90aKaTg7gaCruo/020b9ca668f037ed1e6450309b4041b4/2025-11-24_15-26-15.png)
*Server geography *

## Use a different Bitwarden app or device

Try logging in from a different device or Bitwarden app, such as the mobile app or browser extension. 

Next, check if you're logged in on another Bitwarden app. If you set up a [PIN](https://bitwarden.com/help/unlock-with-pin/) or [biometrics](https://bitwarden.com/help/biometrics/) on that device:

1. Unlock your vault with the previously set up PIN or biometrics.
2. Copy your data manually from the View item screen and paste the data into a [.csv file](https://bitwarden.com/help/condition-bitwarden-import/#condition-a-csv/) for re-import.
3. Create a new Bitwarden account and [import the .csv of copied data](https://bitwarden.com/help/import-data/) there.

## Review master password hint

Get a master password hint by visiting [https://vault.bitwarden.com/#/hint](https://vault.bitwarden.com/#/hint) or [https://vault.bitwarden.eu/#/hint](https://vault.bitwarden.eu/#/hint). If you have one setup, a hint will be emailed to your inbox. If you don't have a hint setup, you'll get an email reporting this. 

## Use emergency access

If you have [emergency access](https://bitwarden.com/help/emergency-access/) enabled, contact your trusted emergency contact to regain read or takeover access to your account.

## Contact administrator for account recovery

If your organization uses [account recovery](https://bitwarden.com/help/account-recovery/), reach out to your administrator to reset your master password.

## Log in with known device

If the browser you are using has been set up as a known device (has been registered with [Log in with Device](https://bitwarden.com/help/log-in-with-device/)), select Log in with device from the web app and you may approve the request using another application.

![Log in with a device](https://bitwarden.com/assets/7owqaTEe9Bo05wfLRZPhn8/38f1d0334964bb3d98a430b80b9d6b95/2025-09-09_10-03-52.png)
*Log in with a device*

## Log in with passkey

If an encryption-enabled (PRF) [Log in passkey](https://bitwarden.com/help/login-with-passkeys/) has been registered with your Bitwarden account, you can log in with that.

> [!WARNING] Check whether client apps are logged in.
> Deleting your account will delete all individually-owned items stored in it, this will include any saved attachments. 
> 
> Before deleting your account, check to see if you are actively logged in to any Bitwarden mobile apps, browser extensions, or desktop apps. If you are, you should manually catalogue your data so that you can add it back in to the new account.

## If none of these options grant you access to your account

Bitwarden recommends double-checking all your devices and browsers for any logged in Bitwarden sessions.

If none of these options grant you access to your account, there is no way for Bitwarden to recover the account or its data. You will need to [delete your account](https://bitwarden.com/help/delete-your-account/#tab-without-logging-in-4KcOdFa6zVp6H7xo9Ui9vc/) and create a new one. If you delete a Bitwarden account that has a premium subscription, [contact us](https://bitwarden.com/contact/) and we'll apply your existing subscription to the new account.

## Next steps

- If you start a new account, Bitwarden recommends using the [security readiness kit](https://bitwarden.com/resources/bitwarden-security-readiness-kit/) to prepare for events like the forgetting of a master password.
- If you had to delete a Bitwarden account with a premium subscription, please [contact us](https://bitwarden.com/contact/) in order to reapply your existing subscription to the new account.
