# GaiaOS release repository instructions

Read README.md, PROJECT-STATUS.md and docs/PUBLISHING.md before changes.
This repository is public: keep private source, credentials, signing private keys,
ROMs, BIOS files, personal data and development/runtime state out of it.

Beta is the default publication channel during GaiaOS development. Publish a Beta
only when a real compatible package has been built and tested. A source-only change
must not create a fake update or claim an unbuilt package exists.

Change the Stable feed or publish/promote a Stable release only when Chris explicitly
requests a Stable release in the active conversation. Preserve that release decision
in the release record. Ordinary development updates must leave Stable unchanged.

Upload and verify release assets before updating a channel pointer. Keep the previous
release downloadable. Validate both channel manifests and run the tests before pushing.
Do not claim the updater, package signing or publishing pipeline is operational until
it has been implemented and verified. The initial feeds intentionally have no release.
Use branches/PRs for later changes and inspect current remote heads before writing.
