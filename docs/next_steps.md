# Next Steps

This is the current working checklist after producing the clean Act I manuscript layer on `main`.

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
- Act I scene inventory expanded into one YAML file per scene.
- Act I story bible converted into individual character, location, and lore files.
- Clean Act I manuscript layer produced under `manuscript/clean/` without changing the raw manuscript.

## Immediate next tasks

1. Review the generated scene files against the clean manuscript before marking any scene `locked`.
2. Fill each scene YAML with `time_of_day`, `emotional_turn`, `plot_turn`, `summary`, `key_dialogue`, `props`, `continuity_notes`, and `adaptation_notes`.
3. Update `adaptation/treatment.md` and `adaptation/beat_sheet.md` after the clean source and scene files are reviewed.

## Hold until review

Do not start shot lists, storyboard prompts, video prompts, or generated media until:

- scene boundaries are approved,
- character and location IDs are stable,
- Aura / Einai / Ousia continuity is confirmed,
- Portara / Act II handoff is clarified.

## Recommended next commit

`Review and fill Act I scene YAML files`

Expected output:

- Each `adaptation/scenes/CH##_SC##.yaml` has complete scene metadata.
- Scene boundaries are cross-checked against `manuscript/clean/chapters/`.
- Scene statuses move from `draft` to `reviewed` or `locked` only after review.

Run validation afterward:

```bash
python tools/scripts/validate_yaml.py
```
