# OPEN-RPGFXS

**CC0 RPG effect sprites and sound effects, ready to use together or independently.** An agent-readable catalogue connects visual effects, sound files, reviewed pairings, timing, gain, and search metadata. No runtime or game engine is required.

**RPG 이펙트 스프라이트와 효과음을 세트 또는 개별 파일로 사용할 수 있는 CC0 에셋 모음입니다.** 에이전트가 검색하고 게임에 적용할 수 있도록 코드, 경로, 프레임 시간, 사운드 재생 시점과 검수 정보를 함께 제공합니다.

| Collection | Contents |
| --- | --- |
| Reviewed pairings | 440 (344 primary, 96 reviewed alternatives) |
| Visuals | 315 transparent sprite sheets and 315 thumbnails |
| Sounds | 246 individual WAV files |
| Formats | PNG sprite sheets; 48 kHz, 16-bit stereo PCM WAV |

The catalogue covers projectiles, physical hits, slashes, elemental impacts, ground effects, environmental effects, healing and protection, status effects, and magic. Counts describe the packaged review snapshot, not a guarantee that every category or level has a matching asset.

## 대표 샘플 / Featured previews

아래 GIF는 GitHub에서 소리 없이 반복 재생됩니다. **소리 포함 MP4**를 열거나 내려받으면 검수된 스프라이트와 사운드를 함께 확인할 수 있습니다. 어두운 배경은 미리보기용이며, 실제 스프라이트는 투명 PNG입니다. Each GIF loops silently; the linked MP4 plays the reviewed pairing with sound. Preview timing is sampled for video; use the source sidecars for exact playback.

### 화살 명중 / Arrow impact

[![화살 명중 이펙트 미리보기](sample/ORFX-01-001-03-P01-preview.gif)](sample/ORFX-01-001-03-P01-preview.mp4)

[소리 포함 MP4](sample/ORFX-01-001-03-P01-preview.mp4) · [스프라이트](spritesheets/01/ORFX-01-001-03.png) · [WAV](audio/01/ORFXS-01-0003.wav) · [조합 정보](pairings/ORFX-01-001-03-P01.json)

### 불 검격 / Fire slash

[![불 검격 이펙트 미리보기](sample/ORFX-03-002-03-P01-preview.gif)](sample/ORFX-03-002-03-P01-preview.mp4)

[소리 포함 MP4](sample/ORFX-03-002-03-P01-preview.mp4) · [스프라이트](spritesheets/03/ORFX-03-002-03.png) · [검격 WAV](audio/03/ORFXS-03-0008.wav) · [불 WAV](audio/01/ORFXS-01-0017.wav) · [조합 정보](pairings/ORFX-03-002-03-P01.json)

### 얼음 파쇄 / Ice shatter

[![얼음 파쇄 이펙트 미리보기](sample/ORFX-04-005-03-P01-preview.gif)](sample/ORFX-04-005-03-P01-preview.mp4)

[소리 포함 MP4](sample/ORFX-04-005-03-P01-preview.mp4) · [스프라이트](spritesheets/04/ORFX-04-005-03.png) · [WAV](audio/04/ORFXS-04-0012.wav) · [조합 정보](pairings/ORFX-04-005-03-P01.json)

### 연속 번개 / Lightning sequence

[![연속 번개 이펙트 미리보기](sample/ORFX-04-009-03-P01-preview.gif)](sample/ORFX-04-009-03-P01-preview.mp4)

[소리 포함 MP4](sample/ORFX-04-009-03-P01-preview.mp4) · [스프라이트](spritesheets/04/ORFX-04-009-03.png) · [WAV 1](audio/04/ORFXS-04-0020.wav) · [WAV 2](audio/04/ORFXS-04-0028.wav) · [WAV 3](audio/04/ORFXS-04-0026.wav) · [조합 정보](pairings/ORFX-04-009-03-P01.json)

### 회복 / Healing

[![회복 이펙트 미리보기](sample/ORFX-07-002-03-P01-preview.gif)](sample/ORFX-07-002-03-P01-preview.mp4)

[소리 포함 MP4](sample/ORFX-07-002-03-P01-preview.mp4) · [스프라이트](spritesheets/07/ORFX-07-002-03.png) · [WAV](audio/07/ORFXS-07-0014.wav) · [조합 정보](pairings/ORFX-07-002-03-P01.json)

샘플 메타데이터: [sample/manifest.json](sample/manifest.json). 전체 목록은 아래의 색인과 로컬 미리보기에서 확인할 수 있습니다.

## License / 라이선스

The project publisher dedicates this repository's assets, metadata, documentation, and tools to the public domain under [CC0 1.0 Universal](LICENSE), to the extent possible under applicable law. You may copy, modify, combine and redistribute them, including in commercial projects. Credit is appreciated but **not required**. A sprite or sound may be used on its own; using its paired counterpart is not required. See the [CC0 legal code](LICENSE) for the full terms.

이 저장소의 에셋·메타데이터·문서·도구는 **CC0 1.0**으로 공개합니다. 상업적 이용, 수정, 재배포가 가능하며 출처 표기는 의무가 아닙니다. 이미지와 사운드는 각각 따로 사용할 수 있습니다. 검수 및 재사용 관련 메타데이터는 제작 당시의 적합성 기록이며 별도의 라이선스 조건이 아닙니다.

## Browse and preview

Download the repository or browse individual files in the folders below. The assets themselves are in the repository; no separate release download is needed. Open [`index.html`](index.html) locally to search and preview. For local playback, use the page's package-folder chooser and select the repository folder containing `audio/` and `spritesheets/`. The preview works offline and does not upload your files.

For the full Korean usage guide, see [`USAGE.ko.md`](USAGE.ko.md). A Korean guide to manually publishing the repository is available in [`PUBLISHING.ko.md`](PUBLISHING.ko.md).

## Find a set or a single asset

All paths stored in the package and [`asset-index.json`](asset-index.json) are relative to the repository root. The compact index lists names, concepts, individual file paths and related pairings; its entries are derived from the authoritative package sidecars. Resolve an original ID with [`package-code-map.json`](doc/package-code-map.json); use [`manifest.json`](doc/manifest.json) to map an `ORFX` animation, `ORFXS` sound or pairing ID to its JSON sidecar. That sidecar identifies the actual PNG or WAV in its `file` field.

For example, original ID `rpg-01-l50` maps to:

| Use | File |
| --- | --- |
| Reviewed set | [`ORFX-01-001-03-P01.json`](pairings/ORFX-01-001-03-P01.json) |
| Sprite | [`ORFX-01-001-03.png`](spritesheets/01/ORFX-01-001-03.png) and [animation metadata](spritesheets/01/ORFX-01-001-03.json) |
| Sound | [`ORFXS-01-0003.wav`](audio/01/ORFXS-01-0003.wav) and [audio metadata](audio/01/ORFXS-01-0003.json) |

For a sprite alone, import its PNG and use its sidecar's frame rectangles and durations. For a sound alone, import the WAV and set its level for your mix; the audio is not peak-normalized. The sidecar's reviewed uses are examples, not a requirement to use the sound with those sprites. A sound may be reused by several pairings without duplicating its file.

To reproduce a reviewed set, schedule **each** `routes[]` entry using its `start_ms` and linear `gain`. A negative start requires audio pre-roll. The WAV already has the recorded crop and fades baked in; do not apply them again. Let the sound's tail finish. For the sprite, use `frames[]` in order, including each `duration_ms`, with nearest filtering and pivot `[192,192]`. Do not play empty sheet cells or assume a universal FPS. Some sounds already contain a complete multi-hit sequence and should be played once per route.

## Agent quick start

Read [`AGENTS.md`](AGENTS.md), then run from the repository root using Python 3 and its standard library:

```sh
python3 tools/recommend.py --pairing rpg-01-l50 --top 8
python3 tools/recommend.py --query "얼음 충돌" --level 99 --top 8
python3 tools/recommend.py --query "ice impact" --exclude fire --top 8
python3 tools/validate.py
```

The recommendation tool ranks **sounds** using metadata and returns paths relative to the package. Its suggested replacements are heuristics: audition them and check timing and mixture headroom. Negative wording is not automatically parsed; use `--exclude` for explicit excluded concepts. Reviewed alternatives and recommendations are different kinds of evidence. See [`recommendation-method.md`](doc/recommendation-method.md) for the scoring and playback contract.

## Repository layout

```text
LICENSE                         CC0 1.0 legal code
AGENTS.md                       Entry point for consuming agents
asset-index.json                Compact index of assets and reviewed sets
tools/build-asset-index.py      Rebuild the derived index
index.html                      Offline browser and preview
sample/                         Animated GIF and sound-enabled MP4 previews
spritesheets/<category>/        PNG + animation JSON and notes
audio/<category>/               WAV + audio JSON and notes
thumbnails/<category>/          Transparent previews
pairings/                       Reviewed sets and route timing
doc/                            Manifests, search data, integrity and review records
tools/                          Offline recommendation and integrity validation
```

The published package was selected from the final review exported at `2026-11-03T21:12:07.925Z`; omitted candidates are recorded separately. See [PROVENANCE.md](PROVENANCE.md) for production and packaging details and [CONTRIBUTING.md](CONTRIBUTING.md) for corrections.
