/* ============================================================
   AKEMI HAIR GLOW — script.js
   Hero interactions: counter animation, CTA ripple, nav scroll
   ============================================================ */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    initAnimatedCounters();
    initCTARipple();
    initNavScroll();
  });

  /* ── Animate rating number and review count on view ─────── */
  function initAnimatedCounters() {
    var items = [
      { selector: '#hero-rc-score', end: 4.8,  decimals: 1 },
      { selector: '#hero-rc-count', end: 3758, decimals: 0, format: true }
    ];

    if (!('IntersectionObserver' in window)) return;

    items.forEach(function (item) {
      var el = document.querySelector(item.selector);
      if (!el) return;

      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          animateNumber(el, item.end, item.decimals, item.format || false);
          observer.unobserve(entry.target);
        });
      }, { threshold: 0.6 });

      observer.observe(el);
    });
  }

  function animateNumber(el, end, decimals, useLocale) {
    var duration  = 1600;
    var startTime = null;

    function tick(ts) {
      if (!startTime) startTime = ts;
      var p = Math.min((ts - startTime) / duration, 1);
      var v = easeOutExpo(p) * end;

      if (decimals > 0) {
        el.textContent = v.toFixed(decimals);
      } else {
        el.textContent = useLocale
          ? Math.floor(v).toLocaleString()
          : Math.floor(v).toString();
      }

      if (p < 1) {
        requestAnimationFrame(tick);
      } else {
        el.textContent = decimals > 0
          ? end.toFixed(decimals)
          : (useLocale ? end.toLocaleString() : end.toString());
      }
    }

    requestAnimationFrame(tick);
  }

  function easeOutExpo(t) {
    return t >= 1 ? 1 : 1 - Math.pow(2, -10 * t);
  }

  /* ── CTA ripple effect ──────────────────────────────────── */
  function initCTARipple() {
    var cta = document.getElementById('hero-cta');
    if (!cta) return;

    // Inject keyframe once
    if (!document.getElementById('akemi-ripple-style')) {
      var s = document.createElement('style');
      s.id = 'akemi-ripple-style';
      s.textContent = '@keyframes akemi-ripple{to{transform:scale(30);opacity:0}}';
      document.head.appendChild(s);
    }

    cta.addEventListener('click', function (e) {
      var rect   = cta.getBoundingClientRect();
      var ripple = document.createElement('span');
      var size   = 10;

      Object.assign(ripple.style, {
        position:      'absolute',
        borderRadius:  '50%',
        width:         size + 'px',
        height:        size + 'px',
        left:          (e.clientX - rect.left - size / 2) + 'px',
        top:           (e.clientY - rect.top  - size / 2) + 'px',
        background:    'rgba(255,255,255,0.3)',
        pointerEvents: 'none',
        animation:     'akemi-ripple 0.6s ease forwards'
      });

      cta.appendChild(ripple);
      setTimeout(function () { ripple.remove(); }, 650);
    });
  }

  /* ── Subtle nav shrink on scroll ────────────────────────── */
  function initNavScroll() {
    var nav = document.getElementById('nav');
    if (!nav) return;

    window.addEventListener('scroll', function () {
      if (window.scrollY > 20) {
        nav.style.background  = 'rgba(249,245,240,0.92)';
        nav.style.backdropFilter = 'blur(10px)';
        nav.style.boxShadow   = '0 1px 16px rgba(27,47,42,0.08)';
        nav.style.transition  = 'all 0.3s ease';
      } else {
        nav.style.background  = '';
        nav.style.backdropFilter = '';
        nav.style.boxShadow   = '';
      }
    }, { passive: true });
  }

})();
