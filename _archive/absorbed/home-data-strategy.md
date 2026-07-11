---
title: hOme Data Strategy
date: 2026-03-14
status: design
tags: [data-model, strategy, pkm, postgresql]
---

# hOme Data Strategy

## Context

This strategy was derived from querying the LifeOS Librarian across SelfKnowledge, HealthNeuroscience, PersonalKnowledgeManagement, BooksLibrary, and DataArcheologyFundamentals collections. The design principles come from our own knowledge — not external templates.

## Core Principles

### 1. PARA-Aligned Home Structure
Applying the PARA method (Projects, Areas, Resources, Archives) to home management:
- **Projects** → Active renovations with deadlines ("Repaint Living Room by April")
- **Areas** → Ongoing responsibilities ("Kitchen maintenance", "HVAC scheduling")
- **Resources** → Reference material (Pinterest boards, contractor contacts, material specs)
- **Archives** → Completed projects (before/after, receipts, lessons learned)

### 2. Bite-Sized Container Design (ADHD-Optimized)
Every home project must be a **bounded container** with:
- Explicit scope — one room or one system, never "fix the whole house"
- Clear inputs — materials list, budget, inspiration board
- Visible completion state — before/after photos, checklist with progress markers
- Natural stopping points — phases, not marathons
- Dopamine architecture — small wins visible early (paint > plumbing)

### 3. Sensory-First Prioritization
Prioritize spaces by **cognitive impact**, not aesthetics:

```text
Priority Score = Sensory Load (negative triggers)
              × Time Spent in Space
              × Gap Between Current and Vision State
```

A noisy, cluttered office where you spend 8 hours/day > a perfect guest bathroom.

### 4. Environmental Design Methodology
From systems thinking + behavioral design:
- **Reduce friction** for desired behaviors (clear desk = easier to start work)
- **Add friction** for undesired behaviors (TV in less accessible spot)
- **Soft fascination elements** — plants, natural light, views → attention restoration
- **Multi-sensory optimization** — lighting + sound + texture + temperature as a package

### 5. Future-Backward Planning
- Start with: "What does this room feel like in my ideal future?"
- Work backward to: "What changes produce that feeling?"
- Reject changes that don't serve the envisioned state (even if trendy)

### 6. Systematic Documentation
- Frontmatter-driven metadata on every space and project (queryable)
- Controlled vocabulary for tags (don't let "renovation", "reno", "remodel" proliferate)
- Decision logs per project (why you chose X over Y)
- Templates for project kickoff, reducing decision fatigue

## Data Model

### home_spaces (PostgreSQL)
Primary table tracking every space in the home.

| Column | Type | Description |
|--------|------|-------------|
| id | UUID | Primary key (auto-generated) |
| instance_id | TEXT | Stable identifier (e.g., `space-1f-kitchen`) |
| name | TEXT | Display name ("Eat-In Kitchen") |
| space_type | TEXT | room, closet, outdoor, storage, mechanical, garage, bathroom |
| level | TEXT | "1st Level", "2nd Level", "Lower Level" |
| dimensions | TEXT | "16' × 23'" |
| sq_ft | INTEGER | Calculated square footage |
| parent_id | UUID | Self-referential FK (closets → rooms) |
| sensory_profile | JSONB | {lighting, noise, clutter, temperature, colors} |
| function_tags | JSONB | ["restorative", "work", "social", "storage"] |
| current_condition | TEXT | good, needs_work, in_progress |
| priority_rank | INTEGER | 1-5 (1 = highest priority) |
| vision_notes | TEXT | "What this space should feel like" |
| features | JSONB | {fireplace: true, walk_out: true, etc.} |
| person_id | TEXT | Owner UUID |
| created_at | TIMESTAMPTZ | Auto |

### home_projects (PostgreSQL, future)
Active renovation/improvement projects scoped to spaces.

| Column | Type | Description |
|--------|------|-------------|
| id | UUID | Primary key |
| instance_id | TEXT | e.g., `proj-kitchen-backsplash` |
| space_id | UUID | FK to home_spaces |
| title | TEXT | Project name |
| status | TEXT | planning, in_progress, review, completed, archived |
| phase | TEXT | Current phase within the project |
| scope_notes | TEXT | Bounded container description |
| budget_estimated | DECIMAL | Planned budget |
| budget_actual | DECIMAL | Actual spend |
| pinterest_board_id | TEXT | Linked inspiration board |
| decision_log | JSONB | Array of {date, decision, rationale} |
| completion_checklist | JSONB | Array of {task, done} |
| priority_rank | INTEGER | 1-5 |
| person_id | TEXT | Owner UUID |
| created_at | TIMESTAMPTZ | Auto |

### home_materials (PostgreSQL, future)
Materials tracking per project.

| Column | Type | Description |
|--------|------|-------------|
| id | UUID | Primary key |
| project_id | UUID | FK to home_projects |
| item | TEXT | Material name |
| quantity | DECIMAL | Amount needed |
| unit | TEXT | sq ft, linear ft, each, etc. |
| unit_cost | DECIMAL | Cost per unit |
| vendor | TEXT | Where to buy |
| status | TEXT | needed, ordered, delivered, installed |
| purchased_date | DATE | When purchased |
| notes | TEXT | |

## Room Inventory (From Floor Plans)

### 1st Level (15 spaces)
1. Eat-In Kitchen (16' × 23')
2. Family Room (21' × 20') — fireplace
3. Living Room (18' × 20') — fireplace
4. Dining Room (16' × 16')
5. Foyer (14' × 13') — curved staircase
6. Sun Room (16' × 27')
7. 1st Floor Bedroom (16' × 15')
8. 1st Floor Bath (8' × 4') — attached to bedroom
9. Laundry Room (9' × 6')
10. Garage (31' × 21')
11. Deck — outdoor, rear
12. 1st Floor Powder Room — near foyer
13-15. Closets (×3) — children of bedroom/foyer

### 2nd Level (8 spaces)
16. Primary Bedroom (16' × 23')
17. Walk-In Closet (11' × 7') — child of primary bedroom
18. Primary Bath (15' × 16') — soaking tub
19. Bedroom 2 (17' × 12')
20. Bedroom 3 (20' × 16')
21. 2nd Floor Bath (10' × 7') — shared
22-23. Closets (×2) — children of bedrooms

### Lower Level (7 spaces)
24. Den (15' × 28')
25. Exercise Room (15' × 13')
26. Storage 1 (15' × 16')
27. Storage 2 (19' × 17')
28. Mechanical/Storage
29. Lower Level Powder Room (9' × 4')
30. Patio — outdoor, walk-out

## Knowledge Sources
- SelfKnowledge KB: sensory triggers, ADHD patterns, environmental sensitivity
- HealthNeuroscience KB: cognitive impact of environment, attention restoration
- PersonalKnowledgeManagement KB: PARA method, GTD workflow, tag governance
- BooksLibrary: systems thinking, behavioral design, project management
- DataArcheologyFundamentals: frontmatter patterns, controlled vocabulary, decision logs

## STL Pipeline Architecture (2026-03-14)

### Breakthrough: STL Export + trimesh = Programmatic 3D Access

SketchUp Free web app cannot be accessed programmatically (no API, Playwright blocked by WebGL loading gate). However, it CAN export STL files. Using `trimesh` + `matplotlib`, we can:
- Load 104MB+ STL meshes
- Generate cross-section views at any height (wall layout at 6", counter height at 36", upper cabinets at 96")
- Extract dimensions, bounding boxes, and geometry data
- Render 2D plan views as PNG images

This eliminates the need for SketchUp Pro, MCP servers, or any paid tools.

### Progressive Enrichment Layers

Derived from DataArcheologyFundamentals and PKM knowledge bases:

```text
Layer 0: Raw STL file (binary mesh)
    ↓ trimesh.load()
Layer 1: Extracted geometry (cross-sections, dimensions, bounding boxes)
    ↓ matplotlib renders
Layer 2: Structured entities (rooms, counters, appliances → PostgreSQL home_spaces)
    ↓ entity resolution
Layer 3: Enriched entities (linked to devices, Pinterest, sensory profiles)
    ↓ query engine
Layer 4: Queryable knowledge ("what countertop run fits my 22 appliances?")
```

### Integration via Stable UUIDs

All data connects through `instance_id`:
- `home_spaces.instance_id` ←→ `devices.space_instance_id`
- `home_spaces` ←→ 3D geometry data (JSONB `geometry_data` column)
- `home_spaces` ←→ Pinterest board pins (future)
- `home_spaces` ←→ `home_projects` (future)
- `home_spaces` ←→ sensory profiles

### Pipeline Design Principles

From SoftwareDevelopment and RAGEngineering KBs:
- **Idempotent** — rerun on any STL version, overwrite Layer 1, cascade
- **Incremental** — process deltas when design changes
- **Provenance** — every data point traces to STL version + extraction date
- **Entity resolution** — match extracted rooms against existing home_spaces records, flag dimension conflicts

### Pipeline Script Architecture

```text
scripts/sketchup_analyze.py
├── load_stl(path) → trimesh mesh
├── extract_cross_sections(mesh, heights=[6, 36, 96])
│   └── saves PNGs to project folder
├── extract_dimensions(mesh) → bounding box, room bounds
├── compare_to_db(dimensions, home_spaces)
│   └── flags mismatches
├── enrich_db(geometry_data) → updates PostgreSQL JSONB
└── generate_report() → markdown summary
```

### Key Decision: Geometry as JSONB

Store extracted geometry data as JSONB in `home_spaces.geometry_data`:
```json
{
  "stl_source": "First Floor - v1.stl",
  "extraction_date": "2026-03-14",
  "bounding_box": {"min": [-500, -475, -47], "max": [558, 417, 188]},
  "dimensions_inches": {"x": 1058, "y": 892, "z": 235},
  "dimensions_feet": {"x": 88.2, "y": 74.3, "z": 19.6},
  "total_faces": 2081600,
  "cross_sections_generated": ["6in", "36in", "96in"]
}
```

This lets the schema evolve without DDL changes and supports versioning when designs update.

### Tools Used
- `trimesh` 4.11.3 — STL loading and cross-sectioning
- `matplotlib` 3.10.8 — 2D rendering of cross-sections
- `numpy` — geometry calculations

## Next Steps
- [x] Strategic research via Librarian
- [x] Design document
- [x] STL pipeline architecture designed
- [x] First STL successfully loaded and cross-sectioned (First Floor - v1.stl, 104MB, 2M faces)
- [ ] Create home_spaces table in PostgreSQL
- [ ] Populate with floor plan inventory (~30 spaces)
- [ ] Build sketchup_analyze.py pipeline script
- [ ] Add geometry_data JSONB column to home_spaces
- [ ] Extract and enrich kitchen geometry into home_spaces
- [ ] Sensory profiling of key spaces (future sessions)
- [ ] Create home_projects table when first project starts
- [ ] Connect Pinterest boards to spaces once API access approved
- [ ] Build Blender headless import pipeline for full materials (Path B, future)
