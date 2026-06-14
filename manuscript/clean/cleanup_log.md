# Cleanup Log — Act I

## Source

- Raw repository source: `manuscript/full_text.md`
- PDF source used for extraction: `Ellipse_Final Edit_Van Geem.pdf`
- Scope: Act I, from `Overture` through `Ellipse`

## Cleanup actions performed

- Removed standalone printed page-number lines from the extracted Act I text.
- Removed hard PDF line wrapping by joining wrapped lines into paragraphs.
- Preserved movement headings and converted them to Markdown headings in the clean layer.
- Preserved the Act I structure and created one clean chapter file per movement.
- Preserved manuscript wording, spelling, invented terms, dialogue, and lore terms.
- Converted the long underscore scene divider in `The Rain of Lights` to a Markdown scene break (`---`).
- Removed four stray terminal exclamation marks that appeared immediately after a period or closing quote at movement endings.

## Counts

- Standalone page-number lines removed: 53
- Stray terminal exclamation artifacts removed: 4
- Scene dividers normalized: 2
- Movement headings found: 11
- Movement headings: Overture, The Clouds, The Rain of Lights, Passacaglia, The Seas, The Stars, The Teacher, Paramours, Transformation, The Father of Time, Ellipse

## Guardrail

This cleanup pass does not rewrite prose for style, grammar, or continuity. Editorial revision belongs in the adaptation layer, not in this clean source layer.
