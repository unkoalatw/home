## 2024-06-15 - Semantic Keyboard Accessible Icon Buttons
**Learning:** In custom interactive toolbars, using `<div>` with `onclick` handlers bypasses native keyboard focus and interaction, leaving screen readers without context. Furthermore, screen readers can misinterpret raw font data from icon libraries if not explicitly hidden.
**Action:** Replaced interactive `<div>` components like `.dock-item` with semantic `<button>` tags including descriptive `aria-label` attributes, and added `aria-hidden="true"` to inner icon tags.
