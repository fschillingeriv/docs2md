---
URL: https://bitwarden.com/help/two-step-recovery-code/
---

# Recovery Code for Two-Step Login

Bitwarden provides a unique recovery code when you activate any [two-step login method](https://bitwarden.com/help/setup-two-step-login/). If you [lose your authentication device](https://bitwarden.com/help/lost-two-step-device/), use this code to disconnect all two-step login methods and regain access to your account. If you lose both your recovery code and two-step device, like a phone with an authenticator app or linked email inbox, you may be locked out of your vault.

## Save your recovery code

Save your recovery code immediately after turning on any two-step login method and store it in the secure location of your choice. A printed copy kept in a safe place is a good option, because it prevents digital theft and accidental deletion.

> [!NOTE] Recovery code changes after use
> After [using a recovery code](https://bitwarden.com/help/two-step-recovery-code/#save-your-recovery-code/), a new one is generated. Make sure to save the updated code. Adding new two-step login methods or changing your master password does not impact the recovery code.

To find your recovery code in the Bitwarden web app:

1. After setting up at least one two-step login method, go to **Settings** → **Security**.
2. Select **Two-step login**.
3. Select **View recovery code**:

![Two-step login](https://bitwarden.com/assets/2BsKs83g4cmiCUwxf2ad83/b2a90e85355f3d937aeb46139203737e/2024-12-02_10-54-31.png)
*Two-step login*
4. Enter your master password and select **Continue**. Your recovery code will appear:

![Example recovery code](https://bitwarden.com/assets/64piqJsX7vN25To16iRFIp/09e977fae9485c0764f832c6bb4b4b04/2024-12-02_11-24-35.png)
*Example recovery code*

## Use your recovery code

To regain access to your account with its recovery code:

1. Go to the recovery page for your account's [server location](https://bitwarden.com/help/server-geographies/):

 - **United States**: [https://vault.bitwarden.com/#/recover-2fa/](https://vault.bitwarden.com/#/recover-2fa/)
 - **European Union**: [https://vault.bitwarden.eu/#/recover-2fa/](https://vault.bitwarden.eu/#/recover-2fa)
 - **Self-hosting**: `https://your.domain.com/#/recover-2fa/`
2. Enter your email address, master password, and recovery code.
3. Select **Submit**.

Once your account details and recovery code are authenticated, you'll be logged in to your vault and all previously set up two-step login methods will be deactivated. 

> [!NOTE] Recovery Codes + Duo for Orgs
> Recovery codes will not deactivate Duo for organizations. If you are locked out of your vault by an organizational Duo prompt, reach out to the Duo administrator at your company for help bypassing the prompt.
> 
> If you're not sure whether the Duo prompt is setup personally or by your organization, try selecting **Use another two-step login method**.

To maintain secure and reliable access to your account afterwards:

- Set up or reactivate at least one [two-step login method](https://bitwarden.com/help/setup-two-step-login/). If you don’t, Bitwarden will send a [verification code](https://bitwarden.com/help/new-device-verification/) to your account email when you log in from an unrecognized device.
- [Save your new recovery code](https://bitwarden.com/help/two-step-recovery-code/#save-your-recovery-code/), because it changes after being used.

### Enterprise members

When you’re an Enterprise organization member, what happens after you submit a valid recovery code may differ.

If your organization [requires single sign-on authentication](https://bitwarden.com/help/policies/#require-single-sign-on-authentication/) but does not [require two-step login](https://bitwarden.com/help/policies/#require-two-step-login/), you will be directed to the SSO login page. Use your SSO credentials to log in and access your Bitwarden vault.

If your organization [requires two-step login](https://bitwarden.com/help/policies/#require-two-step-login/), successfully using the recovery code will remove you from the organization. To rejoin the organization once you’re logged in:

1. Set up a new [two-step login method](https://bitwarden.com/help/setup-two-step-login/).
2. If your organization also [requires single sign-on authentication](https://bitwarden.com/help/policies/#require-single-sign-on-authentication/), reconnect your SSO credentials to your Bitwarden account.
3. Ask an admin or owner to [restore your account](https://bitwarden.com/help/revoke-users/#restore-access/) within the organization.
