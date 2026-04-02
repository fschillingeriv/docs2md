---
URL: https://bitwarden.com/help/website-icons/
---

# Data Privacy for Website Icons

Bitwarden does not collect any information when you download icons for website logins stored in your Bitwarden vault.

## Using website icons

When Bitwarden displays a [login item](https://bitwarden.com/help/managing-items/) with a website (see [Using URIs](https://bitwarden.com/help/uri-match-detection/)) associated with it in your vault, it attempts to accompany it with a graphical icon. Website icons help you to easily identify particular logins in your vault with recognizable iconography, usually represented by a logo or brand image of that website.

> [!NOTE] Icons unavailable on android autofil
> Website icons are not displayed by entries in the auto-fill menu on Android.

### About the icon server

The Bitwarden icon server provides the delivery endpoint for website icons. If you are using website icons on a device, Bitwarden will issue requests to `icons.bitwarden.net` for each login in your vault that has a URI that resembles a website (for example, `google.com` or `https://google.com`, but not `google` or `http://localhost`).

The icon server is fronted with a CDN that caches the icons on Fastly nodes all around the world. Subsequent requests to the same icon will likely hit CDN caches instead of the icon server directly. Your requests may never actually hit Bitwarden's icon server because another Bitwarden user with the same website in their vault requested the icon before you.

> [!NOTE] Icons not cached on self-host
> If you are self-hosting Bitwarden, icons are* *not cached to a CDN. All requests will always hit your icon container directly.

### Privacy considerations

Because a request for an icon contains the hostname of the website stored in your vault, it is important to understand that this feature will "leak" otherwise cryptographically protected information to Bitwarden servers and/or CDN endpoints and be visible in your local cache. An example of an icon request looks like the following:

`https://icons.bitwarden.net/google.com/icon.png`

**The icon server endpoints do not log or collect any information regarding icon image requests**, however this is something you would have to take our word for since we have no way to demonstrate this publicly other than reviewing our [open source codebase](https://github.com/bitwarden).

## Disabling website icons

We understand that certain privacy-minded users may not want to use website icons. We provide the option to disable website icons on all Bitwarden client applications by turning off the following option:

- **Web app:** Settings → Appearance → Show website icons
- **Browser extension:** Settings → Appearance → Show website icons
- **Mobile app:** Settings → Appearance → Show website icons
- **Desktop app:** Settings → Options → Show website icons

When website icons are disabled, Bitwarden will opt to display a generic, locally accessed icon instead ([globe]) for all login items stored in your vault.
