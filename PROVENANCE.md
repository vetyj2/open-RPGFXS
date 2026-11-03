# Production and package record

OPEN-RPGFXS packages 315 effect sprite sheets, 315 thumbnails, 246 WAV sound assets, and 440 reviewed visual/audio pairings. The selection is based on the review export dated `2026-11-03T21:12:07.925Z`: 344 primary selections and 96 reviewed alternatives. Omitted, unreviewed or changed-after-review candidates are recorded separately in [`doc/omitted-candidates.json`](doc/omitted-candidates.json).

According to the existing package record, the images were extracted from reviewed procedural pixel RGBA work in pixFX studio. Sounds were extracted from Grok-generated video audio and existing studio mixes, using the reviewed crop and fade; pairing gain is stored separately. The project owner directed the work with Codex. These names describe production tools and do not imply authorship or endorsement by their providers. Read the original [production record](doc/PROVENANCE.md) and individual asset sidecars for further details.

Generation prompts are treated as actual prompts only where the sidecar records a SHA-traced prompt; other concepts and factors are metadata interpretations. Automated onset and signal measurements are candidates, not proof of perceived impact. Review decisions and reuse notes capture the selection workflow rather than conditions of the CC0 dedication.

The package includes `doc/integrity.json` with SHA-256 file hashes, excluding that manifest itself. Run `python3 tools/validate.py` from the repository root to check the packaged files. The repository-level public documentation and license were added after the original package was assembled.
