# Next Steps

This is the current working checklist after expanding the Act I scene inventory onto `main`.

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

## Immediate next tasks

1. Review the generated scene files against the manuscript before marking any scene `locked`.
2. Convert `story/act_i_story_bible.md` into individual character, location, and lore YAML files.
3. Produce the clean manuscript layer under `manuscript/clean/` without changing `manuscript/full_text.md`.
4. Update `adaptation/treatment.md` and `adaptation/beat_sheet.md` after the clean source and scene files are reviewed.

## Hold until review

Do not start shot lists, storyboard prompts, video prompts, or generated media until:

- scene boundaries are approved,
- character and location IDs are stable,
- Aura / Einai / Ousia continuity is confirmed,
- Portara / Act II handoff is clarified.

## Recommended next commit

`Convert Act I story bible into character, location, and lore YAML files`

Expected output:

- `story/characters/CHAR_AARON.yaml`
- `story/characters/CHAR_AURA.yaml`
- ...
- `story/locations/LOC_TARA_WOODS.yaml`
- `story/locations/LOC_PORTARA_CHAMBER.yaml`
- `story/lore/einai_ousia.md`
- `story/lore/portara.md`

Run validation afterward:

```bash
python tools/scripts/validate_yaml.py
```
