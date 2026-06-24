from playwright.sync_api import sync_playwright
import os
import time

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file://{os.path.abspath('index.html')}")

    # Wait for the page to load
    page.wait_for_timeout(1000)

    # Get the initial progress bar width
    initial_width = page.evaluate("document.getElementById('scroll-progress').style.width")
    print(f"Initial progress bar width: '{initial_width}'")

    # Scroll down by 500 pixels
    page.evaluate("window.scrollBy(0, 500)")

    # Wait for the requestAnimationFrame to trigger
    page.wait_for_timeout(100)

    # Get the new progress bar width
    new_width = page.evaluate("document.getElementById('scroll-progress').style.width")
    print(f"New progress bar width: '{new_width}'")

    if new_width != initial_width and new_width != "0%":
        print("Success: Progress bar width updated correctly.")
    else:
        print("Error: Progress bar width did not update.")

    browser.close()
