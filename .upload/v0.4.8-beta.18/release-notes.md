GaiaOS 0.4.8-beta.18 — global live quick menu and Home transitions

The quick menu now works across Gaia pages and leaves software running by default. Game Preferences → Gaia Behavior offers optional pause with an in-memory retained frame. Home returns use a 320 ms crossfade and the supplied Home sound. Includes updated action icons, animated focus borders, status alignment and confirmations that close software before continuing launch, update, renderer or power actions.

Fresh Debian 13 amd64 build from latest main, source e2fed5da82fb5aa80ea512941345e8de7683a83c. Exact full source commit is embedded in gaia-update.json. Original signing identities preserved; signing remains local.

System assessment: system Beta 15 (257cbe2c2089627534e4d2ab378349455d47c92d) already supplies the required runtime packages, Dolphin, controller HID rules and external-drive support. No os/ changes since that baseline. The added Wayland client uses the existing Qt/SDL/Sway dependency. Compatible A/B systems should install system Beta 15 if needed, reboot, then check again for this launcher. Old Beta 4 verifier recovery requires corrected installation media/reinstall. No new system bundle, ISO or migration is needed for these launcher changes.

Python, QML, ShellCheck, native CTest and focused real-launcher quick-menu validation run before publication. Broad headless held-list timing remains a known intermittent limitation. VM/hardware boot/update/rollback, physical controllers, real audio, gameplay and save/resume acceptance remain pending Chris. Automated fixtures do not establish device acceptance.
