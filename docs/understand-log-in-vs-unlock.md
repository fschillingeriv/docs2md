---
URL: https://bitwarden.com/help/understand-log-in-vs-unlock/
---

# Understand Log In vs. Unlock

Bitwarden uses two distinct processes to secure your vault without sacrificing convenience: logging in to your Bitwarden account and unlocking your vault. This separation ensures Bitwarden [never stores unencrypted data](https://bitwarden.com/help/vault-data/) on its servers. **When your vault is not unlocked or logged in**, your vault data only exists on the server in its [encrypted form](https://bitwarden.com/help/what-encryption-is-used/).

## Logging in

**Logging in** to Bitwarden retrieves the encrypted vault data and decrypts the vault data locally on your device. In practice, that means two things:

- Logging in always requires your master password, [approved device](https://bitwarden.com/help/log-in-with-device/), or [created passkey](https://bitwarden.com/help/login-with-passkeys/) to gain access to the [account encryption key](https://bitwarden.com/help/account-encryption-key/) that's used to decrypt vault data. Any[ enabled two-step login methods](https://bitwarden.com/help/setup-two-step-login/) are also required at this stage.
- Logging in always requires an internet connection (or, if self-hosting, a server connection) to download the encrypted vault to disk. The vault is then decrypted in your device's memory.

[Embedded content]

## Unlocking

**Unlocking** your vault is only done when you're already logged in. This means, according to the above section, your device has **encrypted** vault data stored on disk. In practice, this means two things:

- You don't specifically need your master password. While your master password *can* be used to unlock your vault, so can other methods like [PIN](https://bitwarden.com/help/unlock-with-pin/) codes and [biometrics](https://bitwarden.com/help/biometrics/).

> [!NOTE] PIN/Bio Encryption
> When you setup a PIN or biometrics, a new encryption key derived from the PIN or biometric factor is used to encrypt the [account encryption key](https://bitwarden.com/help/account-encryption-key/), which you will have access to by virtue of being logged in and stored on disk*.
> 
> **Unlocking** your vault causes the PIN or biometric key to decrypt the account encryption key in memory. The decrypted account encryption key is then used to decrypt all vault data in memory.
> 
> **Locking** your vault causes all decrypted vault data, including the decrypted account encryption key, to be deleted.
> 
> *If you use the **Require master password on browser restart** option, this key is stored only in memory rather than on disk.
- You don't need to be connected to the internet (or, if you are self-hosting, connected to the server).

[Embedded content]
