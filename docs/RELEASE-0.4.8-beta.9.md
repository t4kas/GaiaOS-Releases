# GaiaOS 0.4.8-beta.9 — controller UI and reversible rendering

Published: 2026-11-02T23:05:54Z (3 November 2026 in Chris's timezone).
Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.9
Exact built source: `707c37cc033dde9a79adbc4e6f073bd5dff3beb0`.
Beta feed commit: `74447791c5ede4b92fd0bd98bc4c6e244e920a63`.

Settings → Video offers Automatic, GPU accelerated and Software OpenGL with a
20-second Keep changes/Revert trial. An independent supervisor restores the prior
choice after timeout, failed startup or a renderer crash. Hardware trials reject
software-only OpenGL contexts; games and advanced frontends retain their boot
rendering environment. This setting does not install drivers or change the compositor.

Gaia decision windows use the supplied icon/title, centered message, divider and
gradient footer design in Light/Dark. Persistent context-sensitive A/B/X/Y prompts
use Chris's supplied theme-specific SVGs, with a rounded panel above modal dimming.
Long dropdowns reveal selection and show progressive top/bottom edge blur where
more choices remain. Interior controller selection stays clear of the blurred
edges. Fresh UI sound volume is 100%; saved volume and mute settings are preserved.

## Build and validation

Fresh local Debian 13 amd64 container build, packaged and signed locally with the
original Ed25519 trust identity. 133 Python cases (132 passed; one optional RAUC
integration skip), 27 QML syntax checks, ShellCheck and all seven CTest suites
passed. The release build's CTest duration was 53.63 seconds.

Actual native Qt Keep/Revert/unavailable-GPU recovery, real-process game/frontend
environment isolation, native Files/worker, modal/dropdown/controller prompts,
update retry, theme/restart, fullscreen and held-navigation probes passed.
Light/Dark popup, Home, menu, renderer-confirmation and Files captures were reviewed.
The controlled Xvfb check disables server-generated key repeat (-r) because Gaia
owns repeat scheduling; it traversed 19 rows. SDL virtual-controller hold/chord
regressions run separately. Physical keyboard repeat is not claimed verified.

## Publication and verification

The direct binary upload endpoint rejected the session credential with HTTP 401.
Chris explicitly approved the documented temporary upload-only fallback and all
remaining publication/completion steps. One pinned job used GitHub's built-in
repository token, verified the transport and all asset digests, both original-key
signatures and package version/source, then uploaded/published the prerelease:
https://github.com/t4kas/GaiaOS-Releases/actions/runs/41542664346 .
Actual upload job duration: **9 seconds**, not an account-wide billing reading.
It performed no build/signing and received no private key or personal access token.
The temporary workflow was removed after success; no ongoing Actions publisher remains.
The duplicate empty draft from the failed local attempts was removed; older releases remain.

All four public downloads were independently downloaded locally and their sizes,
SHA-256, both signatures and signed checksum contents verified against committed
trust. Only then was Beta advanced and read back; Stable is unchanged (release:null).
No system feed, ISO or full-system image was published. Compatible installations
receive this launcher update; older Beta 4 disk systems retain their documented
one-time recovery/reinstall requirement. Chris owns physical GPU/controller/audio,
gameplay, installed-system update and VM acceptance.

Transport SHA-256: `06c0b2036782bf5df9ea066e1874f6628717e04178c1cb155749ebea87280fe3`.
Public-only Git transport blob: `a7fe284067029a8ceef055d48f71d85dd69a609a`.

## Public assets

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-launcher-0.4.8-beta.9-x86_64.tar.zst | 8487633 | `71efaf74064ac87d33e41003d85bb36283084845e721bde7f2defb9c373be1ef` |
| gaia-launcher-0.4.8-beta.9-x86_64.tar.zst.sig | 64 | `79b4136f366550f4fa69c3451d9c8c7db4444e167a479f478d7fb784166155fb` |
| SHA256SUMS | 220 | `906eed4d4826fc1e7bff1eba305ab5c3432066e7fd84ab41554424bb5f8792fb` |
| SHA256SUMS.sig | 64 | `aeccef264b8ce1e5dff1d9935a83bdbdaf1c78ffa935e615773643d067bf6c9e` |
