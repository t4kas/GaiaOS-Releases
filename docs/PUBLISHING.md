# Publication policy

## Default development publication: Beta

During future GaiaOS development, publish tested update builds to Beta by default.
Do not modify Stable as part of routine Beta work. No timer, background watcher or
automatic publisher is configured by this repository setup.

The pipeline to be implemented must:

1. Select an exact tested source commit and build a compatible binary update package.
2. Check packaging, required files, compatibility and startup; generate integrity and
   authenticity metadata. Keep private source and signing credentials private.
3. Upload all files to a uniquely tagged GitHub prerelease for Beta.
4. Verify the uploaded asset bytes, size, checksum, signature and download availability.
5. Generate and validate the Beta manifest against the real assets, then atomically
   publish that channel pointer. Keep prior downloads available for recovery.
6. Record the source commit, checks and known limitations in the release notes/status.

An application update can avoid rebuilding an ISO. It still needs a build when native
code changes and a running system for acceptance testing. VM and hardware verification
remain necessary where behavior depends on the compositor, emulators or devices.

## Explicit user publication: Stable

Publish/promote Stable only when Chris explicitly asks for a Stable release. A Beta
publication or a source merge is not Stable authorization. Use a normal release tag,
validate the Stable feed, and retain the prior Stable artifacts. An intentional
promotion must identify the tested content and any packaging changes; do not silently
relabel an untested binary. Beta may continue independently.

The policy is recorded for collaborators; it is not yet a GitHub environment approval
rule or a cryptographically enforced permission. The real publishing workflow and
its credentials/approval controls will be configured in the next phase.

## Current state

There are no binary releases to publish/promote at initialization. Keep both feeds
at `release: null` until the package builder and updater contract are implemented.
