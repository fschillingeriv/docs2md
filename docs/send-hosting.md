---
URL: https://bitwarden.com/help/send-hosting/
---

# Self-hosting Send

Once you [update your instance](https://bitwarden.com/help/updating-on-premise/), most implementations will be already setup to begin [using Send](https://bitwarden.com/help/create-send/). An exception to this is if you are using a non-default **mapped volume for attachment storage**.

The files attached to file Sends are stored in a `send` subdirectory of the existing attachments volume (for example, `./bwdata/core/attachments/send`). This is dictated by the `globalSettings__send__baseDirectory=` environment variable, which has the following default configuration in `global.override.env`:

```
globalSettings__send__baseDirectory=/etc/bitwarden/core/attachments/send
```

If you want to store the files attached to file Sends in your non-default attachments volume, you will need to point `globalSettings__send__baseDirectory=` to the new volume. For more information, see [Configure Environment Variables](https://bitwarden.com/help/environment-variables/).
