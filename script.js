/* Keramoti Seaside Rooms — placeholder landing page.
   Progressive enhancement only: the page is fully readable without JS. */
(function () {
  'use strict';

  var root = document.documentElement;

  /* ---- Mobile nav ---- */
  var toggle = document.getElementById('navToggle');
  var menu = document.getElementById('navMenu');

  function closeMenu() {
    menu.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
  }

  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });

    // Close after tapping a link on small screens.
    menu.addEventListener('click', function (e) {
      if (e.target.closest('a')) closeMenu();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('is-open')) {
        closeMenu();
        toggle.focus();
      }
    });
  }

  /* ---- Language switch (ΕΛ / EN / both) ---- */
  var LANG_KEY = 'ksr-lang';
  var buttons = Array.prototype.slice.call(document.querySelectorAll('[data-setlang]'));

  function applyLang(lang) {
    if (['el', 'en', 'both'].indexOf(lang) === -1) lang = 'both';
    root.setAttribute('data-lang', lang);
    root.setAttribute('lang', lang === 'en' ? 'en' : 'el');
    buttons.forEach(function (b) {
      b.setAttribute('aria-pressed', b.getAttribute('data-setlang') === lang ? 'true' : 'false');
    });
    try { localStorage.setItem(LANG_KEY, lang); } catch (err) { /* private mode */ }
  }

  var stored = null;
  try { stored = localStorage.getItem(LANG_KEY); } catch (err) { /* ignore */ }
  if (stored) applyLang(stored);

  buttons.forEach(function (b) {
    b.addEventListener('click', function () {
      applyLang(b.getAttribute('data-setlang'));
    });
  });

  /* ---- Sticky nav shadow ---- */
  var nav = document.getElementById('nav');
  if (nav) {
    var onScroll = function () {
      nav.classList.toggle('is-stuck', window.scrollY > 12);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---- Highlight the section currently in view ---- */
  var links = Array.prototype.slice.call(document.querySelectorAll('.nav__menu a[href^="#"]'));
  var sections = links
    .map(function (a) { return document.querySelector(a.getAttribute('href')); })
    .filter(Boolean);

  if (sections.length && 'IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        links.forEach(function (a) {
          a.classList.toggle('is-active', a.getAttribute('href') === '#' + entry.target.id);
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach(function (s) { observer.observe(s); });
  }
})();
