# OPEN-RPGFXS: repository and asset license

The sprites, sounds, metadata, documentation and tools in this repository are dedicated under CC0 1.0. See [LICENSE](LICENSE). Each asset can be used independently, without attribution. Review and reuse notes record suitability, not license conditions.

Start with [asset-index.json](asset-index.json), a compact, derived index of individual PNGs, WAVs and reviewed sets. Paths in the index and package are relative to the repository root. For authoritative playback and review details read the linked sidecars. Rebuild the index with `python3 tools/build-asset-index.py`. The recommendation tool ranks sounds and returns heuristic suggestions; audition substitutions. Natural-language negation is not parsed; use `--exclude` for exclusions.

# OPEN-RPGFXS — consumer agent instructions

1. Read doc/package-code-map.json and doc/manifest.json to resolve exact source IDs, animation codes and audio routes. Paths are relative to the package root. Never invent a missing intensity or resurrect omitted/rejected candidates.
2. Read doc/keyword-map.json and doc/query-catalog.json. Canonicalize Korean/English synonyms; count each concept once. Do not score the same words again in labels and prompts.
3. Run tools/recommend.py for reproducible scores and reasons. Compare all eligible crops, applying source reuse restrictions. Full same-sprite reviewed alternatives are stronger evidence than a heuristic recombination.
4. Read the shortlisted pairing/audio sidecars. A route gain is mandatory; audio is not peak-normalized. Crop/fade are already baked. Do not apply them twice. Reused WAVs stay one file. Different samples or fade envelopes are different assets.
5. Match causal impact or continuous onset, not brightest frame or maximum audio sample. Preserve the approved main-onset delta when replacing a sound. Where onset or impact is a candidate, say so; do not pretend a waveform algorithm understood the sound.
6. Multi-hit schedules and intrinsic full-sequence sounds are different. Inspect slot_patterns and impact_intervals_ms. Never replay an entire multi-hit file for every visual hit. For 4+ attacks prefer the reviewed dedicated sequence or varied individual sources.
7. Stronger sound means material/scale, event structure, reviewed level and signal metrics together. A gain-only alternative is not a new material-scale recording. Keep mixture headroom. Audition every new replacement.
8. Sprite frames are transparent 384x384, pivot 192,192, nearest. Use frames[].duration_ms, including variable durations. Do not repeat unused sheet cells or assume 24FPS universally.
9. Actual generation prompts exist only when SHA-traced in prompt_records. prompt_factors/concepts are metadata interpretations. These are Grok-generated sounds, not asserted field recordings.
10. Consumer feedback must not overwrite packaged human review provenance. Keep proposed replacements separately. tools/validate.py checks portable file integrity and links.
