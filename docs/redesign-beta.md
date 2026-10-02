---
URL: https://bitwarden.com/help/redesign-beta/
---

# Bitwarden Redesign Beta

Bitwarden is updating the look and feel of apps, now available as a **beta for cloud users of Chrome browser extensions and desktop apps**. This beta is [opt-in](https://bitwarden.com/help/redesign-beta/#join-the-beta/), can be used with your current cloud Bitwarden account, and you can switch back to the mainstream version at any time.

## What's changing

The beta introduces a new look and navigation for your Vault. Here's what to expect:

### New Vault terminology

**Organizations** are now called **Vaults**, and each is labeled in the navigation menu with its own name. Where the classic view read "Vaults," you'll now see your organization's name, such as "Acme Corp." **Collections** are now called **Shared folders**.

![(Beta) Shared folders](https://bitwarden.com/assets/6K8cAenzwAWRFHUfEH7qQK/aa2de13ac228c746b9ff69dbb347c27b/2026-09-22_09-24-03.png)
*(Beta) Shared folders*

> [!TIP] (Beta) Organizations renames are name changes only.
> These are naming changes only. Who can access which items, and how sharing and permissions work, remains the same.

### Redesigned navigation

The side navigation is reorganized, and a new Vault switcher makes it easier to swap views between your personal Vault, any other Vaults you belong to, or both at the same time.

![(Beta) Redesigned navigation](https://bitwarden.com/assets/6L9tVPVN5BPWSTuEqUvNGV/be4d1237bc9875f80a7c8fcd8a9556e2/2026-09-22_09-07-22.png)
*(Beta) Redesigned navigation*

> [!TIP] (Beta) Importing is now first-class
> Importing your credentials is one of the most important first steps for new users! That's why we moved the **Import** button directly to the core Items views of the desktop app (and, once it's generally available, of the web app):
> 
> 
> ![(Beta) Import to your vaults](https://bitwarden.com/assets/rkAIYmIQbxj8m1YofyeH1/256ca500e993a1b00a84b6bf09fced38/2026-09-22_09-19-10.png)
> *(Beta) Import to your vaults*
> 
> On browser extensions and mobile apps, importing is available from the same location in your app's **Settings** menu.

### Combined search and filter

Within your vault, search and filtering are now part of one bar built directly into your item list, instead of two separate controls. Searching and filtering work in tandem, so a search for `Email` while the `Acme Corp` Vault filter is active will result in a `Shared Newsletter Email` login you have access to but not your own `Work Email`, as long as it's not in a shared folder. 

![(Beta) Searching and filtering](https://bitwarden.com/assets/3vOMPXLwJ95gfT9g5x6RWP/d9e60285f792b1641b5d5f63f4162a27/2026-09-28_09-28-57.png)
*(Beta) Searching and filtering*

In the above screenshot, the desktop app has an active Vaults filter but the browser extension does not. Active filters show up as dismissible chips, so it's always clear what's currently applied, and your filter selections stay in place when you navigate away from and back to a list. 

> [!TIP] (Beta) New keyboard shortcuts
> New keyboard shortcuts are also available in the beta. Use `Cmd/Ctrl+F` to search and `Esc` to clear a filter.

## Join the beta

This beta is available for browser extensions and desktop apps. All you need to do is download the beta apps from one of these places:

- Chrome browser extension: [Download it here](https://chromewebstore.google.com/detail/bitwarden-password-manage/hccnnhgbibccigepcmlgppchkpfdophk?pli=1) (**requires**Chrome version 134+).
- Desktop app: [Download it here](https://github.com/bitwarden/clients/releases/tag/desktop-v2026.9.1-beta.1).

 - On Windows, download an `.exe`.
 - On macOS, download a `.dmg`.

Once installed, log into your same cloud Bitwarden server (US or EU) as you usually would, no separate account or server setup is required. 

> [!NOTE] (Beta) Not available for self-host
> The beta experience **will not be available for self-hosted Bitwarden servers**.

**We highly recommend** turning off your mainstream Bitwarden browser extension to prevent the apps from competing on things like autofill and 2FA, and uninstalling your mainstream desktop app to prevent them from competing on biometrics. You should only have **one version of each app** active at a time.

For the desktop app, on macOS you may be prompted prompted to save your OS password to the keychain so that the beta app can access secure storage. We recommend selecting **Always Allow**.

### Send feedback

We're excited to hear what you think about the beta:

- To share your experience with the beta, [fill out the survey](https://docs.google.com/forms/d/e/1FAIpQLSdSVNSLkHTt399Okh_WbdZOZ01iEAcpH5-rFbz4sJDIgqe1Og/viewform) and talk about your experience in the [community forum thread](https://community.bitwarden.com/t/try-out-the-redesigned-bitwarden-apps-now-in-beta/102516).
- To report a bug, [open a GitHub Issue](https://github.com/bitwarden/clients/issues) by selecting **New Issue** and using the **Browser Extension Beta Bug Report** or **Desktop Beta Bug Report** templates.

### Known issues

This section contains a list of known issues in the beta apps as of launch:

| Feature | Client(s) | Description |
|------|------|------|
| Biometric unlock | Desktop | If you have more than one Bitwarden desktop app installed, biometric unlock may not work as expected. To fix this, remove all Bitwarden desktop apps and reinstall only the version you prefer to use. |
| Clearing organization filters | Browser extension | When 2+ organizations are selected, removing one organization’s filter chip also removes the filter chips for that organization’s shared folders. Afterward, the “My folders” filter may be missing from the filter menu. |
| Shared folder names | Desktop | Long shared folder names are truncated. |
| Folder selection dropdowns | Desktop | The folder dropdown experience is not as functional as desired when you have many nested shared folders. |
| Shared folder nesting | Desktop | Nested shared folders are not indented in the vault list, making it unclear which shared folders are inside others. |
| Expanding nested folders | Browser extension | The target click area for expanding a nested shared folder is overly small and can be hard to tap or click. |
| Designating favorites | Desktop | Adding or removing the favorite status from an item may cause other items in the list to briefly flicker or experience other visual artifacts. |
| Loading placeholders | Browser extension | The loading placeholders shown while your vault loads are not smooth. |
| Account switcher | Desktop | An extra divider line appears above “Add account” when only one account is signed in, and the lock icon sits too close to its label. |
| Buttons | Browser extension | Some margins around buttons are not correctly displaying. Additional refinements planned. |

### Leave the beta

You can swap between the beta and mainstream apps until the beta ends on October 31, 2026. If you want to leave the beta before that date, stop using the beta app and uninstall it.

**When the beta ends, it's critical to switch to the mainstream app** to continue receiving updates.
