# joshsoliz.com Redesign Specification
**Date:** August 13, 2026
**Project:** Complete visual redesign + SEO optimization
**Status:** Design approved, ready for implementation

---

## Executive Summary

Redesign joshsoliz.com from dark navy/blue theme to minimal white/black aesthetic (inspired by blasepivovar.com). Simultaneously optimize all project pages for SEO with richer case study content, improved keyword targeting, and enhanced schema markup. Position Josh as a **Director of Photography specializing in corporate communications**, with motion design as a secondary offering.

**Goals:**
1. ✅ Match blasepivovar.com's clean, minimal aesthetic
2. ✅ Improve SEO rankings on project pages through case studies + keywords + schema
3. ✅ Remove photography entirely (word-of-mouth only)
4. ✅ Clear positioning for B2B corporate clients
5. ✅ Lower-friction lead capture (email vs. calendar tool)

---

## Visual Design System

### Color Palette
| Element | Color | Purpose |
|---------|-------|---------|
| Background | Off-white (#f8f8f8) | Primary canvas, warm but clean |
| Primary Text | Deep black (#1a1a1a) | Headlines, primary content |
| Secondary Text | Medium gray (#666-777) | Descriptions, metadata, supporting text |
| Borders/Dividers | Light gray (#e5e5e5) | Subtle separation, minimal |
| Accents | None (all black/gray) | Emphasis through weight + contrast, no blue |
| Links | Black with underline (hover) | Subtle interactive state |

**Rationale:** High contrast for readability, minimal color reduces cognitive load, focuses attention on imagery and typography.

### Typography
- **Headings:** Archivo (keep existing)
  - H1: Bold, large, black
  - H2/H3: Medium weight, clean hierarchy
- **Body:** Sora (keep existing)
  - 16px base, 1.6-1.8 line-height
  - Gray (#666) for secondary text
- **Metadata/Labels:** Monospace (optional)
  - Project categories, dates, small type
  - 12-14px, light gray

**Rationale:** Existing typeface choices are professional and clean; retain for consistency while updating color scheme.

---

## Page Structure & Layout

### Navigation (Global)
**Design:**
- Fixed at top, minimal
- Left: Logo "Josh Soliz Media" (links to home)
- Right: "Work" | "Contact"
- Black text on white background
- No hover effects
- Responsive: hamburger menu on mobile (optional)

**Rationale:** Keep navigation simple, let portfolio be the focus. Fixed nav ensures easy access to key sections.

---

### Homepage

#### Section 1: Hero
**Content:**
```
Josh Soliz Media is a director of photography
specializing in corporate communications, based in
Middle Tennessee and available nationwide.
```

**Design:**
- Full viewport height or 80vh minimum
- Centered text (or left-aligned, TBD based on visual mockup)
- Large headline font (48px+, responsive)
- Optional: subtle hero image or video background (one of your best projects)
- One CTA below: "Get in touch" → scrolls to contact section

**Rationale:** Direct B2B positioning. No aspirational copy. Corporate decision-makers land and immediately know what you do.

---

#### Section 2: Three Touchpoints
**Design:**
Three clickable cards/sections below hero:

1. **Corporate Communications**
   - Brief description: "Full-service video production for corporate clients"
   - Click → filters portfolio to corporate work (or scrolls with highlight)

2. **Motion Designer**
   - Brief description: "Motion design & animation for video projects"
   - Click → filters portfolio to motion work

3. **Contact**
   - Brief description: "Let's talk about your project"
   - Click → scrolls to contact section

**Visual:** Simple card layout (3 columns desktop, stack on mobile), minimal borders, text-heavy.

**Rationale:** Lower friction than navigation. Visitors can immediately choose what interests them. All paths lead to portfolio.

---

#### Section 3: Portfolio Grid
**Design:**
- **Grid:** 3 columns (desktop), 2 (tablet), 1 (mobile)
- **Aspect ratio:** 16:9 or square (consistent across all projects)
- **Thumbnail:** High-quality project image
- **Label:** Category underneath (12-14px monospace gray)
  - Examples: "Corporate Communications", "Motion Design", "Brand Video"
- **Click:** Links to full project page
- **No hover effects**
- **Gap:** 20-24px between items

**Below grid:** "Have a project in mind? Get in touch" + email link

**Rationale:** Visual-first approach, clean and minimal. Category labels help visitors understand project type without reading copy.

---

#### Section 4: Contact Section
**Design:**
- Centered text, 80-100px vertical padding
- Headline: "Let's work together" or "Get in touch"
- Subheading: "Email me at hello@joshsoliz.com to start a conversation"
- Optional: Simple form (name, email, message) → posts to hello@
- No calendar tool

**Rationale:** Email-first reduces friction. You can respond and qualify from there. Better for B2B workflows.

---

### Project Pages

#### Structure
Each project page is a **mini case study** with the following sections:

**1. Hero Section**
- Full-width image or video of project
- Project title overlaid or below (H1)
- Category + year subtitle (e.g., "Corporate Communications · 2024")

**2. Project Meta** (quick reference)
```
Client: [Company Name]
Category: [Corporate Communications / Motion Design / etc.]
Challenge: [1-2 sentence problem statement]
Solution: [1-2 sentence what you did]
Result: [Key metrics or outcome if available]
```

**3. Body Content** (500-1000 words, structured)

**The Problem:**
- What the client needed
- Context and constraints
- Why it mattered

**The Approach:**
- Your creative/technical strategy
- Key decisions and reasoning
- Process or methodology

**The Result:**
- What shipped
- Performance metrics (views, engagement, conversion) if available
- Client feedback or testimonial

Intersperse with:
- Project images and stills
- Video embeds (Vimeo/YouTube)
- Process photos or style frames
- Before/after comparisons if relevant

**4. Navigation**
- Breadcrumb: "← Back to Work"
- Optional: Next/Previous project links (keeps users browsing)

---

## SEO & Schema Strategy

### On-Page Optimization

**Project Page Titles:**
- Format: `[Project Name] — [Service Type] | Josh Soliz Media`
- Example: `Executive Interview: TechCorp Leadership Profile — Corporate Communications | Josh Soliz Media`
- Include target keyword naturally

**Meta Descriptions:**
- 155-160 characters
- Highlight the specific service + result
- Example: "Corporate interview production for TechCorp. See how we captured authentic executive leadership stories."

**Header Hierarchy:**
- H1: Project name/title
- H2: Section headings (The Problem, The Approach, The Result)
- Keyword placement: natural, in service of readability

**Keyword Strategy:**
- Each project targets 2-3 specific keywords
- Examples:
  - "Corporate video production for tech companies"
  - "Executive interview videography"
  - "Motion design for nonprofits"
  - "Conference video coverage Nashville"
- Research keywords for each project type before writing

**Internal Linking:**
- Next/previous project links on project pages
- Related projects linked in body copy (e.g., "Similar work: [link]")
- Portfolio grid links thematically
- Helps Google understand site structure + keeps visitors engaged

---

### Schema Markup (Structured Data)

**Homepage:**
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Josh Soliz Media",
  "description": "Director of photography specializing in corporate communications",
  "url": "https://joshsoliz.com",
  "email": "hello@joshsoliz.com",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Clarksville",
    "addressRegion": "TN",
    "addressCountry": "US"
  },
  "areaServed": ["Clarksville, TN", "Nashville, TN", "United States", "Nationwide"],
  "serviceType": ["Corporate Video Production", "Video Production", "Director of Photography", "Motion Design", "Corporate Communications"]
}
```

**Project Pages:**
```json
{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "name": "[Project Name]",
  "description": "[Project description / case study summary]",
  "creator": {
    "@type": "Person",
    "name": "Josh Soliz",
    "url": "https://joshsoliz.com"
  },
  "image": "[Project hero image URL]",
  "dateCreated": "[Project date]",
  "keywords": "[Relevant keywords for this project]"
}
```

**Project Pages (if video embedded):**
```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "[Video title]",
  "description": "[Video description]",
  "thumbnailUrl": "[Thumbnail image URL]",
  "uploadDate": "[Date published]",
  "url": "[Video URL or embed]"
}
```

**Optional: FAQ Schema (Contact Page)**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What's your process?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Your answer]"
      }
    }
  ]
}
```

---

## Content Strategy for Project Pages

### Goals
1. Rank for service-specific keywords (e.g., "corporate video production for tech companies")
2. Demonstrate expertise and case study quality
3. Provide enough detail to help prospects understand your approach
4. Include enough keyword variation to rank for related searches

### Process per Project Page

1. **Keyword Research**
   - Identify 2-3 target keywords for the project
   - Consider the client type, service type, location
   - Use tools (Google Keyword Planner, Ahrefs, etc.) to validate search volume

2. **Content Outline**
   - **The Problem** (150-250 words): Introduce the challenge
   - **The Approach** (200-350 words): Explain your methodology
   - **The Result** (150-250 words): Show outcomes
   - **Interspersed media:** Images, videos, process shots

3. **Writing Guidelines**
   - Write for humans first, keywords second (natural language)
   - Use descriptive language for images (alt text, captions)
   - Include specific metrics if available (view counts, engagement rates, client feedback)
   - Be authentic about your process and learnings

4. **Visual Content**
   - High-quality project images
   - Embedded video (Vimeo/YouTube preferred for SEO)
   - Process photos or behind-the-scenes
   - Style frames or stills (especially for motion work)
   - Aim for 3-5 images per 500 words of text

---

## Technical Specifications

### File/Directory Structure
- `index.html` (homepage)
- `project-[name].html` (individual project pages)
- `style.css` (global styles, updated color scheme)
- `project-styles.css` (project page styles, keep existing)
- `/images/` (project images, organized by project)
- `/docs/superpowers/specs/` (this design spec and implementation plan)

### Color Replacement
- Replace `--navy-deep`, `--navy`, `--navy-mid`, `--blue*` with new white/black palette
- Keep `--font` and `--font-body` (Archivo, Sora)
- Update all hover/active states to work with new palette

### Responsive Breakpoints
- Desktop: 1140px max-width (existing)
- Tablet: 768px
- Mobile: 375px
- Grid adjusts: 3 columns → 2 → 1

### Performance
- Lazy load project images (loading="lazy" on img tags)
- Optimize images for web (WebP if possible, fallback JPG)
- Minimize CSS/JS (existing setup should suffice)

---

## Content Deletion

**Remove entirely:**
- All photography-related pages and sections
- Photography portfolio pages
- Photography project pages
- References to photography in navigation/menus

**Keep:**
- Video and motion design projects
- Corporate communication work
- Any cross-service projects (if applicable)

---

## Implementation Phases

### Phase 1: Design & Structure (1-2 weeks)
- Update CSS color variables
- Redesign homepage HTML/layout
- Create three-touchpoint section
- Rebuild portfolio grid
- Test responsive design

### Phase 2: Project Pages (2-3 weeks)
- Rewrite project page content (case studies)
- Add keyword targeting per project
- Enhance schema markup
- Add rich media (images, videos)
- Internal link strategy implementation

### Phase 3: Testing & Launch (1 week)
- Audit all SEO elements (titles, descriptions, schema)
- Cross-browser testing
- Mobile testing
- GA4 setup verification
- HubSpot integration verification
- Deploy to production

---

## Success Criteria

✅ New design matches blasepivovar.com aesthetic (white/black minimal)
✅ Clear B2B positioning on homepage (DP specializing in corporate comms)
✅ All photography removed from site
✅ Project pages include case study content (500+ words per project)
✅ All project pages have improved schema markup
✅ At least 3-5 high-value keywords targeted across project pages
✅ Email-first contact strategy implemented
✅ Responsive design tested on mobile/tablet/desktop
✅ Analytics tracking verified (GA4, HubSpot)
✅ Site performance maintained or improved (Core Web Vitals)

---

## Open Questions / Decisions Pending

None — design fully approved.

---

## Next Steps

1. ✅ This spec is reviewed and approved
2. → Invoke writing-plans skill to create detailed implementation plan
3. → Begin Phase 1 (design & CSS update)
4. → Execute phases in sequence with user checkpoints
