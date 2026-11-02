# Release distribution status

Updated: 3 November 2026.

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
