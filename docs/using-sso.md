---
URL: https://bitwarden.com/help/using-sso/
---

# Log In With SSO

If you're a member of an Enterprise organization, you may be [required](https://bitwarden.com/help/policies/#require-single-sign-on-authentication/) or permitted to log in to Bitwarden using single sign-on, similarly to how you log in to other work-related applications:

1. Open the Bitwarden app, enter your email address, and select **Use single sign-on**:

![Use the single sign-on button](https://bitwarden.com/assets/3XPDLW9GBkA4TIk1j6EAXq/37d89e28b4d913e7a5031ff1c06fc783/2025-10-13_10-39-36.png)
*Use the single sign-on button*
2. Your organization **may** require you to enter an **SSO identifier**. If you see the following screen, enter your organization's SSO identifier or ask a manager or administrator to retrieve it for you if you don't know it.

![SSO identifier screen](https://bitwarden.com/assets/5sNF8v7r2HsyLQm8gd6xBC/ac61e5e2bb0c733b3498536be584db9a/2025-10-13_10-46-01.png)
*SSO identifier screen*

> [!TIP] Prevent the need for SSO identifiers.
> **Organization Members**: Bookmark this page with your identifier included in the URL, for example`https://vault.bitwarden.com/#/sso?identifier=my-identifier`so that you don't have to enter it each time you log in.
> 
> **Organization Admins**: Setting up a [claimed domain](https://bitwarden.com/help/claimed-domains/) will automatically bypass this step for your members if they have an email address with a matching domain.
3. Once you're redirected to your IdP (for example, Microsoft Azure, Duo, or OneLogin), enter your SSO credentials to log in as you would with other apps. Often, at this stage, your IdP will require you to complete 2FA.
4. What happens next depends on your organization's chosen [decryption option](https://bitwarden.com/help/sso-decryption-options/):

### Master password

Enter your master password or, if your account is new, create a [master password](https://bitwarden.com/help/master-password/) in order to complete your log in:

![Decrypt with master password](https://bitwarden.com/assets/TJ0nUZ4zs7l38aOQz5WLl/6b95624ef2271198f6fc6447b77d63c1/2025-10-13_12-57-15.png)
*Decrypt with master password*

> [!TIP] Why is master password still required?
> **Why is my master password still required?**
> 
> All item data, including credentials [shared by your organization](https://bitwarden.com/help/sharing/), is stored by Bitwarden **only** in its encrypted form. This means that in order to use any of those credentials, **you** need a way to decrypt that data. We can't.
> 
> Your master password is the source of that decryption key. Even though you are authenticating (proving your identity) to Bitwarden using SSO, you still need to use a decryption key (in this case, your master password) to unscramble vault data.

### Device approval

Choose an option for [establishing trust with the device you're logging in on](https://bitwarden.com/help/add-a-trusted-device/) in order to complete your log in:

![Options for establishing trust](https://bitwarden.com/assets/1zrsBanU5CNhFnDHAXazwP/c94f8bfb5066cb79381676570bd87aa1/2025-10-13_13-06-26.png)
*Options for establishing trust*

> [!TIP] Trusted device if its your first login.
> If it's your first time logging in, you'll be allowed to automatically designate this app as a trusted device instead of being required to use one of the above methods:
> 
> 
> ![First trusted device](https://bitwarden.com/assets/6iahsCNPUcIT51P2oZIUQ1/f6dbb4364d96d80c69c3ec84176e7971/2025-10-13_13-03-59.png)
> *First trusted device*

### Key Connector

If your organization uses Key Connector, you will be asked to verify that they are connecting to the correct organization:

![Verify organization Key Connector](https://bitwarden.com/assets/fTrb2sTLVMdjtlpf2yNGD/59e7c37be145ef6525128f73864e3aee/2025-12-17_13-45-48.png)
*Verify organization Key Connector*

If your account was made prior to Key Connector being rolled out, you may be required to enter a master password. Doing so will remove master password from your account.

> [!NOTE] Encourage end-user to learn about Key Connector impacts.
> We encourage you to read about Key Connector to understand the [implications of removing a master password](https://bitwarden.com/help/about-key-connector/#impact-on-organization-membership/) from your account.
5. Last, you may be asked to complete two-step login using [the option you've setup in Bitwarden](https://bitwarden.com/help/setup-two-step-login/). You typically won't be required to use Bitwarden two-step login if your IdP requires it (**Step 3**).

> [!WARNING] If you're JIT provisioning.
> **If you're joining the organization for the first time**, you won't need to complete **Step 5** and won't be able to access organization data until an administrator confirms your membership.
