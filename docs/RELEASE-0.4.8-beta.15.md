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
