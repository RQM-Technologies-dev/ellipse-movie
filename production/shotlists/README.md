# Shot Lists

This folder contains one YAML file per scene's shot list, based on `shot_schema.yaml`.

## Naming Convention

Files should be named using the scene ID, e.g. `CH01_SC01_shots.yaml`.

## Instructions

1. Complete the scene YAML files in `adaptation/scenes/` first.
2. Create a shot list file for each scene using `shot_schema.yaml` as a template.
3. Number shots sequentially within each scene: `CH01_SC01_SH001`, `CH01_SC01_SH002`, etc.
4. Run `python tools/scripts/validate_yaml.py` to check for parse errors.
