# Next Steps

This is the current working checklist after drafting the remaining visual-anchor storyboard prompts on `main`.

## Completed

- Act I scene YAML files are locked.
- Eros Market continuous sequence is locked and covered by a sequence shot list.
- Shot lists exist for all locked scenes or are covered by the Eros Market sequence.
- Act I shot-list conventions have been added.
- Act I shot-list review record has been added.
- Shot-list index records the shot-list layer as reviewed.
- Storyboard prompt README added under `production/storyboards/`.
- Storyboard prompt schema added.
- Act I storyboard prompt index added.
- First-pass storyboard prompt files started from reviewed shot lists.
- Visual-anchor storyboard prompts drafted for Overture, Rain of Lights, Aura's emergence, Stars over the Elgia, Cottage Creation, Cosmic Transit, Garden of Time, Portara, Father and Son at the Gate, and the Eros Market sequence.

## Immediate next tasks

1. Review the visual-anchor storyboard prompts against `docs/visual_direction.md`.
2. Generate storyboard prompts for the remaining scene shot lists.
3. Review all storyboard prompts for continuity, camera language, and storyboard usability.
4. Keep video prompts and generated media downstream of storyboard prompt review.

## Hold until storyboard prompt review

Do not start video prompts or generated media until:

- storyboard prompts are generated from reviewed shot lists,
- storyboard prompts are reviewed against `docs/visual_direction.md`,
- character and location IDs remain stable,
- visual continuity for Aura / Einai / Ousia, rain of lights, Eros, the Kingdom, and the Portara is confirmed.

## Recommended next commit

`Generate remaining Act I storyboard prompts`

Expected output:

- storyboard prompt files for the remaining scene shot lists,
- updated `production/storyboards/act_i_storyboard_prompt_index.yaml`,
- no video prompts until storyboard prompt review is complete.

Run validation afterward:

```bash
python tools/scripts/validate_yaml.py
```
