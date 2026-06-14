# Next Steps

This is the current working checklist after reviewing and normalizing Act I shot lists on `main`.

## Completed

- Act I scene YAML files are locked.
- Eros Market continuous sequence is locked and covered by a sequence shot list.
- Shot lists exist for all locked scenes or are covered by the Eros Market sequence.
- Act I shot-list conventions have been added.
- Act I shot-list review record has been added.
- Shot-list index now records the shot-list layer as reviewed.

## Immediate next tasks

1. Prepare the storyboard prompt layer using reviewed shot lists as the source of truth.
2. Create a storyboard prompt schema under `production/storyboards/`.
3. Generate first-pass storyboard prompts from reviewed shot lists.
4. Keep video prompts and generated media downstream of storyboard review.

## Hold until storyboard prompt review

Do not start video prompts or generated media until:

- storyboard prompt schema exists,
- storyboard prompts are generated from reviewed shot lists,
- storyboard prompts are reviewed against `docs/visual_direction.md`,
- character and location IDs remain stable,
- visual continuity for Aura / Einai / Ousia, rain of lights, Eros, the Kingdom, and the Portara is confirmed.

## Recommended next commit

`Prepare Act I storyboard prompt layer`

Expected output:

- `production/storyboards/README.md`
- `production/storyboards/storyboard_prompt_schema.yaml`
- `production/storyboards/act_i_storyboard_prompt_index.yaml`
- first-pass storyboard prompts generated from reviewed shot lists

Run validation afterward:

```bash
python tools/scripts/validate_yaml.py
```
