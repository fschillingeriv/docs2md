---
URL: https://bitwarden.com/help/legacy-user-support/
---

# Legacy User Support

> [!NOTE] update encryption scheme if you haven't
> As of the 2025.6.2 server release deployed on June 24, 2025 Bitwarden has officially removed support for legacy users. 
> 
> - **If your account was created after 2017**, you are not impacted by this change.
> - **If your account was created before 2017**, as long as you have logged in to the web app since 2023, you are not impacted by this change.

**Accounts created prior to 2017** leveraged an encryption scheme that used a key derived from your master password directly to encrypt account data. This encryption method was inflexible and created an environment with potential vulnerabilities. In 2017, Bitwarden's [encryption scheme](https://bitwarden.com/help/bitwarden-security-white-paper/#hashing-key-derivation-and-encryption/) was updated to address these vulnerabilities. Following this update:

- (2017) Workflows for automatically migrating accounts to the new encryption scheme were added to the web app.
- (2023) Bitwarden clients, not including the web app, underwent changes that prevented legacy users from logging in. Error messages directed users to log in on the web app to execute migration.
- (2025) Bitwarden servers underwent changes that logged remaining legacy users out of active sessions, requiring them to log in on the web app to execute migration. Impacted users were emailed following these changes.

As a result of these actions, as of version 2025.6.1, it is unlikely that any actively-used Bitwarden accounts still utilize the legacy encryption scheme.
