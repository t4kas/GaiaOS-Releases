# GaiaOS 0.4.8-beta.3 publication record

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

## Asset verification

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| gaia-launcher-0.4.8-beta.3-x86_64.tar.zst | 7466811 | `b297f656e2e36ee5fcc18be8050efe7d09fc225d924e26e82c5fc1b52d7cd4df` |
| gaia-launcher-0.4.8-beta.3-x86_64.tar.zst.sig | 64 | `1f4c861397439bc5ad488ec2719e77ff0161d9a2cba9de0bd89f57f960e726a6` |
| SHA256SUMS | 220 | `9e650096756efd4b3e13242ba35455cfda43b9232383805d34b484681556ace4` |
| SHA256SUMS.sig | 64 | `04c1b6e526e4c5fd0ae40ea6b1b569ea078aa79ede6f676a706c7ae71a50b129` |

GitHub publication timestamp: 2026-11-01T20:31:41Z (UTC).
