---
URL: https://bitwarden.com/help/apple-watch-totp/
---

# Bitwarden on Apple Watch 

Our Password Manager [integration authenticator capabilities](https://bitwarden.com/help/integrated-authenticator/) are now accessible on the Apple Watch. Bitwarden Premium members or those with a premium memberships from a paid organization will now have an additional option for accessing time-based one-time passwords (TOTP) codes. Bitwarden for the Apple Watch will show TOTP codes for vault items with seeds stored for easier access when logging into TOTP protected accounts.

> [!NOTE] TOTP membership requirement
> TOTP code generation requires Bitwarden Premium or individual premium membership from a paid organization (Families, Teams, or Enterprise). Learn more about the details of each plan [here](https://bitwarden.com/help/about-bitwarden-plans/#compare-personal-plans/).

## Setup

1. Have the Bitwarden app installed on your iOS mobile device.
2. Check your Apple Watch, Bitwarden should be installed on your watch automatically. If you do not see Bitwarden your Apple Watch, You can manually install Bitwarden on the Apple Watch.

![Apple Watch Bitwarden app](https://bitwarden.com/assets/6pWZMbYpUERAe7wPVKBANZ/eb3046159b774c207510b762947e144d/Screen_Shot_2022-12-02_at_3.53.40_PM__2_.png)
3. Access your Bitwarden account on the iPhone mobile app and select the ⚙️ **Settings**tab.
4. Select the **Other**option and toggle on **Connect to Watch**. Once selected, confirm that the setting is **on**in the pop-up window.

![Connect to an Apple Watch ](https://bitwarden.com/assets/349i1GulSBErWTuDSFOgkW/25a10a9b2a8584fb074c205236311fc8/2025-01-22_10-10-42.png)
5. Once started, the watch will begin syncing with Bitwarden:

When you log out of an account or switch to a different account, the Apple Watch will wipe the current data. Syncing will occur again when logging back into a Bitwarden account on your iOS mobile device.

> [!NOTE] disable watch app
> Turning the Bitwarden Apple Watch connection off in the mobile app will delete all data and disable communication to the Bitwarden app on the Apple Watch.

## Enabling TOTP

If you are new to enabling TOTP codes for vault items, see [here](https://bitwarden.com/help/authenticator-keys/#generate-totp-codes/). If no items have TOTP setup, the Apple Watch will display this screen:

![Apple Watch add 2FA screen](https://bitwarden.com/assets/28ELSN09aicT7i20KcFekH/6a062e0391357ae18abcf60cf819db06/2fa.png)

## Using the Apple Watch to access TOTP codes

1. Unlock your Apple Watch by entering your watch PIN if one has been enabled.
2. Select Bitwarden on your Apple Watch.

![Apple Watch app selection screens ](https://bitwarden.com/assets/7twiT5CXV1jsizjiVTocGM/abdcfe9af5da2b1712e18a0fed59f338/Screen_Shot_2022-12-12_at_5.06.28_PM.png)
3. The vault will sync with the active Bitwarden account on your iOS mobile device. The current account can be seen at the top of the vault page. 

![Apple Watch vault screen](https://bitwarden.com/assets/6JGjNWcUfjrUkLjxgRnjPD/0a9be44d510816b1edf4ec76b44b8778/vault_view.png)
4. Select the vault item you wish to access. The TOTP code and timer will be displayed on the Apple Watch screen. 

![Apple Watch TOTP screen](https://bitwarden.com/assets/4ENEoPkcwuB2dOb0EHDmhR/efaf2e9278212af2297e5155895865ac/totp_bevel_copy.png)

## Bitwarden on Apple Watch security

Bitwarden's zero-knowledge encryption works together with Apple's WatchConnectivity and Secure Enclave will retain zero-knowledge and a secure communication between the iPhone and Apple Watch. Several steps can be taken to increase the security of your accounts and device by:

- Setting a secure passcode to prevent unwanted access to Bitwarden on Apple Watch. Once the Apple Watch is unlocked, information on the device can be viewed.
- Enabling wrist detection on the Apple Watch so the device will lock automatically once it has been removed from the user's wrist.

> [!NOTE] Unlock with iPhone security
> If the Unlock with iPhone setting is enabled, unlocking the connected iPhone will automatically unlock your Apple Watch if the device is nearby. This could potentially expose Bitwarden information on the Apple Watch.

See Apple's [documentation](https://support.apple.com/guide/security/system-security-for-watchos-secc7d85209d/web) for watchOS security to learn more.
