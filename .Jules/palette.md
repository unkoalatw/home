## 2024-05-24 - Structural Conversion of Interactive Divs
**Learning:** Tailwind's preflight base CSS resets default `<button>` styles in this project, allowing safe structural conversions of interactive `<div>` elements (like `.dock-item`) to semantic `<button>` tags without causing visual regressions.
**Action:** When implementing interactive UI elements, convert `<div>` tags with `onclick` handlers to semantic `<button>` tags to automatically ensure proper keyboard navigation and focus management.
