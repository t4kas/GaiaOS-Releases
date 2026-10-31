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
