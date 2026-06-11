## 2026-06-11 - Converting Divs to Buttons in Tailwind Projects
**Learning:** Tailwind CSS resets all default button styling (borders, background, padding). Therefore, interactive elements using <div> with onclick handlers can be structurally updated to native <button> elements for instant keyboard accessibility (Tab, Enter/Space activation) without causing visual regressions.
**Action:** Use native <button> elements instead of <div> for interactive components like docks and sidebars, especially in projects utilizing Tailwind Preflight.
