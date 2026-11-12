GaiaOS 0.4.8-beta.20 — Home, navigation, toggles and blur polish

Home return now uses a breathing scale/fade transition and only plays its cue on a real return to Home. Navigation glow uses a dithered Gaussian shader with spring motion and icon accents. Settings switches share animated toggles with retained transitions. Dropdown, scrolling edges and Settings headers have updated progressive blurs.

Fresh Debian 13 amd64 launcher from latest main, including HOME-POLISH-091 implementation 8bc766d. Exact source/version embedded in gaia-update.json. Includes the Beta 19 package-layout repair; the archive is checked with the installed updater before signing, and signed installation is verified using the unchanged system Beta 15 updater. Existing signing identities preserved; private keys stay local.

System assessment: system Beta 15 (257cbe2) already supplies required runtime dependencies. No OS recipe or native dependency changes; shaders are embedded in the launcher. No new system bundle, ISO or migration required. Compatible A/B installations should install system Beta 15 if needed, reboot and check Beta again. Old Beta 4 verifier recovery still requires corrected installation media/reinstall.

Python, QML, ShellCheck, native CTest, focused quick-menu UI and signed-package installation checks run before publication. Broad headless held-list timing remains a known intermittent limitation; prior motion/installer harness failures are recorded separately in project status. Physical controller/audio/gameplay/save-resume, motion feel/GPU performance and VM/hardware boot/update/rollback acceptance remain pending Chris. Automated fixtures do not establish physical device acceptance.
