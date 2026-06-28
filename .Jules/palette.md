## 2024-05-24 - Accessibility for Icon-only Dock Items
**Learning:** Using `<div>` tags for icon-only buttons with `onclick` handlers creates accessibility barriers because they lack semantic meaning and focus management, and screen readers may read the raw font data for the icons.
**Action:** Always convert interactive icon-only elements to semantic `<button>` tags, provide descriptive `aria-label` attributes to convey their purpose, and add `aria-hidden="true"` to the internal `<i>` elements.

## 2024-06-28 - ARIA Labels on Content-Rich Buttons
**Learning:** Adding a static `aria-label` attribute to a complex interactive element (like a project card or context menu) that has been converted to a `<button>` completely overrides and masks the inner text content from screen readers, causing a major accessibility regression.
**Action:** When converting content-rich `<div>` elements into semantic `<button>` tags, avoid applying a generic `aria-label`. Instead, rely on the element's natural inner text content or semantic sub-elements to provide context to screen readers.
