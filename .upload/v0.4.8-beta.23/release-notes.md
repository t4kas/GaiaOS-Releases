GaiaOS 0.4.8-beta.23 — launch, close and quick-menu fixes

Includes launch-loop sound and prismatic border clipping fixes, blue on-state arrows, software close-from-Home recovery and quick-menu overlay verification/repair with logs/quick-menu.log. The reported real-device blackout was not reproduced in the author's headless Sway/RetroArch replay; overlay verification is included, but real-device confirmation remains pending.

Fresh Debian 13 amd64 launcher from latest main, including BUGFIX-097 implementation dd5389a. Exact source/version embedded in gaia-update.json. Preserves notifications, prior launch/Home polish and backward-compatible package layout. Existing signing identities preserved; keys stay local. Archive extraction checked before signing and full signed installation verified with the unchanged system Beta 15 updater.

System Beta 15 (257cbe2) already supplies required runtime dependencies. No OS recipe or native dependency changes; no new system bundle, ISO or migration required. Compatible A/B installs should install system Beta 15 if needed, reboot and check Beta again. Old Beta 4 verifier recovery requires corrected installation media/reinstall.

Python, QML, ShellCheck, eight native CTest suites, focused notifications/quick-menu real-launcher checks and signed-package installation are checked before publication. Real-device quick-menu blackout/close behavior, physical controllers, audible output, gameplay/save-resume and VM/hardware boot/update/rollback acceptance remain pending Chris. Automated process/audio fixtures and the author's headless emulator tests do not establish real-device acceptance.
