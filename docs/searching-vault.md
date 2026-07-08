---
URL: https://bitwarden.com/help/searching-vault/
---

# Search your Vault

Bitwarden vaults can be searched to quickly surface relevant items. [Basic searches](https://bitwarden.com/help/searching-vault/#basic-search/) can be made in any Bitwarden app, and more advanced [full-text searches](https://bitwarden.com/help/searching-vault/#full-text-search/) can be made in the web vault, desktop app, and browser extension.

The results available for any search are dependent on what is currently opened through the filter menu or navigation, for example:

- If **All Items** is selected, searches will check all vault items for results.
- If **Login** is selected, searches will check all login items for results.
- If **My Folder** is selected, searches will check items in that folder for results (not including items in a [nested folder](https://bitwarden.com/help/folders/)).
- If a **Collection** is selected, searches will check for results within the selected collection.

The placeholder text in the search box will change to indicate the current search location:

![Search a folder](https://bitwarden.com/assets/2Mdb392zQHEfC44zhwLmGl/9d208498c67672f81c47b66a3084853e/2024-12-02_16-28-17.png)

## Basic search

Basic search is used by Bitwarden **mobile apps**. Entering search text (for example, `Github` or `myusername`) will look for the entered information in the following vault item fields:

- Item **name**
- For logins, **username**
- For logins, **URI**
- For cards, **brand** or last four digits of the **number**
- For identities, **name**

For your convenience, basic searches automatically include leading and trailing [wildcards](https://bitwarden.com/help/searching-vault/#wildcards-and-advanced-search-parameters/). For example, searching for `mail` will return items with the name `gmail` as well as `email`. 

Search results are determined by a simple scoring mechanism. The more fields a search term appears in, the high that vault item's score. [Learn more](https://lunrjs.com/guides/searching.html#scoring). 

## Full-text search

Searches in the web app, desktop app, and browser extension are automatically full-text and, like basic searches, automatically include leading and trailing wildcards. When results aren't found in a full-text search, Bitwarden will fall back to a basic search.

### Indexed fields

Full-text search will search the following fields for every vault item:

- `shortid`: First eight characters of the item's ID.
- `organizationid`: ID of the item's organization (if it belongs to one).
- `name`: Item's designated name.
- `subtitle`: Depending on item type; login **username**, card **brand** or last four digits of the **number**, or identity **name**.
- `notes`: Item's notes. Only full-word matches will be listed unless you [use wildcards](https://bitwarden.com/help/searching-vault/#wildcards-and-advanced-search-parameters/).
- `fields`: Name or value. Only `**Text**` type field values are included.
- `attachments`: Name of the attached file.
- `login.username`: Login item's username.
- `login.uris`: Login item's URI [hostname](https://developer.mozilla.org/en-US/docs/Web/API/HTMLHyperlinkElementUtils/hostname) value.

### Searching specific fields

You can search for data in specific fields by starting a search query with the "greater than" (`>`) character and indicating a field as previously listed in the following format:

- `>login.username:jsmith` will search for login items with `jsmith` specified as the **username**.
- `>+name:Turbo +name:Tax` will search for any vault items with the words `Turbo` and `Tax` included in the **name**, however would also return an item with a name that includes additional words, like `Turbo Fast Tax Service`.
- `>+name:Turbo +name:Tax -name:Fast` will filter the results of the above example to exclude any item that *also* includes the term `Fast` in its name, like `Turbo Fast Tax Service`.

If no field indicator is present, all indexed fields will be searched.

### Wildcards and advanced search parameters

When searching specific fields, you can apply the asterisk (`*`) as a wildcard character for specified search values, for example:

- `>organizationid:*` will search for all vault items that belong to an organization.
- `>-organizationid:*` will search for all vault items that do not belong to an organization.
- `>login.username:*@gmail.com` will search for any login item **username** that ends in `@gmail.com`.
- `>wild*`: Will search for all vault items that contain the word `wild` and vault items with words that contain `wild`, for example `wildcard` .

> [!TIP] Lunr Advanced Tips
> [Lunr](https://lunrjs.com/) provides a variety of advanced query options beyond wildcards, including:
> 
> - **Term presence** using a `+` (must contain) or `-` (must not contain) prefix. When searching based on term presence, each term should be treated separately, even if they're separated by hyphens (`-`).
> 
> For example, if you have multiple Gmail accounts, searching `>+name:Gmail +name:Work` **would** return a vault item with the name `Work Gmail` but **would not** return a vault item with the name `Personal Gmail`. If you use hyphens (`-`) in item names, for example `Work-Gmail`, do not include the hyphen as a search term.
> 
> Term presence can be used for **exact** searches. For example, searching `>+name:5 +name:mail +name:01` would create an exact match for `5-mail-01`.
> - **Fuzzy matching** using a tilde (`~`) prefix combined with an edit distance integer.
> 
> For example, searching `>name:email~1` would return both vault items with the name `email` **and** vault items with the name `gmail`.
> 
> Learn more about writing advanced search queries using [Lunr's Searching Guide](https://lunrjs.com/guides/searching.html).
