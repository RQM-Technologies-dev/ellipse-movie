# Shot List Conventions

These conventions normalize the Act I shot-list layer before storyboard prompt planning.

## File naming

Scene shot lists use:

```text
production/shotlists/scenes/CH##_SC##_shotlist.yaml
```

Sequence shot lists use:

```text
production/shotlists/sequences/SEQ_<CHAPTER>_<SEQUENCE_NAME>_shotlist.yaml
```

## Required scene shot-list fields

Each scene shot list should include:

```yaml
shotlist_id: SHOTLIST_CH##_SC##
scene_id: CH##_SC##
title: <scene title>
status: drafted
source_scene: adaptation/scenes/CH##_SC##.yaml
visual_direction: docs/visual_direction.md
scene_intent: <one-sentence cinematic purpose>
shots:
- shot_id: CH##_SC##_SH###
  type: <shot function>
  framing: <composition / subject>
  camera: <camera behavior / angle / movement>
  action: <what happens in the shot>
  purpose: <why the shot exists>
notes:
- <scene-level note>
```

## Required sequence shot-list fields

Each sequence shot list should include:

```yaml
shotlist_id: SHOTLIST_SEQ_<ID>
sequence_id: SEQ_<ID>
title: <sequence title>
status: drafted
source_sequence: adaptation/sequences/<sequence>.yaml
source_scenes:
- CH##_SC##
visual_direction: docs/visual_direction.md
sequence_intent: <one-sentence cinematic purpose>
shots:
- shot_id: <SEQ>_SH###
  beat_id: <beat id from source sequence>
  type: <shot function>
  framing: <composition / subject>
  camera: <camera behavior / angle / movement>
  action: <what happens in the shot>
  purpose: <why the shot exists>
notes:
- <sequence-level note>
```

## Review standards

A shot list is storyboard-ready when:

- every shot has a clear visual purpose,
- shot IDs are stable and unique,
- the source scene or sequence is linked,
- blocking and camera choices are motivated by emotion, discovery, danger, or story information,
- geography remains readable before spectacle,
- visual continuity is preserved for Aura, Einai/Ousia, the rain of lights, Eros, the Kingdom, and the Portara,
- the shot list follows the project-wide visual direction in `docs/visual_direction.md`.

## Storyboard handoff rule

Storyboard prompts should be generated from reviewed shot lists only. Do not generate video prompts or AI media directly from scene YAML.
