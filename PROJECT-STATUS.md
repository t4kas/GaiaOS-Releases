# Release distribution status

Updated: 1 November 2026.

## Beta 0.4.8-beta.2 published — 31 October 2026

Release: https://github.com/t4kas/GaiaOS-Releases/releases/tag/v0.4.8-beta.2
Source `5283791aea04fa0eaa7a92483f31cffd04e5d885` (GaiaOS main a9af5d5 plus claim;
includes PERF-052 and UPDATE-NET-051). Claude Code built and signed it with
`./dev release --key <file>` in a Debian 13 amd64 chroot (41 Python + 4 CTest
passed; both Ed25519 signatures verified). The Claude cloud session may not create
GitHub releases, so Chris created the pre-release in the GitHub web UI from the
unchanged signed bundle. The release was verified before advancing the feed: all
four anonymous downloads were byte-identical to the signed bundle, and GitHub digests matched.

| Asset | Bytes | SHA-256 |
| --- | --- | --- |
| gaia-launcher-0.4.8-beta.2-x86_64.tar.zst | 7234942 | ab20f9b7f1ebf967893e08d776148071f71ccf28b85618d94a4456e8d9317805 |
| gaia-launcher-0.4.8-beta.2-x86_64.tar.zst.sig | 64 | 557568bb9d80f64e3a73767dcccdb2bf1ebdacbab797bbcff9fa6bad6d41af26 |
| SHA256SUMS | 220 | 635b6d031cc010227b04efc3b8b1f74963458c137fb0bc252b2acb0ad4fd4a79 |
| SHA256SUMS.sig | 64 | 02cd47073091f91176c982ee9c174e035c2a42b1d1e689299702ae1081a15bfe |

Beta feed advanced to 0.4.8-beta.2 in the manifest format written by
tools/publish-update.py; both channel manifests and 6 distribution tests pass.
Stable remains null. Chris owns device/VM acceptance.

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

## Implemented in source

- Public GitHub Releases distribution with separate Stable/Beta feed pointers.
- Local build/check/sign/publish commands; no GitHub Actions workflows required.
- Version selection from feeds/tags; immutable version names, Beta default.
- Signature/checksum validation, streamed asset uploads, public download verification
  before advancing a feed, and API read-back of the new pointer.
- Optional full OS image attachments with signed checksums. Current in-app install
  remains launcher-only; complete images require manual installation.
- Quick checks by development agents; Chris owns VM/device acceptance testing.

## Historical publication blockers

No signed binary release is published; channels/beta.json and channels/stable.json
still contain release:null. Chris supplied the existing matching signing key and a
repository write token; they are configured privately for the current source session.
Authenticated repository access and a real Contents write are verified. No secret is
stored in source, release assets or Gaia devices. The release plan succeeds, but
production packaging stops at its Debian 13 amd64 build-target guard on this Ubuntu
host. The attempted rootless Debian runner lacks an allowed runtime capability.
A compatible local build machine/container is still needed; the old Debian test VM
was not used. Actual release upload/install/restart remain unverified.
Full kernel/base-system in-app updating is not implemented by hosting ISO images.

Local manifest validation and all 6 regression tests passed before this documentation
change was committed. Source tooling is validated with fixture signatures and mocked
GitHub boundaries; real upload/install/restart and Chris's acceptance remain pending.
