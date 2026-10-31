# Release distribution status

Updated: 31 October 2026.

## Implemented in source

- Public GitHub Releases distribution with separate Stable/Beta feed pointers.
- Local build/check/sign/publish commands; no GitHub Actions workflows required.
- Version selection from feeds/tags; immutable version names, Beta default.
- Signature/checksum validation, streamed asset uploads, public download verification
  before advancing a feed, and API read-back of the new pointer.
- Optional full OS image attachments with signed checksums. Current in-app install
  remains launcher-only; complete images require manual installation.
- Quick checks by development agents; Chris owns VM/device acceptance testing.

## Pending live publication

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
