---
URL: https://bitwarden.com/help/cli-auth-challenges/
---

# CLI Authentication Challenges

The August 2021 release of Bitwarden (**2021-09-21**) introduced [Captcha](https://www.hcaptcha.com/about) requirements to increase security against bot traffic. On the CLI, Captcha challenges are substituted with authentication challenges that can validated using your account's [personal API key](https://bitwarden.com/help/personal-api-key/) `client_secret`.

> [!NOTE] bwlogin api key
> **For automated workflows or for providing access to an external application**, we recommend using the `bw login --apikey` [method](https://bitwarden.com/help/cli/#using-an-api-key/). This method follows a more predictable authentication flow and revoking an application or machine's access can be achieved by rotating the [API key](https://bitwarden.com/help/personal-api-key/#rotate-your-api-key/).

## Get your personal API key

To get your personal API key:

1. In the Bitwarden web app, navigate to **Settings** → **Security** → **Keys**:

![Keys settings](https://bitwarden.com/assets/3IHpaOpEB5a13TF3B3RqqB/fab175095404a90d9d372542745bb9bb/Keys_settings.png)
2. Select the **View API key** button and enter your master password to validate access.
3. From the **API key** dialog box, copy the **client_secret:** value, which is a random string like `efrbgT9C6BogEfXi5pZc48XyJjfpR`.

## Answering challenges

Depending on your preferences, you can [save an environment variable](https://bitwarden.com/help/cli-auth-challenges/#answer-challenges-with-an-environment-variable/) to automatically pass authentication challenges or [manually enter](https://bitwarden.com/help/cli-auth-challenges/#using-the-prompt/) your `client_secret` whenever a challenge is made:

### Answer challenges with an environment variable

Authentication challenges will look for a non-empty environment variable `BW_CLIENTSECRET` before prompting you to enter one manually. Saving this variable with the [retrieved client_secret value](https://bitwarden.com/help/cli-auth-challenges/#get-your-personal-api-key/) will allow you to automatically pass authentication challenges. To save this environment variable:

🐧 🍎 Bash

```
export BW_CLIENTSECRET="client_secret"
```

🪟 PowerShell

```
env:BW_CLIENTSECRET="client_secret"
```

> [!NOTE] Client secret value incorrect 
> If your `client_secret` is incorrect, you will receive an error. In most cases, this is because you have [rotated your API key](https://bitwarden.com/help/personal-api-key/#rotate-your-api-key/) since saving the variable. [Use the above steps](https://bitwarden.com/help/cli-auth-challenges/#get-your-personal-api-key/) to retrieve the correct value.

### Answer challenges manually

When an authentication challenge is made and no `BW_CLIENTSECRET` value is found, you will be prompted to manually enter your `client_secret` value:

![Login Prompt with Auth Challenge ](https://bitwarden.com/assets/6YPFmH0ALYCuKcpOs6yf8X/e12166c2a561203f4605401b716f89e6/cli-captcha-1-markup.png)

> [!NOTE] Client secret value incorrect 
> If your `client_secret` is incorrect, you will receive an error. In most cases, this is because you have [rotated your API key](https://bitwarden.com/help/personal-api-key/#rotate-your-api-key/) since saving the variable. [Use the above steps](https://bitwarden.com/help/cli-auth-challenges/#get-your-personal-api-key/) to retrieve the correct value.
