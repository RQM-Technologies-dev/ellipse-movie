# Next Steps

This is the current working checklist after locking the Act I scene YAML files and beginning Act I shot-list generation on `main`.

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

## Immediate next tasks

1. Continue generating scene shot lists under `production/shotlists/scenes/`.
2. Prioritize major visual anchors: Rain of Lights, Aura Appears, Stars over the Elgia, The Teacher/Athenaeum, Cottage Creation, Cosmic Transit, Garden of Time, Portara.
3. Review the drafted Eros Market sequence shot list for continuous-motion logic.
4. After shot lists are reviewed, begin storyboard prompt planning.

## Hold until shot-list review

Do not start storyboard prompts, video prompts, or generated media until:

- shot lists exist for all locked scenes,
- shot lists are reviewed against `docs/visual_direction.md`,
- character and location IDs remain stable,
- visual continuity for Aura / Einai / Ousia, rain of lights, Eros, the Kingdom, and the Portara is confirmed.

## Recommended next commit

`Generate Act I shot lists for major visual anchors`

Expected output:

- `production/shotlists/scenes/CH03_SC02_shotlist.yaml`
- `production/shotlists/scenes/CH03_SC03_shotlist.yaml`
- `production/shotlists/scenes/CH06_SC03_shotlist.yaml`
- `production/shotlists/scenes/CH08_SC04_shotlist.yaml`
- `production/shotlists/scenes/CH09_SC03_shotlist.yaml`
- `production/shotlists/scenes/CH11_SC03_shotlist.yaml`
- `production/shotlists/scenes/CH11_SC04_shotlist.yaml`

Run validation afterward:

```bash
python tools/scripts/validate_yaml.py
```
