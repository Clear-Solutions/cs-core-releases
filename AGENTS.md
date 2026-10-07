# easySTT public distribution

This public repository distributes easySTT installers. Product source remains private
in Clear-Solutions/cs-project-easystt. Do not copy private source, credentials,
internal reports or production data here. Codex, Cursor, Claude Code and Antigravity
load this canonical file. Read the exact pinned policy in docs/policy and
.clear-solutions/project.json; do not silently update its SHA.

## Work and validation

Use make setup, make check and make security. tools/check_release.py validates
manifest/checksum consistency offline. Installers are release assets, never Git files.
The first release preserves upstream v0.1.3 byte for byte; its provenance is recorded.
Do not describe upstream binaries as built or tested by our new CI. New versions
must come from successful native CI for their exact source revision. Publishing
requires a concrete verified artifact set and existing owner authorization.

Read README.md, docs/deployment.md and docs/agent-workflow.md. Keep README, release
manifests, download URLs, Hub catalog and showcase synchronized when publishing.
Use feature branches and PRs, one independent human review, checks and security.
Do not bypass protection, force-push or replace existing release assets. Preserve
unrelated changes. Never execute incoming installers to verify their checksums.
