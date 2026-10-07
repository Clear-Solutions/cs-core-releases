"""Validate distribution manifests and checksum catalogs without executing assets."""
import hashlib,json,re
from pathlib import Path
from check_agents import validate
root=Path(__file__).resolve().parents[1]
validate(root)
for manifest in sorted((root/'releases').glob('*/manifest.json')):
 data=json.loads(manifest.read_text())
 assert data['version']==manifest.parent.name and re.fullmatch(r'v\d+\.\d+\.\d+',data['version'])
 assert re.fullmatch(r'[a-f0-9]{40}',data['source_commit'])
 names=set();lines=[]
 for asset in data['assets']:
  assert Path(asset['name']).name==asset['name'] and asset['name'] not in names
  names.add(asset['name']);assert asset['size']>0 and re.fullmatch(r'[a-f0-9]{64}',asset['sha256'])
  lines.append(asset['sha256']+'  '+asset['name'])
 assert len(names)==5, 'Initial release must preserve all five upstream installers'
 assert (manifest.parent/'SHA256SUMS').read_text()=='\n'.join(lines)+'\n'
print('PASS: agent policy, source provenance and release checksum catalog')
