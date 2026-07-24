---
URL: https://bitwarden.com/help/about-send/
---

# About Send

Bitwarden Send is a tool to transmit sensitive text or files directly to anyone through secure, temporary links. Send can be used to transmit text up to 1,000 encrypted characters or files up to 500 MB (or 100 MB on mobile) and can be [shared with anyone](https://bitwarden.com/help/receive-send/) via text, email, or any preferred communication channel. 

> [!NOTE] Remove Send policy
> If you're a member of an organization that has turned off Send under the [Manage Send policy](https://bitwarden.com/help/policies/#manage-send/), your access to Sends is limited:
> 
> - You cannot create new Sends or edit existing ones.
> - You can view and delete Sends from the **Sends** page in all Bitwarden clients, except the web app.
> - You cannot access the Sends page with the Bitwarden web app.
> 
> Using the Manage Send policy, organization owners and admins can also control which fields are unavailable when creating a new Send.

## Accessing Send

Sends are created, edited, managed, and deleted from the **Send** view in any Bitwarden app. Access the Send view from the primary navigation:

![Send in the web app](https://bitwarden.com/assets/7umXxS0YG58NdB3vb4kwKo/c2a5f8ae8fa0bae6becb2e20e7f59390/2026-02-24_12-52-46.png)
*Send in the web app*

Each Send has a [configured lifespan](https://bitwarden.com/help/send-lifespan/) which allows you to monitor the Send. Your created Sends will display status icons when a lifespan-related event occurs:

| **Icon** | **Meaning** |
|------|------|
| 🔒 | This Send is [protected by a password](https://bitwarden.com/help/send-privacy/#send-passwords/). |
| ✗ | This Send has been [manually disabled](https://bitwarden.com/help/send-lifespan/#manually-deactivate-or-delete/). |
| 🕐 | This Send has reached its specified [expiration date](https://bitwarden.com/help/send-lifespan/#expiration-date/). |
| ✗ | This Send has reached its specified [maximum access count](https://bitwarden.com/help/send-lifespan/#maximum-access-count/). |
| 🗑️ | This Send has reached its specified [deletion date](https://bitwarden.com/help/send-lifespan/#deletion-date/) and is **pending deletion**. |

## Using Send

Using Bitwarden Send is a three-step process:

1. [Create a Send](https://bitwarden.com/help/create-send/) and configure its [lifespan options](https://bitwarden.com/help/send-lifespan/) and [privacy options](https://bitwarden.com/help/send-privacy/) to fit your sharing needs.
2. Share the Send link with recipients through any channel you prefer.
3. [Recipients open the Send link](https://bitwarden.com/help/receive-send/) to access the content.

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
