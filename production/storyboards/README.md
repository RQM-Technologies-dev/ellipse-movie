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
→ detailed storyboard prompt
→ storyboard image
→ reviewed storyboard
→ video prompt
→ AI video clip
```

Do not generate video prompts or AI media directly from scene YAML or shot lists before storyboard prompt review.

## Current status

- Storyboard prompt V1 schema exists.
- Storyboard prompt V2 schema has been added after reviewing uploaded storyboard reference frames.
- Detailed storyboard art-generation methodology has been added.
- Existing first-pass prompt files should be upgraded to V2 before image generation.

## Global visual direction

All storyboard prompts should follow `docs/visual_direction.md`:

- readable geography before spectacle,
- motivated camera movement,
- emotional clarity,
- kinetic discovery,
- classic adventure scale,
- human anchor before fantasy spectacle,
- no shot-for-shot imitation of any existing film.

## Detailed storyboard art direction

Use `production/storyboards/storyboard_art_generation_methodology.md` for prompt generation. The new target is:

- black-and-white rough pencil/ink production storyboard panels,
- wide cinematic frame,
- high environmental detail,
- visible construction lines,
- layered foreground/midground/background,
- readable character blocking,
- detailed architecture, landscape, props, crowds, or spectacle where relevant,
- no color render,
- no polished concept art,
- no generated text labels inside the image.

## Prompt style

Storyboard prompts should be written for previsualization and blocking, not final image polish. A good prompt should describe composition, camera position, action, emotional purpose, continuity anchors, environment detail, character scale, and what the board must hand off to next.
