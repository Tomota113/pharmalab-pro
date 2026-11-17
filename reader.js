(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  let course;
  let page = 1;
  let pdfDocument;
  let currentRender;
  let renderGeneration = 0;
  let resizeTimer;
  let zoom = 1;
  const setText = (id, value) => { $(id).textContent = value; };
  const urlForPage = () => `${course.file}#page=${page}`;

  async function renderPage() {
    if (!pdfDocument) return;
    const generation = ++renderGeneration;
    if (currentRender) {
      currentRender.cancel();
      try { await currentRender.promise; } catch { /* Rendu précédent annulé. */ }
      currentRender = null;
    }
    $('canvas-message').hidden = false;
    setText('canvas-message', `Affichage de la page ${page}…`);
    try {
      const pdfPage = await pdfDocument.getPage(page);
      if (generation !== renderGeneration) return;
      const stage = $('canvas-stage');
      const natural = pdfPage.getViewport({scale: 1});
      const availableWidth = Math.max(200, stage.clientWidth - (window.innerWidth <= 700 ? 24 : 48));
      const scale = Math.min(2, availableWidth / natural.width) * zoom;
      const viewport = pdfPage.getViewport({scale});
      const pixelRatio = Math.min(window.devicePixelRatio || 1, 2);
      const canvas = $('pdf-canvas');
      canvas.setAttribute('aria-label', `Page ${page} sur ${pdfDocument.numPages} du cours ${course.title}`);
      const context = canvas.getContext('2d', {alpha: false});
      canvas.width = Math.floor(viewport.width * pixelRatio);
      canvas.height = Math.floor(viewport.height * pixelRatio);
      canvas.style.width = `${Math.floor(viewport.width)}px`;
      canvas.style.height = `${Math.floor(viewport.height)}px`;
      currentRender = pdfPage.render({
        canvasContext: context,
        viewport,
        transform: pixelRatio !== 1 ? [pixelRatio, 0, 0, pixelRatio, 0, 0] : null
      });
      await currentRender.promise;
      if (generation === renderGeneration) $('canvas-message').hidden = true;
    } catch (error) {
      if (generation !== renderGeneration || error?.name === 'RenderingCancelledException') return;
      setText('canvas-message', 'Cette page ne peut pas être affichée ici. Utilise « Ouvrir le PDF » ou « Télécharger ».');
      console.error('PDF page render failed:', error);
    }
  }

  function selectPage(requested) {
    if (!course) return;
    const total = pdfDocument?.numPages || course.pages;
    page = Math.max(1, Math.min(total, Number.parseInt(requested, 10) || 1));
    $('page-input').value = String(page);
    $('prev-page').disabled = page === 1;
    $('next-page').disabled = page === total;
    const pdfUrl = urlForPage();
    $('open-original').href = pdfUrl;
    $('open-original-bottom').href = pdfUrl;
    const closestStep = course.steps.reduce((best, step, index) => step.page <= page ? index : best, 0);
    $('learn-link').href = `apprendre.html?cours=${encodeURIComponent(course.id)}&etape=${closestStep + 1}`;
    $('chapter-list').querySelectorAll('button').forEach((button, index) => {
      const active = index === closestStep;
      button.classList.toggle('active', active);
      button.setAttribute('aria-current', active ? 'location' : 'false');
    });
    const url = new URL(location.href);
    url.searchParams.set('page', String(page));
    history.replaceState(null, '', url);
    setText('pdf-status', `Page ${page} sur ${total} · Document original`);
    renderPage();
  }

  async function init() {
    try {
      const response = await fetch('learning-data.json');
      if (!response.ok) throw new Error(`Catalogue HTTP ${response.status}`);
      const catalog = await response.json();
      const params = new URLSearchParams(location.search);
      course = catalog.find(item => item.id === params.get('cours'));
      if (!course) throw new Error('Cours introuvable');
      document.title = `Lire ${course.title} · PharmaLab`;
      setText('reader-title', course.title);
      setText('reader-meta', `${course.subject} · ${course.teacher} · ${course.pages} pages`);
      setText('reader-hook', course.hook);
      setText('pdf-area-title', course.title);
      setText('page-total', `/ ${course.pages}`);
      setText('chapter-count', `${course.steps.length} repères`);
      $('page-input').max = String(course.pages);
      $('download-original').href = course.file;
      const list = $('chapter-list');
      course.steps.forEach(step => {
        const button = document.createElement('button');
        button.type = 'button';
        const badge = document.createElement('span');
        badge.className = 'page-badge';
        badge.textContent = `p.${step.page}`;
        const name = document.createElement('span');
        name.textContent = step.title;
        button.append(badge, name);
        button.addEventListener('click', () => selectPage(step.page));
        list.append(button);
      });
      selectPage(params.get('page') || 1);
      const pdfjs = await import('./vendor/pdfjs/pdf.mjs?v=15');
      pdfjs.GlobalWorkerOptions.workerSrc = new URL('./vendor/pdfjs/pdf.worker.mjs?v=15', location.href).href;
      pdfDocument = await pdfjs.getDocument({url: course.file}).promise;
      if (pdfDocument.numPages !== course.pages) console.warn('PDF page count differs from catalog:', course.id);
      setText('page-total', `/ ${pdfDocument.numPages}`);
      $('page-input').max = String(pdfDocument.numPages);
      selectPage(page);
    } catch (error) {
      if (!course) {
        setText('reader-title', 'Cours indisponible');
        setText('reader-meta', 'Retourne au portail pour choisir un autre cours.');
      }
      setText('canvas-message', 'Impossible d’afficher le PDF ici. Utilise « Ouvrir le PDF » ou « Télécharger ».');
      setText('pdf-status', 'Visionneuse indisponible');
      console.error('PDF reader unavailable:', error);
    }
  }
  $('prev-page').addEventListener('click', () => selectPage(page - 1));
  $('next-page').addEventListener('click', () => selectPage(page + 1));
  $('page-input').addEventListener('change', event => selectPage(event.target.value));
  function changeZoom(amount) {
    zoom = Math.max(0.75, Math.min(2.5, Math.round((zoom + amount) * 4) / 4));
    setText('zoom-level', `${Math.round(zoom * 100)} %`);
    $('zoom-out').disabled = zoom <= 0.75;
    $('zoom-in').disabled = zoom >= 2.5;
    renderPage();
  }
  $('zoom-out').addEventListener('click', () => changeZoom(-0.25));
  $('zoom-in').addEventListener('click', () => changeZoom(0.25));
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => { if (pdfDocument) renderPage(); }, 120);
  });
  $('reader-outline').open = !window.matchMedia('(max-width: 700px)').matches;
  init();
})();
