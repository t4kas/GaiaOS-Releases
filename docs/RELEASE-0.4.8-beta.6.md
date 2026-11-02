# GaiaOS 0.4.8-beta.6 — Gaia Files

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

## Assets

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| SHA256SUMS | 220 | 0802439d1f2789196813d44191c832964731b013b2293849965a38c4551add49 |
| SHA256SUMS.sig | 64 | faacd4587572f1d2e4967697d2d48df17646bbadd08c0605a21a8c44f73ee98c |
| gaia-launcher-0.4.8-beta.6-x86_64.tar.zst | 7956453 | faf500f91880190f859c490e1a6f838ed8b96d1485f9fe6517ff3946bf083f40 |
| gaia-launcher-0.4.8-beta.6-x86_64.tar.zst.sig | 64 | 81ad6d5a9708c0d71bf82dbcc8af25d4c1659e8c127319116f038e6bad762d1b |

## Commands and provenance

- Native build, required checks, Files UI/worker and four renders: https://github.com/t4kas/GaiaOS/actions/runs/41441070842
- Full UI/Files replay of the same retained binary: https://github.com/t4kas/GaiaOS/actions/runs/41442098516
- Local package-update.py --stage <retained-stage> --key <existing-key> --version 0.4.8-beta.6 --source-commit daad1f777489bd365dc676ff837eecd972fd9c62; sign SHA256SUMS; publish-update.py --channel beta with that bundle, metadata and notes.
- Staged QML/worker/config byte comparisons and embedded binary version were checked before signing; public signatures and signed checksums verified before feed advance.
- Disposable fixture data only. No ROM, BIOS, private key, token or runtime user data is distributed.
