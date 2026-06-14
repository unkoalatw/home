## 2024-06-14 - Semantic interactive elements
**Learning:** Found multiple instances where non-semantic `<div>` elements are used with `onclick` handlers for critical interactions, like the dock items. This limits keyboard navigation (tabbing, enter/space interaction) and screen reader support natively.
**Action:** Always prefer `<button>` elements over `<div>` for interactive components that trigger scripts to inherit native focus, semantics, and keyboard events, and provide explicit ARIA labels.
