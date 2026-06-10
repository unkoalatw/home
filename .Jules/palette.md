## 2024-06-10 - Replace `<div>` with `<button>` for Floating Dock Items
**Learning:** Icon-only interactive elements in a floating dock built with `<div>` tags and `onclick` lack inherent accessibility. Screen readers don't know they are actionable, and keyboard navigation ignores them.
**Action:** Always use semantic `<button>` tags for such elements, add descriptive `aria-label` attributes to the button itself, and apply `aria-hidden="true"` to the inner `<i>` icon to hide the raw icon from screen readers while exposing the button correctly.
