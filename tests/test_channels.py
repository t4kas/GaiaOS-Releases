import copy
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validate_channels', ROOT / 'tools/validate_channels.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)

def fixture(channel='beta'):
    version = '1.2.3-beta.1' if channel == 'beta' else '1.2.3'
    name = 'gaia-launcher-test.tar.zst'
    return {'schema_version': 1, 'channel': channel, 'release': {
        'version': version, 'tag': 'v' + version, 'published_at': '2026-10-31T00:00:00Z',
        'source_commit': 'a' * 40, 'minimum_updater_version': '1.0.0', 'minimum_base_version': '0.4.0',
        'release_notes': 'Test fixture only; not a published release.', 'assets': [{
            'component': 'launcher', 'platform': 'linux-debian-13', 'architecture': 'x86_64',
            'file_name': name, 'url': f'https://github.com/t4kas/GaiaOS-Releases/releases/download/v{version}/{name}',
            'size_bytes': 123, 'sha256': 'b' * 64}]}}

class ChannelTests(unittest.TestCase):
    def test_empty_channels_are_valid(self):
        for channel in ['stable', 'beta']:
            validator.validate({'schema_version': 1, 'channel': channel, 'release': None}, channel)
    def test_valid_fixture_per_channel(self):
        for channel in ['stable', 'beta']:
            validator.validate(fixture(channel), channel)
    def test_channel_and_version_mismatch_rejected(self):
        for mutate in [lambda d: d.update(channel='stable'), lambda d: d['release'].update(version='1.2.3'), lambda d: d.update(schema_version=True)]:
            d=fixture(); mutate(d)
            with self.assertRaises(ValueError): validator.validate(d, 'beta')
    def test_invalid_asset_metadata_rejected(self):
        changes=[{'url':'https://example.com/package'}, {'sha256':'placeholder'}, {'size_bytes':0},
                 {'size_bytes':True}, {'file_name':'../escape'}, {'architecture':'unknown'}]
        for change in changes:
            with self.subTest(change=change):
                d=fixture();d['release']['assets'][0].update(change)
                with self.assertRaises(ValueError):validator.validate(d,'beta')
    def test_wrong_tag_and_invalid_timestamp_rejected(self):
        for change in [{'tag':'v9.9.9'}, {'published_at':'2026-02-31T00:00:00Z'}, {'source_commit':'not-a-commit'}]:
            d=fixture();d['release'].update(change)
            with self.assertRaises(ValueError):validator.validate(d,'beta')
    def test_duplicate_targets_and_missing_fields_rejected(self):
        d=fixture();d['release']['assets'].append(copy.deepcopy(d['release']['assets'][0]))
        with self.assertRaises(ValueError):validator.validate(d,'beta')
        d=fixture();del d['release']['minimum_base_version']
        with self.assertRaises(ValueError):validator.validate(d,'beta')

if __name__=='__main__':unittest.main()
