---
URL: https://bitwarden.com/help/secrets-manager-sdk/
---

# Secrets Manager SDK

The Bitwarden software development kit (SDK) can help developers create applications for secrets management. The Bitwarden SDK is used by the Bitwarden team to build discrete integrations with popular products, like [GitHub Actions](https://bitwarden.com/help/github-actions-integration/), and can be used by the community to build applications of their own. 

The core SDK, [found here](https://github.com/bitwarden/sdk-sm/), is written in Rust and provides Rust API, CLI, and Node-API bindings. Rust was selected due to its memory safety, multitude of bindings to programming languages we plan to build integrations on, and its support of WebAssembly. Language wrappers can be used for the following languages:

- [C++](https://github.com/bitwarden/sdk-sm/tree/main/languages/cpp#readme)
- [C#](https://github.com/bitwarden/sdk-sm/tree/main/languages/csharp#readme)
- [Go](https://github.com/bitwarden/sdk-sm/tree/main/languages/go#readme)
- [Java](https://github.com/bitwarden/sdk-sm/tree/main/languages/java#readme)
- [JS](https://github.com/bitwarden/sdk-sm/tree/main/languages/js)
- [PHP](https://github.com/bitwarden/sdk-sm/tree/main/languages/php#readme)
- [Python](https://github.com/bitwarden/sdk-sm/tree/main/languages/python#readme)
- [Ruby](https://github.com/bitwarden/sdk-sm/tree/main/languages/ruby#readme)

The SDK, like the Secrets Manager CLI built on-top of it, can be used to execute the following operations:

- Authenticate using an [access token](https://bitwarden.com/help/access-tokens/).
- Retrieve a single [secret](https://bitwarden.com/help/secrets/) or all secrets in a [project](https://bitwarden.com/help/projects/).
- List all secrets, secrets in a project, or projects.

> [!TIP] SM Demo 2
> To see the Python SDK in action, join a live Secrets Manager demo and Q&A! [Register here](https://us02web.zoom.us/webinar/register/WN_8kM9dK4FT6y0Z95G16nN5w#/registration).
