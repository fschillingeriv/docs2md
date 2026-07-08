---
URL: https://bitwarden.com/help/master-password-re-prompt/
---

# Master Password Re-Prompt

For any [item](https://bitwarden.com/help/managing-items/), you can activate the **Master password re-prompt** option from the Add or Edit screen to require verification of your [master password](https://bitwarden.com/help/master-password/) to access or autofill sensitive vault items: 

![Master password re-prompt ](https://bitwarden.com/assets/sgKb0RX5hGdrdKLmXcR0R/f78654839e18b3f474dd3e95ed0d203c/2024-12-02_14-38-06.png)

Master password re-prompt will behave slightly differently depending on which app you're using, for example:

- In the web app, browser extension, and desktop app viewing the item or editing anything about it with this enabled will require you to re-enter your master password.
- On mobile apps, only viewing hidden fields (e.g. passwords, hidden custom fields, credit card numbers) will require you to re-enter your master password. Editing anything about the item will also require you to re-enter your master password.

Users who do not have master passwords, for example those in organizations using [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/) or [Key Connector](https://bitwarden.com/help/about-key-connector/), will not have the master password re-prompt option available to them. Additionally, trusted contacts using [emergency access](https://bitwarden.com/help/emergency-access/#use-emergency-access/) will not be required to re-enter a master password in order to view a protected vault item.

> [!WARNING] MPW Reprompt isn't encryption.
> Master password re-prompt **is not** an encryption mechanism. This feature is an interface-only guardrail that a sophisticated user may find ways to work around. We recommend **never** leaving your vault unlocked when unattended or on a shared workstation.

##
