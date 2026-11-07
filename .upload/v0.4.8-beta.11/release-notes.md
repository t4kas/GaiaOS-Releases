GaiaOS 0.4.8-beta.11

Source: 640356703963dbbb0277944a9e066b9086f85f79

Launcher/application Beta based on latest main, including UX-MEDIA-075.

- Files: external-drive discovery and read-only mount requests, refresh, and import to Gaia with conflict protection.
- Artwork: covers, screenshots, title screens and logo style selection, with immediate cache refresh and local-image priority.
- UI: eased Settings scrolling, focus bounce refinements and animated popup entry/exit.
- Software Update: two-second checking window and clearer up-to-date result.

Existing systems need UDisks and filesystem support packages for unmounted-drive access; launcher updates cannot install OS packages. Already mounted drives remain usable. No ISO or system bundle is included. Stable and system feeds remain unchanged.

Debian 13 amd64 native build; Python, QML syntax, ShellCheck and seven CTest suites passed. Native Files/artwork/full X11 UI replay passed with isolated fixtures. Original trusted Ed25519 key used locally; private keys never uploaded.

VM/device, actual external-drive/exFAT, controller and performance acceptance: pending Chris.
