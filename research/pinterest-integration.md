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

- [x] ~~Evaluate Terryso/mcp-pinterest~~ — Not suitable (scraper, not API)
- [ ] Register Pinterest Developer app and obtain Trial access
- [ ] Run pinterest_test.py auth to complete OAuth flow
- [ ] Test reading personal boards with pinterest_test.py boards
- [ ] Export a home project board to structured markdown
- [ ] Evaluate whether a custom MCP server wrapper is worth building
