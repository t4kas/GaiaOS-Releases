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

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.11

208993556b89d45bb9f5303da814028259e37daf2aab8f1d0bacbbe5cc1a1677  gaia-launcher-0.4.8-beta.11-x86_64.tar.zst
665b12c1b792d6339ffe3cb7951e7fb31d46c356bff8799191108ed574c95f96  gaia-launcher-0.4.8-beta.11-x86_64.tar.zst.sig
