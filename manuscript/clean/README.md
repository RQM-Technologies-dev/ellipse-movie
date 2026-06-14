# Clean Manuscript Layer

This directory is reserved for cleaned source text derived from `manuscript/full_text.md`.

The raw manuscript should remain untouched. Clean files should preserve the author's wording while removing import artifacts such as:

- page numbers inserted into prose,
- PDF line-wrap artifacts,
- front-matter pagination,
- accidental stray punctuation from extraction,
- duplicated whitespace,
- broken words caused by source conversion.

## Proposed files

- `act_i_clean.md` - cleaned continuous Act I text.
- `chapters/CH01_overture.md` through `chapters/CH11_ellipse.md` - cleaned movement files.
- `cleanup_log.md` - record of non-trivial cleanup decisions.

Do not use the clean layer to rewrite prose for style. Adaptation changes belong in `adaptation/`.
