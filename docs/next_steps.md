# Next Steps

This is the current working checklist after drafting shot lists for all locked Act I scenes on `main`.

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
- Act I scene YAML files locked.
- Act I shot-list generation started under `production/shotlists/`.
- Major visual-anchor shot lists drafted.
- Remaining Act I connective shot lists drafted.
- Every locked scene now has a drafted scene shot list or is covered by the Eros Market sequence shot list.

## Immediate next tasks

1. Review all drafted shot lists against `docs/visual_direction.md` for motivated camera movement, readable geography, emotional continuity, and classic adventure scale.
2. Normalize any shot-list fields or naming conventions that need tightening before storyboards.
3. Prepare the storyboard prompt layer using the reviewed shot lists as the source of truth.
4. After storyboard prompt planning is reviewed, begin storyboard prompt generation.

## Hold until shot-list review

Do not start storyboard prompts, video prompts, or generated media until:

- shot lists are reviewed against `docs/visual_direction.md`,
- shot-list naming and numbering are stable,
- character and location IDs remain stable,
- visual continuity for Aura / Einai / Ousia, rain of lights, Eros, the Kingdom, and the Portara is confirmed.

## Recommended next commit

`Review and normalize Act I shot lists`

Expected output:

- All drafted shot lists checked for continuity, numbering, and visual-direction alignment.
- `production/shotlists/act_i_shotlist_index.yaml` remains accurate.
- Storyboard prompt planning can begin after review.

Run validation afterward:

```bash
python tools/scripts/validate_yaml.py
```
