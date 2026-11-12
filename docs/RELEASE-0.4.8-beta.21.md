# GaiaOS Beta 21 publication

## Launcher Beta 0.4.8-beta.21 — RELEASE-094 (12 November 2026)

Fresh Debian 13 amd64 launcher built from latest main source `0a3623cb420cbab4170e348cf8eb6821e69fb99b`
(679d442 plus exclusive release claim). Ships LAUNCH-093: Home remains visible
while software loads, animated cover pop/pulse and supplied SoftwareLaunch sound,
direct software reveal, soft panel-only quick-menu shade and 200 ms Guide hold with
improved tap detection. Preserves prior Home/toggle/blur polish and Beta 19 layout.

Actual feed baselines assessed: launcher Beta 20 source 80ef196; system Beta 15
source 257cbe2. No os/ or native runtime dependency changes; supplied sound and launcher changes add no system dependencies. System 15 supplies required dependencies, Dolphin/HID/external-drive
support. Compatible A/B installations should install system 15 if needed, reboot,
then check for launcher 21. No new system bundle, ISO or migration. Old Beta 4
verifier recovery still needs corrected installation media/reinstall.

Validation: 160 Python tests (one optional real-RAUC skip), 35 QML syntax checks,
ShellCheck, fresh native build and seven CTest suites passed ( 70.40 sec). Focused
real-launcher quick-menu replay and native pointer slider passed. Real launcher
Light/Dark quick-menu captures passed; packaged source files, metadata and signatures verified.
The full signed Beta 21 package installs using the unchanged system Beta 15 updater
in a temporary local installation, including signature/metadata/extraction and atomic
current switch. License bytes match source. Download transport and host compatibility
are controlled test boundaries; no real device boot is claimed.

PySide6/Sway are absent in this retained builder; no new Settings mock/compositor
run claimed. LAUNCH-093 records separate author validation including real isolated
Sway and UI checks. Broad held-list timing and previously recorded motion/installer
harness limitations remain separate; no assertion weakened. Real emulator launch,
motion feel, GPU/VM performance, physical controllers/audio/gameplay/save-resume
and boot/update/rollback acceptance pending Chris.
No old VM, disks or real power/audio services used.

Public files signed locally with the original identity. A temporary pinned signed-only
uploader transferred already signed public bytes; all four anonymous downloads and
both signatures independently verified before feed advancement. Temporary uploader
and transport removed. Eight distribution tests/channel validation and API/raw feed
read-back passed. Stable/system Beta 15 unchanged; previous downloads preserved.

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.21

Upload transport note: run 43258350701 uploaded and published the release, then
failed its runner-side anonymous download retry window (30 seconds). Independent
local anonymous downloads of all four files and both signatures succeeded before
the feed was advanced; API/raw feed and uploader removal verified afterward. The
runner download failure does not indicate an asset/hash or installed-updater failure.

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-launcher-0.4.8-beta.21-x86_64.tar.zst | 11628113 | `1f4c1eaea2cd94e966dda687a9ca6d6c4a2995f2699c524c5c322505b933a1c7` |
| gaia-launcher-0.4.8-beta.21-x86_64.tar.zst.sig | 64 | `4106b05b1110c9afa7deb41a0d4c15f43671195af1fce124086b6a0060219399` |
| SHA256SUMS | 222 | `d17443f5dd175471564eabdd4278e762d6241fbc1f14b4b2661f50156629660a` |
| SHA256SUMS.sig | 64 | `48d6593789d14e845e235e0baa21bdb6c1f3b2798bd0ce0778d2b209aefbfcdc` |
