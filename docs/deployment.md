# Release delivery and rollback

The public release repository keeps installer assets separate from private source.
The initial v0.1.3 import is byte-for-byte from the owner's existing public release;
all five SHA-256 values and sizes are checked against GitHub asset metadata before
upload. The public release tag identifies this distribution manifest commit.
The actual product source revision is manifest.source_commit; GitHub-generated
source archives here contain distribution documentation, not the product source.

For each future version, obtain installers from successful native CI on the private
source repository, record exact SHA/run/artifact identity, verify checksums, create
a new version manifest and pass CI. Publish that verified set using an authorized
maintainer's gh CLI or scoped release credential. Cross-repository automatic asset
publication is not configured; the existing private CD produces verified artifacts.
Do not embed credentials in workflows or distribute an unverified local build.

Catalog CD archives verified main and SHA256SUMS after CI; it does not build/install
applications. A bad release is withdrawn and latest is set to the previous verified
release; never silently overwrite versioned assets. Preserve published provenance.
Main requires checks/security and an independent PR approval; owners retain bypass
for explicitly authorized maintenance only.

All products have separate products/<slug>/releases/<version> directories and tags.
Latest is tracked per product; rollback updates that product's metadata, README
and showcase link to its previous verified tag, not the global latest marker.
