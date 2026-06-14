# Next Steps

This is the current working checklist after converting the Act I story bible into individual production assets on `main`.

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

## Immediate next tasks

1. Produce the clean manuscript layer under `manuscript/clean/` without changing `manuscript/full_text.md`.
2. Review the generated scene files against the clean manuscript before marking any scene `locked`.
3. Fill each scene YAML with `time_of_day`, `emotional_turn`, `plot_turn`, `summary`, `key_dialogue`, `props`, `continuity_notes`, and `adaptation_notes`.
4. Update `adaptation/treatment.md` and `adaptation/beat_sheet.md` after the clean source and scene files are reviewed.

## Hold until review

Do not start shot lists, storyboard prompts, video prompts, or generated media until:

- scene boundaries are approved,
- character and location IDs are stable,
- Aura / Einai / Ousia continuity is confirmed,
- Portara / Act II handoff is clarified.

## Recommended next commit

`Produce clean Act I manuscript layer`

Expected output:

- `manuscript/clean/act_i_clean.md`
- `manuscript/clean/cleanup_log.md`
- `manuscript/clean/chapters/CH01_overture.md`
- ...
- `manuscript/clean/chapters/CH11_ellipse.md`

Run validation afterward:

```bash
python tools/scripts/validate_yaml.py
```
