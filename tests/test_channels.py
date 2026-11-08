import copy
import importlib.util
from pathlib import Path
import unittest
import json
import subprocess
import sys
import tempfile

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

    def test_system_feeds_accept_only_system_packages_and_protocol_two(self):
        for channel in ['stable', 'beta']:
            data=fixture(channel)
            data['release']['minimum_updater_version']='2.0.0'
            asset=data['release']['assets'][0]
            asset.update(component='system',file_name='gaia-system-test.raucb')
            asset['url']=asset['url'].rsplit('/',1)[0]+'/'+asset['file_name']
            validator.validate(data,channel,'system')
            with self.assertRaises(ValueError):validator.validate(data,channel)
            with self.assertRaises(ValueError):validator.validate(fixture(channel),channel,'system')
            invalid=copy.deepcopy(data);invalid['release']['minimum_updater_version']='1.0.0'
            with self.assertRaises(ValueError):validator.validate(invalid,channel,'system')
            invalid=copy.deepcopy(data);invalid['release']['assets'][0]['file_name']='launcher.tar.zst'
            with self.assertRaises(ValueError):validator.validate(invalid,channel,'system')

    def test_command_checks_present_system_feeds_as_well_as_launcher_feeds(self):
        with tempfile.TemporaryDirectory() as temporary:
            channels=Path(temporary)/'channels';channels.mkdir()
            for channel in ['stable','beta']:
                (channels/(channel+'.json')).write_text(json.dumps(dict(schema_version=1,channel=channel,release=None)))
            system=fixture();system['release']['minimum_updater_version']='2.0.0'
            asset=system['release']['assets'][0];asset.update(component='system',file_name='gaia-system-test.raucb')
            asset['url']=asset['url'].rsplit('/',1)[0]+'/'+asset['file_name']
            path=channels/'system-beta.json';path.write_text(json.dumps(system))
            command=[sys.executable,str(ROOT/'tools/validate_channels.py'),'--root',temporary]
            valid=subprocess.run(command,capture_output=True,text=True)
            self.assertEqual(valid.returncode,0,valid.stderr)
            self.assertIn('system-beta: valid',valid.stdout)
            asset['component']='launcher';path.write_text(json.dumps(system))
            invalid=subprocess.run(command,capture_output=True,text=True)
            self.assertNotEqual(invalid.returncode,0)
            self.assertIn('Unsupported target',invalid.stderr)

if __name__=='__main__':unittest.main()
