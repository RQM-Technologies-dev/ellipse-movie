"""
expand_scene_inventory.py

Expands adaptation/scenes/act_i_scene_inventory.yaml into one YAML file per
scene. This script is intentionally conservative: it does not infer new story
content, and it skips existing scene files unless --overwrite is supplied.

Usage:
    python tools/scripts/expand_scene_inventory.py
    python tools/scripts/expand_scene_inventory.py --overwrite
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - user-facing dependency guard
    print("ERROR: PyYAML is not installed. Run: pip install PyYAML")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parents[2]
INVENTORY_PATH = REPO_ROOT / "adaptation" / "scenes" / "act_i_scene_inventory.yaml"
SCENES_DIR = REPO_ROOT / "adaptation" / "scenes"

SCENE_FIELD_ORDER = [
    "scene_id",
    "chapter",
    "title",
    "location",
    "time_of_day",
    "characters",
    "scene_purpose",
    "emotional_turn",
    "plot_turn",
    "summary",
    "key_dialogue",
    "props",
    "continuity_notes",
    "adaptation_notes",
    "status",
]

DEFAULTS: dict[str, Any] = {
    "time_of_day": "",
    "characters": [],
    "scene_purpose": "",
    "emotional_turn": "",
    "plot_turn": "",
    "summary": "",
    "key_dialogue": "",
    "props": [],
    "continuity_notes": "",
    "adaptation_notes": "",
    "status": "draft",
}


def ordered_scene(scene: dict[str, Any]) -> dict[str, Any]:
    """Return a schema-ordered scene dictionary with missing fields filled."""
    scene_id = scene.get("scene_id")
    if not scene_id:
        raise ValueError(f"Scene is missing scene_id: {scene}")

    output: dict[str, Any] = {}
    for field in SCENE_FIELD_ORDER:
        if field in scene:
            output[field] = scene[field]
        elif field in DEFAULTS:
            output[field] = DEFAULTS[field]
        else:
            output[field] = ""
    return output


def load_inventory(path: Path) -> list[dict[str, Any]]:
    """Load the consolidated inventory file."""
    if not path.exists():
        raise FileNotFoundError(f"Scene inventory not found: {path}")

    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}

    scenes = data.get("scenes")
    if not isinstance(scenes, list):
        raise ValueError("Inventory must contain a top-level 'scenes' list.")
    return scenes


def write_scene_files(scenes: list[dict[str, Any]], overwrite: bool = False) -> tuple[int, int]:
    """Write one YAML file per scene. Returns (created_or_updated, skipped)."""
    SCENES_DIR.mkdir(parents=True, exist_ok=True)
    written = 0
    skipped = 0

    for raw_scene in scenes:
        scene = ordered_scene(raw_scene)
        scene_id = scene["scene_id"]
        output_path = SCENES_DIR / f"{scene_id}.yaml"

        if output_path.exists() and not overwrite:
            print(f"SKIP existing: {output_path.relative_to(REPO_ROOT)}")
            skipped += 1
            continue

        content = yaml.safe_dump(scene, sort_keys=False, allow_unicode=True, width=1000)
        output_path.write_text(content, encoding="utf-8")
        print(f"WRITE: {output_path.relative_to(REPO_ROOT)}")
        written += 1

    return written, skipped


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Expand consolidated Act I scene inventory into per-scene YAML files.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing scene YAML files.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    scenes = load_inventory(INVENTORY_PATH)
    written, skipped = write_scene_files(scenes, overwrite=args.overwrite)
    print(f"\nScene expansion complete: {written} written, {skipped} skipped.")


if __name__ == "__main__":
    main()
