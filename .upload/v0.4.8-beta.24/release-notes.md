GaiaOS 0.4.8-beta.24 — quick-menu blackout fix and control polish

Fixes the quick-menu blackout reproduced in the author's Debian 13 Qt 6.8/Sway 1.10/RetroArch 1.20 environment by keeping the launcher window transparent. Light/Dark emulator replay passed there; real-device confirmation remains pending Chris. Removes the previous overlay verification workaround.

Also corrects on-state arrow direction, adds Files bulk placeholder checkboxes, extends Home glow coverage, restores a white volume knob with the supplied KnobAdjust sound and X mute, lets Settings content scroll under its header blur, and uses the Settings panel for Game Preferences.

Fresh Debian 13 amd64 launcher from latest main, BUGFIX-097 round 2 implementation 7d86881 plus the required shared-theme token correction for the white volume knob. Exact source/version embedded in gaia-update.json. Preserves notifications, prior fixes and backward-compatible package layout. Existing signing identities preserved; keys stay local. Archive extraction checked before signing and full signed installation verified with the unchanged system Beta 15 updater.

System Beta 15 (257cbe2) already supplies required runtime dependencies. No OS recipe or native dependency changes; no new system bundle, ISO or migration required. Compatible A/B installs should install system Beta 15 if needed, reboot and check Beta again. Old Beta 4 verifier recovery requires corrected installation media/reinstall.

Python, QML, ShellCheck, eight native CTest suites, focused notifications/quick-menu UI checks and signed-package installation run before publication. Real-device blackout/close behavior, physical controls/audio, game performance/save-resume and VM/hardware boot/update/rollback acceptance remain pending Chris. Automated fixtures and headless emulator tests do not establish real-device acceptance.
