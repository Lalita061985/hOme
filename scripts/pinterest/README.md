# Pinterest API v5 — Test Script

Quick exploration tool for Pinterest API v5. OAuth 2.0, board/pin listing, markdown export.

---

## 1. Create a Pinterest Developer App

1. Go to [developers.pinterest.com](https://developers.pinterest.com)
2. Sign in with your Pinterest account
3. Click **My apps** → **Connect app**
4. Fill in app details (name, description — anything works for testing)
5. Under **Redirect URIs**, add: `http://localhost:8085/callback`
6. Note your **App ID** and **App Secret** from the app settings page

---

## 2. Configure Credentials

```bash
cp .env.example .env
```

Edit `.env` and fill in:
- `PINTEREST_APP_ID` — from your app's settings page
- `PINTEREST_APP_SECRET` — from your app's settings page

Leave `PINTEREST_ACCESS_TOKEN` and `PINTEREST_REFRESH_TOKEN` blank — the auth command fills these in.

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or with uv:

```bash
uv pip install -r requirements.txt
```

---

## 4. Run OAuth Flow

```bash
python pinterest_test.py auth
```

This will:
1. Print an authorization URL — open it in your browser
2. Authorize the app in Pinterest
3. Pinterest redirects to `localhost:8085/callback` — the script catches this automatically
4. Tokens are saved back to `.env`

---

## 5. Commands

```bash
# List all boards
python pinterest_test.py boards

# List pins on a board (get board ID from the boards command)
python pinterest_test.py pins BOARD_ID

# Get details for a specific pin
python pinterest_test.py pin PIN_ID

# Export a board's pins to research/ as markdown
python pinterest_test.py export BOARD_ID
```

---

## Notes

- Tokens expire after 30 days (access token) / 1 year (refresh token). The script auto-refreshes on 401.
- The `export` command writes to `../../research/pinterest/` relative to the script.
- Board IDs look like `123456789` — grab them from the `boards` output.
- Pin IDs look like `123456789012345678`.
