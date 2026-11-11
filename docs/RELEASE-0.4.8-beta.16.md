# GaiaOS Beta 16 publication

## Launcher Beta 0.4.8-beta.16 — RELEASE-085 (11 November 2026)

Published a fresh Debian 13 amd64 launcher build from latest main source
`047984c5343f177d6c202c9082b7dbce05b456f4` (1677616 plus exclusive release claim).
Includes QUICK-084: transparent quick-menu overlay above the paused game, themed
action icons, correct fullscreen focus restoration, and shared Gaia volume sliders
with queued final-target preservation. Earlier controller/emulator/Files features
are included. The prior QUICK-084 locally signed bundle was not reused; this is a
fresh build with exact current source metadata.

System scope assessed against the live published system Beta 15 source `257cbe2`:
no changes to os/ or runtime dependencies since that baseline. Beta 15 already
ships Dolphin/HID and external-drive requirements. This launcher release needs
no new system image. Compatible A/B installs below system 15 should install that
system update, reboot, then check again for launcher 16. Old Beta 4 verification
still needs corrected installation media/reinstall. No new ISO or layout migration.

Validation: 159 Python cases (one optional real-RAUC skip: tool absent), 32 QML
syntax checks, ShellCheck, fresh native build and all seven CTest suites (72.00 s)
passed. Focused real-launcher X11 quick-menu checks passed process pause/resume/
close, audio fixture updates and queued target preservation, scoped preferences,
confirmations, interrupted animation and native pointer drag persistence. Light/Dark
captures reviewed. Extracted package metadata and all staged source assets match
current source; packaged binary reports 0.4.8-beta.16. No new isolated Sway probe
was run in this builder (optional sway/grim/Pillow absent); QUICK-084's recorded
compositor checks remain separate. Broad headless held-list timing remains the
previously recorded intermittent QA limitation; no broad full-pass claim.

Existing Ed25519 and RAUC signing identities verified locally. Package and signed
checksums verified against retained public trust. Direct publisher created empty
draft 442077060 then upload returned HTTP 401. One temporary upload-only run
[43080222152](https://github.com/t4kas/GaiaOS-Releases/actions/runs/43080222152)
(7 seconds) transferred only pinned, locally signed public bytes, verified exact
source/version, every asset digest and both signatures, then published that exact
draft and checked anonymous downloads. No private keys or personal tokens went to
Actions. The initial manual dispatch preceded workflow registration and returned
404; dispatch after registration succeeded. Independent local anonymous downloads
of all four assets, signed checksums and both signatures then passed before Beta
feed advancement. Temporary workflow and transport removed. No ongoing Actions
publisher was installed. Stable and system Beta 15 are unchanged; old downloads
remain available.

Chris owns controller/audio/gameplay, boot/update/rollback and VM/hardware acceptance.
No old Debian test VM, physical disks or real power/audio services were operated.

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.16

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-launcher-0.4.8-beta.16-x86_64.tar.zst | 9073895 | `01256cabbd991fa98b172c5d9190ffd33574a8da083fe1d4bfd98659c625b8ca` |
| gaia-launcher-0.4.8-beta.16-x86_64.tar.zst.sig | 64 | `90021c858ce83618e658ed73cc169b13fd74e15d4f788509b7ed678a27f540e7` |
| SHA256SUMS | 222 | `7aa00fb25f8f36113ed1fe1918facb27123b03d852985aedae0dbb729529f4bd` |
| SHA256SUMS.sig | 64 | `aabdf04f182ec8c4520552a7208a226da52e1e0f5121e5451e255488271c3167` |
