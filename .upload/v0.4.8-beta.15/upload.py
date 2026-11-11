"""One-time transfer of an already locally built, signed and verified system bundle."""
import hashlib,json,os,subprocess,tempfile,time,urllib.error,urllib.request
from pathlib import Path
CONFIG = {'draft_id': 441994458, 'assets': {'gaia-system-0.4.8-beta.15-x86_64.raucb': {'size': 1240552685, 'sha256': '59dc4e514242a364dbd71a53ebb0b5fa87ac6fbe7fe24a56639ae98e8ff336c8'}, 'gaia-system-0.4.8-beta.15-x86_64.raucb.sig': {'size': 64, 'sha256': '163bd66a4beb0dea12f3d476cdd31a92a863fed92973836da0f27143d6fb80fa'}, 'SHA256SUMS': {'size': 214, 'sha256': '3f7ab75f8147ca451346ee1a2e413437828ed807cf2131ef21ec038027d03e82'}, 'SHA256SUMS.sig': {'size': 64, 'sha256': '87ab7d3c8b863fcbcab2e7d43999e883bd6184b708106d3a6d1d88126dacca6e'}}, 'chunks': [{'name': '0000.part', 'size': 47185920, 'sha256': '60ae4594d7d0e6535be2041c03fb5f9d027c14fe69f2e7c707d40efcf8ee4a8e'}, {'name': '0001.part', 'size': 47185920, 'sha256': '6a06943a26f88c839854843bd0a97c53b912a315aa48bb1a9eaac35c97cdac55'}, {'name': '0002.part', 'size': 47185920, 'sha256': '87bd7012b7df46282bf0d8eb5e6f83367ac7627c2dbd665c10e61c962b6ba8ce'}, {'name': '0003.part', 'size': 47185920, 'sha256': '8d80d19399ed921aa03f4bab35f1d7bbf7797b79ba3ca6a76acb1325e149478f'}, {'name': '0004.part', 'size': 47185920, 'sha256': '5b7724aa16e0c9a255142a4fdb7282a1ab3c2224c7161233f8d473aa40735d7c'}, {'name': '0005.part', 'size': 47185920, 'sha256': '5cbb047c6c75d1e11e0d8c2adf4846404fc0495427b063dce16d058692c354d7'}, {'name': '0006.part', 'size': 47185920, 'sha256': '0757319bf758c6aac2be881eadd89ed0ae2b821290d33841a7e24c53480992f2'}, {'name': '0007.part', 'size': 47185920, 'sha256': 'dc41edccaf28f4c530df64953b3bded841e610a3aeffb721a17299d2f230943f'}, {'name': '0008.part', 'size': 47185920, 'sha256': 'c525b5e04e8547f57eb8eb30a46dfe3b444cec8d198ef6939e549bf0a4bc1693'}, {'name': '0009.part', 'size': 47185920, 'sha256': '41702f56854dc0f36c11dcd32c0aaa0985153d90e396c4bc9935e4050cef1c06'}, {'name': '0010.part', 'size': 47185920, 'sha256': '0904813afa7361e50cb5cd43130c43d78f8a98bf1a62af568b25e2eb352204ef'}, {'name': '0011.part', 'size': 47185920, 'sha256': 'da0e06434e7ad374e52a0735dfe91ef46b4ff6f404d3c03177e5abfceafba947'}, {'name': '0012.part', 'size': 47185920, 'sha256': '9cb7ffbda13c3a8087ab72c52c54a860c1329013aaaf59948f55e50705b1c321'}, {'name': '0013.part', 'size': 47185920, 'sha256': 'baed639ad781682f475a6101bfd62be76590e449dfab1b09bc68f198e7a1c0f5'}, {'name': '0014.part', 'size': 47185920, 'sha256': 'f0d75d1823835b9150781a99845dbb2aacaa6cdc56ce26d13502eca45c4d8c68'}, {'name': '0015.part', 'size': 47185920, 'sha256': 'be5dd4fd69b46570b0811538dd1514bda3a99c88a2a7732d489f51df706de7e3'}, {'name': '0016.part', 'size': 47185920, 'sha256': 'cbbd35fd09ff71574882230012e20f6cee4860c98ae06fd40b3a8f94b8323aee'}, {'name': '0017.part', 'size': 47185920, 'sha256': 'e61eebc2c764c6602ce05cd65a242bd4c69e2df8223b3452dccc9eab45447c1d'}, {'name': '0018.part', 'size': 47185920, 'sha256': '7d5b84afcfbbb4d6b7dd6c776c0704771c0b72a606a8883057a044a2c3ec848a'}, {'name': '0019.part', 'size': 47185920, 'sha256': '8d2c9d295fa9f419df63d2d68a4afb7676b03e92f143c5be76608ad90227c1c0'}, {'name': '0020.part', 'size': 34144794, 'sha256': '66e7e030c1802812ebcebea0f0b1c3b7de08762a67b8a8d0123be171b5b702d9'}], 'rootfs_sha256': 'd24bcad225740170840c99e0c70934a8b83abdf9bcff9c6a566a535551da14c1', 'transport': {'update-key.pub': '8190d99631de9d3cfae4070806dfd8dcc03c12e56a3b7fee47563e6f2b4a84f1', 'rauc-cert.crt': '74128e22f08cbfaf1a735656bf94123e1bc7afbd9fb0b9329511acba03644313', 'release-notes.md': 'a228308bc8d8fd8567566a599f673dd8713cc1a238930c8c616337a6a8f1b538'}, 'base': {'url': 'https://github.com/t4kas/GaiaOS-Releases/releases/download/v0.4.8-beta.14/gaia-system-0.4.8-beta.14-x86_64.raucb', 'size': 1263052014, 'sha256': '9558cc7c67f8de1c9ef4383b26f35ad4f6bec53525596b22cd11bf2984bd81e7'}}
D=Path('.upload/v0.4.8-beta.15')
WORK=Path(tempfile.mkdtemp(prefix='gaia-signed-system13-'))
API='https://api.github.com/repos/t4kas/GaiaOS-Releases'
VERSION='0.4.8-beta.15'; SOURCE='257cbe2c2089627534e4d2ab378349455d47c92d'
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
