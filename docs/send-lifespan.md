---
URL: https://bitwarden.com/help/send-lifespan/
---

# Send Lifespan

Unlike regular vault items and file attachments, Sends are ephemeral and have a **default lifespan of seven days**and can be set to last for up to 31 days using the [deletion date](https://bitwarden.com/help/send-lifespan/#deletion-date/) option. When a Send reaches its deletion date, it's purged from Bitwarden systems and inaccessible to both sender and recipients.

Different client apps allow you to set additional limitations on access like an [expiration date](https://bitwarden.com/help/send-lifespan/#expiration-date/) and/or [maximum access count](https://bitwarden.com/help/send-lifespan/#maximum-access-count/) options. You can also manually [deactivate or delete](https://bitwarden.com/help/send-lifespan/#manually-deactivate-or-delete/) a Send at any time.

## Deletion date

By default, Sends will automatically be deleted seven days after they are created. Using the **deletion date** option, you can change this to a range of pre-specified options (for example, 1 hour, 1 day, 14 days, 31 days).

Deletion date has a **maximum allowed value of 31 days from creation**.

### Deletion behavior

When a Send reaches its deletion date:

- For recipients (anyone with the generated link), navigating to the Send link will show a screen reporting that the Send does not exist or is no longer available.
- For the sender, a 🗑️ **Pending Deletion** icon will appear next to the Send. The Send will pend deletion for a few minutes, after which it will be permanently deleted from Bitwarden systems and from the sender's view.

> [!NOTE] Sends have no soft delete.
> Deleted Sends are not sent to or stored in the trash. Once the deletion has been confirmed, you will not be able to access the contents of a Send.

## Expiration date

> [!NOTE] Expiration & disable options
> Only available in the web app and desktop app.

By default, Sends will never expire, [but they will be deleted](https://bitwarden.com/help/send-lifespan/#deletion-date/). Using the **Expiration Date** option, you can select from a range of pre-specified options (for example, 1 hour, 1 day, 7 days) or specify a custom timestamp using the date picker (or in the text input in the format `MM/DD/YYYY HH:MM AM/PM`).

### Expiration behavior

When a Send reaches its expiration date:

- For recipients (anyone with the generated link), navigating to the Send link will show a screen reporting that the Send does not exist or is no longer available.
- For the sender, an 🕐 **Expired** icon will appear next to the Send. The Send will remain accessible to the sender until the specified deletion date is reached.

## Limit views (or, Maximum access count)

For all Sends, a **current view count** ticker will track the number of times the Send link has been accessed:

![Current Access Count ticker ](https://bitwarden.com/assets/0OzPRjLVfEDJ3EIZC90Cp/5f096d609bcd79b29d44c12f6073a2fa/send_limit.png)
*Current Access Count ticker *

You may specify a view limit using the **Limit views** field.

### Maximum access count behavior

When a Send reaches its specified maximum access (or **View**) count:

- For recipients (anyone with the generated link), navigating to the Send link will show a screen reporting that the Send does not exist or is no longer available.
- For the sender, a ✗ **Max access count reached** icon will appear next to the send. The Send will remain accessible to its sender until the specified deletion date is reached.

> [!TIP] Max Access Count
> The **Current Access Count** (or **View**) ticker counts:
> 
> - For text Sends, the number of times the link has been accessed.
> - For file Sends, the number of times the contents are downloaded.

## Manually deactivate or delete

To manually deactivate or delete a Send from any Bitwarden app:

### Web app

#### Delete from the web app

To delete a Send from the web app, use the ⋮ options menu to select the 🗑️ **Delete** button:

![Send options](https://bitwarden.com/assets/1PiQrX748LtTFXChfAIbFP/0ff74124a0d215254c532fe79cff9012/2026-02-25_11-08-25.png)
*Send options*

### Browser extension

#### Delete from browser extensions

To delete a Send from a browser extension, select the 🗑️ **Trash** icon next to the Send you want to delete:

![Delete Send from a browser extension ](https://bitwarden.com/assets/74CotzsfAWKjUQkXfuu7zq/12d90886dbb9e6bd3a26b47efedeef4c/delete_browser.png)
*Delete Send from a browser extension *

### Desktop

#### Delete from desktop apps

To delete a Send from the desktop app, use the ⋮ options menu to select the 🗑️ **Delete** button:

![Delete from a Desktop App ](https://bitwarden.com/assets/12eLcz2aoBkcDRGS3U1jzP/66e1b7625ac1290f2d110d0d4e7086c8/delete_send_desktop.png)
*Delete from a Desktop App *

### Mobile

#### Delete from mobile apps

To delete a Send from a mobile app, tap the ⋯ options menu and tap the **Delete** option:

![Delete a send on mobile](https://bitwarden.com/assets/4jWcljHXWnKZcSZZmVNyQo/f460782cfec20a6246b9fcab1b4d9d1e/send-delete-mobile.png)
*Delete a send on mobile*

### CLI

#### Disable from the CLI

To disable a Send from the CLI, you will need to use the `edit` command to change the `"disabled":false` key-value pair to `"disabled":true`, for example:

```
bw send get <id> | jq '.disabled=false' | bw encode | bw send edit
```

We recommend reading the [Send from CLI](https://bitwarden.com/help/send-cli/) article for more information.

#### Delete from the CLI

To delete a Send from the CLI, use the `delete` command with the Send's exact unique `id` as an argument:

```
bw send delete <id>
```
