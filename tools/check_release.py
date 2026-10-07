"""Validate product versions, provenance and checksum catalogs offline."""
import json,re
from pathlib import Path
from check_agents import validate
root=Path(__file__).resolve().parents[1];validate(root)
products=sorted((root/'products').iterdir());assert products
for folder in products:
 product=json.loads((folder/'product.json').read_text());slug=product['id']
 assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',slug) and slug==folder.name
 assert (folder/'README.md').is_file() and product['platforms']
 manifests=sorted((folder/'releases').glob('*/manifest.json'));assert manifests
 for path in manifests:
  data=json.loads(path.read_text());version=data['version']
  assert version==path.parent.name and re.fullmatch(r'v\d+\.\d+\.\d+',version)
  assert data['product']==slug and data['release_tag']==slug+'-'+version
  assert re.fullmatch(r'[a-f0-9]{40}',data['source_commit'])
  assert data['kind'] in ['verified-upstream-release-import','verified-ci-artifacts']
  if data['kind']=='verified-ci-artifacts':assert data['source_run_url'].startswith('https://github.com/')
  names=set();lines=[]
  for asset in data['assets']:
   assert re.fullmatch(r'[a-zA-Z0-9_.-]+',asset['name']) and asset['name'] not in names
   names.add(asset['name']);assert asset['size']>0 and re.fullmatch(r'[a-f0-9]{64}',asset['sha256'])
   lines.append(asset['sha256']+'  '+asset['name'])
  assert names and (path.parent/'SHA256SUMS').read_text()=='\n'.join(lines)+'\n'
 latest=folder/'releases'/product['latest_version']/'manifest.json';assert latest.is_file()
 assert product['latest_tag']==slug+'-'+product['latest_version']
 url='https://github.com/Clear-Solutions/cs-core-releases/releases/tag/'+product['latest_tag']
 assert url in (folder/'README.md').read_text() and url in (root/'README.md').read_text()
print('PASS: policies, categorized products, source provenance, per-product release links and checksums')
