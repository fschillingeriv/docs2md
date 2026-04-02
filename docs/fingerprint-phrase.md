---
URL: https://bitwarden.com/help/fingerprint-phrase/
---

# Account Fingerprint Phrase

> [!TIP] Fingerprints aren't biometric fingerprints
> Are you looking to unlock your vault with a fingerprint reader? If so, check out [biometrics](https://bitwarden.com/help/biometrics/) instead.

Each Bitwarden account has a "fingerprint phrase" associated with it. Your account's fingerprint phrase is permanent and composed of five random english words that appear in a specific order, such as: `alligator-transfer-laziness-macaroni-blue`

The fingerprint phrase is an important security feature used to confirm a Bitwarden user's identity during encryption-related processes, like sharing credentials. Validating fingerprint phrases ensures that end-to-end encryption is securely initiated and that the Bitwarden server you are communicating with has not been maliciously tampered with.

## What is my fingerprint phrase used for?

Some Bitwarden procedures, like adding a new user to an organization or confirming a [login with device request](https://bitwarden.com/help/log-in-with-device/), will ask you to verify that the presented fingerprint phrase matches your own or another user's. When a fingerprint phrase is presented during a process, coordinate with the Bitwarden user with a secondary form of communication, like phone or messaging.

## Where can I find my fingerprint phrase?

You can find your account's fingerprint phrase from any Bitwarden client application:

- **Web app**: Settings → My account
- **Desktop apps**: Account → Fingerprint Phrase
- **Browser extensions**: Settings → Account Security → Fingerprint Phrase
- **Mobile apps**: Settings → Account security → Account fingerprint Phrase
- **CLI**: Using the command `bw get fingerprint me`

## Do I need to write down my fingerprint phrase?

Not knowing your fingerprint phrase will never result in you being locked out of your vault, so it's not critical to write down or store your fingerprint phrase in a secure location. Some users, however, may choose to do so.

> [!NOTE] Recovery codes 
> [Recovery codes](https://bitwarden.com/help/two-step-recovery-code/), on the other hand, are used for two-step login and should **always** be stored outside of Bitwarden in a way that makes sense for you. This will ensure that you are not locked out of your account in the event that you [lose your two-step login secondary device](https://bitwarden.com/help/lost-two-step-device/).

## Can I change my fingerprint phrase?

You cannot change your current account's fingerprint phrase. If you wish to create a new fingerprint phrase, you can [delete the account](https://bitwarden.com/help/delete-your-account/) and start a new one to generate a new phrase. 

> [!WARNING] Danger Zone
> Deleting an account is permanent and cannot be undone or restored. To create a backup of your vault data to store in a safe location, [export your vault data](https://bitwarden.com/help/export-your-data/).

Our fingerprint phrases are generated from the [Electronic Frontier Foundation's long word list](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases), which has been "manually checked and [the EFF has] attempted to remove as many profane, insulting, sensitive, or emotionally-charged words as possible."
