---
URL: https://bitwarden.com/help/system-administrator-portal/
---

# System Administrator Portal

The Bitwarden System Administrator Portal can be used to:

- Check [currently installed and latest available versions](https://bitwarden.com/help/versioning/#self-hosted-server-version/).
- View [environment configuration settings](https://bitwarden.com/help/environment-variables/).
- View and [delete registered users](https://bitwarden.com/help/delete-member-accounts/).
- View and delete registered organizations.

> [!NOTE] SysAdmin doesn't provide access to unencrypted data
> The System Administrator Portal **does not** provide access to the protected data (for example, vault items) of the server's users or organizations.

## Configure user access

Users will log in to the System Administrator Portal using a secure magic link sent to their email inbox. To configure who has access, add authorized email addresses:

> [!TIP] Requirements for access to SysAdmin Portal
> Because the System Administrator Portal uses email to facilitate access to authorized users, you are required to setup an SMTP mail server prior to any user attempting to log in to the portal.
> 
> Also note that emails authorized to use the System Administrator Portal are not required to have Bitwarden accounts on your server that use the same email addresses.

### Docker

Add authorized email addresses in a comma-separated list to the `adminSettings__admins=` variable in your `global.override.env` file:

```
adminSettings__admins=john@example.com,bill@example.com,tom@example.com
```

**Whenever you make changes to** `global.override.env`**, perform a** `./bitwarden.sh restart` **to apply your configuration changes.**

### Helm

Add authorized email addresses in a comma-separated list to the `general.admins:` value in your `my-values.yaml` file:

```yaml
...
# Comma-separated list of email addresses for Admin users
 admins: john@example.com,bill@example.com,tom@example.com
...
```

**Whenever you make changes to** `my-values.yaml`**, use the**`helm upgrade` **command to apply your configuration changes.**

## Access the portal

The System Administrator Portal for your server is available at `https://<your.domain.com>/admin`. When a user attempts to log in, a secure link is sent to their email address **only** if that email address is authorized using the process documented above.

Clicking this temporary link, which is active for 15 minutes following the login attempt, will log that user into the System Administrator Portal.
