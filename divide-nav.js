'use strict';
const sectionNav = document.querySelector('.divide-index');
if (sectionNav) {
  const disclosure = sectionNav.querySelector('details');
  const summary = sectionNav.querySelector('summary');
  const links = [...sectionNav.querySelectorAll('a[href^="#"]')];
  const sections = links.map(link => document.querySelector(link.hash));
  const compact = matchMedia('(max-width: 1000px)');
  const fitNavigation = () => { disclosure.open = !compact.matches; };
  fitNavigation();
  compact.addEventListener('change', fitNavigation);
  links.forEach(link => link.addEventListener('click', () => {
    if (compact.matches) disclosure.open = false;
  }));
  sectionNav.addEventListener('keydown', event => {
    if (event.key === 'Escape' && compact.matches && disclosure.open) {
      disclosure.open = false;
      summary.focus();
    }
  });
  let pending = false;
  const markSection = () => {
    const threshold = sectionNav.getBoundingClientRect().height + 110;
    let current = 0;
    sections.forEach((section, index) => {
      if (section.getBoundingClientRect().top <= threshold) current = index;
    });
    links.forEach((link, index) => {
      if (index === current) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    pending = false;
  };
  const scheduleMark = () => {
    if (!pending) { pending = true; requestAnimationFrame(markSection); }
  };
  addEventListener('scroll', scheduleMark, { passive: true });
  addEventListener('resize', scheduleMark);
  markSection();
}
