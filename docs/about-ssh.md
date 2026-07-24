---
URL: https://bitwarden.com/help/about-ssh/
---

# About SSH

The Bitwarden SSH Agent is a feature of the desktop app that allows you to store, manage, and use SSH keys across all of your machines. The desktop app acts as an alternative to your operating system's native SSH agent, using the vault for encrypted key storage instead of the local filesystem. 

## How it works

When the SSH Agent is enabled, the Bitwarden desktop app exposes a local socket that your SSH client communicates with. Tools such as `ssh`, `git`, and other SSH-dependent applications send signing requests to the Bitwarden agent instead of the native system agent. Bitwarden handles those requests using keys stored in your vault, prompting you to authorize access based on your configured settings.

The agent supports the following operations:

- **Listing keys**
- **Request signing**
- **Agent forwarding**

## Storing SSH keys

SSH key items are a vault item type supported across the Bitwarden desktop app, web app, browser extension, and mobile apps. Keys can be generated or imported using the desktop app, web app, and browser extension. 

Each SSH key item stores the following fields:

| Field | Description |
|------|------|
| Key name | A display name for the key. |
| Private key | The sensitive key material used for authentication. |
| Public key | The portion of the key shared with servers or services. |
| Fingerprint | A short identifier derived from the public key, useful for verifying signed commits. |

SSH key items support the same Bitwarden features as other vault items, including [folders](https://bitwarden.com/help/folders/), [favorites](https://bitwarden.com/help/favorites/), [master password re-prompt](https://bitwarden.com/help/managing-items/#protect-individual-items/), notes, [cloning items](https://bitwarden.com/help/managing-items/#clone/), [attachments](https://bitwarden.com/help/attachments/), and [custom fields](https://bitwarden.com/help/custom-fields/).

## Create a new SSH key

To create a new SSH key:

1. Select the **New** button and choose **SSH key** as the item type:

![Create new SSH key on desktop](https://bitwarden.com/assets/1XYC3HwXOTMAPvyW1GS3Mk/82a46735327f9085d9380fbb8053b161/new_ssh_key-curent_ui.png)
*Create new SSH key on desktop*
2. Fill in remaining details such as **Name**and select the [save-changes] Save icon once you are finished.

> [!NOTE] Create SSH key only ED25519
> At this time, Bitwarden can only generate `ED25519` type SSH keys.

## Edit a key

To edit an existing SSH key, locate it in your vault and select **Edit**. Editable fields include the key name, folder, owner, and custom fields. The key material itself cannot be modified after creation.

### Organization SSH keys

SSH keys can be created and stored in an organization collection. Organization members with appropriate permissions may create, manage, and access SSH keys owned by an organization. Learn more about [collection permissions](https://bitwarden.com/help/collection-permissions/).

To add a new shared SSH key to the organization vault:

1. On the Vault view of the desktop or web app, select the + **New button** and select **SSH key**.

> [!TIP] Can also be done from Admin Console
> Organization [owners, admins, and some custom users](https://bitwarden.com/help/user-types-access-control/) can also take this step directly from the **Admin Console** to skip some of the steps in this process.
2. Using the **Owner** dropdown, choose the organization you want this item to be owned by.
3. Using the **Collections** dropdown, choose the collection(s) to share this item with.

> [!NOTE] SSH key sharing best practices
> In general, resources that use SSH keys can support per-user keys. We recommend reviewing SSH key best practices before sharing SSH keys to an organization.

## Import key to Bitwarden

The import function for SSH keys is available on the Bitwarden desktop app. Using the Bitwarden desktop app:

- Select the **New** button and choose **SSH key** as the item type.
- Copy the existing SSH key you want to import into Bitwarden.
- Use the **Import key from clipboard** icon. This will automatically paste the SSH key into Bitwarden.

 - At this time, imported keys must be in **OpenSSH** or **PKCS#8** format.

![Import an SSH key](https://bitwarden.com/assets/5QTvyu39h3o0azkjU26P3t/c4987845f91b73efadaa8165f25b4524/Import.png)
*Import an SSH key*

> [!NOTE] import SSH must be in OpenSSH format
> At this time, imported SSH keys from PuTTy are not compatible.

## Supported key types

The SSH Agent supports the following key types:

- Ed25519
- RSA (SHA-256 and SHA-512)

## Agent limitations

The following operations are not currently supported by the Bitwarden SSH Agent.

### No ssh-add key management

The keys available to your agent are determined by what is stored in your vault. They cannot be added, removed, or constrained programmatically with commands such as `ssh-add <key>` or configured in `~/.ssh/config`.

### No per-request key selection

When a signing request comes in, the agent attempts each key in your vault until one succeeds. There is no mechanism to specify which key should be used for a given host. Having multiple keys may result in a failed authentication, even when your vault contains the correct key. As a workaround, you may specify a key in your SSH config file using the `IdentityFile` directive.

### PuTTYgen keys not supported

PuTTygen keys cannot be imported into Bitwarden at this time.

### Multiple accounts

When more than one account is loaded on the desktop app with the SSH agent enabled:

- Each account's keys are loaded when the account is logged in.
- Switching accounts causes the active account's key to be loaded. Before unlocking the second account, the first accounts keys remain active.
- Logging out of an account switches the agent to the remaining logged-in account's keys, if one is available.

The **Enable SSH Agent** setting is global across accounts. If you enable the agent under one account and then switch to another, the setting from the last active account applies.

### Co-existing with a native SSH agent

If you have a native SSH agent installed alongside Bitwarden and have some keys stored locally, your SSH client may default to the native agent if the Bitwarden agent is unavailable or returns a failure. If your authorization settings are set to **Never** or **Remember until vault is locked**, there is no UI interaction which will indicate which agent handled the request.

If you need to store keys locally as well as with the Bitwarden SSH Agent, consider placing the in a non-standard location, rather than `~/.ssh/` to reduce the chance of unintentional fallback.
