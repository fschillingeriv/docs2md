---
URL: https://bitwarden.com/help/basic-auth-autofill/
---

# Autofill Basic Auth Prompts

Login prompts like the one pictured below, called "basic" or "native" authentication prompts, will be automatically autofilled by Bitwarden browser extensions **if there is only one login item with a** [**matching URI**](https://bitwarden.com/help/uri-match-detection/). You can also use the browser extension's [share-square] **Launch** button to automatically open and log in to a basic auth-protected resource.

Autofilling on basic auth prompts will, by default, use the [Host](https://bitwarden.com/help/uri-match-detection/#host/) URI match detection option so that autofilling is more restrictive. This can be changed by setting the [match detection option](https://bitwarden.com/help/uri-match-detection/) for the relevant login.

If more than one login with a matching URI is found, the browser extension will not be able to autofill your credentials and you will need to manually copy/paste your username and password to log in.

If a single login item is present for a matching URI, the credentials will be autofilled in the background and no authentication prompt will be shown.

![Basic Auth Prompt ](https://bitwarden.com/assets/6rUtQ8FzPTPuKM0sXZ4iyc/3fc116ce5eba8bc70f8dbebfac0eafa6/basic-auth-prompt.png)

> [!NOTE]
> Due to the way basic auth prompts are designed, auto-filling must be non-interactive. This means you cannot autofill on a basic auth prompt using the **Vault** view, context-menu, or keyboard shortcuts.
