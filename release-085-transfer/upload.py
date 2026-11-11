import os,json,hashlib,subprocess,tarfile,urllib.request
from pathlib import Path
ROOT=Path('release-085-transfer')
EXPECTED={'gaia-launcher-0.4.8-beta.16-x86_64.tar.zst': [9073895, '01256cabbd991fa98b172c5d9190ffd33574a8da083fe1d4bfd98659c625b8ca'], 'gaia-launcher-0.4.8-beta.16-x86_64.tar.zst.sig': [64, '90021c858ce83618e658ed73cc169b13fd74e15d4f788509b7ed678a27f540e7'], 'SHA256SUMS': [222, '7aa00fb25f8f36113ed1fe1918facb27123b03d852985aedae0dbb729529f4bd'], 'SHA256SUMS.sig': [64, 'aabdf04f182ec8c4520552a7208a226da52e1e0f5121e5451e255488271c3167']}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(ROOT/'signed-assets.tar')=='5e59b7cc6c849c12cc56da28046f9147cc69e14c2886f819c86bb897099058f7'
assert sha(ROOT/'public.pem')=='8190d99631de9d3cfae4070806dfd8dcc03c12e56a3b7fee47563e6f2b4a84f1'
with tarfile.open(ROOT/'signed-assets.tar') as tar:
 assert set(tar.getnames())==set(EXPECTED)
 for member in tar.getmembers():
  assert member.isfile() and '/' not in member.name
  (ROOT/member.name).write_bytes(tar.extractfile(member).read())
for name,(size,digest) in EXPECTED.items():
 p=ROOT/name
 assert p.stat().st_size==size and sha(p)==digest
package=ROOT/'gaia-launcher-0.4.8-beta.16-x86_64.tar.zst'
for p in (package,ROOT/'SHA256SUMS'):
 subprocess.run(['openssl','pkeyutl','-verify','-pubin','-inkey',str(ROOT/'public.pem'),'-rawin','-in',str(p),'-sigfile',str(p)+'.sig'],check=True)
assert (ROOT/'SHA256SUMS').read_text()==''.join(EXPECTED[n][1]+'  '+n+'\n' for n in list(EXPECTED)[:2])
m=json.loads(subprocess.check_output(['tar','--zstd','-xOf',str(package),'gaia-update.json']))
assert (m['version'],m['source_commit'],m['component'])==('0.4.8-beta.16','047984c5343f177d6c202c9082b7dbce05b456f4','launcher')
def api(path,*args):return json.loads(subprocess.check_output(['gh','api','repos/t4kas/GaiaOS-Releases/'+path,*args]))
r=api('releases/442077060')
assert r['draft'] and r['prerelease'] and r['tag_name']=='v0.4.8-beta.16' and not r['assets']
subprocess.run(['gh','release','upload','v0.4.8-beta.16','--repo','t4kas/GaiaOS-Releases',*[str(ROOT/n) for n in EXPECTED]],check=True)
r=api('releases/442077060')
assert {a['name'] for a in r['assets']}==set(EXPECTED)
for a in r['assets']:
 assert [a['size'],a['digest']]==[EXPECTED[a['name']][0],'sha256:'+EXPECTED[a['name']][1]]
api('releases/442077060','--method','PATCH','-F','draft=false')
for n,(size,digest) in EXPECTED.items():
 with urllib.request.urlopen('https://github.com/t4kas/GaiaOS-Releases/releases/download/v0.4.8-beta.16/'+n,timeout=90) as response:data=response.read()
 assert len(data)==size and hashlib.sha256(data).hexdigest()==digest
print('PASS: exact locally signed Beta 16 published; all four public downloads verified; feed untouched')
