---
URL: https://bitwarden.com/help/personal-api-key/
---

# CLI Authentication via API Key

Your Bitwarden personal API key can be used as a method for authenticating into the command line interface (CLI).

> [!NOTE] Personal API key vs organization API key
> Your personal API key is **not the same** as the [organization API key](https://bitwarden.com/help/public-api/#authentication/) used to access the [Bitwarden Public API](https://bitwarden.com/help/public-api/) or [Directory Connector](https://bitwarden.com/help/directory-sync/). Personal API keys will have a `client_id` with format `"user.clientId"`, while organization API keys will have a `client_id` with format `"organization.ClientId"`.

## Get your personal API key

To get your personal API key:

1. In the Bitwarden web app, navigate to **Settings** → **Security** → **Keys**:

![Keys settings](https://bitwarden.com/assets/3IHpaOpEB5a13TF3B3RqqB/fab175095404a90d9d372542745bb9bb/Keys_settings.png)
*Keys settings*
2. Select the **View API key** button and enter your master password to validate access. Once entered, you will be provided the following:

 - `client_id: "user.clientId"` (This value is unique to your account and does not change.)
 - `client_secret: "clientSecret"` (This value is unique and can be rotated).
 - `scope: "api"` (This value will always be `"api"`).
 - `grant_type: "client_credentials"` (This value will always be `"client_credentials"`).

### Rotate your API key

Select the **Rotate API Key** button to rotate your personal API key. Rotating your key will only change your `client_secret`.

Rotating your key will invalidate your previous key and all active sessions using that key.

## Authenticate using your API key

Using the [personal API key](https://bitwarden.com/help/personal-api-key/) for CLI authentication is suitable for automated workflows, for providing access to an external application, or if your account uses a 2FA method not supported by the CLI (FIDO2 or Duo). The following command will prompt you for your personal `client_id` and `client_secret`:

```
bw login --apikey
```

While there are some commands that do not require your data be decrypted, to use many of the CLI commands you will need to subsequently decrypt your data using the `unlock` command ([learn more](https://bitwarden.com/help/cli/#unlock/)), unless you're a member of an organization using [Key Connector](https://bitwarden.com/help/about-key-connector/). Your API key is **not a substitute for your master password.**

#### Using API key environment variables

In scenarios where automated work is being done with the Bitwarden CLI, you can save environment variables to prevent the need for manual intervention at authentication.

| **Environment variable name** | **Required value** |
|------|------|
| BW_CLIENTID | `client_id` |
| BW_CLIENTSECRET | `client_secret` |
