# Brand Guide - tortsuk.com

## Colors

| Role | Variable | Hex | Usage |
|------|----------|-----|-------|
| Background | `--color-bg` | `#F9F9F9` | Page background |
| Text | `--color-text` | `#1A2B3C` | Navy - headings, body text |
| Text light | `--color-text-light` | `#5a6a7a` | Dates, descriptions, secondary text |
| Accent (Mint) | `--color-accent` | `#7FB0A1` | Links, buttons, borders, action box accent |
| Accent hover | `--color-accent-hover` | `#6a9a8b` | Hover states, whisper notes |
| Border | `--color-border` | `#e0e4e8` | Dividers, form borders |
| Surface | `--color-surface` | `#f0f2f4` | Card backgrounds, contact section, boxes |

## Typography

| Role | Font | Weight | Variable |
|------|------|--------|----------|
| Headings | Heebo | 700 (Bold) | `--font-heading` |
| Body | System sans-serif | 400 | `--font-sans` |
| Handwriting / Whisper | Caveat | 400-600 | `--font-handwriting` |

- Line height: 1.7 for body, 1.3 for headings
- Base font size: 18px (16px on mobile)
- Max content width: 640px

Google Fonts import:
```
Heebo:wght@400;700
Caveat:wght@400;600
```

## Components

### Tachles Action Box
Summary box with actionable takeaways. Mint accent border on the right (RTL) or left (LTR).

```html
<div class="tachles">
  <div class="tachles-title">תכל׳ס - מה עושים</div>
  <ul>
    <li>Point one</li>
    <li>Point two</li>
    <li>Point three</li>
  </ul>
</div>
```

### Whisper (Margin Notes)
Handwriting-style aside in Caveat font. For personal asides, soft commentary.

```html
<p class="whisper">הערה אישית בכתב יד...</p>
```

### How-To Box
Technical instructions with steps.

```html
<div class="how-to">
  <div class="how-to-title">How to do it</div>
  <ul>
    <li>Step one</li>
    <li>Step two</li>
  </ul>
</div>
```

### Contact Form
Appears at the bottom of blog posts and key pages.

```html
<section class="contact-section">
  <h2>Section title</h2>
  <p>Description text</p>
  <form class="contact-form" action="https://formspree.io/f/xgonvjop" method="POST">
    <input type="hidden" name="_subject" value="Subject line">
    <div class="form-row">
      <input type="text" name="name" placeholder="..." required>
      <input type="email" name="email" placeholder="..." required>
    </div>
    <textarea name="message" placeholder="..." required></textarea>
    <button type="submit">Button text</button>
  </form>
</section>
```

## Micro-Copy

| Element | Hebrew | English |
|---------|--------|---------|
| Submit button (forms) | בואו נדבר | Let's talk |
| Textarea placeholder (blog) | דברו אליי | — |
| Back to blog link | &rarr; חזרה לבלוג | &larr; Back to blog |
| Blog contact heading | נגע בכם? | — |

## Voice & Tone
- Direct, warm, professional but not corporate
- First person feminine (Hebrew)
- Practical and actionable - not preachy
- Uses real stories and examples from consulting work (anonymized)
- Inspired by sive.rs - quiet, smart, informative, not pushy

## Favicon
SVG sprout/growth icon in `images/favicon.svg`. Dark navy circle (`#2c3e50`) with light stroke (`#e8e0d4`).

## Tech Stack
- Static HTML/CSS (no framework)
- GitHub Pages hosting
- Formspree for contact forms (ID: `xgonvjop`)
- GoatCounter analytics (code: `tortsuk`)
- Bilingual: Hebrew (RTL, default) + English (LTR)
