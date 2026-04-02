---
URL: https://bitwarden.com/help/exclude-domains/
---

# Block Autosave on Specific Sites

Bitwarden browser extensions can be configured to exclude specific sites from triggering [autosave notifications](https://bitwarden.com/help/autosave-from-browser-extensions/). When a domain is in the **Excluded domains** list, Bitwarden won't issue the notification any of the available notifications, including to save a new login, update an existing login, or to save or use a passkey:

![Ask to add login](https://bitwarden.com/assets/4vsurEuH5deik26BWn4n1p/82757186b081890fbe92b4d73baeae53/screenshot_7.png)

To configure excluded domains, navigate to **Settings** → **Notification** → **Excluded domains**:

![Excluded Domains Configuration ](https://bitwarden.com/assets/qUGIVQR379ac3R2dXdoy8/06b4dec0b9e02911903052789c44723c/2024-12-03_11-00-24.png)

Domain exclusion does not register "full" URLs, only the domain component. For example, `https://github.com/bitwarden/browser` would resolve to `github.com` when saved, meaning that the browser extension would explicitly not offer to save credentials for Github.
