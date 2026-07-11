---
title: "Home Appliance Organization Research — Cold Storage & Device Registry"
project: hOme
created: 2026-03-25
status: active
device_id: ba424f6c-a412-46eb-b702-7064f0f4d50d
model: FFUE2024AWA
tags: [freezer, organization, costco, inventory, grocy, bins, research, samsung, ge, homelabs, magic-chef, dyson, hoto, vacuum, smartthings, robot-vacuum]
---

# Home Appliance Organization Research — Cold Storage & Device Registry

## Table of Contents

1. [Device Identification — Frigidaire Upright Freezer](#1-device-identification--frigidaire-upright-freezer)
   - [Cabinet Dimensions](#cabinet-dimensions-from-label)
   - [Interior Layout](#interior-layout-from-photos)
   - [Interior Dimensions (Confirmed 2026-03-25)](#interior-dimensions-confirmed-2026-03-25)
2. [Household Cold Storage Fleet](#2-household-cold-storage-fleet)
   - [Fleet Overview](#fleet-overview)
   - [Unit 1: Frigidaire Upright Freezer (Basement)](#unit-1-frigidaire-upright-freezer-basement)
   - [Unit 2: Samsung Bespoke 4-Door French Door (Main Kitchen)](#unit-2-samsung-bespoke-4-door-french-door-main-kitchen)
   - [Unit 3: Magic Chef Mini Fridge (LPS Office)](#unit-3-magic-chef-mini-fridge-lps-office)
   - [Unit 4: hOmeLabs Beverage Refrigerator (Q's Office)](#unit-4-homelabs-beverage-refrigerator-qs-office)
   - [Unit 5: GE French Door Refrigerator (Garage)](#unit-5-ge-french-door-refrigerator-garage)
3. [API & Services Landscape](#3-api--services-landscape)
   - [Appliance Dimension APIs](#appliance-dimension-apis)
   - [Smart Appliance / IoT APIs](#smart-appliance--iot-apis)
   - [Grocery & Inventory APIs](#grocery--inventory-apis)
   - [Product/Barcode APIs](#productbarcode-apis)
   - [Container/Bin Sizing](#containerbin-sizing)
   - [Key Gap in the Ecosystem](#key-gap-in-the-ecosystem)
4. [Community Best Practices](#4-community-best-practices)
   - [Zone Organization](#zone-organization)
   - [Temperature Reality](#temperature-reality)
   - [FIFO (First In, First Out)](#fifo-first-in-first-out)
   - [Bin Selection](#bin-selection)
   - [Labels That Actually Survive](#labels-that-actually-survive)
   - [Inventory Tracking Tools](#inventory-tracking-tools)
   - [Freezer → Grocery List Automation](#freezer--grocery-list-automation)
   - [Multi-Fridge/Freezer Strategy](#multi-fridgefreezer-strategy)
   - [Top Pitfalls to Avoid](#top-pitfalls-to-avoid)
5. [Related Devices Registered](#5-related-devices-registered)
   - [Samsung Jet Bot R2 Clean 2 Robot Vacuum](#samsung-jet-bot-r2-clean-2-robot-vacuum)
   - [HOTO BlowVac Handheld Vacuum & Air Duster](#hoto-blowvac-handheld-vacuum--air-duster)
   - [Dyson V8 Absolute Cordless Stick Vacuum](#dyson-v8-absolute-cordless-stick-vacuum)
6. [Recommended Approach](#6-recommended-approach)
   - [Phase 1: Physical Organization (Week 1)](#phase-1-physical-organization-week-1)
   - [Phase 2: Digital Foundation (Week 2-3)](#phase-2-digital-foundation-week-2-3)
   - [Phase 3: Multi-Fridge/Freezer Expansion (Week 4+)](#phase-3-multi-fridgefreezer-expansion-week-4)
   - [Phase 4: Automation (Future)](#phase-4-automation-future)
7. [Sources & References](#7-sources--references)

---

## 1. Device Identification — Frigidaire Upright Freezer

- **Brand:** Frigidaire (by Electrolux Home Products)
- **Model:** FFUE2024AWA
- **Type:** 20 cu. ft. Upright Freezer
- **Serial:** 8D41F17443
- **Manufactured:** April 2024
- **Refrigerant:** R600a
- **Electrical:** 115V, 60Hz, 2.0 Amps, 340W
- **Cooling System:** EvenTemp
- **Location:** Basement (space-ll-mechanical)
- **DB Instance ID:** `ba424f6c-a412-46eb-b702-7064f0f4d50d`
- **Photos:** `LPS/IMG_0981.HEIC` through `LPS/IMG_0986.HEIC`

### Cabinet Dimensions (from label)

| Measurement | Imperial | Metric |
|------------|----------|--------|
| Height (top of hinge cover with rollers) | 71 3/4" | 182.2 cm |
| Height (top of door with rollers) | 71 1/8" | 180.7 cm |
| Width | 32 5/8" | 82.7 cm |
| Depth (including doors, without handles) | 28 1/4" | 71.8 cm |

Dimensions may vary 1/4" (6.4mm).

### Interior Layout (from photos)

- 4 shelves creating ~5 tiers of storage space
- Door shelves/bins on the inside of the door
- Wire shelves with clear plastic bin dividers on bottom sections
- EvenTemp cooling system visible on back wall
- Current state: mix of smoked pulled pork, lobster sliders, various meats, frozen veggies, assorted Costco items — mostly unstacked, hard to identify at a glance

### Interior Dimensions (Confirmed 2026-03-25)

Measured via voice memo while standing at the unit. Transcribed via OpenAI Whisper.

| Measurement | Value | Notes |
|-------------|-------|-------|
| **Shelf usable width** | 26.5" | Center shelf measurement |
| **Shelf usable depth** | 16" | Front to back usable space |
| **Total usable height** | 47" | Bottom of bin to top of usable space |
| **Bottom wire bin width** | 27" | Slightly wider than shelves |
| **Bottom wire bin height** | 10" | Fixed bin at bottom |
| **Door/side panel width** | 25.5" | Interior door shelf width |
| **Door/side panel depth** | 4.5" | Door bin depth |
| **Number of adjustable shelves** | 4 | Fully repositionable |
| **Height across 4 shelves** | 34" | Bottom shelf to top shelf |

**Key insight:** Shelves are fully adjustable — the 47" total usable height is a blank canvas. Current shelf placement has dead space from poorly fitting retail packages. Zone layout will be designed around bin selection, not current shelf positions.

**Source:** Voice memo `LPS/29 Walker Ln 28.m4a`, transcribed 2026-03-25.

---

## 2. Pre-Organization Audit Notes

*Captured 2026-03-25 — thinking-out-loud context that shapes the zone design.*

### The Core Problem

The freezer always appears full, yet a Costco trip is always pending. This is a **visibility problem, not a capacity problem.** The freezer is filled with a mix of:

1. **Staples (high rotation)** — the "Lego pieces" that combine into meals:
   - **Proteins (cook-from-scratch):** steak, ground beef, chicken (bought raw at Costco, opened, seasoned, vacuum sealed at home, cooked sous vide with the Breville Joule — registered device: `4f86c2a9-084c-425d-b31e-d564f602e185`)
   - **Starches/bases:** plantains, cauliflower rice
   - **Vegetables:** various frozen veggies
   - **Ingredients:** butter, cream cheese, jalapeños (things that go *into* a dish)
   - **Grab-and-go snacks:** beef sticks, ham, turkey slices (eaten as-is or minimal prep)
   - **Prepared meals:** pre-made meals that are actually in the rotation
2. **One-off impulse buys (low/no rotation)** — frozen meals, specialty Costco items that sounded good but rarely get eaten (e.g., lobster sliders, smoked pulled pork, slow cooker meals visible in photos).
3. **Dead inventory** — items buried for months, potentially freezer-burned, forgotten.

### Why This Matters for Zone Design

- The zone system must be optimized for the **sous vide staples workflow**, not general frozen food storage.
- One-off meals aren't a "zone" — they're clutter that masks true stock levels of staples.
- The reason Costco trips feel overdue despite a full freezer: **staples are buried under things that never get consumed.**

### The Sous Vide Workflow (Primary Consumption Pattern)

```text
Costco bulk purchase → Open packages → Season proteins → Vacuum seal into portions → Store in freezer → Pull for sous vide (Joule) → Cook & eat
```

This workflow defines what "organized" means for this household: clear visibility on **what meal building blocks are in stock, in what quantities, and how old they are.** The freezer is a "mise en place pantry" — not organized by food category but by **visibility and access frequency.** You should be able to glance in and know "I have the Lego pieces to make X tonight" or "I'm low on plantains, add to the Costco list."

### Revised Operational Plan

*Updated 2026-03-25 — realistic phased approach that respects frozen food constraints.*

**Key constraint:** This is frozen perishable food, not a closet cleanout. You can't pull everything out and analyze it on the counter. Every step must minimize thaw risk.

#### Step 0: Noise Removal (do first — lowest friction)

Open the basement freezer and remove everything you know you're NOT going to eat. Move it to the garage GE French Door freezer section (7.3 cu ft). No sorting, no bins, no shelf rearranging — just declutter.

```text
Open basement freezer
  └─ "Are we actually going to eat this?"
      ├─ No  → garage freezer (or trash if freezer-burned)
      └─ Yes → stays
```

**Why this is Step 0:** Eliminates 100% of the noise. After this, you can actually see your staples and assess what you're working with. Takes 5-10 minutes, zero thaw risk for keepers.

**Before/after:** Photograph the freezer before and after Step 0 to see how much space freed up.

#### Step 1: Assess What Remains

After noise removal, photograph what's left. This is your real inventory — the Lego pieces you actually cook with. Note:
- What categories remain (proteins, veggies, starches, ingredients, snacks)?
- Roughly how much of each?
- What's taking the most space?

#### Step 2: Buy a Mix of Bins

Based on what you see after Step 0+1, buy a variety of bin sizes (not all one size). Start with a small order — maybe 6-8 bins across 2-3 size categories. See Bin Catalog section for options.

#### Step 3: Rough Zone Placement

Place bins on shelves, group food loosely by category. This is a hypothesis, not a commitment:
- Proteins (highest rotation) at eye-level or most accessible shelf
- Grab-and-go snacks where they're easy to reach
- Bulk/reserve items lower
- Ingredients wherever they fit

**Work shelf-by-shelf** to minimize food exposure time. Pull one shelf's worth, place into bins, put back. Move to next shelf.

#### Step 4: Live With It (1-2 weeks)

Use the freezer normally. Notice:
- "This bin is too wide for what I put here"
- "I keep reaching past X to get to Y"
- "This category needs more space than I gave it"

Swap, resize, rearrange as needed.

#### Step 5: Lock & Label (Cricut Maker 3)

Only once the layout feels right after real-world testing:
- Design vinyl labels in Cricut Design Space
- Cut and apply to bins
- Permanent — but earned through testing
- Cricut Maker 3 registered: `dd5e75e5-27db-4095-a706-c8214a8bf084`

#### Step 6: Align Costco Trips with New Zones

The freezer will be lowest right before a Costco run. This is the ideal time to:
- Verify what's actually low (visible now that bins are labeled)
- Build the Costco list from what zones are depleted
- Restock directly into the correct zones

#### Operational Timing Tip

**Best time to do Step 0-3:** Right before a scheduled Costco trip, when the freezer is naturally at its lowest. Less food to move = less thaw risk. Then the Costco haul goes directly into the new organized zones.

#### Overflow Capacity

| Unit | Available Freezer Space | Role |
|------|------------------------|------|
| Garage GE French Door | 7.3 cu ft freezer section | Absorb one-offs and dead inventory from Step 0 |
| Samsung Kitchen | 9.0 cu ft freezer drawer | Emergency overflow if needed |
| Coolers + ice | Variable | Backup for full cleanout scenarios |

### Garage Fridge as Overflow — CONFIRMED

The garage GE French Door (7.3 cu ft freezer section) is now confirmed as the overflow destination for frozen meals and one-offs.

### Key Discovery (2026-03-25 — during Step 0)

While executing Step 0 (noise removal), a critical insight emerged from a real dinner conversation:

**The frozen meals are operationally incompatible with how this household eats.**

- Frozen meals require 1-2 days of advance thawing in a regular fridge before cooking
- This household makes dinner decisions same-day ("what do we want tonight?")
- Meals are assembled from components (Lego pieces), not thawed from pre-made frozen packages
- Example: tonight's dinner was Costco cheese pizza + fresh toppings from the fridge — flexible, not planned days ahead
- Therefore: **frozen meals were never going to get eaten** — not because they're bad, but because they don't fit the decision-making pattern

**First migration trip completed 2026-03-25.** One bag of frozen meals moved to garage fridge. Observation: the MAJORITY of food in the basement freezer fits this "requires advance planning" criteria. Continuing migration over the next day or two.

### Revised Scope

This discovery fundamentally changes the project:

| Before | After |
|--------|-------|
| "Organize a full, chaotic freezer" | "Curate a small, high-rotation staples cache" |
| 6 categories across 5 shelves | Possibly 3-4 categories, much less food |
| Complex bin system needed | Simpler system, fewer bins |
| Zones designed around variety | Zones designed around the sous vide + component cooking workflow |

**What remains after migration will be:** proteins (steak, ground beef, chicken), plantains, cauliflower rice, veggies, cheese, butter, cream cheese, jalapeños, snack items (beef sticks, ham, turkey). These are the Lego pieces — the building blocks for same-day flexible cooking.

### Garage Freezer Role (Confirmed)

The garage GE French Door freezer section is now the "maybe someday" overflow:
- Frozen meals that could be thawed if you plan 1-2 days ahead
- One-off Costco impulse buys
- Items that don't fit the daily cooking workflow
- NOT blocking the basement freezer's primary mission

### Next Steps (Updated)

1. Continue Step 0 migration trips (move remaining frozen meals to garage)
2. Once cleared, photograph what remains — the true staples inventory
3. Assess how much space the staples actually need (may be much less than expected)
4. Design zones and buy bins based on the ACTUAL remaining inventory, not the pre-migration chaos
5. Brainstorm from updated photos

---

## 3. Household Cold Storage Fleet

### Fleet Overview

| Unit | Location | Type | Capacity | DB ID | Status |
|------|----------|------|----------|-------|--------|
| Frigidaire FFUE2024AWA | Basement | Upright Freezer | 20 cu. ft. | `ba424f6c-a412-46eb-b702-7064f0f4d50d` | Fully documented; 26.5"W × 16"D × 47"H (confirmed) |
| Samsung RF90F29AEW/AA | Main Kitchen | Bespoke 4-Door French Door | 29 cu. ft. | `312d7a4b-e674-421e-821d-681d53dce13b` | Registered; interior dims unpublished |
| Magic Chef (model TBD) | LPS Office | Compact Mini Fridge | Unknown | `38116022-5e72-42ff-8720-25a6fbc324d2` | Model identification pending |
| hOmeLabs HME020019N | Q's Office | Beverage Refrigerator | 3.2 cu. ft. | `89601009-7527-4ec2-aeda-fda4b7a4a73d` | Fully documented incl. interior dims |
| GE GNE25JSKSS (likely) | Garage | French Door + Bottom Freezer | 24.7 cu. ft. | `e6a2a025-13b5-49ce-a91c-312edc7802b1` | Exact model pending label check |

### Unit 1: Frigidaire Upright Freezer (Basement)

Fully documented in [Section 1](#1-device-identification--frigidaire-upright-freezer) above. This is the primary bulk/reserve freezer — the organizational focus of this document.

### Unit 2: Samsung Bespoke 4-Door French Door (Main Kitchen)

- **Brand:** Samsung (Electrolux)
- **Model:** RF90F29AEW/AA
- **Type:** Bespoke 4-Door French Door with AI Family Hub+ & AI Vision Inside
- **DB Instance ID:** `312d7a4b-e674-421e-821d-681d53dce13b`
- **Photos:** `LPS/IMG_0989.HEIC` (label)

**Capacity:**

| Zone | Capacity |
|------|----------|
| Refrigerator | 16.5 cu. ft. |
| FlexZone | 3.1 cu. ft. |
| Freezer | 9.0 cu. ft. |
| **Total** | **29.0 cu. ft.** |

**Exterior Dimensions:**

| Measurement | Imperial |
|------------|----------|
| Height | 70 1/4" |
| Width | 35 3/4" |
| Depth | 34 1/4" |

**Interior Dimensions:** Not published by Samsung.

**Shelving:** 3 tempered glass spill-proof shelves + 1 slide-in shelf

**Smart Features:**
- AI Family Hub+ with 32" touchscreen
- AI Vision Inside — internal cameras for food tracking and inventory recognition
- Wi-Fi / SmartThings connected
- Dual ice maker: Ice Bites + Cubed
- Finish: White Glass (Bespoke panels)

**Note:** AI Vision Inside has potential SmartThings API integration for automated food inventory — could feed directly into LifeOS without manual barcode scanning. See [Phase 4: Automation](#phase-4-automation-future).

### Unit 3: Magic Chef Mini Fridge (LPS Office)

- **Brand:** Magic Chef or Master Chef (label partially readable)
- **Model:** Unknown — identification pending
- **Type:** Compact beverage mini fridge
- **Location:** LPS Office
- **DB Instance ID:** `38116022-5e72-42ff-8720-25a6fbc324d2`
- **Photos:** `LPS/IMG_0988.HEIC` (interior top-down view)
- **Status:** Model identification pending — need to locate model number on label (typically inside door frame or on rear panel)

### Unit 4: hOmeLabs Beverage Refrigerator (Q's Office)

- **Brand:** hOmeLabs
- **Model:** HME020019N / HME030065N
- **Type:** 120-Can Beverage Refrigerator with Glass Door
- **Location:** Q's Office
- **DB Instance ID:** `89601009-7527-4ec2-aeda-fda4b7a4a73d`

**Exterior Dimensions:**

| Measurement | Imperial |
|------------|----------|
| Height | 33.3" |
| Width | 18.9" |
| Depth | 17.3" |

**Interior Dimensions (confirmed — rare data):**

| Measurement | Imperial |
|------------|----------|
| Height | 29" |
| Width | 16" |
| Depth | 12" |

**Features:**
- Capacity: 3.2 cu. ft. (~70-80 cans realistically)
- 3 removable chrome wire shelves (adjustable)
- Temperature: Down to 34°F
- Digital LED temperature control
- Auto-defrost
- Power: 115V/60Hz, 75W (compressor-based)
- Finish: Matte silver stainless frame, black cabinet, tempered glass door

### Unit 5: GE French Door Refrigerator (Garage)

- **Brand:** GE
- **Model:** GNE25JSKSS (most likely, unconfirmed) — could also be GNE27JSKSS
- **Type:** French Door with bottom freezer drawer
- **Location:** Garage
- **DB Instance ID:** `e6a2a025-13b5-49ce-a91c-312edc7802b1`
- **Photos:** `LPS/IMG_0991.HEIC` (interior), `LPS/IMG_0992.HEIC` (control panel), `LPS/IMG_0993.HEIC` (manual shelf page), `LPS/IMG_0995.HEIC` (XWF data sheet)

**Capacity (if GNE25JSKSS):**

| Zone | Capacity |
|------|----------|
| Refrigerator | 17.4 cu. ft. |
| Freezer | 7.3 cu. ft. |
| **Total** | **24.7 cu. ft.** |

**Exterior Dimensions (if GNE25JSKSS):**

| Measurement | Imperial |
|------------|----------|
| Width | 32 3/4" |
| Height | 69 7/8" |
| Depth (with handle) | 37 1/2" |

**Interior Dimensions:** Not published by GE.

**Features:** Turbo Cool, Door Alarm, Digital Temp Display, Internal Water Dispenser, XWF water filter

**Identification method:** Identified via manual pages (shelf configs for GNE25/GNE27/GFE26/GFE28), control panel features, and XWF filter data sheet.

**Status:** Exact model pending — check label on left wall of fresh food compartment or behind crisper drawers.

**Note:** XWF filter is only used in GE French-door and side-by-side lines, never top-freezers — this helps narrow the model family even without the label.

---

## 3. API & Services Landscape

### Appliance Dimension APIs

**Key finding:** No API returns normalized interior refrigerator dimensions (shelf spacing, zone heights, drawer dimensions). This data exists in manufacturer spec sheets (PDFs) but hasn't been structured and exposed via any API.

| Service | What It Does | Interior Dims? | Free? | Verdict |
|---------|-------------|----------------|-------|---------|
| **Skulytics.io** | Appliance specs by model, 300+ brands | Exterior only | 1K calls/mo free | Best for model lookup |
| **appliance.io** | B2B appliance product data platform | Exterior only | Paid SaaS | Overkill for personal use |
| **appliance-data.com** | Appliance model number data API | Exterior only | Unknown | Evaluate alongside appliance.io |
| **Dimension Express** (dexpress.com) | 43K+ spec sheets & CAD files (since 1993) | Yes — in PDFs | Free guest tier | Best raw source, but PDFs not structured API |
| **Homespy.io** | Serial number decoder (age/identity from serial) | No | Unknown | Niche — serial decode only |

### Smart Appliance / IoT APIs

Not relevant for Frigidaire FFUE2024AWA (not a connected appliance), but relevant for the Samsung Bespoke and GE garage fridge:

| Service | Brands | Notes |
|---------|--------|-------|
| **Electrolux Developer Portal** (developer.electrolux.one) | Frigidaire, AEG, Electrolux | IoT control/status, not spec lookup. Python: `pyelectroluxconnect` |
| **GE SmartHQ** | GE, Profile, Café, Haier | IoT only. SDKs: `gekitchen` (Python), `gehomesdk`, `gea-sdk` (Node) |
| **Samsung SmartThings** | Samsung | REST API + SmartThings SDK — covers Bespoke fridge + Jet Bot R2. AI Vision Inside may expose inventory data. |
| **Home Connect** | Bosch, Siemens, Thermador | First major maker to open APIs for home automation |

### Grocery & Inventory APIs

| Service | What It Does | Costco? | Verdict |
|---------|-------------|---------|---------|
| **Grocy** (grocy.info) | Self-hosted "ERP beyond your fridge" — stock tracking, barcode scanning, shopping lists, meal planning. Full REST API. **MCP server exists** (`mcp-grocy-api` on GitHub) | No native integration | **Top pick** for inventory layer |
| **Instacart Developer Platform** | 85K+ stores, 1B+ products, real-time shelf-level inventory. Launched March 2024. | Costco is on Instacart | High value but requires partnership approval (~3 weeks) |
| **Open Food Facts** | Open-source food product database | No | Useful for nutrition/barcode lookup |

### Product/Barcode APIs

| Service | Notes |
|---------|-------|
| **Go-UPC** | Free tier. Returns product name, category, basic dims. Not interior specs. |
| **Barcode Lookup / Barcode Spider** | Paid plans. Shipping box dimensions, not interior. |
| **UPCitemdb** | General product data by UPC/EAN/ASIN |

### Container/Bin Sizing

**BinSizes.com** — search bins by exact W×D×H across Amazon/Target/Walmart. No API, consumer-facing search tool only. The concept is exactly right — could scrape once to build a local bin-matching table.

### Key Gap in the Ecosystem

Nobody has built the **interior fridge dimensions → zone map → matching bins** pipeline as an API. Appliance APIs stop at exterior dimensions. Grocery/inventory apps start at "what's in the bin" but don't help you pick the bin. The middle layer — the physical schematic — is an unsolved problem.

---

## 4. Community Best Practices

### Zone Organization

The dominant pattern is **shelf-per-category** with 5-6 zones max.

**Recommended zone layout for upright freezer (top to bottom):**

| Shelf | Zone | Rationale |
|-------|------|-----------|
| Top | Bread, baked goods, ice cream | Easy grab, less critical temp zone |
| Upper-mid | Ready meals / meal prep | High rotation |
| Middle | Vegetables & fruit | Medium rotation |
| Lower-mid | Poultry & fish | Colder zone, denser items |
| Bottom | Red meat & bulk proteins | Coldest zone (cold air falls) |
| Door bins | Fast-turnover only (ice packs, waffles) | Warmest zone — temp cycles with door opens |

**Category system depends on household use pattern:**

| If you mostly... | Use this system |
|---|---|
| Buy in bulk (Costco) and cook from scratch | **Protein-type zones** — chicken, beef, pork, fish each get own bin |
| Meal prep in batches and reheat | **Meal-based zones** — breakfast, lunch, dinner, components |
| Mixed household | **Hybrid** — one shelf raw proteins by type, one shelf prepped meals, one shelf produce |

### Temperature Reality

Upright freezers are **not temperature-uniform:**
- Back is colder than front
- Bottom is generally colder than top (cold air falls)
- Door bins experience the most temperature cycling
- Ideal fill level: 75-80% full (over-packing blocks airflow; under-packing wastes energy)

**Practical implications:**
- Long-term storage (bulk meat, expensive proteins) → bottom/back
- High-rotation items (frozen veggies, bread, grab-and-go) → middle/upper shelves near front
- Door bins → only things used fast and replaced often

### FIFO (First In, First Out)

The single most consistently cited best practice:
- New purchases go **behind** existing stock
- Label everything with **date frozen**, not just what it is
- Bins create natural FIFO channels — older items migrate to front
- In a 2-deep bin setup (front = active, back = reserve), FIFO happens automatically

### Bin Selection

**Clear wins overwhelmingly** — see contents at a glance, monitor for freezer burn, notice low stock without formal inventory check.

**Top products for ~32"W × ~25"D interior:**

| Bin | Size | Layout per Shelf | Price | Notes |
|-----|------|-----------------|-------|-------|
| **YouCopia FreezeUp 15"** | 15" wide | 2 side-by-side (30" + 2" gap) | ~$20-25 each | Adjustable dividers, integrated handle |
| **YouCopia FreezeUp 12"** | 12" wide | 2 per shelf + gap, or mix 12"+15" | ~$20-25 each | Same quality, narrower |
| **iDesign Linus** | 10" × 6" × 5" | 3 across (30" + 2" margin) | ~$15-20 for 4-pack | Available at Costco! Simpler, durable |
| **Wire baskets w/ handles** | Various | Good airflow, reduces frost | Varies | Popular in hunting community; wire can snag vacuum-seal bags |

**2-deep layout:** With ~25" interior depth, two bins front-to-back per shelf works well. Front = "current/active," Back = "reserve." Natural FIFO.

### Labels That Actually Survive

Standard adhesive fails within 60-90 days at freezer temperatures. What works:

- **Freezer-grade tape** (rubber or hot-melt adhesive rated for 0°F)
- **Apply to dry surface** — condensation prevents adhesion; label before item gets cold
- **Solvent-based permanent markers** on masking tape survive longer than label adhesives alone
- **Lab-grade cryogenic labels** (LabTAG brand) — overkill but perfect; used in scientific freezers
- **Best strategy: label the BIN, not the item** — permanent laminated card on bin face, with whiteboard/chalkboard label for updating contents

### Inventory Tracking Tools

| Tool | Stack | Verdict |
|------|-------|---------|
| **Grocy** (standalone Docker) | Self-hosted, full REST API, MCP server | Most mature; HA add-on deprecated May 2025, run standalone |
| **simple_inventory** (HA integration) | HA custom component | Lightest viable — threshold → auto-add to HA to-do list |
| **PantrLytics** (HA add-on) | Home Assistant | Most data-driven: dashboards, expiry analytics, label printing via IPP |
| **Mealie** | Self-hosted Docker | Primarily recipe-focused, not inventory-first; has barcode via ESPHome |
| **KitchenOwl** | Flutter + Flask | Household collaboration focus |
| **Spreadsheets** | Any | **Die in 2-4 weeks.** Friction too high. |
| **Notion** | Cloud | Pretty but fails for daily operations without barcode scanning |

### Freezer → Grocery List Automation

Best automated path (HA ecosystem):
1. Item quantity drops below threshold in Grocy/simple_inventory
2. Auto-adds to a **store-specific** shopping list (separate "Costco list" from "weekly grocery")
3. Set minimum stock to **2-3 units, not 0** — gives lead time before a Costco run
4. HA companion app surfaces the list on mobile
5. Optional: HA notification fires when threshold crossed

**DIY barcode scanner:** ESPHome barcode scanner project by MattFryer — scans items, auto-adds to HA shopping list synced with Mealie. Requires soldering but eliminates all manual entry friction.

### Multi-Fridge/Freezer Strategy

**Assign roles, not categories.** Don't try to unify category systems across units.

| Unit | Role | Contains |
|------|------|----------|
| Kitchen freezer (Samsung Bespoke — attached) | Active stock — daily access | Current meal prep, frozen veggies, breakfast items, ice cream |
| Basement upright (Frigidaire FFUE2024AWA) | Reserve / warehouse — weekly restock | Costco bulk proteins, bulk veggies, long-horizon items |
| Garage fridge (GE French Door) | Overflow / beverages / secondary active | Drinks, overflow produce, backup stock |
| Q's Office (hOmeLabs beverage cooler) | Beverages only | Canned/bottled beverages, single-serve items |
| LPS Office (Magic Chef mini fridge) | Personal office stock | Grab-and-go, personal beverages |

**Key workflow:** Restock kitchen freezer FROM basement freezer. Treat basement as warehouse, kitchen as shop floor. Track locations separately so "low stock" in kitchen triggers "transfer from basement" vs. "buy from store."

### Top Pitfalls to Avoid

**Physical:**
1. Labels falling off — use freezer-grade tape or label the bin, not items
2. Too many categories at launch — start with 5-6, subdivide only if bins overflow
3. Blocking air vents — leave 1-2" clearance behind bins
4. Overpacking bins to the rim — "avalanche bins" that spill; fill to 80%
5. Categories that don't match actual use patterns — organize by meal occasion or heat method, not provenance
6. Door bins for anything that matters — reserve for fast-turnover items only
7. Frost accumulation on solid-bottom bins — consider wire or open-bottom; quarterly defrost

**Digital:**
1. Over-engineering before testing the habit — start lightest, add complexity after 2+ weeks
2. Household buy-in problem — friction must be near-zero (mounted scanner > phone app)
3. Grocy HA add-on breakage — run standalone Docker, not HACS component
4. Expiry date tracking overreach — track expiry for cooked/seafood only; use "date frozen" for raw meat

---

## 5. Related Devices Registered

### Samsung Jet Bot R2 Clean 2 Robot Vacuum

- **Brand:** Samsung
- **Model:** VR50T95735W/AA
- **Serial:** 09HU8NER900003T
- **Firmware:** RVC.5.1.2 (Secured by Knox)
- **Location:** Kitchen (terracotta tile)
- **DB Instance ID:** `32569d04-f141-4f30-9722-01df91c8a29e`
- **Photos:** `LPS/IMG_0990.HEIC`
- **Smart:** SmartThings connected

**Note:** Part of the Samsung SmartThings ecosystem alongside the Bespoke kitchen fridge — both devices are manageable via a single SmartThings API integration point, which is a meaningful LifeOS simplification. SmartThings becomes the single API for Samsung home devices.

### HOTO BlowVac Handheld Vacuum & Air Duster

- **Brand:** HOTO
- **Model:** B0FXFWPDLF
- **DB Instance ID:** `aaecb4c7-b4af-4675-b73f-8ce60e2037b8`

**Specs:**

| Attribute | Value |
|-----------|-------|
| Motor | 130,000 RPM brushless DC |
| Power | 225W, 18V DC |
| Battery | 2500mAh ×5 Li-ion |
| Charging | USB-C fast charge, ~90 min |
| Dimensions | 5.33" × 2.76" × 11.34" |
| Weight | 2.09 lbs |

**Operating Modes:**

| Mode | Suction | Runtime |
|------|---------|---------|
| Eco | 8,000 Pa | 45 min |
| Standard | 15,000 Pa | 20 min |
| Boost | 23,000 Pa | 10 min |

### Dyson V8 Absolute Cordless Stick Vacuum

- **Brand:** Dyson
- **Model:** 214730-01
- **DB Instance ID:** `984ae36c-86ef-49e5-8197-21deca0133a8`

**Specs:**

| Attribute | Value |
|-----------|-------|
| Motor | Digital Motor V8, 110,000 RPM |
| Suction | 115 Air Watts |
| Cyclones | 15 (HEPA filtration — 99.99% down to 0.1 microns) |
| Battery | 21.6V 6000mAh |
| Dimensions | 49"L × 9.8"H × 8.8"W |
| Weight | 5.75 lbs |

**Runtime:**

| Mode | Runtime |
|------|---------|
| Standard | 40 min |
| Motorized floor tool | 25 min |
| Max power | 7 min |

**Included accessories:** Direct Drive cleaner head, Soft Roller cleaner head, motorized floor tool, combination tool, crevice tool, mini motorized tool, mini soft dusting brush

---

## Bin Catalog — Options by Size Category

*Compiled 2026-03-25 from YouCopia, iDesign, Container Store, Target Brightroom, mDesign, Walmart Mainstays, Amazon. All options verified for 26.5"W × 16"D freezer shelves.*

### Freezer Material Safety

Not all clear plastics survive 0°F. This matters.

| Material | Freezer Safe? | Notes |
|----------|--------------|-------|
| **PETG** (Polyethylene Terephthalate Glycol) | Excellent | Stays clear and flexible at 0°F; best choice |
| **PET / PETE** (Resin #1) | Excellent | Lightweight, shatter-resistant at freezer temps |
| **HDPE** (#2) | Excellent | Usually opaque, but safe |
| **Polypropylene (PP, #5)** | Risky | Standard PP becomes brittle below 0°F; only use if brand explicitly states freezer-safe |
| **Acrylic / PMMA** | No | Cracks and shatters at 0°F — avoid entirely |
| **Polycarbonate (PC)** | Good | Durable but often contains BPA |

**Rule of thumb:** Look for explicit "freezer-safe" labeling + PETG or PET material confirmation.

### Wide Bins (8–9" width)

Best for: proteins, bulk items, high-rotation staples. 2-3 per shelf.

| Product | W × D × H | Price | Freezer-Safe | Material | Source |
|---------|-----------|-------|-------------|----------|--------|
| **YouCopia FreezeUp 15"** | 8.2" × 15.2" × 4.9" | ~$28 | Yes (purpose-built) | BPA-free food-safe | [YouCopia](https://youcopia.com/products/freezeup-freezer-bin-15) / [Amazon](https://www.amazon.com/YouCopia-FreezeUp-Organizer-Food-Safe-Container/dp/B098FXJ5NS) |
| **YouCopia FreezeUp 12"** | 8.2" × 12.2" × 4.9" | ~$23 | Yes (purpose-built) | BPA-free food-safe | [YouCopia](https://youcopia.com/products/freezeup-freezer-bin-12) / [Amazon](https://www.amazon.com/YouCopia-FreezeUp-Organizer-Food-Safe-Container/dp/B098FK8VGK) |
| **YouCopia FreezeUp Rack 15"** | 7.3" × 15.1" × 3.9" | ~$30 | Yes (holds boxes upright) | BPA-free food-safe | [YouCopia](https://youcopia.com/products/freezeup-freezer-rack-15) / [Amazon](https://www.amazon.com/YouCopia-BPA-Free-Organizer-Adjustable-Dividers/dp/B098GGH4CP) |
| **YouCopia FreezeUp Rack 12"** | 7.4" × 12.1" × 3.9" | ~$26 | Yes (holds boxes upright) | BPA-free food-safe | [YouCopia](https://youcopia.com/products/freezeup-freezer-rack-12) / [Amazon](https://www.amazon.com/YouCopia-FreezeUp-Freezer-Rack-Clear/dp/B098G1456X) |
| **Brightroom Large Wide** | 9.14" × 14.5" × 6" | ~$8 | Yes (PETG confirmed) | PETG | [Target](https://www.target.com/p/6-34-x14-5-34-x9-1-34-large-fridge-38-pantry-bin-clear-brightroom-8482/-/A-85318248) |
| **iDesign Linus Pullz 8"** | 8" × 11.5" × 3.5" | ~$12 | Yes | BPA-free plastic | [iDesign](https://idesignlivesimply.com/products/69630-linus-pullz-8-clear) |
| **iDesign Linus 8"** | 8" × 11.5" × 3.5" | ~$12 | Yes | BPA-free plastic | [Container Store](https://www.containerstore.com/s/kitchen/refrigerator-freezer/refrigerator-bins/idesign-linus-deep-fridge-bins/123d?productId=11000497) |
| **mDesign Open-Front Stackable** | 8" × 11" × 5" | ~$14 | Yes | BPA-free shatter-resistant | [mDesign](https://mdesignhomedecor.com/products/open-front-stackable-bin-11-8-5-asm-34045) |
| **The Home Edit Divided Freezer Bin** | ~13.5" × 10" × 6" | ~$28 | Yes (PET) | PET | [The Home Edit](https://thehomeedit.com/products/the-home-edit-divided-freezer-bin) / [Container Store](https://www.containerstore.com/s/kitchen/refrigerator-freezer/the-home-edit-divided-freezer-bin/12d?productId=11012908) |

### Medium Bins (6–7.75" width)

Best for: veggies, starches, ingredients. 3 per shelf or mixed combos.

| Product | W × D × H | Price | Freezer-Safe | Material | Source |
|---------|-----------|-------|-------------|----------|--------|
| **Brightroom Deep Freezer** | 7.4" × 13" × 8.25" | ~$10 | Yes (PETG confirmed) | PETG | [Target](https://www.target.com/p/deep-fridge-38-freezer-bin-clear-brightroom-8482/-/A-85318290) |
| **Brightroom Medium 7.75"** | 7.75" × 14.5" × 4.75" | ~$7 | Yes (PETG confirmed) | PETG | [Target](https://www.target.com/p/7-34-x-14-5-34-x-4-34-medium-fridge-38-pantry-bin-clear-brightroom-8482/-/A-85318242) |
| **Brightroom Small Wide** | 7" × 10.5" × 4" | ~$6 | Yes (PETG confirmed) | PETG | [Target](https://www.target.com/p/7-34-x-10-5-34-x-4-34-standard-fridge-38-pantry-bin-clear-brightroom-8482/-/A-85318243) |
| **iDesign Linus 7" (RPET)** | 7" × 11" × 3.5" | ~$9 | Yes | 51% recycled RPET | [iDesign](https://idesignhome.com/products/rpet-linus-binz-7) |
| **iDesign Linus 6"** | 6" × 11.5" × 3.5" | ~$10 | Yes | BPA-free plastic | [Amazon](https://www.amazon.com/iDesign-Plastic-Container-Organization-BPA-Free/dp/B002BRXYQW) |
| **Mainstays Large (in 6pc set)** | 7.5" × 12" × 4" | ~$3 ea | Yes (PET confirmed) | PET | [Walmart](https://www.walmart.com/ip/Mainstays-6pc-Fridge-Storage-Set-2-12x4-5-2-12x6-2-12x7-5/16815405890) |
| **mDesign Kitchen Bin w/ Handles** | 6" × 10" × 6" | ~$14 | Yes | BPA-free shatter-resistant | [mDesign](https://mdesignhomedecor.com/products/kitchen-storage-bin-with-handles-10-x-6-x-6-asm-9963) |
| **Container Store Everything Organizer Wide** | ~14" × 13" × 5" | ~$17 | Yes | BPA-free | [Container Store](https://www.containerstore.com/s/kitchen/refrigerator-freezer/refrigerator-bins/everything-organizer-wide-stacking-fridge-bins-with-dividers/123d?productId=11027235) |
| **Container Store Everything Organizer Freezer** | ~12" × 8" × 8" | ~$20 | Yes (freezer-specific) | BPA-free | [Container Store](https://www.containerstore.com/s/kitchen/refrigerator-freezer/freezer-safe/everything-organizer-freezer-bin-with-divider/123d?productId=11026867) |

### Slim Bins (5–6" width)

Best for: ingredients (butter, cream cheese, jalapenos), smaller veggies. 4 per shelf.

| Product | W × D × H | Price | Freezer-Safe | Material | Source |
|---------|-----------|-------|-------------|----------|--------|
| **Brightroom 5.5"** | 5.5" × 14.5" × 4.75" | ~$6 | Yes (PETG confirmed) | PETG | [Target](https://www.target.com/p/5-5-34-x14-5-34-x4-34-narrow-fridge-38-pantry-bin-clear-brightroom-8482/-/A-85318241) |
| **iDesign Linus 5.25" (RPET)** | 5.25" × 11" × 3.5" | ~$9 | Yes | 51% recycled RPET | [iDesign](https://idesignhome.com/products/rpet-linus-binz-5-5) |
| **iDesign Linus 5.5"** | 5.5" × 11" × 3.5" | ~$10 | Yes | BPA-free plastic | [Amazon](https://us.amazon.com/iDesign-Organizer-Container-Organization-BPA-Free/dp/B00WSO1ZG4) |
| **Mainstays Medium (in 6pc set)** | 6" × 12" × 4" | ~$3 ea | Yes (PET confirmed) | PET | [Walmart](https://www.walmart.com/ip/Mainstays-6pc-Fridge-Storage-Set-2-12x4-5-2-12x6-2-12x7-5/16815405890) |
| **Container Store Everything Organizer Small** | 5.25" × 11.75" × 4.25" | ~$10 | Yes | BPA-free | [Container Store](https://www.containerstore.com/s/kitchen/refrigerator-freezer/refrigerator-bins/everything-organizer-fridge-bin-with-handle/123d?productId=11026868) |
| **mDesign Pull-Out Drawer** | 6" × 8.5" × 6" | ~$14 | Yes | BPA-free | [mDesign](https://mdesignhomedecor.com/products/stackable-closet-bin-with-pull-out-drawer-8-5-x-6-x-6-asm-40006) |

### Narrow Bins (4–4.5" width)

Best for: snacks, small items, dividers between categories. 5+ per shelf or gap-fillers.

| Product | W × D × H | Price | Freezer-Safe | Material | Source |
|---------|-----------|-------|-------------|----------|--------|
| **Brightroom Small Narrow** | 4.5" × 10.5" × 4" | ~$5 | Yes (PETG confirmed) | PETG | [Target](https://www.target.com/p/4-5-34-x-10-5-34-x-4-34-small-fridge-38-pantry-bin-clear-brightroom-8482/-/A-85318247) |
| **iDesign Linus 4"** | 4" × 11" × 3.5" | ~$8 | Yes | BPA-free plastic | [iDesign](https://idesignhome.com/products/56830-linus-binz-4-clear) / [Amazon](https://www.amazon.com/iDesign-Plastic-Organizer-Container-Organization/dp/B004D8YYSE) |
| **Mainstays Small (in 6pc set)** | 4.5" × 12" × 4" | ~$3 ea | Yes (PET confirmed) | PET | [Walmart](https://www.walmart.com/ip/Mainstays-6pc-Fridge-Storage-Set-2-12x4-5-2-12x6-2-12x7-5/16815405890) |
| **mDesign Slim w/ Handles** | 4" × 16" × 5" | ~$13 | Yes | BPA-free | [mDesign](https://mdesignhomedecor.com/products/stackable-breast-milk-storage-with-handles-16-x-4-x-5-asm-8341) |
| **mDesign Small Pantry** | 4" × 14.5" × 4" | ~$12 | Yes | BPA-free | [mDesign](https://mdesignhomedecor.com/small-plastic-pantry-storage-bin-with-handles-14-5-x-4-x-4/) |

### Value Sets (Multiple Sizes, One Purchase)

| Set | Contents | Price | Material | Source |
|-----|----------|-------|----------|--------|
| **Mainstays 6-piece** | 2×(4.5"W) + 2×(6"W) + 2×(7.5"W) | ~$15 | PET (confirmed) | [Walmart](https://www.walmart.com/ip/Mainstays-6pc-Fridge-Storage-Set-2-12x4-5-2-12x6-2-12x7-5/16815405890) |
| **Brightroom mix-and-match** | 4.5", 5.5", 7", 7.75", 9.14" — all match | ~$5-10 each | PETG (confirmed) | [Target](https://www.target.com/c/refrigerator-storage-freezer-organizers/brightroom/-/N-dvrslZq643le5t6vk) |
| **Heyuzb 8-pack XL** | 8 bins, multiple sizes | ~$38 | PETG (confirmed) | [Amazon](https://www.amazon.com/Heyuzb-Stackable-Organizer-Refrigerator-Organizers/dp/B0CXPK8WP1) |
| **Vtopmart 4L+4N Combo** | 4 large (~7.5"W) + 4 narrow (~4"W) | ~$28 | BPA-free (verify type) | [Amazon](https://www.amazon.com/Refrigerator-Vtopmart-Organizers-Countertops-Organization/dp/B089GXTBZZ) |
| **Sorbus 10-Pack** | Wide + narrow mixed set | ~$45 | BPA-free (verify type) | [Home Depot](https://www.homedepot.com/p/Sorbus-10-Pack-Clear-Plastic-Storage-Bins-for-fridge-and-Pantry-Stackable-organizer-set-FR-SET8/323131938) |

### Shelf Layout Combos (totaling ~26.5" width)

These are example configurations showing how different bin widths can tile across a shelf:

| Combo | Bins | Total Width | Gap | Best For |
|-------|------|-------------|-----|----------|
| **A** | 3× YouCopia FreezeUp (8.2") | 24.6" | 1.9" | Uniform premium — proteins shelf |
| **B** | 2× Brightroom 9.14" + 1× Brightroom 7.75" | 26.0" | 0.5" | All-Target budget — 3 zones |
| **C** | 2× FreezeUp (8.2") + 1× iDesign 6" + 1× iDesign 4" | 26.4" | 0.1" | Mixed premium — 4 zones, tight fit |
| **D** | 4× Brightroom 5.5" + 1× Brightroom 4.5" | 26.5" | 0" | Max visibility — 5 narrow categories |
| **E** | 1× Wide (8.2") + 2× Medium (6") + 1× Narrow (4.5") | 24.7" | 1.8" | Mixed sizes — varied content types |
| **F** | 3× Brightroom 7.75" + 1× Narrow 4.5" | 27.75" | -1.25" | Too snug — needs smaller narrow |
| **G** | 3× Mainstays 7.5" + 1× Mainstays 4.5" | 27" | -0.5" | Slightly snug — may work with flex |

### Recommendation Summary

| Strategy | Bins | Best For | Cost (per shelf) |
|----------|------|----------|-----------------|
| **Premium purpose-built** | YouCopia FreezeUp | Protein zone, highest-rotation shelves | ~$70-90/shelf |
| **Value + confirmed safe** | Brightroom PETG or Mainstays PET | All other shelves | ~$15-30/shelf |
| **Snack zone special** | mDesign pull-out drawer | Grab-and-go shelf (beef sticks, ham) | ~$40-56/shelf |
| **Mix-and-match** | YouCopia for 1-2 key shelves, Brightroom for rest | Full freezer setup | ~$80-150 total |

---

## 6. Recommended Approach

### Phase 1: Physical Organization (Week 1)
1. Interior dimensions confirmed: 26.5"W × 16"D × 47"H. Next: design zone layout and select bins.
2. Create zone schematic (5-6 zones based on current contents and buying habits)
3. Order bins — start with YouCopia FreezeUp 15" (2 per shelf) or iDesign Linus 10" (3 per shelf)
4. Label bins with permanent laminated category cards
5. Sort current contents into zones, photograph the "after" state

### Phase 2: Digital Foundation (Week 2-3)
1. Evaluate Grocy vs simple_inventory vs PantrLytics based on HA integration needs
2. Deploy chosen tool (Docker for Grocy, HA add-on for others)
3. Initial inventory capture — photograph + catalog current contents per zone
4. Set up store-specific shopping lists (Costco list, weekly grocery list)
5. Set minimum stock thresholds for key items (2-3 units)

### Phase 3: Multi-Fridge/Freezer Expansion (Week 4+)

Most units are now registered in PostgreSQL. Remaining work:

**Pending identification/measurement:**
- Magic Chef mini fridge (LPS Office) — model number still needed (check inside door frame or rear panel label)
- GE garage fridge — exact model pending; check label on left wall of fresh food compartment or behind crisper drawers
- Samsung Bespoke RF90F29AEW/AA — interior dimensions not published by Samsung
- GE GNE25JSKSS — interior dimensions not published by GE

**Workflow steps:**
1. Assign roles per the [Multi-Fridge/Freezer Strategy](#multi-fridgefreezer-strategy) table above
2. Set up location-aware tracking (transfer vs. purchase triggers)
3. Build zone schematics for each unit once interior dims are confirmed

### Phase 4: Automation (Future)

1. **SmartThings ecosystem integration:** Samsung Bespoke (AI Vision Inside) + Jet Bot R2 both connect to SmartThings — a single SmartThings API integration could provide automated food inventory from the kitchen fridge cameras + robot vacuum status into LifeOS. High-value, low-friction compared to barcode-scanning alternatives.
2. Instacart Developer Platform application (if Costco ordering desired)
3. ESPHome barcode scanner build (if friction reduction needed for non-Samsung units)
4. HA dashboard for cross-freezer inventory view
5. GE SmartHQ integration for garage fridge (if model confirmed as SmartHQ-compatible)
6. Integration with LifeOS PostgreSQL for unified home management

---

## 7. Sources & References

### Appliance APIs
- [Skulytics.io](https://skulytics.io/) — appliance specs API, 1K free calls/mo
- [appliance.io](https://appliance.io/) — B2B appliance data platform
- [Dimension Express](https://dexpress.com/) — 43K+ appliance spec sheets
- [Homespy.io](https://homespy.io/) — serial number decoder
- [Electrolux Developer Portal](https://developer.electrolux.one/)
- [GE SmartHQ](https://www.smarthqsolutions.com/smarthq-platform-api)
- [Samsung SmartThings API](https://developer.smartthings.com/)

### Inventory & Grocery Tools
- [Grocy](https://grocy.info/) — self-hosted grocery/household management
- [mcp-grocy-api](https://github.com/saya6k/mcp-grocy-api) — Grocy MCP server
- [simple_inventory](https://github.com/blaineventurine/simple_inventory) — HA integration
- [PantrLytics](https://github.com/Psychman52OS/PantrLytics) — HA pantry analytics
- [Instacart Developer Platform](https://www.instacart.com/company/business/developers)
- [BinSizes.com](https://binsizes.com/) — bin search by dimension

### Community Sources
- [HA Community: Pantry/Freezer Tracking](https://community.home-assistant.io/t/pantry-freezer-and-meal-prep-inventory-tracking-in-home-assistant/974858)
- [HA Community: Food in the Freezer Tracker](https://community.home-assistant.io/t/food-in-the-freezer-tracker/589712)
- [HA Community: Freezer Content Dashboard](https://community.home-assistant.io/t/freezer-content/927607)
- [Phil Hawthorne: Automating Shopping List with HA + Grocy](https://philhawthorne.com/automating-your-shopping-list-with-home-assistant-and-grocy/)
- [MattFryer: HA-Mealie-Barcode-Scanner](https://github.com/MattFryer/HA-Mealie-Barcode-Scanner)
- [YouCopia FreezeUp Review — Today.com](https://www.today.com/shop/youcopia-freezeup-freezer-bin-t247146)
- [iDesign Linus at Costco — Tasting Table](https://www.tastingtable.com/2069409/affordable-costco-kitchen-organize-idesign/)
- [Upright Freezer Temp Zones — Fridge.com](https://fridge.com/blogs/news/upright-freezer-organization-for-optimum-temperature)
- [Grocy Alternatives — AlternativeTo](https://alternativeto.net/software/grocy/?license=opensource)
