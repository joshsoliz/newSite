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
