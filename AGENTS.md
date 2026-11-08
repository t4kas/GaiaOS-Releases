# GaiaOS release repository instructions

Read README.md, PROJECT-STATUS.md and docs/PUBLISHING.md before changes.
This repository is public: keep private source, credentials, signing private keys,
ROMs, BIOS files, personal data and development/runtime state out of it.

Every completed development change must produce a new tested Beta release, including
documentation/configuration changes. Version numbers are managed automatically and
must advance beyond the latest Stable/Beta releases; never reuse release tags.
If a build/signing/publishing prerequisite blocks publication, report it explicitly.
Never create a fake update or claim an unbuilt package exists.

Change the Stable feed or publish/promote a Stable release only when Chris explicitly
requests a Stable release in the active conversation. Preserve that release decision
in the release record. Ordinary development updates must leave Stable unchanged.

Upload and verify release assets before updating a channel pointer. Keep the previous
release downloadable. Validate both channel manifests and run the tests before pushing.
Do not claim the updater, package signing or publishing pipeline is operational until
it has been implemented and verified. The initial feeds intentionally have no release.
Codex and Claude Code share development. Claim work in the source repository's
WORK-CLAIMS.md before edits, avoid active overlap, and re-read current ownership
before publishing or pushing. All distribution uses GitHub Releases directly; do
not add an Actions dependency. Quick checks may run here; Chris owns VM/device
acceptance, and the old Debian test VM is off limits unless explicitly reassigned.
Commit tested routine changes directly to main; use a
PR only if Chris explicitly requests one. Inspect current remote heads before writing.

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
this standing policy does not transfer ownership of the paused SYSTEM-BETA-074.

Current example: external-drive discovery/import is in launcher Beta 12, but
unmounted-drive support also requires udisks2, exfatprogs, ntfs-3g and the matching
UDisks/Polkit image configuration. The package list already includes these; they
have not been delivered by Beta 12's launcher package. System publication and real
USB/exFAT acceptance remain pending; already mounted drives remain usable.
