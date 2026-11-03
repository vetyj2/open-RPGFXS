#!/usr/bin/env python3
"""Build a compact, derived index without changing the original asset package."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT
OUTPUT = ROOT / "asset-index.json"


def read(path):
    return json.loads((PACKAGE / path).read_text(encoding="utf-8"))


def main():
    manifest = read("doc/manifest.json")
    index = {
        "schema": "open-rpgfxs.asset-index/1",
        "description": "Derived navigation index; original sidecars are authoritative.",
        "paths_relative_to": ".",
        "categories": manifest["categories"],
        "animations": [],
        "sounds": [],
        "pairings": [],
    }
    for code, path in sorted(manifest["animations"].items()):
        a = read(path)
        index["animations"].append({
            "code": code, "name_ko": a["name_ko"], "category": a["category"],
            "file": a["file"], "metadata": path, "thumbnail": a["thumbnail"],
            "game_level": a["game_level"], "concepts": a["concepts"],
            "pairings": a["pairings"],
        })
    for code, path in sorted(manifest["audio"].items()):
        a = read(path)
        index["sounds"].append({
            "code": code, "name_ko": a["name_ko"], "file": a["file"],
            "metadata": path, "duration_ms": a["metrics"]["duration_ms"],
            "concepts": a["concepts"], "usage_levels": a["usage_levels"],
            "pairings": a["pairings"],
        })
    for code, path in sorted(manifest["pairings"].items()):
        p = read(path)
        index["pairings"].append({
            "code": code, "source_id": p["source_id"], "name_ko": p["name_ko"],
            "metadata": path, "animation": p["animation"], "sheet": p["sheet"],
            "level": p["level"], "role": p["role"],
            "sounds": [route["audio"] for route in p["routes"]],
        })
    OUTPUT.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)}: {len(index['animations'])} animations, "
          f"{len(index['sounds'])} sounds, {len(index['pairings'])} pairings")


if __name__ == "__main__":
    main()
