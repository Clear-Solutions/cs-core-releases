"""Download pinned Linux x86_64 CI tools and verify their release checksums."""

import hashlib
import io
import json
import shutil
import tarfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def install():
    out = ROOT / "work" / "bin"
    out.mkdir(parents=True, exist_ok=True)
    for name, tool in json.loads((ROOT / "policies/tools.json").read_text()).items():
        archive = out / (name + "-" + tool["version"] + ".tar.gz")
        blob = (
            archive.read_bytes()
            if archive.exists()
            else urllib.request.urlopen(tool["url"], timeout=60).read()
        )
        if hashlib.sha256(blob).hexdigest() != tool["sha256"]:
            raise RuntimeError("Checksum mismatch: " + name)
        archive.write_bytes(blob)
        with tarfile.open(fileobj=io.BytesIO(blob)) as tar:
            members = [m for m in tar.getmembers() if m.isfile() and Path(m.name).name == name]
            if len(members) != 1:
                raise RuntimeError("Ambiguous tool archive: " + name)
            member = members[0]
            if not member.isfile() or member.size > 100 * 1024 * 1024:
                raise RuntimeError("Unexpected archive entry: " + name)
            with tar.extractfile(member) as source, (out / name).open("wb") as dest:
                shutil.copyfileobj(source, dest)
        (out / name).chmod(0o755)
        print("Verified " + name + " " + tool["version"])


if __name__ == "__main__":
    install()
