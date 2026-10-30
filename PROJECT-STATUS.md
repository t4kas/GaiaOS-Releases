# Release distribution status

Updated: 31 October 2026.

## Ready
- Public repository: t4kas/GaiaOS-Releases.
- Independent Beta and Stable channel feeds, both initially empty.
- Versioned manifest contract, validation script, regression tests and validation workflow.
- Beta-default and explicit-Stable publishing policy for future development sessions.

## Not published or implemented yet
No binary update package or release has been published. Gaia's channel selector,
update flow, downloader/installer, package builder, trusted signing keys, rollback
and authenticated publishing pipeline are awaiting the next phase and UI references.
The private source repository remains separate; source changes alone do not release binaries.

## Next
Use Chris's supplied screenshots to implement the in-Gaia channel selector and update
flow. Finalize package installation/signing/compatibility, then publish a real Beta
through the pipeline and test check/download/verification/install/restart/recovery.
Stable publication is reserved for an explicit user request.
