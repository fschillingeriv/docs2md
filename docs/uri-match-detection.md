---
URL: https://bitwarden.com/help/uri-match-detection/
---

# Form URIs for Autofill

Include a Uniform Resource Identifier (URI) in login items to use [autofill](https://bitwarden.com/help/auto-fill-browser/) and select the [share-square]**Launch icon** to open a website or app directly from your vault. A URI is a string of characters that identifies a website address (URL), server IP address, [mobile app package ID](https://bitwarden.com/help/uri-match-detection/#uris-for-mobile-apps/), and more. 

## Save URIs in login items

When you create or edit a login item, enter it into the **Website (URI)** field. The website's URI is automatically populated when the browser extension [autosaves](https://bitwarden.com/help/autosave-from-browser-extensions/) a new login.

You can add multiple URIs to a single login item. To reorder them, edit the item in the web app or browser extension and drag-and-drop the URIs into your preferred order:

![Edit Website (URI) fields](https://bitwarden.com/assets/aDbOEJ6x8G44gkDYcuHJ6/dfef7ac49894805dd0e1e718452e6a60/2025-03-25_09-45-56.png)
*Edit Website (URI) fields*

### Save URI to existing login item

You may use the browser extension to Autofill a login item that does not have a matching URI to the website you are attempting to log in to.

1. Open the browser extension and locate the login item you wish to fill. This item can be searched, or located in the **All items** list. Select the ⋮ menu and choose **Autofill**. The Confirm autofill screen will be displayed in the browser extension. The screen will show any URIs saved to the login item, and the URI of the current website you are on. 

![Confirm Autofill](https://bitwarden.com/assets/67h2UzB5cit1oVpEKTUcVs/dfeadfd6749961b76fb9746a36cc9085/2025-12-04_09-37-06.png)
*Confirm Autofill*
2. Select the action you would like to take.

### Format URI schemes

Well-formed URIs should include a scheme at the beginning to securely reference a website address, like `https://`. If no scheme is specified, `http://` is assumed.

Schemes include:

- `http://` or `https://` reference website addresses (for example, `https://github.com`).
- `androidapp://` references an Android application package ID or name (for example, `androidapp://com.instagram.android`).

### Find URIs for mobile apps

It can be tricky to obtain URIs for apps installed on iOS and Android devices. Here are a few tips for getting URIs on iOS and Android apps:

### iOS

On iOS, the easiest way to find a URI for native applications is:

1. On the app's login screen, use 🔑 **Passwords** to open Bitwarden.
2. Once Bitwarden is open, select the + icon on the top right corner of the screen.
3. The URI that has been included in the new vault item (if permitted by the app), can be copied and pasted into any existing login items.

### Android

> [!WARNING] Android autofill vulnerability
> On Android, Password Manager uses a package name (e.g. `com.google.android.gm`) to autofill in installed applications. When it comes to installed applications, it is important that you **only install and autofill into applications from trusted sources**, like the Google Play Store or F-Droid.
> 
> Outside sources like the Google Play Store or F-Droid, Android does not enforce the uniqueness of package names. This means a malicious developer could create and distribute an application intended to harvest credentials that uses the same package name (e.g. `com.google.android.gm`) as an official and well-known application. Such an application would be offered by autofill, but you can protect yourself by:
> 
> - Only installing applications from trusted sources, like Google Play Store or F-Droid.
> - Only autofilling credentials into applications that are the official versions.

On Android, the easiest way to find a URI for native applications is:

1. Visit the app's page in the Google Play Store.
2. Locate the share button and copy the link to your clipboard.
3. Paste the copied link somewhere you can read it. The link will look like: 

`https://play.google.com/store/apps/details?id=com.instagram.android`. 
The value after `id= `is your URI, in this case `com.instagram.android`.

> [!NOTE] Android 13+ needed for launch
> Launching applications is supported in Android versions 13 and newer.

## Set match detection

You can fine-tune how Bitwarden compares the URI you saved with the website or app you're currently using, ensuring your credentials are suggested for autofill at the right time. There are several [match detection options](https://bitwarden.com/help/uri-match-detection/#match-detection-options/) to choose from.

### Default match detection

The default URI match method for all new login items is [**Base domain**](https://bitwarden.com/help/uri-match-detection/#base-domain/). To change your account's default match detection:

1. Go to ⚙️ **Settings.**
2. Select **Autofill**.
3. Choose your preferred method from the **Default URI match detection** dropdown menu.

> [!NOTE] No default URI match setting because policy
> If the **Default URI match detection** option is not present, then your organization owner or admin already picked a [default match for your organization](https://bitwarden.com/help/policies/#default-uri-match-detection/).

### Match detection by item

You can also change the match detection on an item-by-item basis. Within the login item's **Website (URI)** field, select the ⚙️ **Settings icon** to choose a **Match detection** method. This will override your account's default match detection option.

## Match detection options

The match detection method determines when Bitwarden will suggest the login for autofill, typically by matching against specific component pieces. The following graphic breaks down component pieces of a URI:

![URI diagram](https://bitwarden.com/assets/2J7AdBKH3DLQwoyGhNAWJA/7fcfdc4cf80202d9c90a1350a75542e2/urlgraphic.png)
*URI diagram*

> [!NOTE] Android clients can't port match
> Due to limitations in what the Android APIs can provide the autofill service, Android Password Manager clients cannot currently match URIs based on **port** or **path**.

### Base domain

Selecting **Base domain** will prompt Bitwarden to offer autofill when the top-level domain (`.com`) and second-level domain (`google`) of the URI match the detected resource. Base domain matching is implemented to work with any country code top-level domain (for example, `.it` or `.co.uk`). For sites that use unique domains, such as for different countries, create additional base domain entries.

For example, if the URI `https://google.com` uses base domain match detection:

| **URL** | **Autofill?** |
|------|------|
| `http://google.com` | ✓ |
| `https://accounts.google.com` | ✓ |
| `https://google.net` | [close] |
| `http://yahoo.com` | [close] |

> [!NOTE] Single-term & local DNS entries
> Login items intended to autofill in a URI with a local TLD (e.g. `http://mysite.local` or `https://mysite.lan`) or single-term hostname (e.g. `http://localdevice`) will not be available for base domain detection. We recommend using [host matching](https://bitwarden.com/help/uri-match-detection/#host/).

### Host

> [!NOTE] Android clients can't port match
> Due to limitations in what the Android APIs can provide the autofill service, Android Password Manager clients cannot currently match URIs based on **port** or **path**.

Selecting **Host** will prompt Bitwarden to offer autofill when the hostname and (if specified) port of the URI matches the detected resource.

For example, if the URI `https://sub.domain.com:4000` uses host match detection:

| **URL** | **Autofill?** |
|------|------|
| `http://sub.domain.com:4000` | ✓ |
| `https://sub.domain.com:4000/page.html` | ✓ |
| `https://domain.com` | [close] |
| `https://sub.domain.com` | [close] |
| `https://sub2.sub.domain.com:4000` | [close] |
| `https://sub.domain.com:5000` | [close] |

> [!NOTE] OS standard keyboard fill
> While using [keyboard based suggestions](https://bitwarden.com/help/auto-fill-ios/#keyboard-auto-fill/), iOS will always use base domain matching for autofill suggestions. Opening the Bitwarden app during login will allow you to manually select the appropriate app for autofill.

### Starts with

> [!NOTE] Starts with: advanced option
> **Starts with** is an advanced option and can be quite dangerous if used incorrectly. You should not use this option if you do not know exactly what you are doing.

Selecting **Starts with** will prompt Bitwarden to offer autofill when the detected resource starts with the URI, regardless of what follows it.

For example, if the URI `https://sub.domain.com/path/` uses starts with match detection:

| **URL** | **Autofill?** |
|------|------|
| `https://sub.domain.com/path/` | ✓ |
| `https://sub.domain.com/path/page.html` | ✓ |
| `https://sub.domain.com` | [close] |
| `https://sub.domain.com:4000/path/page.html (interrupted with a port)` | [close] |
| `https://sub.domain.com/path (absent trailing slash)` | [close] |

### Regular expression

> [!WARNING] Don't use regex
> Regular expressions are an advanced option and can be quite dangerous if used incorrectly. You should not use this option if you do not know exactly what you are doing.

Selecting **Regular expression** will prompt Bitwarden to offer autofill when the detected resource matches a specified [regular expression](https://en.wikipedia.org/wiki/Regular_expression). Regular expressions are always case insensitive.

#### Unsafe example

If the URI `^https://.*google\.com$` uses regular expression match detection:

| **URL** | **Autofill?** |
|------|------|
| `https://google.com` | ✓ |
| `https://sub.google.com` | ✓ |
| `https://malicious-site.com?q=google.com` | ✓ |
| `http://google.com` | [close] |
| `https://yahoo.com` | [close] |

This probably matches more than what is intended. Consider avoiding periods (`.`), which unless escaped (`\`) match on any character.

#### Safe example

If the URI `^https://[a-z]+\.wikipedia\.org/w/index\.php` uses regular expression match detection:

| **URL** | **Autofill?** |
|------|------|
| `https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Bitwarden` | ✓ |
| `https://pl.wikipedia.org/w/index.php?title=Specjalna:Zaloguj&returnto=Bitwarden` | ✓ |
| `https://en.wikipedia.org/w/index.php` | ✓ |
| `https://malicious-site.com` | [close] |
| `https://en.wikipedia.org/wiki/Bitwarden` | [close] |

### Exact

Selecting **Exact** will prompt Bitwarden to offer autofill when the URI matches the detected resource exactly.

For example, if the URI `https://www.google.com/page.html` uses exact match detection:

| **URL** | **Autofill?** |
|------|------|
| `https://www.google.com/page.html` | ✓ |
| `http://www.google.com/page.html` | [close] |
| `https://www.google.com/page.html?query=123` | [close] |
| `https://www.google.com` | [close] |

> [!NOTE] Exact Match Detection
> As shown in the table, you can use exact match detection to restrict autofill to only `https://` sites. Note that, whether you use exact or not, browser extensions will warn users before autofilling an HTTP site when HTTPS is expected based on that item’s saved URI(s).

### Never

Selecting **Never** will prompt Bitwarden to exclude the URI from match detection for autofill.

## Equivalent domains

Equivalent domains, which can be set from the **Account settings** → **Domain rules** page of the web vault, allow you to link domains for easier autofill. For example, setting `turbotax.com` and `intuit.com` as equivalent means that a vault item with `turbotax.com` saved as a URI will also be offered for auto-fill at `intuit.com`.

Bitwarden maintains a vetted list of default equivalent domains of major sites, for example `apple.com` and `icloud.com`, to improve your autofill experience. You can disable any given equivalence by hovering over it and using the ⚙️ **Settings icon** to select [close] **Exclude.**

> [!TIP] Equivalent Domains + Match Detection
> An equivalent domain will be negated for an item that uses [exact match detection](https://bitwarden.com/help/uri-match-detection/#exact/). For example, an item with the saved URI `apple.com` set to **Exact** will not offer autofill for `icloud.com` despite that being a default equivalent.
