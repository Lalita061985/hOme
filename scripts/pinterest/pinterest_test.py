#!/usr/bin/env python3
"""
Pinterest API v5 — exploration / test script.
No SDK — raw requests only.

Usage:
    python pinterest_test.py auth               # OAuth flow → saves tokens to .env
    python pinterest_test.py boards             # List all boards
    python pinterest_test.py pins BOARD_ID      # List pins on a board
    python pinterest_test.py pin PIN_ID         # Get a single pin's details
    python pinterest_test.py export BOARD_ID    # Export board pins to research/ as markdown
"""

import argparse
import base64
import json
import os
import re
import secrets
import sys
import urllib.parse
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from threading import Thread
from typing import Any, Optional

import requests
from dotenv import dotenv_values, set_key

# ── Config ────────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent
ENV_FILE = SCRIPT_DIR / ".env"
GLOBAL_ENV_FILE = Path.home() / ".env"
RESEARCH_DIR = SCRIPT_DIR / "../../research/pinterest"

BASE_URL = "https://api.pinterest.com/v5"
TOKEN_URL = "https://api.pinterest.com/v5/oauth/token"
REDIRECT_URI = "http://localhost:8085/callback"
SCOPES = "boards:read,pins:read"


# ── Credentials ───────────────────────────────────────────────────────────────

def load_env() -> dict[str, str]:
    """Load env vars: global ~/.env as base layer, local scripts/pinterest/.env as override.
    At least one must exist; local .env takes precedence on key conflicts."""
    global_exists = GLOBAL_ENV_FILE.exists()
    local_exists = ENV_FILE.exists()

    if not global_exists and not local_exists:
        print(f"No .env file found at {ENV_FILE} or {GLOBAL_ENV_FILE}")
        print("Run: cp .env.example .env  — then fill in APP_ID and APP_SECRET")
        sys.exit(1)

    # Load global first (base layer), then local (overrides)
    env: dict[str, str] = {}
    if global_exists:
        env.update(dotenv_values(GLOBAL_ENV_FILE))
    if local_exists:
        env.update(dotenv_values(ENV_FILE))
    return env


def save_token(key: str, value: str) -> None:
    """Always save tokens to the local .env (creating it if needed)."""
    ENV_FILE.touch(exist_ok=True)
    set_key(str(ENV_FILE), key, value)


def get_credentials() -> dict[str, str]:
    env = load_env()
    app_id = env.get("PINTEREST_APP_ID", "").strip()
    app_secret = env.get("PINTEREST_APP_SECRET", "").strip()
    if not app_id or not app_secret:
        print("PINTEREST_APP_ID and PINTEREST_APP_SECRET must be set in .env")
        sys.exit(1)
    return env


# ── HTTP helpers ──────────────────────────────────────────────────────────────

def auth_header(access_token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {access_token}"}


def api_get(path: str, access_token: str, params: Optional[dict] = None) -> dict[str, Any]:
    """GET from Pinterest API. Returns parsed JSON. Raises on HTTP errors."""
    url = f"{BASE_URL}{path}"
    resp = requests.get(url, headers=auth_header(access_token), params=params or {})
    if resp.status_code == 401:
        raise TokenExpiredError()
    resp.raise_for_status()
    return resp.json()


def paginate(path: str, access_token: str, result_key: str = "items", extra_params: Optional[dict] = None) -> list[dict]:
    """Collect all pages from a paginated endpoint."""
    results = []
    params = dict(extra_params or {})
    params["page_size"] = 100

    while True:
        data = api_get(path, access_token, params)
        results.extend(data.get(result_key, []))
        bookmark = data.get("bookmark")
        if not bookmark:
            break
        params["bookmark"] = bookmark

    return results


class TokenExpiredError(Exception):
    pass


# ── Token refresh ─────────────────────────────────────────────────────────────

def refresh_access_token(env: dict[str, str]) -> str:
    """Use refresh_token to get a new access_token. Saves to .env. Returns new token."""
    refresh_token = env.get("PINTEREST_REFRESH_TOKEN", "").strip()
    if not refresh_token:
        print("No refresh token available. Run: python pinterest_test.py auth")
        sys.exit(1)

    app_id = env["PINTEREST_APP_ID"].strip()
    app_secret = env["PINTEREST_APP_SECRET"].strip()
    credentials = base64.b64encode(f"{app_id}:{app_secret}".encode()).decode()

    resp = requests.post(
        TOKEN_URL,
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
        },
    )

    if resp.status_code != 200:
        print(f"Token refresh failed ({resp.status_code}): {resp.text}")
        print("Your refresh token may be expired. Run: python pinterest_test.py auth")
        sys.exit(1)

    tokens = resp.json()
    new_access_token = tokens["access_token"]
    save_token("PINTEREST_ACCESS_TOKEN", new_access_token)
    if "refresh_token" in tokens:
        save_token("PINTEREST_REFRESH_TOKEN", tokens["refresh_token"])

    print("Access token refreshed and saved to .env")
    return new_access_token


def get_valid_token(env: dict[str, str]) -> str:
    """Return access token, refreshing if expired."""
    access_token = env.get("PINTEREST_ACCESS_TOKEN", "").strip()
    if not access_token:
        print("No access token. Run: python pinterest_test.py auth")
        sys.exit(1)
    return access_token


def call_with_refresh(fn, env: dict[str, str], *args, **kwargs):
    """Call fn(*args). On 401, refresh token and retry once."""
    try:
        return fn(*args, **kwargs)
    except TokenExpiredError:
        print("Access token expired — refreshing...")
        new_token = refresh_access_token(env)
        # Update token in args if it's positional (access_token is always last positional)
        args = args[:-1] + (new_token,) if args else args
        # Re-patch kwargs if token passed that way
        if "access_token" in kwargs:
            kwargs["access_token"] = new_token
        return fn(*args, **kwargs)


# ── OAuth flow ────────────────────────────────────────────────────────────────

def cmd_auth(env: dict[str, str]) -> None:
    """Full OAuth 2.0 flow: open browser URL, catch callback, exchange code for tokens."""
    app_id = env["PINTEREST_APP_ID"].strip()
    app_secret = env["PINTEREST_APP_SECRET"].strip()

    state = secrets.token_urlsafe(16)
    auth_url = (
        "https://www.pinterest.com/oauth/"
        f"?client_id={app_id}"
        f"&redirect_uri={urllib.parse.quote(REDIRECT_URI)}"
        f"&response_type=code"
        f"&scope={SCOPES}"
        f"&state={state}"
    )

    print("\n── Pinterest OAuth ──────────────────────────────────────")
    print("Open this URL in your browser:\n")
    print(f"  {auth_url}\n")
    print("After authorizing, you'll be redirected to localhost:8085.")
    print("Waiting for callback...\n")

    # Temporary HTTP server to catch the redirect
    auth_code: list[str] = []  # mutable container for thread closure

    class CallbackHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = urllib.parse.urlparse(self.path)
            params = dict(urllib.parse.parse_qsl(parsed.query))

            if params.get("state") != state:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"State mismatch. Try again.")
                return

            code = params.get("code")
            if not code:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"No auth code in callback.")
                return

            auth_code.append(code)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Authorization successful. You can close this tab.")

        def log_message(self, format, *args):
            pass  # suppress request logs

    server = HTTPServer(("localhost", 8085), CallbackHandler)

    def serve():
        server.handle_request()  # handle exactly one request

    t = Thread(target=serve, daemon=True)
    t.start()
    t.join(timeout=120)

    if not auth_code:
        print("Timed out waiting for OAuth callback (120s).")
        sys.exit(1)

    code = auth_code[0]

    # Exchange auth code for tokens
    credentials = base64.b64encode(f"{app_id}:{app_secret}".encode()).decode()
    resp = requests.post(
        TOKEN_URL,
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
        },
    )

    if resp.status_code != 200:
        print(f"Token exchange failed ({resp.status_code}):")
        print(resp.text)
        sys.exit(1)

    tokens = resp.json()
    save_token("PINTEREST_ACCESS_TOKEN", tokens["access_token"])
    save_token("PINTEREST_REFRESH_TOKEN", tokens.get("refresh_token", ""))

    print("Tokens saved to .env")
    print(f"  Access token: {tokens['access_token'][:20]}...")
    if tokens.get("refresh_token"):
        print(f"  Refresh token: {tokens['refresh_token'][:20]}...")
    print("\nRun `python pinterest_test.py boards` to verify access.")


# ── Board commands ────────────────────────────────────────────────────────────

def cmd_boards(env: dict[str, str]) -> None:
    access_token = get_valid_token(env)

    print("Fetching boards...")
    boards = call_with_refresh(paginate, env, "/boards", access_token, "items")

    if not boards:
        print("No boards found.")
        return

    print(f"\n{'ID':<20} {'Pins':>5}  {'Privacy':<10}  Name")
    print("─" * 80)
    for b in boards:
        board_id = b.get("id", "")
        name = b.get("name", "")
        pin_count = b.get("pin_count", "?")
        privacy = b.get("privacy", "?")
        print(f"{board_id:<20} {pin_count:>5}  {privacy:<10}  {name}")

    print(f"\n{len(boards)} board(s) total.")


def cmd_pins(env: dict[str, str], board_id: str) -> None:
    access_token = get_valid_token(env)

    print(f"Fetching pins for board {board_id}...")
    pins = call_with_refresh(paginate, env, f"/boards/{board_id}/pins", access_token, "items")

    if not pins:
        print("No pins found (or board doesn't exist).")
        return

    print(f"\n{'PIN ID':<20}  {'Title':<35}  Link")
    print("─" * 100)
    for p in pins:
        pin_id = p.get("id", "")
        title = (p.get("title") or "")[:33]
        link = p.get("link") or ""
        print(f"{pin_id:<20}  {title:<35}  {link}")

    print(f"\n{len(pins)} pin(s) total.")


def cmd_pin(env: dict[str, str], pin_id: str) -> None:
    access_token = get_valid_token(env)

    print(f"Fetching pin {pin_id}...")
    try:
        pin = call_with_refresh(api_get, env, f"/pins/{pin_id}", access_token)
    except requests.HTTPError as e:
        print(f"Error fetching pin: {e}")
        sys.exit(1)

    # Pretty-print the key fields
    print(f"\n── Pin {pin.get('id')} ──────────────────────────────────")
    print(f"  Title       : {pin.get('title') or '(none)'}")
    print(f"  Description : {pin.get('description') or '(none)'}")
    print(f"  Link        : {pin.get('link') or '(none)'}")
    print(f"  Board ID    : {pin.get('board_id') or '(none)'}")
    print(f"  Created     : {pin.get('created_at') or '(none)'}")

    media = pin.get("media", {})
    images = media.get("images", {})
    if images:
        # Prefer 'original' or largest available
        key = "original" if "original" in images else sorted(images.keys())[-1]
        img = images[key]
        print(f"  Image URL   : {img.get('url', '(none)')}")
        print(f"  Dimensions  : {img.get('width')}×{img.get('height')}")
    else:
        alt_url = pin.get("media", {}).get("cover_image_url", "")
        if alt_url:
            print(f"  Image URL   : {alt_url}")

    print()


# ── Export command ────────────────────────────────────────────────────────────

def _image_url(pin: dict) -> str:
    """Extract best-quality image URL from a pin object."""
    images = pin.get("media", {}).get("images", {})
    if images:
        key = "original" if "original" in images else sorted(images.keys())[-1]
        return images[key].get("url", "")
    return pin.get("media", {}).get("cover_image_url", "")


def cmd_export(env: dict[str, str], board_id: str) -> None:
    access_token = get_valid_token(env)

    # Fetch board metadata
    print(f"Fetching board {board_id}...")
    try:
        board = call_with_refresh(api_get, env, f"/boards/{board_id}", access_token)
    except requests.HTTPError as e:
        print(f"Error fetching board: {e}")
        sys.exit(1)

    board_name = board.get("name", board_id)
    board_url = board.get("url", "")
    pin_count = board.get("pin_count", "?")

    print(f"Board: {board_name} ({pin_count} pins)")
    print("Fetching pins...")
    pins = call_with_refresh(paginate, env, f"/boards/{board_id}/pins", access_token, "items")

    if not pins:
        print("No pins found.")
        return

    # Build markdown
    today = datetime.now().strftime("%Y-%m-%d")
    safe_name = re.sub(r"[^\w\s-]", "", board_name).strip().replace(" ", "_")
    filename = f"{safe_name}_{board_id}_{today}.md"

    export_dir = (SCRIPT_DIR / "../../research/pinterest").resolve()
    export_dir.mkdir(parents=True, exist_ok=True)
    output_path = export_dir / filename

    lines = [
        f"# Pinterest Board: {board_name}",
        f"",
        f"- **Board ID:** {board_id}",
        f"- **URL:** {board_url}",
        f"- **Exported:** {today}",
        f"- **Total pins:** {len(pins)}",
        f"",
        "---",
        "",
    ]

    for i, pin in enumerate(pins, 1):
        title = pin.get("title") or "(no title)"
        description = (pin.get("description") or "").strip()
        link = pin.get("link") or ""
        image_url = _image_url(pin)
        pin_id = pin.get("id", "")

        lines.append(f"## {i}. {title}")
        lines.append("")
        if description:
            lines.append(description)
            lines.append("")
        if link:
            lines.append(f"**Source:** {link}")
            lines.append("")
        if image_url:
            lines.append(f"![{title}]({image_url})")
            lines.append("")
        lines.append(f"*Pin ID: {pin_id}*")
        lines.append("")
        lines.append("---")
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nExported {len(pins)} pins to:")
    print(f"  {output_path}")


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pinterest API v5 test script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("auth", help="Run OAuth flow to get tokens")
    subparsers.add_parser("boards", help="List all boards")

    p_pins = subparsers.add_parser("pins", help="List pins on a board")
    p_pins.add_argument("board_id", help="Board ID")

    p_pin = subparsers.add_parser("pin", help="Get details for a single pin")
    p_pin.add_argument("pin_id", help="Pin ID")

    p_export = subparsers.add_parser("export", help="Export board pins to markdown")
    p_export.add_argument("board_id", help="Board ID")

    args = parser.parse_args()
    env = get_credentials()

    try:
        if args.command == "auth":
            cmd_auth(env)
        elif args.command == "boards":
            cmd_boards(env)
        elif args.command == "pins":
            cmd_pins(env, args.board_id)
        elif args.command == "pin":
            cmd_pin(env, args.pin_id)
        elif args.command == "export":
            cmd_export(env, args.board_id)
    except KeyboardInterrupt:
        print("\nAborted.")
        sys.exit(0)
    except requests.HTTPError as e:
        print(f"API error: {e}")
        if hasattr(e, "response") and e.response is not None:
            print(e.response.text)
        sys.exit(1)


if __name__ == "__main__":
    main()
