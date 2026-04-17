---
URL: https://bitwarden.com/help/link-to-an-item/
---

# Hyperlink Organization Items

When you need to direct members of your organization to a specific* *vault item, for example in documentation, you can copy the URL of an item to be used as a direct link for users that **have access to the item**.

> [!TIP] Linkable Items for Personal Use
> Item linking is not exclusive to organizations! You can save links to items in your individual vault if you find it useful, but only you will be able to access them.

When you are viewing an item in the web vault, the URL in your address bar will include a query parameter like `?itemnrId=fced56b3-d83c-4b01-8751-ae9301551da7`, where the `itemId` value represents the unique item identifier:

![Item link](https://bitwarden.com/assets/6v3WH6FljmTFOlSqOjjAqZ/a9c1ae50155e6692d52987fe4f0cc888/2024-12-04_09-55-51.png)

Copy the full value in the address bar and use that link to direct organization members directly to this item. Users **must already have access to the item**in order to successfully use a link.

> [!NOTE] You'll need to log in
> Unless the user opens that link in a browser tab that is already logged in to Bitwarden, **they'll need to log in**. Most browsers, for example, default to opening a clicked-link in a new tab and therefore would require the user to log in. Once they log in, the vault item will be automatically opened.
