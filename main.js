// ── REEL MODAL ──
const reelModal    = document.getElementById('reelModal');
const reelIframe   = document.getElementById('reelModalIframe');
const watchReelBtn = document.getElementById('watchReelBtn');
const modalClose   = document.getElementById('reelModalClose');
const REEL_SRC     = 'https://iframe.mediadelivery.net/embed/563470/fda19b02-1470-49c8-8bd5-f665973f8e04?autoplay=true&loop=false&muted=false&preload=false&responsive=true';

function openReel() {
  if (!reelModal) return;
  reelIframe.src = REEL_SRC;
  reelModal.classList.add('open');
  reelModal.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
}

function closeReel() {
  if (!reelModal) return;
  reelModal.classList.remove('open');
  reelModal.setAttribute('aria-hidden', 'true');
  reelIframe.src = '';
  document.body.style.overflow = '';
}

if (watchReelBtn) watchReelBtn.addEventListener('click', openReel);
if (modalClose)   modalClose.addEventListener('click', closeReel);

if (reelModal) {
  reelModal.addEventListener('click', (e) => {
    if (!e.target.closest('.reel-modal-content')) closeReel();
  });
}

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape' && reelModal && reelModal.classList.contains('open')) closeReel();
});

// ── STYLEFRAME VIDEO STILLS ──
document.querySelectorAll('video[data-frametime]').forEach(v => {
  const t = parseFloat(v.dataset.frametime);
  const seek = () => { v.currentTime = t; };
  if (v.readyState >= 1) {
    seek();
  } else {
    v.addEventListener('loadedmetadata', seek, { once: true });
  }
  v.addEventListener('play', () => v.pause());
});

// ── SCROLL FADE-IN OBSERVER ──
const fadeEls = document.querySelectorAll('.fade-in');

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

fadeEls.forEach(el => observer.observe(el));

// Nav background on scroll
const nav = document.querySelector('nav');
window.addEventListener('scroll', () => {
  if (window.scrollY > 60) {
    nav.style.background = 'rgba(5, 8, 15, 0.97)';
  } else {
    nav.style.background = 'linear-gradient(to bottom, rgba(5,8,15,0.95) 0%, transparent 100%)';
  }
});

// ── QUOTE BUILDER ──
(function () {
  const rows     = document.querySelectorAll('.qb-row');
  if (!rows.length) return;

  const totalEl  = document.getElementById('qbTotal');
  const ctaEl    = document.getElementById('qbCta');
  const selected = new Map(); // id -> { label, price, category }

  function fmt(n) {
    return '$' + n.toLocaleString();
  }

  // Tab switching — exclusive, one open at a time
  const allSections = document.querySelectorAll('.qb-section');
  const allTabBtns  = document.querySelectorAll('.qb-tab-btn');

  allTabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      if (btn.classList.contains('active')) return; // already open
      allSections.forEach(s => s.classList.remove('open'));
      allTabBtns.forEach(b => b.classList.remove('active'));
      document.getElementById(btn.dataset.target).classList.add('open');
      btn.classList.add('active');
    });
  });

  function updateBadge(category) {
    const count  = Array.from(selected.values()).filter(s => s.category === category).length;
    const badge  = document.getElementById('badge-' + category);
    if (!badge) return;
    badge.textContent = count || '';
    badge.classList.toggle('visible', count > 0);
  }

  function update() {
    const total = Array.from(selected.values()).reduce((sum, s) => sum + s.price, 0);

    totalEl.textContent = fmt(total);
    totalEl.classList.toggle('has-value', selected.size > 0);

    if (selected.size > 0) {
      const lines = Array.from(selected.values())
        .map(s => `  - ${s.label} (starting at ${fmt(s.price)})`);
      const msg =
        `Hey Josh,\n\nI'm interested in building a quote for the following:\n\n` +
        lines.join('\n') +
        `\n\nEstimated starting total: ${fmt(total)}\n\nWould love to chat!`;
      ctaEl.href = 'contact.html?message=' + encodeURIComponent(msg);
    } else {
      ctaEl.href = 'contact.html';
    }
  }

  rows.forEach(row => {
    row.addEventListener('click', () => {
      const id       = row.dataset.id;
      const price    = parseInt(row.dataset.price, 10);
      const label    = row.dataset.label;
      const category = row.dataset.category;

      if (selected.has(id)) {
        selected.delete(id);
        row.classList.remove('selected');
      } else {
        selected.set(id, { label, price, category });
        row.classList.add('selected');
      }
      updateBadge(category);
      update();
    });
  });
}());
