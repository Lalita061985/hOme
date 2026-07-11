#!/usr/bin/env python3
"""Interactive SketchUp screenshot tool.

Opens the shared SketchUp model in a visible browser,
waits for user confirmation that the 3D model has loaded,
then takes screenshots from multiple angles.
"""

from playwright.sync_api import sync_playwright
from pathlib import Path
import time

SKETCHUP_URL = (
    "https://app.sketchup.com/share/tc/northAmerica/NT97e3oIwpA"
    "?source=web&stoken=iKNuQ6J57_r7GpwdPf5-JeEGsnrxiNLVVuLasL6l-kwS0uBI3iAe6RkPS7R77pcC"
)
OUTPUT_DIR = Path(__file__).parent.parent / "Kitchen Reno"


def take_screenshots():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        print("Opening SketchUp viewer...")
        page.goto(SKETCHUP_URL, wait_until="domcontentloaded", timeout=60000)

        print("\n" + "=" * 50)
        print("BROWSER IS OPEN")
        print("Wait for the 3D kitchen model to fully render.")
        print("=" * 50)
        input("\nPress ENTER when the model is fully loaded... ")

        # Screenshot 1: Default view
        path1 = OUTPUT_DIR / "sketchup_default_view.png"
        page.screenshot(path=str(path1))
        print(f"Saved: {path1}")

        # Orbit right
        input("\nRotate the model to a different angle in the browser, then press ENTER... ")
        path2 = OUTPUT_DIR / "sketchup_view_2.png"
        page.screenshot(path=str(path2))
        print(f"Saved: {path2}")

        # Another angle
        input("\nRotate to another angle, then press ENTER... ")
        path3 = OUTPUT_DIR / "sketchup_view_3.png"
        page.screenshot(path=str(path3))
        print(f"Saved: {path3}")

        # Optional: more shots
        while True:
            more = input("\nTake another screenshot? (y/n): ").strip().lower()
            if more != "y":
                break
            count = len(list(OUTPUT_DIR.glob("sketchup_view_*.png"))) + 1
            path = OUTPUT_DIR / f"sketchup_view_{count}.png"
            page.screenshot(path=str(path))
            print(f"Saved: {path}")

        browser.close()
        print(f"\nDone! All screenshots saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    take_screenshots()
