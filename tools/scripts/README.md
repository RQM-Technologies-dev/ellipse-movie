# Scripts

Python scripts for automating pipeline steps.

| Script | Description |
|--------|-------------|
| `ingest_manuscript.py` | Verifies `manuscript/full_text.md` exists and prints word/page count |
| `split_chapters.py` | Splits the manuscript into per-chapter files in `manuscript/chapters/` |
| `generate_scene_files.py` | Creates placeholder scene YAML files in `adaptation/scenes/` |
| `validate_yaml.py` | Recursively validates all YAML files in the repository |

Run all scripts from the repository root directory.
