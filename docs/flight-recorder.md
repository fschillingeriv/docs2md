---
URL: https://bitwarden.com/help/flight-recorder/
---

# Troubleshoot Mobile with Bitwarden Support

On Bitwarden mobile apps, including Password Manager and Authenticator, you can activate **Flight Recorder** to capture additional log activity for troubleshooting unexpected behaviors. This can be particularly useful when you're working with Bitwarden Support.

Flight Recorder is a lightweight, temporary event logger that captures recent app activity like user interactions and key system events. You're in control of this information, it is only ever stored on your device and can be exported to share with the Bitwarden Support team if you wish. Flight Recorder **does not** log sensitive information like your master password or vault data.

## Using Flight Recorder

> [!TIP] When to use Flight Recorder
> You may be asked to activate Flight Recorder when working with Bitwarden Support if you're experiencing an issue that's difficult to reproduce or if you've encountered a crash or unexpected behavior.

Flight Recorder is deactivated by default. To activate Flight Recorder:

1. In the Bitwarden mobile app, tap **Settings**→ **About**.
2. Scroll down and tap **Flight Recorder**.
3. Go through the tasks or workflow that caused the issue you want to report to Support.

> [!NOTE] Flight Recorder limited time
> Flight Recorder only stores a short window of recent activity, so Bitwarden recommends trying to reproduce the issue you're experiencing immediately after activating Flight Recorder.

Once Flight Recorder has captured the issue you're experiencing:

1. Deactivate logging by toggling **Flight Recorder** off from the same menu.
2. Tap **Settings**→ **About** → **View recorded logs** to download your log file. Each log will be available to you until you delete it or until it expires 30 days after creation.
3. Include your log file in future communications with Bitwarden Support on the topic of your unexpected app behavior, issue, or potential bug.

## Data captured by Flight Recorder

Bitwarden prioritizes your security. Flight Recorder is designed such that:

- Logs are only stored on your device and never transmitted automatically.
- Logs can only be started, stopped, or shared by you.
- Logs do not include sensitive user data like master passwords or vault data.

The following data may be captured while Flight Recorder is active:

| Category | Data |
|------|------|
| User events | Screen navigations and navigation timestamps, key button taps and user interactions, transitions into and out of modals, sheets or overlaps. |
| App & build information | Bitwarden app version, built type, device platform, device model, OS version |
| Crash & exception reporting | Exception messages, exception types, exception-specific metadata, stack traces |
| Flight Recorder metadata | Start time of logging session, logging session duration, log file size |
