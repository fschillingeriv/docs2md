---
URL: https://bitwarden.com/help/what-encryption-is-used/
---

# Encryption Protocols

Bitwarden **always** encrypts and/or hashes your data on your local device before anything is sent to cloud servers for storage. **Bitwarden servers are only used for storing encrypted data.** For more information, see [Storage](https://bitwarden.com/help/data-storage/).

All vault data is encrypted by Bitwarden before being stored anywhere. To learn how, refer to the [Bitwarden Security Whitepaper](https://bitwarden.com/help/bitwarden-security-white-paper/#how-vault-items-are-secured/). Bitwarden is a zero knowledge encryption solution, meaning you are the only party with access to the keys required to decrypt the vault data. 

> [!NOTE] Bitwarden encryption
> If you'd like to learn more about how these encryption keys are used to protect your vault, you can also check out our [Security Whitepaper](https://bitwarden.com/help/bitwarden-security-white-paper/).

## Authenticated symmetric encryption

Bitwarden uses Advanced Encryption Standard in cipher block-chaining mode (AES-CBC), with 256 bit keys. AES is a standard in cryptography, used by the US government and other leading security agencies around the world to protect top-secret data. With proper implementation (Generated using a CSPRNG or derived using a KDF from your strong master password), and a strong encryption key, AES is considered unbreakable.

In order to enforce integrity and authentication with AES, Bitwarden also uses Hash-based Message Authentication Code (HMAC) with SHA-256. HMAC is an additional step Bitwarden takes to ensure that your encrypted data is from a trusted source and has not been tampered with in transit. This combined scheme is called AES256-CBC-HMAC-SHA256.

[Embedded content]## Public key cryptography

Public Key cryptography, also known as asymmetric cryptography, facilitates secure data sharing features in Bitwarden such as organizations and emergency access. Bitwarden uses the RSA cryptosystem with Optimal Asymmetric Encryption Padding (OAEP) scheme.

> [!NOTE] Bitwarden investigating post-quantim cryptography
> Bitwarden is currently investigating post-quantum cryptography options.

##
