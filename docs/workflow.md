# Workflow Guide

This document describes the recommended phased workflow for the AI-assisted fantasy film production pipeline.

---

## Phase 1 — Manuscript Ingestion

**Goal:** Load and verify the source manuscript.

1. Place the full manuscript text in `manuscript/full_text.md`.
2. Run `python tools/scripts/ingest_manuscript.py` to confirm the file exists and review word/page count.
3. Note the total page count to estimate the scope of work for adaptation.

**Output:** Verified manuscript file, word count baseline.

---

## Phase 2 — Chapter and Scene Inventory

**Goal:** Break the manuscript into chapters and identify scenes.

1. Run `python tools/scripts/split_chapters.py` to divide the manuscript into per-chapter files in `manuscript/chapters/`.
2. Review chapter boundaries for accuracy. Correct any misdetected splits.
3. Run `python tools/scripts/generate_scene_files.py` to create placeholder scene YAML files in `adaptation/scenes/`.
4. For each chapter, manually count and name the scenes, creating additional scene files as needed (e.g., `CH01_SC02.yaml`).

**Output:** Chapter files, placeholder scene YAML files.

---

## Phase 3 — Character, Location, and Lore Bible

**Goal:** Build a comprehensive story bible from the manuscript.

1. Read through the manuscript and populate character files in `story/characters/` using `character_schema.yaml`.
2. Populate location files in `story/locations/` using `location_schema.yaml`.
3. Add world-building notes in `story/lore/`.
4. Build `story/timeline.md` with key events.
5. Maintain `story/continuity_notes.md` throughout.
6. Run `python tools/scripts/validate_yaml.py` to check for YAML errors.

**Output:** Story bible (characters, locations, lore, timeline).

**Human review checkpoint:** Verify character and location consistency before proceeding.

---

## Phase 4 — Adaptation Treatment and Screenplay

**Goal:** Adapt the novel into a screenplay-length story.

1. Write `adaptation/treatment.md` — a prose summary of the adapted film.
2. Write `adaptation/beat_sheet.md` — structural beats mapped to page targets.
3. Fill in scene YAML files in `adaptation/scenes/` with purpose, emotional arc, and plot turns.
4. Write screenplay scenes in `adaptation/screenplay/`.

**Output:** Treatment, beat sheet, scene files, screenplay draft.

**Human review checkpoint:** Confirm adaptation fidelity and compression decisions.

---

## Phase 5 — Shot Lists

**Goal:** Break each scene into individual shots.

1. For each scene YAML file, create a corresponding shot list file in `production/shotlists/` using `shot_schema.yaml`.
2. Assign shot IDs following the naming convention (e.g., `CH01_SC01_SH001`).
3. Fill in shot type, camera movement, subject, action, and composition for each shot.
4. Run `python tools/scripts/validate_yaml.py` to validate shot YAML files.

**Output:** Shot list YAML files for all scenes.

**Human review checkpoint:** Review shot coverage before storyboard generation.

---

## Phase 6 — Storyboards

**Goal:** Generate storyboard frames for every shot.

1. Complete `production/visual_bible/style_guide.md` and character/location reference notes.
2. Write image prompts in `production/prompts/` using `image_prompt_schema.yaml`.
3. Generate storyboard frames using an AI image model and save to `production/storyboards/`.
4. Name each frame using the shot ID (e.g., `CH01_SC01_SH001.png`).

**Output:** Storyboard image frames for all shots.

**Human review checkpoint:** Approve visual direction before video generation.

---

## Phase 7 — AI Video Generation

**Goal:** Generate short video clips for each shot.

1. Write video prompts in `production/prompts/` using `video_prompt_schema.yaml`.
2. Use approved storyboard frames as source images where applicable.
3. Generate 4–8 second clips per shot using an AI video model.
4. Store clips in `production/render_outputs/` named by shot ID (e.g., `CH01_SC01_SH001_v1.mp4`).
5. Track every clip back to its `shot_id` and `prompt_id`.

**Output:** Video clips for all shots.

**Human review checkpoint:** Review clips for continuity before assembly.

---

## Phase 8 — Editing, Sound, Music, and Polish

**Goal:** Assemble clips into a complete film.

1. Import video clips into a video editing application.
2. Assemble clips in scene and act order.
3. Add dialogue, sound effects, and music.
4. Color grade and apply final visual polish.
5. Export the finished film.

**Output:** Final edited film.
