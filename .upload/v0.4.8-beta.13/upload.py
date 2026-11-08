"""One-time transfer of an already locally built, signed and verified system bundle."""
import hashlib,json,os,subprocess,tempfile,time,urllib.error,urllib.request
from pathlib import Path
CONFIG = {'draft_id': 438588677, 'assets': {'gaia-system-0.4.8-beta.13-x86_64.raucb': {'size': 1262339309, 'sha256': 'b96729b43f46920196c130993b602f3dca032dd7191e08ef468463ac365dac8a'}, 'gaia-system-0.4.8-beta.13-x86_64.raucb.sig': {'size': 64, 'sha256': 'b392a50ca09dd1b56e9a646fea9b9918dc09317c2922e4eb1f2259d577572663'}, 'SHA256SUMS': {'size': 214, 'sha256': 'd6a9ea32c617d5c13e9b73f095b028eab03aaddd73b381800d9d7f45907ca591'}, 'SHA256SUMS.sig': {'size': 64, 'sha256': '26a780135bcae4766832f3b8bebef804dbd9ea1802078071ce5d766842e2e105'}}, 'chunks': [{'name': '0000.part', 'size': 33554432, 'sha256': 'd04e39af485b3356bf54a2d7370b1fccda4a9955e7383d800eb8886a1c0b5dfc'}, {'name': '0001.part', 'size': 33554432, 'sha256': '30f77005b1926cbd52216ad1172bbff2e04d307904c96f206ab702d9188f5dc5'}, {'name': '0002.part', 'size': 33554432, 'sha256': '2691c685ea9816b3a3f8601c9fdf8a72adea273a2b5e8917aad69f1a69a167f9'}, {'name': '0003.part', 'size': 33554432, 'sha256': '755fab6dd8ac31029b0b2046b8e9e95893b15a535aad04b3e8cad76fc89d344e'}, {'name': '0004.part', 'size': 33554432, 'sha256': '558373251868f1cb8ec0708876651a21fe4b521eb2529bf53d680248a580e72b'}, {'name': '0005.part', 'size': 33554432, 'sha256': '16a63261a95215a9b7792ab9704f1f6b1bd8ad63a850689e32db5247452b99da'}, {'name': '0006.part', 'size': 33554432, 'sha256': '9a1ef6d49940b1985d1cc7fbd84900e3c2e1acf23aa8c228d50bb5bad646fb6a'}, {'name': '0007.part', 'size': 33554432, 'sha256': '7e54a61b14f28b9dd1390a73e2d3e2fd3519b8fac0b89905447a4f443707207c'}, {'name': '0008.part', 'size': 33554432, 'sha256': '1b4841f2eeee2643e05e7fcc1bbac036f4c0e12b5931d562c5a2ba0f30476a6a'}, {'name': '0009.part', 'size': 33554432, 'sha256': '7a7592624f9e4499e03b4205ae4bcc4875b50839222eac9f225fc471956ae339'}, {'name': '0010.part', 'size': 33554432, 'sha256': '680246cfc1db1b3b21ec0cf68efafbe5d5500f9226d072e1a60da9f0243cf358'}, {'name': '0011.part', 'size': 33554432, 'sha256': '02dd8fd3712c66f11c65e73c54d5fb9fbe502d0a177741173cce09b8c123affe'}, {'name': '0012.part', 'size': 33554432, 'sha256': '749bb5820f0f38a2a2ca5c77f0f19aef9c30141c1325b2cdb7fa172895fa38c8'}, {'name': '0013.part', 'size': 33554432, 'sha256': '9e77767f5e99e0e18abbbcd54dc56a30eb36d4b819966f02a9039f73bbf56d0d'}, {'name': '0014.part', 'size': 33554432, 'sha256': 'c4ded56bb0e392ef9517c3007246ee2d0f1291bc6887758bb59cbab9940c76b6'}, {'name': '0015.part', 'size': 33554432, 'sha256': '78b29d4f1e627695a634ccccdd2e3e0414257db347b52680e457160f3036c36f'}, {'name': '0016.part', 'size': 33554432, 'sha256': '2c29c6e2bdf54d244b925929bcd61e51ce26e1dc2de0f659f95e5d44cebd9660'}, {'name': '0017.part', 'size': 33554432, 'sha256': 'b26b160bb4c0df07f70ff6da418ecab039f3d773999bc26914b60e7b646f9263'}, {'name': '0018.part', 'size': 33554432, 'sha256': '4b2d954a246b9bb1d4ac59c210541dcd951e0d6bf12d7acf2df1ead41bc5dedf'}, {'name': '0019.part', 'size': 33554432, 'sha256': '206786c29a59aa4721fa270b3371aecc63604d26f8594384cba5313ab1bf6600'}, {'name': '0020.part', 'size': 33554432, 'sha256': 'c6347abab3fed361402ddd87a4625e83787ec27ff01afd043a170c0d027bd1b1'}, {'name': '0021.part', 'size': 33554432, 'sha256': 'd6461bbe870bed4276b4fdce047deb7e522c0ce7b11f38ae37cc6682a66db440'}, {'name': '0022.part', 'size': 33554432, 'sha256': '5db6a6a7360d4b35d4f33819ceab2fc2143a558fb1b829304d42a75e3a79a1a5'}, {'name': '0023.part', 'size': 33554432, 'sha256': '54b2cdddf6e1e50c8e62f1c740de9e61c649b85bfb23bf1f1016cb0c9bd228a5'}, {'name': '0024.part', 'size': 33554432, 'sha256': '7a25e581726c658a9969518d679d038b923e7081c4074b529425083fcbf2dd2c'}, {'name': '0025.part', 'size': 33554432, 'sha256': '2dcb565c273ba162e65882f436f443f26d46fa38882103d3e44d2c2406088118'}, {'name': '0026.part', 'size': 33554432, 'sha256': 'c5a0b146a3e97ede4db62c98ffcdb22f79a5a6565267bfedc6783b20c3707fe3'}, {'name': '0027.part', 'size': 33554432, 'sha256': '9881aa182fb1aa1641483402b494aa0f2dcb1b645cd2c7d2efb343754f822ba9'}, {'name': '0028.part', 'size': 33554432, 'sha256': '8230920d8c0399dd469a0684a0a0185e747b3e2ef775720638c738de1c45e2a3'}, {'name': '0029.part', 'size': 33554432, 'sha256': '49208cd8087335731019e70a85e0a1bd0c04987ad843d34dcf04feb19d6f4e20'}, {'name': '0030.part', 'size': 33554432, 'sha256': '8b0fb11ffdd4af532604dcf05a2da3098bb93288cb429d38b0c71b33ea09cb9d'}, {'name': '0031.part', 'size': 33554432, 'sha256': 'fffb8db70a8ad02bd54498785ad966c8ccc1f50d628a6cf737db58136cbfb46a'}, {'name': '0032.part', 'size': 33554432, 'sha256': '27a025f0aadec8f0d27f6cb8dbe90fbd915def7ebb411640e662d5ba8acf7172'}, {'name': '0033.part', 'size': 33554432, 'sha256': 'ee8abd59dc7c46745ad32243a1cbfb8b809c4d1a3a8e466326e6254d696c97d6'}, {'name': '0034.part', 'size': 33554432, 'sha256': '50cb726a103542a15da52434742c0888cd4eec820bfcfe5206f48ab4ae1e4e0b'}, {'name': '0035.part', 'size': 33554432, 'sha256': '231e0844826b6173021c6d414db6c6771b1fe155bbc0fecc1d0f501d226b3059'}, {'name': '0036.part', 'size': 33554432, 'sha256': '6215be029497bdc0f4754a5a8989334b5a5e67bcee20afdcd28f2bcf68839dac'}, {'name': '0037.part', 'size': 20825325, 'sha256': '4c4b4e25bbb534b3189971b0be61d07aace5bdfe865aaa05c8b24259ec7585da'}], 'rootfs_sha256': '7ee58448d7e2430baed8c6b36ede47497523c11913e99d4daf0d8ceb5b571c88', 'transport': {'update-key.pub': '8190d99631de9d3cfae4070806dfd8dcc03c12e56a3b7fee47563e6f2b4a84f1', 'rauc-cert.crt': '74128e22f08cbfaf1a735656bf94123e1bc7afbd9fb0b9329511acba03644313', 'release-notes.md': '0b35833860d9dfd2b251134a2a8d3ee08cb67dcd2384d5efd38e2dcbe352a33f'}}
D=Path('.upload/v0.4.8-beta.13')
WORK=Path(tempfile.mkdtemp(prefix='gaia-signed-system13-'))
API='https://api.github.com/repos/t4kas/GaiaOS-Releases'
VERSION='0.4.8-beta.13'; SOURCE='67f1de12024ca9e0b26047ddd816a519a4f6b3fd'
PKG='gaia-system-'+VERSION+'-x86_64.raucb'
def sha(path):
 with Path(path).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
with (WORK/PKG).open('wb') as out:
 for part in CONFIG['chunks']:
  p=D/'chunks'/part['name']
  assert p.stat().st_size==part['size'] and sha(p)==part['sha256'],part['name']
  with p.open('rb') as f:
   while block:=f.read(1024*1024):out.write(block)
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
