---
URL: https://bitwarden.com/help/bitwarden-for-msps/
---

# Managed Service Providers

Learn how to get started with Bitwarden Password Manager as Managed Service Provider (MSP) and deploy it to your customer in this video guide. 

[![Vimeo Video](https://vumbnail.com/668382756.jpg)](https://vimeo.com/668382756)
*[Watch on Vimeo](https://vimeo.com/668382756)*

Learn more about becoming a Bitwarden MSP or reseller [here](https://bitwarden.com/partners/), or jump to the following points in the video to learn more about specific topics:

- **1:36**: Overview of Bitwarden Password Manager.

 - **1:46**: Bitwarden client apps.
 - **2:15**: How Bitwarden integrates with your tech stack.
 - **4:53**: Overview of terminology and concepts.
- **8:34**: MSP architecture deep dive.

 - **10:05**: Your organization.
 - **16:19**: The Provider Portal.
 - **23:13**: Client organizations.
- **25:49**: Manage your clients.

 - **26:50**: Manage policies.
 - **27:43**: Import data.
 - **28:18**: Set up SSO and SCIM.
- **29:00**: Q&A.

# MSP customer deployment guide 

Use the following steps and best practices to deploy Bitwarden to your customers.

## Phase 1 - Pre-onboarding

Define technical requirements and onboarding strategy for your customer's Bitwarden organization and environment.

| Step | Topic | Action | Resources | Duration (hours) |
|------|------|------|------|------|
| 1 | Environment decision | Determine Cloud or Self-Hosted environment | [Hosting FAQs](https://bitwarden.com/help/hosting-faqs/) | 0.5 |
| 2 | Authentication strategy | Determine if the customer will use Single Sign-On (SSO) | [About SSO](https://bitwarden.com/help/about-sso/) | 0.25 |
| 3 | Decryption method | If using Login with SSO, select Master Password or trusted devices for decryption | [About trusted devices](https://bitwarden.com/help/about-trusted-devices/) | 0.25 |
| 4 | Provisioning strategy | Select provisioning strategy like SCIM, directory connector, or manual provisioning. | [Managing users](https://bitwarden.com/help/managing-users/#onboard-users/) | 0.25 |
| 5 | User identification | Identify users, teams, or departments for rollout groups | | 0.25 |
| 6 | Training strategy | Identify groups and internal advocates who will attend training. Example: end users, service desk, admins | | 0.5 |
| 7 | Document collection (sharing) strategy | Determine how collections will be configured. Considerations include: Will users be allowed to create collections? Will collections be configured by department, project, function? Will data be imported from another application, which often defines structure? Do Admin and Owner users get access to all shared items, or only the Managers of delegated Collections? | [About collections](https://bitwarden.com/help/about-collections/) | 1 |
| 8 | Policy planning | Select policies to be configured at launch | [Policies](https://bitwarden.com/help/policies/) | 0.5 |
| 9 | Rollout timeline | Determine invitation and onboarding mechanisms and timing | | 0.5 |
| 10 | Internal communication | Create internal messaging or memo about Bitwarden rollout. Review Bitwarden templates to get a sense of the communications | [Welcome email templates](https://bitwarden.com/help/welcome-email-templates/) | 1 |
| 11 | Leadership communication | Communicate to internal leaders about Password Management Rollout Strategy | | 0.25 |

## Phase 2 - Organization set up

Set up the technical foundation and configure Bitwarden settings for your customer. 

| Step | Topic | Action | Resources | Duration (hours) |
|------|------|------|------|------|
| 12 | Organization owner | Identify the organization owner. The owner is the super-user that can control all aspects of your organization. Decide if you want the email to be associated with a specific user or a team inbox. Additionally, the best practice is two owner accounts for redundancy | [Member roles](https://bitwarden.com/help/user-types-access-control/#member-roles/) | 0.25 |
| 13 | Enterprise policies | Configure Enterprise policies. Any policies should be enabled prior to user invitation. Be sure to check out the following policies: Account recovery administration Enforce organization data ownership Activate autofill | [Policies](https://bitwarden.com/help/policies/) | 1 |
| 14 | Collection management settings | Choose how collections will behave in the organization. These settings allow for a spectrum of full admin control to completely self-serve where users can create their own collections. These settings can be used to establish a policy of least privilege | [Managing users](https://bitwarden.com/help/managing-users/) | 0.25 |
| 15 | Co-managed environment | Add administrators or owners to the client organization to co-manage. Best practice is to configure a second owner for redundancy | [Managing users](https://bitwarden.com/help/managing-users/) | 0.5 |
| 16 | Create collections | Collections are where secure items are located and shared with groups of users | [Collections](https://bitwarden.com/help/collections/) | 0.5 |
| 17 | Create user groups | Creating user groups allows easy assignment of collections. If you decide to sync groups and users from your Identity Provider or Directory Service, you may need to reconfigure user and group assignments later | [Groups](https://bitwarden.com/help/groups/) | 0.5 |
| 18 | Collection assignment | Assign groups to collections, making sure to test and demonstrate 'Read Only' and 'Hide Password' options | [User types access control](https://bitwarden.com/help/user-types-access-control/) | 0.5 |
| 19 | Add items | Add items manually to test collections or import via CSV or JSON from another password management application | [Collections](https://bitwarden.com/help/collections/) | 0.25 |
| 20 | Login with SSO | If applicable, configure Login with SSO and organization identifier Configure to work with SAML 2.0 or OpenID Connect | [Get started with SSO](https://bitwarden.com/help/getting-started-with-sso/) | 1.5 |
| 21 | Domain verification | if applicable, verify company and/or other email domains to allow your users to skip entering the Organization identifier during the Enterprise SSO process. Not necessary for non-SSO organizations | [Domain verification](https://bitwarden.com/help/domain-verification/) | 0.5 |

## Phase 3 - Organization roll out

Deploy Bitwarden across your customer's teams and functions. 

| Step | Topic | Action | Resources | Duration (hours) |
|------|------|------|------|------|
| 22 | Technical cadence meeting | Plan implementation phase 3 with client | | 0.5 |
| 23 | Add items to collections | Add items manually to production collections or import data from another password management application | [About collections](https://bitwarden.com/help/about-collections/) | 0.25 |
| 24 | Enterprise policies | Enterprise Policies can be used to tailor your Bitwarden Organization to fit your security needs. Enable and configure desired policies before user onboarding begins | [Policies](https://bitwarden.com/help/policies/) | 0.1 |
| 25 | Login with SSO | If applicable, configure Bitwarden to authenticate using your SAML 2.0 or OIDC Identity Provider | [About SSO](https://bitwarden.com/help/about-sso/) | 1.5 |
| 26 | Early users | Add a set of users to the client organization manually and assign them to different groups. With these users, you'll broadly test all pre-configured functionality in the next step, before moving on to advanced functions like Directory Connector. Share the attached onboarding workflow instructions with the users | [Managing users - Invite](https://bitwarden.com/help/managing-users/#invite/) [Onboarding Workflows](https://bitwarden.com/help/onboarding-workflows/) | 0.5 |
| 27 | SIEM integration | If applicable, connect Bitwarden to customer's SIEM tool | [SIEM](https://bitwarden.com/help/event-logs/#siem-and-external-systems-integrations/) | 0.5 |
| 28 | Bitwarden clients | All Organization members added for the pilot group should download Bitwarden on an assortment of devices, login, and test access to shared items via collections. They should test the proper implementation of policies. | [Download](https://bitwarden.com/download/) | 0.5 |
| 29 | Deploy client applications | Configure your application management or MDM tooling to prepare for mass deployment of Bitwarden applications | [Deploy client applications](https://bitwarden.com/help/browserext-deploy/) | 0.5 |
| 30 | Disable built-in password manager | Make Bitwarden Password Manager the default password manager and turn off built-in browser solutions. Educate users how to do the same when onboarded | [Disable built-in password manager](https://bitwarden.com/help/getting-started-browserext/#disable-a-built-in-password-manager/) | 0.25 |
| 31 | Test user onboarding | Configure and test Bitwarden SCIM or Directory Connector integrations to automatically sync users and groups | [About SCIM](https://bitwarden.com/help/about-scim/) [About Directory Connector](https://bitwarden.com/help/directory-sync/) | 1.5 |
| 32 | User onboarding | Execute on SCIM or Directory Connector syncing to invite additional users in groups to the organization. Share the attached onboarding workflow instructions with the users | [About SCIM](https://bitwarden.com/help/about-scim/) [About Directory Connector](https://bitwarden.com/help/directory-sync/) [Onboarding Workflows](https://bitwarden.com/help/onboarding-workflows/) | 1 |

## Phase 4 - User training 

Train all users and stakeholders on how to use Bitwarden and provide continuing education. 

| Step | Topic | Action | Resources | Duration (hours) |
|------|------|------|------|------|
| 33 | Admin training | Provide essential day-to-day task training for administrative users with the addition of any special topics requested Example special topics include, but are not limited to: Demonstrating the configured SSO login flow User onboarding and offboarding Custom roles | [Get to know the Admin Console](https://bitwarden.com/help/get-started-administrator/#get-to-know-the-admin-console/) [Bitwarden for business admins](https://bitwarden.com/help/courses/bitwarden-for-business-admins/) | 0.75 |
| 34 | Service desk training | Advise service desk users on their role/operations. Review what tasks can be done with the custom role and what require admin intervention | | 0.75 |
| 35 | Team member training | A general training session for end users will cover: Bitwarden for all devices Setting up the Bitwarden Browser Extension Creating your account Getting to know the Bitwarden vault How to use the Bitwarden Password Manager Bitwarden Send | [Get to know your vault ](https://bitwarden.com/help/get-started-team-member/#get-to-know-your-vault/) [Get to know Password Manager](https://bitwarden.com/help/get-to-know-password-manager/) | 0.75 |
| 36 | Ongoing education | All users can take advantage of monthly new and updated learning content in the Bitwarden Learning Center | [Learning](https://bitwarden.com/learning/) | 0.75 |
