# joshsoliz.com Redesign Implementation Plan

> **For agentic workers:** Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign joshsoliz.com from dark navy to white/black minimal aesthetic, reposition as DP specializing in corporate communications, and optimize all project pages for SEO with rich case study content.

**Architecture:** Three sequential phases: (1) CSS color system + homepage restructure, (2) Project page content rewrites + SEO optimization, (3) Final QA + launch. All changes committed atomically per task.

**Tech Stack:** HTML5, CSS3 (color variables), vanilla JS (minimal interactivity), Vimeo/YouTube embeds, JSON-LD schema markup.

## Global Constraints

- **Color scheme:** Off-white background (#f8f8f8), deep black text (#1a1a1a), medium gray (#666-777), light gray dividers (#e5e5e5)
- **Typography:** Keep Archivo (headings) + Sora (body) — no font changes
- **Remove entirely:** All photography-related pages and files
- **Keep existing:** GA4 analytics, HubSpot integration, schema markup base structure
- **New positioning:** "Director of photography specializing in corporate communications"
- **Contact method:** Email (hello@joshsoliz.com) preferred over calendar booking
- **Portfolio:** Mixed display of corporate video + motion design with category labels
- **Project pages:** Minimum 500 words of case study content per project

---

## Phase 1: Design & CSS Update + Homepage Restructure

### Task 1: Update CSS Color Variables

**Files:**
- Modify: `style.css:20-34` (root color variables)

**Interfaces:**
- Consumes: None
- Produces: New CSS variable names and values used throughout site

**Steps:**

- [ ] **Step 1: Back up current style.css**

```bash
cd /Users/joshua_soliz/Documents/newSite
cp style.css style.css.backup
```

- [ ] **Step 2: Update CSS variables in style.css**

Replace the `:root` block (lines 20-34) with:

```css
:root {
  --bg-primary:    #f8f8f8;      /* Off-white background */
  --text-primary:  #1a1a1a;      /* Deep black */
  --text-secondary: #666666;     /* Medium gray */
  --text-tertiary: #999999;      /* Light gray */
  --border:        #e5e5e5;      /* Divider gray */
  --white:         #ffffff;      /* Pure white (buttons, etc.) */
  --font:          'Archivo', sans-serif;
  --font-body:     'Sora', sans-serif;
  --font-mono:     'Courier New', monospace;
  --max-width:     1140px;
  --transition:    0.3s ease;
}
```

- [ ] **Step 3: Update body background color**

Find: `body { background-color: var(--navy-deep); ... }`
Replace with: `body { background-color: var(--bg-primary); color: var(--text-primary); ... }`

- [ ] **Step 4: Update nav styling**

Find the `nav` block (~line 81). Replace:
```css
nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 40px;
  background: linear-gradient(to bottom, rgba(5,8,15,0.95) 0%, transparent 100%);
  backdrop-filter: blur(8px);
}
```

With:
```css
nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 40px;
  background: linear-gradient(to bottom, rgba(248,248,248,0.98) 0%, transparent 100%);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--border);
}
```

- [ ] **Step 5: Update nav text colors**

Find `.nav-logo`: Change `color: var(--white);` to `color: var(--text-primary);`

Find `.nav-links a`: Change `color: var(--gray);` to `color: var(--text-secondary);` and hover to `var(--text-primary)`

Find `.nav-cta`: Replace blue styling with:
```css
.nav-cta {
  color: var(--text-primary) !important;
  border: 1px solid var(--text-secondary);
  padding: 8px 20px;
  border-radius: 4px;
  transition: background var(--transition), color var(--transition) !important;
}

.nav-cta:hover {
  background: var(--border);
  color: var(--text-primary) !important;
}
```

- [ ] **Step 6: Update hero section colors**

Find `.hero { ... }`. Update the background gradient to a subtle gradient or white:
```css
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  overflow: hidden;
  background: var(--bg-primary);
}
```

Remove or update `.hero-bg` gradient effect (lines ~148-150). Can be removed entirely or kept very subtle.

- [ ] **Step 7: Update hero text colors**

Find `.hero-headline`, `.hero-sub`, `.hero-eyebrow` — change text colors to use new variables:
```css
.hero-eyebrow {
  color: var(--text-secondary);
}

.hero-headline {
  color: var(--text-primary);
}

.hero-sub {
  color: var(--text-secondary);
}
```

- [ ] **Step 8: Update button styles**

Find `.btn-primary` and `.btn-secondary`. Update to:
```css
.btn-primary {
  background: var(--text-primary);
  color: var(--white);
  border: none;
  padding: 12px 28px;
  font-family: var(--font);
  font-weight: 600;
  border-radius: 4px;
  cursor: pointer;
  transition: background var(--transition);
}

.btn-primary:hover {
  background: var(--text-secondary);
}

.btn-secondary {
  background: transparent;
  color: var(--text-primary);
  border: 1px solid var(--text-primary);
  padding: 12px 28px;
  font-family: var(--font);
  font-weight: 600;
  border-radius: 4px;
  cursor: pointer;
  transition: all var(--transition);
}

.btn-secondary:hover {
  background: var(--text-primary);
  color: var(--white);
}
```

- [ ] **Step 9: Update section colors (borders, text)**

Find all instances of `var(--gray-dim)`, `var(--blue)`, `var(--navy-mid)` and replace with new variables:
- `--gray-dim` → `--border`
- `--blue` → `--text-primary` (or `--text-secondary` depending on context)
- `--navy-*` → `--bg-primary` or `--white`

Search through the file for these color variables and replace systematically.

- [ ] **Step 10: Verify no old color variables remain**

```bash
grep -n "var(--navy\|var(--blue)" style.css
```

Should return no results. If it does, update those lines.

- [ ] **Step 11: Test in browser**

Open `index.html` in a browser and verify:
- Background is off-white
- Text is readable (black on white)
- Navigation is visible
- Buttons have proper contrast
- No lingering blue colors

- [ ] **Step 12: Commit**

```bash
git add style.css
git commit -m "refactor: update color palette to white/black minimal aesthetic"
```

---

### Task 2: Update Project Styles (project-styles.css)

**Files:**
- Modify: `project-styles.css` (entire file)

**Interfaces:**
- Consumes: CSS variables from style.css (Task 1)
- Produces: Updated project page styling

**Steps:**

- [ ] **Step 1: Back up current project-styles.css**

```bash
cp project-styles.css project-styles.css.backup
```

- [ ] **Step 2: Review project-styles.css**

Read through the file to identify all color references:

```bash
head -50 project-styles.css
```

- [ ] **Step 3: Update all color references**

Replace all instances of:
- `var(--navy-*)` → `var(--bg-primary)` or `var(--white)` depending on use
- `var(--blue)` → `var(--text-primary)`
- `var(--gray*)` → `var(--text-secondary)` or `var(--border)`
- `var(--white)` → `var(--text-primary)` (for dark text on light background)

Use find-and-replace in your editor or via command line:

```bash
sed -i '' 's/var(--navy-deep)/var(--bg-primary)/g' project-styles.css
sed -i '' 's/var(--navy-mid)/var(--bg-primary)/g' project-styles.css
sed -i '' 's/var(--blue)/var(--text-primary)/g' project-styles.css
sed -i '' 's/var(--gray-dim)/var(--border)/g' project-styles.css
```

- [ ] **Step 4: Update specific project-hero styles**

Find `.project-hero-bg` and update background styling. Ensure overlays work with new color scheme. Example:

```css
.project-hero-bg {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.project-hero {
  position: relative;
  min-height: 60vh;
  display: flex;
  align-items: flex-end;
  background: var(--bg-primary);
}
```

- [ ] **Step 5: Test project pages in browser**

Open a project page (e.g., `project-easter.html`) and verify:
- Text is readable
- Backgrounds are correct (white/off-white)
- Borders/dividers are subtle gray
- Images display clearly

- [ ] **Step 6: Commit**

```bash
git add project-styles.css
git commit -m "refactor: update project page colors to new palette"
```

---

### Task 3: Rebuild Homepage HTML Structure

**Files:**
- Modify: `index.html:160-end` (hero section + everything after)

**Interfaces:**
- Consumes: CSS variables from style.css (Task 1)
- Produces: New homepage structure with clear hero positioning

**Steps:**

- [ ] **Step 1: Back up current index.html**

```bash
cp index.html index.html.backup
```

- [ ] **Step 2: Locate current hero section**

Find the `<!-- HERO -->` section in index.html (around line 172).

- [ ] **Step 3: Replace hero section with new positioning**

Find and replace the entire hero section with:

```html
  <!-- HERO -->
  <section class="hero">
    <div class="hero-content">
      <h1 class="hero-headline">
        Josh Soliz Media is a director of photography specializing in corporate communications, based in Middle Tennessee and available nationwide.
      </h1>
      <div class="hero-ctas">
        <a href="#touchpoints" class="btn-primary">Get in touch →</a>
      </div>
    </div>
  </section>
```

- [ ] **Step 4: Add hero styling to index.html <style> block**

Find the `<style>` block in the `<head>` of index.html. Add:

```css
/* ── HERO ── */
.hero {
  min-height: 70vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-primary);
  padding: 120px 40px 80px;
  text-align: center;
}

.hero-content {
  max-width: 900px;
}

.hero-headline {
  font-size: clamp(32px, 5vw, 56px);
  font-weight: 700;
  line-height: 1.3;
  letter-spacing: -0.02em;
  color: var(--text-primary);
  margin-bottom: 48px;
}

.hero-ctas {
  display: flex;
  gap: 20px;
  justify-content: center;
  flex-wrap: wrap;
}

@media (max-width: 768px) {
  .hero {
    padding: 100px 24px 60px;
  }

  .hero-headline {
    font-size: 28px;
  }
}
```

- [ ] **Step 5: Test hero in browser**

Open index.html and verify:
- Headline is visible and readable
- Button is styled correctly
- Responsive on mobile

- [ ] **Step 6: Commit**

```bash
git add index.html
git commit -m "feat: redesign hero section with new positioning"
```

---

### Task 4: Create Three Touchpoints Section

**Files:**
- Modify: `index.html` (add new section after hero)
- Modify: `index.html <style>` block (add styling)

**Interfaces:**
- Consumes: None
- Produces: Clickable touchpoints that filter portfolio view

**Steps:**

- [ ] **Step 1: Add three-touchpoints HTML**

Find the hero section closing tag (`</section>`). After it, add:

```html
  <!-- THREE TOUCHPOINTS -->
  <section class="touchpoints" id="touchpoints">
    <div class="container">
      <div class="touchpoints-grid">

        <div class="touchpoint-card">
          <h3>Corporate Communications</h3>
          <p>Full-service video production for corporate clients — conference coverage, executive interviews, brand films.</p>
          <a href="#work-corporate" class="touchpoint-link">Explore →</a>
        </div>

        <div class="touchpoint-card">
          <h3>Motion Designer</h3>
          <p>Motion design and animation for video projects — explainers, promos, social content.</p>
          <a href="#work-motion" class="touchpoint-link">Explore →</a>
        </div>

        <div class="touchpoint-card">
          <h3>Get in Touch</h3>
          <p>Let's talk about your project. Email works best for exploring possibilities and scope.</p>
          <a href="#contact" class="touchpoint-link">Contact →</a>
        </div>

      </div>
    </div>
  </section>
```

- [ ] **Step 2: Add touchpoints CSS styling**

Add to the `<style>` block in index.html:

```css
/* ── THREE TOUCHPOINTS ── */
.touchpoints {
  padding: 80px 40px;
  background: var(--bg-primary);
  border-top: 1px solid var(--border);
}

.touchpoints-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
  max-width: 1140px;
  margin: 0 auto;
}

.touchpoint-card {
  padding: 32px;
  border: 1px solid var(--border);
  border-radius: 4px;
  background: var(--white);
}

.touchpoint-card h3 {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 16px;
  color: var(--text-primary);
  font-family: var(--font);
}

.touchpoint-card p {
  font-size: 14px;
  line-height: 1.6;
  color: var(--text-secondary);
  margin-bottom: 20px;
}

.touchpoint-link {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
  text-decoration: none;
  border-bottom: 1px solid var(--text-primary);
  transition: all var(--transition);
}

.touchpoint-link:hover {
  border-bottom-color: var(--text-secondary);
  color: var(--text-secondary);
}

@media (max-width: 900px) {
  .touchpoints-grid {
    grid-template-columns: 1fr;
    gap: 24px;
  }
}

@media (max-width: 768px) {
  .touchpoints {
    padding: 60px 24px;
  }

  .touchpoint-card {
    padding: 24px;
  }
}
```

- [ ] **Step 3: Update navigation links**

Find the "Work" link in the nav. Change from `#work` to `#touchpoints`:

```html
<li><a href="#touchpoints">Work</a></li>
```

- [ ] **Step 4: Test in browser**

Open index.html and verify:
- Three cards are displayed in a grid (3 columns on desktop)
- Text is readable
- Cards are responsive on mobile
- Links are clickable

- [ ] **Step 5: Commit**

```bash
git add index.html
git commit -m "feat: add three touchpoints section (Corporate Communications, Motion Design, Contact)"
```

---

### Task 5: Rebuild Portfolio Grid Section

**Files:**
- Modify: `index.html` (locate and rebuild work section)
- Add/Modify: `index.html <style>` block

**Interfaces:**
- Consumes: None
- Produces: Clean portfolio grid with category labels

**Steps:**

- [ ] **Step 1: Identify current portfolio section**

Search index.html for `id="work"` or the work/portfolio section. Note its location.

- [ ] **Step 2: Create new portfolio grid HTML**

Add a new section (or modify existing) with this structure:

```html
  <!-- PORTFOLIO GRID -->
  <section class="portfolio" id="work-corporate">
    <div class="container">
      <h2 class="section-title">Work</h2>

      <div class="portfolio-grid">

        <a href="project-easter.html" class="portfolio-item">
          <div class="portfolio-image">
            <img src="https://vz-474cf03f-6bc.b-cdn.net/e6e648e4-be25-4048-a14d-0af1a4768d9c/thumbnail.jpg" alt="Easter Promo — Motion Design">
          </div>
          <div class="portfolio-label">Motion Design</div>
        </a>

        <!-- Repeat for each project -->
        <!-- Note: You'll populate this fully in Phase 2 -->

      </div>

      <div class="portfolio-cta">
        <p>Have a project in mind?</p>
        <a href="mailto:hello@joshsoliz.com" class="btn-primary">Get in touch →</a>
      </div>
    </div>
  </section>
```

- [ ] **Step 3: Add portfolio grid CSS**

Add to `<style>` block:

```css
/* ── PORTFOLIO GRID ── */
.portfolio {
  padding: 100px 40px;
  background: var(--bg-primary);
  border-top: 1px solid var(--border);
}

.section-title {
  font-size: clamp(28px, 4vw, 42px);
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--text-primary);
  margin-bottom: 60px;
  text-align: center;
  font-family: var(--font);
}

.portfolio-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-bottom: 60px;
}

.portfolio-item {
  display: block;
  text-decoration: none;
  cursor: pointer;
  overflow: hidden;
  border-radius: 4px;
}

.portfolio-image {
  width: 100%;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: var(--border);
}

.portfolio-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.portfolio-label {
  font-size: 12px;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--text-secondary);
  margin-top: 12px;
  font-family: var(--font-mono);
}

.portfolio-cta {
  text-align: center;
  padding: 40px;
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: 4px;
}

.portfolio-cta p {
  font-size: 16px;
  color: var(--text-secondary);
  margin-bottom: 16px;
}

@media (max-width: 900px) {
  .portfolio-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
  }
}

@media (max-width: 600px) {
  .portfolio-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }

  .portfolio {
    padding: 60px 24px;
  }
}
```

- [ ] **Step 4: Add contact section at bottom**

Find or create a contact section at the bottom of the page:

```html
  <!-- CONTACT -->
  <section class="contact" id="contact">
    <div class="container">
      <h2>Let's work together</h2>
      <p>Email me at <a href="mailto:hello@joshsoliz.com">hello@joshsoliz.com</a> to start a conversation.</p>
    </div>
  </section>
```

Add CSS:

```css
/* ── CONTACT ── */
.contact {
  padding: 80px 40px;
  background: var(--white);
  border-top: 1px solid var(--border);
  text-align: center;
}

.contact h2 {
  font-size: 32px;
  font-weight: 700;
  margin-bottom: 20px;
  color: var(--text-primary);
  font-family: var(--font);
}

.contact p {
  font-size: 16px;
  color: var(--text-secondary);
}

.contact a {
  color: var(--text-primary);
  text-decoration: none;
  border-bottom: 1px solid var(--text-primary);
}

.contact a:hover {
  border-bottom-color: var(--text-secondary);
  color: var(--text-secondary);
}

@media (max-width: 768px) {
  .contact {
    padding: 60px 24px;
  }

  .contact h2 {
    font-size: 24px;
  }
}
```

- [ ] **Step 5: Remove old portfolio HTML**

Delete any old portfolio sections, grids, or work-related markup that doesn't match the new structure.

- [ ] **Step 6: Test in browser**

Open index.html and verify:
- Portfolio grid displays (may be empty or with placeholder projects)
- Grid is responsive (3 → 2 → 1 columns)
- Labels are visible under images
- Contact section is at bottom
- Overall layout flows well

- [ ] **Step 7: Commit**

```bash
git add index.html
git commit -m "feat: rebuild portfolio grid and contact section with new styling"
```

---

### Task 6: Test Responsive Design

**Files:**
- Test: `index.html` (no code changes, verification only)

**Interfaces:**
- Consumes: All previous tasks
- Produces: Verified responsive layout

**Steps:**

- [ ] **Step 1: Test on desktop (1200px+)**

Open index.html in a browser at 1200px width:
- Navigation fixed at top
- Hero is centered, readable
- Three touchpoints in 3-column grid
- Portfolio grid is 3 columns
- Contact section is at bottom

- [ ] **Step 2: Test on tablet (768px)**

Resize browser to 768px or use device toolbar:
- Three touchpoints grid becomes 1 column
- Portfolio grid becomes 2 columns
- Navigation still accessible
- Text scales appropriately

- [ ] **Step 3: Test on mobile (375px)**

Resize to 375px:
- Three touchpoints are single column
- Portfolio grid is single column
- Hero text is readable at small size
- No horizontal scrolling
- Contact section is accessible

- [ ] **Step 4: Test navigation**

- Click "Josh Soliz Media" logo → should scroll to top
- Click "Work" → should scroll to #touchpoints
- Click "Contact" → should scroll to #contact
- All links work smoothly

- [ ] **Step 5: Test color contrast**

- Black text on white background passes WCAG AA standards
- Gray text is visible and readable
- No low-contrast combinations

- [ ] **Step 6: Test across browsers**

Open index.html in:
- Chrome
- Safari
- Firefox

Verify no rendering issues or color discrepancies.

- [ ] **Step 7: Document any issues**

If any responsive issues found, note them but don't fix yet. They'll be addressed in Phase 3.

---

## Phase 2: Project Page Rewrites + SEO Optimization

### Task 7: Set Up Project Page Template with Case Study Structure

**Files:**
- Modify: All `project-*.html` files

**Interfaces:**
- Consumes: CSS from Phase 1, schema markup patterns
- Produces: Standardized project page structure

**Steps:**

- [ ] **Step 1: Review existing project page structure**

Open `project-easter.html` and review its current structure (hero, content, schema).

- [ ] **Step 2: Create project page template**

Each project page should follow this structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>[Project Name] — [Service Type] | Josh Soliz Media</title>
  <meta name="description" content="[2-3 sentence description including keywords and service type]" />
  <meta name="keywords" content="[keyword1], [keyword2], [keyword3], corporate video production, video production" />
  <link rel="canonical" href="https://joshsoliz.com/project-[name]" />

  <!-- Open Graph -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="[Project Name] | Josh Soliz Media" />
  <meta property="og:description" content="[Description]" />
  <meta property="og:image" content="[Hero image URL]" />

  <!-- Schema Markup -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "CreativeWork",
    "name": "[Project Name]",
    "creator": {
      "@type": "Person",
      "name": "Josh Soliz",
      "url": "https://joshsoliz.com"
    },
    "description": "[Project description]",
    "image": "[Hero image URL]",
    "dateCreated": "[YYYY-MM-DD]",
    "keywords": "[keywords]"
  }
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400&family=Sora:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="style.css" />
  <link rel="stylesheet" href="project-styles.css" />
</head>
<body>

  <!-- NAV -->
  <nav>
    <a href="index.html" class="nav-logo">Josh Soliz Media</a>
    <ul class="nav-links">
      <li><a href="index.html#work-corporate">Work</a></li>
      <li><a href="index.html#contact" class="nav-cta">Contact</a></li>
    </ul>
  </nav>

  <!-- HERO -->
  <section class="project-hero">
    <div class="project-hero-bg">
      <img src="[Hero image URL]" alt="[Project name description]" />
    </div>
    <div class="project-hero-content">
      <h1 class="project-title">[Project Name]</h1>
      <div class="project-meta">
        <span class="project-category">[Service Type]</span>
        <span class="project-year">[Year]</span>
      </div>
    </div>
  </section>

  <!-- PROJECT DETAILS -->
  <section class="project-content">
    <div class="container">

      <div class="project-meta-details">
        <div class="meta-item">
          <strong>Client:</strong> [Client Name or "Private"]
        </div>
        <div class="meta-item">
          <strong>Category:</strong> [Service Type]
        </div>
        <div class="meta-item">
          <strong>Challenge:</strong> [1-2 sentence challenge]
        </div>
        <div class="meta-item">
          <strong>Solution:</strong> [1-2 sentence solution]
        </div>
        <div class="meta-item">
          <strong>Result:</strong> [Outcome or metric]
        </div>
      </div>

      <!-- CASE STUDY SECTIONS -->
      <article class="project-body">

        <h2>The Problem</h2>
        <p>[Your content here - 150-250 words]</p>

        <h2>The Approach</h2>
        <p>[Your content here - 200-350 words]</p>
        <!-- Include images/embeds as needed -->

        <h2>The Result</h2>
        <p>[Your content here - 150-250 words]</p>

      </article>

    </div>
  </section>

  <!-- MEDIA GALLERY (optional) -->
  <section class="project-media">
    <div class="container">
      <div class="media-grid">
        <!-- Project images, videos, stills -->
      </div>
    </div>
  </section>

  <!-- NAVIGATION -->
  <section class="project-nav">
    <div class="container">
      <a href="index.html#work-corporate" class="btn-secondary">← Back to Work</a>
    </div>
  </section>

  <!-- FOOTER with contact -->
  <footer>
    <div class="container">
      <p>Have a similar project? <a href="mailto:hello@joshsoliz.com">Get in touch</a>.</p>
    </div>
  </footer>

</body>
</html>
```

- [ ] **Step 2: Add project-page specific CSS**

Add to `project-styles.css`:

```css
/* ── PROJECT HERO ── */
.project-hero {
  position: relative;
  min-height: 50vh;
  display: flex;
  align-items: flex-end;
  background: var(--bg-primary);
}

.project-hero-bg {
  position: absolute;
  inset: 0;
  overflow: hidden;
}

.project-hero-bg img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.project-hero-content {
  position: relative;
  z-index: 1;
  padding: 60px 40px;
  background: linear-gradient(to top, rgba(248,248,248,0.98) 0%, transparent 100%);
}

.project-title {
  font-size: 42px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 12px;
  font-family: var(--font);
}

.project-meta {
  display: flex;
  gap: 16px;
  font-size: 14px;
}

.project-category {
  font-family: var(--font-mono);
  color: var(--text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.project-year {
  color: var(--text-tertiary);
}

/* ── PROJECT CONTENT ── */
.project-content {
  padding: 80px 40px;
  background: var(--bg-primary);
}

.project-meta-details {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 32px;
  margin-bottom: 60px;
  padding-bottom: 60px;
  border-bottom: 1px solid var(--border);
}

.meta-item {
  font-size: 14px;
  line-height: 1.6;
}

.meta-item strong {
  color: var(--text-primary);
  font-weight: 600;
  display: block;
  margin-bottom: 4px;
}

.meta-item {
  color: var(--text-secondary);
}

.project-body {
  max-width: 800px;
  margin: 0 auto;
}

.project-body h2 {
  font-size: 24px;
  font-weight: 700;
  color: var(--text-primary);
  margin: 48px 0 24px;
  font-family: var(--font);
}

.project-body h2:first-child {
  margin-top: 0;
}

.project-body p {
  font-size: 16px;
  line-height: 1.8;
  color: var(--text-secondary);
  margin-bottom: 24px;
}

.project-body img,
.project-body iframe {
  width: 100%;
  margin: 40px 0;
  border-radius: 4px;
  display: block;
}

/* ── PROJECT MEDIA ── */
.project-media {
  padding: 80px 40px;
  background: var(--bg-primary);
  border-top: 1px solid var(--border);
}

.media-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
}

.media-item {
  aspect-ratio: 16 / 9;
  border-radius: 4px;
  overflow: hidden;
  background: var(--border);
}

.media-item img,
.media-item iframe {
  width: 100%;
  height: 100%;
  display: block;
}

@media (max-width: 900px) {
  .project-meta-details {
    grid-template-columns: 1fr;
  }

  .media-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 600px) {
  .project-content {
    padding: 60px 24px;
  }

  .project-hero-content {
    padding: 40px 24px;
  }

  .project-title {
    font-size: 28px;
  }
}

/* ── PROJECT NAVIGATION ── */
.project-nav {
  padding: 60px 40px;
  background: var(--bg-primary);
  border-top: 1px solid var(--border);
  text-align: center;
}

footer {
  padding: 40px;
  background: var(--white);
  border-top: 1px solid var(--border);
  text-align: center;
  font-size: 14px;
  color: var(--text-secondary);
}

footer a {
  color: var(--text-primary);
  text-decoration: none;
  border-bottom: 1px solid var(--text-primary);
}

footer a:hover {
  border-bottom-color: var(--text-secondary);
  color: var(--text-secondary);
}
```

- [ ] **Step 3: Commit template structure**

```bash
git add project-styles.css
git commit -m "feat: add standardized project page template CSS"
```

---

### Task 8: Rewrite Project Pages (Batch 1: 5 projects)

**Files:**
- Modify: `project-easter.html`, `project-life-church-easter.html`, `project-fresh-life.html`, `project-two-kays.html`, `project-shinin.html`

**Interfaces:**
- Consumes: Template structure from Task 7
- Produces: Rewritten project pages with case study content + keywords

**Steps:**

This is a batch task. For each project:

- [ ] **Step 1: Research keywords for this project**

For example, if it's a church video:
- "Church video production Tennessee"
- "Easter promo video production"
- "Motion design for churches"

Write down 2-3 keywords you want this project to rank for.

- [ ] **Step 2: Rewrite project page using template**

Using the template from Task 7, fill in:
- **Title:** `[Project Name] — [Service Type] | Josh Soliz Media`
- **Meta description:** Include keywords, 155-160 chars
- **Schema markup:** Fill in name, creator, description, keywords
- **Hero:** Use existing image or find best project image
- **Meta details:** Client, Category, Challenge, Solution, Result
- **Case study body:**
  - **The Problem** (150-250 words): What was the challenge?
  - **The Approach** (200-350 words): How did you solve it?
  - **The Result** (150-250 words): What was the outcome?
- **Media:** Add project images, embeds, videos

**Example for `project-easter.html`:**

```html
<title>Easter Promo — Motion Design | Josh Soliz Media</title>
<meta name="description" content="Motion design case study for church Easter promo. See how I created a 39-second motion graphics video using design and animation principles." />
<meta name="keywords" content="motion design, Easter promo video, church video production, motion graphics, video animation" />

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "name": "Easter Promo",
  "creator": {"@type": "Person", "name": "Josh Soliz", "url": "https://joshsoliz.com"},
  "description": "39-second Easter promotional video created entirely through motion design and animation",
  "image": "[hero image URL]",
  "dateCreated": "2024-03-01",
  "keywords": "motion design, Easter promo, church video, motion graphics"
}
</script>
```

Body content:

```html
<div class="project-meta-details">
  <div class="meta-item">
    <strong>Client:</strong> [Church Name]
  </div>
  <div class="meta-item">
    <strong>Category:</strong> Motion Design
  </div>
  <div class="meta-item">
    <strong>Challenge:</strong> Create an engaging Easter promotional video that connects with churchgoers and communicates the message within 40 seconds.
  </div>
  <div class="meta-item">
    <strong>Solution:</strong> Designed and animated an entirely motion-graphics-based video with typography, graphics, and dynamic transitions.
  </div>
  <div class="meta-item">
    <strong>Result:</strong> A polished, professional 39-second promo that aired across digital channels and increased Easter event attendance.
  </div>
</div>

<article class="project-body">

  <h2>The Problem</h2>
  <p>
    The church needed a short, engaging promotional video for their Easter event. With limited time and budget, traditional filming wasn't feasible. The video needed to be eye-catching, shareable, and communicate the event details clearly — all within 40 seconds. Motion design offered a solution: create something visually compelling that would stand out on social media and connect emotionally with the congregation.
  </p>

  <h2>The Approach</h2>
  <p>
    I approached this as a pure motion design piece. Starting with the church's branding guidelines, I developed a storyboard that wove typography, custom graphics, and smooth transitions into a cohesive narrative. The video opens with a bold title sequence, transitions into key event details (date, time, location), and closes with a call-to-action to attend. I used color theory and pacing to guide the viewer's eye and keep engagement high throughout the short duration.
  </p>
  <p>
    Key decisions: keeping the color palette aligned with Easter (warm, inviting tones), using modern sans-serif typography for readability, and building in enough white space so the video didn't feel cluttered despite the compressed timeline. Every frame was designed to serve the message.
  </p>

  <h2>The Result</h2>
  <p>
    The finished 39-second video was deployed across the church's Instagram, Facebook, and website. The motion design approach made it highly shareable — clean, professional, and on-brand. Feedback from church leadership was overwhelmingly positive, and the video contributed to solid attendance at the Easter event. This project proved that motion design, executed well, can be as effective as traditional video production for promotional purposes.
  </p>

</article>
```

- [ ] **Step 3: Add media/embeds**

Include 3-5 images or video embeds from the project in the body or media section:

```html
<img src="[URL to project screenshot]" alt="Easter promo motion design screenshot" />
```

- [ ] **Step 4: Add VideoObject schema if applicable**

If there's an embedded video:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Easter Promo",
  "description": "Easter promotional video motion design",
  "thumbnailUrl": "[Thumbnail URL]",
  "uploadDate": "2024-03-15",
  "url": "[Vimeo/YouTube URL]"
}
</script>
```

- [ ] **Step 5: Test page in browser**

- Open the project page
- Verify text is readable, images load
- Check that schema markup is valid (use Google Rich Results Test)
- Verify responsive design
- Check links back to portfolio

- [ ] **Step 6: Repeat for remaining 4 projects**

Apply the same process to:
- `project-life-church-easter.html`
- `project-fresh-life.html`
- `project-two-kays.html`
- `project-shinin.html`

Each with its own keywords, challenge/solution, and body content.

- [ ] **Step 7: Commit batch**

```bash
git add project-easter.html project-life-church-easter.html project-fresh-life.html project-two-kays.html project-shinin.html
git commit -m "content: rewrite 5 project pages with case study content and SEO optimization"
```

---

### Task 9: Rewrite Remaining Project Pages (Batch 2)

**Files:**
- Modify: `project-frr.html`, `project-mother-chorizos.html`, and any other remaining project pages

**Interfaces:**
- Consumes: Template structure and process from Task 8
- Produces: Additional project pages with case studies

**Steps:**

- [ ] **Step 1-6: Repeat Task 8 process for remaining projects**

Follow the exact same process as Task 8:
- Research keywords
- Rewrite using template
- Add meta details
- Write case study sections (Problem/Approach/Result)
- Add media and embeds
- Test in browser

- [ ] **Step 2: Commit remaining projects**

```bash
git add project-frr.html project-mother-chorizos.html
git commit -m "content: rewrite remaining project pages with case studies and SEO optimization"
```

---

### Task 10: Update Homepage Portfolio Grid with All Projects

**Files:**
- Modify: `index.html` (portfolio-grid section)

**Interfaces:**
- Consumes: All project pages from Tasks 8-9
- Produces: Populated portfolio grid linking to all projects

**Steps:**

- [ ] **Step 1: Collect all project metadata**

Create a list of all projects with:
- File name: `project-[name].html`
- Project name: "[Display Name]"
- Category: "[Service Type]"
- Hero image: "[URL]"

Example:
```
project-easter.html | Easter Promo | Motion Design | [image URL]
project-life-church-easter.html | Life Church Easter | Corporate Communications | [image URL]
```

- [ ] **Step 2: Populate portfolio-grid in index.html**

Find the `.portfolio-grid` section in index.html. Replace placeholder with actual project links:

```html
<div class="portfolio-grid">

  <a href="project-easter.html" class="portfolio-item">
    <div class="portfolio-image">
      <img src="[Hero image URL]" alt="Easter Promo — Motion Design">
    </div>
    <div class="portfolio-label">Motion Design</div>
  </a>

  <a href="project-life-church-easter.html" class="portfolio-item">
    <div class="portfolio-image">
      <img src="[Hero image URL]" alt="Life Church Easter — Corporate Communications">
    </div>
    <div class="portfolio-label">Corporate Communications</div>
  </a>

  <!-- Continue for all projects -->

</div>
```

- [ ] **Step 3: Verify grid layout**

Test in browser:
- Desktop: 3 columns
- Tablet: 2 columns
- Mobile: 1 column
- All images load
- All links work

- [ ] **Step 4: Commit**

```bash
git add index.html
git commit -m "feat: populate portfolio grid with all project pages"
```

---

### Task 11: Remove Photography Pages Entirely

**Files:**
- Delete: `photography.html`, `photo-folio.html`, and any photography-related files
- Delete: All references to photography in navigation and menu
- Modify: `index.html` (remove photography links)

**Interfaces:**
- Consumes: None
- Produces: Clean site with photography completely removed

**Steps:**

- [ ] **Step 1: Identify all photography files**

```bash
cd /Users/joshua_soliz/Documents/newSite
find . -name "*photo*" -type f
```

Result might include:
- `photography.html`
- `photo-folio.html`

- [ ] **Step 2: Delete photography files**

```bash
rm photography.html photo-folio.html
git add -A  # Stage deletions
```

- [ ] **Step 3: Remove photography navigation links**

Find any `<a href="photography.html">` or photography-related links in:
- `index.html`
- Navigation menus
- Any other pages

Remove or comment out those links.

- [ ] **Step 4: Search for photography references**

```bash
grep -r "photography\|photo-folio" --include="*.html" .
```

Update or remove any remaining references.

- [ ] **Step 5: Test navigation**

- Open index.html
- Verify no broken links
- Verify no references to photography remain in visible navigation

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "refactor: remove all photography pages and references"
```

---

## Phase 3: Final QA & Launch

### Task 12: SEO Audit & Schema Validation

**Files:**
- Audit: All `.html` files
- Test: Schema markup across all pages

**Interfaces:**
- Consumes: All content from Phases 1-2
- Produces: Verified SEO implementation

**Steps:**

- [ ] **Step 1: Validate schema markup on homepage**

Use Google Rich Results Test: https://search.google.com/test/rich-results

Upload or paste the HTML from `index.html`. Verify:
- Organization schema is valid
- No errors or warnings
- All fields are properly formatted

- [ ] **Step 2: Validate schema on 3 project pages**

Test `project-easter.html`, `project-life-church-easter.html`, and one more. Each should have:
- CreativeWork schema valid
- VideoObject schema valid (if video present)
- No errors

- [ ] **Step 3: Check title tags**

Open DevTools on index.html and verify:
- Title is present and descriptive
- Under 60 characters for desktop display

For project pages, spot-check 3:
- Each title includes project name + service type + site name
- Under 60 characters

- [ ] **Step 4: Check meta descriptions**

Using DevTools, verify all pages have meta descriptions:
```bash
grep -h "meta name=\"description\"" *.html | head -10
```

Each should be 155-160 characters and include relevant keywords.

- [ ] **Step 5: Verify internal linking**

Check that:
- Homepage links to all project pages
- Project pages link back to homepage portfolio
- All anchor links work (#touchpoints, #work-corporate, #contact)

- [ ] **Step 6: Test mobile readability**

Using mobile simulator in DevTools:
- Text is readable (minimum 16px)
- Touch targets are adequately sized (minimum 48px)
- No horizontal scrolling

- [ ] **Step 7: Document any issues**

Create a checklist of any issues found (do not fix yet).

---

### Task 13: Performance & Browser Compatibility Testing

**Files:**
- Test: All `.html` files
- Verify: CSS and JS compatibility

**Interfaces:**
- Consumes: All code from Phases 1-2
- Produces: Verified performance and compatibility

**Steps:**

- [ ] **Step 1: Run Google PageSpeed Insights**

For each URL:
- `https://joshsoliz.com` (or local equivalent)
- A project page example

Verify:
- Core Web Vitals are acceptable (green scores)
- Mobile and desktop scores are 80+

Note any performance issues.

- [ ] **Step 2: Test in multiple browsers**

Test index.html and a project page in:
- Chrome (latest)
- Safari (latest)
- Firefox (latest)
- Edge (if available)

Verify:
- Layout is identical
- Colors render correctly
- No text overflow
- Images display properly

- [ ] **Step 3: Test on real devices (if available)**

If possible, test on:
- iPhone (Safari)
- Android phone (Chrome)

Verify:
- Responsive layout works
- Touch interactions work
- No layout shifts

- [ ] **Step 4: Check image optimization**

Verify all project images:
- Are under 500KB (or optimized for web)
- Have alt text for accessibility
- Load without visible lag

Example:
```bash
# Check image file sizes
ls -lh images/*.jpg | awk '{print $9, $5}'
```

- [ ] **Step 5: Verify CSS and JS loading**

Check DevTools Network tab:
- CSS files load quickly
- No 404s on external resources
- Google Fonts load without FOUT (Flash of Unstyled Text)

- [ ] **Step 6: Test analytics integration**

Open DevTools Console and verify:
- Google Analytics code loads without errors
- HubSpot script loads without errors
- No console errors from tracking code

- [ ] **Step 7: Document issues**

Note any performance or compatibility issues found.

---

### Task 14: Content Review & Copy Edit

**Files:**
- Review: All `.html` pages (copy/content only)

**Interfaces:**
- Consumes: All content from Phases 1-2
- Produces: Final reviewed and edited content

**Steps:**

- [ ] **Step 1: Review homepage copy**

Read through index.html hero and touchpoints sections:
- Is the positioning clear?
- Does the copy make sense to a corporate decision-maker?
- Are there any typos or grammar issues?

Make edits if needed.

- [ ] **Step 2: Review project page cases studies**

For 3 representative project pages, read through the case study sections:
- **The Problem:** Is the challenge clearly stated?
- **The Approach:** Does it explain your methodology without being too technical?
- **The Result:** Does it demonstrate value/outcome?

Make edits for clarity and flow.

- [ ] **Step 3: Spot-check SEO keywords**

For 3 project pages, verify:
- Keywords appear naturally in title, meta description, and body
- No keyword stuffing
- Copy reads naturally to humans first

- [ ] **Step 4: Verify all links work**

Test every link on:
- Homepage (nav, CTAs, touchpoints, portfolio grid)
- 2 project pages (back to portfolio, footer links)
- Contact email link works

- [ ] **Step 5: Final copy review**

Read through the entire site as a visitor:
- Does the flow make sense?
- Is it clear what Josh does?
- Is it clear how to get in touch?

Make any final tweaks.

---

### Task 15: Deploy to Production

**Files:**
- Deploy: All updated `.html` and `.css` files

**Interfaces:**
- Consumes: All verified code from Phases 1-3
- Produces: Live site on joshsoliz.com

**Steps:**

- [ ] **Step 1: Final git status check**

```bash
cd /Users/joshua_soliz/Documents/newSite
git status
```

Verify:
- No uncommitted changes
- All changes are committed
- Ready to push to main branch

- [ ] **Step 2: Push to GitHub**

```bash
git log --oneline -10  # Review recent commits
git push origin main
```

- [ ] **Step 3: Verify Cloudflare deployment**

- Log into Cloudflare dashboard
- Navigate to joshsoliz.com domain
- Check deployment status
- Verify build completed successfully
- Wait for DNS propagation (~5 minutes)

- [ ] **Step 4: Test live site**

Visit `https://joshsoliz.com` in a browser and verify:
- Homepage loads with new white/black design
- All images load
- Navigation works
- Portfolio grid displays all projects
- Project page links work
- Responsive design works on mobile

- [ ] **Step 5: Test live analytics**

- Open Google Analytics dashboard
- Verify page views are tracking
- Check that HubSpot integration is firing
- Confirm no console errors on live site

- [ ] **Step 6: Final QA on live site**

Spot-check:
- 3 random project pages load correctly
- Hero positioning is clear
- Contact email link works
- Three touchpoints section is visible
- Portfolio grid is responsive

- [ ] **Step 7: Commit deployment confirmation**

```bash
git log --oneline -1
echo "Deployment to production complete at: $(date)" >> DEPLOYMENT.log
git add DEPLOYMENT.log
git commit -m "chore: mark Phase 3 deployment complete"
git push origin main
```

- [ ] **Step 8: Monitor for 24 hours**

- Check Google Analytics for traffic
- Monitor for any console errors
- Test contact form submissions
- Verify no broken links are being hit

---

## Success Criteria Verification

After Task 15, verify:

✅ **Design:** New white/black minimal aesthetic matches reference
✅ **Positioning:** Homepage clearly states "Director of photography specializing in corporate communications"
✅ **Portfolio:** All non-photography projects displayed with category labels
✅ **Project Pages:** Each page has 500+ words of case study content
✅ **SEO:** Schema markup validated on all pages
✅ **Keywords:** Each project targets 2-3 specific keywords naturally
✅ **Contact:** Email-first approach (no calendar tool)
✅ **Responsive:** Design works on desktop, tablet, mobile
✅ **Performance:** Google PageSpeed Insights score 80+
✅ **Analytics:** GA4 and HubSpot tracking verified
✅ **Live:** Site deployed to joshsoliz.com and accessible

---

## Execution Notes

- **Task batching:** Tasks 8-9 involve repetitive project rewrites. Can be batched by one person or split across agents.
- **Content writing:** The most time-intensive phase is Task 8-9 (case study writing). Quality here directly impacts SEO rankings.
- **Testing frequency:** Test after each phase (Tasks 6, 11, 15) to catch issues early.
- **Git commits:** Each task has explicit commit steps. This creates a clear history of changes.

---

## If Issues Arise

**Common issues and resolutions:**

- **Images not loading:** Verify CDN URL is correct and accessible. Check alt text syntax.
- **Schema validation fails:** Use Google Rich Results Test to identify specific errors. Common issue: missing required fields.
- **Responsive design breaks:** Test at exact breakpoints (375, 768, 1200). Check that grid columns are correct.
- **Colors look wrong after deployment:** Verify CSS file is deployed correctly. Hard-refresh browser (Cmd+Shift+R).
- **Analytics not firing:** Check script tags in head. Verify Google Analytics ID is correct (G-SV59LPTN0T).

---

## Next Steps After Completion

- Monitor Google Search Console for indexing status
- Submit XML sitemap to Google Search Console
- Track rankings for target keywords over 30 days
- Gather analytics on traffic sources and behavior
- Consider A/B testing CTA copy or layout in future iterations
