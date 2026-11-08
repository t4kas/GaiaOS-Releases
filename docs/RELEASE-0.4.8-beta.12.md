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
