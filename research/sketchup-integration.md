---
title: SketchUp Integration Research
date: 2026-03-14
status: initial-research
tags: [sketchup, 3d-modeling, tools, integration]
---

# SketchUp Integration Research

## Context

Evaluated programmatic integration options with SketchUp (https://app.sketchup.com) for the hOme projects repo.

## Key Finding

The **free web app** (`app.sketchup.com`) is a closed environment — no API, no extensions, no programmatic access. Meaningful integration requires SketchUp Pro (desktop).

## Integration Options

### 1. SketchUp MCP Server (Most Promising)
- **Repo:** [mhyrr/sketchup-mcp](https://github.com/mhyrr/sketchup-mcp)
- **Requires:** SketchUp Pro desktop (~$399/yr)
- **How it works:** Ruby extension runs TCP server inside SketchUp; Python MCP server bridges Claude ↔ SketchUp
- **Capabilities:** Create/modify geometry, apply materials, inspect scenes, execute arbitrary Ruby code
- **Notable fork:** [BearNetwork-BRNKC/SketchUp-MCP](https://github.com/BearNetwork-BRNKC/SketchUp-MCP) — woodworking-focused with joinery tools (dovetail, mortise-and-tenon, finger joints)

### 2. C SDK (Headless)
- **Cost:** Free download
- **Use case:** Read/write `.skp` files without SketchUp running
- **Good for:** Batch processing, format conversion, server-side geometry extraction
- **Language:** C/C++

### 3. Trimble Connect REST API
- **Requires:** Pro + corporate domain credentials (personal subscribers not eligible)
- **Capabilities:** CRUD for projects/folders/files, BIM metadata queries, task management
- **Auth:** Trimble Identity (OAuth2)
- **Docs:** https://developer.trimble.com/docs/connect/

### 4. Ruby API (Desktop Extensions)
- **Requires:** SketchUp Pro or Studio
- **Use case:** Build custom in-app extensions
- **Access:** Full model access — geometry, entities, layers, components, materials, scenes
- **Docs:** https://ruby.sketchup.com/

## File Format Support

| Format | Import | Export | Notes |
|--------|--------|--------|-------|
| `.skp` | Native | Native | SketchUp native format |
| `.glTF` / `.glb` | Pro+ | Pro+ | PBR materials (2025+) |
| `.usdz` | Pro+ | Pro+ | Apple Vision Pro compatible |
| `.dwg` / `.dxf` | Pro+ | Pro+ | CAD interchange |
| `.ifc` | Pro+ | Pro+ | BIM standard |
| `.stl` | Plugin | Plugin | 3D printing |
| `.obj` | Extension | Pro+ | Mesh format |
| `.fbx` | Pro+ | Pro+ | Game engines |

## Tier Comparison (Relevant Features)

| Feature | Free (web) | Go | Pro | Studio |
|---------|------------|-----|-----|--------|
| Extensions/API | None | None | Yes | Yes |
| DWG/DXF | No | No | Yes | Yes |
| glTF/USDZ (PBR) | Limited | Limited | Yes | Yes |
| Commercial use | No | Yes | Yes | Yes |
| Price | $0 | ~$19.99/mo | ~$399/yr | ~$819/yr |

## Current Approach

Without SketchUp Pro, the hOme repo can still:
- Track project specs (dimensions, materials, costs)
- Store `.skp` file references
- Generate materials/cut lists
- Create diagrams via Mermaid or Excalidraw

## Next Steps

- [ ] Evaluate whether SketchUp Pro is worth the investment for home projects
- [ ] Test the MCP server with a trial/demo if available
- [ ] Explore the woodworking fork for joinery-specific features
- [ ] Consider alternative free 3D tools with better API access (FreeCAD, Blender)
