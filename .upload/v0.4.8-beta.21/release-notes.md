GaiaOS 0.4.8-beta.21 — direct software launch and transparent quick menu

Home stays visible while software loads, with an animated cover pop/pulse and the supplied launch sound. Software reveals directly with a short fade when ready. The quick menu leaves software visible with a soft shade behind its panel. Guide hold is 200 ms, with improved tap detection. Includes prior Home, toggle and blur polish and the backward-compatible package layout.

Fresh Debian 13 amd64 launcher from latest main, including LAUNCH-093 implementation 679d442. Exact source/version embedded in gaia-update.json. Packages are checked with the device extractor before signing; signed installation is verified with the unchanged system Beta 15 updater. Existing signing identities preserved; keys stay local.

System Beta 15 (257cbe2) already supplies required runtime dependencies. No OS recipe or native dependency changes; no new system bundle, ISO or migration required. Compatible A/B installations should install system Beta 15 if needed, reboot and check Beta again. Old Beta 4 verifier recovery requires corrected installation media/reinstall.

Python, QML, ShellCheck, native CTest, focused real-launcher quick-menu and signed-package installation checks run before publication. Broad headless held-list timing remains a known intermittent limitation; motion/installer harness limitations are recorded separately. Physical controllers, audible output, actual game launch/performance/save-resume and VM/hardware boot/update/rollback acceptance remain pending Chris. Automated process/audio fixtures do not establish hardware or gameplay acceptance.
