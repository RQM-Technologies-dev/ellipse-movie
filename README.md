# ellipse-movie — AI-Assisted Fantasy Film Production Pipeline

This is an AI-assisted preproduction repository for turning a novel into a cinematic adaptation. The pipeline takes a full young adult fantasy manuscript and progressively organizes it into chapters, scenes, a screenplay adaptation, shot lists, storyboard prompts, visual bible materials, and AI-video production packets.

## Pipeline

```
Manuscript → Chapters → Scenes → Beats → Screenplay → Shots → Storyboards → Video Prompts → AI Video Clips → Final Edit
```

## Folder Structure

```
young-adult-fantasy-film-pipeline/
  manuscript/         Raw manuscript text and per-chapter splits
  story/              Characters, locations, lore, timeline, continuity
  adaptation/         Treatment, beat sheet, screenplay, scene files
  production/         Visual bible, shot lists, storyboards, prompts, render outputs
  tools/              Python scripts for ingestion, splitting, generation, validation
  docs/               Workflow guide, naming conventions, AI video pipeline notes
```

## Getting Started

1. Place your manuscript text in `manuscript/full_text.md`.
2. Install dependencies: `pip install -r requirements.txt`
3. Run `python tools/scripts/ingest_manuscript.py` to verify the manuscript.
4. Run `python tools/scripts/split_chapters.py` to split chapters.
5. Follow the phased workflow in `docs/workflow.md`.

## Documentation

- [Workflow](docs/workflow.md)
- [Naming Conventions](docs/naming_conventions.md)
- [AI Video Pipeline](docs/ai_video_pipeline.md)
- [Project Brief](PROJECT_BRIEF.md)
