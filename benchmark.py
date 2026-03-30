from playwright.sync_api import sync_playwright
import time
import os

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file://{os.path.abspath('index.html')}")

    # Wait for the page to load
    page.wait_for_timeout(1000)

    # We want to measure the time it takes to process scroll events.
    # We will dispatch 5000 scroll events and measure the time it takes in the browser context.

    js_code = """
    () => {
        return new Promise((resolve) => {
            const start = performance.now();
            let count = 0;

            function doScrolls() {
                for (let i = 0; i < 500; i++) {
                    window.dispatchEvent(new Event('scroll'));
                    count++;
                }
                if (count >= 10000) {
                    requestAnimationFrame(() => {
                        const end = performance.now();
                        resolve(end - start);
                    });
                } else {
                    requestAnimationFrame(doScrolls);
                }
            }

            doScrolls();
        });
    }
    """

    time_taken = page.evaluate(js_code)
    print(f"Time taken in browser: {time_taken:.2f}ms")

    browser.close()
