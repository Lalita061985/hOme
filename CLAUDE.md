# hOme — Project Context

**Project UUID:** `43edf4c9-5b77-4b67-9fa6-2356ba1a508a`
**Last Updated:** 2026-03-26

---

## Purpose

hOme is the physical home environment layer of the LifeOS system — household management, kitchen renovation, device tracking, space optimization, and sensory profiling. It sits alongside the four LifeOS pillars as the environmental substrate that makes healthy living possible.

**Framing:** "Responsibility Laura" — the home is managed as infrastructure, not decoration.

---

## Connection to LifeOS

hOme is the physical counterpart to the LifeOS pillar system:

| LifeOS Pillar | hOme Intersection |
|---------------|-------------------|
| Sleep | Bedroom sensory profile, blackout, humidifier, ECOVACS schedule |
| Nutrition | Kitchen reno, freezer organization, appliance catalog, grocery/meal infrastructure |
| Movement | Floor plan clearances, robot vacuum schedules, garage gym potential |
| Soul | Environmental calm, clutter reduction, sensory walk-throughs |

Cross-project references from LifeOS Cortex docs use the `hOme:` prefix in `related_to` fields. hOme is a candidate for future Cortex absorption.

---

## Cortex Absorption Status

Organic research and documentation has been absorbed into Cortex. This repo now holds binary assets and operational scripts only.

| Cortex Doc | Content | Domain |
|------------|---------|--------|
| LF-LIF-060 | Freezer Organization | LIF/ |
| LF-LIF-061 | Kitchen Renovation | LIF/ |
| LF-TOL-019 | Pinterest Integration | TOL/ |
| LF-TOL-020 | SketchUp Integration | TOL/ |
| LF-GOV-001 | Home Data Strategy | GOV/ |

Absorbed markdown files are preserved in `_archive/absorbed/` for reference.

---

## What Remains in This Repo

This is a thin asset and operational repo. Content lives in Cortex; data lives in PostgreSQL.

```text
hOme/
├── CLAUDE.md                      ← You are here
│
├── Floor Plans/                   ← MLS floor plans (PNG): 1st Level, 2nd Level, Basement
│
├── Kitchen Reno/                  ← SketchUp STL (First Floor - v1.stl) + cross-section PNGs
│   ├── First Floor - v1.stl       ← 104MB — do not embed; use sketchup_screenshot.py
│   └── *.png                      ← Cross-section views generated from STL
│
├── LPS/                           ← Session artifacts: photos, voice memos, transcripts, recaps
│   ├── *.HEIC                     ← Appliance label photos, interior photos
│   ├── 29 Walker Ln 28.m4a        ← Voice memo of freezer interior measurements
│   ├── NoteGPT_TRANSCRIPT_*.txt   ← Transcription of voice memo
│   └── SESSION_RECAP_*.md         ← Session recaps (historical reference)
│
├── research/                      ← (empty — content absorbed to Cortex)
│
├── scripts/
│   ├── sketchup_screenshot.py     ← Playwright tool: STL → interactive screenshots
│   └── pinterest/
│       ├── pinterest_test.py      ← Pinterest API v5 CLI (auth, boards, pins, export)
│       ├── requirements.txt
│       └── README.md
│
└── _archive/
    ├── absorbed/                  ← Pre-absorption markdown docs (historical reference)
    └── NEXT_SESSION.md            ← Deprecated (ADR-005); preserved for history
```

**Large files — do not embed:**

| File | Size | Note |
|------|------|------|
| `Kitchen Reno/First Floor - v1.stl` | ~104 MB | Use `scripts/sketchup_screenshot.py` for views |

---

## Key Data Sources

All operational data lives in PostgreSQL. This repo holds the raw assets that feed it.

| Table | Contents | Filter |
|-------|----------|--------|
| `home_spaces` | 31 spaces across 3 levels | `SELECT * FROM home_spaces ORDER BY level, name` |
| `devices` | All registered appliances + smart home devices | `WHERE project_id = '43edf4c9-...'` |
| `tasks` | Active hOme tasks | `WHERE project_id = '43edf4c9-...'` |
| `decisions` | Architecture decisions (HOME-DEC-001 through 006) | `WHERE project_id = '43edf4c9-...'` |
| `webpages` | 912 imported Safari bookmarks (home, shopping, etc.) | `WHERE discovery_source = 'safari-bookmarks'` |

**NocoDB:** `entities` table with `project = 'hOme'` filter for taxonomy-level browsing.

---

## Active Workstreams

### Kitchen Renovation
- STL model loaded (`Kitchen Reno/First Floor - v1.stl`), cross-section views generated
- Sensory profiling in progress (living room done as baseline; kitchen next)
- LG Studio wall oven + microwave combo pending installation
- **Cortex doc:** LF-LIF-061

### Freezer Organization
- Basement Frigidaire FFUE2024AWA (20 cu ft): 26.5"W x 16"D x 47"H usable interior
- Household pattern: "Lego pieces" (same-day, component-based) — frozen meals incompatible
- Step 0 in progress: migrate frozen meals to garage GE fridge before zoning
- Bin catalog compiled (YouCopia, iDesign, Brightroom, Mainstays — PETG/PET only)
- **Cortex doc:** LF-LIF-060

### Pinterest Integration
- API trial submitted 2026-03-14; check developer portal for approval status
- On approval: get App Secret → update `~/.env` → run `python scripts/pinterest/pinterest_test.py auth`
- **Cortex doc:** LF-TOL-019

### Sensory Walk-Through
- Living room: complete (baseline — all excellent, HA-integrated)
- Kitchen, family room, dining room, sun room, library: pending
- Task: `task-home-sensory-profile-1f-primary`

---

## Session Pattern

1. Run `/next` — queries tasks table + latest session chronicle
2. Check `LPS/SESSION_RECAP_*.md` for context from the most recent session
3. One workstream per session; do not context-switch mid-workstream
4. Tag every new task with `project_id = '43edf4c9-5b77-4b67-9fa6-2356ba1a508a'`
5. Run `/eos` to update task statuses in PostgreSQL

---

## Common Queries

### Query all hOme tasks

```sql
SELECT instance_id, task, status, pillar
FROM tasks
WHERE project_id = '43edf4c9-5b77-4b67-9fa6-2356ba1a508a'
  AND status NOT IN ('completed', 'superseded')
ORDER BY status, task;
```

### Query registered devices

```sql
SELECT name, model, space_name, status
FROM devices
WHERE project_id = '43edf4c9-5b77-4b67-9fa6-2356ba1a508a'
ORDER BY space_name, name;
```

### Query home spaces by level

```sql
SELECT level, name, type, sensory_profile_status
FROM home_spaces
ORDER BY level, name;
```

### Query architectural decisions

```sql
SELECT instance_id, title, status, created_at
FROM decisions
WHERE project_id = '43edf4c9-5b77-4b67-9fa6-2356ba1a508a'
ORDER BY created_at;
```

---

## Smart Home Ecosystem

5 platforms currently active:

| Platform | Devices |
|----------|---------|
| Samsung SmartThings | Bespoke 4-Door Fridge, Jet Bot R2 Robot Vacuum |
| LG ThinQ | WashCombo Washer/Dryer, Smart Dishwasher, Studio Wall Oven (pending) |
| ECOVACS Home | Deebot N8 Pro+ (primary bedroom), Deebot N79S (basement, inactive) |
| Midea SmartHome | Cube Dehumidifier (basement) |
| LEVOIT/VeSync | Superior 6000S Humidifier (primary bedroom) |

Home Assistant is the integration layer (morning brightness, evening dimming).

---

## Key Architectural Decisions

| ID | Decision | Status |
|----|----------|--------|
| HOME-DEC-001 | PostgreSQL `home_spaces` as canonical space registry | Accepted |
| HOME-DEC-002 | SketchUp STL as geometry source of truth | Accepted |
| HOME-DEC-003 | Living room as sensory baseline reference | Accepted |
| HOME-DEC-004 | Frozen meals operationally incompatible with household cooking pattern | Accepted |
| HOME-DEC-005 | Garage GE fridge as overflow destination | Accepted |
| HOME-DEC-006 | Purge before bins — incremental Step 0 approach | Accepted |

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 1.0.0 | 2026-03-26 | Initial CLAUDE.md — thin asset repo post-Cortex absorption |
