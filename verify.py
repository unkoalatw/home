import sys
from playwright.sync_api import sync_playwright

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Monitor console errors
        errors = []
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)

        # Navigate to local server
        page.goto("http://localhost:8080")

        # Wait for social links to be populated
        page.wait_for_selector("#social-links a", timeout=10000)

        # Fetch the rendered social links
        social_links = page.locator("#social-links a").all()

        assert len(social_links) > 0, "No social links were rendered."

        for link in social_links:
            href = link.get_attribute("href")
            assert href is not None and href != "", "Found a social link without an href."
            print(f"Verified link: {href}")

        if len(errors) > 0:
            print("Console errors found:", errors)
            sys.exit(1)

        print("Verification successful!")
        browser.close()

if __name__ == "__main__":
    verify()