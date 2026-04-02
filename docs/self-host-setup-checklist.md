---
URL: https://bitwarden.com/help/self-host-setup-checklist/
---

# Self host setup checklist

With self-hosting, your team is responsible for infrastructure, security, and operational responsibilities. Use this checklist to understand the additional overhead involved with self-host deployments.

## Pre-deployment planning

- Choose self hosted deployment method (Linux standard/manual/offline, Windows standard/offline, or Kubernetes)
- Define server/VM specs and hosting environment (environment variables, firewall or proxy)
- Select database option (packaged MSSQL, separate MSSQL, Unified)
- Decide on SSL certificate approach
- Plan network architecture, firewall or proxy rules, access controls
- Scalability planning
- Certificate selection for secure data in-transit

**Support links:**

- [Self-hosted deployment method](https://bitwarden.com/help/self-host-bitwarden/)

## Stakeholder selections

Select key roles:

- Project lead
- Executive sponsor
- Server admin
- Docker admin
- Network admin
- Firewall admin
- Support/help desk admin
- Database admin
- Identity provider admin
- SMTP admin
- Security and compliance admin
- Backups admin
- Business continuity admin
- Disaster recovery admin
- Device management admin

## Security and compliance decisions

- Choose between SSO integration or Bitwarden authentication
- Select provisioning method (SCIM, Directory Connector)
- Define backup strategy (frequency, retention)
- Identify regulatory compliance needs (HIPAA, SOC2)
- Plan user roles, permissions, and organizational structure

**Support links:**

- [SSO integration ](https://bitwarden.com/help/about-sso/)
- [SCIM](https://bitwarden.com/help/about-scim/)
- [Directory Connector](https://bitwarden.com/help/directory-sync-cli/)

## Server provisioning, configuration, database setup

- Provision servers/VMs meeting min specs
- Configure Windows-specific requirements
- Install Docker, Docker compose
- Configure database system
- Test database connectivity strings and authentication
- Implement database security best practices
- Obtain installation ID and key from Bitwarden hosting portal
- Create dedicated Bitwarden system user and directory structure
- Configure SSL certificates and HTTPS encryption

**Support links:**

- [Configure environment variables ](https://bitwarden.com/help/environment-variables/)
- [Database options](https://bitwarden.com/help/database-options/)
- [Certificate options](https://bitwarden.com/help/certificates/)

## Backup and disaster recovery implementation 

- Implement backup schedules for server and database
- Configure off-site backup and retention policies
- Test backup integrity and restoration procedures
- Document backup and recovery processes
- Set up monitoring and alerting for backup failures
- Evaluate backup methods
- Create disaster recovery runbooks

**Support links:**

- [Backup options](https://bitwarden.com/help/backup-on-premise/)
- [Disaster recovery options](https://bitwarden.com/help/bitwarden-security-white-paper/#business-continuity-and-disaster-recovery/)

## User provisioning and directory integration

- Enable SCIM provisioning in admin console
- Obtain SCIM URL and API key from Bitwarden
- Configure identity provider
- Map user attributes and group memberships
- Test SCIM synchronization
- Download and install directory connector
- Configure server URL and authentication
- Set up directory source connection
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
