GaiaOS 0.4.8-beta.8 fixes system updates on disk installations and brings the launcher update support for installed systems.

- Installed systems now accept Gaia's signed system updates. Earlier images rejected the signing certificate ("unsuitable certificate purpose") because RAUC checked the wrong certificate purpose; the A/B system configuration now checks Code Signing.
- Disk installations check both the launcher feed and the system feed, so launcher updates also reach installed systems.
- The launcher reports its real release version on new images instead of 0.4.8-beta.1.

Existing 0.4.8-beta.4 disk installations cannot install system updates and need a one-time reinstall from the 0.4.8-beta.8 installer ISO. Launcher/application update only; no full-system bundle. Beta only; Stable unchanged.

Quick local checks passed in a Debian 13 chroot. VM/hardware acceptance: pending Chris.
