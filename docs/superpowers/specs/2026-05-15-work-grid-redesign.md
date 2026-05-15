# Work Grid Redesign — joshsoliz.com
*2026-05-15*

## Goal

Transform the homepage "Selected Work" section into a bold, image-first grid inspired by jonduncanphoto.com/clients/ — where the work speaks immediately without pitch copy getting in the way first.

## Scope

Changes are limited to `index.html` and `style.css`. All individual project pages remain untouched.

---

## Changes

### 1. Section Reorder

Move the "What I make" services section (`.services`) to *below* the work grid instead of above it.

**Before:** Hero → Services → Work → About → …
**After:** Hero → Work → Services → About → …

Rationale: lead with the work, let it speak, then explain what you offer.

---

### 2. Work Grid — Full-Bleed Layout

Remove the `.container` wrapper from the work section so the grid goes edge-to-edge (matching how `.folios` already works at the bottom of the page). Add `12px` padding and gap to match the folios section.

---

### 3. Work Card — Image-First Treatment

**Card structure changes:**
- Remove the `.work-info` div (title + description below the card) entirely
- Project name moves onto the image as a centered white overlay (bold, uppercase, large — similar to Jon Duncan's treatment)
- Keep the category tag (e.g. "Church", "Nonprofit") as a small pill, bottom-left on the image
- Keep the media-type tag (e.g. "Photography", "Video Production") as a small pill, bottom-right on the image

**Aspect ratio:** Change from `16/9` to `4/3` — taller cards give images more visual weight.

**Video badge:** For video projects, add a subtle `▶` play indicator in the top-right corner of the card (small, semi-transparent pill). Photo projects get nothing extra.

**Hover state:**
- Overlay darkens slightly
- Project name stays visible
- "View project →" CTA appears centered (fades in, same pattern as existing `.service-card-cta`)
- Subtle scale (existing `scale(1.02)` behavior stays)

---

### 4. Expand to 6 Projects

Add two more projects currently missing from the homepage grid:
- **Easter Promo** (`project-easter.html`) — Motion Design
- **Mother Chorizo's** (`project-mother-chorizos.html`) — Video / Social

Grid becomes 2 columns × 3 rows = 6 cards.

Thumbnail images to use:
- Easter Promo: `https://vz-474cf03f-6bc.b-cdn.net/e6e648e4-be25-4048-a14d-0af1a4768d9c/thumbnail.jpg` (Bunny CDN auto-thumbnail)
- Mother Chorizo's: `images/mother-chorizos-before.png` (existing local file)

**Video badge projects** (gets the `▶` indicator):
- First Responder REBOOT — Video Production ✓
- Shinin' Lyric Video — Motion Design ✓
- Easter Promo — Motion Design ✓
- Mother Chorizo's — Video / Social ✓

**Photo-only projects** (no badge):
- Fresh Life Worship — Photography
- Two Kay's Flower Farm — Photography

---

### 5. Section Label Update

Keep the `section-label` ("Selected work") and position it above the full-bleed grid with left-aligned padding to match the rest of the page.

---

## What Does NOT Change

- Individual project pages (`project-*.html`) — untouched
- Hero section
- About section
- Quote builder
- Testimonials
- Contact section
- Folios section
- Footer
- `style.css` color palette, typography, nav

---

## Files Affected

- `index.html` — section reorder, card markup changes, 2 new project cards
- `style.css` — `.work-grid`, `.work-card`, `.work-thumb`, `.work-overlay`, `.work-info` (removed), new `.work-name` overlay styles, video badge styles
