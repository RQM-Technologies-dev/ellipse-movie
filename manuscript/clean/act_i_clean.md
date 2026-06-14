# Act I Clean Manuscript

This clean Act I layer preserves the manuscript wording while removing extraction artifacts such as printed page numbers and hard PDF line wrapping.

The authoritative clean Act I text is organized by movement under `manuscript/clean/chapters/`:

1. [`CH01_overture.md`](chapters/CH01_overture.md)
2. [`CH02_the_clouds.md`](chapters/CH02_the_clouds.md)
3. [`CH03_the_rain_of_lights.md`](chapters/CH03_the_rain_of_lights.md)
4. [`CH04_passacaglia.md`](chapters/CH04_passacaglia.md)
5. [`CH05_the_seas.md`](chapters/CH05_the_seas.md)
6. [`CH06_the_stars.md`](chapters/CH06_the_stars.md)
7. [`CH07_the_teacher.md`](chapters/CH07_the_teacher.md)
8. [`CH08_paramours.md`](chapters/CH08_paramours.md)
9. [`CH09_transformation.md`](chapters/CH09_transformation.md)
10. [`CH10_the_father_of_time.md`](chapters/CH10_the_father_of_time.md)
11. [`CH11_ellipse.md`](chapters/CH11_ellipse.md)

The raw manuscript remains unchanged at `manuscript/full_text.md`.

## Build note

For tools that require a single continuous file, concatenate the clean movement files in chapter order:

```bash
cat manuscript/clean/chapters/CH01_overture.md \
    manuscript/clean/chapters/CH02_the_clouds.md \
    manuscript/clean/chapters/CH03_the_rain_of_lights.md \
    manuscript/clean/chapters/CH04_passacaglia.md \
    manuscript/clean/chapters/CH05_the_seas.md \
    manuscript/clean/chapters/CH06_the_stars.md \
    manuscript/clean/chapters/CH07_the_teacher.md \
    manuscript/clean/chapters/CH08_paramours.md \
    manuscript/clean/chapters/CH09_transformation.md \
    manuscript/clean/chapters/CH10_the_father_of_time.md \
    manuscript/clean/chapters/CH11_ellipse.md \
    > manuscript/clean/act_i_continuous.generated.md
```

Do not edit the generated continuous file by hand. Update the chapter files first, then regenerate.
