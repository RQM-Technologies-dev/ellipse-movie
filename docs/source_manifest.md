# Source Manifest

## Canonical source files

- `manuscript/full_text.md` - raw imported text for *Ellipse*, Act I.
- `manuscript/chapters/chapter_001.md` through `manuscript/chapters/chapter_011.md` - movement-based splits generated from the raw manuscript.
- `docs/chapter_map.md` - human-readable mapping from pipeline IDs (`CH01` etc.) to Act I movement titles.
- `adaptation/scenes/act_i_scene_inventory.yaml` - consolidated scene inventory used for review before one-file-per-scene expansion.
- `story/act_i_story_bible.md` - first-pass character, location, and lore bible for Act I.

## Source handling policy

The raw manuscript is treated as a preservation layer. Do not overwrite it during adaptation work.

All cleanup, scene extraction, adaptation compression, story-bible notes, and screenplay work should be additive and traceable back to the raw source. When a spelling, punctuation, or line-break issue appears to be an import artifact, preserve the raw source and document the cleanup decision in a derived file instead of silently changing the original.

## Current source status

- Act I has been imported into `manuscript/full_text.md`.
- Act I has been split by movement headings.
- The next production-ready source layer should be a cleaned manuscript under `manuscript/clean/`, preserving wording while removing page numbers, PDF line-break artifacts, and front-matter pagination.

## Guardrails

- Do not invent story content that cannot be tied to the manuscript.
- Do not start shot lists, storyboard prompts, or video prompts until the Act I scene inventory and story bible have been reviewed.
- Track all adaptation compression choices in scene-level `adaptation_notes`.
- Keep all AI-visual notes free of copyrighted third-party visual references.
