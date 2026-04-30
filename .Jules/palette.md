## 2024-04-30 - Semantic Structural Conversion to Buttons
**Learning:** Tailwind's preflight base CSS in this project resets default `<button>` styles, allowing safe structural conversions of interactive `<div>` elements (like `.dock-item`) to semantic `<button>` tags without causing visual regressions.
**Action:** When implementing interactive UI elements, structurally convert `<div onclick="...">` to semantic `<button>` tags to automatically gain keyboard navigation and focus management. Always include `aria-label` and `aria-hidden="true"` on inner icons.
