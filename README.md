# GaiaOS Releases

Public distribution metadata and downloadable updates for **GaiaOS**, or **Gaia**.
The source project is maintained separately. Gaia devices will not need a GitHub
account to read these public channel feeds or download public release assets.

| Channel | Feed | Policy |
| --- | --- | --- |
| Stable | [channels/stable.json](channels/stable.json) | Released only on Chris's explicit instruction |
| Beta | [channels/beta.json](channels/beta.json) | Default channel for tested new development builds |

Feed endpoints used by the Gaia updater:

- `https://raw.githubusercontent.com/t4kas/GaiaOS-Releases/main/channels/stable.json`
- `https://raw.githubusercontent.com/t4kas/GaiaOS-Releases/main/channels/beta.json`

Both feeds still contain `release: null`: no signed update has been published.
The source repository now contains the updater, signature verification, rollback,
local builder and publisher. Production publication needs the existing signing
private key and a repository write token on the publishing machine.

GitHub Releases is the distribution host for all update artifacts. There are no
GitHub Actions workflows in either repository. Maintainers build/sign locally,
verify anonymous release downloads, then advance the selected feed. Beta is the
default for development; Stable remains Chris's explicit decision. Devices need
no GitHub account/token to download public assets.

From a clean source checkout with local publishing credentials:

```sh
./dev release --plan
./dev release --key /secure/gaia-update-private.pem --publish
```

Add `--attach /path/GaiaOS.iso` to include existing full OS installation media and
signed checksums in the same release. The current in-Gaia installer handles signed
launcher/application packages; full OS images are manual installation media until
a base-system update/rollback mechanism is implemented. They are not advertised
as app-install assets. Tags are unique versions such as `v0.4.8-beta.1` (examples,
not currently published releases). The selected channel feed, not GitHub's generic
latest-release endpoint, identifies the correct application update.

Codex/Claude run quick source/native checks when available. Chris owns VM/device
acceptance testing; the old Debian test VM is not part of the publication pipeline.
A compatible Debian 13 build machine/container is still needed for production
binaries; it need not be a VM and no VM test is performed automatically.

See [channel format](docs/CHANNELS.md), [publishing policy](docs/PUBLISHING.md), and
[repository status](PROJECT-STATUS.md).

Validate metadata locally:

```sh
python3 tools/validate_channels.py
python3 -m unittest discover -s tests -v
```
