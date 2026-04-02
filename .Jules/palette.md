## 2026-04-02 - Icon-Only Button Accessibility
**Learning:** Using semantic `<button>` elements for icon-only actions (like the dock and card close buttons) ensures better native keyboard focus visibility and structural accessibility over using generic `<div>` tags with `onclick` handlers, but they must be given descriptive `aria-label` attributes to be decipherable by screen readers since they lack text content.
**Action:** Always prefer native semantic `<button>` tags with `aria-label`s for interactive icon-only elements rather than relying on `<div>` structures and custom click handlers.
