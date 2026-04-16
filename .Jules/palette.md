## 2024-05-18 - Icon-Only Button Accessibility
**Learning:** Icon-only interactive elements implemented as `<div>` tags lacking semantic roles and `aria-label`s create a severe accessibility barrier for screen readers, while raw icon elements like FontAwesome `<i>` tags can pollute screen reader output if not explicitly hidden.
**Action:** Always use semantic `<button>` tags for interactive elements, provide descriptive `aria-label`s for icon-only buttons, and apply `aria-hidden="true"` to inner icon elements to ensure clean and meaningful screen reader announcements.
