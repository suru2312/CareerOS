/**
 * CareerOS — Sidebar JS
 * Handles: desktop collapse, mobile open/close, active link, persist state
 */

(function () {
  'use strict';

  const sidebar      = document.getElementById('sidebar');
  const mainWrapper  = document.getElementById('mainWrapper');
  const overlay      = document.getElementById('sidebarOverlay');
  const toggleBtns   = document.querySelectorAll('.sidebar-toggle');

  if (!sidebar) return;

  const COLLAPSED_KEY = 'cos_sidebar_collapsed';

  // ── Restore persisted state (desktop) ──────────────────────────

  function isDesktop() { return window.innerWidth > 768; }

  function applyCollapsed(collapsed) {
    if (collapsed && isDesktop()) {
      sidebar.classList.add('collapsed');
      mainWrapper && mainWrapper.classList.add('sidebar-collapsed');
    } else {
      sidebar.classList.remove('collapsed');
      mainWrapper && mainWrapper.classList.remove('sidebar-collapsed');
    }
  }

  if (isDesktop()) {
    const stored = localStorage.getItem(COLLAPSED_KEY);
    applyCollapsed(stored === 'true');
  }

  // ── Desktop collapse toggle ─────────────────────────────────────

  toggleBtns.forEach(btn => {
    btn.addEventListener('click', function () {
      if (!isDesktop()) {
        // Mobile: slide in/out
        toggleMobile();
        return;
      }

      const isNowCollapsed = !sidebar.classList.contains('collapsed');
      applyCollapsed(isNowCollapsed);
      localStorage.setItem(COLLAPSED_KEY, isNowCollapsed);
    });
  });

  // ── Mobile open/close ──────────────────────────────────────────

  function toggleMobile() {
    const open = sidebar.classList.toggle('mobile-open');
    overlay && overlay.classList.toggle('visible', open);
    document.body.style.overflow = open ? 'hidden' : '';
  }

  overlay && overlay.addEventListener('click', () => {
    sidebar.classList.remove('mobile-open');
    overlay.classList.remove('visible');
    document.body.style.overflow = '';
  });

  // Close sidebar on ESC
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && sidebar.classList.contains('mobile-open')) {
      sidebar.classList.remove('mobile-open');
      overlay && overlay.classList.remove('visible');
      document.body.style.overflow = '';
    }
  });

  // ── Active link ────────────────────────────────────────────────

  const currentPath = window.location.pathname;
  const navLinks = sidebar.querySelectorAll('.sidebar-item[href]');

  navLinks.forEach(link => {
    // Exact match or prefix match (for sub-pages)
    const href = link.getAttribute('href');
    if (href && href !== '/' && currentPath.startsWith(href)) {
      link.classList.add('active');
    } else if (href === '/' && currentPath === '/') {
      link.classList.add('active');
    }
  });

  // ── Resize handler ─────────────────────────────────────────────

  let resizeTimer;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
      if (isDesktop()) {
        // Remove mobile-open state when switching to desktop
        sidebar.classList.remove('mobile-open');
        overlay && overlay.classList.remove('visible');
        document.body.style.overflow = '';

        // Reapply desktop collapsed state
        const stored = localStorage.getItem(COLLAPSED_KEY);
        applyCollapsed(stored === 'true');
      } else {
        // On mobile, always remove desktop collapsed
        sidebar.classList.remove('collapsed');
        mainWrapper && mainWrapper.classList.remove('sidebar-collapsed');
      }
    }, 150);
  });

})();