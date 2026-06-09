## 2024-05-18 - Semantic HTML for Interactive Dock Elements
**Learning:** The floating dock utilized `<div>` tags with `onclick` handlers and raw FontAwesome icons, rendering it invisible to screen readers and difficult to navigate via keyboard.
**Action:** Always use semantic `<button>` tags for interactive, icon-only UI elements like the dock, along with descriptive `aria-label`s on the button and `aria-hidden="true"` on the internal icon elements to ensure robust accessibility.
