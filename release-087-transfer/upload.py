import os,json,hashlib,subprocess,tarfile,urllib.request
from pathlib import Path
ROOT=Path('release-087-transfer')
EXPECTED={'gaia-launcher-0.4.8-beta.17-x86_64.tar.zst': [9450480, '4185a9d11da70fbf7a95947935448f727d3d546ed746888b944c4797f9276c9c'], 'gaia-launcher-0.4.8-beta.17-x86_64.tar.zst.sig': [64, '8dbe9e52ca17772c8d5bb3b674a31e1620fc2d65f9e878c221c28df7c8f06955'], 'SHA256SUMS': [222, '90a28d9a79f707a2aaca4c41d7f2a9890ec85c3f17d5a737997bc8b52f954999'], 'SHA256SUMS.sig': [64, '420154734d7902610cb30702bafb0418aab30e6847cd18809febc773b0751295']}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(ROOT/'signed-assets.tar')=='bd056767d68e9c4d2e128a51f0690996e3dcb6548ab2867dedcb47ef85ca0a75'
assert sha(ROOT/'public.pem')=='8190d99631de9d3cfae4070806dfd8dcc03c12e56a3b7fee47563e6f2b4a84f1'
with tarfile.open(ROOT/'signed-assets.tar') as tar:
 assert set(tar.getnames())==set(EXPECTED)
 for member in tar.getmembers():
  assert member.isfile() and '/' not in member.name
  (ROOT/member.name).write_bytes(tar.extractfile(member).read())
for name,(size,digest) in EXPECTED.items():
 p=ROOT/name
 assert p.stat().st_size==size and sha(p)==digest
package=ROOT/'gaia-launcher-0.4.8-beta.17-x86_64.tar.zst'
for p in (package,ROOT/'SHA256SUMS'):
 subprocess.run(['openssl','pkeyutl','-verify','-pubin','-inkey',str(ROOT/'public.pem'),'-rawin','-in',str(p),'-sigfile',str(p)+'.sig'],check=True)
assert (ROOT/'SHA256SUMS').read_text()==''.join(EXPECTED[n][1]+'  '+n+'\n' for n in list(EXPECTED)[:2])
m=json.loads(subprocess.check_output(['tar','--zstd','-xOf',str(package),'gaia-update.json']))
assert (m['version'],m['source_commit'],m['component'])==('0.4.8-beta.17','3e7b714006e36e9620f384e28978f5d5f2ee35f0','launcher')
def api(path,*args):return json.loads(subprocess.check_output(['gh','api','repos/t4kas/GaiaOS-Releases/'+path,*args]))
r=api('releases/442137825')
assert r['draft'] and r['prerelease'] and r['tag_name']=='v0.4.8-beta.17' and not r['assets']
subprocess.run(['gh','release','upload','v0.4.8-beta.17','--repo','t4kas/GaiaOS-Releases',*[str(ROOT/n) for n in EXPECTED]],check=True)
r=api('releases/442137825')
assert {a['name'] for a in r['assets']}==set(EXPECTED)
for a in r['assets']:
 assert [a['size'],a['digest']]==[EXPECTED[a['name']][0],'sha256:'+EXPECTED[a['name']][1]]
api('releases/442137825','--method','PATCH','-F','draft=false')
for n,(size,digest) in EXPECTED.items():
 with urllib.request.urlopen('https://github.com/t4kas/GaiaOS-Releases/releases/download/v0.4.8-beta.17/'+n,timeout=90) as response:data=response.read()
 assert len(data)==size and hashlib.sha256(data).hexdigest()==digest
print('PASS: exact locally signed Beta 17 published; all four public downloads verified; feed untouched')
