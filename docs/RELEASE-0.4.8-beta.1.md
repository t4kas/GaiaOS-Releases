# GaiaOS 0.4.8-beta.1 publication record

## Beta 0.4.8-beta.1 published — 1 November 2026

Built and signed on Debian 13 amd64 in the prepared gaia-dev:debian13 container
(image sha256:813904acdc8c13819dd9c35f7610dd655d859ed091b9935ed80d5914985a96d0).
Exact source: `f0300473315873854fb7ee04d3e28a46ef55372e` (application code unchanged
from ef84d63; the source commit adds the exclusive publisher claim).
Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.1

`./dev release --plan` selected 0.4.8-beta.1 from live feeds/tags.
`./dev release --key <private-key-file> --publish` returned 0, with umask 022,
using the existing matching Ed25519 key outside the checkout. No GitHub Actions
or old Debian test VM was used. GitHub access and Docker required network-enabled
execution in this cloud task; default sandbox proxy failures were not a stale-runtime
finding. The first check run exposed restrictive checkout permissions; restoring
readable checkout permissions and Git executable modes resolved it without source edits.
The failed run made no signed bundle/upload; its output directory was empty.

Validation: 40 Python + 60 native cases, ShellCheck, native Qt 6.8.2 build;
all four CTest suites passed in 47.45 seconds. Both actual channel manifests and
all six distribution regressions passed after publication. Package and checksum
list have Ed25519 signatures verified against the committed trust public key.
The publisher verified uploaded sizes/digests, published the prerelease, verified
all four anonymous downloads, advanced Beta and read the feed back. A separate
public-download/API check confirmed all four hashes and sizes, exact Beta version/
source, and Stable release:null. Feed commit: 60624ca.

Launcher package: 7,225,450 bytes; SHA-256
`e2dc1c2aaa5050827534c856e77cdd03d05ce7e3513fed7ded56afade14d583f`.
Full asset hashes are recorded in the distribution report
`docs/RELEASE-0.4.8-beta.1.md`. The signed bundle is retained under
`dist/releases/0.4.8-beta.1/` in the isolated build checkout.

Chris owns VM/device acceptance. Real device install/restart/health rollback,
VirtualBox compatibility, audio/display/controller checks remain pending. This is
a launcher/application update; no ISO was built or attached, and no kernel/base-system
OTA is claimed. Publisher reservation is released. Earlier blockers below are historical.

## Published asset hashes

| Asset | Bytes | SHA-256 |
| --- | ---: | --- |
| gaia-launcher-0.4.8-beta.1-x86_64.tar.zst | 7225450 | `e2dc1c2aaa5050827534c856e77cdd03d05ce7e3513fed7ded56afade14d583f` |
| gaia-launcher-0.4.8-beta.1-x86_64.tar.zst.sig | 64 | `c73cee2b5f421b3f0a966654b9badc6190dd1338c6f90ac65f4a8c3fe0f5b824` |
| SHA256SUMS | 220 | `66c9ec8c49b3b0a0f55725478fc381cbefb1bd847d8c7d568f5be749dacca99c` |
| SHA256SUMS.sig | 64 | `e4fe95ae01e11c1669793b89118066a9c37d5ebd9efbd31b1d6cb44362125010` |

GitHub publication timestamp: 2026-10-31T22:19:52Z (UTC).
