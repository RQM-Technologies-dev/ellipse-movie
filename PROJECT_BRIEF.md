# Project Brief — AI-Assisted Fantasy Film Production Pipeline

## Goal

Transform a full young adult fantasy manuscript into a structured cinematic adaptation using AI-assisted preproduction tools. The pipeline produces chapters, scene files, a treatment, beat sheet, screenplay, shot lists, storyboard prompts, and AI video generation packets.

## Scope

- Ingest and organize the full manuscript
- Build a story bible (characters, locations, lore, timeline, continuity)
- Adapt the story into screenplay format
- Produce detailed shot lists and storyboard prompts
- Generate AI image storyboard frames shot-by-shot
- Produce AI video clips per shot, tracked back to shot IDs
- Assemble a final edit-ready asset library

## Non-Goals

- This repo does not produce a final rendered film
- No story content is invented without manuscript source material
- No audio mixing or final color grading is performed here
- No distribution or rights management is handled in this repo

## First Milestone

- Manuscript uploaded to `manuscript/full_text.md`
- Chapter split completed into `manuscript/chapters/`
- Story bible stubs created (characters, locations, lore)
- Scene inventory generated for at least one chapter

## Recommended Workflow

1. **Manuscript Ingestion** — Upload `manuscript/full_text.md`, run `ingest_manuscript.py` to confirm word count and page estimate.
2. **Chapter Split** — Run `split_chapters.py` to divide the manuscript into per-chapter files in `manuscript/chapters/`.
3. **Story Bible** — Populate character, location, and lore files using the YAML schemas in `story/`.
4. **Scene Inventory** — Run `generate_scene_files.py` to create placeholder scene YAML files in `adaptation/scenes/`.
5. **Adaptation** — Write treatment, beat sheet, and screenplay in `adaptation/`.
6. **Shot Lists** — Populate `production/shotlists/` using `shot_schema.yaml`.
7. **Storyboards** — Generate image prompts in `production/prompts/` and storyboard frames in `production/storyboards/`.
8. **AI Video** — Generate 4–8 second clips per shot using `video_prompt_schema.yaml`, stored in `production/render_outputs/`.
9. **Edit** — Assemble clips into scenes and sequences for final edit.

## Human Review Checkpoints

- After chapter split: review chapter boundaries for accuracy
- After story bible: verify character and location consistency
- After scene inventory: validate scene purpose and emotional arc
- After beat sheet: confirm adaptation fidelity to source material
- After shot list: review shot coverage before storyboard generation
- After storyboard generation: approve visual direction before video generation
- After video generation: review clips for continuity before assembly

## Risks

| Risk | Description |
|------|-------------|
| **Continuity** | Character appearance, wardrobe, and prop details may drift across generated assets. Use `continuity_notes` fields in all schemas and conduct regular audits. |
| **Adaptation Compression** | A novel must be compressed significantly for film. Key subplots, characters, or world-building may need to be cut. Track all omissions explicitly. |
| **Generation Cost** | AI image and video generation can be expensive at scale. Plan generation in phases; generate storyboards before committing to video. |
| **Copyright / IP Management** | All generated content is derived from the source manuscript. Ensure rights clearances are handled before any public distribution. Avoid training on third-party copyrighted reference material without permission. |
