---
URL: https://bitwarden.com/help/generator/
---

# Username & Password Generator

Use the Bitwarden generator tool to easily create strong passwords and unique usernames. The password generator is available in all Bitwarden apps and the username generator is available in the web vault, browser extension, desktop app, and mobile app.

If you are not a current Bitwarden user, you can also test our free password generator at [https://bitwarden.com/password-generator/](https://bitwarden.com/password-generator/).

## Generate a password

To generate a strong password:

### Web app

Select **Tools** → **Generator**from the navigation:

![Web app password generator](https://bitwarden.com/assets/70bx0hWvxAvkz5RJdIj04n/63febc4043e13292461c768d910cd450/2025-02-14_11-00-10.png)

The [options you specify](https://bitwarden.com/help/generator/#password-types/) on this page will be saved until you log out of the web app. You can also quickly generate a strong password using those same options directly from the Add or Edit Item screens using the [generate] **Generate**button:

![In-item password generator](https://bitwarden.com/assets/5ZVBOSK13MaXJ2S8iJTOMX/1324db87fd867667cbb6e8c1c1f4539a/2024-12-02_14-44-30.png)

> [!NOTE] Generator history
> Select [**Generator history**](https://bitwarden.com/help/password-and-generator-history/#generator-history/) to access passwords and usernames created in either location with that specific client—even if you don't save them to an item. This history is cleared when you log out.

### Browser extension

Select the [generate] **Generator** tab:

![Browser extension password generator](https://bitwarden.com/assets/6eOmI3kZOdnfw9i5JinfUD/f1a7129244f49c7d904664632e329076/2024-10-29_10-34-01.png)

You can also generate a strong password from the Edit screen using the [generate] **Generate**button:

![Browser extension password generator](https://bitwarden.com/assets/2Cbja6OBxW2S6GVxLOqlYh/b71de03b37f5a4f4960e344a5b17cc01/2024-10-29_10-35-25.png)

If you're creating an account that isn't stored in Bitwarden, you can also use the inline autofill menu to generate and autofill a password using the **Fill generated password** prompt:

![Fill generated password](https://bitwarden.com/assets/2JcceqWgFbk4ViLCMe6qm5/ce116e8ff337f90fbbd57b52aa15fdcd/2024-11-05_10-07-08.png)

When using inline, use the [generate] generate button to generate a new password until you're satisfied with it. Inline password generation uses the settings from the browser extension's **Generator** tab. Make sure you select **New login** when prompted to save the login to Bitwarden. [Learn more](https://bitwarden.com/help/auto-fill-browser/#use-the-inline-autofill-menu/).

> [!NOTE] Generator history
> Select [**Generator history**](https://bitwarden.com/help/password-and-generator-history/#generator-history/) to access passwords and usernames created in either location with that specific client—even if you don't save them to an item. This history is cleared when you log out.

### Desktop

Select **Generator** from the navigation menu:

![Desktop App Password Generator](https://bitwarden.com/assets/6cFQ3iojZXLy1ZIdIXp6Zr/cfff50e193c533ef1bbc09c489693e9e/2026-01-28_10-59-21.png)
*Desktop App Password Generator*

You can also generate a strong password from the Add/Edit Item screen using the [generate] **Generate**button:

![Desktop App Password Generator](https://bitwarden.com/assets/6VInVRr9tZBOndfe4VrpXf/b57e2bd43fad800bc010ebf767d26784/2026-01-28_11-06-53.png)
*Desktop App Password Generator*

> [!NOTE] Generator history
> Select [**Generator history**](https://bitwarden.com/help/password-and-generator-history/#generator-history/) to access passwords and usernames created in either location with that specific client—even if you don't save them to an item. This history is cleared when you log out.

### Mobile

Select the [generate] **Generator** tab:

![Password generator on mobile](https://bitwarden.com/assets/Cqrt6OGquQLRJvZDuqtCk/5b42dad11498bc5c62a749c4fc096fc9/2025-01-21_15-49-19.png)

You can also generate a strong password from the Add/Edit Item screen, as well as from the iOS app extension accessible by tapping the Share icon, using the [generate] **Generate**button:

![Password generator on mobile](https://bitwarden.com/assets/4NeVmiRcKfedg6Fzwp0N1Y/f91ad1097dcd379925cedee724dc7592/2025-01-21_15-51-01.png)

> [!NOTE] Generator history
> Select [**Generator history**](https://bitwarden.com/help/password-and-generator-history/#generator-history/) to access passwords and usernames created in either location with that specific client—even if you don't save them to an item. This history is cleared when you log out.

### CLI

Use the generate command to generate a password:

```
bw generate -uln --length 14
```

Additional options flags for generated passwords include:

- `--minNumber`
- `--minSpecial`
- `--ambiguous`

For more information, please refer to the Bitwarden [CLI documentation](https://bitwarden.com/help/cli/).

### Password types

#### Password

Passwords are randomly generated strings of a customizable set of character types. Options for passwords include:

- **Length**: Number of characters in your password.
- **Minimum numbers**: Minimum number of numbers in your password if **0-9**is enabled.
- **Minimum special**: Minimum number of special characters in your password if **!@#$%^&*** is enabled.
- **A-Z**: Include uppercase letters in your password.
- **a-z**: Include lowercase letters in your password.
- **0-9**: Include numbers in your password.
- **!@#$%^&***: Include special characters in your password.
- **Avoid ambiguous characters**: Prevent your passwords from having both a `1` and `l` or both a `0` and `o`.

> [!WARNING] PW Generator Options & Entropy
> Unless you need to satisfy a site's specific password requirements, we recommend keeping **Minimum Numbers** and **Minimum Special**as low as possible (0-1) as over-constraint limits the strength of generated passwords.

#### Passphrase

Passphrases are randomly generated groups of words, for example `panda-lunchroom-uplifting-resisting`. Options for passphrases include: 

- **Number of words**: Number of words in your passphrase.
- **Word separator**: Character to use to separate words in your passphrase (`-` in the above example).
- **Capitalize**: Capitalize the first letter of each word in your passphrase.
- **Include number**: Include a single numerical character in your passphrase.

## Generate a username

To generate a username:

### Web app

Select **Tools** → **Generator**from the navigation:

![Web app username generator](https://bitwarden.com/assets/2862v5xPV5qQM7XfdUvNlI/0f8fe47b6d9efb0a6d77b245a1f63cdf/2025-02-14_11-02-02.png)

You can also generate a username from the Edit screen using the [generate] **Generate**button: 

![Web app username generator](https://bitwarden.com/assets/1zpNFR8fu9DBo2krqln5hr/e893f1f3e8d85d58d20c8e316f247666/2024-12-02_14-44-30.png)

> [!NOTE] Generator history
> Select [**Generator history**](https://bitwarden.com/help/password-and-generator-history/#generator-history/) to access passwords and usernames created in either location with that specific client—even if you don't save them to an item. This history is cleared when you log out.

### Browser extension

Select the [generate] **Generator** tab and choose **Username**:

![Browser extension username generator](https://bitwarden.com/assets/3WEaJYUplgEdjgoSxlQ842/40d3eed8347cb6b0a600d06f42cc1941/2024-10-29_10-39-00.png)

You can also generate a username from the Edit screen using the [generate] **Generate**button: 

![Browser extension username generator](https://bitwarden.com/assets/23CDvd3ErFQIZNYwgh000F/c19c373ecb6ca2d6aad2587a1b16dd12/2024-10-29_10-39-56.png)

> [!NOTE] Generator history
> Select [**Generator history**](https://bitwarden.com/help/password-and-generator-history/#generator-history/) to access passwords and usernames created in either location with that specific client—even if you don't save them to an item. This history is cleared when you log out.

### Desktop

Select **Generator** from the navigation menu:

![Desktop App Username Generator](https://bitwarden.com/assets/2VGPd4WOwydbovDJdyVT51/3f27f0390d85b8622e6b1baae611d3fc/2026-01-28_11-10-11.png)
*Desktop App Username Generator*

You can also generate a username from the Add/Edit Item screen using the [generate] **Generate**button:

![Desktop App Username Generator](https://bitwarden.com/assets/7xTg7VVE7CgTZhBl5LlYui/b40a5255fcef08a3d17c3bad13c34f16/2026-01-28_11-13-24.png)
*Desktop App Username Generator*

> [!NOTE] Generator history
> Select [**Generator history**](https://bitwarden.com/help/password-and-generator-history/#generator-history/) to access passwords and usernames created in either location with that specific client—even if you don't save them to an item. This history is cleared when you log out.

### Mobile

Select the [generate]**Generator** tab:

![Username generator on mobile](https://bitwarden.com/assets/6nfsTiHypQvXrfz7qI7AKI/6e41b1fedea81895497268b0fd825215/2025-01-21_15-56-24.png)

You can also generate a username from the Add/Edit item screen, as well as from the iOS app extension accessible by tapping the Share icon, using the [generate]**Generate**button:

![Username generator on mobile](https://bitwarden.com/assets/2Obfpm7UdBizkwASepMS6j/998c1448556484b867160f7412aa984c/2025-01-21_15-51-01.png)

### Username types

#### Plus Addressed Email

Select this type to use your email provider's sub-addressing (aka "plus addressing" or "aliasing") capabilities. This will generate a plus addressed (named for the `+` and random string of characters) username based on your specified email address.

On the Add/Edit Item screen of the browser extensions, mobile, and desktop apps, you can select between generating username with a **Random**(for example, `alice+gsd4aqqe@bitwarden.com`) string or one based on the item's **email address** (for example, `alice+github.com@bitwarden.com`). **Email address** is limited to browser and desktop as it requires knowledge of the login's [URI](https://bitwarden.com/help/uri-match-detection/), in other locations the username generator will default to **Random.**

> [!NOTE] Why use plus addressing?
> **Why use plus addressed email?**
> 
> Plus addressed emails allow you to filter your email for all the junk mail you get when signing up for a new service. Signing up for a service with the username `alice+rnok6xsh@bitwarden.com` will still send emails to `alice@bitwarden.com`, but you can easily filter emails that include `+rnok6xsh` to prevent them from clogging up your inbox.

#### Catch-all email

Select this type to use your domain's configured catch-all inbox. This will generate a random email address at your specified **Domain.**

On the Add/Edit Item screen of browser extensions and desktop apps, you can select between generating username with a **Random**(for example, `bqzjlero@gardenllc.com`) string or one based on the item's **Domain Name** (for example, `Instagram.com@gardenllc.com`). **Domain Name** is limited to browser and desktop as it requires knowledge of the login's [URI](https://bitwarden.com/help/uri-match-detection/), in other locations the username generator will default to **Random.**

> [!NOTE] Why use catch-all email
> **Why use catch-all email?**
> 
> In some cases, catch-all inboxes are used by companies with their own domain (for example, `@bitwarden.com`) to prevent emails from going to your personal inbox and instead route them to a shared (and sometimes unchecked) company inbox in case record of them is needed in the future.
> 
> In other cases, individuals with their own domain (for example, `@gardenllc.com`) use catch-all setups to route email from accounts with privacy-oriented usernames (for example `Instagram.com@gardenllc.com)` to their actual inbox.

#### Forwarded email alias

Select this type to integrate the username generator with your external aliasing service. Most Bitwarden apps support integration with SimpleLogin, AnonAddy, Firefox Relay, Fastmail, Forward Email, and DuckDuckGo. The mobile app currently supports integration with SimpleLogin, AnonAddy, Forward Email, and Firefox Relay.

> [!NOTE] Why use Forwarded Email Alias?
> **Why use forwarded email alias?**
> 
> Using email aliasing services such as [SimpleLogin](https://simplelogin.io/) and [Addy.io](https://addy.io/), you can sign up for web accounts using an anonymous address (for example, `nobody-knows-its-me.d0p0r@slmail.me`) that will forward mail to your actual inbox (for example, `alice@bitwarden.com`). This will prevent the website or service from collecting personal information (in this example, the name Alice and the fact that she works at Bitwarden) when you sign up.

To set up your email alias integration:

### SimpleLogin

1. Log in to your SimpleLogin account.
2. Select the profile icon and choose **API Keys**from the dropdown. SimpleLogin may require you to enter your password to create an API key.
3. In the New API Key section, enter a name that indicates the new key will be used by Bitwarden and select **Create**.

![SimpleLogin API Keys](https://bitwarden.com/assets/6ie1Qpk8LYapG6JRX3X1dD/06c1083c6e146c2822f0e4a47b507785/Screen_Shot_2022-06-30_at_3.17.59_PM.png)
4. **Copy**the API key and paste it in the **API Key**field in the Bitwarden username generator.
5. Password Manager browser extensions, mobile apps, and desktop apps can connect to a self-hosted SimpleLogin server. If you're self-hosting SimpleLogin, enter a **Server URL**.
6. Select **Regenerate Username **to generate a username and automatically create the corresponding alias in SimpleLogin.

### Addy.io

1. Log in to your Addy.io account.
2. In Addy.io, select **Settings**from the navigation menu.

![AnonAddy Settings](https://bitwarden.com/assets/18PUguJXkABllufHgtNEJi/564febbfe28d3f0cd491c3216d62db9e/addy_settings.png)
3. On the **General** tab of the settings screen, scroll down to **Update Default Alias Domain**. Select the default domain you wish to use for your alias. 

> [!NOTE] addy.io domain
> The default domain selected here must match the Domain name used in the Bitwarden Username generator.
4. Select the **API Keys** tab and click the **Create New API Key** button.
5. In the Create New API Key dialog, enter a **Name**that indicates the new token will be used by Bitwarden, an **Expiration,** and Confirm your Addy.io account password**.**Once you have completed the required fields, select**Create API Key**.

![AnonAddy Generate Token](https://bitwarden.com/assets/6o8021KYChu6jzEGvUbXDH/b56977c26a44b431486796cb4965f23d/create_new_api_key.png)
6. Copy the Personal Access Key and paste it in the **API Access Token**field in the Bitwarden username generator.

> [!NOTE] Addy.io Save Credential
> We also recommend adding this Personal Access Token to your Addy.io vault item in Bitwarden, since this is the only time the token will be displayed in Addy.io.
7. In the **Domain Name** field, enter the Addy.io domain name you selected in **Step 3**. As a free user of Addy.io, your options are `anonaddy.me`, `<username>.anonaddy.me` or `<username>.anonaddy.com`.
8. Password Manager browser extensions, mobile apps, and desktop apps can connect to a self-hosted Addy.io server. If you're self-hosting Addy.io, enter a **Server URL**.
9. Select **Regenerate Username**to generate a username and automatically create the corresponding alias in Addy.io.

### Firefox Relay

1. Log in to your Firefox Relay account.
2. Select the profile icon and choose **Settings**from the dropdown:

![Firefox Relay Settings Menu](https://bitwarden.com/assets/3jK0OhlASgzDZo1Xu2c97O/f24ae0b64e7fe7736e757b33a89510c6/Screen_Shot_2022-06-01_at_3.38.56_PM.png)
3. Copy **API Key**into the **API Access Token**field of the Bitwarden username generator.
4. Select **Regenerate Username**to generate a username and automatically create the corresponding mask in Firefox Relay.

### Fastmail

1. Log in to your Fastmail account.
2. Select the profile icon and choose **Settings**from the dropdown.
3. From the navigation menu, select**Privacy & Security**and then **Manage API tokens**: 

![Fastmail API token](https://bitwarden.com/assets/J1fPSFIIO7FgPyAyBgpbh/d4dd85f7f7201731936de872ff4a5134/2024-12-23_15-17-17.png)
4. Select **New API token** to generate an API token.

![New API token](https://bitwarden.com/assets/1FieLCzKTItKNqDIhWBrbH/2816de1ec7580e2e90cf80e38d311993/2024-12-23_15-18-50.png)

Include to following settings:

 - **Read-only access** **disabled**.
 - **Masked Email enabled.**
5. Copy **API Key**into the **API Access Token**field of the Bitwarden username generator.
6. Select **Regenerate Username**to generate a username and automatically create the corresponding alias in Fastmail.

### Forward Email

1. Log in to your [Forward Email](https://forwardemail.net/) account.
2. Forward Email uses the default domain `hideaddress.net`, however if you have a registered domain you can connect it to the service. For more information, refer to the [Forward Email setup guides](https://forwardemail.net/en/guides).
3. In Forward Email, navigate to the **My Account** → **Security** page and copy the Developer Access API token:

![Copy Forward Email API token](https://bitwarden.com/assets/0bYzljpbdqH7AdFqDh7sr/f43a225e5614a00b1dd391f17fbd916d/Screen_Shot_2023-06-30_at_1.06.04_PM.png)
4. In the Bitwarden username generator, paste the copied token in the **API access token**and enter `hideaddress.net` or your registered **Domain name**.
5. Select **Regenerate Username**to generate a username and automatically create the corresponding alias in Forward Email.

### DuckDuckGo

1. Follow the [DuckDuckGo instructions](https://duckduckgo.com/email/) to setup your Duck Address.
2. Once your Duck Address has been setup, select the **Autofill** tab on the DuckDuckGo email protection page, and open your web browser's developer tools.
3. Click the **Generate Private Duck Address**button and view the **Network** tab on your developer tools window. Select the "Addresses" call for the API POST request, and locate the API authorization item. The item will look like this: `authorization: Bearer <API token value>.`

 

![Generate DuckDuckGo email alias](https://bitwarden.com/assets/5Rj9xrPrgp13Pl9KGuap7Z/855fa2f0defc41a68b512b92027bf540/DDG_generate_private_address.png)
4. Copy the API authorization token value and paste it into the API key field on the Bitwarden generator feature.
5. Select **Regenerate Username**to generate a username and automatically create the corresponding alias in DuckDuckGo.

#### Random word

Select this type to generate a random word for your username. Options for random words include:

- **Capitalize**: Capitalize your username.
- **Include Number**: Include a 4-digit number in your username.
