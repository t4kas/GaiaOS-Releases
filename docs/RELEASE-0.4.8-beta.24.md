# GaiaOS Beta 24 publication

## Launcher Beta 0.4.8-beta.24 — RELEASE-099 (13 November 2026)

Fresh Debian 13 amd64 launcher from latest main source `ee461e0165c1db61765e45f3a2178c82505f99bc`
(7d86881 plus release claim and required slider palette-token correction). Ships BUGFIX-097 round 2: always-transparent launcher
window fixes the quick-menu blackout reproduced by the author on Debian 13 Qt6.8/
Sway1.10/RetroArch1.20; Light/Dark replay passed there. Removes round 1 overlay
verification workaround. Also includes corrected on-state arrows, Files bulk
checkboxes, glow overscan, white volume knob with supplied KnobAdjust sound and X
mute, Settings content scrolling under header blur and shared Game Preferences panel.
Real-device confirmation remains pending Chris. The initial release check caught
a hardcoded white slider color; it now uses the identical existing Theme.thumb
value, and the theme test/full release checks passed after the correction.

Actual feed baselines: launcher Beta 23 source 98bb58f; system Beta 15 source
257cbe2. No os/ or native runtime dependency changes; launcher repairs reuse existing Sway/process facilities. System 15 supplies required dependencies.
Compatible A/B installs should install system 15 if needed, reboot, then check for
launcher 24. No new system bundle, ISO or migration. Old Beta 4 verifier recovery
still requires corrected installation media/reinstall.

Validation: 164 Python tests (one optional real-RAUC skip), 38 QML syntax checks,
ShellCheck, fresh native build and eight CTest suites passed ( 79.97 sec). Focused
real-launcher notification and quick-menu/pointer replays passed, with Light/Dark
captures. Package signatures/checksums, metadata and source bytes verified. Full
signed Beta 24 installs using the unchanged system Beta 15 updater in a temporary
installation: real signature/metadata/extraction and atomic current switch, with
controlled local download transport and host compatibility. License bytes match.
No new real Sway/device test claimed; BUGFIX-097 records separate author Sway/emulator
validation. PySide6/Sway absent here. Broad headless held-list timing and prior
motion/installer harness limitations remain recorded; no assertion weakened.

Original signing identities preserved; signing stayed local. Temporary pinned
public-only upload removed after independent verification of all four anonymous
downloads and both signatures before Beta feed advancement. Eight distribution
tests, channel validation and API/raw feed read-back passed. Stable/system Beta
15 unchanged; previous downloads preserved.

Pending Chris: device blackout/close verification, physical controller shortcuts,
real update notifications, audio/gameplay/save-resume and VM/hardware
boot/update/rollback. No old VM, disks or real power/audio services used. Automated
process/audio/network fixtures do not establish real device acceptance.

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.24

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-launcher-0.4.8-beta.24-x86_64.tar.zst | 12213081 | `fb0159350ad93cd193dc84277491790b3ac40c507a35c80d76a7bbc590a6e140` |
| gaia-launcher-0.4.8-beta.24-x86_64.tar.zst.sig | 64 | `de3a287a8734d88e6cb5733745d07762d87e43a4a189a72051b1a73e7f5a5625` |
| SHA256SUMS | 222 | `033984953d2cf7b5105a2cb9a1c3d104d2b8d2e36ddffa1618343a50c8e96252` |
| SHA256SUMS.sig | 64 | `32c813a3c4142166a912935a122db028db6c5fa3364a3088c2cc792eff163659` |
