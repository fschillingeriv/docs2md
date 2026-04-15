---
URL: https://bitwarden.com/help/auto-fill-card-id/
---

# Autofill Cards & Identities

Bitwarden can do more than just [autofill your usernames and passwords](https://bitwarden.com/help/auto-fill-browser/)! Some Bitwarden apps can autofill [cards](https://bitwarden.com/help/managing-items/#cards/) and [identities](https://bitwarden.com/help/managing-items/#identities/) to simplify online purchases, account creation, and more. For organization members, a policy may [prevent the use of card items](https://bitwarden.com/help/policies/#remove-card-item-type/) and therefore the ability to autofill them.

> [!NOTE] Support for auto-fill cards and identities.
> Autofill of cards is currently available for browser extensions and Android. Autofill of identities is currently only available for browser extensions.

## Set up card & identity autofill

> [!TIP] Android autofill card setup
> On Android, autofill of cards does not require any setup beyond the [baseline autofill setup](https://bitwarden.com/help/auto-fill-android/). The following instructions are for browser extensions only.

You can add or remove cards from your autofill suggestions and from the inline autofill menu using four settings found in the **Settings** → **Autofill** menu:

- **Display identities as suggestions**: Include identities in the inline autofill menu. This requires the **Show autofill suggestions on form fields** option to be on.
- **Display cards as suggestions**: Include cards in the inline autofill menu. This requires the **Show autofill suggestions on form fields** option to be on.
- **Always show cards as Autofill suggestions on Vault view**: Include cards in the suggestions located in the Vault view. These can be autofilled using the **Fill** button.
- **Always show identities as Autofill suggestions on Vault view**: Include identities in the suggestions located in the Vault view. These can be autofilled using the **Fill** button.

## Use card & identity autofill

There are a few different methods you can use to autofill cards or identities:

### Browser extensions

### Using the inline menu

To enable card and identity autofill using the inline autofill menu, turn on the **Display identities as suggestions** and **Display cards as suggestions** options as described in the previous section. The **Show autofill suggestions on form fields**option must also be turned on.

Once on, your stored cards and identities will be listed when you click on a form. Select the card or identity you wish to use when filling out a form information:

![Inline Autofill Card](https://bitwarden.com/assets/2IZKkQJjPBvDgT3Z6IZMoR/2d00c6b6789b78addd486fd974720ddd/2024-08-13_13-10-20.png)

> [!NOTE] Save new card inline autofill
> If you do not have a card or identity saved in your Bitwarden vault, you may select + **New Card**/ **New identity** from the inline menu after filling out the information to save the new item in your Bitwarden vault.

### Using the Fill button

To autofill a card or identity using the **Fill**button, turn on the **Show cards as Autofill suggestions on Vault view** and **Show identities as Autofill suggestions on Vault view** options as described in the previous section.

Once on, your cards and identities will be available in the **Autofill suggestions**section of the **Vault**view. Select the **Fill**button to autofill:

![Fill Card and Identities](https://bitwarden.com/assets/78MbqVeoL6Juo7E5cMUUNh/57b31fd7fd315aa6334125bf168fb67d/Card___identity_fill.png)

The browser extension will find any fields on the web page that map to card or identity information and autofill them.

### Using the context menu

> [!NOTE] No context-menu in safari extension
> Autofill with a context menu is currently unavailable in the Safari browser extension.

Without opening your browser extension, you can autofill cards and identities by right-clicking on an input field and using the **Bitwarden** → **Autofill** option. If your vault is locked when you attempt this, a window will open prompting you to unlock. Once unlocked, the browser extension will automatically proceed with autofilling your information.

![Browser Extension Context Menu](https://bitwarden.com/assets/6GKKvIe7GwwOBtp9gmh862/4d39f59a8a862bb83d53e50f9f68d107/2024-12-03_09-12-06.png)

### Using keyboard shortcuts

Cards and Identities can be autofilled using keyboard shortcuts. To use this feature, keyboard shortcuts must be manually set for cards and identities:

1. Open the Bitwarden browser extension and select ⚙️ **Settings**.
2. Select **Autofill** from the settings menu and then **Manage shortcuts** to open your browsers autofill settings window.
3. In the Bitwarden Password Manager keyboard shortcuts, configure keyboard shortcuts you would like to use for **Autofill the last used card for the current website** and **Autofill the last used identity for the current website**.

### Android apps

On Android, cards will automatically appear as suggestions inline (in your keyboard) or as a popup over the field depending on [which autofill method is active](https://bitwarden.com/help/auto-fill-android/#list-of-autofill-methods/). This is currently available for Chrome and Chromium browsers. For example, as a popup:

![Android card popup](https://bitwarden.com/assets/2ekny75ulY7xoyqz80Kz1z/f3954ac976db5283aa064efc6a78cc5e/2025-08-12_10-32-44.png)
