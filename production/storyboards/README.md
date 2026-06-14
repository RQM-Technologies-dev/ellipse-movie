# Storyboards

This folder contains storyboard image frames for each shot.

## Naming Convention

Image files should be named using the shot ID, e.g. `CH01_SC01_SH001.png`.

## Instructions

1. Complete the shot list YAML files in `production/shotlists/` first.
2. Use the `image_prompt` field from each shot to generate storyboard frames.
3. Store generated frames here using the shot ID as the filename.
4. Review all frames before proceeding to video generation.

> Note: Image files are excluded from git by default via `.gitignore`. Store large assets externally if needed.
