/**
 * CareerOS — Main JS
 * Handles: toast auto-dismiss, confirm dialogs, misc UI
 */

(function () {
  'use strict';

  // ── Auto-dismiss toast messages ──────────────────────────────────

  function initToasts() {
    const toasts = document.querySelectorAll('.toast-msg');
    toasts.forEach(function (toast, i) {
      setTimeout(function () {
        toast.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(20px)';
        setTimeout(function () { toast.remove(); }, 400);
      }, 3500 + i * 300);
    });
  }

  // ── Delete confirmation dialogs ──────────────────────────────────

  function initDeleteConfirm() {
    document.querySelectorAll('[data-confirm]').forEach(function (el) {
      el.addEventListener('click', function (e) {
        const msg = el.getAttribute('data-confirm') || 'Are you sure you want to delete this?';
        if (!window.confirm(msg)) {
          e.preventDefault();
          e.stopPropagation();
        }
      });
    });
  }

  // ── Progress bar animation ───────────────────────────────────────

  function initProgressBars() {
    const bars = document.querySelectorAll('.progress-bar[data-value]');
    bars.forEach(function (bar) {
      const value = parseInt(bar.getAttribute('data-value'), 10) || 0;
      setTimeout(function () {
        bar.style.width = Math.min(Math.max(value, 0), 100) + '%';
      }, 100);
    });
  }

  // ── Topbar page title from sidebar active link ───────────────────

  function initPageTitle() {
    const titleEl = document.querySelector('.topbar-page-title');
    if (!titleEl) return;
    const active = document.querySelector('#sidebar .sidebar-item.active .sidebar-item-label');
    if (active) titleEl.textContent = active.textContent.trim();
  }

  // ── Init ─────────────────────────────────────────────────────────

  document.addEventListener('DOMContentLoaded', function () {
    initToasts();
    initDeleteConfirm();
    initProgressBars();
    initPageTitle();
  });

})();