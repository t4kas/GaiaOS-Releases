# GaiaOS Beta 22 publication

## Launcher Beta 0.4.8-beta.22 — RELEASE-096 (12 November 2026)

Fresh Debian 13 amd64 launcher from latest main source `d2325195f8f8b96528efe1095d4664568cc8d4ed`
(6477d71 plus release claim). Ships NOTIFY-095: notification toasts, notification
center with quick-menu bell, Downloads/Uploads pages, main-button toast shortcut,
quiet update/version/emulator notifications and Beta-only Debugging controls.
No Gaia screen starts real transfers yet; engine/pages are ready. Two notification
icon stand-ins are documented. Chris's new publication request supersedes the
prior NOTIFY-095 source-only instruction, as recorded in the release claim.

Actual feed baselines: launcher Beta 21 source 0a3623c; system Beta 15 source
257cbe2. No os/ or native runtime dependency changes; transfers use Python standard
library and toast staging reuses Sway. System 15 supplies required dependencies.
Compatible A/B installs should install system 15 if needed, reboot, then check for
launcher 22. No new system bundle, ISO or migration. Old Beta 4 verifier recovery
still requires corrected installation media/reinstall.

Validation: 164 Python tests (one optional real-RAUC skip), 37 QML syntax checks,
ShellCheck, fresh native build and eight CTest suites passed ( 74.11 sec). Focused
real-launcher notification and quick-menu/pointer replays passed, with Light/Dark
captures. Package signatures/checksums, metadata and source bytes verified. Full
signed Beta 22 installs using the unchanged system Beta 15 updater in a temporary
installation: real signature/metadata/extraction and atomic current switch, with
controlled local download transport and host compatibility. License bytes match.
No new real Sway/device test claimed; NOTIFY-095 records separate author Sway/UI
validation. PySide6/Sway absent here. Broad headless held-list timing and prior
motion/installer harness limitations remain recorded; no assertion weakened.

Original signing identities preserved; signing stayed local. Temporary pinned
public-only upload removed after independent verification of all four anonymous
downloads and both signatures before Beta feed advancement. Eight distribution
tests, channel validation and API/raw feed read-back passed. Stable/system Beta
15 unchanged; previous downloads preserved.

Pending Chris: real emulator toast overlay, physical controller main-button
shortcut, actual feed notification, audio/gameplay/save-resume and VM/hardware
boot/update/rollback. No old VM, disks or real power/audio services used. Automated
process/audio/network fixtures do not establish real device acceptance.

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.22

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-launcher-0.4.8-beta.22-x86_64.tar.zst | 12225004 | `7b38de58980dbd34a7b8ff9021bd7cbd0f97bd93b88934227a18afc4e9ff153b` |
| gaia-launcher-0.4.8-beta.22-x86_64.tar.zst.sig | 64 | `5ca44dc38c48c32085555461a81382141973330617b7af71540b88c4de48d2cf` |
| SHA256SUMS | 222 | `c401dbc041c82a706963a867b135319bf124491740e2d32c4b0324b6f6e0417f` |
| SHA256SUMS.sig | 64 | `0ab7d55c7b6a6732fca52250d27673083c1d670f8e93b21dba9e0253ab7c5e48` |
