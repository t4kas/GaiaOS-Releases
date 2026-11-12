# GaiaOS Beta 19 publication

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
