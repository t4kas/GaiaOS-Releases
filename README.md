# GaiaOS Releases

Public distribution metadata and downloadable updates for **GaiaOS**, or **Gaia**.
The source project is maintained separately. Gaia devices will not need a GitHub
account to read these public channel feeds or download public release assets.

| Channel | Feed | Policy |
| --- | --- | --- |
| Stable | [channels/stable.json](channels/stable.json) | Released only on Chris's explicit instruction |
| Beta | [channels/beta.json](channels/beta.json) | Default channel for tested new development builds |

Feed endpoints for the forthcoming updater:

- `https://raw.githubusercontent.com/t4kas/GaiaOS-Releases/main/channels/stable.json`
- `https://raw.githubusercontent.com/t4kas/GaiaOS-Releases/main/channels/beta.json`

Both feeds currently contain `release: null`: **no update has been published yet**.
Repository initialization does not install an updater or publish the existing source
ZIP as an update. The updater UI, package builder, signing/verification and publishing
pipeline are the next implementation phase.

GitHub Releases will carry the downloadable packages. Beta builds use prerelease tags
such as `v0.4.3-beta.1`; Stable builds use ordinary tags such as `v0.4.3`. Those are tag
examples, not existing releases. Gaia will follow its explicit selected-channel feed,
not GitHub's generic "latest release" endpoint.

This initial contract describes launcher/application packages. Kernel/base-system
updates need a separate supported installation mechanism and compatibility contract.
A public release repository alone does not provide that mechanism.

See [channel format](docs/CHANNELS.md), [publishing policy](docs/PUBLISHING.md), and
[repository status](PROJECT-STATUS.md).

Validate metadata locally:

```sh
python3 tools/validate_channels.py
python3 -m unittest discover -s tests -v
```
