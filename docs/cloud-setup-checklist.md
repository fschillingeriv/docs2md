---
URL: https://bitwarden.com/help/cloud-setup-checklist/
---

# Cloud setup checklist

With cloud hosting, Bitwarden manages the infrastructure, security, and operational responsibilities. Use this checklist to understand the organizational and user management requirements for cloud deployments.

## Pre-deployment planning

- Determine cloud server region (US, EU)
- Choose authentication strategy (Email or SSO via identity provider)
- Select encryption type (Master Password or Trusted Device)
- Define user provisioning approach (Manual, Directory Connector, SCIM, Just-in-Time SSO)
- Define vault ownership strategy (Individual vaults vs. Organization-only)
- Identify user groups for rollout phases

**Support links:**

- [Server geographies](https://bitwarden.com/help/server-geographies/)
- [Bitwarden authentication guide](https://bitwarden.com/resources/reference-guide-bitwarden-authentication/)
- [Bitwarden implementation guide ](https://bitwarden.com/resources/bitwarden-enterprise-password-manager-implementation-guide/)

## Stakeholder selections

Select key roles:

- Project lead
- Identity provider admin
- Executive sponsor
- Security and compliance admin
- Support/help desk admin
- Device management admin (for client deployment)
- Business continuity admin
- Directory/user management admin

## Security and compliance decisions

- Determine cloud server region (US, EU)
- Choose authentication strategy (Email or SSO via identity provider)
- Select encryption type (Master Password or Trusted Device)
- Define user provisioning approach (Manual, Directory Connector, SCIM, Just-in-Time SSO)
- Define vault ownership strategy (Individual vaults vs. Organization-only)
- Identify user groups for rollout phases

**Support links:**

- [SSO integration ](https://bitwarden.com/help/about-sso/)
- [SCIM](https://bitwarden.com/help/about-scim/)
- [Directory Connector](https://bitwarden.com/help/directory-sync-cli/)

## Organizational build-out and configuration

- Identify Organization Owner(s) (recommend two for redundancy)
- Add additional administrators to the organization
- Configure enterprise policies (before user invitation)
- Select collection management settings
- Create collections for administrators and users to share
- Create groups for managing users
- Assign collections to groups
- Test 'Read Only' and 'Hide Password' options
- Add test items to collections

**Support links:**

- [Bitwarden implementation guide](https://bitwarden.com/resources/bitwarden-enterprise-password-manager-implementation-guide/)
- [Least privilege access](https://bitwarden.com/blog/additional-enterprise-options-for-least-privileged-access-control/#flexible-collections-options-for-your-organization/)

## User provisioning and directory integration

- Enable SCIM provisioning in admin console
- Configure identity provider
- Map user attributes and group memberships
- Test SCIM synchronization
- Download and install directory connector
- Configure sync filters, user/group mappings

**Support links:**

- [Enable SCIM provisioning](https://bitwarden.com/help/about-scim/)
- [Microsoft Entra ID SCIM Integration](https://bitwarden.com/help/microsoft-entra-id-scim-integration/)
- [JumpCloud SCIM Integration](https://bitwarden.com/help/jumpcloud-scim-integration/)
- [OneLogin SCIM Integration](https://bitwarden.com/help/onelogin-scim-integration/)
- [Ping Identity SCIM Integration](https://bitwarden.com/help/ping-identity-scim-integration/)

## Deployment and go-live preparation 

- Complete final security review and sign off from stakeholders
- Set up production monitoring and alerting systems
- Coordinate with network and security teams for go-live

## Monitoring

- Monitor system performance and adoption metrics
- Conduct post-implementation review with stakeholders
- Plan ongoing maintenance and update procedures
- Document lessons learned and process improvements
- Schedule regular security audits and policy reviews

**Support links:**

- [Vault health reports](https://bitwarden.com/help/reports/)

## Change management and training

- Develop communication plan for organization
- Create timeline for rollout announcements and milestones
- Prepare exec updates on security benefits and ROI
- Schedule admin and end-user training
- Plan ongoing communication and feedback channels
- Set up support processes and escalation procedures
