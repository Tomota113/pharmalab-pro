(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  let catalog = [];
  let course = null;
  let stepIndex = 0;
  let mode = 'simple';
  let answered = false;
  const stateKey = id => `pharmalab-learning-v1:${id}`;
  const getDone = id => {
    try {
      const value = JSON.parse(localStorage.getItem(stateKey(id)) || '[]');
      const total = catalog.find(item => item.id === id)?.steps.length || 0;
      return Array.isArray(value) ? [...new Set(value.filter(index => Number.isInteger(index) && index >= 0 && index < total))] : [];
    }
    catch { return []; }
  };
  const saveDone = (id, done) => {
    try { localStorage.setItem(stateKey(id), JSON.stringify([...new Set(done)])); }
    catch { /* La lecture reste disponible si le stockage est désactivé. */ }
  };
  function setText(id, value) { $(id).textContent = value; }
  function updateUrl() {
    const url = new URL(location.href);
    url.searchParams.set('cours', course.id);
    url.searchParams.set('etape', String(stepIndex + 1));
    history.replaceState(null, '', url);
  }
  function renderNav() {
    const done = getDone(course.id);
    const nav = $('lesson-nav');
    nav.replaceChildren();
    course.steps.forEach((step, index) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = `${index === stepIndex ? 'active ' : ''}${done.includes(index) ? 'done' : ''}`;
      button.setAttribute('aria-current', index === stepIndex ? 'step' : 'false');
      const number = document.createElement('span');
      number.className = 'number';
      number.textContent = done.includes(index) ? '✓' : String(index + 1).padStart(2, '0');
      const label = document.createElement('span');
      label.textContent = step.title;
      button.append(number, label);
      button.addEventListener('click', () => selectStep(index));
      nav.append(button);
    });
    const percent = Math.round(100 * done.length / course.steps.length);
    setText('progress-label', `${done.length} / ${course.steps.length}`);
    $('progress-fill').style.width = `${percent}%`;
    $('progress-bar').setAttribute('aria-valuenow', String(percent));
    $('course-complete').hidden = done.length !== course.steps.length;
  }
  function renderMap() {
    const map = course.map;
    $('course-map').hidden = !map;
    if (!map) return;
    setText('map-intro', map.intro);
    const nodes = $('map-nodes');
    nodes.replaceChildren();
    function selectNode(index) {
      const node = map.nodes[index];
      nodes.querySelectorAll('button').forEach((button, i) => button.setAttribute('aria-pressed', String(i === index)));
      setText('map-title', node.label);
      setText('map-text', node.text);
      setText('map-source', `Vérifier dans le PDF · page ${node.page} ↗`);
      $('map-source').href = `lire.html?cours=${encodeURIComponent(course.id)}&page=${node.page}`;
    }
    map.nodes.forEach((node, index) => {
      const button = document.createElement('button');
      button.type = 'button';
      const number = document.createElement('span');
      number.textContent = String(index + 1).padStart(2, '0');
      const label = document.createElement('span');
      label.textContent = node.label;
      button.append(number, label);
      button.addEventListener('click', () => selectNode(index));
      nodes.append(button);
    });
    const page = course.steps[stepIndex].page;
    selectNode(map.nodes.reduce((best, node, index) => node.page <= page ? index : best, 0));
  }
  function renderExplanation() {
    const step = course.steps[stepIndex];
    const detailed = mode === 'detail';
    setText('explanation-kicker', detailed ? 'POUR ALLER PLUS LOIN' : 'EN MOTS SIMPLES');
    setText('explanation-icon', detailed ? '🔎' : '💡');
    setText('explanation-text', detailed ? step.detail : step.simple);
    $('mode-simple').setAttribute('aria-selected', String(!detailed));
    $('mode-detail').setAttribute('aria-selected', String(detailed));
    $('mode-simple').tabIndex = detailed ? -1 : 0;
    $('mode-detail').tabIndex = detailed ? 0 : -1;
  }
  function renderQuestion() {
    const step = course.steps[stepIndex];
    setText('quiz-heading', step.question);
    $('answers').replaceChildren();
    setText('quiz-feedback', '');
    $('quiz-feedback').className = 'quiz-feedback';
    answered = false;
    const order = step.choices.map((_, i) => i);
    const rotation = (stepIndex + course.id.length) % order.length;
    order.push(...order.splice(0, rotation));
    order.forEach(originalIndex => {
      const button = document.createElement('button');
      button.type = 'button';
      button.textContent = step.choices[originalIndex];
      button.addEventListener('click', () => {
        if (answered) return;
        if (originalIndex === step.correct) {
          answered = true;
          button.classList.add('correct');
          $('answers').querySelectorAll('button').forEach(b => { b.disabled = true; });
          setText('quiz-feedback', `Bravo ! ${step.feedback}`);
          $('quiz-feedback').className = 'quiz-feedback good';
        } else {
          button.classList.add('wrong');
          button.disabled = true;
          setText('quiz-feedback', 'Pas encore. Relis l’explication, puis essaie une autre réponse.');
          $('quiz-feedback').className = 'quiz-feedback try-again';
        }
      });
      $('answers').append(button);
    });
  }
  function renderStep() {
    const step = course.steps[stepIndex];
    setText('lesson-counter', `ÉTAPE ${String(stepIndex + 1).padStart(2, '0')} / ${String(course.steps.length).padStart(2, '0')}`);
    setText('lesson-title', step.title);
    const words = `${step.simple} ${step.detail} ${step.example}`.split(/\s+/).length;
    setText('lesson-time', `Lecture · ${Math.max(1, Math.ceil(words / 180))} min`);
    setText('example-text', step.example);
    setText('page-source', `📄 Voir la page ${step.page} du cours original`);
    $('page-source').href = `lire.html?cours=${encodeURIComponent(course.id)}&page=${step.page}`;
    $('prev-step').disabled = stepIndex === 0;
    setText('complete-step', stepIndex === course.steps.length - 1 ? 'J’ai compris · Terminer ✓' : 'J’ai compris · Étape suivante →');
    mode = 'simple';
    renderExplanation();
    renderQuestion();
    renderNav();
    renderMap();
    updateUrl();
  }
  function selectStep(index) {
    stepIndex = Math.max(0, Math.min(index, course.steps.length - 1));
    renderStep();
    if (window.scrollY > 500) {
      $('lesson-panel').focus({preventScroll:true});
      $('lesson-panel').scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth', block:'start'});
    }
  }
  function renderCourse() {
    setText('subject-pill', course.subject);
    setText('page-count', `${course.pages} pages`);
    setText('course-title', course.title);
    document.title = `${course.title} · Apprendre · PharmaLab`;
    setText('course-hook', course.hook);
    setText('course-teacher', `PDF source · ${course.teacher}`);
    $('source-download').href = course.file;
    $('source-open').href = `lire.html?cours=${encodeURIComponent(course.id)}`;
    const objectives = $('objectives-list');
    objectives.replaceChildren();
    course.objectives.forEach(item => {
      const li = document.createElement('li');
      li.textContent = item;
      objectives.append(li);
    });
    $('loading').hidden = true;
    $('lesson-content').hidden = false;
    renderStep();
  }
  function selectCourse(id, step) {
    course = catalog.find(item => item.id === id) || catalog[0];
    if (!course) return;
    const done = getDone(course.id);
    const next = course.steps.findIndex((_, index) => !done.includes(index));
    stepIndex = Math.max(0, Math.min(step ?? (next < 0 ? 0 : next), course.steps.length - 1));
    $('course-select').value = course.id;
    renderCourse();
  }
  async function init() {
    try {
      const response = await fetch('learning-data.json');
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      catalog = await response.json();
      if (!Array.isArray(catalog) || !catalog.length) throw new Error('Catalogue vide');
      catalog.forEach(item => {
        const option = document.createElement('option');
        option.value = item.id;
        option.textContent = `${item.subject} · ${item.title}`;
        $('course-select').append(option);
      });
      const params = new URLSearchParams(location.search);
      const requestedStep = Number.parseInt(params.get('etape'), 10) - 1;
      selectCourse(params.get('cours'), Number.isFinite(requestedStep) ? requestedStep : undefined);
    } catch (error) {
      $('loading').textContent = 'Impossible de charger les parcours. Actualise la page ou ouvre le portail des cours.';
      console.error('Learning catalog unavailable:', error);
    }
  }
  $('course-select').addEventListener('change', event => selectCourse(event.target.value));
  $('reset-progress').addEventListener('click', () => {
    if (!course) return;
    saveDone(course.id, []);
    selectStep(0);
  });
  $('mode-simple').addEventListener('click', () => { mode = 'simple'; renderExplanation(); });
  $('mode-detail').addEventListener('click', () => { mode = 'detail'; renderExplanation(); });
  const modeButtons = [$('mode-simple'), $('mode-detail')];
  modeButtons.forEach(button => button.addEventListener('keydown', event => {
    if (!['ArrowLeft', 'ArrowRight', 'Home', 'End'].includes(event.key)) return;
    event.preventDefault();
    const index = event.key === 'Home' ? 0 : event.key === 'End' ? 1 : 1 - modeButtons.indexOf(button);
    modeButtons[index].focus();
    modeButtons[index].click();
  }));
  $('prev-step').addEventListener('click', () => selectStep(stepIndex - 1));
  $('complete-step').addEventListener('click', () => {
    if (!course) return;
    const done = getDone(course.id);
    done.push(stepIndex);
    saveDone(course.id, done);
    if (stepIndex < course.steps.length - 1) selectStep(stepIndex + 1);
    else {
      renderNav();
      setText('complete-step', getDone(course.id).length === course.steps.length ? 'Cours parcouru ✓' : 'Étape marquée comme parcourue ✓');
    }
  });
  $('lesson-outline').open = !window.matchMedia('(max-width: 900px)').matches;
  $('course-map').open = !window.matchMedia('(max-width: 900px)').matches;
  init();
})();
