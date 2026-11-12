# GaiaOS Beta 20 publication

## Launcher Beta 0.4.8-beta.20 — RELEASE-092 (12 November 2026)

Fresh Debian 13 amd64 launcher built from latest main source `80ef19645c01aa447bea474a5f7eee4ec801c41d`
(8bc766d plus exclusive release claim). Ships HOME-POLISH-091: actual Home-return
cue, breathing page/frame transitions, dithered Gaussian navigation glow with icon
accents and spring motion, shared animated Settings toggles, progressive header,
scroll-edge and dropdown blurs. Preserves Beta 19's backward-compatible license layout.

Actual feed baselines assessed: launcher Beta 19 source 587914f; system Beta 15
source 257cbe2. No os/ or native runtime dependency changes; new shaders are embedded
in the launcher. System 15 supplies required dependencies, Dolphin/HID/external-drive
support. Compatible A/B installations should install system 15 if needed, reboot,
then check for launcher 20. No new system bundle, ISO or migration. Old Beta 4
verifier recovery still needs corrected installation media/reinstall.

Validation: 160 Python tests (one optional real-RAUC skip), 35 QML syntax checks,
ShellCheck, fresh native build and seven CTest suites passed ( 72.94 sec). Focused
real-launcher quick-menu replay and native pointer slider passed. Real launcher
Light/Dark captures passed; packaged source files, metadata and signatures verified.
The full signed Beta 20 package installs using the unchanged system Beta 15 updater
in a temporary local installation, including signature/metadata/extraction and atomic
current switch. License bytes match source. Download transport and host compatibility
are controlled test boundaries; no real device boot is claimed.

PySide6 is absent in this retained builder, so check-settings-qml could not run here;
HOME-POLISH-091 records its prior separate pass. No new Sway/compositor run is claimed.
Broad held-list timing and previously recorded motion/installer harness limitations
remain separate; no assertion weakened. Motion feel, GPU/VM performance, physical
controllers/audio/gameplay/save-resume and boot/update/rollback acceptance pending Chris.
No old VM, disks or real power/audio services used.

Public files signed locally with the original identity. A temporary pinned signed-only
uploader transferred already signed public bytes; all four anonymous downloads and
both signatures independently verified before feed advancement. Temporary uploader
and transport removed. Eight distribution tests/channel validation and API/raw feed
read-back passed. Stable/system Beta 15 unchanged; previous downloads preserved.

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.20

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-launcher-0.4.8-beta.20-x86_64.tar.zst | 10371526 | `6173a702cff8ed260b5982efcca996a202cecf5d44368fa961817aa92181daa3` |
| gaia-launcher-0.4.8-beta.20-x86_64.tar.zst.sig | 64 | `a9d64cf4d6b038529de8757b62c789d143ecec38a72f8fc073e55b7972c12919` |
| SHA256SUMS | 222 | `992543cb8a436017b110e936d322e88f9d61b2b5a93f053483522b179b74f488` |
| SHA256SUMS.sig | 64 | `a51eabd17c67a78938137f7fd33191b678f3929378f57c9188cc4c78580956de` |
