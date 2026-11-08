> Withdrawn from the system Beta feed: reported post-update startup failure, `XDG_RUNTIME_DIR: parameter not set` in console-kiosk.sh:14. Do not install Beta 13 while UPDATE-BOOT-080 investigates. Assets retained for audit.

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
