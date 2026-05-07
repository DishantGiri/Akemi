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
    initFAQ();
    initNavToggle();
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
      if (window.scrollY > 10) {
        nav.classList.add('is-scrolled');
      } else {
        nav.classList.remove('is-scrolled');
      }
    }, { passive: true });
  }

  /* ── FAQ Accordion ─────────────────────────────────── */
  function initFAQ() {
    var faqQuestions = document.querySelectorAll(".faq__question");
    if (!faqQuestions.length) return;

    faqQuestions.forEach(function (question) {
      question.addEventListener("click", function () {
        var item = question.parentElement;
        var isActive = item.classList.contains("active");

        // Close all other items
        document.querySelectorAll(".faq__item").forEach(function (otherItem) {
          otherItem.classList.remove("active");
        });

        // Toggle current item
        if (!isActive) {
          item.classList.add("active");
        }
      });
    });
  }

  /* ── Mobile Nav Toggle ─────────────────────────────── */
  function initNavToggle() {
    var toggle = document.getElementById('nav-toggle');
    var menu   = document.getElementById('nav-menu');
    var links  = document.querySelectorAll('.nav__link');

    if (!toggle || !menu) return;

    toggle.addEventListener('click', function () {
      toggle.classList.toggle('is-active');
      menu.classList.toggle('is-active');
      document.body.classList.toggle('no-scroll');
    });

    links.forEach(function (link) {
      link.addEventListener('click', function () {
        toggle.classList.remove('is-active');
        menu.classList.remove('is-active');
        document.body.classList.remove('no-scroll');
      });
    });
  }

})();
