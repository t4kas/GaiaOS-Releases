#!/usr/bin/env python3
"""Validate local channel feeds; does not download or publish anything."""
import argparse
from datetime import datetime
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
VERSION = r'(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)'

def require(condition, message):
    if not condition:
        raise ValueError(message)

def keys(obj, expected):
    require(isinstance(obj, dict) and set(obj) == set(expected), 'Unexpected or missing fields')

def validate(data, expected_channel):
    keys(data, ['schema_version', 'channel', 'release'])
    require(type(data['schema_version']) is int and data['schema_version'] == 1, 'Unsupported schema version')
    require(expected_channel in ('stable', 'beta') and data['channel'] == expected_channel, 'Channel mismatch')
    release = data['release']
    if release is None:
        return
    keys(release, ['version', 'tag', 'published_at', 'source_commit', 'minimum_updater_version', 'minimum_base_version', 'release_notes', 'assets'])
    suffix = r'-beta\.[1-9][0-9]*' if expected_channel == 'beta' else ''
    require(isinstance(release['version'], str) and re.fullmatch(VERSION + suffix, release['version']), 'Invalid version for channel')
    require(release['tag'] == 'v' + release['version'], 'Tag/version mismatch')
    stamp = release['published_at']
    require(isinstance(stamp, str) and re.fullmatch(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z', stamp), 'Invalid UTC timestamp')
    datetime.fromisoformat(stamp.replace('Z', '+00:00'))
    require(isinstance(release['source_commit'], str) and re.fullmatch('[0-9a-f]{40}', release['source_commit']), 'Invalid source commit')
    for name in ['minimum_updater_version', 'minimum_base_version']:
        require(isinstance(release[name], str) and re.fullmatch(VERSION, release[name]), 'Invalid compatibility version')
    require(isinstance(release['release_notes'], str) and release['release_notes'].strip(), 'Missing release notes')
    require(isinstance(release['assets'], list) and release['assets'], 'Missing assets')
    targets, names = set(), set()
    for asset in release['assets']:
        keys(asset, ['component', 'platform', 'architecture', 'file_name', 'url', 'size_bytes', 'sha256'])
        require(asset['component'] == 'launcher' and asset['platform'] == 'linux-debian-13' and asset['architecture'] == 'x86_64', 'Unsupported target')
        name = asset['file_name']
        require(isinstance(name, str) and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', name), 'Invalid filename')
        url = f"https://github.com/t4kas/GaiaOS-Releases/releases/download/{release['tag']}/{name}"
        require(asset['url'] == url, 'Wrong repository, tag or asset URL')
        require(type(asset['size_bytes']) is int and asset['size_bytes'] > 0, 'Invalid asset size')
        require(isinstance(asset['sha256'], str) and re.fullmatch('[0-9a-f]{64}', asset['sha256']), 'Invalid checksum')
        target = (asset['component'], asset['platform'], asset['architecture'])
        require(target not in targets and name not in names, 'Duplicate asset target or filename')
        targets.add(target)
        names.add(name)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        for channel in ['stable', 'beta']:
            validate(json.loads((args.root / 'channels' / f'{channel}.json').read_text()), channel)
            print(f'{channel}: valid')
    except (ValueError, OSError, TypeError) as error:
        parser.exit(1, f'Invalid channel metadata: {error}\n')

if __name__ == '__main__':
    main()
