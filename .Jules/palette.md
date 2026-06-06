## 2026-06-06 - Accessible Icon Buttons
**Learning:** Generic 'div' tags used for interactive icon-only components (like dock items) fail to provide proper semantic structure or context for screen readers. Tailwind's preflight resets button styles, allowing safe structural conversion.
**Action:** Convert interactive 'div' elements to semantic '<button>' elements, assign descriptive 'aria-label' attributes, and add 'aria-hidden="true"' to inner decorative/font icons as a reusable pattern.
