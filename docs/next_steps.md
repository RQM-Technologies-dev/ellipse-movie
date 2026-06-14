# Next Steps

This is the current working checklist after merging the Act I preproduction foundation onto `main`.

## Completed

- Repository scaffold created.
- Raw Act I manuscript imported.
- Act I movement split completed.
- Source manifest added.
- Chapter/movement map added.
- Consolidated Act I scene inventory added.
- First-pass Act I story bible added.
- Timeline and continuity notes populated.
- Act I treatment draft added.
- Act I beat sheet draft added.

## Immediate next tasks

1. Run `python tools/scripts/expand_scene_inventory.py` to create one YAML file per Act I scene.
2. Review the generated scene files against the manuscript before marking any scene `locked`.
3. Convert `story/act_i_story_bible.md` into individual character, location, and lore YAML files.
4. Produce the clean manuscript layer under `manuscript/clean/` without changing `manuscript/full_text.md`.
5. Update `adaptation/treatment.md` and `adaptation/beat_sheet.md` after the clean source and scene files are reviewed.

## Hold until review

Do not start shot lists, storyboard prompts, video prompts, or generated media until:

- scene boundaries are approved,
- character and location IDs are stable,
- Aura / Einai / Ousia continuity is confirmed,
- Portara / Act II handoff is clarified.

## Recommended next commit

`Expand Act I scene inventory into per-scene YAML files`

Expected output:

- `adaptation/scenes/CH01_SC01.yaml`
- `adaptation/scenes/CH02_SC01.yaml`
- ...
- `adaptation/scenes/CH11_SC04.yaml`

Run validation afterward:

```bash
python tools/scripts/validate_yaml.py
```
