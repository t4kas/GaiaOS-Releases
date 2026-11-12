GaiaOS 0.4.8-beta.19 — fix Unsupported package layout during update

Fixes the Beta 18 installation failure: the Wayland protocol license now ships under config/licenses, a directory accepted by existing installed updaters. No manual updater replacement is needed. Check Beta again and install Beta 19 instead of Beta 18.

Includes Beta 18's global live quick menu, optional pause with retained frame, Home crossfades/sound and action confirmations. A new packaging gate extracts the real archive using the device updater before signing. Regression covers the installed CMake license destination, signed installation and rollback, and rejects unsupported layouts before signing.

Fresh Debian 13 amd64 launcher from the source commit embedded in gaia-update.json. Existing Ed25519 trust identity preserved. System Beta 15 already supplies runtime dependencies; no OS runtime/recipe changes, new system bundle, ISO or migration are required. Compatible A/B installations need system Beta 15. Old Beta 4 verifier recovery still requires corrected installation media/reinstall.

Python, QML, ShellCheck, native CTest and actual signed-package installation with the unchanged system Beta 15 updater are checked before publication. Broad headless held-list timing remains a known intermittent limitation. Physical controllers, audio, gameplay/save-resume and VM/hardware boot/update/rollback acceptance remain pending Chris. Installer tests use a temporary local installation and local download transport; no real device or VM is operated.
