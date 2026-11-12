# GaiaOS Beta 23 publication

## Launcher Beta 0.4.8-beta.23 — RELEASE-098 (13 November 2026)

Fresh Debian 13 amd64 launcher from latest main source `98bb58fc5e074beed699224ac359f0935f158e7a`
(dd5389a plus release claim). Ships BUGFIX-097: launch-loop sound correction,
clipped prismatic border handling, blue on-state arrows, software close-from-Home
recovery and bounded quick-menu overlay verification/repair with mismatch logging.
The reported device blackout was not reproduced by the author's headless fixture
and real RetroArch replay; real-device confirmation remains pending Chris.

Actual feed baselines: launcher Beta 22 source d232519; system Beta 15 source
257cbe2. No os/ or native runtime dependency changes; launcher repairs reuse existing Sway/process facilities. System 15 supplies required dependencies.
Compatible A/B installs should install system 15 if needed, reboot, then check for
launcher 23. No new system bundle, ISO or migration. Old Beta 4 verifier recovery
still requires corrected installation media/reinstall.

Validation: 164 Python tests (one optional real-RAUC skip), 38 QML syntax checks,
ShellCheck, fresh native build and eight CTest suites passed ( 77.81 sec). Focused
real-launcher notification and quick-menu/pointer replays passed, with Light/Dark
captures. Package signatures/checksums, metadata and source bytes verified. Full
signed Beta 23 installs using the unchanged system Beta 15 updater in a temporary
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

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.23

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-launcher-0.4.8-beta.23-x86_64.tar.zst | 12235185 | `c4f23ba5f08ea035ee6fce3e37fbb112732864f738387add0c76a91f452559a6` |
| gaia-launcher-0.4.8-beta.23-x86_64.tar.zst.sig | 64 | `de52efdab3acf11603f90365df744c1f76b2e737b5593626b1d0cb9d7dbfc818` |
| SHA256SUMS | 222 | `f9ec89acbed04a54faf3f65a523d143d2706f160f09c0030a0f66d7ca74f3f3e` |
| SHA256SUMS.sig | 64 | `1cbcf4276643ef0d9fbde297ed691fb8c6e86325de1f73c4c86bc27354130f65` |
