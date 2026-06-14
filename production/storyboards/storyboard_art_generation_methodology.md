# Storyboard Art Generation Methodology

This methodology upgrades the Ellipse storyboard prompt layer so generated boards are closer to detailed production storyboards like the uploaded reference frames.

## Goal

Generate storyboard panels that are useful for blocking, camera planning, and sequencing. The boards should feel like rough professional production boards: detailed, readable, cinematic, and emotionally clear.

The purpose is not final concept art. The purpose is visual direction.

## Core visual style

Use this baseline style for storyboard image generation:

> Detailed black-and-white production storyboard panel, rough pencil and ink linework, clean widescreen cinematic frame, visible construction lines, high environmental detail, clear foreground/midground/background depth, readable character blocking, no color, no polished render, no photorealism, no generated text labels.

## Board anatomy

Each storyboard prompt should specify five layers.

### 1. Frame format

- Widescreen cinematic panel.
- Thin border around drawing area.
- Optional blank white header/slate space above the board.
- No generated text in the image; labels should be added outside the image if needed.

### 2. Camera and geography

- Camera placement: wide, medium-wide, low angle, over-shoulder, close object reveal, etc.
- Lens feel: expansive wide, compressed close, intimate two-shot, towering vertical reveal.
- Readable geography before spectacle.
- Clear direction of movement and handoff to the next board.

### 3. Blocking

- Character positions and silhouettes.
- Foreground, midground, and background roles.
- What the audience should notice first, second, and third.
- How character posture expresses emotion.

### 4. Environment detail

- Use concrete location details from location bible and shot lists.
- Avoid empty backgrounds.
- Include architecture, nature, props, ships, crowds, bookshelves, masts, rails, gates, trees, cliffs, or cosmic structures when relevant.
- Environments should be detailed enough for staging continuity.

### 5. Emotional / sequence handoff

- What feeling must the board communicate?
- What visual element hands off to the next board?
- What should remain unresolved for the next panel?

## Detail-density rules

### Establishing and world-building boards

Use high environment density. The character may be small, but the world must be specific.

Examples: Tara vista, Eros port, Eros market, Academy exterior, Kingdom arrival, Portara chamber.

### Character decision boards

Use moderate environment density. The staging should support the emotional decision.

Examples: Aaron choosing to leave Tara, Aaron confronting Aura, Aaron asking if he will die.

### Object/reveal boards

Use low-to-moderate environment density with a strong object focus.

Examples: gold leaf, Elgia inscription, green Academy textbook, thousand-faceted gem, Garden plaque.

### Spectacle boards

Use high compositional clarity. The fantasy effect can be large, but the human anchor must remain visible.

Examples: Rain of Lights, Aura pulls down the stars, Cottage Creation, Cosmic Transit, Portara crossing.

## Prompt construction template

Use this structure inside the `prompt` field:

```text
Detailed black-and-white production storyboard panel, rough pencil and ink linework, widescreen cinematic frame, [shot subject/action], [foreground], [midground], [background], [environment detail], [character posture/emotion], [camera angle/movement implication], readable geography, high detail, no color.
```

Then use the schema fields to separate:

- `camera`
- `blocking`
- `continuity`
- `emotional_intent`
- `next_handoff`
- `negative_prompt`

## Negative prompt baseline

Use a baseline negative prompt for most boards:

```text
no photorealism, no color render, no polished concept art, no anime style, no modern objects, no generated text labels, no empty background, no copied film still, no abstract composition without readable geography
```

Customize per scene by adding specific exclusions.

## Spielberg-scale visual grammar

The global visual direction remains a broad classic adventure north star: readable geography, emotional clarity, wonder, suspense, motivated camera movement, and kinetic discovery.

For storyboard generation this means:

- show the character seeing before revealing what they see,
- let motion or gaze hand off to the next panel,
- use foreground/midground/background to make the world feel alive,
- stage spectacle around a human emotional anchor,
- keep blocking clear enough that the board could become a shot.

This is a broad directional grammar, not shot-for-shot imitation of any existing film.

## Application notes for Ellipse

### Tara

Use natural depth: branches, rocks, river, lake, mountains. Aaron should often be small against the landscape.

### Elgia / Sea

Use masts, rails, ropes, sails, harbor depth, ship levels, crew silhouettes, and sea horizon for scale.

### Eros Market

High density. Layer crowds, vendors, smoke, fabrics, bird cages, roots, scopes, signs without relying on generated readable text. The market is a continuous sequence, not a montage.

### Academy

Strong interior architecture: marble, shelves, balconies, scrolls, geometric sculptures, doorways, firelit den. Character positions should show power dynamics.

### Aura creation imagery

Maintain blue/silver vapor, elemental light, and human anchor. Aura should not be framed as a villain or generic sorceress.

### Kingdom / Garden / Portara

Use scale: Aaron and Aura small against architecture. Keep amethyst palace geometry, Garden warmth, Pezzotaite Portara, and father-son emotional gravity.

## Review checklist

A storyboard prompt is ready when it answers:

1. Is the frame clearly a storyboard panel rather than concept art?
2. Is the environment specific and detailed enough?
3. Are foreground, midground, and background clear?
4. Is the character blocking readable?
5. Is the camera intention clear?
6. Is the emotional intent clear?
7. Does it hand off to the next board?
8. Does it preserve Ellipse continuity?
9. Does it avoid generated text and copied film still language?
10. Does it follow the visual direction in `docs/visual_direction.md`?
