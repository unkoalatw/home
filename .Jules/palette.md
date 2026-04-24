
## 2024-05-24 - Interactive icon elements as buttons
**Learning:** Tailwind's preflight base CSS resets default `<button>` styles, allowing safe structural conversions of interactive `<div>` elements (like `.dock-item`) to semantic `<button>` tags without causing visual regressions. Using `button` automatically ensures proper keyboard navigation and focus management.
**Action:** When implementing interactive UI elements (such as icon-only buttons), use semantic `<button>` tags rather than `<div>` tags with `onclick` handlers. Always include descriptive `aria-label` attributes and hide internal FontAwesome icons with `aria-hidden="true"` to provide proper context for screen readers.
