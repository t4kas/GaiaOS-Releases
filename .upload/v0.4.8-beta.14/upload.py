"""One-time transfer of an already locally built, signed and verified system bundle."""
import hashlib,json,os,subprocess,tempfile,time,urllib.error,urllib.request
from pathlib import Path
CONFIG = {'draft_id': 438620381, 'assets': {'gaia-system-0.4.8-beta.14-x86_64.raucb': {'size': 1263052014, 'sha256': '9558cc7c67f8de1c9ef4383b26f35ad4f6bec53525596b22cd11bf2984bd81e7'}, 'gaia-system-0.4.8-beta.14-x86_64.raucb.sig': {'size': 64, 'sha256': 'be36a0b485545cd1df4fd4c30f113ba734dc798890e97ba71ce3c2f44190a905'}, 'SHA256SUMS': {'size': 214, 'sha256': '08f746800f73ef884bcc2193661b950b5720671d02f81c9464c6c0014d51679d'}, 'SHA256SUMS.sig': {'size': 64, 'sha256': 'd6957d045801ba75086fae2941ca151638e93d73926db1750864381eb12e458a'}}, 'chunks': [{'name': '0000.part', 'size': 11297041, 'sha256': '34cfd7480ef121688f9bc52afc44d5a5ffedf6cc763d202ef5dcfe775bd92427'}], 'rootfs_sha256': 'c89af4dfbfa61becb92f5db25a9b5b8bc9ca37f9883f015f3d4a499f173c5093', 'transport': {'update-key.pub': '8190d99631de9d3cfae4070806dfd8dcc03c12e56a3b7fee47563e6f2b4a84f1', 'rauc-cert.crt': '74128e22f08cbfaf1a735656bf94123e1bc7afbd9fb0b9329511acba03644313', 'release-notes.md': '89f4f33633f7bbb7d0449ca002c882a46d829c44c2e31c494e0b66095ef7b3ce'}, 'base': {'url': 'https://github.com/t4kas/GaiaOS-Releases/releases/download/v0.4.8-beta.13/gaia-system-0.4.8-beta.13-x86_64.raucb', 'size': 1262339309, 'sha256': 'b96729b43f46920196c130993b602f3dca032dd7191e08ef468463ac365dac8a'}}
D=Path('.upload/v0.4.8-beta.14')
WORK=Path(tempfile.mkdtemp(prefix='gaia-signed-system13-'))
API='https://api.github.com/repos/t4kas/GaiaOS-Releases'
VERSION='0.4.8-beta.14'; SOURCE='08cd11b57edbbe48a5814c48ab10c21d7ee31d55'
PKG='gaia-system-'+VERSION+'-x86_64.raucb'
def sha(path):
 with Path(path).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
PATCH=WORK/'bundle.vcdiff'
with PATCH.open('wb') as out:
 for part in CONFIG['chunks']:
  p=D/'chunks'/part['name']
  assert p.stat().st_size==part['size'] and sha(p)==part['sha256'],part['name']
  with p.open('rb') as f:
   while block:=f.read(1024*1024):out.write(block)
# Public base is treated only as bytes; no code from it is executed.
BASE=WORK/'base.raucb';digest=hashlib.sha256();size=0
with urllib.request.urlopen(CONFIG['base']['url'],timeout=180) as src,BASE.open('wb') as out:
 while block:=src.read(1024*1024):out.write(block);digest.update(block);size+=len(block)
assert (size,digest.hexdigest())==(CONFIG['base']['size'],CONFIG['base']['sha256'])
subprocess.run(['xdelta3','-d','-s',str(BASE),str(PATCH),str(WORK/PKG)],check=True)
for name in CONFIG['assets']:
 if name!=PKG:
  (WORK/name).write_bytes((D/name).read_bytes())
for name,expected in CONFIG['assets'].items():
 p=WORK/name;assert p.stat().st_size==expected['size'] and sha(p)==expected['sha256'],name
for name in ('update-key.pub','rauc-cert.crt','release-notes.md'):
 assert sha(D/name)==CONFIG['transport'][name],name
for name in (PKG,'SHA256SUMS'):
 subprocess.run(['openssl','pkeyutl','-verify','-pubin','-inkey',str(D/'update-key.pub'),'-rawin','-in',str(WORK/name),'-sigfile',str(WORK/(name+'.sig'))],check=True)
checks={line.split('  ')[1]:line.split('  ')[0] for line in (WORK/'SHA256SUMS').read_text().splitlines()}
assert checks=={name:CONFIG['assets'][name]['sha256'] for name in (PKG,PKG+'.sig')}
conf=WORK/'system.conf'
conf.write_text('[system]\ncompatible=gaia-debian13-amd64-ab-v1\nbootloader=noop\nbundle-formats=verity\n[keyring]\npath='+str((D/'rauc-cert.crt').resolve())+'\ncheck-purpose=codesign\n')
info=json.loads(subprocess.check_output(['rauc','info','--conf='+str(conf),'--output-format=json',str(WORK/PKG)],text=True))
assert (info['compatible'],info['version'],info['build'])==('gaia-debian13-amd64-ab-v1',VERSION,SOURCE)
assert info['images'][0]['rootfs']['checksum']==CONFIG['rootfs_sha256']
H={'Authorization':'Bearer '+os.environ['GITHUB_TOKEN'],'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'GaiaOS-One-Time-Signed-System-Upload'}
def req(url,data=None,method='GET',binary=False):
 h=dict(H)
 if data is not None:
  h['Content-Type']='application/octet-stream' if binary else 'application/json'
  if binary:h['Content-Length']=str(os.fstat(data.fileno()).st_size)
  else:data=json.dumps(data).encode()
 with urllib.request.urlopen(urllib.request.Request(url,data=data,headers=h,method=method),timeout=180) as r:return json.load(r)
rel=req(API+'/releases/'+str(CONFIG['draft_id']))
assert rel['tag_name']=='v'+VERSION and rel['draft'] and rel['prerelease'] and not rel['assets']
assert rel['body']==(D/'release-notes.md').read_text()
for name,expected in CONFIG['assets'].items():
 with (WORK/name).open('rb') as f:asset=req('https://uploads.github.com/repos/t4kas/GaiaOS-Releases/releases/'+str(rel['id'])+'/assets?name='+name,f,'POST',True)
 assert asset['size']==expected['size'],name
 if asset.get('digest'):assert asset['digest']=='sha256:'+expected['sha256'],name
req(API+'/releases/'+str(rel['id']),{'draft':False},'PATCH')
for name,expected in CONFIG['assets'].items():
 url='https://github.com/t4kas/GaiaOS-Releases/releases/download/v'+VERSION+'/'+name
 for attempt in range(10):
  try:
   size=0;digest=hashlib.sha256()
   with urllib.request.urlopen(url,timeout=180) as r:
    while block:=r.read(1024*1024):digest.update(block);size+=len(block)
   break
  except urllib.error.HTTPError:time.sleep(3)
 else:raise SystemExit('Anonymous verification unavailable: '+name)
 assert (size,digest.hexdigest())==(expected['size'],expected['sha256']),name
 print('verified',name,size,flush=True)
