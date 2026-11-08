GaiaOS 0.4.8-beta.13 — system Beta

Fresh Debian 13 amd64 system rootfs from source 67f1de12024ca9e0b26047ddd816a519a4f6b3fd. Includes the current launcher built as Beta 13, external-drive discovery/import and the required udisks2, exfatprogs and ntfs-3g packages and UDisks policy. Also includes current graphics/session startup scripts, kernel, firmware and the corrected RAUC Code Signing purpose configuration.

This is a signed full-system RAUC update for provisioned Gaia A/B installations. The launcher-only Beta feed remains at Beta 12; its application behavior is already included here. Settings → Software Update checks both feeds and offers the newer system component first.

Compatibility: the installed root must already have the corrected RAUC codesign verification configuration. Old Beta 4 images with the original certificate-purpose bug cannot install system bundles and require reinstalling a corrected installation image. This release contains no new installer ISO and does not migrate live/legacy layouts.

Validation passed: 151 Python tests, 30 QML syntax checks, ShellCheck, seven native CTest suites on the build host and again inside the fresh system root, native Files/artwork and complete X11 UI replay on the installed binary, and an actual render using the new root's runtime libraries. Image checks confirmed all 69 recipe packages, the installed launcher files, system version/source, UDisks policy and trust configuration; ext4 filesystem check passed. The complete UI replay passed after a held-key timing failure during concurrent image assembly.

Existing RAUC and Ed25519 trust identities preserved. Signing stays local. Real USB/exFAT, BIOS/UEFI boot, update/reboot/rollback, controllers, GPU/performance and hardware/VM acceptance remain pending Chris. No old VM or physical disk was used.
