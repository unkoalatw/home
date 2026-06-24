const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto(`file://${path.resolve('index.html')}`);

  // Wait for the page to load
  await page.waitForTimeout(1000);

  const start = Date.now();
  // Simulate 1000 scroll events
  await page.evaluate(() => {
    return new Promise((resolve) => {
      let count = 0;
      const interval = setInterval(() => {
        window.dispatchEvent(new Event('scroll'));
        count++;
        if (count >= 5000) {
          clearInterval(interval);
          // Wait a bit for any pending frames
          requestAnimationFrame(() => resolve());
        }
      }, 0);
    });
  });

  const end = Date.now();
  console.log(`Time taken: ${end - start}ms`);

  await browser.close();
})();
