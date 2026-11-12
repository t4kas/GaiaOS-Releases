# Release distribution status

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


## Launcher Beta 0.4.8-beta.19 — UPDATE-LAYOUT-090 (12 November 2026)

Corrects Beta 18's reported Unsupported package layout install failure. Reproduced
using the unchanged system Beta 15 extractor: payload/licenses was outside its
accepted directory list. The Wayland protocol XML and MIT notice now install under
config/licenses/wlr-protocols. No updater bootstrap or manual device change is needed.
Check Beta again to replace the offered version with Beta 19.

Fresh Debian 13 amd64 source `587914f`; preserves GLOBAL-088 features from Beta 18.
The packager now extracts its real archive with the device extractor before signing.
Regression includes the actual CMake license destination through signed install and
rollback, and rejects unsupported stages before compression/signing. Existing layout
and link/traversal restrictions remain unchanged.

Validation: 160 Python tests (one optional real-RAUC skip), 33 QML syntax checks,
ShellCheck, native build and all seven CTest suites passed. The actual full signed
Beta 18 package reproduces the error without changing the temporary current install;
the actual signed Beta 19 package verifies, extracts, checks metadata and atomically
installs with the unchanged system Beta 15 updater. Its license bytes match source.
Local transport and host compatibility are controlled boundaries; installation logic,
archives, signatures, metadata and filesystem switch are real. No VM/device boot is
claimed. Existing focused global-menu UI replay passed for the unchanged UI in
RELEASE-089. Broad held-list timing remains the known intermittent limitation.

Published system Beta 15 source 257cbe2 already supplies required dependencies;
no os/ or runtime changes are introduced. No new system bundle/ISO or migration.
Old Beta 4 verifier recovery still needs corrected installation media/reinstall.
Stable and system feeds unchanged. Beta 18 files remain available for audit, but the
Beta feed now offers corrected Beta 19. Original signing identities preserved.

Locally signed public bytes transferred through a temporary pinned upload-only
workflow, removed after verification. All four anonymous downloads, both Ed25519
signatures and signed checksums independently verified before feed advancement.
No private keys or personal tokens sent to Actions. Eight distribution tests and
channel validation passed; API/raw feed read-back verified.

Chris owns physical-controller/audio/gameplay/save-resume and VM/hardware
boot/update/rollback acceptance. No old VM or physical disks were used.

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.19

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-launcher-0.4.8-beta.19-x86_64.tar.zst | 10344979 | `508fb9acba171acb6c032b43ec708141c0d60d6f8a11de8c2df4efaabfe1e6ee` |
| gaia-launcher-0.4.8-beta.19-x86_64.tar.zst.sig | 64 | `e33fc05e5ac986d762ef9f4ad4290b4b3279c8aeb318c09dc9c54e7f4fe29589` |
| SHA256SUMS | 222 | `5ecb7b6938e90cdedd3cfdf0f2a5b8e5769d4b875d448e0b9109804507b57a04` |
| SHA256SUMS.sig | 64 | `18b61782afd99ea98bac9cdc33a1e60f8246790ccbbed5b8556eb00516450379` |


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


## Launcher Beta 0.4.8-beta.17 — RELEASE-087 (11 November 2026)

Fresh Debian 13 amd64 launcher built from latest main source
`3e7b714006e36e9620f384e28978f5d5f2ee35f0` (dac75e4 plus exclusive release claim).
Includes HOME-086 implementation 3cd6842: 500 ms Guide/PS/Xbox/Home hold for the
quick menu, short-tap Home with the process paused, profile-avatar Playing tile
and same-process resume, narrower quick menu with inline volume/status/Power,
faster animated navigation glow, bottom-button bounce and three supplied random
click sounds. The prior HOME-086 locally signed bundle was not reused.

Assessed the actual published system Beta 15 baseline `257cbe2`: no os/ or native
runtime dependency changes since that baseline. System 15 already provides
Dolphin, controller HID rules and external-drive packages. Compatible A/B installs
should install system 15 if needed, reboot, then check again for launcher 17.
No new system bundle/ISO, disk-layout migration or Stable change. Old Beta 4
certificate-purpose verification still needs corrected installation media/reinstall.

Validation: 159 Python tests (one optional real-RAUC skip), 33 QML syntax checks,
ShellCheck, fresh native build and all seven CTest suites passed (71.31 seconds).
Focused real-launcher X11 quick-menu replay passed tap Home/Playing resume,
software glow entry/exit, bouncing random navigation click without duplicate cues,
actual process pause/resume/close, scoped Gaia preferences and confirmations.
Native pointer drag commits the final volume-slider position. Light/Dark captures
were reviewed. Extracted metadata, actual binary version and every packaged QML,
sound, helper and font match the exact source. Existing Ed25519 and RAUC identities
verified; both Ed25519 signatures and signed checksums verified locally.
Optional Sway/grim/Pillow are absent in this builder, so no new isolated Sway run
is claimed; HOME-086's earlier compositor validation is separate. Broad headless
held-list timing remains the previously recorded intermittent QA limitation.

Direct upload to draft 442137825 returned HTTP 401. The documented temporary
signed-only upload run [43090279526](https://github.com/t4kas/GaiaOS-Releases/actions/runs/43090279526)
transferred pinned local public bytes and verified exact source/version, asset
hashes and public-key signatures before publication. No private keys or personal
tokens went to Actions. Independent local anonymous downloads of all four assets,
both signatures and signed checksums passed before Beta feed advancement.
Temporary workflow and transport removed; no ongoing Actions publisher installed.
Stable and system Beta 15 remain unchanged, and previous downloads are retained.

Chris owns physical-controller/audio/gameplay/save-resume and VM/hardware
boot/update/rollback acceptance. No old test VM, disks or real power/audio
services were used. Fixtures establish application behavior, not device acceptance.

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.17

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-launcher-0.4.8-beta.17-x86_64.tar.zst | 9450480 | `4185a9d11da70fbf7a95947935448f727d3d546ed746888b944c4797f9276c9c` |
| gaia-launcher-0.4.8-beta.17-x86_64.tar.zst.sig | 64 | `8dbe9e52ca17772c8d5bb3b674a31e1620fc2d65f9e878c221c28df7c8f06955` |
| SHA256SUMS | 222 | `90a28d9a79f707a2aaca4c41d7f2a9890ec85c3f17d5a737997bc8b52f954999` |
| SHA256SUMS.sig | 64 | `420154734d7902610cb30702bafb0418aab30e6847cd18809febc773b0751295` |

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


## System Beta 0.4.8-beta.15 — RELEASE-083 (11 November 2026)

Published signed system Beta 15 with matching launcher from source `257cbe2c2089627534e4d2ab378349455d47c92d`.
Fresh Debian 13 amd64 packages/root and the current tracked overlay/image hook;
no retained root image or VM was used. Runtime build inputs staged before the
QA-only commit are byte-identical at this source. The full-system bundle delivers
QUICK-082 and EMULATOR-081 together: Guide quick menu, process pause/resume/close,
live output controls, controller status/test, scoped emulator editors, launch/window
recovery, Dolphin 2503 and active-seat Sony/Microsoft/Nintendo HID rules. Retains
Beta 14 session/service permission fixes and external-drive packages.

Channel validation and all eight distribution tests passed. Installed recipe checked in full. Key packages: Dolphin 2503+dfsg-1+deb13u1,
kernel 6.12.116-1, Qt 6.8.2, RAUC 1.13-3+deb13u1, udisks2 2.10.1-12.1+deb13u2,
exfatprogs 1.2.9-1+deb13u1 and ntfs-3g 1:2022.10.3-5+deb13u3.
Rootfs SHA-256 `d24bcad225740170840c99e0c70934a8b83abdf9bcff9c6a566a535551da14c1`.

Passed: 159 Python cases including real RAUC/ext4, 31 QML syntax checks,
ShellCheck, seven native CTest suites on the Debian builder (74.12 s) and again
inside the fresh root (72.46 s), focused quick-menu and emulator-editor UI replays,
reviewed Light/Dark captures, real non-root console rendering from the prepared
root, package/overlay checks, controller udev verification, service-user config
readability and read-only ext4 check. The quick-menu keyboard replay starts at
Resume explicitly because a stationary virtual pointer can hover a new popup row;
production behavior and assertions remain unchanged. Broad X11 replay passed
controller/blur, dropdown/modal, Home/boundary and picker checks but failed the
previously recorded held-navigation timing check (a 36 ms observed interval).
Broad replay is not recorded as fully passed; no timing assertion was weakened.

Original Ed25519 and RAUC identities verified, inner codesign/verity identity and
rootfs digest verified, both Ed25519 signatures and signed asset checksums passed.
Direct disposable draft 441971694 accepted, tiny upload failed HTTP 401; only that
probe draft was removed. One-time signed-only upload run 43068447542 reconstructed
pinned locally signed bytes from a hash-pinned public base/delta, verified exact
assets, signatures and RAUC identity, published and verified public downloads.
Independent local anonymous downloads matched all four assets and both signatures
before advancing system Beta. Private keys stayed local. Temporary transport and
workflow removed with feed advancement; no ongoing Actions publisher installed.

This is for compatible provisioned A/B installs and includes launcher Beta 15.
Launcher feed remains Beta 12; Stable unchanged. No new ISO, disk erase, layout
migration, old Debian test VM or physical disk use. Old Beta 4 certificate-purpose
verification still requires corrected installation media/reinstall. Chris owns
VM/device boot/update/rollback, real controllers/USB/exFAT/audio, commercial-game
and performance acceptance; none is claimed passed here.

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.15

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-system-0.4.8-beta.15-x86_64.raucb | 1240552685 | `59dc4e514242a364dbd71a53ebb0b5fa87ac6fbe7fe24a56639ae98e8ff336c8` |
| gaia-system-0.4.8-beta.15-x86_64.raucb.sig | 64 | `163bd66a4beb0dea12f3d476cdd31a92a863fed92973836da0f27143d6fb80fa` |
| SHA256SUMS | 214 | `3f7ab75f8147ca451346ee1a2e413437828ed807cf2131ef21ec038027d03e82` |
| SHA256SUMS.sig | 64 | `87ab7d3c8b863fcbcab2e7d43999e883bd6184b708106d3a6d1d88126dacca6e` |


## Corrected system Beta 0.4.8-beta.14 — UPDATE-BOOT-080 (9 November 2026)

Signed system Beta 14 replaces withdrawn Beta 13. Exact system source:
`08cd11b57edbbe48a5814c48ab10c21d7ee31d55`.
Chris's recording showed launcher Beta 11 / system Beta 8 offering system Beta 13,
then a reboot ending at console-kiosk.sh:14, XDG_RUNTIME_DIR unset. Chris reports
one clean Ctrl+Alt+Delete restart restored Gaia; its version after recovery was
not independently measured. No claim that the corrected VM boot has passed.

Root cause reproduced in an isolated systemd container: Beta 13's /usr/share
was mode 0700, inherited from a restored checkout directory by copytree/rsync.
The messagebus service account could not open /usr/share/dbus-1/system.conf;
D-Bus failed, leaving the user runtime unavailable. Polkit parents had similarly
restricted directory modes. Earlier root rendering/native checks missed this
service-account access failure. Recording load does not explain these permissions.

Fixes: image staging normalizes public paths independently of checkout modes;
service/polkit parents are readable/traversable; the signing tool checks the actual
ext4 service paths and rejects the Beta 13 permissions before signing. A real ext4
corruption regression proves the gate. The kiosk validates its runtime ownership,
mode and user-bus socket, using the canonical systemd runtime if PAM omits the
variable. Greetd waits for logind and the console user's manager. The failed-boot
watchdog requests reboot even when RAUC mark-bad fails. Per-boot /run build state
is excluded. No operator key rotation or new update protocol.

Validation: 159 Python tests with real RAUC/ext4 cases, 30 QML syntax checks and
ShellCheck passed. Seven native CTest suites passed in 56.34s; current launcher
was rebuilt as Beta 14. Actual image rendering succeeded as non-root console.
Actual messagebus/polkit UIDs could read their configs. Service dependency
verification passed. An isolated systemd container then started the real system
bus, logind, user@1000 and user D-Bus; under production ordering a console-user
probe with XDG_RUNTIME_DIR deliberately unset passed. A probe replaced the
compositor: this is not BIOS/UEFI, Parallels or full Sway/DRM acceptance. Ext4 check
passed; filesystem UUID regenerated and /run is empty in the image.

System base is the retained verified Debian 13 Beta 13 root, updated offline with
exact source changes and the rebuilt launcher; no fresh Debian package install
or new ISO is claimed. All external-drive packages/kernel/firmware from that base
remain. Rootfs SHA-256:
`c89af4dfbfa61becb92f5db25a9b5b8bc9ca37f9883f015f3d4a499f173c5093`.
The signed RAUC manifest matches this checksum, source and version. Existing CMS
and Ed25519 signatures, signed checksums and all four anonymous public assets
were verified independently before advancing system-beta.

Direct upload probe HTTP 401 left empty reviewed draft 438620381. One temporary
upload-only job (run 42539813681) reconstructed the exact signed bundle from a
pinned 11,297,041-byte transfer delta plus the pinned public Beta 13 bytes, then
verified digest, Ed25519 signatures, RAUC identity/certificate/root checksum before
upload and anonymous verification. No base code was executed. Users download the
complete 1,263,052,014-byte RAUC asset; this is only transfer compression. No private
keys or personal tokens went to Actions. Temporary workflow/transport removed.
Beta 13 remains marked withdrawn with assets available for audit. Launcher Beta 12
and Stable unchanged; eight distribution cases and real updater selection passed.

Compatible provisioned A/B installs can update through Software Update. Old Beta 4
certificate-purpose verification still needs a corrected image/reinstall. No disk
erase/layout migration/new ISO. Chris owns corrected-update boot, USB/exFAT,
update/reboot/rollback, GPU/controller/performance and hardware/VM acceptance.

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.14

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-system-0.4.8-beta.14-x86_64.raucb | 1263052014 | `9558cc7c67f8de1c9ef4383b26f35ad4f6bec53525596b22cd11bf2984bd81e7` |
| gaia-system-0.4.8-beta.14-x86_64.raucb.sig | 64 | `be36a0b485545cd1df4fd4c30f113ba734dc798890e97ba71ce3c2f44190a905` |
| SHA256SUMS | 214 | `08f746800f73ef884bcc2193661b950b5720671d02f81c9464c6c0014d51679d` |
| SHA256SUMS.sig | 64 | `d6957d045801ba75086fae2941ca151638e93d73926db1750864381eb12e458a` |


## System Beta 13 withdrawn — UPDATE-BOOT-080 (9 November 2026)

Chris's recording shows a Beta 8 system upgrading, rebooting, then console-kiosk.sh
exiting at line 14 because XDG_RUNTIME_DIR is unset. This is a post-update session
startup failure; the recording does not establish screen-recording load as its cause.
System Beta is temporarily empty to stop further offers while Codex investigates
and prepares a corrected system update. Signed .13 assets/tag retained for audit.
Launcher/Stable feeds unchanged. Recovery/boot acceptance pending Chris.


## System Beta 0.4.8-beta.13 published — SYSTEM-BETA-079 (9 November 2026)

First signed system Beta published from exact source
`67f1de12024ca9e0b26047ddd816a519a4f6b3fd`. Chris reassigned the previously
stopped system work to Codex and authorized completing the required OS update.
Fresh Debian 13 amd64 root prepared with debootstrap, the actual 69-package image
recipe, repository overlay and standard 0900 image hook. No retained WSL artifact
was reused or modified. Launcher built as Beta 13 is included in the system image;
launcher Beta stays at 12 because its features are already included here.

External-drive dependencies are installed: udisks2 2.10.1-12.1+deb13u2,
exfatprogs 1.2.9-1+deb13u1 and ntfs-3g 1:2022.10.3-5+deb13u3, plus the
UDisks policy. Kernel metapackage 6.12.116-1, current firmware/graphics startup
and RAUC 1.13-3+deb13u1/codesign configuration are included.

Checks passed: 151 Python cases (including real RAUC certificate-purpose checks),
30 QML syntax checks, ShellCheck, seven CTest suites on the Debian builder (57.27s)
and again in the fresh root (56.55s). Native Files/artwork checks, full X11 UI replay
on the installed binary and an actual render using the root's runtime libraries
passed. An initial held-select replay failed during concurrent image assembly;
the complete replay passed afterward without product changes. Ext4 read-only
filesystem check passed. Image extraction confirmed all 138 installed launcher
files, all 69 recipe packages, UDisks policy and exact trust/config/source/version.
No operator private keys, host SSH keys or runtime test data entered the root.
The sole complete PEM-block scan match was GnuTLS's embedded public self-test
constant, verified against the unchanged Debian package checksum.

The rootfs-only builder produced the regular 8 GiB slot image; no boot disk/ISO
or physical-disk operation was performed. Rootfs SHA-256:
`7ee58448d7e2430baed8c6b36ede47497523c11913e99d4daf0d8ceb5b571c88`.
RAUC's signed manifest matches this exact image checksum/source/version. Existing
RAUC CMS and Ed25519 signatures were independently verified with retained public
trust, as were signed SHA256SUMS. Packaging fix 67f1de1 preserves sparse files
rather than expanding the staging copy; its real sparse-copy regression passed.

A small direct upload probe returned HTTP 401, leaving reviewed empty draft
438588677. A one-time upload-only fallback (run 42534594029) reconstructed 38
pinned chunks, verified their complete digest, both outer signatures and real RAUC
identity/certificate/image checksum, uploaded and verified public assets. No private
key or personal token went to Actions. Local independent anonymous verification
matched all four assets before advancing system-beta. Temporary uploader and
transport files removed; old releases and launcher/Stable feeds retained.
Distribution validation now also checks existing system feeds and rejects mixed
components, non-RAUC system assets and protocol-1 system metadata; eight tests pass.

Compatibility: provisioned A/B installs must already have corrected codesign
certificate-purpose verification. Old Beta 4 root images require a corrected
installation image/reinstall; this bundle cannot repair a verifier that rejects it.
No new installer ISO or layout migration is included. Chris owns real USB/exFAT,
BIOS/UEFI boot, install/reboot/rollback, GPU/controller/performance and VM/device
acceptance. None is claimed as passed. The old Debian VM was not used.

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.13

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-system-0.4.8-beta.13-x86_64.raucb | 1262339309 | `b96729b43f46920196c130993b602f3dca032dd7191e08ef468463ac365dac8a` |
| gaia-system-0.4.8-beta.13-x86_64.raucb.sig | 64 | `b392a50ca09dd1b56e9a646fea9b9918dc09317c2922e4eb1f2259d577572663` |
| SHA256SUMS | 214 | `d6a9ea32c617d5c13e9b73f095b028eab03aaddd73b381800d9d7f45907ca591` |
| SHA256SUMS.sig | 64 | `26a780135bcae4766832f3b8bebef804dbd9ea1802078071ce5d766842e2e105` |


## Coordinated release scope — RELEASE-POLICY-078 (9 November 2026)

Chris directs every update to include newly required OS packages and any necessary
system release without a separate reminder. Shared AGENTS.md and publishing guidance
now require dependency review against the last actual published system baseline,
image-recipe updates, rootfs verification and coordinated component/feed publication.
Launcher-only publication cannot mark an OS-dependent feature fully delivered.

External-drive packages udisks2/exfatprogs/ntfs-3g are already in the image recipe;
Beta 12 delivers the launcher half only. Required system delivery remains pending.
SYSTEM-BETA-074 was explicitly stopped by Chris and remains owned by Claude Code;
its artifacts were not resumed or republished. This policy task changes no binary,
feed or device. No extra launcher-only release was made to close this record.
Validation: policy/document diff reviewed, external-drive recipe requirements
confirmed, distribution manifest validation and six existing cases passed.
Policy scope complete; system release and Chris's real-device acceptance pending.


## Beta 0.4.8-beta.12 published — RELEASE-077 (9 November 2026)

Fresh signed Debian 13 amd64 launcher build from exact latest-main source
`eda96b378d351c5f1537829c30fa77aad62f7b6a` (5fd6321 plus publisher claim).
Application behavior is unchanged from Beta 11; intervening changes record release
coordination and validation. Beta 12 was explicitly requested from latest main.

Validation passed: 150 Python cases (one optional real-RAUC skip), 30 QML syntax
checks, ShellCheck, all seven CTest suites (56.92 seconds), native Files/artwork
probes and full X11 UI replay using disposable fixtures. Original signing identities
verified with the installed VERIFY.py; signing remained local. Initial empty/build
attempts were discarded after a missing temporary target and symlink-relative MOC
include failure; the final regular-directory build passed all required checks.

Direct upload returned HTTP 401 after creating empty draft 438577173. The documented
one-time upload fallback resumed only that draft and verified exact source/version,
asset digests and public-key signatures. Initial job 42532339388 stopped before
upload because the transport archive matched .gitignore; the archive was explicitly
tracked and job 42532361607 succeeded. No signing key or personal token went to
Actions. All four anonymous downloads and both signatures were independently
verified before advancing Beta. Temporary workflow/transport files removed.

Stable and system-beta feeds unchanged; previous releases retained. No ISO/system
bundle, VM or physical-disk operations. Chris owns hardware/VM, USB/exFAT,
controller and performance acceptance. Unmounted-drive support still needs the OS
UDisks/filesystem packages; a launcher update cannot install them.

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.12

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-launcher-0.4.8-beta.12-x86_64.tar.zst | 8545326 | `d9557b981f5833e0f52faca72f971394c96233470480d256fb2b677df1178a41` |
| gaia-launcher-0.4.8-beta.12-x86_64.tar.zst.sig | 64 | `b9126c83321faf689e2d3d2cc9789f1b759d5e81c0f5c49cb3bc290735238aa1` |
| SHA256SUMS | 222 | `8172ba56f3a91a503378a9c011a335a52817703b420781edde6d3945522038ec` |
| SHA256SUMS.sig | 64 | `3a3b42d600f98c8ad57a04d317709b54d52e31c9a409ea0c52f69c1050cc3d9b` |


## Beta 0.4.8-beta.11 published — RELEASE-076 (7 November 2026)

Signed launcher **0.4.8-beta.11** is public. Exact built source:
`640356703963dbbb0277944a9e066b9086f85f79` (latest-main UX-MEDIA-075 plus a native
QA padding expectation correction; later source commits only record release coordination).
Debian 13 amd64 native build, 150 Python cases (one optional RAUC skip), 30 QML
syntax checks, ShellCheck and seven CTest suites passed. Native Files, artwork and
complete X11 UI replay passed with disposable fixtures. The standalone PySide6 motion
probe was unavailable in this image; earlier source-session results remain separate.

Package: 8,545,324 bytes; SHA-256
`208993556b89d45bb9f5303da814028259e37daf2aab8f1d0bacbbe5cc1a1677`.
Original Ed25519 identity verified and signing performed locally. Direct upload returned
HTTP 401 after creating empty draft 437673862. The documented pinned upload-only fallback
filled that exact reviewed draft: run 42388745190 succeeded in 10 seconds. No keys or
personal tokens were sent to Actions. All four public anonymous downloads matched local
bytes; package and checksum signatures verified independently before advancing Beta.
Temporary uploader and transport copy removed. Stable/system feeds unchanged; no ISO,
system bundle, VM or physical-drive operation. Chris owns device/USB/exFAT/controller
and performance acceptance. Unmounted-drive support needs OS UDisks/filesystem packages;
this launcher package cannot add them to existing images.

Updated: 3 November 2026.

## Beta 0.4.8-beta.10 published — RELEASE-073 (3 November 2026)

Signed launcher **0.4.8-beta.10** is published:
https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.10 .
Redesigned Files app, clearer unavailable-GPU message, and the launcher half of
VM GPU graphics (needs the matching OS startup scripts, not yet in any system image).
Built by Claude Code in a fresh Debian 13 chroot from exact source
`07dfe8dc7bb85f1b3695288bb39a3a92fb2c2ad7`; original Ed25519 key verified against
the committed public key. 142 Python cases (one optional skip), 29 QML syntax files,
seven CTest suites and the native Files UI probe passed. Package 8,505,443 bytes;
SHA-256 `ed0850741e74f3095f2a7fbc18646a406dc6a2505595a5b9e917e16e365c883c`.
Uploaded by one-time push-triggered job 41549735739 (built-in token, no keys);
workflow and transport copy removed afterwards. All four anonymous downloads matched
the local bytes before the Beta feed advanced. Stable and system feeds unchanged;
no ISO/system bundle. Chris owns device acceptance.

## Beta 0.4.8-beta.9 published — UI-GRAPHICS-069 (3 November 2026)

Signed launcher **0.4.8-beta.9** is published:
https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.9 .
GPU/Software OpenGL trial with independent 20-second rollback; Gaia decision
windows, persistent supplied Light/Dark controller prompts and dropdown edge blur;
fresh UI sound volume 100%, saved preferences preserved. Exact built source
`707c37cc033dde9a79adbc4e6f073bd5dff3beb0`. Fresh local Debian 13 amd64 build and local signing;
133 Python cases (one optional skip), 27 QML syntax checks, seven CTest suites,
native renderer/Files/full UI regressions and Light/Dark visual review passed.
Package 8,487,633 bytes; SHA-256
`71efaf74064ac87d33e41003d85bb36283084845e721bde7f2defb9c373be1ef`.

The documented, explicitly approved upload-only fallback used one 9-second job,
41542664346, with GitHub's built-in token. Keys stayed local; no build/signing on
Actions. The temporary workflow and duplicate empty draft were removed. All four
anonymous downloads, both signatures/checksums and Beta read-back were verified;
feed commit `74447791c5ede4b92fd0bd98bc4c6e244e920a63`. Stable and system feeds are unchanged.
No ISO/system bundle. Chris owns device/graphics/input/audio/gameplay acceptance.
Full provenance and assets: docs/RELEASE-0.4.8-beta.9.md.

## Beta 0.4.8-beta.8 published — UPDATE-SYSTEM-068 (2 November 2026)

Signed launcher **0.4.8-beta.8** is published:
https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.8 .
Built by Claude Code in a fresh Debian 13 chroot from exact source
`cc2d65c6c1f4029c9090b8d4a2d16096c3d62ce2` (RAUC check-purpose=codesign fix,
installed-system launcher updates, image version stamping). ./dev check: 125 Python
cases and all seven CTest suites passed. Package 8,234,465 bytes; SHA-256
`722ec0b109be24e7ca5c5f9b5b59168105f9c37424bd8feae6608debc81f7b22`.
Signed locally with the existing Ed25519 key; a one-time upload-only job
(run 41525236184; first attempt 41525099531 failed before any API call because
`*.tar.zst` is git-ignored) used built-in repository credentials, then the job and
staged public files were removed. All four anonymous downloads, SHA256SUMS and both
signatures verified independently; Beta feed advanced and read back; Stable and
system-beta unchanged. Existing Beta 4 disk installs need the 0.4.8-beta.8 installer
ISO (reinstall). Chris owns device acceptance.

## Beta 0.4.8-beta.7 published — ARTWORK-063 / RELEASE-065 (2 November 2026)

Signed launcher **0.4.8-beta.7** is published:
https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.7 .
It adds automatic Libretro artwork and optional ScreenScraper BYO developer
credentials under Settings → Software → Library artwork, with local-image priority,
offline cache, credential testing/removal, region choice and complete-cover display.

Exact built source `b6d605d51b8c0a3c75ae11ac317cd1e1097f3c41`.
Package 8,257,644 bytes; SHA-256 `6b1f4bc1c47024c5a434b9feb1d84c575a5812bb4cfd9c5b037f870855dec550`.
Retained Debian stage, not a fresh build. 105 Python cases, 24 QML syntax checks,
native build, all six CTest suites (50.97s), native artwork/Files and full UI
regressions passed in source QA 41467847726. Light/Dark artwork captures reviewed.
Both signatures/checksums and all four anonymous downloads verified independently.

Keys stayed local. A one-time upload-only GitHub job used its built-in repository
token because this chat's connector does not expose release/asset-upload operations.
Upload run 41476305851 passed; its temporary workflow was removed after success.
No personal token/private key was supplied to Actions; no ongoing upload dependency.
Beta feed advanced and read back; Stable remains null. Publisher reservation released.
No ISO/reinstall or full-system bundle; Chris owns device/provider/game acceptance.
Full provenance and asset table: docs/RELEASE-0.4.8-beta.7.md.

## Beta 0.4.8-beta.6 published — FILES-062 (2 November 2026)

Home's button before Settings is now **Files**. The Gaia Light/Dark browser has
ROMs, Emulator Files and recoverable Trash views; console/emulator and file-type
filters, recursive name search, sorting, Places/Up/Back/Forward, multi-selection,
copy/move/paste, rename/folders, details and bounded text/raster previews. Gaia
naming/search/path dialogs include a controller keyboard with letters, digits and
case controls. File changes rescan the game library. X selects items, B goes back,
Y opens actions; dialogs retain their normal cancellation routing.

Advanced mode is explicit and session-only: hidden files, direct paths, mounted
media/import and OS browsing. OS core files remain read-only. Mutations are limited
to Gaia game/emulator-data folders, reject overwrites/root removal/symlink writes,
and use cancellable staged copies and recoverable Trash. Cross-filesystem Move is
refused; use copy/verify/Trash. See docs/FILES.md for actual supported paths/limits.
No external desktop dialogs, shell file actions or privileged service were added.

Published signed launcher **0.4.8-beta.6**, source
`daad1f777489bd365dc676ff837eecd972fd9c62`:
https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.6 .
Package 7,956,453 bytes; SHA-256
`faf500f91880190f859c490e1a6f838ed8b96d1485f9fe6517ff3946bf083f40`.
Existing signing trust preserved; signing/publishing ran locally, no credentials
on Actions. All four anonymous asset sizes/hashes and Beta feed read-back verified;
Stable is unchanged (release:null). Distribution channel validator and six cases pass.

Validation: 79 Python cases (18 new real-file operation cases), 23 authored QML syntax
checks, hidden Qt 6.8.3 Files/controller-keyboard tests, Debian 13 Qt 6.8.2 native build
and all five CTest suites (corrected build: 51.30 seconds). Actual native Files/worker
checks exercise copy/rename/preview/Trash/restore, controller X selection, Advanced
confirmation and refusal of writes outside Gaia folders. Four Light/Dark captures
were inspected. Native source/build/capture run: 41441070842. No VM/disk/game use.

Initial source e3c3cc9 passed all checks in run 41438977107 and was published as
0.4.8-beta.5. Final review caught an X-selection label/routing mismatch with Gaia's
global X/Close mapping; .6 supersedes .5 with a Files-local selection mapping and
regression check. The corrected build passed all native/Files checks; the existing
held-scroll timing check failed once under load. The complete existing UI suite and
Files suite then passed on the exact retained .6 binary in runtime-only replay
41442098516, without recompilation. No production held-input changes were made.

Actions use: two build jobs (255s + 239s), one runtime-only replay (73s): **567s /
9m27s total actual job duration**, not an account-wide billing reading. No further
builds were started. Workflow remains manual/explicit-marker only, no schedule or
matrix; build/replay caps 6/2 minutes and artifacts expire after three days. Signing,
public GitHub Releases distribution and channel advance remain outside Actions.

Application update only: no ISO/system bundle/reinstall was produced or required
for this feature on an existing compatible installation. Chris owns physical-device,
USB/media, gameplay/save compatibility, graphics/audio and installed-OS acceptance.
Scope complete; publisher reservation released. Previous release evidence retained.

Hashes and commands: docs/RELEASE-0.4.8-beta.6.md.

## Beta 0.4.8-beta.4 published — SETTINGS-061 (2 November 2026)

Settings → Software now provides scoped RetroArch Video, Audio, Saves & resume
and Controllers preferences: rotation/threaded video, audio latency/sync, automatic
states, save intervals/slots, player ports and controller detection. Per-key
help/inheritance reset, safe scope reset confirmation and scrolling are implemented.
Shared Gaia Light/Dark windows/buttons cover Settings information, emulator readiness,
advanced-frontend confirmation and display Keep/Revert. Routine success stays quiet.
See docs/EMULATOR-PREFERENCES.md for controls/defaults and support boundaries.

Published launcher Beta **0.4.8-beta.4**, exact built source
`c08e80d78d6e2204a72cad5d2181d7ec88e6d425` (implementation c24f72f plus QA fixes):
https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.4 .
Package: 7,557,627 bytes, SHA-256
`df757f28329d1f3adf03037b6d08db95b43a7ed1ce94a01c4320edfa5b130603`.
Existing Ed25519 trust key verified; signing/publishing ran locally, with no publisher
credentials on Actions. All four public asset sizes/hashes and Beta read-back verified.
Stable is unchanged (release:null). Public channel validator and six manifest cases pass.

Validation passed: 61 Python cases, 20 authored QML syntax checks, ShellCheck,
hidden Qt 6.8.3 settings-flow probe with mocks, Debian 13 native Qt 6.8.2 build and
all four CTest suites (50.26 seconds). Native Xvfb/Mesa OpenGL Light/Dark captures
were inspected. Build/check/capture run 41429568432 retained the exact unsigned stage.
The complete native UI suite passed in runtime-only replay 41431116419 of that same
binary, without product changes or recompilation: modal/dropdown routing, held
Select/repeat acceleration (19 rows), update error/retry/restart, theme persistence,
fullscreen and actual-backend emulator save/single-key reset/confirmation.

Actions used five Linux jobs, 790 seconds total (13m10s actual job duration, not an
account-wide billing reading). Initial attempts found checkout trust and test-fixture
cleanup/indentation defects; those fixtures were fixed and locally smoke-tested.
The full build job's update-retry timeout did not recur in the complete replay;
its cause is not established. Timeout output is now retained for diagnosis.
The workflow has no schedule/matrix or normal source-push trigger: one explicit
four-minute build job, or an optional two-minute manual replay of a retained build;
artifacts expire after three days. Publishing remains independent of Actions.

This is an application update, not a new ISO/system image. No old VM, physical disk
or real game was used. Emulator gameplay/save reliability, physical audio/controllers,
VM/GPU and installer/system-update acceptance remain with Chris. Scope complete;
publisher reservation released.

Full asset hashes and commands: docs/RELEASE-0.4.8-beta.4.md.

## Beta 0.4.8-beta.3 published — BETA-059 (1 November 2026)

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.3
Exact source: `43d47bb267e3780e406f364f53027d032f4bf4f2` (4d1382c plus publisher claim).
A fresh isolated Debian 13 amd64 build includes INSTALLER-QML-058. The rejected
BETA-057 bundle is preserved separately and was never uploaded. No source/UI code
was changed by this build task; GitHub Actions and the old VM were not used.

Commands: `./dev release --plan`; `./dev release --key <existing-private-key-file>`;
then `python3 tools/publish-update.py --channel beta --version 0.4.8-beta.3
--source-commit 43d47bb267e3780e406f364f53027d032f4bf4f2 --package <new-bundle>
--checksums <new-SHA256SUMS> --notes-file <release-notes.md>`. All returned 0.
Build umask was 022. The existing Ed25519 key matches the committed trust key;
credentials were private/outside source and absent from release assets.

Validation: 61 Python cases, 19 authored QML syntax checks, ShellCheck, native Qt
6.8.2 compilation, all four CTest suites (62 native cases, 47.35 seconds), and six
distribution manifest regressions passed. The real native `--installer --screenshot`
render returned 0; the 2048x1152 welcome capture was inspected. Both corrected QML
files and the exact version/source metadata inside the signed package match source.

Input investigation: under default Xvfb, an instrumented temporary QML probe saw
server-generated press/release repeat pairs marked isAutoRepeat=false, explaining
repeated Select and too-fast navigation. Core X11 input (QT_XCB_NO_XI2=1) improved
repeat marking; with persistent Xvfb (-noreset) the complete unmodified check-ui.py
suite passed, keeping server key auto-repeat enabled. Held Select fired once;
list navigation traversed 18 rows, early gaps 129/90/91/119 ms and late gaps
60/60/60/60/90 ms. Home/modal/picker, update retry, themes/restart and fullscreen
probes passed. This is a test-environment configuration, not a production input
fix or hardware acceptance. Diagnostic failures/logs remain available in work/.

The publisher verified signatures and checksums, upload size/digests, all four
anonymous downloads, and Beta feed read-back. A separate public/API verification
confirmed all four downloaded hashes/sizes and the exact Beta version/source.
Stable remains release:null; other feed files are unchanged. Old releases remain
available. Full asset hashes are in GaiaOS-Releases docs/RELEASE-0.4.8-beta.3.md.

Package: 7,466,811 bytes; SHA-256
`b297f656e2e36ee5fcc18be8050efe7d09fc225d924e26e82c5fc1b52d7cd4df`.
The new signed bundle is retained under /workspace/work/gaia-beta-059/dist/releases/
0.4.8-beta.3/. Build image: gaia-dev:debian13, sha256:813904acdc8c13819dd9c35f7610dd655d859ed091b9935ed80d5914985a96d0.

This release is the launcher/application package. No ISO, A/B disk or RAUC system
bundle was built/attached. System image/trust provisioning, actual disk installation,
BIOS/UEFI boot, real install/restart/reboot/rollback, GPU/audio/controller acceptance
remain pending Chris. No disks or VM were touched. Publisher reservation released.
Earlier failed-build/source-only records below remain historical evidence.

## Beta 0.4.8-beta.2 published — 31 October 2026

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.2
Source `5283791aea04fa0eaa7a92483f31cffd04e5d885` (GaiaOS main a9af5d5 plus claim;
includes PERF-052 and UPDATE-NET-051). Claude Code built and signed it with
`./dev release --key <file>` in a Debian 13 amd64 chroot (41 Python + 4 CTest
passed; both Ed25519 signatures verified). The Claude cloud session may not create
GitHub releases, so Chris created the pre-release in the GitHub web UI from the
unchanged signed bundle. The release was verified before advancing the feed: all
four anonymous downloads were byte-identical to the signed bundle, and GitHub digests matched.

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-launcher-0.4.8-beta.2-x86_64.tar.zst | 7234942 | ab20f9b7f1ebf967893e08d776148071f71ccf28b85618d94a4456e8d9317805 |
| gaia-launcher-0.4.8-beta.2-x86_64.tar.zst.sig | 64 | 557568bb9d80f64e3a73767dcccdb2bf1ebdacbab797bbcff9fa6bad6d41af26 |
| SHA256SUMS | 220 | 635b6d031cc010227b04efc3b8b1f74963458c137fb0bc252b2acb0ad4fd4a79 |
| SHA256SUMS.sig | 64 | 02cd47073091f91176c982ee9c174e035c2a42b1d1e689299702ae1081a15bfe |

Beta feed advanced to 0.4.8-beta.2 in the manifest format written by
tools/publish-update.py; both channel manifests and 6 distribution tests pass.
Stable remains null. Chris owns device/VM acceptance.

## Beta 0.4.8-beta.1 published — 1 November 2026

Built and signed on Debian 13 amd64 in the prepared gaia-dev:debian13 container
(image sha256:813904acdc8c13819dd9c35f7610dd655d859ed091b9935ed80d5914985a96d0).
Exact source: `f0300473315873854fb7ee04d3e28a46ef55372e` (application code unchanged
from ef84d63; the source commit adds the exclusive publisher claim).
Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.1

`./dev release --plan` selected 0.4.8-beta.1 from live feeds/tags.
`./dev release --key <private-key-file> --publish` returned 0, with umask 022,
using the existing matching Ed25519 key outside the checkout. No GitHub Actions
or old Debian test VM was used. GitHub access and Docker required network-enabled
execution in this cloud task; default sandbox proxy failures were not a stale-runtime
finding. The first check run exposed restrictive checkout permissions; restoring
readable checkout permissions and Git executable modes resolved it without source edits.
The failed run made no signed bundle/upload; its output directory was empty.

Validation: 40 Python + 60 native cases, ShellCheck, native Qt 6.8.2 build;
all four CTest suites passed in 47.45 seconds. Both actual channel manifests and
all six distribution regressions passed after publication. Package and checksum
list have Ed25519 signatures verified against the committed trust public key.
The publisher verified uploaded sizes/digests, published the prerelease, verified
all four anonymous downloads, advanced Beta and read the feed back. A separate
public-download/API check confirmed all four hashes and sizes, exact Beta version/
source, and Stable release:null. Feed commit: 60624ca.

Launcher package: 7,225,450 bytes; SHA-256
`e2dc1c2aaa5050827534c856e77cdd03d05ce7e3513fed7ded56afade14d583f`.
Full asset hashes are recorded in the distribution report
`docs/RELEASE-0.4.8-beta.1.md`. The signed bundle is retained under
`dist/releases/0.4.8-beta.1/` in the isolated build checkout.

Chris owns VM/device acceptance. Real device install/restart/health rollback,
VirtualBox compatibility, audio/display/controller checks remain pending. This is
a launcher/application update; no ISO was built or attached, and no kernel/base-system
OTA is claimed. Publisher reservation is released. Earlier blockers below are historical.

## Implemented in source

- Public GitHub Releases distribution with separate Stable/Beta feed pointers.
- Local build/check/sign/publish commands; no GitHub Actions workflows required.
- Version selection from feeds/tags; immutable version names, Beta default.
- Signature/checksum validation, streamed asset uploads, public download verification
  before advancing a feed, and API read-back of the new pointer.
- Optional full OS image attachments with signed checksums. Current in-app install
  remains launcher-only; complete images require manual installation.
- Quick checks by development agents; Chris owns VM/device acceptance testing.

## Historical publication blockers

No signed binary release is published; channels/beta.json and channels/stable.json
still contain release:null. Chris supplied the existing matching signing key and a
repository write token; they are configured privately for the current source session.
Authenticated repository access and a real Contents write are verified. No secret is
stored in source, release assets or Gaia devices. The release plan succeeds, but
production packaging stops at its Debian 13 amd64 build-target guard on this Ubuntu
host. The attempted rootless Debian runner lacks an allowed runtime capability.
A compatible local build machine/container is still needed; the old Debian test VM
was not used. Actual release upload/install/restart remain unverified.
Full kernel/base-system in-app updating is not implemented by hosting ISO images.

Local manifest validation and all 6 regression tests passed before this documentation
change was committed. Source tooling is validated with fixture signatures and mocked
GitHub boundaries; real upload/install/restart and Chris's acceptance remain pending.
