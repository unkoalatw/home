## 2024-05-24 - Accessibility for Icon-only Dock Items
**Learning:** Using `<div>` tags for icon-only buttons with `onclick` handlers creates accessibility barriers because they lack semantic meaning and focus management, and screen readers may read the raw font data for the icons.
**Action:** Always convert interactive icon-only elements to semantic `<button>` tags, provide descriptive `aria-label` attributes to convey their purpose, and add `aria-hidden="true"` to the internal `<i>` elements.
