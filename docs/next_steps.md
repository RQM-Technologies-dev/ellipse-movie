# Next Steps

This is the current working checklist after adding the Eros Market continuous sequence plan and project visual-direction note on `main`.

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
- Human adaptation decisions applied: no Act II framing, wordless Overture, augmented Teacher explanation, bittersweet Captain translation, and full/expanded Eros market.
- Eros Market continuous sequence plan added under `adaptation/sequences/`.
- Project-wide visual direction added under `docs/visual_direction.md`.

## Immediate next tasks

1. Mark approved scene YAML files from `reviewed` to `locked`.
2. After scenes are locked, begin Act I shot-list generation under `production/shotlists/`.
3. Use `docs/visual_direction.md` as the blocking, camera-angle, and storyboard north star.

## Hold until lock

Do not start storyboard prompts, video prompts, or generated media until:

- scene statuses are locked,
- character and location IDs remain stable after review,
- Aura / Einai / Ousia continuity remains confirmed,
- the Portara ending is confirmed as the film endpoint.

## Recommended next commit

`Lock reviewed Act I scene YAML files`

Expected output:

- Approved `adaptation/scenes/CH##_SC##.yaml` statuses move from `reviewed` to `locked`.
- Treatment, beat sheet, and Eros sequence plan remain aligned with the locked scene sequence.
- Shot-list generation can begin after lock.

Run validation afterward:

```bash
python tools/scripts/validate_yaml.py
```
