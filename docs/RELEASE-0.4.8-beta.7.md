# GaiaOS 0.4.8-beta.7 — automatic game artwork

Published: 2026-11-02T15:55:18Z
Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.7
Exact built source: `b6d605d51b8c0a3c75ae11ac317cd1e1097f3c41`.

GaiaOS 0.4.8-beta.7 adds automatic Libretro game artwork with offline caching and optional ScreenScraper bring-your-own developer credentials. Settings → Software → Library artwork offers manual downloads, provider enable/disable, masked credential entry, connection testing, preferred region and credential removal. Local covers take priority; portrait artwork is displayed without cropping.

ScreenScraper matches supported raw ROM/ISO files using locally calculated CRC32/MD5/SHA1 and file size. Compressed disc containers use Libretro/local images. Only metadata and hashes leave the device; no ROMs or shared API keys are included.

Exact built source: b6d605d51b8c0a3c75ae11ac317cd1e1097f3c41. Debian 13 QA: https://github.com/t4kas/GaiaOS/actions/runs/41467847726 . Passed 105 Python tests, 24 QML syntax checks, ShellCheck, native build, all six CTest suites, native artwork/credential and Files probes, and the complete existing UI suite. Light/Dark artwork captures reviewed. Provider HTTP/authentication uses fixtures; real provider/device/game acceptance remains with Chris.

This is the exact retained Debian 13 build, packaged and signed locally using the existing Ed25519 trust key. Signing keys were not sent to Actions. Launcher/application update only; no ISO reinstall or full-system bundle. Beta only; Stable unchanged.


## Verification

The retained unsigned Debian 13 install stage came from source QA run
https://github.com/t4kas/GaiaOS/actions/runs/41467847726 . Its artifact transport
digest and all 110 staged source/assets were checked against the exact built tree.
No native rebuild, emulator/game, ISO, VM or disk operation was performed.

Signing and packaging ran locally with the original verified Ed25519 key. Both
package/checksum signatures and signed checksums passed locally. The public-only
signed transport ZIP contained the package, signatures, notes and verification data;
no signing keys, ROMs or private runtime data were included.

The currently exposed ChatGPT GitHub connection supports repository writes but not
direct release creation or binary asset upload. For this requested publication a
one-time, upload-only job used GitHub's built-in repository token:
https://github.com/t4kas/GaiaOS-Releases/actions/runs/41476305851 .
It verified the pinned transport/asset hashes, original public-key signatures and
package version/source before uploading a draft and publishing the prerelease.
It performed no build or signing, received no private key or personal access token,
and did not update the channel. The temporary workflow was removed after success;
this introduces no ongoing Actions dependency for the updater or normal publisher.

All four anonymous public downloads were checked in the upload job and again from
the local publisher, including byte counts, SHA-256, both original-key signatures
and signed checksum contents. Only after those checks was Beta advanced. Stable
stays unchanged (release:null). Channel validator and all six manifest cases passed.
Source implementation/native/UI results are recorded in the source repository.
Physical-device, real provider-account and gameplay acceptance remain with Chris.

## Public assets

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-launcher-0.4.8-beta.7-x86_64.tar.zst | 8257644 | 6b1f4bc1c47024c5a434b9feb1d84c575a5812bb4cfd9c5b037f870855dec550 |
| gaia-launcher-0.4.8-beta.7-x86_64.tar.zst.sig | 64 | 1c227a009999dc1d90814929c54dc04238e923160bd1a721f1554cdd3058b2c2 |
| SHA256SUMS | 220 | c1d7d1459c50b0cdb6dade5f1e6bbb311e303a0517af40593cfce06b70e19754 |
| SHA256SUMS.sig | 64 | 5f7039d291a0722bdf23d696db5960007cfc6a481a897f08821be5d21ebf4a82 |
