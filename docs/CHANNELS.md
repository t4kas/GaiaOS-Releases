# Channel manifest contract, schema 1

Each channel has an independent JSON feed. Clients request only their selected feed.
The channel in the response must match the requested channel. Schema versions other
than 1 must be rejected until supported. `release: null` means no available release.

A nonempty release has:

- `version`: numeric major.minor.patch; Beta appends `-beta.N` (N starts at 1).
- `tag`: `v` followed by that exact version.
- `published_at`: UTC RFC 3339 timestamp ending in Z.
- `source_commit`: exact 40-character lowercase Git source commit SHA.
- `minimum_updater_version` and `minimum_base_version`: required compatibility floors.
- `release_notes`: plain release-note text.
- `assets`: one or more launcher assets with unique platform/architecture targets.

Each asset specifies component (`launcher`), platform (`linux-debian-13` initially),
architecture (`x86_64` initially), filename, HTTPS GitHub release download URL, positive
byte size and SHA-256. URLs must point to this repository's `/releases/download/<tag>/`
path and match the filename/tag. A checksum identifies the package bytes; it is not
an authenticity signature. Trusted signing/verification will be finalized with the
installer before any package is accepted for installation. Schema additions must be
versioned if they change the validation contract.

No channel, manifest version or tag example guarantees that a package is compatible.
The updater must enforce supported platform/architecture, base/updater floors, version
ordering, integrity/authenticity, disk-space checks and installation recovery.
Channel switching should check the new feed and let the user choose an available
compatible update; it must not silently downgrade an installed newer version.

Beta and Stable are distribution choices. This repository does not choose the default
channel for a freshly installed Gaia device; that product setting will be implemented
with the update UI. "Beta by default" here refers to publishing new development builds.
