---
URL: https://bitwarden.com/help/auto-fill-card-id/
---

# Autofill Cards & Identities

Bitwarden can do more than just [autofill your usernames and passwords](https://bitwarden.com/help/auto-fill-browser/). The Bitwarden browser extension and Android apps can also autofill [cards](https://bitwarden.com/help/managing-items/#cards/) and [identities](https://bitwarden.com/help/managing-items/#identities/) to simplify online purchases, account creation, and more.

## Set up card & identity autofill

For Android, confirm that the [standard autofill setup](https://bitwarden.com/help/auto-fill-android/) is complete. Autofilling cards and identities does not require any additional steps.

For the browser extension, there are a few customizable options for autofilling cards and identities. To add cards and identities to your listed autofill suggestions, go to **Settings** → **Autofill** and select:

- **Always show cards as Autofill suggestions on Vault view** to include cards in the suggestions located in the Vault view. When located in **Autofill suggestions**, click the card item to autofill.
- **Always show identities as Autofill suggestions on Vault view** to include identities in the suggestions located in the Vault view. When located in **Autofill suggestions**, click the identify item to autofill.

> [!NOTE] Jumping from favorites to autofill suggestions
> Autofill suggestions always supersede [favorites](https://bitwarden.com/help/favorites/). If you have a favorited card or identity, it will jump from **Favorites** to **Autofill suggestions** when you turn these options on.

To include cards and identities in the browser extension's [autofill inline menu](https://bitwarden.com/help/auto-fill-browser/#inline-menu/):

1. Go to **Settings** → **Autofill**.
2. Check **Show autofill suggestions on form fields**.
3. Check which setting(s) to activate:

 - **Display identities as suggestions**
 - **Display cards as suggestions**

## Use card & identity autofill

[Embedded content]There are a few different methods you can use to autofill cards or identities:

### Browser extensions

### Using the inline menu

To enable card and identity autofill using the inline autofill menu, turn on the **Display identities as suggestions** and **Display cards as suggestions** options as described in the previous section. The **Show autofill suggestions on form fields**option must also be turned on.

Once on, your stored cards and identities will be listed when you click on a form. Select the card or identity you wish to use when filling out a form information:

![Inline Autofill Card](https://bitwarden.com/assets/2IZKkQJjPBvDgT3Z6IZMoR/2d00c6b6789b78addd486fd974720ddd/2024-08-13_13-10-20.png)
*Inline Autofill Card*

> [!NOTE] Save new card inline autofill
> If you do not have a card or identity saved in your Bitwarden vault, you may select + **New Card**/ **New identity** from the inline menu after filling out the information to save the new item in your Bitwarden vault.

### Using the browser extension's vault view

To autofill a card or identity from the extension's vault, turn on the **Show cards as Autofill suggestions on Vault view** and **Show identities as Autofill suggestions on Vault view** options as described in the previous section.

Once on, your cards and identities will be available in the **Autofill suggestions**section of the **Vault**view. Click anywhere on the card or identity to autofill:

[Embedded content]The browser extension will find any fields on the web page that map to card or identity information and autofill them.

### Using the context menu

> [!NOTE] No context-menu in safari extension
> Autofill with a context menu is currently unavailable in the Safari browser extension.

Without opening your browser extension, you can autofill cards and identities by right-clicking on an input field and using the **Bitwarden** → **Autofill** option. If your vault is locked when you attempt this, a window will open prompting you to unlock. Once unlocked, the browser extension will automatically proceed with autofilling your information.

![Browser Extension Context Menu](https://bitwarden.com/assets/6GKKvIe7GwwOBtp9gmh862/4d39f59a8a862bb83d53e50f9f68d107/2024-12-03_09-12-06.png)
*Browser Extension Context Menu*

### Using keyboard shortcuts

Cards and Identities can be autofilled using keyboard shortcuts. To use this feature, keyboard shortcuts must be manually set for cards and identities:

1. Open the Bitwarden browser extension and select ⚙️ **Settings**.
2. Select **Autofill** from the settings menu and then **Manage shortcuts** to open your browsers autofill settings window.
3. In the Bitwarden Password Manager keyboard shortcuts, configure keyboard shortcuts you would like to use for **Autofill the last used card for the current website** and **Autofill the last used identity for the current website**.

### Android apps

On Android, cards and identities will automatically appear as suggestions inline (in your keyboard) or as a popup over the field depending on [which autofill method is active](https://bitwarden.com/help/auto-fill-android/#list-of-autofill-methods/). This is currently available for Chrome and Chromium browsers. For example, as a popup:

![Android card popup](https://bitwarden.com/assets/2ekny75ulY7xoyqz80Kz1z/f3954ac976db5283aa064efc6a78cc5e/2025-08-12_10-32-44.png)
