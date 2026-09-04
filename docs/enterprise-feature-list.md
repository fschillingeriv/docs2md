---
URL: https://bitwarden.com/help/enterprise-feature-list/
---

# Bitwarden for Enterprise Features Datasheet

This document describes and references the features available to [Bitwarden Enterprise Organizations](https://bitwarden.com/products/business/) in several categories:

#### Application Range and Ease-of-use

| Enterprise Features | Description |
|------|------|
| Deployment options | Use the included Bitwarden cloud service or install to a private cloud or on-prem self-hosted solution. Bitwarden may also be installed completely offline in an air-gapped environment. |
| Web application | Fully encrypted cloud web app at [https://vault.bitwarden.com](https://vault.bitwarden.com/), or on your self-hosted server. |
| Mobile apps | Available for iOS and Android. [Learn more](https://bitwarden.com/help/getting-started-mobile/). |
| Browser extensions | Available for Chrome, Firefox, Opera, Edge, Vivaldi, Brave, Tor, and Safari. [Learn more](https://bitwarden.com/help/getting-started-browserext/). |
| Desktop applications | Available for Windows, Mac, and Linux. [Learn more](https://bitwarden.com/help/getting-started-desktop/). |
| Command-line interface (CLI) | Available for Windows, Mac, and Linux. [Learn More](https://bitwarden.com/help/cli/). |

#### Administrative Features and Capabilities

| Enterprise Features | Description |
|------|------|
| Simple user management | Add or remove seats and onboard or offboard users directly from the web app. [Learn more](https://bitwarden.com/help/managing-users/). |
| Role based access control | Assign role-based access for Organization users, including a custom role and granular permissions (e.g. Hide Passwords, Read-Only). [Learn more](https://bitwarden.com/help/user-types-access-control/). |
| Directory sync | Synchronize your Bitwarden organization with your existing user directory. Provision and deprovision users, groups, and group associations. [Learn more](https://bitwarden.com/help/directory-sync/). |
| SCIM support | Use the SCIM protocol to manage and provision Bitwarden users, groups, and group associations from your Identity Provider or directory service for easy onboarding and employee succession. [Learn more](https://bitwarden.com/help/about-scim/). |
| Account recovery | Designated administrators can reset and assign a master password of end-user accounts if an employee loses access. [Learn more](https://bitwarden.com/help/admin-reset/). |
| Collections with curated access and role-based access control (RBAC) | Create an unlimited amount of password collections containing an unlimited amount of passwords. Collections can be assigned to groups or individual users. [Learn more](https://bitwarden.com/help/about-collections/). |
| Enterprise policies | Enforce security rules for all users, for example mandating use of Two-step Login. [Learn more](https://bitwarden.com/help/policies/). |
| Claimed domains and accounts | Admins can claim ownership of email domains, giving the organization control over Bitwarden accounts registered with company email addresses, even before those users are formally onboarded. [Learn more.](https://bitwarden.com/help/claimed-domains/) |
| Temporary password sharing and generation | Create and share ephemeral data using Bitwarden Send. [Learn more](https://bitwarden.com/help/about-send/). |
| Managed client deployment support | Deploy browser extensions, desktop apps, and mobile apps at scale using MDM tools like Microsoft Intune, GPO, and Linux/macOS policy files. [Learn more.](https://bitwarden.com/help/browserext-deploy/) |
| Complimentary Families plan for users | All enterprise users receive a complimentary family plan for personal use to practice good security habits outside of the workplace. [Learn more](https://bitwarden.com/help/families-for-enterprise/). |

#### Reporting

| Enterprise Features | Description |
|------|------|
| Access Intelligence | Gain actionable visibility into risky or unusual access patterns within your organization's vault, helping security teams proactively identify and address credential health issues. [Learn more.](https://bitwarden.com/help/access-intelligence/) |
| Vault health reports | Run reports for Exposed Passwords, Reused Passwords, Weak Passwords, and more. [Learn more](https://bitwarden.com/help/reports/). |
| Data breach reports | Run reports for data compromised in known breaches (e.g. email addresses, passwords). [Learn more](https://bitwarden.com/help/reports/). |
| Auditable event logs and SIEM integration | Time stamped records of events that occur within your organization vault for easy use in the web app or ingestion by SIEM tools. Built-in integrations include Splunk, Microsoft Sentinel, Elastic, Rapid7, Panther, and Sumo Logic. Others can be supported via API calls. [Learn more](https://bitwarden.com/help/event-logs/). |

#### Authentication

| Enterprise Features | Description |
|------|------|
| 2FA for individuals | A robust set of 2FA options for any Bitwarden user. [Learn more](https://bitwarden.com/help/setup-two-step-login/). |
| 2FA at organization-level | Enable 2FA via Duo for your entire organization. [Learn more](https://bitwarden.com/help/setup-two-step-login-duo/). |
| Biometric authentication | Available for browser extension, desktop and mobile applications. [Learn more](https://bitwarden.com/help/biometrics/). |
| Log in with device | Users can approve login from a trusted device instead of entering a master password, reducing friction while maintaining security. [Learn more.](https://bitwarden.com/help/log-in-with-device/) |
| Log in with passkey | Users can log in utilizing a FIDO-compliant passkey supporting the WebAuthn PRF extension in both the web app and browser extensions (for compatible browsers). Logging in with a passkey bypasses the need for two-step login, master password, and login email address, making this method ideal for a break-glass administrator account. [Learn more.](https://bitwarden.com/help/login-with-passkeys/) |
| New device login verification | Protects against unauthorized access by requiring verification when a login attempt is made from an unrecognized device. and an account does not have two-step login set up nor is subject to SSO policies. [Learn more.](https://bitwarden.com/help/new-device-verification/) |
| SSO with trusted devices | SSO with trusted devices allows users to authenticate using SSO and decrypt their vault using a device-stored encryption key, eliminating the need to enter a master password. [Learn more.](https://bitwarden.com/help/about-trusted-devices/) |
| Login with SSO | Leverage your existing Identity Provider (IdP) to authenticate your Bitwarden organization users via SAML 2.0 or OpenID Connect (OIDC). [Learn more](https://bitwarden.com/help/about-sso/). Using Login with SSO, you can use one of two decryption options to determine how users decrypt Vault data once authenticated. [Learn more](https://bitwarden.com/help/sso-decryption-options/). |
| SSO with customer managed encryption (self-host only) | Employees use their SSO credentials to authenticate and decrypt all in a single step. This option shifts retention of the users master passwords to companies requiring the business to deploy a key connector to store the user keys. [Learn more. ](https://bitwarden.com/help/about-key-connector/) |

#### Security

| Enterprise Features | Description |
|------|------|
| Secure storage for logins, passkeys, notes, cards, identities, and SSH keys. | Bitwarden [vault items](https://bitwarden.com/help/managing-items/) are encrypted before being stored anywhere. [Learn more](https://bitwarden.com/help/what-encryption-is-used/). |
| Zero knowledge encryption | All vault data is end-to-end encrypted. [Learn more](https://bitwarden.com/blog/vault-security-bitwarden-password-manager/). |
| Secure username and password generator | Generate secure, random, and unique credentials for every vault item. [Learn more](https://bitwarden.com/help/generator/). |
| Encrypted export | Download encrypted exports for secure storage of Vault data backups. [Learn more](https://bitwarden.com/help/encrypted-export/). |
| Biometric authentication | Available for browser extension, desktop and mobile applications. [Learn more](https://bitwarden.com/help/biometrics/). |
| Emergency access | Users can designate and manage trusted emergency contacts, who may request access to their vault in case of emergency. [Learn more](https://bitwarden.com/help/emergency-access/). |
| Account fingerprint phrase | Security measure that uniquely and securely identifies a Bitwarden user account when encryption-related or onboarding operations are performed. [Learn more](https://bitwarden.com/help/fingerprint-phrase/). |
| Enterprise policies for vault timeout and locking | Enforce organization-wide timeout and lock settings to reduce exposure risk on inactive sessions. [Learn more.](https://bitwarden.com/help/policies/#session-timeout/) |
| Subprocessors | See the full list of subprocessors: [Bitwarden Subprocessors](https://bitwarden.com/help/subprocessors/). |

#### Compliance, Audits, Certifications

| Enterprise Features | Description |
|------|------|
| SOC 2 Type II and SOC 3 | [Read about Bitwarden SOC Certifications](https://bitwarden.com/blog/bitwarden-achieves-soc-2-certification/). |
| ISO 27001 | Bitwarden is ISO 27001 certified and in compliance with ISO 27001 control sets surrounding data security. |
| Security and compliance assessments | Bitwarden invests in annual third party audits, security assessments, and other compliance standards. All reports are available on the [Bitwarden compliance page](https://bitwarden.com/compliance/). |
| GDPR, CCPA, & HIPAA | [Read about Bitwarden compliance with various privacy frameworks](https://bitwarden.com/compliance/). |
| White-box testing | Performed by unit tests and QA engineers. |
| Black-box testing | Performed via automation and manual testing. |
| Bug Bounty Program | Conducted through HackerOne. [Learn more](https://hackerone.com/bitwarden/?type=team). |

#### APIs and Extensibility

| Enterprise Features | Description |
|------|------|
| Programmatically accessible | Public and Private APIs for Organizations. [Learn more](https://bitwarden.com/help/public-api/). |
| Command line interface | Fully featured and self-documented command-line tool. [Learn more](https://bitwarden.com/help/cli/). |
| Extensibility support | Automate workflows by combining API and CLI. |
| SSH Agent | The Bitwarden desktop app can serve as an SSH agent, securely storing and serving SSH keys to terminals and development tools without exposing private keys on disk. [Learn more.](https://bitwarden.com/help/ssh-agent/) |
| Secrets Manager | A dedicated secrets management product (separate subscription required) for DevOps and engineering teams to securely store, share, and inject secrets (API keys, tokens, credentials) into CI/CD pipelines and infrastructure tools. Integrates with GitHub Actions, GitLab CI/CD, Ansible, Terraform, and Kubernetes. [Learn more.](https://bitwarden.com/products/secrets-manager/) |

#### Resiliency

| Enterprise Features | Description |
|------|------|
| Server geographies | Select to have your cloud data hosted on either US- or EU-based Microsoft Azure servers. [Learn more.](https://bitwarden.com/help/server-geographies/) |
| Local cache & offline access | Logged in clients can access Bitwarden vaults with a read-only cache that remains on the device for 30 days. [Learn more](https://bitwarden.com/help/security-faqs/). |
| Data backup tools | In addition to vault exports that may be scripted, self-host deployments have access to [toolsets to assist with data backup](https://bitwarden.com/help/backup-on-premise/) and restoration. Cloud deployments are supported by [Azure point-in-time restoration policies](https://bitwarden.com/help/data-storage/#on-bitwarden-servers/) for disaster recovery. |
| Dedicated customer support | Enterprise customers receive priority support and access to dedicated customer success resources, including onboarding playbooks, the [Customer Success Hub](https://bitwarden.com/help/customer-success-hub/), and direct support channels. [Learn more.](https://bitwarden.com/products/business-support/) |
