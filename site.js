/* Consent banner, analytics consent, sticky mobile CTA */
(function () {
  var KEY = 'cookieConsent';
  window.dataLayer = window.dataLayer || [];
  if (typeof window.gtag !== 'function') window.gtag = function () { dataLayer.push(arguments); };

  function loadHubSpot() {
    if (document.getElementById('hs-script-loader')) return;
    var s = document.createElement('script');
    s.id = 'hs-script-loader'; s.async = true; s.defer = true;
    s.src = '//js-na2.hs-scripts.com/246885288.js';
    document.head.appendChild(s);
  }
  function grant() {
    gtag('consent', 'update', { analytics_storage: 'granted' });
    loadHubSpot();
  }

  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (e) {}
  if (saved === 'granted') grant();

  function banner() {
    var b = document.createElement('div');
    b.className = 'cookie-banner';
    b.setAttribute('role', 'dialog');
    b.setAttribute('aria-label', 'Cookie notice');
    b.innerHTML =
      '<p>This site uses cookies for analytics so I can see which pages are useful. ' +
      '<a href="privacy.html">Privacy policy</a></p>' +
      '<div class="cookie-actions">' +
      '<button type="button" class="cookie-btn" data-c="denied">Decline</button>' +
      '<button type="button" class="cookie-btn cookie-accept" data-c="granted">Accept</button></div>';
    b.addEventListener('click', function (e) {
      var c = e.target.getAttribute && e.target.getAttribute('data-c');
      if (!c) return;
      try { localStorage.setItem(KEY, c); } catch (err) {}
      if (c === 'granted') grant();
      b.remove();
    });
    document.body.appendChild(b);
  }
  var path = location.pathname;
  var onForm = /contact|thank-you/.test(path);

  function init() {
    if (!saved) banner();
    if (!onForm) {
      var a = document.createElement('a');
      a.className = 'sticky-cta';
      a.href = 'contact.html';
      a.textContent = 'Book a call';
      document.body.appendChild(a);
      document.body.classList.add('has-sticky-cta');
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
}());
