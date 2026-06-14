# Act I Story Bible

This is the first-pass review layer for Act I. After review, the entries should be expanded into individual YAML files under `story/characters/`, `story/locations/`, and `story/lore/`.

## Core characters

| Character ID | Name | Function | Continuity notes |
|---|---|---|---|
| CHAR_AARON | Aaron | Protagonist; farm boy drawn into cosmic responsibility | Lean teenage boy; ocean-blue eyes; restless, empathetic, imaginative; future father of Eternity. |
| CHAR_AURA | Aura | Ousia / Spirit of All Things; guide and co-protagonist | Deep-cut turquoise eyes; pale skin; can mirror emotion and make imagination into substance; born of the Garden of Time. |
| CHAR_TEACHER | The Teacher | Astronomer of Eros; Academy master; partial explainer | Dark man in gray robes; resists Aura's influence; explains Einai/Ousia but does not know the full truth. |
| CHAR_ETERNITY | Eternity / Father of Time | Cosmic guide; Aaron and Aura's son | Long white hair, beard, ivory cloak, ice-blue eyes, staff; reveals father-son link at the Portara. |
| CHAR_CAPTAIN_ELGIA | Captain of the Elgia | Passage-giver and phrase translator | Broad, scarred, intimidating, ultimately nostalgic; translates the Elgia phrase. |
| CHAR_MATIS | Matis | Young sailor on the Elgia | Helps Aaron and Aura board; practical crew contact. |
| CHAR_ILYICH | Ilyich | Sailor associated with spices and Aura's dress | Gives Aura a dress; tied visually to hull/spice area. |
| CHAR_JERICKS | Jericks | Surly Elgia sailor | Often at rudder or deck; suspicious presence. |
| CHAR_PERIDOT | Peridot | Erosian Black Hair horse | Carries Aaron and Aura to the Academy; linked to Aaron's first vision of Aura's wider nature. |

## Secondary characters to track

- CHAR_FLOWER_SELLER - older woman in Eros flower shop who points toward the Academy.
- CHAR_EROS_BOY - child with Academy textbook who gives directions to Tritaselo Pass.
- CHAR_STABLE_KEEPER - West Eros Stables keeper who rents Peridot.
- CHAR_BALD_SENTRY - Academy doorkeeper in gray robe.

## Locations

| Location ID | Name | Function | Visual / continuity notes |
|---|---|---|---|
| LOC_TARA_WOODS | Woods of Tara | Aaron's refuge and approach to the river | Morning gold, wildlife, gossamer, lesser-known paths. |
| LOC_TARA_RIVER | Tara River | Threshold where Aaron hears the call and finds Aura | Cold current, gold leaf, split mound, blue/silver vapor. |
| LOC_LAKE_TARA | Lake Tara | Sunset longing and first rumble | Ice-melt basin; sunset orange/crimson; later star reflections. |
| LOC_TARA_VALLEY | Tara Valley Trail | Flight path during the rain of lights | Extreme darkness/light contrast, shockwaves, birds in panic. |
| LOC_AARON_FARM | Aaron's Farm | Recovery and decision point | Simple domestic farm space; bandages, bread, pantry, packed bag. |
| LOC_TARA_PORT | Port of Tara | Departure point | Smaller working harbor; The Elgia stands out. |
| LOC_ELGIA | The Elgia | Sea-passage vessel | Three masts, Nonabel wood, ivory sails, silver door inscription. |
| LOC_ELGIA_DECK | Deck of the Elgia | Community, navigation, stars revelation | Foremast, rail, starfield, luminous motes. |
| LOC_ELGIA_HULL | Hull room by the spices | Sleeping quarters | Two cots near spice racks; cramped private transition space. |
| LOC_EROS_PORT | Port of Eros | Arrival into larger world | Busy harbor, large vessels, vanilla sails, market banners. |
| LOC_EROS_MARKET | Market of Eros | Search maze | Cardamom/chili, fabrics, roots, scopes, ale houses, crowd pressure. |
| LOC_EROS_FLOWER_SHOP | Flower shop | First Academy clue | Mint doorway, protocultures, quieter sensory refuge. |
| LOC_WEST_EROS_STABLES | West Eros Stables | Peridot acquisition | Banner, hay, stable gate, twilight. |
| LOC_TRITASELO_PASS | Tritaselo Pass | Road to Academy | Thick pines, Academy triangle marker, Aura's hovering light. |
| LOC_ACADEMY | The Academy | The Teacher's domain | Bluffside, vines, ancient doors, gray/white marble, geometric sculptures. |
| LOC_ACADEMY_LIBRARY | The Athenaeum | Reveal space | Three-story library, illuminated scrolls, old knowledge. |
| LOC_ACADEMY_DEN | The Teacher's den | Private philosophical confrontation | Fire, cushions, round table, pine smoke. |
| LOC_FOREST_COTTAGE | Aura-created cottage | Home/love image and proof of creation | Petrified wood, amethyst, fresh spring, suspended fire. |
| LOC_COSMIC_TRANSIT | Cosmic transit sphere | Travel between worlds | Wind sphere, iron/magnesium plasma, ammolite, turquoise, silver, gold. |
| LOC_KINGDOM_BEGINNING_END | Kingdom at the Beginning and End | Cosmic palace realm | Amethyst palace, regolith, nebula, trillion lights. |
| LOC_GARDEN_OF_TIME | Garden of Time | Aura's origin and thematic center | Colors felt as well as seen; plaque; scaffolding of all beings. |
| LOC_PORTARA_CHAMBER | Portara chamber | Act I gate and reveal | Pezzotaite arch, amethyst walls, refracted light, Eternity's staff. |

## Lore threads

### Einai and Ousia

The Teacher describes Aura as an Einai: energy without form. In contact with a human, the Einai becomes Ousia, the substance form of that person's imagination. Eternity later reframes Aura as her own Ousia and the Spirit of All Things.

### The rain of lights

The rain of lights is both destructive inciting incident and later-recognized creation language. Its visual vocabulary includes iron, magnesium, turquoise, silver, ammolite, azure, rhodonite, and gold.

### Elgia lore lasant, enta ty

The phrase links Aura's arrival, the ship inscription, the Captain's translation, the Garden plaque, and the Portara ending. Use it sparingly so the final translation retains emotional force.

### Kingdom cosmology

The Kingdom stands at the focal balance of the universe's beginning and end. Time is nonlinear there; Eternity can speak of Aaron's future as something already integrated into the cosmic structure.

### Portara

The Portara is a Pezzotaite arch that sends Aaron not simply back, but somewhere he can start from the beginning. It is the physical gate into Act II.

## Expansion tasks

- Convert each character row into `story/characters/CHAR_*.yaml` using `character_schema.yaml`.
- Convert each location row into `story/locations/LOC_*.yaml` using `location_schema.yaml`.
- Split lore threads into separate files under `story/lore/`.
- Cross-check every scene in `adaptation/scenes/act_i_scene_inventory.yaml` against this ID list before writing shot lists.
