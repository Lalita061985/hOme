---
title: Pinterest Integration Research
date: 2026-03-14
status: initial-research
tags: [pinterest, inspiration, mood-boards, integration]
---

# Pinterest Integration Research

## Context

Evaluated programmatic integration options with Pinterest (https://www.pinterest.com) for the hOme projects repo — specifically for capturing home project inspiration, mood boards, and design references.

## Key Finding

Pinterest has a **free, well-documented REST API (v5)** with automatic Trial access. Reading your own boards/pins requires only OAuth 2.0 authentication. Multiple MCP servers already exist for Claude integration.

## Integration Options

### 1. Pinterest API v5 (Primary Option)
- **Endpoint:** `https://api.pinterest.com/v5`
- **Cost:** Free
- **Auth:** OAuth 2.0 (Authorization Code Flow)
- **Docs:** https://developers.pinterest.com/docs/api/v5/
- **Key capabilities:**
  - Read all boards and pins (`boards:read`, `pins:read`)
  - Access secret/private boards (`boards:read_secret`, `pins:read_secret`)
  - Pin metadata: title, description, link, image CDN URLs, created date
  - Create/organize boards and pins (`boards:write`, `pins:write`)
  - Public pin search by keyword
  - Product catalog data for linked products

### 2. Pinterest MCP Servers (Claude Integration)
- **Terryso/mcp-pinterest** — Open source, image search + pin detail retrieval + download via MCP
  - Listed at: https://mcp.so/server/mcp-pinterest/terryso
- **CData Pinterest MCP Server** — Read-only via JDBC drivers (also CRUD version available)
  - https://www.cdata.com/drivers/pinterest/mcp/
- **Adzviser** — No-code connector for Pinterest Organic data to Claude
- **InsightfulPipe** — Pinterest Ads account to Claude for performance queries

### 3. Python SDK
- **Official:** `pinterest/pinterest-python-sdk` on GitHub (`pinterest-api-sdk` on PyPI)
- **Generated client:** `pinterest/pinterest-python-generated-api-client` (full v5 coverage)
- **Quickstart:** `pinterest/api-quickstart` repo (Python, Node.js, PHP, bash examples)

### 4. Automation Platforms
- **n8n:** Full native Pinterest integration node + AI workflow templates
- **Zapier:** Basic pin creation and board management
- **Make (Integromat):** Pinterest module available
- **Airbyte:** Native Pinterest connector for ETL pipelines

## Revised Assessment (2026-03-14)

### Terryso/mcp-pinterest — Not Suitable
The Terryso MCP server does NOT use the official Pinterest API. It's a **Puppeteer-based scraper** that drives headless Chrome against pinterest.com. This means:
- Cannot access your personal boards or pins (search-only)
- Fragile — breaks if Pinterest changes DOM structure
- ToS grey area (scraping)
- Only 3 tools: `pinterest_search`, `get_image_info`, `search_and_download`

For home project use (reading your own inspiration boards), this is the wrong tool.

### Revised Approach: Official API v5 + Custom Tooling
Instead of the scraper-based MCP server, the approach is:
1. **Register a Pinterest Developer app** (free, Trial tier)
2. **OAuth 2.0** for authentication (30-day access token, 1-year refresh token)
3. **Test with a Python script** (`scripts/pinterest/pinterest_test.py`) wrapping the v5 REST API
4. **Evaluate** whether an MCP server wrapper is worth building based on test results

### Pinterest Developer Setup Summary
1. Go to `developers.pinterest.com/apps/` → sign in
2. Click Connect app → fill in name/description
3. Copy App ID and App Secret
4. Set redirect URI to `http://localhost:8085/`
5. Run the test script's `auth` command to complete OAuth flow
6. Scopes needed: `pins:read,boards:read,boards:read_secret,user_accounts:read`

## OAuth Strategy: Option B (2026-03-14)

### Decision: Keep Both Accounts, OAuth Personal Through Business App

The Pinterest developer app was registered under a **new business account** (0 pins/boards). The personal account has all the home project inspiration boards.

**Approach:** Use the business account's app credentials to OAuth-authorize the **personal account**. The resulting access token will be scoped to the personal account's boards and pins.

**Why this works:** OAuth 2.0 tokens represent the *authorizing user*, not the app owner. Any Pinterest user can authorize the app — we just log in as the personal account during the OAuth browser flow.

### Current Status: Waiting for Trial Access Approval

- App ID: 1553072
- App Secret: Unavailable (pending trial approval)
- Trial access submitted: 2026-03-14
- Expected approval: 1-2 business days (by ~2026-03-16)
- API test result: HTTP 401, code 3 — "consumer type not supported" (expected while pending)

### Steps Once Approved (Walk-Through)

**Step 1 — Get the App Secret**
- Log into the Pinterest Developer Portal with the business account
- Go to My Apps → select the app → copy the App Secret
- Update `~/.env` with the real `PINTEREST_APP_SECRET`

**Step 2 — Run the OAuth Flow**
- IMPORTANT: In your browser, log OUT of the business Pinterest account
- Log IN to your **personal** Pinterest account (the one with all your boards)
- Then run: `cd /Users/LPS/META_Projects/META/PROJECTS/hOme/scripts/pinterest && python pinterest_test.py auth`
- The script will open a browser window asking you to authorize the app
- Click "Allow" — you should be logged in as your personal account
- The script will capture the token and save it to `.env`

**Step 3 — Test**
- Run: `python pinterest_test.py boards`
- You should see all your personal boards listed
- Try: `python pinterest_test.py pins <BOARD_ID>` with one of your home project boards
- Try: `python pinterest_test.py export <BOARD_ID>` to generate a markdown doc

## Authentication Details

### OAuth 2.0 Flow
1. Register app at Pinterest Developer portal → get App ID + Secret
2. Redirect user to Pinterest authorization URL
3. Receive authorization code → exchange for access token
4. Use bearer token in API requests

### Scopes (Relevant for Home Projects)
```text
boards:read            — Read your boards
boards:read_secret     — Read secret/private boards
pins:read              — Read pins
pins:read_secret       — Read secret pins
pins:write             — Create, update, delete pins
boards:write           — Create, update, delete boards
user_accounts:read     — Read user profile
```

### Access Tiers

| Tier | Access | Limits | Notes |
|------|--------|--------|-------|
| Trial | Automatic on app creation | Daily rate limits (low) | Pins only visible to authenticated user |
| Standard | Manual review required | Per-minute limits (higher) | Pins publicly visible |

- Trial is sufficient for personal read-only use
- Hard limit: 100 calls/second per user per app
- Standard tier approval can be slow/difficult for personal apps

## Home Project Use Cases

- **Mood board extraction:** Retrieve all pins from a board with metadata and image URLs → build a local index of inspiration
- **Materials discovery:** Pin metadata often links to retailers/product pages → extract product sources
- **Design brief generation:** Pull board contents → generate structured design briefs
- **Cross-board organization:** Programmatically organize pins across project boards
- **Keyword search:** Find DIY, interior design, and materials inspiration via public search

## Terms of Service — Key Points

### Permitted
- Reading own pins/boards via authenticated API calls
- Displaying pin images inline (rendering from CDN URL)
- Using pin metadata (title, description, URL, image URL) within your app
- Creating/organizing pins and boards for OAuth-authorized users

### Prohibited
- Scraping without authorization
- Bulk image downloading for offline storage
- Data extraction as primary use case
- Using undocumented methods to access Pinterest

### Practical Guidance
Reading board/pin metadata and image URLs via the official API is within ToS. Rendering images from CDN URLs (not downloading) is fine. Building a local offline image archive crosses the line.

## Next Steps

- [x] ~~Evaluate Terryso/mcp-pinterest~~ — Not suitable (Puppeteer scraper, not API)
- [x] Register Pinterest Developer app — Done (App ID: 1553072, trial pending)
- [x] Create public GitHub repo with privacy policy — Done (github.com/Lalita061985/hOme)
- [ ] **WAITING:** Trial access approval (submitted 2026-03-14, expect ~2026-03-16)
- [ ] Get App Secret from developer portal once approved
- [ ] Run `pinterest_test.py auth` — log in as PERSONAL account during OAuth
- [ ] Test reading personal boards with `pinterest_test.py boards`
- [ ] Export a home project board to structured markdown
- [ ] Evaluate whether a custom MCP server wrapper is worth building
