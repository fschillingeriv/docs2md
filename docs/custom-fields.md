---
URL: https://bitwarden.com/help/custom-fields/
---

# Custom Fields

Custom fields, available for any [vault item type](https://bitwarden.com/help/managing-items/), allow you to store additional well-structured data fields for a vault item. Custom fields are saved as `Name:Value` pairs, and can be one of four types:

- **Text**: Field value stores a freeform input (text, numbers, and more).
- **Hidden**: Field value stores freeform input that is hidden from view (particularly useful for organizations using [hidden passwords permissions](https://bitwarden.com/help/collection-permissions/)).
- **Checkbox**: (**Boolean** on some clients) Field value stores a boolean value (true/false).
- **Linked**: Field value is linked to the item's username or password. Given the [right field name](https://bitwarden.com/help/custom-fields/#custom-field-names/), linked custom fields can be used to solve issues where your browser extension can't autofill usernames and passwords for a particular site ([learn more](https://bitwarden.com/help/auto-fill-custom-fields/#using-linked-custom-fields/)).

> [!NOTE] custom fields for keys
> **Custom fields for keys**
> 
> In addition to common web service inputs like PINs and security questions, custom fields can be used to store values up to 5000 characters in length, for example RSA 4096-bit SSH keys.
> 
> Character limits for custom field values are imposed on the **post-encryption character count**. For example, a 3383-character RSA-4096 Private SSH key would grow to about 4400-characters when it's encrypted and stored in your Vault.

## Creating custom fields

Custom fields can be added to a vault item from any Bitwarden client using the **Custom Fields** section of the **Edit Item** panel:

![Custom fields in web app](https://bitwarden.com/assets/NoGCwyAZcnzss1EeYXKD1/23a7e619dfdcb4baa023f54923335050/2024-12-02_14-52-43.png)

### Custom field names

The specified **Name** is important to get right in order to successfully [autofill a custom field](https://bitwarden.com/help/auto-fill-custom-fields/). Using the Bitwarden browser extension, you can quickly get the correct field name using the **Copy custom field name** option in the context menu (in most cases, by right-clicking on the form element):

![Copy custom field name](https://bitwarden.com/assets/5nnPLqyzgAhDCinQNB0uUC/a721194f39f0a8fa919066d73ff9e2c8/2024-10-29_10-50-34.png)

Selecting this context menu option will copy the form element's `id`, `name`, `aria-label`, or `placeholder` value (in that order of preference).

Once you have saved a custom field, you can [autofill it from the browser extension](https://bitwarden.com/help/auto-fill-custom-fields/).

#### Find custom field names manually

If you don't use the browser extension, the best way to find a field name is to use your web browser's developer tools, as in the following example:

[![Vimeo Video](https://vumbnail.com/1139125687.jpg)](https://vimeo.com/1139125687)
*[Watch on Vimeo](https://vimeo.com/1139125687)*

To locate a custom field name:

1. On the webpage with the custom field, right-click the field you want to autofill and select **Inspect**. The HTML element will open and be highlighted in the developer console.
2. Find and copy the element `id` (find `id="xxx"`, where `xxx` is the element's `id` value).
3. In the relevant vault item's **Custom fields** section, choose the appropriate field type and select the + **New custom field** button.
4. Paste the copied element `id` in the **Name** field.
5. Specify the desired information to be autofilled (in the above example, a telephone number) in the **Value** field.
6. Save the vault item.

Once you have saved a custom field, you can [autofill it from the browser extension](https://bitwarden.com/help/auto-fill-custom-fields/).

### More about custom field names

#### Order of preference

If you are naming a custom field manually, you should use one of the following HTML form element attributes/values **in order of preference**:

1. HTML form element's `id` attribute.
2. HTML form element's `name` attribute.
3. HTML form element's `aria-label` attribute.
4. HTML form element's `placeholder` attribute.

#### Matching

Field name matching is an **exact** and **case-insensitive** comparison. For example, if your custom field has the name `PIN`:

- **Autofill is offered** for `pin`, `PiN`, `PIN`, etc.
- **Autofill is not offered** for `pin2` or `mypin`

#### Prefixing

There are two cases in which you can exercise more control over [matching](https://bitwarden.com/help/custom-fields/#matching/) by using prefixes:

- **csv**: Prefixing your custom field's name with `csv=` allows you to specify multiple names to search for and compare against for autofill, for example `csv=pin,mypin,pincode`.
- **regex**: Prefixing your custom field's name with `regex=` allows you to perform [regular expression comparisons](https://regexone.com) when auto-fill is performed. For example, `regex=^first.*name` will offer autofill for `firstName`, `First_name`, and `First Name`.
