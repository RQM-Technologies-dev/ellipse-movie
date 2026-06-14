# AI Video Pipeline

This document describes the intended workflow for generating AI video clips from the shot list and storyboard assets.

---

## Overview

Video generation is done **shot-by-shot**, not scene-by-scene or act-by-act. Each shot produces one short clip (typically 4–8 seconds). Clips are then assembled in post-production.

This approach:
- Keeps generation costs manageable
- Makes retakes and corrections targeted (re-generate one shot, not an entire scene)
- Ensures every asset is traceable back to a specific `shot_id`

---

## Step 1 — Generate Still Storyboard Frames First

Before generating any video, generate a storyboard frame for every shot using an AI image model.

- Use the `image_prompt` field from each shot YAML in `production/shotlists/`.
- Or create a dedicated image prompt file in `production/prompts/` using `image_prompt_schema.yaml`.
- Review every storyboard frame and approve it before using it as a source image for video.

**Why this matters:** Video generation is more expensive than image generation. Catching compositional or continuity errors at the storyboard stage avoids wasted video generation costs.

---

## Step 2 — Lock Character and Location References

Before generating video, confirm:

- Character appearance is consistent with `production/visual_bible/character_reference_notes.md`
- Location appearance is consistent with `production/visual_bible/location_reference_notes.md`
- Style and lighting match `production/visual_bible/style_guide.md`

Do not proceed to video generation if character or location references are still in flux.

---

## Step 3 — Generate 4–8 Second Clips Shot-by-Shot

For each shot:

1. Confirm the storyboard frame is approved.
2. Write or update the video prompt in `production/prompts/` using `video_prompt_schema.yaml`.
3. Generate the clip using an AI video model, using the storyboard frame as the source image where supported.
4. Save the clip to `production/render_outputs/` named by shot ID and version:
   - Example: `CH01_SC01_SH001_v1.mp4`

Aim for clips of 4–8 seconds. This length is well-suited to current AI video models and maps naturally to individual shots in a film.

---

## Step 4 — Track Every Asset Back to a Shot ID

Every generated image and video clip **must** be traceable to:

- A `shot_id` (e.g., `CH01_SC01_SH001`)
- A `prompt_id` (e.g., `CH01_SC01_SH001_VID_v1`)

Use the `prompt_id` and `shot_id` fields in the prompt YAML files to maintain this traceability. Do not generate assets outside the structured schema.

---

## Step 5 — Keep Prompts Versioned

Never overwrite a prompt file. Instead, create a new versioned copy:

- `CH01_SC01_SH001_video_v1.yaml`
- `CH01_SC01_SH001_video_v2.yaml`

Record the `seed` value in image prompt files when locking a result for reproducibility.

---

## Step 6 — Do Not Rely on One Long Generation for Entire Scenes

Current AI video models produce best results with short clips. Do not attempt to generate an entire scene or sequence in a single generation. Instead:

- Generate each shot individually
- Assemble shots into scenes in a video editor
- Use consistent visual references to maintain continuity across cuts

Long single-generation outputs are difficult to control, prone to drift, and cannot be re-generated partially if one portion needs correction.

---

## Asset Storage

Generated media files (`.mp4`, `.mov`, `.png`, `.jpg`, etc.) are excluded from git by default (see `.gitignore`). Use external cloud storage for generated assets and reference them by shot ID in your asset tracking log.
