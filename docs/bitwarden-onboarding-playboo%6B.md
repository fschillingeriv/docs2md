---
URL: https://bitwarden.com/help/bitwarden-onboarding-playboo%6B/
---

# Bitwarden Onboarding Playbook

This playbook provides IT administrators with a flexible roadmap for onboarding users to Bitwarden Password Manager across five key phases. While the phases are presented in sequence, they're not strictly linear. Many steps can happen in parallel based on your team's needs and timeline.

Throughout this guide, you'll find action items in code boxes that can be copied and pasted directly into your project management tools, internal documentation, or team communication platforms. This makes it easy to track progress, assign tasks, and maintain accountability during your Bitwarden rollout. Use this guide as a foundation and adapt it to fit your environment. 

### 1: Training 

> [!NOTE] Phase 1 tip
> Phase 1 focuses on educating stakeholders, preparing systems, and establishing the knowledge base for successful setup. Bitwarden recommends scheduling training sessions for each group or team before or during rollout. 

## Key objectives

- Establish training programs for all user levels
- Prepare technical infrastructure and requirements
- Create organizational and collection management policies and procedures
- Build internal expertise and support capabilities

## Activities

#### Step 1: Administrator training

**Key personnel:** IT directors, system admins, owners

**Training topics:**

- Bitwarden architecture and enterprise features
- Scalable sharing capabilities

 - Collection setup; organize and group related credentials, secrets, or other vault items
 - Adding a user to the Bitwarden organization 
 - Assigning appropriate permissions to members or groups for each collection
 - Assigning certain items to multiple collections so the right people can access without duplication 
- Setup and Policies

 - SSO setup and integration workflows
 - Two-factor authentication setup and policies
 - Security policies and enterprise controls
- Management and reporting

 - Custom fields and roles management
 - User and group management best practices
 - Event logging and reporting capabilities

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
[ ] Schedule administrator training sessions
[ ] Review enterprise feature requirements
[ ] Document SSO integration requirements
[ ] Plan custom roles and permission structures
[ ] Establish security policy framework
[ ] Document cyber insurance compliance requirement
 [ ] Prepare business case including insurance premium impact
 [ ] Align rollout timeline with insurance renewal dates
```

#### Step 2: Service desk training 

**Key personnel:** Help desk staff, customer success leads

**Training topics:**

- Common user issues and troubleshooting
- Password reset procedures and limitations
- Account recovery processes
- Escalation procedures for complex issues

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
[ ] Train support staff on Bitwarden functionality
[ ] Create troubleshooting documentation
[ ] Establish support ticket workflows
[ ] Define escalation procedures
```

#### Step 3: End user training 

Note: For many customers, end user training comes right before or during rollout, as each department is onboarded. Bitwarden recommends prioritizing admin training first. 

**Key personnel:** All end users across the company

**Training topics:**

- Password import processes and best practices if applicable 
- Cross-platform Bitwarden usage (desktop, mobile, web, browser)
- Account creation and master password guidelines
- Vault navigation and organization features
- How to save a new login
- Autofill options
- Password generator 
- Bitwarden Send for secure sharing
- Collaboration through collections

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
[ ] Schedule organization-wide training sessions by functions; recommend starting with more technical teams (ie. tech team, data team)
[ ] Create user documentation and quick reference guides. Leverage resources available in the Bitwarden help center
[ ] Prepare import templates and migration tools
[ ] Establish help desk support procedures
```

#### Step 4: Leadership training

**Key personnel:** Department leads, executive leadership

**Training topics:**

- Why Bitwarden is important for securing the organization 
- Password import processes and best practices if applicable 
- Identify at-risk passwords with Vault Health reports 
- Cross-platform Bitwarden usage (desktop, mobile, web, browser)
- Account creation and master password guidelines
- Vault navigation and organization features
- How to save a new login
- Autofill options
- Password generator 
- Bitwarden Send for secure sharing
- Collaboration through collections

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
[ ] Get leadership buy-in and identify advocates. Bitwarden research shows that company-wide password management mandates more than doubles regular usage. 
[ ] Train leadership on importance of using a password manager
[ ] Show leadership how easy it is to use
```

### 2: Setup 

> [!NOTE] Phase 2 Tip
> Phase 2 is the technical setup phase where Bitwarden is deployed and configured for your organization. 

## Key objectives

- Deploy Bitwarden infrastructure (cloud or self-host)
- Configure organizational structure and policies
- Establish security and identity integrations ([SSO](https://bitwarden.com/resources/choose-the-right-sso-login-strategy/), [SCIM](https://bitwarden.com/help/about-scim/))
- Prepare for user rollout (see [phase 3](https://bitwarden.com/help/bitwarden-onboarding-playbook/#tab-3:-prep-5hNzVYHnEiUgdYnhS6KJ0t/)) 

## Option A: Bitwarden cloud (recommended)

Bitwarden hosted is recommended for most organizations. Enjoy easy scalability, automatic updates, and minimal maintenance on secure, reliable servers managed by Bitwarden.

#### Step 1: Pre-setup planning

Before diving into the technical setup, it's important to establish your organizational strategy and approach. Below are key recommendations to consider.

##### Choose between US or EU cloud server regions

Organizations must choose [between US or EU cloud server](https://bitwarden.com/help/server-geographies/) regions based on data residency requirements. Bitwarden cannot migrate accounts from one region to another for customers. A script is available for organizations to help facilitate migrations. Subscriptions can be transferred from one region to another region by contacting support.

##### Set the foundation for centralized ownership and credential lifecycle management 

**New customers **

- Begin with centralized ownership by enabling the **Enforce organization data ownership**policy from day one and start managing the entire credential lifecycle across applications. 
- Every user (excepting admins and owners at this time) receives an organization-owned **My items** space for seamless, day-to-day work
- All credentials are organization-owned, with reporting benefits built in
- Simplify employee transitions, so credentials follow the person’s role changes and can be seamlessly reassigned when responsibilities shift. 

**Existing customers**

- Continue using your current setup while Bitwarden prepares a seamless path to centralized ownership for previously individual-held credentials. 
- You’ll soon be able to bring every credential into the company vault, aligning all users under a single model of ownership
- Contact your account team for more information on timing
- Gain organization-wide control and insights into credential health and usage with centralized reporting.
- Ensure seamless employee transitions by securely reassigning or deleting credentials without disruption.
- Enforce least privilege by assigning roles, segmenting credentials into collections by department or function, granting users and groups access only to the collections they need.
- Reinforce good password practices and begin bringing insights into the credential lifecycle - creation, access, transfer, and deletion - with enterprise policies.

##### Bitwarden recommends SSO with trusted devices

For the best user experience, Bitwarden recommends [SSO with trusted devices](https://bitwarden.com/help/about-trusted-devices/). This allows employees to log in and decrypt their vaults in a single step, though it requires additional IT admin setup time. Here are items to consider with this approach:

- Enforce a session timeout policy of "Log out" which provides one consistent user experience: after timeout, employees simply re-authenticate via SSO with no master password required.
- In trusted devices environments, “Unlock” behaves as “Log out” unless users configure PIN or biometrics
- If your organization actively promotes PIN or biometrics, admins may choose “Unlock” but only if user communications make that expectation clear.
- Session timeout: Bitwarden recommends between 4-10 hours for most use cases to balance productivity and security.

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
[ ] Determine cloud server region (US, EU)
[ ] Determine overall organizational data ownership
[ ] Choose authentication and decryption strategy
[ ] Define user onboarding and deprovisioning approach 
 [ ] Manual invitation
 [ ] Bitwarden Directory Connector
 [ ] SCIM
 [ ] Just-in-Time SSO
[ ] Define vault ownership strategy (Individual vaults vs. Organization-only)
[ ] Identify user groups for rollout phases
[ ] Stakeholder selections:
 [ ] Project lead
 [ ] Identity provider admin
 [ ] Executive sponsor
 [ ] Security and compliance admin
 [ ] Support/help desk admin
 [ ] Device management admin (for client deployment)
 [ ] Business continuity admin
 [ ] Directory/user management admin
```

#### Step 2: Organization creation

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
[ ] Create new Bitwarden organization account
[ ] Select appropriate enterprise plan
[ ] Configure billing and payment methods
```

#### Step 3: Core setup

Follow the recommendations below to ensure a smooth Bitwarden setup.

##### Claim all corporate email domains 

To restrict certain user actions, grant administrators greater control, and simplify the login experience for your users.

##### Set up enterprise policies before user onboarding

Set up all [enterprise policies](https://bitwarden.com/help/policies/) before user onboarding begins to ensure consistent security controls from day one.

##### Establish strong security baselines

With minimum 14-16 character [master passwords](https://bitwarden.com/help/policies/#master-password-requirements/) (including uppercase, lowercase, numbers, and symbols) and password generator minimums of at least 14 characters with symbols and numbers.

##### Enable single organization restriction

To prevent users from joining other Bitwarden organizations, maintain data governance and prevent potential data leaks.

##### Set up your organization vault

If you already use groups and objects in your IdP or Directory, mirror that framework in Bitwarden for consistency. Folder-like objects will automatically be converted to collections during import.

Remember: Bitwarden is different from traditional applications. For Bitwarden, everything is protected with end-to-end encryption, and access policies are enforced at the client level. That means:

- Admins can define and assign access, but they can’t see the credentials themselves.
- Collections and groups are the way Bitwarden enforces access while preserving zero-knowledge.
- Some operations (syncing, policy checks, vault actions) require additional processing on the client side instead of being visible in plaintext to the server.

If starting from scratch:

- [Collections (what gets shared)](https://bitwarden.com/help/collection-management/)**:** Best practice is to organize Collections based on the function of the resources being shared (eg. shipping profiles, advertising platform logins)  Keep collections broad at first; add granularity when necessary. Typically, IT admins manage org-wide collections, while team leads manage department-specific ones.
- [Groups (who gets access)](https://bitwarden.com/help/about-groups/): Use Groups to represent departments or teams (eg. Marketing, Finance) and aligning them 1:1 with collections for clarity. Unique groups that span functions (executive assistants, IT admins, purchase approvers) are also common.

> [!NOTE] Scalable sharing tip
> **Remember**: The Bitwarden scalable sharing model means that items can live in multiple collections simultaneously, without compromising security. Teams can access credentials they need without unnecessary exposure to entire vaults

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
[ ] Configure domain claiming
[ ] Set up enterprise policies for mandatory security controls
[ ] Set up password and password generator minimums
[ ] Organization data ownership enforcement to require all vault items in organization
[ ] Create organizational structure - collections, groups
[ ] Configure user roles and permissions
```

#### Step 4: Integration setup

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
SSO integration (if applicable):
[ ] Configure SAML 2.0 or OIDC with identity provider
[ ] Test SSO login workflows
[ ] Configure trusted devices (if applicable)
[ ] Document SSO troubleshooting procedures

Directory Integration (if applicable):
[ ] Install and configure Directory Connector
[ ] Set up SCIM provisioning (Azure AD, Okta, OneLogin, JumpCloud)
[ ] Test user and group synchronization
[ ] Schedule automated sync intervals
```

#### Step 5: Security controls

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
[ ] Set up event logging and SIEM integration
[ ] Establish backup and recovery procedures
```

## Option B: Self-hosted (advanced)

*What does it mean to self-host?*

Running Bitwarden on your own servers requires advanced technical knowledge and IT infrastructure. It also means that you are responsible for server maintenance, security, uptime, and updates. 

To assess whether self host is right for you:

- Do you already have anything else self-hosted?
- Do you have dedicated hardware to run the server?
- Is there an IT or DevOps team that will be responsible for the server?
- Are you familiar with Docker, or Kubernetes and Helm charts?
- Are you comfortable installing software using [Linux terminal](https://bitwarden.com/help/install-on-premise-linux/) or [PowerShell](https://bitwarden.com/help/install-on-premise-windows/#installation-procedure/)?

If you decide to self-host Bitwarden, follow the steps below. 

#### Step 1: Pre-setup planning

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
[ ] Choose self hosted deployment method (Linux standard/manual/offline, Windows standard/offline, or Kubernetes)
[ ] Define server/VM specs and hosting environment (environment variables, firewall or proxy)
[ ] Decide on SSL certificate approach
[ ] Plan network architecture, firewall or proxy rules, access controls
[ ] Scalability planning
[ ] Select key roles
 [ ] Project lead
 [ ] Executive sponsor
 [ ] Server admin
 [ ] Docker admin
 [ ] Network admin
 [ ] Firewall admin
 [ ] Support/help desk admin
 [ ] Database admin
 [ ] Identity provider admin
 [ ] SMTP admin
 [ ] Security and compliance admin
 [ ] Backups admin
 [ ] Business continuity admin
 [ ] Disaster recovery admin
 [ ] Device management admin
```

#### Step 2: Infrastructure preparation

Set up a dedicated environment for your Bitwarden server. Requirements vary depending on your operating system. See [Help center](https://bitwarden.com/help/self-host-bitwarden/) for detailed instructions.  

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
[ ] Provision hardware that meets minimum requirements 
[ ] Configure DNS records and domain name
[ ] Open ports 80 and 443
[ ] Install server offerings and containerization tools
[ ] Obtain installation ID and key from Bitwarden
[ ] Secure SSL certificates
```

#### Step 3: Bitwarden server installation

Install Bitwarden in your prepared environment. The exact steps differ depending on the operating system. 

#### Step 4: Organization setup

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
[ ] Create cloud organization for billing purposes
[ ] Link self-hosted installation to billing organization
[ ] Configure enterprise settings and policies
[ ] Set up collections and groups structure
[ ] Test all integrations (SSO, SCIM)
```

#### Step 5: Maintenance planning

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
[ ] Create server update and maintenance schedule
[ ] Implement automated backup system
[ ] Set up off-site backup storage
[ ] Test disaster recovery procedures
[ ] Document maintenance and backup/recovery procedures
[ ] Set up monitoring and alerting for backup failures; evaluate backup methods
```

### 3: Plan

> [!NOTE] Phase 3 Tip
> Phase 3 focuses on organizational readiness and communication before user onboarding begins. This phase ensures smooth user adoption by setting proper expectations, addressing concerns, and creating organizational momentum for the change.

## Key objectives

- Communicate the Bitwarden implementation to the entire organization
- Address user concerns and resistance to change
- Prepare support resources and documentation
- Conduct final system testing and validation
- Create organizational excitement and buy-in for improved security

## Activities

#### Step 1: Prepare company-wide communication from leadership

> [!NOTE] Mandate Tip
> Leadership is critical to adoption success. [Bitwarden research](https://bitwarden.com/resources/bitwarden-security-impact-report/) shows that company-wide password management mandates more than doubles regular usage. 

**Key Personnel:** Executive leadership, IT leadership, communications team, department leads.

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
[ ] Prepare leadership talking points about security benefits
[ ] Schedule leadership communication sessions (all-hands, team meetings)
[ ] CEO/Leadership announcement about password security initiative
[ ] Clear messaging about why Bitwarden was chosen
[ ] Timeline communication for rollout phases
[ ] Expectation setting for mandatory adoption
[ ] Emphasis on security benefits for both work and personal use
[ ] Highlight cyberinsurance benefits and that implementing Bitwarden is a prerequisite to get approved for higher level of coverage; document insurance coverage being met
```

#### Step 2: Organizational communication campaign

**Key personnel:** Communications team, HR, IT support.

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
Communication strategy:
[ ] Develop multi-channel communication plan (email, intranet, meetings)
[ ] Create consistent messaging about security benefits
[ ] Address common concerns and objections proactively
[ ] Highlight ease of use and convenience benefits
[ ] Share success stories from pilot users or other organizations

Pre-rollout communications:
[ ] All hands meeting: Initial introduction to Bitwarden
 [ ] Why we're implementing password management / Bitwarden
 [ ] Security benefits for the organization and individuals
 [ ] Why it is important to follow the directions shared by IT
 [ ] Expect more details in your email inbox

[ ] Announcement email: More details on Bitwarden and roll out plan
 [ ] Recap: Why we're implementing password management / Bitwarden
 [ ] Recap: Security benefits for the organization and individuals
 [ ] Timeline for rollout and training
 [ ] What to expect in coming weeks

[ ] FAQ document: Address common questions and concerns
 [ ] "Will this slow down my workflow?"
 [ ] "What happens to my existing passwords?"
 [ ] "Is my personal information secure?"
 [ ] "What if I forget my master password?"
 [ ] "Do I have to use this for personal passwords, too?"
```

#### Step 3: Change management readiness

**Key personnel:** HR, change management team, department managers

**Change management activities**

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
 [ ]  Identify and engage change champions in each department
 [ ]  Conduct department-specific communication sessions
 [ ]  Address cultural and workflow concerns
 [ ]  Plan for resistance management and additional support
 [ ]  Create peer support networks and feedback channels
```

### 4: Rollout 

> [!NOTE] Phase 4 Tip
> Phase 4 ensures Bitwarden is actively used with the introduction of users to Bitwarden, ensuring proper account setup and initial usage. 
> 
> Reminder for admins that all Bitwarden onboarding **process flow:** Invite → Accept → Confirm

## Key objectives

- Onboard all users to the platform in phases or all at once
- Ensure proper account setup and security setup
- Facilitate password migration and initial vault population
- Establish user proficiency with core features

## Choose your rollout path

**Option A: Phased rollout (recommended for most organizations)**

- Roll out in waves across teams and departments (eg.10% > 20% > 70%)
- Ideal for larger organizations or those who want to reduce internal disruption
- Easier to pace communications, training, prevent service desk overload, and allows admins to iterate and improve the process.

**Option B: All at once (advanced)**

- Works well for smaller organizations or large organizations with strong IT and training resources
- Best if you can coordinate communications and support for everyone at once

> [!NOTE] Rollout Callout
> Running a small pilot (20-100 users, depending on your organization size) can help validate rollout across all main use cases (desktop, mobile, browser, SSO, etc) This helps refine communications and creates internal champions.

Important note on the invitation and re-invitation process: Invite users after enterprise policies are configured and the core admin team has onboarded. This ensures new members are immediately subject to your organization’s security and usage standards.

Users automatically receive an email invitation when provisioned via SCIM or Directory Connector. For phased rollouts, coordinate with your IT or email team to filter (based on subject lines) specific onboarding emails at the mail gateway and send these emails when you’re ready for the next group to onboard.  After a user accepts their invitation, an organization admin or owner must confirm their membership before vault access is granted. During rollout, admins should check the Members screen regularly (multiple times per day for larger orgs) to approve pending users. Confirmation can be automated with a script, but note that doing so reduces security visibility.

Invitations expire after 7 days. Users still showing as Invited after several days may need IT follow-up to ensure adoption. Admins can also trigger a Reinvite, which sends a fresh invitation email as a reminder to join the organization.

#### Step 1: Rollout planning

> [!NOTE] Phased Rollout
> The phased rollout approach, department by department, was selected by [Bitwarden customers as being “very effective.”](https://bitwarden.com/resources/bitwarden-security-impact-report/)

**Key personnel:**Organization administrators

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
[ ] Identify groups of users who will be onboarded first (usually more technical teams)
[ ] Follow a 10-20-70 rule for roll out (first 10% of users, then 20%, then 70%)
[ ] Document timeline for each roll out phase
```

#### Step 2: User account creation and access

**Key personnel:** All invited users, organization administrators

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
User actions:
[ ] Accept organization invitation via email link
[ ] Log in with existing account or create new account using invited email
[ ] If applicable, create strong master password (14-16+ characters with mixed case, numbers, symbols)

Administrator actions:
[ ] Send organization invitations in planned waves (remember process flow: Invite → Accept → Confirm)
[ ] Distribute Bitwarden onboarding guides and/or customized onboarding guides and intranet knowledge base articles
[ ] Monitor invitation acceptance rates
[ ] Confirm user accounts after acceptance
[ ] Assign users to appropriate groups and collections
[ ] Verify SSO and authentication workflows
[ ] Configure MDM deployment if needed
```

#### Step 3: Client installation and setup

**Key personnel:** All users

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
Installations:
[ ] Configure server URL if not using vault.bitwarden.com and confirm web vault access
[ ] Install browser extension and pin to toolbar
[ ] Install and configure web vault access
[ ] Download and install desktop application (Windows/macOS/Linux)
[ ] Download mobile apps (iOS/Android)
[ ] Log into all installed clients with master password and 2FA

Setup tasks:
[ ] Configure browser extension settings and permissions
[ ] Set up mobile autofill permissions
[ ] Configure biometric unlock (desktop/mobile, if available)
[ ] Test synchronization across all devices
```

#### Step 4: Vault setup and navigation

**Key personnel:** All users

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
Navigation training:
[ ] Explore web vault interface and main navigation elements
[ ] Understand difference between My Vault (individual) and Organization Vault (shared)
[ ] Learn to use search functionality across vault items
[ ] Familiarize with item types (Logins, Notes, Cards, Identities)

Collection and organization understanding:
[ ] Understand Collections concept for shared items
[ ] Access items shared through collections
[ ] Learn about Groups and permission levels
[ ] Practice organizing items with folders
```

#### Step 5: Password management implementation

**Key Personnel:** All users

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
Core functionality:
[ ] Practice manually adding new login items
[ ] Learn to edit existing vault items
[ ] Set up browser extension autofill and auto-save features
[ ] Practice different autofill experiences from browser extension
[ ] Use built-in password generator for creating strong passwords

Advanced features:
[ ] Explore Bitwarden Send for secure item sharing with individuals outside of your organization
[ ] Review password history for login items
[ ] Configure autofill options (inline vs context menu)
[ ] Set up TOTP (Time-based One-Time Password) generation
[ ] Utilize clipboard history features
```

#### Step 6: Password migration and import

**Key Personnel:** All users, with IT support

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
Migration process:
[ ] Export passwords from current password managers
[ ] Use Bitwarden import tools for bulk migration
[ ] Manually add critical passwords not captured in import
[ ] Verify all imported items are accessible and functional
[ ] Update weak or duplicate passwords using generator

Quality assurance:
[ ] Complete security audit of imported passwords using Bitwarden vault health reports
[ ] Identify and update weak passwords
[ ] Resolve duplicate entries
[ ] Verify critical business applications are included
```

### 5: Adoption 

> [!NOTE] Phase 5 Tip
> Phase 5 focuses on adoption, maximizing value, ensuring security compliance, and maintaining long-term success.

## Key objectives

- Achieve full organizational adoption 
- Establish ongoing security and maintenance practices
- Optimize workflows and advanced feature utilization
- Maintain continuous improvement and support
- Incorporate Bitwarden training into new employee onboarding

## Activities

#### Step 1: Adoption and optimization 

**Key stakeholders:** All users, organization administrators.

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
User verification:
[ ] Test login across all devices and browsers
[ ] Verify sharing and collaboration features work properly
[ ] Confirm understanding of organization's password policies
[ ] Validate emergency access and recovery procedures
[ ] Document personal backup and security measures

Administrative verification:
[ ] Monitor user adoption metrics through event logs
[ ] Verify policy compliance across the organization
[ ] Review and optimize collection and group structures
[ ] Analyze usage patterns and identify improvement opportunities
[ ] Deploy technical enforcements such as:
 [ ] Turn off browser based password managers
 [ ] Remove access to documents (google docs, excel, etc) where passwords were previously stored 
```

#### Step 2: Security audit and compliance

**Key stakeholders:** Security team, organization administrators.

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
Security review:
[ ] Complete comprehensive security audit using Bitwarden reports
[ ] Review exposed passwords and security breaches
[ ] Analyze password strength across the organization
[ ] Monitor 2FA adoption rates
[ ] Review and update security policies as needed

Compliance activities:
[ ] Document compliance with organizational security standards
[ ] Review event logs for suspicious activities
[ ] Validate backup and disaster recovery procedures
[ ] Ensure proper data retention and deletion policies
[ ] Conduct periodic security assessments
```

#### Step 3: Advanced feature implementation

**Key stakeholders:** Power users, organization administrators.

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
Advanced capabilities:
[ ] Implement custom fields for specialized data
[ ] Configure advanced sharing workflows
[ ] Utilize API integrations for business applications
[ ] Set up automated reporting and monitoring
[ ] Implement CLI tools for advanced users
```

#### Step 4: Ongoing support 

**Key stakeholders:** IT support, organization administrators.

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
Support structure:
[ ] Establish regular support office hours
[ ] Create escalation procedures for complex issues
[ ] Maintain updated documentation and training materials
[ ] Monitor and respond to user feedback
[ ] Provide ongoing training for new features
```

#### Step 5: Continuous improvement

**Key stakeholders:** All users, organizational administrators.

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability: 

```plain text
Regular reviews:
[ ] Schedule quarterly security and usage reviews
[ ] Collect and analyze user feedback
[ ] Monitor industry best practices and updates
[ ] Review and update organizational policies
[ ] Plan for future enhancements and expansions

Success metrics:
[ ] User adoption and engagement rates
[ ] Indicators of vault usage such as stored credentials in organizational vaults
[ ] Regular usage of key features (autofill, password saving, password sharing)
[ ] Password security improvements
[ ] Reduction in security incidents
[ ] Time savings in credential management
[ ] Compliance with organizational security standards
```

#### Step 6: New employee onboarding

**Key stakeholders:** new employees, HR, organizational administrators.

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability: 

```plain text
[ ] Document Bitwarden best practices in onboarding resources or new hire checklist
[ ] Offer recurring Bitwarden trainings for new employees
[ ] Encourage new hires to ask for help from existing employees 
```

### Resources

Use these additional resources to help guide you through the phases during your Bitwarden journey:

## Success checklist

Copy and paste this list directly into your project management tools, internal documentation, or team communication platforms to easily track progress, assign tasks, and maintain accountability:

```plain text
[ ] 100% user adoption of all purchased Bitwarden seats 
[ ] Complete password migration from legacy systems and other password managers
[ ] Security posture improvements (reduction of breaches, promotes safe password habits) 
[ ] Reduce number of at-risk credentials (reused, exposed, weak) across the entire organization
[ ] Value achieved beyond password management (Bitwarden Send, storing sensitive information such as credit cards, identifies, notes, and more)
[ ] Internal champions excited to help others achieve password security success
[ ] Full integration with existing identity and security infrastructure
[ ] Established security policies and compliance procedures
[ ] Ongoing support and maintenance frameworks
[ ] Documented Bitwarden procedures for onboarding new employees
[ ] Optimized workflows for maximum efficiency and security
[ ] Regular monitoring and continuous improvement processes
```

## Bitwarden support

- **Billing support:** Contact customer success for expedited billing assistance
- **Technical support:** Available for all users with comprehensive troubleshooting
- **Enterprise customers:** Ongoing meetings with global accounts managers
- **Executive access:** Periodic meetings with Bitwarden executives for enterprise clients

## Templates

[<u>Rollout email templates</u>](https://bitwarden.com/help/rollout-email-templates/): Email templates to announce the Bitwarden Password Manager rollout to your end users, administrative users, and IT teams. Attach your branding to these emails and adapt them as needed. 

[<u>End user onboarding email templates</u>](https://bitwarden.com/help/end-user-onboarding-emails/): Onboarding emails sent to new Bitwarden Enterprise and Teams users from care@bitwarden.com. 

[<u>Customer activation kit</u>](https://bitwarden.com/help/customer-activation-kit/): Ready-made communication materials including one-pagers, training videos, posters, email templates, and promotional resources to support your rollout.

[<u>Slide deck announcement template</u>](https://docs.google.com/presentation/d/1zK8NDB6E8ID_ok_yxn5x5qjO7mzeI5CZ-kqcOsfcQcU/edit?usp=sharing): Slide deck template to the Bitwarden Password Manager to the whole company or organization. Attach your company branding and roll-out details as needed.

## Go deeper

[<u>Bitwarden Courses</u>](https://bitwarden.com/help/courses/) - Monthly updated video content

[<u>Weekly Live Demos</u>](https://bitwarden.com/resources/demos/) - Interactive Q&A sessions

[<u>Enterprise Feature List</u>](https://bitwarden.com/help/enterprise-feature-list/) - Comprehensive feature documentation

[<u>API Documentation</u>](https://bitwarden.com/help/api/) - For advanced integrations

[<u>Community Forums</u>](https://community.bitwarden.com/) - User community and support
