> **DEPRECATED (2026-03-16):** This file is retired per ADR-005. Session orientation is now automated — run `/next` to query PostgreSQL tasks + latest session chronicle. This file is preserved for historical reference only.

---

# Next Session Entry Point

**Last Updated:** 2026-03-14
**Updated By:** Claude Opus 4.6

---

## Current Focus

**Goal:** Continue kitchen renovation planning — sensory profile current kitchen, analyze STL design dimensions, and check Pinterest API trial approval
**Primary Document:** research/home-data-strategy.md

---

## Context

- hOme repo bootstrapped from scratch: public GitHub repo, floor plans, research docs, PostgreSQL `home_spaces` table (31 spaces), STL pipeline
- Kitchen renovation is the first active project — SketchUp design loaded (First Floor - v1.stl, 104MB), cross-section views generated, 25 kitchen devices linked
- Pinterest API trial access submitted 2026-03-14, expecting approval ~2026-03-16
- Living room sensory profiled as baseline reference (all excellent, HA-integrated)
- 3 architectural decisions captured (HOME-DEC-001 through 003)

---

## Next Actions

1. **Check Pinterest trial access** — if approved, get App Secret, run `pinterest_test.py auth` (log in as personal account), test `boards` command
2. **Sensory profile the kitchen** — rate lighting/noise/clutter/temperature/feel, compare to living room baseline (task: task-home-sensory-profile-1f-primary)
3. **Analyze kitchen STL geometry** — extract room dimensions, counter runs, appliance bay positions from cross-sections
4. **Continue sensory walk-throughs** — family room, dining room, sun room, library (remaining 1F primary rooms)
5. **Map devices to rooms during walk-throughs** — update devices.space_instance_id for workspace devices, computing, personal care
6. **Build sketchup_analyze.py** — formalize the STL → geometry → PostgreSQL enrichment pipeline

---

## Key References

- research/home-data-strategy.md — full architecture and schema design
- research/pinterest-integration.md — Pinterest API strategy + OAuth walkthrough
- research/sketchup-integration.md — SketchUp options evaluated
- Kitchen Reno/ — STL file, cross-section PNGs
- Floor Plans/ — original MLS floor plans (3 levels)
- scripts/pinterest/pinterest_test.py — Pinterest API test CLI
- scripts/sketchup_screenshot.py — Playwright screenshot tool (interactive mode)
- ~/.env — Pinterest credentials (PINTEREST_APP_ID, etc.)

---

## First Action

Check Pinterest developer portal for trial access approval. If approved, update ~/.env with App Secret and run the OAuth flow.
