# GaiaOS 0.4.8-beta.4 — SETTINGS-061

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

## Assets

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| SHA256SUMS | 220 | 2e7eb6f1ff2039985e4b3b646af4412fba92342dc195d75d5067aa8ad314cc1c |
| SHA256SUMS.sig | 64 | bf5097ce6b8d2229bcf30c1c83a4d51570b36a0a709e411a714214ca8649de47 |
| gaia-launcher-0.4.8-beta.4-x86_64.tar.zst | 7557627 | df757f28329d1f3adf03037b6d08db95b43a7ed1ce94a01c4320edfa5b130603 |
| gaia-launcher-0.4.8-beta.4-x86_64.tar.zst.sig | 64 | 59b0deab3d94d4c9cc2e58892750e35ef1c288e106c02b55e1456c530ca88b03 |

## Commands and provenance

- Native Debian build/check/captures: https://github.com/t4kas/GaiaOS/actions/runs/41429568432
- Complete native UI replay (same retained executable): https://github.com/t4kas/GaiaOS/actions/runs/41431116419
- Local: package-update.py --stage <retained-stage> --key <existing-private-key> --version 0.4.8-beta.4 --source-commit c08e80d78d6e2204a72cad5d2181d7ec88e6d425; signed SHA256SUMS; publish-update.py --channel beta with that package, metadata and notes.
- Staged QML, updater/config files and embedded binary version checked against the built source before packaging.
- Source test-harness diagnostic follow-up: 5d81475; it does not change product code or the retained binary.
- Quick local checks are distinct from native rendered captures and Chris's pending acceptance.
