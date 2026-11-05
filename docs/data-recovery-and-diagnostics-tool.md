---
URL: https://bitwarden.com/help/data-recovery-and-diagnostics-tool/
---

# Data Recovery and Diagnostics Tool

The data recovery and diagnostics tool should be used in collaboration with Bitwarden Customer Support to:

- **Diagnose decryption issues**. The tool will first perform a full sync of data, and subsequently attempt to decrypt your private key, folders, and vault items.
- **Repair decryption issues**. Once decryption has been attempted by the tool, you'll be given the option to fix any decryption issues discovered during the diagnostic phase:

 - If your private key cannot be decrypted, the tool can replace your private key with a new one.
 - If your folders or vault items cannot be decrypted, the tool can delete the corrupted data.

When the tool is run, diagnostic logs are automatically created. You may, in collaboration with Bitwarden Customer Support, be asked to provide these diagnostic logs. Logs can be downloaded using the **Save Diagnostic Logs** button. They **do not contain** any key material, password data, or PII, but do contain information that can help Customer Support provide better service, including:

- Your globally-unique user identifier.
- Identifiers for any folders and vault items that could not be decrypted.
- An indicator of which encryption version your account is currently using.

Diagnostic logs are stored only in memory until you choose to save them to disk, if you navigate away from or refresh the page they are deleted from memory. They are not automatically sent or saved anywhere. Whether and where they're saved, as well as who can see them, is **fully under your control**. Bitwarden recommends deleting these logs safely once they are no longer needed.
