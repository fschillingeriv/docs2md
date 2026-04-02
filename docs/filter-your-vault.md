---
URL: https://bitwarden.com/help/filter-your-vault/
---

# Filter your Vault

Filtering your vault will control which items will be listed in the Vault or Vaults views. To control vault filtering:

### Web app

Either:

- Select a characteristic from the **Filter**column (in the following screenshot, **Login**).
- Select one of the colored cards next to an item (in the following screenshot, either **Me**or **My Organization**).

![Web app filtering](https://bitwarden.com/assets/1UhfLlwmahJgbi0bcBtPLT/b4b1875602b0ea555626c98a388779b8/2024-12-02_14-23-39.png)

### Browser extension

Use the **Vault**, **Collection**, **Folder**, or **Type** selectors at the top of the 🔒 **Vault** tab. You toggle the visibility of the filter dropdown menus with the 🎚️ button:

![Browser extension filters and suggestions](https://bitwarden.com/assets/12UsFuA2sxbUCBMIczJsxv/689221013fac56ddb555ed9dabddbdc9/screenshot_6.png)

### Mobile

Choose a vault by selecting the **Vault**menu button (⋯ ) on the **Vaults**tab:

![Filter vaults on mobile](https://bitwarden.com/assets/44WqYfqzP9JOJPSZ4Yrzjb/9167f19bc2e27a158be5ed3fc29a5689/2025-01-21_15-38-59.png)

### Desktop

Select a vault from the left-most column (in the following screenshot, **My Vault**or **My Organization**):

![Filtering on desktop](https://bitwarden.com/assets/2Lng0L2TRQ177CaU8EUQ1m/fc80b9452396db84c9f1abd405275ddb/2026-01-28_10-20-04.png)
*Filtering on desktop*

### CLI

Use the `bw list` command with the `--organizationid` option, which can take either an organization identifier or `null`, to list items by vault. [Learn more](https://bitwarden.com/help/cli/#list/).
