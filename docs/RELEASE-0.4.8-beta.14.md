## Corrected system Beta 0.4.8-beta.14 — UPDATE-BOOT-080 (9 November 2026)

Signed system Beta 14 replaces withdrawn Beta 13. Exact system source:
`08cd11b57edbbe48a5814c48ab10c21d7ee31d55`.
Chris's recording showed launcher Beta 11 / system Beta 8 offering system Beta 13,
then a reboot ending at console-kiosk.sh:14, XDG_RUNTIME_DIR unset. Chris reports
one clean Ctrl+Alt+Delete restart restored Gaia; its version after recovery was
not independently measured. No claim that the corrected VM boot has passed.

Root cause reproduced in an isolated systemd container: Beta 13's /usr/share
was mode 0700, inherited from a restored checkout directory by copytree/rsync.
The messagebus service account could not open /usr/share/dbus-1/system.conf;
D-Bus failed, leaving the user runtime unavailable. Polkit parents had similarly
restricted directory modes. Earlier root rendering/native checks missed this
service-account access failure. Recording load does not explain these permissions.

Fixes: image staging normalizes public paths independently of checkout modes;
service/polkit parents are readable/traversable; the signing tool checks the actual
ext4 service paths and rejects the Beta 13 permissions before signing. A real ext4
corruption regression proves the gate. The kiosk validates its runtime ownership,
mode and user-bus socket, using the canonical systemd runtime if PAM omits the
variable. Greetd waits for logind and the console user's manager. The failed-boot
watchdog requests reboot even when RAUC mark-bad fails. Per-boot /run build state
is excluded. No operator key rotation or new update protocol.

Validation: 159 Python tests with real RAUC/ext4 cases, 30 QML syntax checks and
ShellCheck passed. Seven native CTest suites passed in 56.34s; current launcher
was rebuilt as Beta 14. Actual image rendering succeeded as non-root console.
Actual messagebus/polkit UIDs could read their configs. Service dependency
verification passed. An isolated systemd container then started the real system
bus, logind, user@1000 and user D-Bus; under production ordering a console-user
probe with XDG_RUNTIME_DIR deliberately unset passed. A probe replaced the
compositor: this is not BIOS/UEFI, Parallels or full Sway/DRM acceptance. Ext4 check
passed; filesystem UUID regenerated and /run is empty in the image.

System base is the retained verified Debian 13 Beta 13 root, updated offline with
exact source changes and the rebuilt launcher; no fresh Debian package install
or new ISO is claimed. All external-drive packages/kernel/firmware from that base
remain. Rootfs SHA-256:
`c89af4dfbfa61becb92f5db25a9b5b8bc9ca37f9883f015f3d4a499f173c5093`.
The signed RAUC manifest matches this checksum, source and version. Existing CMS
and Ed25519 signatures, signed checksums and all four anonymous public assets
were verified independently before advancing system-beta.

Direct upload probe HTTP 401 left empty reviewed draft 438620381. One temporary
upload-only job (run 42539813681) reconstructed the exact signed bundle from a
pinned 11,297,041-byte transfer delta plus the pinned public Beta 13 bytes, then
verified digest, Ed25519 signatures, RAUC identity/certificate/root checksum before
upload and anonymous verification. No base code was executed. Users download the
complete 1,263,052,014-byte RAUC asset; this is only transfer compression. No private
keys or personal tokens went to Actions. Temporary workflow/transport removed.
Beta 13 remains marked withdrawn with assets available for audit. Launcher Beta 12
and Stable unchanged; eight distribution cases and real updater selection passed.

Compatible provisioned A/B installs can update through Software Update. Old Beta 4
certificate-purpose verification still needs a corrected image/reinstall. No disk
erase/layout migration/new ISO. Chris owns corrected-update boot, USB/exFAT,
update/reboot/rollback, GPU/controller/performance and hardware/VM acceptance.

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.14

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-system-0.4.8-beta.14-x86_64.raucb | 1263052014 | `9558cc7c67f8de1c9ef4383b26f35ad4f6bec53525596b22cd11bf2984bd81e7` |
| gaia-system-0.4.8-beta.14-x86_64.raucb.sig | 64 | `be36a0b485545cd1df4fd4c30f113ba734dc798890e97ba71ce3c2f44190a905` |
| SHA256SUMS | 214 | `08f746800f73ef884bcc2193661b950b5720671d02f81c9464c6c0014d51679d` |
| SHA256SUMS.sig | 64 | `d6957d045801ba75086fae2941ca151638e93d73926db1750864381eb12e458a` |
