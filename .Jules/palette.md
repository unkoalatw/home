## 2024-06-03 - Structural Conversion with Tailwind Preflight
**Learning:** Tailwind's preflight base CSS resets default `<button>` styles, allowing safe structural conversions of interactive `<div>` elements (like `.dock-item`) to semantic `<button>` tags without causing visual regressions.
**Action:** Convert `<div>` elements with `onclick` handlers to semantic `<button>` tags to automatically ensure proper keyboard navigation and focus management.
