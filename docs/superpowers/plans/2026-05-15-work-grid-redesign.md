# Work Grid Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the homepage "Selected Work" section into a full-bleed, image-first 6-card grid with project names on the image, a video badge for video/motion projects, and services section moved below the work.

**Architecture:** All changes in `index.html` (markup) and `style.css` (CSS). No new files. No JS changes. Individual project pages untouched.

**Tech Stack:** Vanilla HTML/CSS. Deployed via Cloudflare Workers (`wrangler`). Git remote: `git@github.com:joshsoliz/newSite.git`

---

### Task 1: Reorder sections — move Services below Work

**Files:**
- Modify: `index.html` — cut `.services` section, paste it after `.work` section

- [ ] **Step 1: Move the services section**

In `index.html`, cut the entire `<section class="services" id="services">…</section>` block (currently between the hero and the work section) and paste it immediately after the closing `</section>` of the `<section class="work" id="work">` block.

Result order: Hero → Work → Services → About → Quote Builder → Testimonials → Contact → Folios → Footer

- [ ] **Step 2: Verify in browser**

Open `index.html` locally in a browser. Scroll past hero — work grid should appear first, then the 01/02/03 service cards below it.

- [ ] **Step 3: Commit**

```bash
cd /Users/joshua_soliz/Documents/newSite
git add index.html
git commit -m "reorder: move services section below work grid"
```

---

### Task 2: Upgrade work card markup — full-bleed, name-on-image, 6 cards

**Files:**
- Modify: `index.html` — `.work` section container, all `.work-card` elements

- [ ] **Step 1: Remove the `.container` wrapper from the work section**

Change:
```html
<section class="work" id="work">
  <div class="container">
    <p class="section-label">Selected work</p>
    <div class="work-grid">
```

To:
```html
<section class="work" id="work">
  <div class="work-section-header container">
    <p class="section-label">Selected work</p>
  </div>
  <div class="work-grid">
```

And remove the closing `</div>` that was closing the `.container` (keep the one closing `.work-grid` and then `</section>`).

- [ ] **Step 2: Replace all 4 work cards with the new markup pattern**

Each card drops the `.work-info` div and gains a `.work-name` overlay. Use this exact pattern for each card:

**Fresh Life Worship (Photography — no video badge):**
```html
<a href="project-fresh-life.html" class="work-card">
  <div class="work-thumb">
    <img src="https://images.squarespace-cdn.com/content/v1/687be35b43e91200aeaa965b/426c125c-3ad9-4e5b-a45a-5a6e41750dde/_1130393-min.jpg" alt="Fresh Life Worship church event photography" style="width:100%;height:100%;object-fit:cover;" />
    <div class="work-overlay">
      <span class="work-tag">Church</span>
      <span class="work-tag work-tag-cat">Photography</span>
    </div>
    <div class="work-name-overlay">
      <span class="work-name">Fresh Life Worship</span>
      <span class="work-view-cta">View project →</span>
    </div>
  </div>
</a>
```

**First Responder REBOOT (Video — add badge):**
```html
<a href="project-frr.html" class="work-card">
  <div class="work-thumb">
    <img src="images/frr-thumbnail-final.jpg" alt="First Responder REBOOT — nonprofit video" style="width:100%;height:100%;object-fit:cover;" />
    <div class="work-overlay">
      <span class="work-tag">Nonprofit</span>
      <span class="work-tag work-tag-cat">Video Production</span>
    </div>
    <span class="work-video-badge">▶ Video</span>
    <div class="work-name-overlay">
      <span class="work-name">First Responder REBOOT</span>
      <span class="work-view-cta">View project →</span>
    </div>
  </div>
</a>
```

**Shinin' Lyric Video (Motion — add badge):**
```html
<a href="project-shinin.html" class="work-card">
  <div class="work-thumb">
    <img src="images/shinin-thumb-final.jpg" alt="Shinin' lyric video — motion design" style="width:100%;height:100%;object-fit:cover;" />
    <div class="work-overlay">
      <span class="work-tag">Lyric Video</span>
      <span class="work-tag work-tag-cat">Motion Design</span>
    </div>
    <span class="work-video-badge">▶ Motion</span>
    <div class="work-name-overlay">
      <span class="work-name">Shinin' — Lyric Video</span>
      <span class="work-view-cta">View project →</span>
    </div>
  </div>
</a>
```

**Two Kay's Flower Farm (Photography — no badge):**
```html
<a href="project-two-kays.html" class="work-card">
  <div class="work-thumb">
    <img src="https://images.squarespace-cdn.com/content/v1/687be35b43e91200aeaa965b/b5819081-9bb5-4c36-80b6-2378687c90a6/_1220389-min.jpg" alt="Two Kay's Flower Farm brand video Kalispell MT" style="width:100%;height:100%;object-fit:cover;" />
    <div class="work-overlay">
      <span class="work-tag">Small Business</span>
      <span class="work-tag work-tag-cat">Photography</span>
    </div>
    <div class="work-name-overlay">
      <span class="work-name">Two Kay's Flower Farm</span>
      <span class="work-view-cta">View project →</span>
    </div>
  </div>
</a>
```

**Easter Promo (Motion — add badge) — NEW:**
```html
<a href="project-easter.html" class="work-card">
  <div class="work-thumb">
    <img src="https://vz-474cf03f-6bc.b-cdn.net/e6e648e4-be25-4048-a14d-0af1a4768d9c/thumbnail.jpg" alt="Easter promo motion design" style="width:100%;height:100%;object-fit:cover;" />
    <div class="work-overlay">
      <span class="work-tag">Church</span>
      <span class="work-tag work-tag-cat">Motion Design</span>
    </div>
    <span class="work-video-badge">▶ Motion</span>
    <div class="work-name-overlay">
      <span class="work-name">Easter Promo</span>
      <span class="work-view-cta">View project →</span>
    </div>
  </div>
</a>
```

**Mother Chorizo's (Video — add badge) — NEW:**
```html
<a href="project-mother-chorizos.html" class="work-card">
  <div class="work-thumb">
    <img src="images/mother-chorizos-before.png" alt="Mother Chorizo's social media content" style="width:100%;height:100%;object-fit:cover;" />
    <div class="work-overlay">
      <span class="work-tag">Small Business</span>
      <span class="work-tag work-tag-cat">Video / Social</span>
    </div>
    <span class="work-video-badge">▶ Video</span>
    <div class="work-name-overlay">
      <span class="work-name">Mother Chorizo's</span>
      <span class="work-view-cta">View project →</span>
    </div>
  </div>
</a>
```

- [ ] **Step 3: Commit**

```bash
git add index.html
git commit -m "feat: upgrade work cards — name-on-image, 6 projects, full-bleed container"
```

---

### Task 3: CSS — full-bleed grid, 4:3 ratio, name overlay, video badge

**Files:**
- Modify: `style.css` — update `.work`, `.work-grid`, `.work-thumb`, `.work-overlay`; add `.work-section-header`, `.work-name-overlay`, `.work-name`, `.work-view-cta`, `.work-video-badge`; remove `.work-info`

- [ ] **Step 1: Update the work section and grid styles**

Find and replace the `.work` and `.work-grid` blocks in `style.css`:

```css
/* ============================================
   WORK
============================================ */
.work {
  padding: 100px 0;
}

.work-section-header {
  margin-bottom: 24px;
}

.work-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  padding: 0 12px;
}
```

- [ ] **Step 2: Update `.work-thumb` aspect ratio and overflow**

Find the `.work-thumb` block and update it:

```css
.work-thumb {
  width: 100%;
  aspect-ratio: 4/3;
  border-radius: 6px;
  background-color: var(--navy-mid);
  background-size: cover;
  background-position: center;
  position: relative;
  overflow: hidden;
  transition: transform var(--transition);
}
```

- [ ] **Step 3: Add name overlay styles**

After the `.work-overlay` block, add:

```css
/* Name overlay — centered on image */
.work-name-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
  z-index: 2;
  pointer-events: none;
}

.work-name {
  font-family: var(--font);
  font-size: clamp(18px, 2.5vw, 28px);
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--white);
  text-align: center;
  text-shadow: 0 2px 12px rgba(0,0,0,0.6);
  padding: 0 24px;
  line-height: 1.2;
}

.work-view-cta {
  font-family: var(--font);
  font-size: 13px;
  font-weight: 600;
  letter-spacing: 0.05em;
  color: var(--blue);
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.work-card:hover .work-view-cta {
  opacity: 1;
  transform: translateY(0);
}
```

- [ ] **Step 4: Add video badge styles**

```css
/* Video / Motion badge */
.work-video-badge {
  position: absolute;
  top: 14px;
  right: 14px;
  z-index: 3;
  font-family: var(--font);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--white);
  background: rgba(5, 8, 15, 0.65);
  border: 1px solid rgba(255,255,255,0.18);
  padding: 4px 10px;
  border-radius: 100px;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
}
```

- [ ] **Step 5: Update `.work-overlay` — darken slightly on hover**

Find and update:

```css
.work-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(5,8,15,0.75) 0%, rgba(5,8,15,0.25) 50%, transparent 100%);
  padding: 20px;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  z-index: 1;
  transition: background 0.3s ease;
}

.work-card:hover .work-overlay {
  background: linear-gradient(to top, rgba(5,8,15,0.88) 0%, rgba(5,8,15,0.45) 60%, rgba(5,8,15,0.2) 100%);
}
```

- [ ] **Step 6: Remove `.work-info` styles**

Delete the entire `.work-info` block:
```css
.work-info {
  padding: 16px 4px 8px;
}

.work-info h4 {
  font-size: 17px;
  font-weight: 600;
  color: var(--white);
  margin-bottom: 4px;
}

.work-info p {
  font-size: 14px;
  color: var(--gray);
}
```

- [ ] **Step 7: Update mobile responsive styles for work**

Find the `@media (max-width: 600px)` block and ensure this is present:

```css
/* Work grid — full width cards on mobile */
.work-grid {
  grid-template-columns: 1fr;
  gap: 12px;
  padding: 0 12px;
}

.work-thumb {
  aspect-ratio: 4/3;
}
```

- [ ] **Step 8: Commit**

```bash
git add style.css
git commit -m "feat: full-bleed work grid, 4:3 cards, name overlay, video badge"
```

---

### Task 4: Visual QA and push

- [ ] **Step 1: Open index.html locally and check**

- Work grid appears immediately after hero (before services)
- 6 cards in 2-column grid, 4:3 ratio
- Project names centered on images
- Video badge visible top-right on FRR, Shinin', Easter, Mother Chorizo's
- No badge on Fresh Life, Two Kay's
- Hover: overlay darkens, "View project →" appears in blue
- Services section appears below the work grid
- No broken images

- [ ] **Step 2: Check mobile (resize browser to ~390px wide)**

- Grid collapses to 1 column
- Cards still 4:3
- Names still readable on image

- [ ] **Step 3: Push to GitHub**

```bash
cd /Users/joshua_soliz/Documents/newSite
git push origin main
```

