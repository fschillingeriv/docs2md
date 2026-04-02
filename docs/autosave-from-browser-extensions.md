---
URL: https://bitwarden.com/help/autosave-from-browser-extensions/
---

# Autosave from Browser Extension

Bitwarden browser extensions offer an array of in-browser notifications that compare your decrypted data with data that you enter into login, registration, and similar web forms. This includes:

- A notification to add an undetected login.
- A notification to update an existing login.
- A notification to save or use passkeys.
- A notification to save a new URI

These notifications are active by default, but can be turned off from the browser extension's **Settings** → **Notifications** menu.

> [!TIP] Block autosave
> You can also block specific sites from triggering autosave notifications from the **Settings** → **Notification** → **Excluded domains** menu. Learn more in [Block Autosave on Specific Sites](https://bitwarden.com/help/exclude-domains/).

## Ask to save and use passkeys

When Bitwarden detects that you're creating a new passkey for a website, or if you're being prompted to login with a passkey that you have saved in Bitwarden, Bitwarden will prompt you to either save a new passkey or log in with an already-saved one:

![Log in with passkey](https://bitwarden.com/assets/5KeuUZox5shd0zDMxPHKXn/1aab35dfceed0ed9cdb17b143be9a890/2024-10-29_11-39-33.png)

More information can be found in [Autofill Passkeys](https://bitwarden.com/help/storing-passkeys/).

## Ask to add login

When Bitwarden detects that you've entered login information for a page that isn't stored in Bitwarden, you'll be prompted to save those credentials in Bitwarden:

![Ask to add login](https://bitwarden.com/assets/4vsurEuH5deik26BWn4n1p/82757186b081890fbe92b4d73baeae53/screenshot_7.png)

From this notification, you can select whether to store this among your personal items (i.e. **My vault**) or with an organization. You can also edit the item before saving it using the edit [pencil-square] button.

## Ask to update existing login

When Bitwarden detects that login information you enter on a form for an item you have saved in Bitwarden is different from what you have saved, for example if you've recently updated your password on a website but not in Bitwarden, you'll be prompted to update your credentials in Bitwarden:

![Ask to update existing login](https://bitwarden.com/assets/3nn8Vz526Il3onWPHMUUAi/90fd3af3616b60c2961064a56205d525/2025-05-20_16-19-00.png)

## Ask to save a URI

When using the browser extension to **Autofill**a login item that does not have a URI matching the website you are on, the browser extension will give you the option to save the new URI to the item:

![Confirm Autofill](https://bitwarden.com/assets/67h2UzB5cit1oVpEKTUcVs/dfeadfd6749961b76fb9746a36cc9085/2025-12-04_09-37-06.png)
*Confirm Autofill*
