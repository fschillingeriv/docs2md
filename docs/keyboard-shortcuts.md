---
URL: https://bitwarden.com/help/keyboard-shortcuts/
---

# Keyboard Shortcuts

Keyboard shortcuts can speed up common tasks in Bitwarden, like [autofilling logins](https://bitwarden.com/help/auto-fill-browser/) and saving new items. They help you navigate more efficiently and provide a vital alternative to using a mouse.

## Browser extension shortcuts

These shortcuts allow you to use the Bitwarden browser extension with your keyboard. If they don't work, you may need to [update your browser's shortcut settings](https://bitwarden.com/help/keyboard-shortcuts/#customize-browser-extension-shortcuts/).

### General

| To do this | Press |
|------|------|
| Activate the extension. | `Ctrl/Cmd` + `Shift` + `Y` |
| Generate a password and copy it to the clipboard. | `Ctrl/Cmd` + `Shift` + `9` |
| Lock the vault. | `Ctrl/Cmd` + `Shift` + `N` |

### Autofill

You can use a [keyboard shortcut to autofill credentials](https://bitwarden.com/help/auto-fill-browser/#keyboard-shortcuts/) into websites. The autofill shortcut works when username and password fields appear together on one page and separately in split login workflows.

| To do this | Press |
|------|------|
| Autofill the last used login for the current website. | `Ctrl/Cmd` + `Shift` + `L` Press again to cycle through multiple matches. |
| Autofill the last used card. | [Create a keyboard shortcut.](https://bitwarden.com/help/auto-fill-card-id/#using-keyboard-shortcuts/) |
| Autofill the last used identity. | [Create a keyboard shortcut.](https://bitwarden.com/help/auto-fill-card-id/#using-keyboard-shortcuts/) |

> [!TIP] Authenticator keyboard shortcut
> If the login uses the [Bitwarden authenticator](https://bitwarden.com/help/integrated-authenticator/) for TOTPs and you use the autofill shortcut, the TOTP is automatically copied to the clipboard after autofill. Press `Cmd/Ctrl` + `V` to paste the TOTP.

### Customize browser extension shortcuts

Some browsers, including Microsoft Edge and Safari, use default shortcuts that overlap with the Bitwarden shortcuts. To fix this, adjust your browser's default shortcuts to allow the Bitwarden ones to function as intended. The steps vary by browser:

- **Chromium-based browsers, including Chrome, Edge, Vivaldi, and Brave**: Go to the browser settings page, like `chrome://extensions/shortcuts` or `edge://extensions/shortcuts` to change the shortcuts that conflict or apply a new one.
- **Safari**: Update the [Mac keyboard shortcuts](https://support.apple.com/en-ca/guide/mac-help/mchlp2271/mac). You may need to reassign the shortcut for Show/Hide Sidebar so the [autofill shortcut](https://bitwarden.com/help/keyboard-shortcuts/#autofill/) works.
- **Firefox**: Update the [shortcut settings for extensions](https://support.mozilla.org/en-US/kb/manage-extension-shortcuts-firefox).

## Desktop app shortcuts

Use the following keyboard shortcuts to navigate the Bitwarden desktop app with your keyboard.

### General

| To do this | Press |
|------|------|
| Lock the vault. | `Ctrl/Cmd` + `L` |
| Open Bitwarden preferences. | `Ctrl/Cmd` + `,` |
| Reload the Bitwarden desktop app. | `Ctrl/Cmd` + `Shift` + `R` |
| Quit the Bitwarden desktop app. | `Ctrl/Cmd` + `Q` |
| Place the cursor in the vault's search box. | `Ctrl/Cmd` + `F` |
| Open the [Bitwarden generator](https://bitwarden.com/help/generator/). | `Ctrl/Cmd` + `G` |

### Edit items

| To do this | Press |
|------|------|
| Add a new login. | `Ctrl/Cmd` + `N` |
| Undo the last action when editing an item. | `Ctrl/Cmd` + `Z` |
| Redo the last action from editing an item. | `Ctrl/Cmd` + `Y` |
| Select all text in the active field or item. | `Ctrl/Cmd` + `A` |
| Cut the selected text and copy it. | `Ctrl/Cmd` + `X` |
| Copy the selected text. | `Ctrl/Cmd` + `C` |
| Paste the last copied text. | `Ctrl/Cmd` + `V` |
| Copy the open item's username. | `Ctrl/Cmd` + `U` |
| Copy the open item's password. | `Ctrl/Cmd` + `P` |
| Copy the open item's TOTP. | `Ctrl/Cmd` + `T` |

### Adjust display

| To do this | Press |
|------|------|
| Zoom in. | `Ctrl/Cmd` + `=` |
| Zoom out. | `Ctrl/Cmd` + `-` |
| Reset the zoom level. | `Ctrl/Cmd` + `0` |
| Enter full-screen mode. | Windows and Linux: `F11` Mac: `Fn` + `F` |
| Open developer mode. | Windows and Linux: `F12` |

### Control window

| To do this | Press |
|------|------|
| Minimize the Bitwarden desktop app. | `Ctrl/Cmd` + `M` |
| Hide Bitwarden desktop app in the tray. | `Ctrl/Cmd` + `Shift` + `M` |
| Always keep the Bitwarden desktop app on top. | `Ctrl/Cmd` + `Shift` + `T` Press again to undo the action. |
| Close the Bitwarden desktop app window. | `Ctrl/Cmd` + `W` |
