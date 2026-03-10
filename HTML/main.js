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
