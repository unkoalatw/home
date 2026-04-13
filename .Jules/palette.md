## 2024-06-25 - Semantic Interactive Elements
**Learning:** Found a pattern where interactive UI elements (like floating dock items and dynamically generated close buttons) were implemented using `<div>` tags with `onclick` handlers. This approach breaks native keyboard navigation (tab order) and removes implicit context for screen readers.
**Action:** Replaced interactive `<div>`s with semantic `<button>` tags and added descriptive `aria-label` attributes. This ensures keyboard accessibility and screen reader support without relying on custom JavaScript for focus management.
