# Next Steps

This is the current working checklist after generating Act I shot lists for the major visual anchors on `main`.

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

## Immediate next tasks

1. Continue generating the remaining scene shot lists under `production/shotlists/scenes/`.
2. Prioritize connective and threshold scenes next: Aaron wakes under the stars, thought-mirroring panic, Academy entry, Teacher/Athenaeum, Teacher's den, Aaron flees, Make Us a Light, Thousand-Faceted Gem, Kingdom arrival, Meeting Eternity, and Palace of Impossible Rooms.
3. Review drafted shot lists against `docs/visual_direction.md` for motivated camera movement, readable geography, emotional continuity, and classic adventure scale.
4. After all shot lists are drafted and reviewed, begin storyboard prompt planning.

## Hold until shot-list review

Do not start storyboard prompts, video prompts, or generated media until:

- shot lists exist for all locked scenes,
- shot lists are reviewed against `docs/visual_direction.md`,
- character and location IDs remain stable,
- visual continuity for Aura / Einai / Ousia, rain of lights, Eros, the Kingdom, and the Portara is confirmed.

## Recommended next commit

`Generate remaining Act I connective shot lists`

Expected output:

- Shot lists for all remaining `pending` scenes in `production/shotlists/act_i_shotlist_index.yaml`.
- The index updated so every scene is either `drafted` or `covered_by_sequence`.
- No storyboard prompts until shot-list review is complete.

Run validation afterward:

```bash
python tools/scripts/validate_yaml.py
```
