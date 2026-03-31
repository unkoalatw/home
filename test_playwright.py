import time
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto('http://localhost:8080')
        page.wait_for_load_state('networkidle')

        # Hide preloader to get clear view
        page.evaluate("document.getElementById('preloader').style.display = 'none';")

        time.sleep(2) # Give animations a little bit of time

        page.screenshot(path='screenshot.png')
        print("Screenshot captured to screenshot.png")

        browser.close()

if __name__ == '__main__':
    main()
