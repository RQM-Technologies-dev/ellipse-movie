# Act I Storyboard Prompts

This folder contains storyboard prompt planning for the Ellipse Act I / film adaptation target.

Storyboard prompts are generated from the reviewed shot-list layer, not directly from scene YAML. The prompt layer translates each shot into a visual storyboard instruction while preserving:

- locked scene continuity,
- reviewed shot-list intent,
- project-wide visual direction,
- character and location IDs,
- the Eros Market continuous-sequence design,
- the film endpoint at the Portara.

## Source hierarchy

```text
locked scene YAML
→ reviewed shot list
→ storyboard prompt
→ storyboard image
→ reviewed storyboard
→ video prompt
→ AI video clip
```

Do not generate video prompts or AI media directly from scene YAML or shot lists before storyboard prompt review.

## Current status

- Storyboard prompt schema added.
- Act I storyboard prompt index added.
- First-pass storyboard prompt files started for the Overture, Eros Market sequence, and major visual anchors.

## Global visual direction

All storyboard prompts should follow `docs/visual_direction.md`:

- readable geography before spectacle,
- motivated camera movement,
- emotional clarity,
- kinetic discovery,
- classic adventure scale,
- human anchor before fantasy spectacle,
- no shot-for-shot imitation of any existing film.

## Prompt style

Storyboard prompts should be written for previsualization and blocking, not final image polish. A good prompt should describe composition, camera position, action, emotional purpose, continuity anchors, and what the board must hand off to next.
