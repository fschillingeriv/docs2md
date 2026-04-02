---
URL: https://bitwarden.com/help/bitwarden-apis/
---

# Password Manager APIs

Bitwarden currently offers two APIs with differing sets of functionality and use-cases:

## Public API

The Bitwarden Public API provides organizations with a suite of tools for managing members, collections, groups, event logs, and policies.

The Public API is a RESTful API with predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

Learn more about the [Bitwarden Public API](https://bitwarden.com/help/public-api/) or view the [API Specification](https://bitwarden.com/help/api/) documentation.

## Vault Management API

The Vault Management API provides Bitwarden users with a suite of tools for managing vault items, including those owned by organizations provided you have the appropriate permissions.

The Vault Management API allows most actions that can be taken by the Bitwarden CLI to be taken in the form of RESTful API calls from an HTTP interface. Using the Vault Management API requires that you use the `serve` command from the CLI to start a local express web server from which to make requests.

> [!NOTE] Vault management API JSON requests
> The Vault Management API accepts JSON request bodies and returns JSON responses, including standard HTTP response codes.

Learn more about the [serve command](https://bitwarden.com/help/cli/#serve/) or view the [API Specification](https://bitwarden.com/help/vault-management-api/) documentation.
