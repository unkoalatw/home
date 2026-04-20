## 2026-04-20 - Use semantic HTML for interactive elements
**Learning:** Replacing custom interactive `<div>` elements (like .dock-item) with semantic `<button>` tags significantly improves accessibility by automatically providing keyboard navigation and focus management. Tailwind CSS resets default button styles, which prevents visual regressions during the structural conversion.
**Action:** When implementing interactive UI components, default to `<button>` rather than `<div>` with an `onclick` handler to natively ensure keyboard accessibility.
