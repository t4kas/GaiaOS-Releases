# Direct GitHub Releases publication

## Coordinated launcher and OS releases — Chris, 9 November 2026

Every Beta or explicitly requested Stable release must assess both launcher and
system changes. A request to release GaiaOS includes building/signing/publishing
the required OS/system component on that channel; Chris need not separately ask
for OS packages each time. Stable still requires an explicit Stable request.

Before selecting artifacts, compare latest main with the actual source/version
in each last published component feed. In particular, compare OS requirements
with the last published system image/bundle, not the last launcher release: an
intervening launcher release does not ship or clear pending OS changes. An empty
system feed means there is no published system baseline, not that OS work is done.
Review os/ (package lists, overlay, services, Polkit, graphics, kernel/firmware,
boot/RAUC configuration), native runtime dependencies and feature release notes.
Add any newly required OS packages and configuration to the tracked image recipe.
Check the built rootfs actually contains those dependencies and configuration.

When features need OS changes, build a compatible current system rootfs, sign and
verify its RAUC bundle and public assets, then advance the matching system feed
alongside any required launcher feed. A complete system bundle may carry its own
matching launcher; record which components/artifacts deliver each feature rather
than publishing a redundant launcher blindly. Record exact source/version for each
artifact, compatibility/migration limits and pending Chris acceptance. An attached
ISO alone does not update installed systems. Preserve existing signing identities,
old downloads, channel boundaries and verify-before-feed publication order.

If a required system build/publication is blocked, identify the concrete blocker
and mark the feature/release as partially delivered; do not call a launcher-only
release complete for that feature. Do not produce another launcher-only Beta just
to close the missing-system-release work or its release-policy record. Existing
explicit stop instructions and another agent's owned artifacts remain in force;
record any explicit resumption or reassignment in WORK-CLAIMS.md before proceeding.

Current example: external-drive discovery/import is in launcher Beta 12, but
unmounted-drive support also requires udisks2, exfatprogs, ntfs-3g and the matching
UDisks/Polkit image configuration. The package list includes these. Launcher Beta 12 delivered the UI; signed system
Beta 13 now delivers the OS dependencies on compatible provisioned A/B installs.
Old Beta 4 verification needs a corrected installation image/reinstall. Real USB/
exFAT and boot/update/rollback acceptance remain pending Chris.


GitHub Releases hosts all update artifacts; publishing is independent of GitHub Actions.
Optional bounded QA may build/test an unsigned Debian artifact on Actions, then a
local publisher verifies its source/version and signs it outside the runner. Source
pushes do not themselves create binaries. The source repository provides local
`dev release`, package-update.py and publish-update.py commands.

1. Select a clean source commit. Run quick checks on the available environment.
2. Build the Debian 13 amd64 application on a compatible machine/container. No VM
   acceptance step is automatically invoked; Chris owns device/VM testing.
3. Sign the package and checksum list with the existing trusted private key file.
   The private key must match the committed public trust key. Keep credentials
   on the publisher; never put them in this repository, release assets or devices.
4. Upload a uniquely versioned GitHub draft release; Beta is a prerelease.
5. Verify uploaded size/digest, publish, and verify anonymous public download
   bytes. Only then update the selected channel pointer and read it back.
6. Retain old releases and record the exact source, quick checks and pending
   acceptance in release notes. A failed/unreferenced publication does not justify
   reusing its tag. Review the draft/release before retrying.

The local command defaults to preparing a signed bundle, with `--publish` opting
into the upload/pointer step. Normal development must publish to Beta or report
its concrete credential/build blocker. Version selection uses channel state and
existing release/tag names, including authenticated drafts, without an Actions
run counter. A retained bundle can be published by publish-update.py without a
rebuild. See the source docs/SOFTWARE-UPDATES.md for complete commands.

`--attach` distributes existing full OS images or other artifacts in the same
GitHub Release with signed SHA256SUMS. Each asset must be smaller than 2 GiB.
The application channel contract still contains only compatible launcher packages.
Attached ISO images are manual installation media. Kernel/base-system installation
inside Gaia requires a separate supported installer and rollback protocol.

Stable requires a new explicit instruction from Chris and `--authorize-stable`.
A source commit, Beta publication or passing quick test is not Stable authorization.
VM/device tests are run by Chris for now; never claim they passed without his result.

Signed Beta 0.4.8-beta.9 is published and verified; Stable remains empty. See
[the publication record](RELEASE-0.4.8-beta.9.md) for checks, source and hashes.

For RELEASE-065, an upload-only temporary job transferred an already locally signed
bundle using the built-in repository token. It was removed after verified upload;
no private keys/personal tokens were sent to the runner. This one-time transfer did
not add an ongoing Actions requirement. See the .7 publication record.
