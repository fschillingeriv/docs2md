---
URL: https://bitwarden.com/help/prepare-your-org-for-prod/
---

# Prepare your Trial Organization for Production

This guide will help guide your business in preparing for a production implementation of Bitwarden after a successful trial period. If you're just starting your trial period, we recommend starting with the [Proof-of-Concept Project Checklist](https://bitwarden.com/help/proof-of-concept/) before using this guide.

## Step 1: Upgrade or restart your organization

When you're ready to move a trial organization into production for your business, you can upgrade your existing organization in-place or start a new organization from scratch.

Most customers upgrade their existing organization in-place and purge their vault of test data used during their trial period before importing all shared data into production (**Step 4a**). 

| Step | Duration (hrs) | Action | Description |
|------|------|------|------|
| 1a | 0.5 | Upgrade or restart your organization | [Upgrade your organization](https://bitwarden.com/help/about-organizations/#upgrade-an-organization/) or [start a new organization](https://bitwarden.com/help/about-organizations/#create-an-organization/). |

> [!TIP] Return to POC Guide
> If you choose to start a new organization for your production implementation, revisit the [Proof-of-Concept Project Checklist](https://bitwarden.com/help/proof-of-concept/) and work through those steps before proceeding.

## Step 2: Prep for broader onboarding

While you probably have a number of members in your trial organization, most businesses add a lot more users when they move to production. With that in mind, here are a few critical steps you should take before onboarding the rest of your team:

| Step | Duration (hrs) | Action | Description |
|------|------|------|------|
| 2a | 0.5 | Check your policy configuration | To make sure your configured policies are applied to all members as soon they join, [check that all desired policies are enabled](https://bitwarden.com/help/policies/). |
| 2b | 0.25 | Activate account recovery | The account recovery policy is considered critical by many organizations for its ability to recover the accounts of users that forget their master password or are deprovisioned. [Activate this policy now](https://bitwarden.com/help/policies/). |

## Step 3: Get a production license

**This step only applies if you're self-hosting Bitwarden**. During your trial of Bitwarden, you're using a special trial license that will need to be upgraded to a production license. Once you upgrade your self-hosted server to the production license, you can activate automatic license syncing. Follow these steps:

| Step | Duration (hrs) | Action | Description |
|------|------|------|------|
| 3a | 0.25 | Retrieve your production license | Retrieve your production license from the Bitwarden cloud web app by following [these steps](https://bitwarden.com/help/licensing-on-premise/#retrieve-organization-license/). |
| 3b | 0.25 | Manually update your license file | Upload the retrieved license to your self-hosted server by following the **Manual update**procedure [here](https://bitwarden.com/help/licensing-on-premise/#update-organization-license/). |
| 3c | 0.5 | Activate billing sync | Setup your organization to automatically pull your license file in the future by following the **Automatic sync**procedure [here](https://bitwarden.com/help/licensing-on-premise/#update-organization-license/). |

## Step 4: Import your data

Before onboarding the rest of your team, ensure that all required credentials are collected in your organization, and that members will only have access to what they need once onboarded. 

Many customers purge their vault of test data used during their trial period before importing all shared data into production (**Step 4a**). Purging vault data, which can be done from the organization's **Settings**→ **Organization info**view, will prevent the creation of duplicates and help you start with a clean slate.

You may have completed most or all of these steps, but we recommend double checking that they're done to your satisfaction:

| Step | Duration (hrs) | Action | Description |
|------|------|------|------|
| 4a | 0.5 | Import your data | [Import all shared data](https://bitwarden.com/help/import-to-org/) to your production organization. |
| 4b | 0.5 | Audit collections | Ensure that your [collections](https://bitwarden.com/help/about-collections/) contain the right vault items before granting broader access. |
| 4c | 0.5 | Audit groups | Ensure that your [groups](https://bitwarden.com/help/about-groups/) are assigned to the right collections before assigning more users. |

Additionally, now is a good time to check the privileges you're granting to individual users on your administrative team. Defining good practices for member roles and permissions now will make promoting users easier once you begin onboarding more employees:

| Step | Duration (hrs) | Action | Description |
|------|------|------|------|
| 4d | 0.75 | Review member role assignments | Review the pre-defined [member roles](https://bitwarden.com/help/user-types-access-control/) available in Bitwarden and determine which role is appropriate for IT, managers, etc. |
| 4e | 1 | Set up custom admin accounts | Many organizations find it useful to create custom roles for admins in order to assign granular levels of permission to users. Check out [this guide](https://bitwarden.com/resources/setting-up-administrative-accounts-with-lesser-privileges/) for some best practices. |

## Step 5: Configure client apps

Since you'll have a large number of users starting to use Bitwarden soon, it can be useful to setup some processes for centrally configuring and deploying key Bitwarden applications:

| Step | Duration (hrs) | Action | Description |
|------|------|------|------|
| 5a | 1 | Configure clients for self-hosting | **Self-hosted only**. Bitwarden clients can be pre-configured to point to your self-hosted server. To do so, follow [these instructions](https://bitwarden.com/help/configure-clients-selfhost/). |
| 5b | 1 | Deploy browser extensions to managed devices | Bitwarden browser extensions, the app end-users will most often use in their day-to-day workflows, can be deployed in automated fashion to your users' devices. To do so, follow [these instructions](https://bitwarden.com/help/browserext-deploy/). |

## Step 6: Onboard your team

Now that your organization is ready for use in production, onboard the rest of your users. Depending on how you setup your organization during the trial period, this may be:

- [Using SCIM](https://bitwarden.com/help/about-scim/)
- [Using Directory Connector](https://bitwarden.com/help/directory-sync/)
- [Using manual invitation](https://bitwarden.com/help/managing-users/#onboard-users/)

We highly recommend reviewing, or re-reviewing, the [Onboarding and Succession](https://bitwarden.com/help/onboarding-and-succession/) guide before onboarding your remaining users.
