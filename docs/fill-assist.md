---
URL: https://bitwarden.com/help/fill-assist/
---

# Fill Assist

Fill assist **improves autofill accuracy on a Bitwarden-curated selection of websites**, those known to widely cause autofill issues for users, by providing human-written and reviewed instructions that your browser extension can use to determine how to autofill credentials.

Often, websites cause autofill issues because they deviate from a widely-adopted set of norms found in the code for login or account creation forms. Fill assist solves this problem by allowing Bitwarden to identify sites that behave differently and create custom instructions for how browser extensions should autofill on those sites.

## Turn on fill assist

Fill assist can be turned on for Bitwarden browser extensions from the **Settings** → **Autofill** menu and is available for all users on version 2026.6.0 or later. 

> [!NOTE] Fill assist, keep reading for more details.
> No further action is required! Once turned on, you should observe better autofill performance on sites included the curated list. The rest of the article covers more detail about how fill assist works.

Because fill assist is one method for facilitating easier autofill, [custom fields](https://bitwarden.com/help/custom-fields/) are superseded by sites that are fill assisted.

## How it works

Powered by the [Map the Web](https://github.com/bitwarden/map-the-web/) project, fill assist is one of several tools built to resolve autofill issues. It does this by substituting the default autofill logic with human-written and reviewed instructions for how autofill should behave on any site that it supports. Let's break that down:

- **Supported sites**: Fill assist only steps in when the site you're browsing is included in the maps; typically, these are websites that are broadly reported to cause autofill issues for Bitwarden users.
- **Substituting for default logic**: When autofilling on one of those supported sites, fill assist instructs browser extensions to ignore the typical heuristics, including user-created [custom fields](https://bitwarden.com/help/custom-fields/), that they look in favor of a more targeted alternative.
- **Human-written instructions**: Fill assist uses a map of CSS selectors, that has been written and reviewed by humans, to describe where Bitwarden should autofill which credentials on a fill assisted site.

Those maps are retrieved by your browser extension client on every sync or every 6 hours in order to keep up-to-date with the latest fill assist instructions. As a result, there are two key things to note:

- **Data privacy**: Once retrieved, your browser extension stores this file locally so that **no data needs to be or is sent to Bitwarden** when an autofill action uses a fill assist.
- **Independent of client release**: Because the browser extension recurrently retrieves the latest map, you won't need to wait for a client release in order for a new or updated instruction to take effect.

### Report an issue

Please also note that, because fill assist instructions are targeted on specific CSS selectors on a form, they are liable to stop working when the maintainers of that website make changes. We encourage all users to continue to [report autofill issues](https://docs.google.com/forms/d/e/1FAIpQLSfkxh1w6vK8fLYwAbAAEVhvhMAJwfFNDtYtPUVk1y5WTHvJmQ/viewform), as some reports may be good candidates for updating or adding fill assist instructions.
