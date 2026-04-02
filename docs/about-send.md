---
URL: https://bitwarden.com/help/about-send/
---

# About Send

Bitwarden Send is an encrypted file and text sharing tool that transmits sensitive information directly to anyone through secure, temporary links. Send can be used to transmit text up to 1000 encrypted characters or files up to 500 MB (or 100 MB on mobile) and can be [shared with anyone](https://bitwarden.com/help/receive-send/) via text, email, or any preferred communication channel. 

## Accessing Send

Sends are created, edited, managed, and deleted from the Send view in any Bitwarden app. Access the send view from the primary navigation:

![Send in the web app](https://bitwarden.com/assets/7umXxS0YG58NdB3vb4kwKo/c2a5f8ae8fa0bae6becb2e20e7f59390/2026-02-24_12-52-46.png)
*Send in the web app*

## Using Send

Using Bitwarden Send is a two-step process: [Create your Send](https://bitwarden.com/help/create-send/) and share with [intended recipients](https://bitwarden.com/help/receive-send/). To create a Send:

1. Select **New Send**:

![New Send](https://bitwarden.com/assets/5ixV8tBpmNQsujpAfan69u/bc04bef94830ec05cfa414bc4b1d7a58/2026-02-24_10-39-18.png)
*New Send*
2. Select the required [lifespan options](https://bitwarden.com/help/send-lifespan/) and [privacy options](https://bitwarden.com/help/send-privacy/) to fit your sharing needs.

![Send options](https://bitwarden.com/assets/5vAk27se4vF8LYczDueYex/9b624f8fd77801241f48263f4428e16d/2026-02-24_10-48-59.png)
*Send options*
3. Share the Send link using any communication channel you prefer.

Each Send has a [configured lifespan](https://bitwarden.com/help/send-lifespan/) that allows you to track the Send. Sends will display [a set of status icons](https://bitwarden.com/help/send-faqs/#q-what-do-the-icons-next-to-my-sends-indicate/) whenever a lifespan event (for example, expiration) has occurred. The icons are as follows:

| **Icon** | **Meaning** |
|------|------|
| 🔒 | This Send is [protected by a password](https://bitwarden.com/help/send-privacy/#send-passwords/). |
| ✗ | This Send has been [manually disabled](https://bitwarden.com/help/send-lifespan/#manually-deactivate-or-delete/). |
| 🕐 | This Send has reached its specified [expiration date](https://bitwarden.com/help/send-lifespan/#expiration-date/). |
| ✗ | This Send has reached its specified [maximum access count](https://bitwarden.com/help/send-lifespan/#maximum-access-count/). |
| 🗑️ | This Send has reached its specified [deletion date](https://bitwarden.com/help/send-lifespan/#deletion-date/) and is **pending deletion**. |

## 

## Send security

### End-to-end encrypted

Data is [encrypted](https://bitwarden.com/help/send-encryption/#send-encryption/) on creation and only [decrypted](https://bitwarden.com/help/send-encryption/#send-decryption/) when a recipient opens the link. A Send's contents are stored **encrypted** in Bitwarden systems just like a traditional vault item. The link generated for each Send doesn't contain any data related to its contents, so it's safe to share over intermediary communications services without exposing information.

### Dynamically ephemeral

Sends are designed for ephemeral sharing, so every [Send that you create](https://bitwarden.com/help/create-send/) has specified [lifespan](https://bitwarden.com/help/send-lifespan/) (max. 31 days) that can be chosen from a few options or a custom timestamp. When its deletion date is reached, the Send and its contents will be completely purged. Using other options like [expiration date](https://bitwarden.com/help/send-lifespan/#expiration-date/) and [maximum access count](https://bitwarden.com/help/send-lifespan/#limit-views-or-maximum-access-count/), you can ensure that access to recipients is terminated according to your needs.

### Flexibly private

You can protect the contents of your Send with several flexible privacy options:

- [Configuring a password](https://bitwarden.com/help/send-privacy/#send-passwords/) for access.
- [Email-verified access](https://bitwarden.com/help/send-privacy/#email-verified-recipients/) for specific recipients.
- [Hiding your email address from recipients](https://bitwarden.com/help/send-privacy/#hide-email/).

For text Sends, you can also optionally [require users to toggle visibility](https://bitwarden.com/help/send-privacy/#hide-text/) to prevent exposure to unintentional onlookers.

> [!NOTE] Sends and Attachments utilize storage space
> Attachments on individual vault items and all Sends use the individual storage space granted by premium subscriptions or organizations. Attachments on organization owned items use shared organizational storage space. Learn how to [add storage space](https://bitwarden.com/help/attachments/#add-storage-space/).

## Next steps

Now that you have learned the basics of Bitwarden Send, we recommend:

- [Creating your first Send](https://bitwarden.com/help/create-send/)
- [Go premium for file Sends](https://bitwarden.com/help/password-manager-plans/#premium-individual/)
- For a more in-depth overview of send, see [Bitwarden Send - How it works](https://bitwarden.com/blog/bitwarden-send-how-it-works/).
