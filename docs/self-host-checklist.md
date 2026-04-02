---
URL: https://bitwarden.com/help/self-host-checklist/
---

# Self-host Checklist

Use this checklist to ensure that the key stakeholders in your deployment of Bitwarden in a self-hosted environment are aware of the critical stages and timelines. Reduce the risk of delays and miscommunication by aligning on these topics.

## Stakeholders

| Role | Assigned team or member |
|------|------|
| Self-host project lead | |
| Executive sponsor | |
| Server (Windows or Linux) admin Docker or Kubernetes admin Network admin Firewall admin Database admin (optional) | |
| Identity Provider & Single Sign-On admin | |
| SMTP admin | |
| Security & Compliance lead Backups admin | |
| Business continuity Disaster recovery | |
| Device management admin Support or Help Desk admin | |

## Deployment stages

### Server preparation

Address the following key decisions *before* deploying your Bitwarden server:

| Key decision | Description | Assigned team or member | Support links |
|------|------|------|------|
| Deployment method | Will you deploy in the Bitwarden US or EU cloud? Or self-host with Docker on Linux or Windows, or Kubernetes? | | [Self-host Bitwarden](https://bitwarden.com/help/self-host-bitwarden/) |
| Server configuration | What environment variables will you leverage on your server to meet organizational security requirements? Will you place your server behind a firewall or proxy? | | [Configure Environment Variables](https://bitwarden.com/help/environment-variables/) |
| Database selection | Will your server use the packaged MSSQL database or will connect to a separate MSSQL database? If Lite, will you use a different database platform? | | [Database Options](https://bitwarden.com/help/database-options/) |
| Certificate selection | Which certificate option will you use to secure data in-transit? | | [Certificate Options](https://bitwarden.com/help/certificates/) |

### Rollout preparation

Address the following key decisions *before* onboarding users to your server:

| Key decision | Description | Assigned team or member | Support links |
|------|------|------|------|
| Administration team | Who are the administrators who will manage and maintain your server? | | [Administer a Server](https://bitwarden.com/help/system-administrator-portal/) |
| Maintenance plan | What is your strategy for executing updates, and performing security audits to keep Bitwarden secure and up-to-date? | | [Update a Server](https://bitwarden.com/help/updating-on-premise/) |
| Backup plan | What are your processes for taking and automating regular backups of the server, virtual machine, and other services? Will you take user-level backups, hypervisor backups, and database snapshots? | | [Backup Server Data](https://bitwarden.com/help/backup-on-premise/) |
| Disaster recovery plan | What is your strategy for disaster recovery and how will you enumerate and test DR scenarios? | | [Business Continuity and Disaster Recovery](https://bitwarden.com/help/bitwarden-security-white-paper/#business-continuity-and-disaster-recovery/) |
| Testing | How will you test server-client connections, server performance, and maintenance, backup, and DR plans? | | |
| Compliance & integration plan | How will you ensure your setup meets regulatory compliance requirements and integrates with your existing IT infrastructure? | | |
