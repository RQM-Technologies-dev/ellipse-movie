# Act I Shot List Review

## Review outcome

The Act I shot-list layer is ready for storyboard prompt planning.

## Scope reviewed

- Individual scene shot lists under `production/shotlists/scenes/`.
- Eros Market sequence shot list under `production/shotlists/sequences/`.
- Tracking index at `production/shotlists/act_i_shotlist_index.yaml`.
- Global visual direction at `docs/visual_direction.md`.

## Coverage check

- All locked Act I scene YAML files have a drafted scene shot list or are covered by the Eros Market continuous sequence shot list.
- CH07_SC01 through CH07_SC05 are intentionally covered by `SEQ_CH07_EROS_MARKET` rather than separate isolated scene shot lists, because the market is designed as a continuous chained sequence.
- The Overture and all major visual anchors have dedicated shot lists.

## Convention check

The current shot-list files follow the normalized conventions:

- scene shot-list IDs use `SHOTLIST_CH##_SC##`,
- scene shot IDs use `CH##_SC##_SH###`,
- sequence shot-list ID uses `SHOTLIST_SEQ_<ID>`,
- sequence shot IDs use `ERM_SH###` for the Eros Market sequence,
- source scene or source sequence references are present,
- `visual_direction: docs/visual_direction.md` is present,
- each shot includes `type`, `framing`, `camera`, `action`, and `purpose`,
- scene-level or sequence-level notes are present.

## Visual-direction check

The shot-list layer is aligned with the project's visual direction:

- scenes are anchored in readable geography before spectacle,
- camera movement is motivated by discovery, danger, wonder, or emotional pressure,
- major fantasy set pieces keep Aaron or Aura as the human anchor,
- the Eros Market is treated as continuous chained discovery rather than montage compression,
- the Overture and Portara ending mirror each other emotionally,
- The Teacher/Athenaeum material is staged as emotional destabilization rather than lecture,
- the Cottage Creation reuses the rain-of-lights palette as creation rather than terror.

## Continuity check

The shot-list layer preserves the required visual continuity for:

- Aura's turquoise eyes, mud/wounds, blue-silver vapor, and autonomy,
- Einai/Ousia as true-but-incomplete Teacher explanation corrected by Eternity,
- rain-of-lights color language and later creative recontextualization,
- the Elgia phrase from river to ship to Garden to Portara,
- Eros as a full fantasy-world sequence,
- the Kingdom's amethyst architecture, Garden warmth, and Portara final threshold.

## Normalization decision

No scene-boundary changes were required. No shot-list IDs were changed. The shot-list index now records the overall layer as reviewed while the individual shot-list files remain `status: drafted`, preserving the fact that these are production drafts ready for storyboard prompt generation rather than final locked storyboards.

## Next approved step

Prepare the storyboard prompt layer using the reviewed shot lists as the source of truth.
