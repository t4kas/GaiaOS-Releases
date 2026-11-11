# GaiaOS Beta 17 publication

## Launcher Beta 0.4.8-beta.17 — RELEASE-087 (11 November 2026)

Fresh Debian 13 amd64 launcher built from latest main source
`3e7b714006e36e9620f384e28978f5d5f2ee35f0` (dac75e4 plus exclusive release claim).
Includes HOME-086 implementation 3cd6842: 500 ms Guide/PS/Xbox/Home hold for the
quick menu, short-tap Home with the process paused, profile-avatar Playing tile
and same-process resume, narrower quick menu with inline volume/status/Power,
faster animated navigation glow, bottom-button bounce and three supplied random
click sounds. The prior HOME-086 locally signed bundle was not reused.

Assessed the actual published system Beta 15 baseline `257cbe2`: no os/ or native
runtime dependency changes since that baseline. System 15 already provides
Dolphin, controller HID rules and external-drive packages. Compatible A/B installs
should install system 15 if needed, reboot, then check again for launcher 17.
No new system bundle/ISO, disk-layout migration or Stable change. Old Beta 4
certificate-purpose verification still needs corrected installation media/reinstall.

Validation: 159 Python tests (one optional real-RAUC skip), 33 QML syntax checks,
ShellCheck, fresh native build and all seven CTest suites passed (71.31 seconds).
Focused real-launcher X11 quick-menu replay passed tap Home/Playing resume,
software glow entry/exit, bouncing random navigation click without duplicate cues,
actual process pause/resume/close, scoped Gaia preferences and confirmations.
Native pointer drag commits the final volume-slider position. Light/Dark captures
were reviewed. Extracted metadata, actual binary version and every packaged QML,
sound, helper and font match the exact source. Existing Ed25519 and RAUC identities
verified; both Ed25519 signatures and signed checksums verified locally.
Optional Sway/grim/Pillow are absent in this builder, so no new isolated Sway run
is claimed; HOME-086's earlier compositor validation is separate. Broad headless
held-list timing remains the previously recorded intermittent QA limitation.

Direct upload to draft 442137825 returned HTTP 401. The documented temporary
signed-only upload run [43090279526](https://github.com/t4kas/GaiaOS-Releases/actions/runs/43090279526)
transferred pinned local public bytes and verified exact source/version, asset
hashes and public-key signatures before publication. No private keys or personal
tokens went to Actions. Independent local anonymous downloads of all four assets,
both signatures and signed checksums passed before Beta feed advancement.
Temporary workflow and transport removed; no ongoing Actions publisher installed.
Stable and system Beta 15 remain unchanged, and previous downloads are retained.

Chris owns physical-controller/audio/gameplay/save-resume and VM/hardware
boot/update/rollback acceptance. No old test VM, disks or real power/audio
services were used. Fixtures establish application behavior, not device acceptance.

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.17

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-launcher-0.4.8-beta.17-x86_64.tar.zst | 9450480 | `4185a9d11da70fbf7a95947935448f727d3d546ed746888b944c4797f9276c9c` |
| gaia-launcher-0.4.8-beta.17-x86_64.tar.zst.sig | 64 | `8dbe9e52ca17772c8d5bb3b674a31e1620fc2d65f9e878c221c28df7c8f06955` |
| SHA256SUMS | 222 | `90a28d9a79f707a2aaca4c41d7f2a9890ec85c3f17d5a737997bc8b52f954999` |
| SHA256SUMS.sig | 64 | `420154734d7902610cb30702bafb0418aab30e6847cd18809febc773b0751295` |
