---
URL: https://bitwarden.com/help/self-host-an-organization/
---

# Self-host an Organization

## Step 1: Install and deploy your server

Before you can self-host an organization, you'll need to install and deploy Bitwarden to your server. Bitwarden can be run, using Docker, on Linux and Windows machines. While there are a variety of methods for installing Bitwarden, including methods for offline or air-gapped environments, we recommend starting with one of these guides:

- [Install and Deploy - Linux](https://bitwarden.com/help/install-on-premise-linux/)
- [Install and Deploy - Windows](https://bitwarden.com/help/install-on-premise-windows/)

## Step 2: Configure organization environment variables

Some features used by Bitwarden organizations are not configured by the standard installation procedure documented in the above articles. To equip your self-hosted server with all the features available to Bitwarden organizations, set the following variables in your `./bwdata/env/global.override.env` file:

| Variable | Description | Use |
|------|------|------|
| globalSettings__mail__smtp__host= | Your SMTP server hostname (recommended) or IP address. | Used for [inviting users](https://bitwarden.com/help/managing-users/#invite/) to your organization. |
| globalSettings__mail__smtp__port= | The SMTP port used by the SMTP server. | Used for [inviting users](https://bitwarden.com/help/managing-users/#invite/) to your organization. |
| globalSettings__mail__smtp__ssl= | (Boolean) Whether your SMTP server uses an encryption protocol: `true` = SSL `false` = TLS | Used for [inviting users](https://bitwarden.com/help/managing-users/#invite/) to your organization. |
| globalSettings__mail__smtp__username= | A valid username for the `smtp__host`. | Used for [inviting users](https://bitwarden.com/help/managing-users/#invite/) to your organization. |
| globalSettings__mail__smtp__passsword= | A valid password for the `smtp__username`. | Used for [inviting users](https://bitwarden.com/help/managing-users/#invite/) to your organization. |
| globalSettings__enableCloudCommunication= | Set to `true` to allow communication between your server and our cloud system. | Used for [billing and license sync](https://bitwarden.com/help/self-host-an-organization/#step-4-setup-billing-and-license-sync/). |
| globalSettings__duo__aKey= | A randomly generated Duo akey. For more information, see [Duo's Documentation](https://duo.com/docs/duoweb-v2#1.-generate-an-akey). | Used for [organization-wide two-step login via Duo](https://bitwarden.com/help/setup-two-step-login-duo/). |
| globalSettings__hibpApiKey= | Your HaveIBeenPwned (HIBP) API Key, available [here](https://haveibeenpwned.com/API/Key). | Allows users to run the [Data Breach report](https://bitwarden.com/help/reports/#data-breach-individual-vaults-only/) and to check their master password for presence in breaches when they create an account. |
| globalSettings__disableUserRegistration= | Specify `true` to disable new users signing up for an account on this instance via the registration page. | Used to limit users on the server to those invited to the organization. |
| globalSettings__sso__enforceSsoPolicyForAllUsers= | Specify `true` to enforce the [Require SSO authentication](https://bitwarden.com/help/policies/#require-single-sign-on-authentication/) policy for owner and admin roles. | Used to enforce the [Require SSO authentication](https://bitwarden.com/help/policies/#require-single-sign-on-authentication/) policy for owner and admin roles. |

Once you've made changes to your environment variables, perform a `./bitwarden.sh restart` to apply the changes to your server.

## Step 3: Start your organization

### Start a cloud organization

At this stage, you're ready to start your organization and port it over to your self-hosted server. For billing purposes, organizations must first be created in the Bitwarden cloud web vault ([https://vault.bitwarden.com](https://vault.bitwarden.com)). Follow [these instructions](https://bitwarden.com/help/about-organizations/#create-an-organization/) to create an organization.

### Start a self-hosted organization

Once your cloud organization is created, follow [these instructions](https://bitwarden.com/help/licensing-on-premise/#organization-license/) to retrieve your license from the cloud and upload it to your self-hosted server to create a self-hosted copy of the organization.

Self-hosted Bitwarden organizations will be able to utilize all paid features provided by their chosen plan. Only Families and Enterprise organizations can be imported to self-hosted servers. Learn more [here](https://bitwarden.com/help/about-bitwarden-plans/).

## Step 4: Setup billing and license sync

Next, setup your self-hosted organization for billing and license sync from your cloud organization. Doing so is optional, but will have a few advantages:

- Enabling easier license updating when you change your organization's seat count.
- Enabling easier license updating when your subscription comes to its renewal date.
- Unlocking [sponsored Families organizations](https://bitwarden.com/help/families-for-enterprise/) for members of Enterprise organizations.

Follow [these instructions](https://bitwarden.com/help/licensing-on-premise/#update-a-renewed-organization-license/) to setup billing and license sync for your organization.

> [!NOTE] B&L Sync requires cloudComms
> Billing and license syncing requires that the `globalSettings__enableCloudCommunication=` environment variable is set to `true` ([learn more](https://bitwarden.com/help/environment-variables/)).

## Step 5: Start organization administration

You're now ready to start administering your self-hosted organization! Here's how you might approach it:

### Password Manager

### Invite your admin team

Every all-star organization needs an all-star admin team. Start inviting high-privileged members who can help you build a foundation for secure credential sharing with Bitwarden. If you’re building an Enterprise organization, you can give members [highly-flexible custom permissions to fit your needs](https://bitwarden.com/help/user-types-access-control/#custom-role/).

For protective redundancy, we recommend including at least one other **organization owner**in [your newly-formed admin team](https://bitwarden.com/help/managing-users/#onboard-users/).

### Set policies (Enterprise-only)

Your business has unique security needs. Use policies to build a consistent deployment and experience for all team members, like requiring SSO authentication or enrolling members in admin password reset. To get your organization ready for more team members, it's important to [set your policies early](https://bitwarden.com/help/policies/).

### Import your data

Is your business coming to Bitwarden from another password manager? Good news! You can import that data directly to your organization to [avoid a painful day of copy-and-pasting](https://bitwarden.com/help/import-to-org/). 

### Build groups & collections

Once you've got items in your vault, it's a good time to set up collections and groups to ensure that the *right *users have access to the *right *credentials. Every organization is different, but here are some tips to help you [get started with collections](https://bitwarden.com/help/about-collections/#using-collections/) and [get started with groups](https://bitwarden.com/help/about-groups/#using-groups/).

### Invite your team

It's finally time to start inviting users! If you use an identity provider or directory service like Azure Active Directory, use [SCIM](https://bitwarden.com/help/about-scim/) or [Directory Connector](https://bitwarden.com/help/directory-sync/) to automatically sync users. Otherwise, follow the same steps you took to build your admin team to invite more users to the organization.

### Secrets Manager

### Invite your admin team

Every all-star organization needs an all-star admin team. Start inviting high-privileged members who can help you build a foundation for secure secret sharing with Bitwarden.

For protective redundancy, we recommend including at least one other **organization owner**in [your newly-formed admin team](https://bitwarden.com/help/manage-your-secrets-org/#member-roles/).

### Set policies

Your business has unique security needs. Use policies to build a consistent deployment and experience for all team members, like requiring SSO authentication or enrolling members in admin password reset. To get your organization ready for more team members, it's important to [set your policies early](https://bitwarden.com/help/policies/).

### Import your data

Is your business coming to Bitwarden from another secret manager? Good news! You can import that data directly to your organization to [avoid a painful day of copy-and-pasting](https://bitwarden.com/help/import-secrets-data/). 

### Invite your team

It's finally time to start inviting users! If you use an identity provider or directory service like Azure Active Directory, use [SCIM](https://bitwarden.com/help/about-scim/) or [Directory Connector](https://bitwarden.com/help/directory-sync/) to automatically sync users. Otherwise, follow the same steps you took to build your admin team to invite more users to the organization. Once everyone is onboarded, [start giving users access to Secrets Manager](https://bitwarden.com/help/secrets-manager-quick-start/#give-members-access/).
