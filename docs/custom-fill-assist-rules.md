---
URL: https://bitwarden.com/help/custom-fill-assist-rules/
---

# Custom Fill Assist Rules

Enterprise organizations can [use a policy](https://bitwarden.com/help/policies/#activate-fill-assist/) to set a default [fill assist](https://bitwarden.com/help/fill-assist/) state for members and, optionally, replace the Bitwarden-curated fill assist rules with a ruleset hosted and maintained by the organization. 

This article covers building a custom ruleset. Refer to the links above for articles covering how fill assist and the associated policy work in practice.

## Custom rulesets

By default, fill assist will use a ruleset curated by Bitwarden. You might want to iterate on, or replace, that ruleset to expand coverage to the websites and applications that members of your organization use most often. Intranet sites, for example, are one good reason for building and maintaining a custom ruleset.

### Ruleset contents

Custom rulesets are a **directory**, not a single file. When you provide the policy a **custom autofill ruleset** URL, you must provide a link to that **directory**. Clients using fill assist expect four files in the ruleset directory:

- `forms.v1.json`: Your rules data.
- `forms.v1.schema.json`: Schema of your rules data.
- `manifest.json`: Build metadata and per-map schema version.
- `manifest.schema.json`: Schema of the manifest.

Your custom ruleset must be served to clients over HTTPS. Clients will re-fetch a ruleset every 6 hours to ensure your members are getting up-to-date rules.

### Rules in the ruleset

> [!TIP] Link to the map-the-web repo
> We'll cover the basics of rule creation in this article, however the [Map the Web](https://github.com/bitwarden/map-the-web/) repository maintained by Bitwarden includes comprehensive information on structuring rules. We recommend using that repository's README when writing custom rules.

Rules are written in JSON. Each rule lives under a `host` (i.e. a domain) and describes the form(s) on that host's page using CSS selectors. 

```javascript
{
 "schemaVersion": "1.0.0",
 "hosts": {
 "example.com": {
 "forms": [
 {
 "category": "account-login",
 "container": ["form#login-form"],
 "fields": {
 "username": ["input#email"],
 "password": ["input#password"]
 },
 "actions": {
 "submit": ["button[type='submit']"]
 }
 }
 ]
 }
 }
}
```

A rule typically includes four pieces:

| Key | Value | Required? |
|------|------|------|
| `category` | What type of form this is, `account-login`, `account-creation`, `payment-card`, `address`, and so on. | Yes |
| `container` | The element that wraps the form, typically `<form>` tags. | No |
| `fields` | A fixed set of keys mapped to one or more CSS selectors. Refer to the following section for more information | Yes |
| `actions` | Buttons or other interactive elements, such as `submit` or `next`. | No |

When a host has multiple forms that are structured differently, add `pathnames` to specific rules that supersede the global rules for that host:

```javascript
"example.com": {
 "forms": [ /* the rule for every other page */ ],
 "pathnames": {
 "/login": {
 "forms": [ /* a completely different rule, just for this page */ ]
 }
 }
}
```

#### Fields

Fields join a fixed set of keys, for example `username`, `password`, `email`, `firstName`, and `cardNumber`, to CSS selectors represented as corresponding values, for example:

```javascript
"fields": {
 "username": ["input#email"],
 "password": ["input#password"]
}
```

In this example, `username` is the key chosen from a discrete list of available options and `input#email` is the CSS selector, represented in an array because field keys may be mapped to multiple selectors:

```javascript
"username": ["input#email", "input[autocomplete='username']"]
```

> [!TIP] Write fill assist rules to be brittle
> Write fields to be **intentionally brittle**. Each selector is a record of exactly what a specific field looks like *today*, if the page changes underneath it you want the rule to **break**, not adapt, in order to send a deliberate signal that a human should review it. A selector that keeps matching through a change could just as easily be pointing at the wrong thing now, with nothing to catch it.

## Build a custom ruleset

In order to build a custom ruleset, the recommended procedure is:

1. Fork the `github.com/bitwarden/map-the-web` repository.
2. In the fork, edit `maps/forms/forms.jsonc` to fit your organization's needs. It's recommended that existing entries are kept intact and that new entries are added according to the formatting instructions in the prior section.
3. Validate and build with `npm run check && npm run build`. A passing build emits the minified artifacts and manifests expected by the clients.
4. Publish the build artifacts so that all four expected files sit together in a single HTTPS-reachable directory. A GitHub Release is a good example of a straightforward path to doing so.
5. Point your policy's **custom autofill ruleset** at the HTTPS-reachable directory, [from the UI](https://bitwarden.com/help/policies/#activate-fill-assist/) if you're cloud-hosted or [using an environment variable](https://bitwarden.com/help/environment-variables/#optional-variables/) if you're self-hosted. If you used GitHub, this would look something like `https://github.com/<your-org>/forked-map-the-web/releases/latest/download/`.

## Maintain a custom ruleset

Using a custom ruleset in the way described in this document will fully replace the ruleset curated by Bitwarden, keeping your fork current is your responsibility. Note that a fork that isn't regularly synced with the upstream curated repository will quietly drift as Bitwarden adds and corrects rules over time. Pull upstream changes regularly.

### Ruleset validation

There is currently no error reporting that would surface a malformed ruleset. If your ruleset URL is unreachable, returns an error, or serves invalid JSON, fill assist will silently do nothing for affected members, with no fallback to the Bitwarden-curated ruleset. To validate your ruleset is working properly:

1. Open each of the four files directly in a browser and confirm they return valid JSON over HTTPS.
2. Confirm `manifest.json` reports the schema version you expect.
3. Test on a page you know your ruleset covers. Clients only re-fetch every 6 hours, so allow time for a fix to take effect before re-testing.
4. If you're unsure whether the custom ruleset is the cause of an issue, temporarily point the policy back at Bitwarden's default rules URL to isolate the issue.

### Version pinning

Policy setup in the Bitwarden Admin Console will take one URL, but which URL you use can determine how much control you have over when ruleset changes reach members' clients. If you're using GitHub Releases, you have at least two options: 

1. **Always latest**. Set the URL to the following so that clients always pull whatever artifacts you've published most recently. Useful if you want an automatic process for fixes and new coverage to reach clients.

```plain text
https://github.com/<your-org>/forked-map-the-web/releases/latest/download/
```
2. **Pin a version**. Set the URL to the following so that clients stay on that exact version of the artifacts until you update the field in the Bitwarden Admin Console. Useful for a higher level of control.

```plain text
https://github.com/<your-org>/forked-map-the-web/releases/download/v20260904.1/
```

### Security considerations

When using a custom ruleset, your organization owns the security and correctness of rules. Bitwarden does not vet, review, or validate custom rules or rulesets, that content is fetched and applied to members' clients as authored. All implementations of custom rulesets should:

- Be hosted on infrastructure that your organization controls.
- Treat write access to that location as a sensitive permission.
- Include a process for reviewing rule changes before publishing new artifact versions.

Understand that compromised or neglected rulesets affect autofill behavior for every member with fill assist active, on every site that rules are constructed for. In order to fix autofill on broken and poorly constructed forms, fill assist rules can intentionally bypass field-visibility checks, field-type checks, and clickjacking protections. This means a maliciously or poorly written rule could cause credentials to be filled where they shouldn't.
