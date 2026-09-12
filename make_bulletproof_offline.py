#!/usr/bin/env python3
"""
Make PharmaLab Pro 100% bulletproof for iOS, Android, Safari, Chrome, and offline Files preview.
Embeds compiled Tailwind CSS directly, adds safety guards around external libraries (Lucide, Chart.js, 3Dmol),
provides native Canvas 2D fallback for the PK chart, and ensures tab switching works even in sandboxed QuickLook.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(BASE_DIR, 'index.html')
TEMPLATE_FILE = os.path.join(BASE_DIR, 'template_pro.html')
COMPILED_CSS_FILE = '/tmp/tailwind_compiled.css'

with open(COMPILED_CSS_FILE, 'r', encoding='utf-8') as f:
    compiled_css = f.read()

with open(INDEX_FILE, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace Tailwind CDN and tailwind.config with embedded pure compiled CSS
css_block = f"""
  <!-- STANDALONE EMBEDDED PURE CSS (Zero dependency, Works 100% Offline & iOS QuickLook) -->
  <style>
    /* Emergency Base Styles */
    html, body {{
      background-color: #020617 !important;
      color: #f8fafc !important;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }}
    .hidden {{
      display: none !important;
    }}
    
    /* Compiled Tailwind CSS */
    {compiled_css}

    /* Custom Scrollbar & Container Overrides */
    ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
    ::-webkit-scrollbar-track {{ background: #020617; }}
    ::-webkit-scrollbar-thumb {{ background: #334155; border-radius: 9999px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #475569; }}

    #g3d-container {{
      width: 100%;
      height: 380px;
      position: relative;
    }}

    /* iOS QuickLook Safe Navigation */
    @media (max-width: 768px) {{
      .master-tab-btn {{
        font-size: 11px;
        padding: 6px 10px;
      }}
    }}
  </style>
"""

# Remove old CDN script and tailwind.config
html = re.sub(r'<script src="https://cdn\.tailwindcss\.com"></script>', '', html)
html = re.sub(r'<script>\s*tailwind\.config\s*=\s*\{.*?\};\s*</script>', '', html, flags=re.DOTALL)

# Insert the embedded CSS block right before </head>
html = html.replace('</head>', f'{css_block}\n</head>', 1)

# 2. Add Safe Lucide Icon creation function
safe_lucide_def = """
    // Safe Lucide Icons (no crash if offline/blocked)
    function safeCreateIcons() {
      if (typeof lucide !== 'undefined' && lucide && typeof lucide.createIcons === 'function') {
        try { lucide.createIcons(); } catch(e) { console.warn("Lucide:", e); }
      }
    }
"""

# Replace all lucide.createIcons(); with safeCreateIcons();
html = html.replace('lucide.createIcons();', 'safeCreateIcons();')

# Inject safe_lucide_def right after <script> in body
html = re.sub(r'(<script>\s*// Embedded Databases)', r'<script>\n' + safe_lucide_def + r'\n    // Embedded Databases', html, count=1)

# 3. Robust Native Canvas PK Chart fallback (if Chart.js is blocked)
native_pk_code = """
    function drawNativePkChart(canvas, timePoints, concentrations, cmt, cme) {
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      const w = canvas.width || 600;
      const h = canvas.height || 280;

      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#020617';
      ctx.fillRect(0, 0, w, h);

      const padL = 45, padR = 20, padT = 25, padB = 35;
      const pw = w - padL - padR;
      const ph = h - padT - padB;

      const maxC = Math.max(cmt * 1.3, ...concentrations, 20);
      const maxT = timePoints[timePoints.length - 1] || 24;

      function xPos(t) { return padL + (t / maxT) * pw; }
      function yPos(c) { return padT + (1.0 - Math.min(1.0, c / maxC)) * ph; }

      // Grid & Axes
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 1;
      for (let i = 0; i <= 4; i++) {
        const cVal = (maxC * (i / 4)).toFixed(1);
        const y = yPos(cVal);
        ctx.beginPath();
        ctx.moveTo(padL, y);
        ctx.lineTo(w - padR, y);
        ctx.stroke();
        ctx.fillStyle = '#64748b';
        ctx.font = '10px monospace';
        ctx.fillText(cVal, 8, y + 3);
      }

      // Time ticks
      for (let t = 0; t <= maxT; t += (maxT <= 24 ? 4 : 8)) {
        const x = xPos(t);
        ctx.beginPath();
        ctx.moveTo(x, padT);
        ctx.lineTo(x, h - padB);
        ctx.stroke();
        ctx.fillStyle = '#64748b';
        ctx.font = '10px monospace';
        ctx.fillText(t + 'h', x - 6, h - padB + 14);
      }

      // CME Line (green)
      ctx.strokeStyle = '#10b981';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(padL, yPos(cme));
      ctx.lineTo(w - padR, yPos(cme));
      ctx.stroke();
      ctx.fillStyle = '#10b981';
      ctx.fillText('Seuil Efficace (CME)', padL + 10, yPos(cme) - 5);

      // CMT Line (red)
      ctx.strokeStyle = '#f43f5e';
      ctx.setLineDash([6, 6]);
      ctx.beginPath();
      ctx.moveTo(padL, yPos(cmt));
      ctx.lineTo(w - padR, yPos(cmt));
      ctx.stroke();
      ctx.fillStyle = '#f43f5e';
      ctx.fillText('Seuil Toxique (CMT)', padL + 10, yPos(cmt) - 5);
      ctx.setLineDash([]);

      // C(t) Curve (teal)
      ctx.strokeStyle = '#14b8a6';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i < timePoints.length; i++) {
        const x = xPos(timePoints[i]);
        const y = yPos(concentrations[i]);
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Fill under curve
      ctx.lineTo(xPos(timePoints[timePoints.length - 1]), h - padB);
      ctx.lineTo(padL, h - padB);
      ctx.closePath();
      ctx.fillStyle = 'rgba(20, 184, 166, 0.15)';
      ctx.fill();
    }
"""

html = html.replace('function updatePkFromSliders() {', native_pk_code + '\n    function updatePkFromSliders() {')

# 4. Update initPkChart & updatePkFromSliders to use native Canvas fallback
old_init_pk = """    function initPkChart() {
      const ctx = document.getElementById('pkCanvas').getContext('2d');
      pkChart = new Chart(ctx, {"""

new_init_pk = """    function initPkChart() {
      const canvas = document.getElementById('pkCanvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      if (typeof Chart !== 'undefined') {
        try {
          pkChart = new Chart(ctx, {"""

html = html.replace(old_init_pk, new_init_pk)

# Close the try catch for new Chart
old_chart_end = """          plugins: {
            legend: { labels: { color: '#cbd5e1', font: { family: '"Plus Jakarta Sans"' } } }
          }
        }
      });
    }"""

new_chart_end = """          plugins: {
            legend: { labels: { color: '#cbd5e1', font: { family: '"Plus Jakarta Sans"' } } }
          }
        }
      });
        } catch(e) {
          console.warn("Chart.js error:", e);
          pkChart = null;
        }
      } else {
        pkChart = null;
      }
    }"""

html = html.replace(old_chart_end, new_chart_end)

# In updatePkFromSliders, call drawNativePkChart if pkChart is null
old_pk_update = """      pkChart.data.labels = timePoints;
      pkChart.data.datasets[0].data = concentrations;
      pkChart.data.datasets[1].data = timePoints.map(() => cmt);
      pkChart.data.datasets[2].data = timePoints.map(() => cme);
      pkChart.update('none');"""

new_pk_update = """      if (pkChart) {
        pkChart.data.labels = timePoints;
        pkChart.data.datasets[0].data = concentrations;
        pkChart.data.datasets[1].data = timePoints.map(() => cmt);
        pkChart.data.datasets[2].data = timePoints.map(() => cme);
        pkChart.update('none');
      } else {
        const cvs = document.getElementById('pkCanvas');
        drawNativePkChart(cvs, timePoints, concentrations, cmt, cme);
      }"""

html = html.replace(old_pk_update, new_pk_update)

# 5. Safe 3D Viewer Init
old_3d_init = """    function init3DViewer() {
      const el = document.getElementById('g3d-container');
      if (!el) return;
      viewer3D = $3Dmol.createViewer(el, { backgroundColor: '#020617' });
      select3DMol('paracetamol');
    }"""

new_3d_init = """    function init3DViewer() {
      const el = document.getElementById('g3d-container');
      if (!el) return;
      if (typeof $3Dmol !== 'undefined') {
        try {
          viewer3D = $3Dmol.createViewer(el, { backgroundColor: '#020617' });
          select3DMol('paracetamol');
        } catch(e) {
          console.warn("3D viewer:", e);
        }
      } else {
        el.innerHTML = '<div class="h-full flex flex-col items-center justify-center p-6 text-center text-slate-400 text-xs space-y-2"><div class="w-12 h-12 rounded-2xl bg-teal-500/20 text-teal-300 border border-teal-500/40 flex items-center justify-center font-bold text-lg">3D</div><p class="font-bold text-slate-200">Studio 3D Moléculaire (WebGL)</p><p>Pour manipuler les structures 3D interactives, ouvrez ce fichier dans Safari ou Chrome.</p></div>';
      }
    }"""

html = html.replace(old_3d_init, new_3d_init)

# 6. Make switchMasterTab ultra-resilient with inline style.display
old_switch_tab = """        if (t === tabId) {
          sec.classList.remove('hidden');
          if (btn) btn.className = 'master-tab-btn active px-3.5 py-2 rounded-xl transition-all flex items-center space-x-2 bg-teal-600 text-white shadow-md font-bold';
          if (mob) mob.className = 'flex-1 py-1.5 px-2.5 rounded-lg font-bold bg-teal-600 text-white whitespace-nowrap text-center';
        } else {
          sec.classList.add('hidden');
          if (btn) btn.className = 'master-tab-btn px-3.5 py-2 rounded-xl transition-all flex items-center space-x-2 text-slate-300 hover:text-white hover:bg-slate-700/60 font-semibold';
          if (mob) mob.className = 'flex-1 py-1.5 px-2.5 rounded-lg font-medium text-slate-300 whitespace-nowrap text-center';
        }"""

new_switch_tab = """        if (t === tabId) {
          sec.classList.remove('hidden');
          sec.style.display = 'block';
          if (btn) btn.className = 'master-tab-btn active px-3.5 py-2 rounded-xl transition-all flex items-center space-x-2 bg-teal-600 text-white shadow-md font-bold';
          if (mob) mob.className = 'flex-1 py-1.5 px-2.5 rounded-lg font-bold bg-teal-600 text-white whitespace-nowrap text-center';
        } else {
          sec.classList.add('hidden');
          sec.style.display = 'none';
          if (btn) btn.className = 'master-tab-btn px-3.5 py-2 rounded-xl transition-all flex items-center space-x-2 text-slate-300 hover:text-white hover:bg-slate-700/60 font-semibold';
          if (mob) mob.className = 'flex-1 py-1.5 px-2.5 rounded-lg font-medium text-slate-300 whitespace-nowrap text-center';
        }"""

html = html.replace(old_switch_tab, new_switch_tab)

# 7. Safe DOMContentLoaded with try/catch on every single step
old_dom_init = """    // Initialization
    document.addEventListener('DOMContentLoaded', () => {
      safeCreateIcons();
      renderEncyclopedia(MOLECULES);
      init3DViewer();
      initPkChart();
      loadPkPreset('paracetamol');
      loadClinicalCase(1);
      runOpioidRotation();
      renderSrsCard();
      loadEcosScenario(1);
      updateRumackPlot();
      setCYP2D6Phenotype('EM');
      populateAudioSelector();
      populatePocketTable();
      renderSrsCard();
      loadEcosScenario(1);
      updateRumackPlot();
      setCYP2D6Phenotype('EM');
      populateAudioSelector();
      populatePocketTable();
    });"""

new_dom_init = """    // Initialization with Safe Guards
    document.addEventListener('DOMContentLoaded', () => {
      const safeRun = (fn) => { try { fn(); } catch(e) { console.warn("Init error:", e); } };

      safeRun(() => safeCreateIcons());
      safeRun(() => renderEncyclopedia(MOLECULES));
      safeRun(() => init3DViewer());
      safeRun(() => initPkChart());
      safeRun(() => loadPkPreset('paracetamol'));
      safeRun(() => loadClinicalCase(1));
      safeRun(() => runOpioidRotation());
      safeRun(() => renderSrsCard());
      safeRun(() => loadEcosScenario(1));
      safeRun(() => updateRumackPlot());
      safeRun(() => setCYP2D6Phenotype('EM'));
      safeRun(() => populateAudioSelector());
      safeRun(() => populatePocketTable());
      safeRun(() => switchMasterTab('encyclopedia'));
    });"""

html = html.replace(old_dom_init, new_dom_init)

# Write to both index.html and template_pro.html
with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

with open(TEMPLATE_FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print("Both index.html and template_pro.html made 100% bulletproof and offline ready!")
print(f"File size: {os.path.getsize(INDEX_FILE)} bytes")
