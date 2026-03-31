## 2024-05-24 - Semantic Buttons for Interactive Elements
**Learning:** The application extensively uses `<div>` elements for interactive components like the dock icons, which completely breaks keyboard accessibility and tab navigation.
**Action:** Replace interactive `<div>` elements with semantic `<button>` elements, and ensure icon-only buttons have descriptive `aria-label` attributes for screen reader compatibility.
