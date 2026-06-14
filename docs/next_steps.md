# Next Steps

This is the current working checklist after updating the Act I treatment and beat sheet from the reviewed scene YAML files on `main`.

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
- Act I treatment and beat sheet updated from reviewed scene YAML.

## Immediate next tasks

1. Perform a final human review of the filled scene YAML files, treatment, and beat sheet.
2. Resolve the remaining adaptation questions in `adaptation/beat_sheet.md`.
3. Mark approved scene YAML files from `reviewed` to `locked`.
4. After scenes are locked, begin Act I shot-list generation under `production/shotlists/`.

## Hold until lock

Do not start storyboard prompts, video prompts, or generated media until:

- scene statuses are locked,
- character and location IDs remain stable after review,
- Aura / Einai / Ousia continuity remains confirmed,
- Portara / Act II handoff is clarified.

## Recommended next commit

`Lock reviewed Act I scene YAML files after human approval`

Expected output:

- Approved `adaptation/scenes/CH##_SC##.yaml` statuses move from `reviewed` to `locked`.
- Any scene-boundary edits from human review are applied.
- Treatment and beat sheet remain aligned with the locked scene sequence.

Run validation afterward:

```bash
python tools/scripts/validate_yaml.py
```
