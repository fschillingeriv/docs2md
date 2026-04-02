---
URL: https://bitwarden.com/help/auto-fill-custom-fields/
---

# Autofill Custom Fields

Bitwarden can do more than just [autofill your usernames and passwords](https://bitwarden.com/help/auto-fill-browser/)! Bitwarden browser extensions can autofill [custom fields](https://bitwarden.com/help/custom-fields/) to simplify filling in security questions, PINS, and more.

Additionally, if your browser extension is having issues autofilling usernames and passwords for a particular site, using [linked custom fields](https://bitwarden.com/help/auto-fill-custom-fields/#using-linked-custom-fields/) can force an autofill.

> [!TIP] Name custom fields correctly.
> It's important to name the custom field correctly in order for autofill to work. [Learn more](https://bitwarden.com/help/custom-fields/#custom-field-names/).

To autofill custom fields:

1. Open the browser extension to the **Vault** view. This view automatically detects the website (for example, `myverizon.com`) of the page displayed in the open tab and surfaces any logins with corresponding URIs.
2. Select the **Fill** button on item that contains the custom field you want to autofill:

![Item with a custom field ](https://bitwarden.com/assets/4ExHyb45ZapKssCpRl6Uro/b8e686e8a58e0ed24f8aa58dd746253e/2024-12-03_09-55-22.png)

The browser extension will find any fields that match the [custom field name](https://bitwarden.com/help/custom-fields/#custom-field-names/) and autofill that field's value.

### Using linked custom fields

Linked custom fields can be used to solve issues where your browser extension can't autofill usernames and passwords for a particular site. To create and autofill a linked custom field:

1. In the **Custom fields** section of an item's **Edit** panel, choose **Linked** from the Field type dropdown.
2. In the **Name** input, [give the custom field a name](https://bitwarden.com/help/custom-fields/#custom-field-names/) that corresponds to the username or password's HTML form element `id`, `name`, `aria-label`, or `placeholder`.

> [!TIP] Use context menu for custom field name.
> You can get the right value by right-clicking the form element and using the **Copy Custom Field Name** context menu option:
> 
> ![Copy custom field name](https://bitwarden.com/assets/5nnPLqyzgAhDCinQNB0uUC/a721194f39f0a8fa919066d73ff9e2c8/2024-10-29_10-50-34.png)
3. Select **Add**.
4. Select **Username** or **Password** for the field's value depending on which credential you are having trouble autofilling. In many cases, you'll need to create a linked custom field for each.
5. **Save** the changes to the vault item.

Now that you have created one or more linked custom fields, you can autofill using the [method described in an earlier section](https://bitwarden.com/help/auto-fill-custom-fields/#auto-fill-custom-fields/). When you do, your browser extension will autofill the username, password, or both into the HTML form element given for a field Name.

## Special autofill scenarios

### HTML `<span>` elements

Typically custom fields are autofilled in HTML `<form>` or `<input>` elements, however Bitwarden browser extensions can autofill custom field values into the `innerText` of HTML `<span>` elements as well.

In order to autofill into a `<span>` element, the opening tag must have the `data-bwautofill` attribute. So, in the following scenario:

```
<span data-bwautofill id="myspan">Bitwarden is great.</span>
```

A custom field with **name:** `myspan` will replace `Bitwarden is great` with whatever is saved in the custom field's **value**.
