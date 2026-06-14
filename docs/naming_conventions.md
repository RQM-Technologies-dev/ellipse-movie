# Naming Conventions

All assets in this pipeline use a consistent hierarchical naming system so every file can be traced back to its source chapter, scene, and shot.

---

## Chapter IDs

Format: `CH##`

| Example | Meaning |
|---------|---------|
| `CH01` | Chapter 1 |
| `CH12` | Chapter 12 |

---

## Scene IDs

Format: `CH##_SC##`

| Example | Meaning |
|---------|---------|
| `CH01_SC01` | Chapter 1, Scene 1 |
| `CH03_SC04` | Chapter 3, Scene 4 |

---

## Shot IDs

Format: `CH##_SC##_SH###`

| Example | Meaning |
|---------|---------|
| `CH01_SC01_SH001` | Chapter 1, Scene 1, Shot 1 |
| `CH02_SC03_SH012` | Chapter 2, Scene 3, Shot 12 |

---

## Character IDs

Format: `CHAR_<NAME_IN_CAPS>`

| Example | Meaning |
|---------|---------|
| `CHAR_ELARA` | Character named Elara |
| `CHAR_LORD_VETH` | Character named Lord Veth |

---

## Location IDs

Format: `LOC_<LOCATION_NAME_IN_CAPS>`

| Example | Meaning |
|---------|---------|
| `LOC_MOONWATER_BRIDGE` | Location: Moonwater Bridge |
| `LOC_ELDER_FOREST` | Location: Elder Forest |

---

## File Naming

| Asset Type | Format | Example |
|------------|--------|---------|
| Chapter file | `chapter_###.md` | `chapter_001.md` |
| Scene YAML | `<scene_id>.yaml` | `CH01_SC01.yaml` |
| Shot list | `<scene_id>_shots.yaml` | `CH01_SC01_shots.yaml` |
| Storyboard frame | `<shot_id>.png` | `CH01_SC01_SH001.png` |
| Image prompt | `<shot_id>_image.yaml` | `CH01_SC01_SH001_image.yaml` |
| Video prompt | `<shot_id>_video.yaml` | `CH01_SC01_SH001_video.yaml` |
| Video clip | `<shot_id>_v#.mp4` | `CH01_SC01_SH001_v1.mp4` |

---

## Versioning

When multiple versions of a prompt or render exist, append `_v#`:

- `CH01_SC01_SH001_image_v1.yaml`
- `CH01_SC01_SH001_image_v2.yaml`
- `CH01_SC01_SH001_v1.mp4`
- `CH01_SC01_SH001_v2.mp4`

Never overwrite a previous version. Always increment the version number.
