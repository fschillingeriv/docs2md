---
URL: https://bitwarden.com/help/blocking-uris/
---

# Block Autofill on Specific Sites

Users of the Bitwarden browser extensions and Android mobile app can explicitly prevent autofill from being allowed on certain domains or URIs:

### Browser extensions

> [!TIP] What blocking autofill does on browser extension
> Domains that are designated for blocking will block autofill, passkey prompts, and prompts to save or update your credentials.

To specify domains to block for browser extensions:

1. In the Bitwarden browser extension, open the ⚙️ **Settings** tab.
2. Select **Autofill**, then scroll to the bottom of the screen and select **Blocked domains**.
3. Select **Add domain** and specify the domain you want to block on.
4. Select **Save**.

### Android

> [!NOTE] Support for URI blacklisting
> Autofill blocking URIs is currently only available for Bitwarden **Android 8.0 (Oreo)** or higher.

To specify URIs to block autofill on for Android:

1. In the Bitwarden Android app, tap ⚙️ **Settings**.
2. Tap **Autofill**.
3. Scroll down and tap **Block autofill**.
4. Tap **New blocked URI** and enter the URIs. Separate multiple URIs with a comma, like:

```
https://instagram.com,androidapp://com.instagram.android,https://facebook.com
```
5. Tap **Save**.

#### Getting Android app URIs

For websites accessed via a web browser, a proper URI will be the `https://..` address of the login page, for example `https://instagram.com` or `https://instagram.com/accounts/login`.

**For Android apps**, the [URI scheme](https://bitwarden.com/help/uri-match-detection/#uri-schemes/) always starts with `androidapp://` and is usually a bit different from a typical web browser URI. For example,

- The Instagram Android app has the URI `androidapp://com.instagram.android`
- The Reddit Android app has the URI `androidapp://com.reddit.frontpage`
- The Bitwarden Android app has the URI `androidapp://com.x8bit.bitwarden`

> [!TIP] Get URI from Mobile
> An easy way to obtain the proper URI for an Android app is to visit the app's page in the Google Play Store, tap the share button, and paste the copied link somewhere you can read it. The link will look like `https://play.google.com/store/apps/details?id=com.instagram.android`. The value after `id= `is your URI, in this case `com.instagram.android`. 
> 
> For iOS users, an app URI can be obtained by using autofill to open Bitwarden. Once Bitwarden is open, select the + icon on the top right corner of the screen. From here, copy the URI that has been included in the new vault item. Paste the URI into your existing login item for this app.

``
