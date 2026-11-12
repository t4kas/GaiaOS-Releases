# GaiaOS Beta 18 publication

## Launcher Beta 0.4.8-beta.18 — RELEASE-089 (12 November 2026)

Fresh Debian 13 amd64 build from latest main source
`e2fed5da82fb5aa80ea512941345e8de7683a83c` (170049e plus release claim).
Includes GLOBAL-088 implementation dfa747b: global live quick menu, inherited
optional pause with an in-memory retained frame, 320 ms Home crossfades and sound,
updated supplied icons, animated focus borders and close-and-continue actions.
The earlier GLOBAL-088 signed stage was not reused.

Actual published baselines assessed: launcher Beta 17 source 3e7b714; system Beta
15 source 257cbe2. No os/ changes since system 15. Wayland client runtime is already
provided by Qt/SDL/Sway dependencies; development headers/scanner are supplied by
existing libsdl2-dev. System 15 supplies Dolphin, HID rules and external-drive
packages. Compatible A/B installs should install system 15 if needed, reboot, then
check Beta for launcher 18. No new system bundle, ISO, migration or Stable change.
Old Beta 4 verifier recovery still requires corrected install media/reinstall.

Validation: 159 Python tests (one optional real-RAUC skip), 33 QML syntax checks,
ShellCheck, fresh native build and seven CTest suites passed (71.52 seconds).
Focused real-launcher X11 quick-menu replay passed global/live behavior, optional
pause, Files/Settings/Info Home crossfades and cue, icons, animated borders,
close-and-continue actions and slider; native pointer drag passed. Both Ed25519
signatures, signed checksums, package source/version and 167 packaged source files
verified. No new real Sway or hardware acceptance run is claimed. Broad headless
held-list timing remains the previously recorded intermittent QA limitation.

No GAIA_RELEASES_TOKEN was configured. The documented temporary signed-only
upload [43128905389](https://github.com/t4kas/GaiaOS-Releases/actions/runs/43128905389)
succeeded, verifying pinned asset hashes, package identity and public-key signatures.
Independent anonymous downloads of all four files matched local bytes and both
signatures verified before Beta feed advancement. Signing remained local; no private
keys or personal tokens went to Actions. Temporary workflow and public transport
removed. Stable and system Beta 15 remain unchanged; previous downloads retained.
Eight distribution tests and all channel validation passed.

Chris owns VM/hardware boot/update/rollback, physical controllers, real audio,
gameplay and save/resume acceptance. No old VM, disks or real power/audio services
were used; process/audio fixtures do not establish physical-device acceptance.

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.18

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-launcher-0.4.8-beta.18-x86_64.tar.zst | 10340618 | `52f0369360cc39b3ecbb81e24f1f1a64705406f3cdc630bfe4337e379393c0b0` |
| gaia-launcher-0.4.8-beta.18-x86_64.tar.zst.sig | 64 | `d72c6ce169fe4b388a9394f13b5ae1c13860847eba213da98a4f099df4cf8a19` |
| SHA256SUMS | 222 | `64f962b8d73b4c1cc62e49d2ce791a898cfc41bf6e00b23836c553e93dd52baf` |
| SHA256SUMS.sig | 64 | `f6b24a3a0821229915e8c87b234e831feee6eb73cc4e8827cc107aaba7208053` |
