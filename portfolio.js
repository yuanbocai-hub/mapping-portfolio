'use strict';

// Each group remains fully readable when JavaScript is unavailable.
document.querySelectorAll('[data-switcher]').forEach(group => {
  const buttons = [...group.querySelectorAll('[data-view]')];
  const panels = [...group.querySelectorAll('[data-panel]')];
  function select(value) {
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.view === value)));
    panels.forEach(panel => { panel.hidden = panel.dataset.panel !== value; });
  }
  buttons.forEach(button => button.addEventListener('click', () => select(button.dataset.view)));
  select(buttons[0].dataset.view);
});

const dialog = document.querySelector('#image-dialog');
const image = document.querySelector('#lightbox-image');
const caption = document.querySelector('#image-caption');
const original = document.querySelector('#image-original');
const stage = document.querySelector('.lightbox-stage');
let lastTrigger;
document.querySelectorAll('[data-lightbox]').forEach(link => {
  link.addEventListener('click', event => {
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || !dialog.showModal) return;
    event.preventDefault();
    lastTrigger = link;
    caption.textContent = link.dataset.caption;
    image.alt = link.querySelector('img').alt;
    image.src = document.body.hasAttribute('data-preview-mode') ? link.querySelector('img').src : link.href;
    original.href = link.href;
    stage.classList.remove('zoomed');
    dialog.showModal();
    document.querySelector('#close-image').focus();
  });
});
document.querySelector('#close-image').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
dialog.addEventListener('close', () => { image.removeAttribute('src'); if (lastTrigger) lastTrigger.focus(); });
image.addEventListener('click', () => stage.classList.toggle('zoomed'));

if ('IntersectionObserver' in window) {
  const links = [...document.querySelectorAll('.chapter-nav a')];
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      links.forEach(link => {
        if (link.hash === '#' + entry.target.id) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    });
  }, { rootMargin: '-10% 0px -55% 0px' });
  links.forEach(link => observer.observe(document.querySelector(link.hash)));
}
