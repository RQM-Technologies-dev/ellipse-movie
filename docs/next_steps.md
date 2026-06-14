# Next Steps

This is the current working checklist after adding a more detailed storyboard art-generation methodology based on the uploaded storyboard reference frames.

## Completed

- Act I scene YAML files are locked.
- Eros Market continuous sequence is locked and covered by a sequence shot list.
- Shot lists exist for all locked scenes or are covered by the Eros Market sequence.
- Act I shot-list review record has been added.
- Storyboard prompt V1 framework was started.
- Uploaded storyboard reference frames were reviewed for style and methodology.
- Detailed storyboard art-generation methodology has been added.
- Storyboard prompt V2 schema has been added.
- Storyboard prompt index now marks existing prompt sets as needing V2 upgrade before image generation.

## Immediate next tasks

1. Upgrade the existing visual-anchor storyboard prompt files to V2 detail level.
2. Generate a new example storyboard deck using the V2 methodology.
3. Review whether the new deck matches the uploaded reference style: detailed black-and-white production boards with high environmental detail and readable cinematic staging.
4. Generate remaining scene storyboard prompts only after the V2 method is approved.

## Hold until V2 storyboard review

Do not start video prompts or generated media until:

- V2 storyboard prompts are generated from reviewed shot lists,
- V2 example boards are reviewed against the uploaded storyboard reference methodology,
- storyboard prompts are reviewed against `docs/visual_direction.md`,
- character and location IDs remain stable,
- visual continuity for Aura / Einai / Ousia, rain of lights, Eros, the Kingdom, and the Portara is confirmed.

## Recommended next commit

`Upgrade visual-anchor storyboard prompts to V2 detail`

Expected output:

- V2-upgraded prompt files for the existing visual-anchor prompt sets,
- detailed black-and-white production-board methodology applied consistently,
- a new pageable example storyboard deck generated from V2 prompts.

Run validation afterward:

```bash
python tools/scripts/validate_yaml.py
```
