# Next Steps

This is the current working checklist after preparing the Act I storyboard prompt layer on `main`.

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

## Immediate next tasks

1. Draft the remaining visual-anchor storyboard prompt files:
   - `CH06_SC03_storyboard_prompts.yaml`
   - `CH08_SC04_storyboard_prompts.yaml`
   - `CH09_SC03_storyboard_prompts.yaml`
   - `CH10_SC03_storyboard_prompts.yaml`
   - `CH11_SC03_storyboard_prompts.yaml`
   - `CH11_SC04_storyboard_prompts.yaml`
2. Generate storyboard prompts for the remaining scene shot lists after the visual anchors are complete.
3. Review storyboard prompts against `docs/visual_direction.md`.
4. Keep video prompts and generated media downstream of storyboard prompt review.

## Hold until storyboard prompt review

Do not start video prompts or generated media until:

- storyboard prompts are generated from reviewed shot lists,
- storyboard prompts are reviewed against `docs/visual_direction.md`,
- character and location IDs remain stable,
- visual continuity for Aura / Einai / Ousia, rain of lights, Eros, the Kingdom, and the Portara is confirmed.

## Recommended next commit

`Draft remaining visual-anchor storyboard prompts`

Expected output:

- first-pass storyboard prompts for Stars over the Elgia,
- Cottage Creation,
- Cosmic Transit,
- Garden of Time,
- Portara,
- Father and Son at the Gate.

Run validation afterward:

```bash
python tools/scripts/validate_yaml.py
```
