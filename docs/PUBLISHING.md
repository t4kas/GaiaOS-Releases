# Direct GitHub Releases publication

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
