# Next Steps

This is the current working checklist after reviewing and filling the Act I scene YAML files on `main`.

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
- Act I scene YAML files reviewed and filled with scene metadata.

## Immediate next tasks

1. Perform a final human review of the filled scene YAML files before changing any scene status from `reviewed` to `locked`.
2. Update `adaptation/treatment.md` and `adaptation/beat_sheet.md` using the filled scene YAML files as the source of truth.
3. After scenes are locked, begin Act I shot-list generation under `production/shotlists/`.

## Hold until lock

Do not start storyboard prompts, video prompts, or generated media until:

- scene statuses are locked,
- character and location IDs remain stable after review,
- Aura / Einai / Ousia continuity remains confirmed,
- Portara / Act II handoff is clarified.

## Recommended next commit

`Update Act I treatment and beat sheet from reviewed scene YAML`

Expected output:

- `adaptation/treatment.md` reflects the reviewed scene sequence.
- `adaptation/beat_sheet.md` reflects the reviewed scene sequence.
- Scene status remains `reviewed` until final approval.

Run validation afterward:

```bash
python tools/scripts/validate_yaml.py
```
