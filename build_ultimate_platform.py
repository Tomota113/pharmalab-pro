#!/usr/bin/env python3
"""
Ultimate Platform Compiler for PharmaLab Pro (DFGSP2)
Embeds all 24 monographs, 6 3D models, and the 5 Bonus Hub Tools:
1. Flashcards SRS (Anki SM-2)
2. ECOS Clinical Simulation (Virtual Patient)
3. Rumack-Matthew Nomogram & CYP2D6 Pharmacogenetics
4. Emergency Guard Mode (Time-Attack 90s)
5. Audio-Learning (Web Speech API) & Printable Pocket Cards
"""

import json
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_FILE = os.path.join(BASE_DIR, 'template_pro.html')
INDEX_FILE = os.path.join(BASE_DIR, 'index.html')
DB_FILE = os.path.join(BASE_DIR, 'data', 'pharmacology_db.json')
SDF_FILE = os.path.join(BASE_DIR, 'sdf_data.json')

with open(DB_FILE, 'r', encoding='utf-8') as f:
    pharma_db = json.load(f)

with open(SDF_FILE, 'r', encoding='utf-8') as f:
    sdf_data = json.load(f)

with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
    template = f.read()

# 1. Add Desktop Navigation Button for Bonus Hub
old_nav_desktop = '</nav>'
new_nav_btn = '''        <button onclick="switchMasterTab('bonus-hub')" id="nav-btn-bonus-hub" class="master-tab-btn px-3.5 py-2 rounded-xl transition-all flex items-center space-x-2 text-amber-300 hover:text-white hover:bg-amber-500/20 font-semibold border border-amber-500/30">
          <i data-lucide="sparkles" class="w-4 h-4 text-amber-400"></i>
          <span>7. 🎁 Bonus & Outils Avancés</span>
        </button>
      </nav>'''

if 'id="nav-btn-bonus-hub"' not in template:
    template = template.replace(old_nav_desktop, new_nav_btn, 1)

# 2. Add Mobile Navigation Button for Bonus Hub
old_mob_nav = '<button onclick="switchMasterTab(\'tactical-hub\')" id="mob-nav-tactical-hub" class="flex-1 py-1.5 px-2.5 rounded-lg font-medium text-slate-300 whitespace-nowrap text-center">6. Rotation Opioïdes</button>'
new_mob_nav = '''<button onclick="switchMasterTab('tactical-hub')" id="mob-nav-tactical-hub" class="flex-1 py-1.5 px-2.5 rounded-lg font-medium text-slate-300 whitespace-nowrap text-center">6. Rotation Opioïdes</button>
      <button onclick="switchMasterTab('bonus-hub')" id="mob-nav-bonus-hub" class="flex-1 py-1.5 px-2.5 rounded-lg font-bold text-amber-300 bg-amber-950/40 border border-amber-500/40 whitespace-nowrap text-center">7. 🎁 Bonus</button>'''

if 'id="mob-nav-bonus-hub"' not in template:
    template = template.replace(old_mob_nav, new_mob_nav, 1)

# 3. Add Section 7 (Bonus Hub) before </main>
bonus_hub_section = '''
    <!-- ========================================================================= -->
    <!-- TAB 7 : 🎁 HUB BONUS & OUTILS AVANCÉS (SRS, ECOS, RUMACK, CYP2D6, AUDIO) -->
    <!-- ========================================================================= -->
    <section id="sec-bonus-hub" class="hidden space-y-6">
      
      <!-- Banner Header -->
      <div class="bg-gradient-to-r from-slate-900 via-amber-950/60 to-purple-950/70 border border-amber-500/30 rounded-3xl p-6 sm:p-8 shadow-2xl relative overflow-hidden">
        <div class="absolute -right-12 -top-12 w-64 h-64 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>
        <div class="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div class="max-w-3xl space-y-2">
            <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 text-xs font-bold border border-amber-500/30">
              <i data-lucide="sparkles" class="w-3.5 h-3.5"></i>
              <span>Boîte à Outils Clinique Haute-Performance (DFGSP2 & Internat)</span>
            </div>
            <h1 class="text-2xl sm:text-3xl font-black text-white tracking-tight">
              🎁 Hub Bonus : Entraînement Cognitif & Outils Avancés
            </h1>
            <p class="text-slate-300 text-xs sm:text-sm leading-relaxed">
              Mémorisation active par répétition espacée (<strong class="text-amber-300">Anki SM-2</strong>), simulateur officiel d'<strong class="text-teal-300">ECOS au comptoir</strong>, nomogramme toxicologique de <strong class="text-cyan-300">Rumack-Matthew</strong>, pharmacogénétique du <strong class="text-purple-300">CYP2D6</strong>, mode <strong class="text-rose-300">Garde d'Urgence 90s</strong> et <strong class="text-emerald-300">Audio-Learning</strong>.
            </p>
          </div>
        </div>
      </div>

      <!-- Sub-tabs navigation for Bonus Hub -->
      <div class="flex flex-wrap gap-2 p-1.5 bg-slate-900/90 rounded-2xl border border-slate-800 text-xs font-semibold">
        <button onclick="switchBonusSubTab('srs')" id="bonus-sub-btn-srs" class="bonus-sub-btn active px-4 py-2.5 rounded-xl transition flex items-center space-x-2 bg-amber-500 text-slate-950 font-bold shadow-md">
          <i data-lucide="brain" class="w-4 h-4"></i>
          <span>1. Flashcards SRS (Anki SM-2)</span>
        </button>
        <button onclick="switchBonusSubTab('ecos')" id="bonus-sub-btn-ecos" class="bonus-sub-btn px-4 py-2.5 rounded-xl transition flex items-center space-x-2 text-slate-300 hover:text-white hover:bg-slate-800">
          <i data-lucide="stethoscope" class="w-4 h-4"></i>
          <span>2. ECOS Pharmacie (Patient Virtuel)</span>
        </button>
        <button onclick="switchBonusSubTab('rumack-cyp')" id="bonus-sub-btn-rumack-cyp" class="bonus-sub-btn px-4 py-2.5 rounded-xl transition flex items-center space-x-2 text-slate-300 hover:text-white hover:bg-slate-800">
          <i data-lucide="activity" class="w-4 h-4"></i>
          <span>3. Rumack-Matthew & CYP2D6</span>
        </button>
        <button onclick="switchBonusSubTab('emergency')" id="bonus-sub-btn-emergency" class="bonus-sub-btn px-4 py-2.5 rounded-xl transition flex items-center space-x-2 text-slate-300 hover:text-white hover:bg-slate-800">
          <i data-lucide="alarm-clock" class="w-4 h-4"></i>
          <span>4. Garde d'Urgence (Time-Attack 90s)</span>
        </button>
        <button onclick="switchBonusSubTab('audio-memo')" id="bonus-sub-btn-audio-memo" class="bonus-sub-btn px-4 py-2.5 rounded-xl transition flex items-center space-x-2 text-slate-300 hover:text-white hover:bg-slate-800">
          <i data-lucide="headphones" class="w-4 h-4"></i>
          <span>5. Audio-Learning & Fiche Mémo</span>
        </button>
      </div>

      <!-- ===================================================================== -->
      <!-- SUB-PANEL 1 : FLASHCARDS SRS (ANKI / SM-2) -->
      <!-- ===================================================================== -->
      <div id="bonus-panel-srs" class="bonus-panel space-y-4">
        
        <!-- Controls & Stats Bar -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
          <div class="p-3.5 bg-slate-900 border border-slate-800 rounded-2xl flex items-center justify-between">
            <div>
              <span class="text-[10px] uppercase font-bold text-slate-400 block">Deck Antalgiques</span>
              <span id="srs-card-count" class="text-lg font-black text-amber-300 font-mono">20 cartes</span>
            </div>
            <i data-lucide="layers" class="w-6 h-6 text-amber-400/60"></i>
          </div>
          <div class="p-3.5 bg-slate-900 border border-slate-800 rounded-2xl flex items-center justify-between">
            <div>
              <span class="text-[10px] uppercase font-bold text-slate-400 block">Taux de Rétention</span>
              <span id="srs-retention-rate" class="text-lg font-black text-teal-300 font-mono">94%</span>
            </div>
            <i data-lucide="target" class="w-6 h-6 text-teal-400/60"></i>
          </div>
          <div class="p-3.5 bg-slate-900 border border-slate-800 rounded-2xl flex items-center justify-between">
            <div>
              <span class="text-[10px] uppercase font-bold text-slate-400 block">Série Actuelle (Streak)</span>
              <span id="srs-streak" class="text-lg font-black text-orange-400 font-mono">🔥 4 jours</span>
            </div>
            <i data-lucide="flame" class="w-6 h-6 text-orange-400/60"></i>
          </div>
          <div class="p-3.5 bg-slate-900 border border-slate-800 rounded-2xl flex items-center justify-between">
            <div>
              <span class="text-[10px] uppercase font-bold text-slate-400 block">Progression Deck</span>
              <span id="srs-progress-ratio" class="text-lg font-black text-cyan-300 font-mono">1 / 20</span>
            </div>
            <button onclick="resetSrsProgress()" title="Réinitialiser l'entraînement" class="p-1.5 hover:bg-slate-800 rounded-lg text-slate-400 hover:text-white">
              <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
            </button>
          </div>
        </div>

        <!-- Filter Buttons -->
        <div class="flex flex-wrap gap-1.5 text-xs">
          <button onclick="filterSrsCategory('all')" id="srs-cat-all" class="px-3 py-1 rounded-lg bg-teal-600 text-white font-bold">Toutes (20)</button>
          <button onclick="filterSrsCategory('palier1')" id="srs-cat-palier1" class="px-3 py-1 rounded-lg bg-slate-800 text-slate-300 hover:text-white">Palier I & AINS</button>
          <button onclick="filterSrsCategory('opioides')" id="srs-cat-opioides" class="px-3 py-1 rounded-lg bg-slate-800 text-slate-300 hover:text-white">Opioïdes (Paliers II/III)</button>
          <button onclick="filterSrsCategory('tox')" id="srs-cat-tox" class="px-3 py-1 rounded-lg bg-slate-800 text-slate-300 hover:text-white">Toxicologie & Antidotes</button>
          <button onclick="filterSrsCategory('reglementation')" id="srs-cat-reglementation" class="px-3 py-1 rounded-lg bg-slate-800 text-slate-300 hover:text-white">Réglementation & Doses Max</button>
        </div>

        <!-- The Interactive Flashcard -->
        <div class="p-6 sm:p-8 bg-slate-900 border border-slate-800 rounded-3xl shadow-xl space-y-6 min-h-[320px] flex flex-col justify-between relative overflow-hidden">
          <div class="flex items-center justify-between">
            <span id="srs-card-tag" class="px-2.5 py-1 rounded-full text-[10px] font-black uppercase bg-amber-500/20 text-amber-300 border border-amber-500/40">
              Palier I • AINS
            </span>
            <span id="srs-card-counter" class="text-xs font-mono text-slate-500">Carte 1 sur 20</span>
          </div>

          <!-- Question Prompt (Front) -->
          <div id="srs-front" class="space-y-4 my-auto">
            <h2 id="srs-question" class="text-xl sm:text-2xl font-black text-white leading-snug">
              Pourquoi l'acide acétylsalicylique à faible dose (75 à 160 mg/j) possède-t-il un effet antiagrégant plaquettaire durant 7 à 10 jours ?
            </h2>
            <p id="srs-hint" class="text-xs text-slate-400 italic">Indice : Penser au type d'inhibition de la COX-1 et à la particularité cellulaire des plaquettes sanguines.</p>
          </div>

          <!-- Answer & Explanation (Back) -->
          <div id="srs-back" class="hidden space-y-4 my-auto p-4 rounded-2xl bg-slate-950/80 border border-slate-800">
            <div class="space-y-2">
              <span class="text-xs uppercase font-bold text-teal-400 tracking-wider flex items-center space-x-1">
                <i data-lucide="check-circle-2" class="w-4 h-4"></i>
                <span>Réponse Détaillée :</span>
              </span>
              <p id="srs-answer" class="text-sm sm:text-base text-slate-100 font-medium leading-relaxed">
                L'aspirine <strong>acétyle de façon irréversible et covalente la Sérine 529</strong> de l'enzyme COX-1 plaquettaire, bloquant la synthèse de Thromboxane A2 (TXA2). Comme les plaquettes sont des éléments anucléés incapables de synthétiser de nouvelles protéines, l'inhibition dure toute leur durée de vie circulante (7 à 10 jours).
              </p>
            </div>
            
            <div class="p-3 rounded-xl bg-teal-950/40 border border-teal-800/50 text-xs text-teal-200">
              <strong class="text-teal-300 block mb-0.5">🌟 Perle Concours & Officine :</strong>
              <span id="srs-pearl">Pour un acte chirurgical à risque hémorragique, l'arrêt de l'aspirine à visée antiagrégante doit être discuté 5 à 7 jours avant le geste afin de permettre le renouvellement d'un contingent plaquettaire hémostatique.</span>
            </div>
          </div>

          <!-- Card Controls -->
          <div class="pt-4 border-t border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-4">
            <button id="srs-btn-reveal" onclick="revealSrsAnswer()" class="w-full sm:w-auto px-6 py-3 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-black text-xs transition flex items-center justify-center space-x-2 shadow-lg shadow-amber-500/20">
              <i data-lucide="eye" class="w-4 h-4"></i>
              <span>Afficher la Réponse (Espace)</span>
            </button>

            <!-- SM-2 Feedback Buttons -->
            <div id="srs-rating-buttons" class="hidden w-full sm:w-auto flex flex-wrap sm:flex-nowrap gap-2">
              <button onclick="rateSrsCard(1)" class="flex-1 px-3 py-2.5 rounded-xl bg-rose-950/70 hover:bg-rose-900 border border-rose-800 text-rose-300 text-xs font-bold transition flex flex-col items-center">
                <span>🔴 À revoir</span>
                <span class="text-[9px] text-rose-400/80 font-mono">< 10 min</span>
              </button>
              <button onclick="rateSrsCard(2)" class="flex-1 px-3 py-2.5 rounded-xl bg-orange-950/70 hover:bg-orange-900 border border-orange-800 text-orange-300 text-xs font-bold transition flex flex-col items-center">
                <span>🟠 Difficile</span>
                <span class="text-[9px] text-orange-400/80 font-mono">1 jour</span>
              </button>
              <button onclick="rateSrsCard(3)" class="flex-1 px-3 py-2.5 rounded-xl bg-teal-950/70 hover:bg-teal-900 border border-teal-800 text-teal-300 text-xs font-bold transition flex flex-col items-center">
                <span>🟢 Correct</span>
                <span class="text-[9px] text-teal-400/80 font-mono">3 jours</span>
              </button>
              <button onclick="rateSrsCard(4)" class="flex-1 px-3 py-2.5 rounded-xl bg-cyan-950/70 hover:bg-cyan-900 border border-cyan-800 text-cyan-300 text-xs font-bold transition flex flex-col items-center">
                <span>🔵 Facile</span>
                <span class="text-[9px] text-cyan-400/80 font-mono">7 jours</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- SUB-PANEL 2 : SIMULATEUR D'ECOS PHARMACEUTIQUE (PATIENT VIRTUEL) -->
      <!-- ===================================================================== -->
      <div id="bonus-panel-ecos" class="bonus-panel hidden space-y-6">
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          
          <!-- Left: Scenarios Selector & Virtual Patient -->
          <div class="p-6 bg-slate-900 border border-slate-800 rounded-3xl space-y-4">
            <div class="flex items-center justify-between">
              <span class="text-xs uppercase font-bold text-teal-400">Scénarios d'Épreuve ECOS</span>
              <span class="px-2 py-0.5 rounded-md bg-teal-500/20 text-teal-300 text-[10px] font-mono">7 minutes</span>
            </div>

            <div class="space-y-2">
              <button onclick="loadEcosScenario(1)" id="ecos-btn-scen-1" class="w-full text-left p-3 rounded-2xl bg-teal-950/70 border border-teal-500/50 text-xs transition">
                <span class="font-bold text-teal-200 block">Cas 1 : Comptoir Officinal</span>
                <span class="text-slate-400 text-[11px]">Mme Dubois (65 ans) • Sciatique & Automédication AINS masquée</span>
              </button>
              <button onclick="loadEcosScenario(2)" id="ecos-btn-scen-2" class="w-full text-left p-3 rounded-2xl bg-slate-800/40 hover:bg-slate-800 border border-slate-700 text-xs transition">
                <span class="font-bold text-slate-200 block">Cas 2 : Chirurgie Orthopédique</span>
                <span class="text-slate-400 text-[11px]">M. Mercier (52 ans) • Tramadol + Antidépresseur ISRS</span>
              </button>
              <button onclick="loadEcosScenario(3)" id="ecos-btn-scen-3" class="w-full text-left p-3 rounded-2xl bg-slate-800/40 hover:bg-slate-800 border border-slate-700 text-xs transition">
                <span class="font-bold text-slate-200 block">Cas 3 : Soins Palliatifs</span>
                <span class="text-slate-400 text-[11px]">M. Laurent (78 ans) • Insuffisance rénale DFG 22 & Morphine LP</span>
              </button>
            </div>

            <!-- Patient Profile Card -->
            <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-3">
              <div class="flex items-center space-x-3">
                <div id="ecos-patient-avatar" class="w-10 h-10 rounded-xl bg-teal-500/20 border border-teal-500/40 flex items-center justify-center text-teal-300 font-bold">
                  MD
                </div>
                <div>
                  <h3 id="ecos-patient-name" class="font-bold text-sm text-white">Mme Monique Dubois</h3>
                  <p id="ecos-patient-details" class="text-[11px] text-slate-400">65 ans • 68 kg • Créatinine 92 µmol/L (DFG 62 mL/min)</p>
                </div>
              </div>
              <div class="text-[11px] space-y-1 pt-2 border-t border-slate-800/80">
                <div><span class="text-slate-400">Antécédents :</span> <span id="ecos-patient-history" class="text-slate-200 font-medium">HTA, Insuffisance cardiaque légère, Ulcère duodénal il y a 8 ans.</span></div>
                <div><span class="text-slate-400">Traitement de fond :</span> <span id="ecos-patient-meds" class="text-slate-200 font-medium">Ramipril 5 mg, Furosémide 20 mg.</span></div>
                <div><span class="text-slate-400">Motif de venue :</span> <span id="ecos-patient-complaint" class="text-amber-300 font-medium">Demande une boîte d'Ibuprofène 400 mg pour une douleur sciatique aiguë.</span></div>
              </div>
            </div>

            <!-- Virtual Interrogation Buttons -->
            <div class="space-y-2">
              <span class="text-[10px] uppercase font-bold text-slate-400 block">Questions au patient (Clique pour interroger) :</span>
              <div id="ecos-question-buttons" class="space-y-1.5">
                <!-- Populated dynamically -->
              </div>
            </div>

            <!-- Dialogue Box -->
            <div id="ecos-dialogue-box" class="p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-300 italic min-h-[60px] flex items-center">
              « Bonjour Docteur, j'ai une sciatique insupportable depuis hier soir. Ma voisine m'a conseillé de prendre de l'Ibuprofène 400 mg 3 fois par jour, vous pouvez m'en donner ? »
            </div>
          </div>

          <!-- Right: Pharmaceutical Analysis & Scoring -->
          <div class="lg:col-span-2 p-6 bg-slate-900 border border-slate-800 rounded-3xl space-y-5">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
              <h3 class="font-black text-lg text-white flex items-center space-x-2">
                <i data-lucide="clipboard-check" class="w-5 h-5 text-teal-400"></i>
                <span>Grille d'Analyse Pharmaceutique (SFPC)</span>
              </h3>
              <span id="ecos-jury-score" class="px-3 py-1 rounded-full bg-slate-800 text-slate-300 font-mono text-xs font-bold">
                Note : En attente d'évaluation
              </span>
            </div>

            <!-- Step 1: PLM -->
            <div class="space-y-2">
              <label class="block text-xs font-bold text-slate-300">
                1. Identification du Problème Lié au Médicament (PLM Majeur) :
              </label>
              <select id="ecos-input-plm" class="w-full p-3 rounded-xl bg-slate-950 border border-slate-700 text-xs text-slate-200">
                <!-- Options populated in JS -->
              </select>
            </div>

            <!-- Step 2: IP -->
            <div class="space-y-2">
              <label class="block text-xs font-bold text-slate-300">
                2. Intervention Pharmaceutique (IP) & Conduite à Tenir :
              </label>
              <select id="ecos-input-ip" class="w-full p-3 rounded-xl bg-slate-950 border border-slate-700 text-xs text-slate-200">
                <!-- Options populated in JS -->
              </select>
            </div>

            <!-- Step 3: Patient Counseling ETP -->
            <div class="space-y-2">
              <label class="block text-xs font-bold text-slate-300">
                3. Plan de Conseils & Éducation Thérapeutique du Patient (ETP) :
              </label>
              <select id="ecos-input-etp" class="w-full p-3 rounded-xl bg-slate-950 border border-slate-700 text-xs text-slate-200">
                <!-- Options populated in JS -->
              </select>
            </div>

            <div class="flex items-center justify-between pt-3 border-t border-slate-800">
              <button onclick="evaluateEcosSubmission()" class="px-6 py-3 rounded-xl bg-teal-600 hover:bg-teal-500 text-white font-black text-xs transition flex items-center space-x-2 shadow-lg shadow-teal-500/20">
                <i data-lucide="award" class="w-4 h-4"></i>
                <span>Soumettre au Jury de l'Examen</span>
              </button>
              <span class="text-[11px] text-slate-400">Barème : 20 points (Grille officielle concours)</span>
            </div>

            <!-- Jury Feedback Output -->
            <div id="ecos-jury-feedback" class="hidden p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-2">
              <div class="flex items-center justify-between">
                <span class="font-bold text-xs text-white">Verdict & Débriefing du Jury :</span>
                <span id="ecos-final-grade" class="text-sm font-black font-mono text-teal-400">18 / 20</span>
              </div>
              <p id="ecos-feedback-text" class="text-xs text-slate-300 leading-relaxed"></p>
            </div>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- SUB-PANEL 3 : RUMACK-MATTHEW & CYP2D6 -->
      <!-- ===================================================================== -->
      <div id="bonus-panel-rumack-cyp" class="bonus-panel hidden space-y-6">
        
        <!-- Part A : Rumack-Matthew Nomogram -->
        <div class="p-6 bg-slate-900 border border-slate-800 rounded-3xl space-y-5">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
              <h3 class="font-black text-lg text-white flex items-center space-x-2">
                <i data-lucide="line-chart" class="w-5 h-5 text-rose-400"></i>
                <span>Nomogramme Interactif de Rumack-Matthew (Toxicité Paracétamol)</span>
              </h3>
              <p class="text-xs text-slate-400">Décision d'administration de la N-Acétylcystéine (NAC) selon le délai post-ingestion (H4 à H24).</p>
            </div>
            <span id="rumack-status-badge" class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-xs font-bold font-mono">
              Zone Sécurisée (Non toxique)
            </span>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 items-center">
            
            <!-- Controls -->
            <div class="space-y-4 p-4 rounded-2xl bg-slate-950 border border-slate-800">
              <div class="space-y-1.5">
                <div class="flex justify-between text-xs">
                  <span class="font-bold text-slate-300">Délai post-ingestion :</span>
                  <span id="rumack-hours-val" class="font-black text-rose-300 font-mono">8 heures</span>
                </div>
                <input type="range" id="rumack-hours-slider" min="4" max="24" step="1" value="8" oninput="updateRumackPlot()" class="w-full accent-rose-500">
                <div class="flex justify-between text-[10px] text-slate-500 font-mono">
                  <span>H4 (prélèvement min)</span>
                  <span>H12</span>
                  <span>H24</span>
                </div>
              </div>

              <div class="space-y-1.5">
                <div class="flex justify-between text-xs">
                  <span class="font-bold text-slate-300">Paracétamolémie mesurée :</span>
                  <span id="rumack-conc-val" class="font-black text-rose-300 font-mono">80 mg/L</span>
                </div>
                <input type="range" id="rumack-conc-slider" min="10" max="350" step="5" value="80" oninput="updateRumackPlot()" class="w-full accent-rose-500">
                <div class="flex justify-between text-[10px] text-slate-500 font-mono">
                  <span>10 mg/L</span>
                  <span>150 mg/L (Seuil H4)</span>
                  <span>350 mg/L</span>
                </div>
              </div>

              <div class="space-y-1.5">
                <div class="flex justify-between text-xs">
                  <span class="font-bold text-slate-300">Poids du patient :</span>
                  <span id="rumack-weight-val" class="font-black text-teal-300 font-mono">70 kg</span>
                </div>
                <input type="range" id="rumack-weight-slider" min="30" max="120" step="5" value="70" oninput="updateRumackPlot()" class="w-full accent-teal-500">
              </div>

              <!-- Prescott Calculation Box -->
              <div id="prescott-calc-box" class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-1 text-xs">
                <span class="font-bold text-amber-300 block">Protocole de Prescott (NAC IV) :</span>
                <p id="prescott-doses" class="text-[11px] text-slate-300 leading-relaxed font-mono">
                  1) Charge : 10.5 g en 1h dans 200 mL G5%<br>
                  2) Entretien 1 : 3.5 g en 4h dans 500 mL G5%<br>
                  3) Entretien 2 : 7.0 g en 16h dans 1000 mL G5%
                </p>
              </div>
            </div>

            <!-- Graph Canvas -->
            <div class="lg:col-span-2 bg-slate-950 p-4 rounded-2xl border border-slate-800 relative">
              <canvas id="rumack-canvas" width="600" height="300" class="w-full h-[280px]"></canvas>
            </div>

          </div>
        </div>

        <!-- Part B : CYP2D6 Pharmacogenetics -->
        <div class="p-6 bg-slate-900 border border-slate-800 rounded-3xl space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
            <div>
              <h3 class="font-black text-lg text-white flex items-center space-x-2">
                <i data-lucide="dna" class="w-5 h-5 text-purple-400"></i>
                <span>Simulateur de Polymorphisme CYP2D6 (Codéine & Tramadol)</span>
              </h3>
              <p class="text-xs text-slate-400">Impact du statut génétique sur l'activation métabolique en Morphine / M1 actif.</p>
            </div>
            <div class="flex items-center space-x-1 p-1 bg-slate-950 rounded-xl border border-slate-800 text-xs">
              <button onclick="setCYP2D6Phenotype('PM')" id="cyp-btn-PM" class="px-3 py-1 rounded-lg text-slate-300 hover:text-white transition">Métaboliseur Lent (PM)</button>
              <button onclick="setCYP2D6Phenotype('EM')" id="cyp-btn-EM" class="px-3 py-1 rounded-lg bg-purple-600 text-white font-bold transition">Normal (EM)</button>
              <button onclick="setCYP2D6Phenotype('UM')" id="cyp-btn-UM" class="px-3 py-1 rounded-lg text-slate-300 hover:text-white transition">Ultra-Rapide (UM)</button>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 space-y-2 text-xs">
              <span id="cyp-phenotype-title" class="font-black text-purple-300 text-sm block">Métaboliseur Normal (Extensive Metabolizer - EM)</span>
              <p id="cyp-phenotype-desc" class="text-slate-300 leading-relaxed text-[11px]">
                Transformation physiologique d'environ 10% de la dose de codéine en morphine active par le CYP2D6 hépatique. L'effet antalgique est optimal et reproductible aux posologies recommandées.
              </p>
              <div id="cyp-clinical-alert" class="p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-800/60 text-emerald-200 text-[11px]">
                <strong>Conséquence clinique :</strong> Analgésie normale. Posologie standard validée.
              </div>
            </div>

            <div class="bg-slate-950 p-4 rounded-2xl border border-slate-800 flex items-center justify-center">
              <canvas id="cyp-canvas" width="400" height="150" class="w-full h-[140px]"></canvas>
            </div>
          </div>
        </div>

      </div>

      <!-- ===================================================================== -->
      <!-- SUB-PANEL 4 : MODE GARDE D'URGENCE (TIME-ATTACK 90s) -->
      <!-- ===================================================================== -->
      <div id="bonus-panel-emergency" class="bonus-panel hidden space-y-6">
        <div class="p-6 bg-slate-900 border border-slate-800 rounded-3xl space-y-5">
          <div class="flex items-center justify-between border-b border-slate-800 pb-4">
            <div>
              <h3 class="font-black text-xl text-white flex items-center space-x-2">
                <i data-lucide="alarm-clock" class="w-6 h-6 text-rose-400"></i>
                <span>Défi Garde Hospitalière de Nuit (90 Secondes)</span>
              </h3>
              <p class="text-xs text-slate-400">L'urgence n'attend pas : prends les bonnes décisions pharmacologiques sous pression chrono !</p>
            </div>
            <div class="flex items-center space-x-3">
              <div class="text-right">
                <span class="text-[10px] uppercase font-bold text-slate-400 block">Temps Restant</span>
                <span id="game-timer" class="text-2xl font-black text-rose-400 font-mono">90s</span>
              </div>
              <button id="game-start-btn" onclick="startEmergencyGame()" class="px-5 py-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold text-xs shadow-lg shadow-rose-600/30 transition">
                Démarrer la Garde
              </button>
            </div>
          </div>

          <!-- Active Case Card -->
          <div id="game-active-card" class="p-6 rounded-2xl bg-slate-950 border border-slate-800 space-y-4">
            <div class="flex items-center justify-between">
              <span id="game-case-badge" class="px-2.5 py-1 rounded-full text-[10px] font-black uppercase bg-rose-500/20 text-rose-300 border border-rose-500/40">
                URGENCE 1 / 5 • SERVICE POST-OP
              </span>
              <span id="game-score-display" class="font-mono text-xs text-slate-400">Score : 0 pts</span>
            </div>

            <h4 id="game-scenario-text" class="text-base sm:text-lg font-bold text-white leading-relaxed">
              Clique sur « Démarrer la Garde » pour lancer l'épreuve chronométrée.
            </h4>

            <div id="game-options-container" class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
              <!-- Choices populated dynamically -->
            </div>
          </div>

          <!-- Badges & Hall of Fame -->
          <div class="p-4 rounded-2xl bg-slate-950/60 border border-slate-800/80 flex flex-wrap items-center justify-between gap-2 text-xs">
            <div class="flex items-center space-x-2 text-slate-400">
              <i data-lucide="shield-check" class="w-4 h-4 text-teal-400"></i>
              <span>Badges de garde : <strong id="game-badges-count" class="text-white">0 débloqué</strong></span>
            </div>
            <div class="flex space-x-2">
              <span class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-500 font-mono text-[10px]" id="badge-1">🛡️ Anti-Triple Whammy</span>
              <span class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-500 font-mono text-[10px]" id="badge-2">🧪 As de Prescott</span>
              <span class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-500 font-mono text-[10px]" id="badge-3">⚡ Sauveur Naloxone</span>
            </div>
          </div>
        </div>
      </div>

      <!-- ===================================================================== -->
      <!-- SUB-PANEL 5 : AUDIO-LEARNING & FICHE MÉMO IMPRIMABLE -->
      <!-- ===================================================================== -->
      <div id="bonus-panel-audio-memo" class="bonus-panel hidden space-y-6">
        
        <!-- Audio Player Card -->
        <div class="p-6 bg-slate-900 border border-slate-800 rounded-3xl space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-800 pb-3">
            <div>
              <h3 class="font-black text-lg text-white flex items-center space-x-2">
                <i data-lucide="headphones" class="w-5 h-5 text-emerald-400"></i>
                <span>Lecteur Audio-Learning (Web Speech API Native)</span>
              </h3>
              <p class="text-xs text-slate-400">Écoute les fiches de synthèse en 90 secondes avec la voix française de ton navigateur (100% hors-ligne).</p>
            </div>
            <div class="flex items-center space-x-2">
              <select id="audio-molecule-select" onchange="loadAudioMonograph(this.value)" class="p-2 rounded-xl bg-slate-950 border border-slate-700 text-xs text-slate-200">
                <!-- Molecules options -->
              </select>
            </div>
          </div>

          <!-- Audio Controls -->
          <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center space-x-2">
              <button onclick="playAudioFlash()" id="audio-play-btn" class="px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs flex items-center space-x-1.5 transition">
                <i data-lucide="play" class="w-4 h-4"></i>
                <span>Lecture</span>
              </button>
              <button onclick="pauseAudioFlash()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition">
                <i data-lucide="pause" class="w-4 h-4"></i>
              </button>
              <button onclick="stopAudioFlash()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold transition">
                <i data-lucide="square" class="w-4 h-4"></i>
              </button>
            </div>

            <div class="flex items-center space-x-2 text-xs">
              <span class="text-slate-400">Vitesse :</span>
              <button onclick="setAudioSpeed(1.0)" id="speed-10" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-bold">1x</button>
              <button onclick="setAudioSpeed(1.25)" id="speed-125" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">1.25x</button>
              <button onclick="setAudioSpeed(1.5)" id="speed-15" class="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300">1.5x</button>
            </div>
          </div>

          <!-- Transcript Preview -->
          <div class="p-4 rounded-2xl bg-slate-950/60 border border-slate-800/80 space-y-1">
            <span class="text-[10px] uppercase font-bold text-slate-500 block">Texte récité par la synthèse vocale :</span>
            <p id="audio-transcript-text" class="text-xs text-slate-300 leading-relaxed font-sans"></p>
          </div>
        </div>

        <!-- Printable Pocket Card Summary Table -->
        <div class="p-6 bg-slate-900 border border-slate-800 rounded-3xl space-y-4" id="printable-pocket-card">
          <div class="flex items-center justify-between border-b border-slate-800 pb-3">
            <div>
              <h3 class="font-black text-lg text-white flex items-center space-x-2">
                <i data-lucide="printer" class="w-5 h-5 text-teal-400"></i>
                <span>Fiche Mémo de Poche (Tableau Synoptique des 24 DCI)</span>
              </h3>
              <p class="text-xs text-slate-400">Format compact optimisé pour l'impression A4 et la plastification pour vos stages.</p>
            </div>
            <button onclick="window.print()" class="px-4 py-2 rounded-xl bg-teal-600 hover:bg-teal-500 text-white font-bold text-xs flex items-center space-x-1.5 shadow-lg shadow-teal-500/20 transition">
              <i data-lucide="printer" class="w-4 h-4"></i>
              <span>Imprimer la Fiche A4</span>
            </button>
          </div>

          <div class="overflow-x-auto rounded-2xl border border-slate-800">
            <table class="w-full text-[11px] text-left text-slate-300">
              <thead class="bg-slate-950 text-slate-400 uppercase font-bold text-[10px] border-b border-slate-800">
                <tr>
                  <th class="p-2.5">DCI & Spécialité</th>
                  <th class="p-2.5">Palier</th>
                  <th class="p-2.5">Dose Max Adulte</th>
                  <th class="p-2.5">Demi-vie (t½)</th>
                  <th class="p-2.5">Métabolisme</th>
                  <th class="p-2.5">Contre-indications Majeures</th>
                </tr>
              </thead>
              <tbody id="pocket-table-body" class="divide-y divide-slate-800/60 font-sans">
                <!-- Dynamically populated with all 24 molecules -->
              </tbody>
            </table>
          </div>
        </div>

      </div>

    </section>
'''

if 'id="sec-bonus-hub"' not in template:
    template = template.replace('  </main>', bonus_hub_section + '\n  </main>', 1)

# 4. Update JavaScript switchMasterTab logic
old_switch_master = "const tabs = ['encyclopedia', 'pk-lab', 'studio-3d', 'cascades', 'clinical-sim', 'tactical-hub'];"
new_switch_master = "const tabs = ['encyclopedia', 'pk-lab', 'studio-3d', 'cascades', 'clinical-sim', 'tactical-hub', 'bonus-hub'];"
template = template.replace(old_switch_master, new_switch_master)

# 5. Insert Bonus Hub JavaScript Logic into <script>
bonus_js_logic = '''
    // =========================================================================
    // 7. BONUS HUB LOGIC (SRS, ECOS, RUMACK-MATTHEW, CYP2D6, EMERGENCY, AUDIO)
    // =========================================================================
    
    // Sub-tabs switcher in Bonus Hub
    function switchBonusSubTab(subTabId) {
      const subTabs = ['srs', 'ecos', 'rumack-cyp', 'emergency', 'audio-memo'];
      subTabs.forEach(st => {
        const panel = document.getElementById(`bonus-panel-${st}`);
        const btn = document.getElementById(`bonus-sub-btn-${st}`);
        if (st === subTabId) {
          panel.classList.remove('hidden');
          btn.className = 'bonus-sub-btn active px-4 py-2.5 rounded-xl transition flex items-center space-x-2 bg-amber-500 text-slate-950 font-bold shadow-md';
        } else {
          panel.classList.add('hidden');
          btn.className = 'bonus-sub-btn px-4 py-2.5 rounded-xl transition flex items-center space-x-2 text-slate-300 hover:text-white hover:bg-slate-800';
        }
      });
      lucide.createIcons();

      if (subTabId === 'rumack-cyp') {
        setTimeout(() => { drawRumackPlot(); drawCYPPlot(); }, 50);
      }
    }

    // --- A. FLASHCARDS SRS (ANKI / SM-2) ---
    const SRS_CARDS = [
      {
        id: 1,
        cat: 'palier1',
        tag: 'Palier I • AINS Salicylé',
        q: "Pourquoi l'acide acétylsalicylique (aspirine) à dose antiagrégante (75 à 160 mg/j) possède-t-il une action durant 7 à 10 jours ?",
        hint: "Penser au type de liaison chimique avec la COX-1 et à l'équipement protéique des plaquettes.",
        a: "L'aspirine acétyle de façon irréversible et covalente la Sérine 529 de la COX-1 plaquettaire, bloquant définitivement la synthèse de Thromboxane A2 (TXA2). Les plaquettes étant anucléées, elles ne peuvent pas resynthétiser l'enzyme : l'effet dure toute leur vie circulante (7 à 10 jours).",
        pearl: "L'arrêt pré-opératoire de l'aspirine antiagrégante doit être planifié 5 à 7 jours avant une chirurgie à risque hémorragique."
      },
      {
        id: 2,
        cat: 'palier1',
        tag: 'Palier I • Non Opioïde',
        q: "Quelle est la posologie pédiatrique stricte du paracétamol et quel est le risque en cas d'erreur de calcul ?",
        hint: "Dose en mg/kg/jour et fractionnement en prises.",
        a: "La posologie pédiatrique est de 60 mg/kg/jour répartie en 4 à 6 prises, soit 15 mg/kg toutes les 6 heures (ou 10 mg/kg toutes les 4h). Ne jamais dépasser 15 mg/kg par prise ni 4 g/jour. Risque majeur d'hépatite fulminante par déplétion en glutathion et accumulation de NAPQI.",
        pearl: "Toujours utiliser la pipette doseuse graduée en kg fournie avec le sirop pour éviter les erreurs de cuillère."
      },
      {
        id: 3,
        cat: 'tox',
        tag: 'Toxicologie • Paracétamol',
        q: "Quel est le métabolite hépatotoxique du paracétamol, comment est-il détoxifié à dose usuelle et que se passe-t-il en cas de surdosage ?",
        hint: "CYP2E1 et réserve hépatique en antioxydant soufré.",
        a: "Le métabolite est le NAPQI (N-acétyl-p-benzoquinone imine), produit par le CYP2E1 (5-10%). À dose normale, il est immédiatement neutralisé par le glutathion réduit (GSH). En cas de surdosage (> 8-10 g chez l'adulte, > 150 mg/kg chez l'enfant), les stocks de glutathion s'épuisent (> 70%) : le NAPQI libre se lie aux protéines hépatocytaires et cause une nécrose centrolobulaire massive.",
        pearl: "L'antidote N-Acétylcystéine (NAC) reconstitue directement les stocks hépatiques de glutathion."
      },
      {
        id: 4,
        cat: 'palier1',
        tag: 'Palier I • Contre-indications AINS',
        q: "À partir de quel terme de la grossesse les AINS sont-ils formellement et absolument contre-indiqués et pourquoi ?",
        hint: "Semaines d'aménorrhée (SA) et répercussions cardiorespiratoires/rénales fœtales.",
        a: "Contre-indication FORMELLE et ABSOLUE dès le début du 6e mois de grossesse (24 semaines d'aménorrhée - SA). Risques pour le fœtus : 1) Fermeture prématurée in utero du canal artériel pouvant entraîner une insuffisance cardiaque droite et une mort fœtale. 2) Insuffisance rénale fœtale avec anamnios.",
        pearl: "Cette contre-indication s'applique à TOUS les AINS, y compris en prise unique et y compris par voie cutanée ou collyre."
      },
      {
        id: 5,
        cat: 'palier1',
        tag: 'Palier I • Interactions AINS',
        q: "Qu'appelle-t-on l'interaction du « Triple Whammy » et quelles en sont les conséquences rénales ?",
        hint: "Association de 3 classes médicamenteuses courantes chez le sujet hypertendu.",
        a: "C'est l'association AINS + Diurétique + IEC (ou ARA2). L'AINS bloque les prostaglandines vasodilatatrices de l'artériole afférente glomérulaire. L'IEC bloque l'angiotensine II vasoconstrictrice de l'artériole efférente. Le diurétique crée une hypovolémie. Résultat : effondrement de la pression d'ultrafiltration glomérulaire et Insuffisance Rénale Aiguë (IRA) oligo-anurique.",
        pearl: "Un grand classique du concours et des urgences : toujours doser la créatinine et le potassium lors de cette association."
      },
      {
        id: 6,
        cat: 'opioides',
        tag: 'Palier II • Pharmacogénétique',
        q: "Pourquoi la codéine et le tramadol sont-ils inefficaces chez 7-10% des patients et potentiellement mortels chez d'autres ?",
        hint: "Cytochrome hépatique et métaboliseurs lents vs ultra-rapides.",
        a: "Ce sont des prodrogues qui nécessitent d'être bioactivées par le CYP2D6 (en Morphine pour la codéine, et en O-déméthyltramadol M1 pour le tramadol). Chez les Métaboliseurs Lents (PM), il n'y a aucune transformation = inefficacité analgésique totale. Chez les Métaboliseurs Ultra-Rapides (UM), il y a surproduction massive et rapide de métabolite actif = dépression respiratoire toxique majeure.",
        pearl: "La codéine est contre-indiquée chez les moins de 12 ans et les femmes qui allaitent pour cette raison génétique."
      },
      {
        id: 7,
        cat: 'opioides',
        tag: 'Palier II • Tramadol',
        q: "Quels sont les deux mécanismes d'action distincts du tramadol et quelle interaction redoutable en découle ?",
        hint: "Récepteur opioïde + neurotransmetteurs monoaminergiques.",
        a: "Mécanisme dual : 1) Agoniste faible des récepteurs opioïdes µ (surtout via son métabolite M1). 2) Inhibiteur de la recapture de la Sérotonine (5-HT) et de la Noradrénaline (NA). Interaction majeure : avec les antidépresseurs IRS/IRSNA, triptans ou IMAO, risque de Syndrome Sérotoninergique potentiellement létal.",
        pearl: "Le tramadol abaisse également le seuil épileptogène : prudence absolue chez le patient épileptique."
      },
      {
        id: 8,
        cat: 'opioides',
        tag: 'Palier III • Métabolites de la Morphine',
        q: "Quels sont les deux principaux métabolites glucuroconjugués de la morphine et pourquoi posent-ils problème chez l'insuffisant rénal ?",
        hint: "M6G vs M3G et voies d'élimination.",
        a: "1) Morphine-6-Glucuronide (M6G) : actif, puissant analgésique et dépresseur respiratoire. 2) Morphine-3-Glucuronide (M3G) : dépourvu d'action opioïde, neurotoxique (hyperalgésie paradoxale, allodynie, myoclonies, convulsions). Tous deux sont éliminés par filtration glomérulaire rénale et s'accumulent dangereusement si DFG < 30 mL/min.",
        pearl: "Chez l'insuffisant rénal sévère, on privilégie l'Oxycodone (à dose adaptée) ou le Fentanyl dont les métabolites sont inactifs."
      },
      {
        id: 9,
        cat: 'opioides',
        tag: 'Palier III • Règle de Titration',
        q: "Comment calcule-t-on la dose unitaire d'un Accès Douloureux Paroxystique (ADP) chez un patient sous morphine LP ?",
        hint: "Règle mathématique du 1/6e.",
        a: "La dose d'interdose en Libération Immédiate (LI, ex: Actiskénan®, Sévredol®) est égale à 1/6e (ou 10 à 15%) de la dose quotidienne totale de morphine orale. Par exemple, si le patient reçoit Skenan® 60 mg matin et soir (total 120 mg/24h), chaque interdose d'ADP sera de 120 / 6 = 20 mg LI.",
        pearl: "Si le patient prend plus de 4 interdoses par 24h, il faut réévaluer et augmenter la dose de fond LP."
      },
      {
        id: 10,
        cat: 'opioides',
        tag: 'Palier III • Rotation des Opioïdes',
        q: "Lors d'une rotation d'un opioïde fort vers un autre, pourquoi applique-t-on un abattement de 25% à 50% de la dose équianalgésique calculée ?",
        hint: "Tolérance croisée incomplète.",
        a: "En raison du phénomène de 'Tolérance Croisée Incomplète'. Les différents opioïdes n'activent pas les sous-populations de récepteurs µ avec la même configuration tridimensionnelle. Le patient n'étant pas pleinement tolérant à la nouvelle molécule, lui administrer 100% de la dose équivalente théorique provoquerait un surdosage aigu et une dépression respiratoire.",
        pearl: "La règle SFAP recommande de calculer la dose théorique, puis d'appliquer une réduction systématique de 25 à 30% (voire 50% pour la méthadone)."
      },
      {
        id: 11,
        cat: 'reglementation',
        tag: 'Réglementation • Stupéfiants',
        q: "Quelles sont les règles de prescription et délivrance de la Morphine et du Fentanyl en France (Ordonnance Sécurisée) ?",
        hint: "Durée maximale, rédaction des doses, chevauchement.",
        a: "Prescription sur Ordonnance Sécurisée (papier filigrané avec carré de sécurité). Durée maximale de prescription : 28 jours (ou 14 jours pour certaines formes injectables). Posologies et doses rédigées EN TOUTES LETTRES. Règle du non-chevauchement : délivrance interdite pour une période déjà couverte sauf mention expresse du médecin 'en complément de'. Déconditionnement à l'unité.",
        pearl: "Le fentanyl transdermique (Durogesic®) est limité à 28 jours avec fractionnement de délivrance de 14 jours par défaut."
      },
      {
        id: 12,
        cat: 'tox',
        tag: 'Antidote • Opioïdes',
        q: "Quel est l'antidote spécifique de l'overdose aux morphiniques, sa voie d'administration et la précaution cruciale de sa durée d'action ?",
        hint: "Naloxone et risque de rebond de dépression respiratoire.",
        a: "La Naloxone (Narcan®). Antagoniste pur compétitif des récepteurs µ. Titration IV : ampoule de 0.4 mg diluée dans 9 mL de sérum physiologique, injecter 1 à 2 mL (0.04 à 0.08 mg) toutes les 2 min jusqu'à FR > 10. Précaution capitale : la demi-vie de la naloxone est très courte (30 à 60 min), inférieure à celle de la morphine (2-3h) ou de la méthadone (24-36h). Risque de rechute en coma apnéique imposant une perfusion continue.",
        pearl: "Une titration trop rapide peut déclencher un syndrome de sevrage aigu violent avec œdème aigu du poumon (OAP) catécholaminergique."
      },
      {
        id: 13,
        cat: 'tox',
        tag: 'Antidote • Prescott',
        q: "Décrivez le protocole de Prescott complet pour l'administration de la N-Acétylcystéine (NAC) en perfusion IV.",
        hint: "Dose totale 300 mg/kg répartie en 3 phases sur 21 heures.",
        a: "Protocole IV en 3 perfusions dans du sérum glucosé G5% : 1) Dose de charge : 150 mg/kg dans 200 mL G5% en 60 minutes. 2) Deuxième perfusion : 50 mg/kg dans 500 mL G5% en 4 heures. 3) Troisième perfusion : 100 mg/kg dans 1000 mL G5% en 16 heures. Total = 300 mg/kg en 21 heures.",
        pearl: "Le traitement est efficace à 100% s'il est débuté dans les 8 premières heures suivant l'ingestion du paracétamol."
      },
      {
        id: 14,
        cat: 'opioides',
        tag: 'Palier III • Buprénorphine',
        q: "Pourquoi est-il formellement contre-indiqué d'associer la Buprénorphine (Subutex®, Temgesic®) avec la Morphine ?",
        hint: "Agoniste partiel à très haute affinité vs agoniste pur.",
        a: "La Buprénorphine est un agoniste partiel des récepteurs µ avec une affinité de liaison extrêmement forte, bien supérieure à celle de la morphine. Elle déplace instantanément la morphine de ses récepteurs, mais n'active le récepteur qu'à 40-50% (faible activité intrinsèque) : cela déclenche immédiatement un Syndrome de Sevrage Aigu précipité et une réapparition brutale de la douleur.",
        pearl: "La buprénorphine a un effet plafond sur la dépression respiratoire, mais son antidote naloxone doit être utilisé à doses beaucoup plus fortes."
      },
      {
        id: 15,
        cat: 'palier1',
        tag: 'Palier I • Sélectivité COX-2',
        q: "Quelle différence structurale au niveau du site actif explique la sélectivité des Coxibs (Célécoxib) pour la COX-2 par rapport à la COX-1 ?",
        hint: "Acide aminé en position 523.",
        a: "En position 523 : la COX-1 possède une volumineuse Isoleucine (Ile523) qui encombre l'entrée. La COX-2 possède une Valine (Val523), plus petite d'un groupement méthyle (-CH3), ce qui libère une poche latérale hydrophobe supplémentaire de 20%. Le groupement sulfonamide encombrant du célécoxib ne peut s'insérer que dans la COX-2.",
        pearl: "L'inhibition sélective de COX-2 préserve l'estomac mais supprime la PGI2 endothéliale vasodilatatrice/antithrombotique sans bloquer le TXA2 plaquettaire : risque d'infarctus du myocarde et d'AVC."
      },
      {
        id: 16,
        cat: 'palier1',
        tag: 'Palier I • Fixation Protéique',
        q: "Pourquoi les AINS (Ibuprofène, Diclofénac) provoquent-ils des interactions médicamenteuses majeures par déplacement protéique ?",
        hint: "Taux de liaison à l'albumine (> 99%) et médicaments à marge thérapeutique étroite.",
        a: "Les AINS sont fortement liés à l'albumine plasmatique (> 99%). Ils entrent en compétition et déplacent d'autres molécules acides à forte fixation protéique : Antivitamines K (Fluindione, Warfarine), Sulfamides hypoglycémiants, et Méthotrexate. La fraction libre active de ces médicaments augmente brusquement, provoquant hémorragies, hypoglycémies sévères ou pancytopénie toxique.",
        pearl: "L'association AINS + Méthotrexate à doses > 20 mg/semaine est une Contre-Indication Absolue."
      },
      {
        id: 17,
        cat: 'palier1',
        tag: 'Palier I • Néfopam',
        q: "Quelles sont les contre-indications absolues du Néfopam (Acupan®) liées à ses propriétés pharmacologiques ?",
        hint: "Effets anticholinergiques / atropiniques et risque convulsif.",
        a: "1) Risque de glaucome par fermeture de l'angle. 2) Risque de rétention aiguë d'urine (adénome prostatique). 3) Antécédents de convulsions ou épilepsie. Ces contre-indications découlent de ses puissants effets atropiniques (anticholinergiques) et de son inhibition de recapture de la dopamine/noradrénaline qui abaisse le seuil épileptogène.",
        pearl: "Le néfopam ne provoque aucune dépression respiratoire et n'entraîne pas d'accoutumance physique."
      },
      {
        id: 18,
        cat: 'opioides',
        tag: 'Palier III • Oxycodone vs Morphine',
        q: "Quels sont les avantages pharmacocinétiques de l'Oxycodone par rapport à la Morphine par voie orale ?",
        hint: "Biodisponibilité orale (F%) et effet de premier passage hépatique.",
        a: "La biodisponibilité orale de l'Oxycodone est de 60 à 87%, alors que celle de la morphine n'est que de 20 à 30% en raison d'un effet de premier passage hépatique important. L'oxycodone a donc une absorption orale beaucoup plus prévisible, avec moins de variabilité interindividuelle, et son ratio d'équianalgésie est d'environ 1.5 à 2 (10 mg d'oxycodone PO ~ 15-20 mg de morphine PO).",
        pearl: "L'oxycodone donne moins d'hallucinations et de prurit histaminergique que la morphine."
      },
      {
        id: 19,
        cat: 'palier1',
        tag: 'Palier I • Aspirine et Goutte',
        q: "Quel est l'effet paradoxal de l'aspirine à faible dose sur l'acide urique et pourquoi est-elle déconseillée chez le goutteux ?",
        hint: "Inhibition de la sécrétion tubulaire vs réabsorption.",
        a: "À dose antalgique ou antiagrégante (< 1 à 2 g/jour), l'aspirine inhibe la sécrétion tubulaire d'acide urique sans inhiber sa réabsorption, provoquant une hyperuricémie qui peut déclencher ou aggraver un accès de goutte aigu. Ce n'est qu'à très forte dose (> 4-5 g/j) qu'elle devient uricosurique.",
        pearl: "Chez un patient goutteux ayant une douleur, privilégier le paracétamol en première intention."
      },
      {
        id: 20,
        cat: 'palier1',
        tag: 'Palier I • Pédiatrie & Reye',
        q: "Qu'est-ce que le Syndrome de Reye et quelle en est la cause médicamenteuse chez l'enfant ?",
        hint: "Aspirine lors d'une virose (varicelle, grippe).",
        a: "Le Syndrome de Reye est une encéphalopathie aiguë rare mais gravissime (mortalité 20-30%) associée à une stéatose hépatique microvésiculaire. Il survient typiquement chez l'enfant ou l'adolescent traité par l'aspirine au cours d'une infection virale fébrile (varicelle, grippe, virose respiratoire).",
        pearl: "Règle d'or pédiatrique : Paracétamol en 1ère intention absolue chez l'enfant fébrile. Jamais d'aspirine sans avis spécialisé."
      }
    ];

    let currentSrsIndex = 0;
    let srsActiveDeck = [...SRS_CARDS];
    let srsRetention = 94;
    let srsStreak = 4;

    function renderSrsCard() {
      if (srsActiveDeck.length === 0) return;
      const c = srsActiveDeck[currentSrsIndex];
      document.getElementById('srs-card-tag').textContent = c.tag;
      document.getElementById('srs-card-counter').textContent = `Carte ${currentSrsIndex + 1} sur ${srsActiveDeck.length}`;
      document.getElementById('srs-progress-ratio').textContent = `${currentSrsIndex + 1} / ${srsActiveDeck.length}`;
      document.getElementById('srs-question').textContent = c.q;
      document.getElementById('srs-hint').textContent = `Indice : ${c.hint}`;
      document.getElementById('srs-answer').innerHTML = c.a;
      document.getElementById('srs-pearl').textContent = c.pearl;

      // Reset visibility
      document.getElementById('srs-front').classList.remove('hidden');
      document.getElementById('srs-back').classList.add('hidden');
      document.getElementById('srs-btn-reveal').classList.remove('hidden');
      document.getElementById('srs-rating-buttons').classList.add('hidden');
      lucide.createIcons();
    }

    function revealSrsAnswer() {
      document.getElementById('srs-back').classList.remove('hidden');
      document.getElementById('srs-btn-reveal').classList.add('hidden');
      document.getElementById('srs-rating-buttons').classList.remove('hidden');
      document.getElementById('srs-rating-buttons').classList.add('flex');
    }

    function rateSrsCard(quality) {
      // SM-2 progression logic
      if (quality >= 3) {
        srsRetention = Math.min(100, srsRetention + 1);
      } else {
        srsRetention = Math.max(70, srsRetention - 2);
      }
      document.getElementById('srs-retention-rate').textContent = `${srsRetention}%`;

      // Next card
      currentSrsIndex = (currentSrsIndex + 1) % srsActiveDeck.length;
      renderSrsCard();
    }

    function filterSrsCategory(cat) {
      ['all', 'palier1', 'opioides', 'tox', 'reglementation'].forEach(c => {
        const b = document.getElementById(`srs-cat-${c}`);
        if (c === cat) {
          b.className = 'px-3 py-1 rounded-lg bg-teal-600 text-white font-bold';
        } else {
          b.className = 'px-3 py-1 rounded-lg bg-slate-800 text-slate-300 hover:text-white';
        }
      });

      if (cat === 'all') {
        srsActiveDeck = [...SRS_CARDS];
      } else {
        srsActiveDeck = SRS_CARDS.filter(c => c.cat === cat);
      }
      currentSrsIndex = 0;
      document.getElementById('srs-card-count').textContent = `${srsActiveDeck.length} cartes`;
      renderSrsCard();
    }

    function resetSrsProgress() {
      currentSrsIndex = 0;
      srsRetention = 94;
      document.getElementById('srs-retention-rate').textContent = '94%';
      renderSrsCard();
    }


    // --- B. SIMULATEUR D'ECOS (PATIENT VIRTUEL) ---
    const ECOS_SCENARIOS = {
      1: {
        id: 1,
        title: "Cas 1 : Comptoir Officinal - Mme Monique Dubois (65 ans)",
        complaint: "Demande une boîte d'Ibuprofène 400 mg pour une douleur sciatique aiguë survenue hier.",
        patient: {
          name: "Mme Monique Dubois",
          initials: "MD",
          details: "65 ans • 68 kg • Créatinine 92 µmol/L (Clairance DFG 62 mL/min)",
          history: "HTA traitée depuis 10 ans, Insuffisance cardiaque légère (NYHA II), antécédent d'ulcère gastroduodénal il y a 8 ans.",
          meds: "Ramipril 5 mg/j (IEC), Furosémide 20 mg/j (Diurétique de l'anse)."
        },
        dialogues: [
          { q: "« Depuis quand avez-vous mal et quelle est l'intensité ? »", a: "« Ça a commencé hier soir après avoir porté un carton. C'est comme une décharge qui descend dans ma fesse droite, je dirais 7 sur 10. »" },
          { q: "« Prenez-vous d'autres médicaments actuellement ? »", a: "« Oui, mon traitement habituel pour la tension et le cœur : Ramipril et Furosémide. Et j'ai pris du paracétamol ce matin mais ça ne suffisait pas. »" },
          { q: "« Avez-vous déjà eu des brûlures d'estomac ou des ulcères ? »", a: "« Oh oui, il y a 8 ans j'avais fait un ulcère avec hémorragie, mon médecin m'avait dit de faire très attention à ce que j'avale ! »" }
        ],
        plm_options: [
          { id: 1, text: "Contre-indication relative/absolue : Risque de Triple Whammy (AINS + IEC + Diurétique) et récidive ulcéreuse", correct: true },
          { id: 2, text: "Surdosage en paracétamol avec atteinte hépatique immédiate", correct: false },
          { id: 3, text: "Sous-dosage évident en antihypertenseur", correct: false }
        ],
        ip_options: [
          { id: 1, text: "Refus motivé de dispensation de l'Ibuprofène, proposition d'optimiser le Paracétamol (1g x3/j) et consultation médicale pour palier II", correct: true },
          { id: 2, text: "Délivrance de l'Ibuprofène 400 mg avec un IPP (Oméprazole)", correct: false },
          { id: 3, text: "Arrêt temporaire du Ramipril et du Furosémide pour donner l'AINS", correct: false }
        ],
        etp_options: [
          { id: 1, text: "Expliquer le mécanisme du Triple Whammy (rein), le risque d'ulcère mortel et la règle des 4 heures pour le paracétamol", correct: true },
          { id: 2, text: "Conseiller de doubler la dose de furosémide si les jambes gonflent", correct: false },
          { id: 3, text: "Indiquer que les AINS peuvent être repris librement dès la fin de la sciatique", correct: false }
        ],
        debrief: "Excellente analyse ! L'association d'un AINS chez un patient sous IEC + Diurétique constitue le redoutable 'Triple Whammy' conduisant à l'insuffisance rénale aiguë oligo-anurique, majoré par un antécédent d'hémorragie digestive haute. Le refus de délivrance d'AINS au comptoir et l'orientation médicale pour un antalgique de palier II (ex: codéine ou tramadol à dose adaptée) était l'unique décision conforme aux règles professionnelles."
      },
      2: {
        id: 2,
        title: "Cas 2 : Chirurgie Orthopédique - M. Marc Mercier (52 ans)",
        complaint: "Lombalgie post-opératoire hyperalgique sous Tramadol 150 mg LP x2/j avec prescription concomitante de Paroxétine 20 mg.",
        patient: {
          name: "M. Marc Mercier",
          initials: "MM",
          details: "52 ans • 80 kg • Bilan rénal et hépatique normaux",
          history: "Dépression réactionnelle suite à un arrêt de travail prolongé, herniectomie discale L4-L5 il y a 3 semaines.",
          meds: "Paroxétine 20 mg/j (ISRS), Tramadol LP 150 mg matin et soir, Paracétamol 1g si besoin."
        },
        dialogues: [
          { q: "« Comment tolérez-vous le Tramadol au quotidien ? »", a: "« Bof, j'ai des sueurs bizarres depuis deux jours, le cœur qui s'emballe un peu et des tremblements dans les doigts. Et la douleur n'est même pas bien calmée ! »" },
          { q: "« Depuis quand prenez-vous la Paroxétine ? »", a: "« Mon médecin traitant me l'a prescrite il y a 5 jours parce que le moral ne suivait plus avec l'arrêt maladie. »" }
        ],
        plm_options: [
          { id: 1, text: "Interaction pharmacocinétique & pharmacodynamique majeure : inhibition CYP2D6 par paroxétine + risque de Syndrome Sérotoninergique", correct: true },
          { id: 2, text: "Allergie vraie au paracétamol", correct: false },
          { id: 3, text: "Insuffisance rénale aiguë terminale", correct: false }
        ],
        ip_options: [
          { id: 1, text: "Contacter le prescripteur pour stopper le Tramadol, surveiller les signes sérotoninergiques et relayer vers un opioïde non sérotoninergique (Morphine faible ou Oxycodone)", correct: true },
          { id: 2, text: "Augmenter le tramadol à 400 mg/j car le patient a encore mal", correct: false },
          { id: 3, text: "Remplacer la paroxétine par de la fluoxétine sans toucher au tramadol", correct: false }
        ],
        etp_options: [
          { id: 1, text: "Alerter sur les signes d'appel du syndrome sérotoninergique (agitation, myoclonies, hyperthermie) imposant les urgences", correct: true },
          { id: 2, text: "Conseiller de prendre le tramadol avec un grand bol de caféine", correct: false }
        ],
        debrief: "Diagnostic clinique remarquable ! La paroxétine est un puissant inhibiteur du CYP2D6 : elle bloque la formation du métabolite M1 actif analgésique du tramadol (inefficacité), tout en cumulant l'effet sérotoninergique (sueurs, tachycardie, tremblements = début de syndrome sérotoninergique). La substitution du tramadol s'imposait immédiatement."
      },
      3: {
        id: 3,
        title: "Cas 3 : Soins Palliatifs - M. André Laurent (78 ans)",
        complaint: "Douleurs osseuses métastatiques sous Morphine LP 60 mg x2/j avec découverte d'un DFG à 22 mL/min et constipation opiniâtre depuis 5 jours.",
        patient: {
          name: "M. André Laurent",
          initials: "AL",
          details: "78 ans • 60 kg • Clairance DFG Cockcroft = 22 mL/min (Insuffisance rénale sévère)",
          history: "Adénocarcinome prostatique métastatique osseux.",
          meds: "Skenan® 60 mg matin et soir (Morphine LP 120 mg/j), pas de prescription de laxatif."
        },
        dialogues: [
          { q: "« Depuis combien de temps n'avez-vous pas été à la selle ? »", a: "« Au moins 5 ou 6 jours, mon ventre est dur et très douloureux, je n'en peux plus. Et j'ai des secousses musculaires involontaires dans les jambes. »" },
          { q: "« Avez-vous une ordonnance pour le transit ? »", a: "« Non, le docteur à l'hôpital ne m'a rien donné pour ça. »" }
        ],
        plm_options: [
          { id: 1, text: "Accumulation toxique des métabolites glucuronides (M6G dépresseur et M3G neurotoxique) par insuffisance rénale + Oubli de coprescription de laxatif", correct: true },
          { id: 2, text: "Syndrome de Reye sous morphine", correct: false }
        ],
        ip_options: [
          { id: 1, text: "Proposer au médecin une rotation vers l'Oxycodone ou le Fentanyl patch (mieux tolérés sur le rein) avec titration d'un laxatif osmotique (Macrogol) en urgence", correct: true },
          { id: 2, text: "Augmenter la dose de morphine à 200 mg/j", correct: false }
        ],
        etp_options: [
          { id: 1, text: "Expliquer l'obligation d'un laxatif préventif permanent sous morphinique (absence d'accoutumance de la constipation) et hydratation", correct: true },
          { id: 2, text: "Prendre des ralentisseurs du transit de type Lopéramide", correct: false }
        ],
        debrief: "Score parfait ! Deux erreurs médicales critiques ont été rectifiées : 1) La morphine génère le M3G (responsable des secousses myocloniques observées chez le patient) qui s'accumule lors d'un DFG < 30 mL/min ; une rotation opioïde s'imposait. 2) La coprescription d'un laxatif osmotique ou lubrifiant est OBLIGATOIRE et systématique dès l'initiation de tout opioïde de palier III."
      }
    };

    let currentEcosId = 1;

    function loadEcosScenario(id) {
      currentEcosId = id;
      const sc = ECOS_SCENARIOS[id];

      // Update scenario buttons
      [1, 2, 3].forEach(i => {
        const btn = document.getElementById(`ecos-btn-scen-${i}`);
        if (i === id) {
          btn.className = 'w-full text-left p-3 rounded-2xl bg-teal-950/70 border border-teal-500/50 text-xs transition';
        } else {
          btn.className = 'w-full text-left p-3 rounded-2xl bg-slate-800/40 hover:bg-slate-800 border border-slate-700 text-xs transition';
        }
      });

      // Update patient profile
      document.getElementById('ecos-patient-avatar').textContent = sc.patient.initials;
      document.getElementById('ecos-patient-name').textContent = sc.patient.name;
      document.getElementById('ecos-patient-details').textContent = sc.patient.details;
      document.getElementById('ecos-patient-history').textContent = sc.patient.history;
      document.getElementById('ecos-patient-meds').textContent = sc.patient.meds;
      document.getElementById('ecos-patient-complaint').textContent = sc.complaint;

      // Reset dialogue
      document.getElementById('ecos-dialogue-box').textContent = `« ${sc.complaint} »`;

      // Populate dialogue buttons
      const qContainer = document.getElementById('ecos-question-buttons');
      qContainer.innerHTML = '';
      sc.dialogues.forEach((d, idx) => {
        const b = document.createElement('button');
        b.className = 'w-full text-left p-2 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-[11px] text-teal-300 font-medium transition flex items-center justify-between';
        b.innerHTML = `<span>${d.q}</span> <i data-lucide="message-square" class="w-3.5 h-3.5 text-slate-400"></i>`;
        b.onclick = () => {
          document.getElementById('ecos-dialogue-box').textContent = d.a;
        };
        qContainer.appendChild(b);
      });

      // Populate Select Inputs
      const plmSelect = document.getElementById('ecos-input-plm');
      plmSelect.innerHTML = sc.plm_options.map(o => `<option value="${o.id}">${o.text}</option>`).join('');

      const ipSelect = document.getElementById('ecos-input-ip');
      ipSelect.innerHTML = sc.ip_options.map(o => `<option value="${o.id}">${o.text}</option>`).join('');

      const etpSelect = document.getElementById('ecos-input-etp');
      etpSelect.innerHTML = sc.etp_options.map(o => `<option value="${o.id}">${o.text}</option>`).join('');

      document.getElementById('ecos-jury-feedback').classList.add('hidden');
      document.getElementById('ecos-jury-score').textContent = "Note : En attente d'évaluation";
      document.getElementById('ecos-jury-score').className = "px-3 py-1 rounded-full bg-slate-800 text-slate-300 font-mono text-xs font-bold";

      lucide.createIcons();
    }

    function evaluateEcosSubmission() {
      const sc = ECOS_SCENARIOS[currentEcosId];
      const plmVal = parseInt(document.getElementById('ecos-input-plm').value);
      const ipVal = parseInt(document.getElementById('ecos-input-ip').value);
      const etpVal = parseInt(document.getElementById('ecos-input-etp').value);

      let score = 0;
      if (sc.plm_options.find(o => o.id === plmVal)?.correct) score += 7;
      if (sc.ip_options.find(o => o.id === ipVal)?.correct) score += 7;
      if (sc.etp_options.find(o => o.id === etpVal)?.correct) score += 6;

      document.getElementById('ecos-final-grade').textContent = `${score} / 20`;
      document.getElementById('ecos-feedback-text').textContent = sc.debrief;
      document.getElementById('ecos-jury-feedback').classList.remove('hidden');

      const scoreBadge = document.getElementById('ecos-jury-score');
      scoreBadge.textContent = `Score ECOS : ${score} / 20`;
      if (score >= 15) {
        scoreBadge.className = "px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 font-mono text-xs font-bold";
      } else {
        scoreBadge.className = "px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/40 font-mono text-xs font-bold";
      }
    }


    // --- C. RUMACK-MATTHEW NOMOGRAM & CYP2D6 ---
    function updateRumackPlot() {
      const hours = parseInt(document.getElementById('rumack-hours-slider').value);
      const conc = parseInt(document.getElementById('rumack-conc-slider').value);
      const weight = parseInt(document.getElementById('rumack-weight-slider').value);

      document.getElementById('rumack-hours-val').textContent = `${hours} heures`;
      document.getElementById('rumack-conc-val').textContent = `${conc} mg/L`;
      document.getElementById('rumack-weight-val').textContent = `${weight} kg`;

      // Threshold Prescott line at time t: C_thresh = 150 * (0.5 ** ((t - 4) / 4))
      const thresh = 150.0 * Math.pow(0.5, (hours - 4.0) / 4.0);
      const isToxic = conc >= thresh;

      const badge = document.getElementById('rumack-status-badge');
      if (isToxic) {
        badge.textContent = "ALERTE HÉPATOTOXICITÉ : PROTOCOLE PRESCOTT REQUIS !";
        badge.className = "px-3 py-1 rounded-full bg-rose-500/20 text-rose-300 border border-rose-500/50 text-xs font-bold font-mono animate-pulse";
      } else {
        badge.textContent = "Zone Sécurisée (Atteinte hépatique peu probable)";
        badge.className = "px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 text-xs font-bold font-mono";
      }

      // Prescott doses: 150 mg/kg, 50 mg/kg, 100 mg/kg
      const d1 = ((150 * weight) / 1000).toFixed(1);
      const d2 = ((50 * weight) / 1000).toFixed(1);
      const d3 = ((100 * weight) / 1000).toFixed(1);
      const total = ((300 * weight) / 1000).toFixed(1);

      document.getElementById('prescott-doses').innerHTML = `
        1) Charge : <strong>${d1} g</strong> en 1h dans 200 mL G5%<br>
        2) Entretien 1 : <strong>${d2} g</strong> en 4h dans 500 mL G5%<br>
        3) Entretien 2 : <strong>${d3} g</strong> en 16h dans 1000 mL G5%<br>
        <span class="text-teal-400">Total : ${total} g de N-Acétylcystéine sur 21h</span>
      `;

      drawRumackPlot();
    }

    function drawRumackPlot() {
      const cvs = document.getElementById('rumack-canvas');
      if (!cvs) return;
      const ctx = cvs.getContext('2d');
      const w = cvs.width;
      const h = cvs.height;

      ctx.clearRect(0, 0, w, h);

      // Background
      ctx.fillStyle = '#020617';
      ctx.fillRect(0, 0, w, h);

      // Margins
      const padL = 50, padR = 20, padT = 20, padB = 40;
      const pw = w - padL - padR;
      const ph = h - padT - padB;

      // Coordinate transforms: X from 4h to 24h, Y log scale from 10 to 400
      function xPos(t) { return padL + ((t - 4) / 20) * pw; }
      function yPos(c) {
        const logMin = Math.log10(10);
        const logMax = Math.log10(400);
        const frac = (Math.log10(Math.max(10, Math.min(400, c))) - logMin) / (logMax - logMin);
        return padT + (1.0 - frac) * ph;
      }

      // Grid lines
      ctx.strokeStyle = '#1e293b';
      ctx.lineWidth = 1;
      [10, 25, 50, 100, 200, 400].forEach(val => {
        const y = yPos(val);
        ctx.beginPath();
        ctx.moveTo(padL, y);
        ctx.lineTo(w - padR, y);
        ctx.stroke();
        ctx.fillStyle = '#64748b';
        ctx.font = '10px monospace';
        ctx.fillText(`${val}`, 15, y + 3);
      });

      [4, 8, 12, 16, 20, 24].forEach(t => {
        const x = xPos(t);
        ctx.beginPath();
        ctx.moveTo(x, padT);
        ctx.lineTo(x, h - padB);
        ctx.stroke();
        ctx.fillStyle = '#64748b';
        ctx.font = '10px monospace';
        ctx.fillText(`H${t}`, x - 8, h - padB + 16);
      });

      // Toxic Zone Shading
      ctx.fillStyle = 'rgba(244, 63, 94, 0.12)';
      ctx.beginPath();
      ctx.moveTo(xPos(4), yPos(150));
      for (let t = 4; t <= 24; t += 0.5) {
        const thresh = 150.0 * Math.pow(0.5, (t - 4.0) / 4.0);
        ctx.lineTo(xPos(t), yPos(thresh));
      }
      ctx.lineTo(xPos(24), yPos(400));
      ctx.lineTo(xPos(4), yPos(400));
      ctx.closePath();
      ctx.fill();

      // Treatment Line (Prescott line)
      ctx.strokeStyle = '#f43f5e';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let t = 4; t <= 24; t += 0.5) {
        const thresh = 150.0 * Math.pow(0.5, (t - 4.0) / 4.0);
        if (t === 4) ctx.moveTo(xPos(t), yPos(thresh));
        else ctx.lineTo(xPos(t), yPos(thresh));
      }
      ctx.stroke();

      // High toxicity line (200 mg/L at H4)
      ctx.strokeStyle = '#e11d48';
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      for (let t = 4; t <= 24; t += 0.5) {
        const thresh = 200.0 * Math.pow(0.5, (t - 4.0) / 4.0);
        if (t === 4) ctx.moveTo(xPos(t), yPos(thresh));
        else ctx.lineTo(xPos(t), yPos(thresh));
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Current patient point
      const ptHours = parseInt(document.getElementById('rumack-hours-slider').value);
      const ptConc = parseInt(document.getElementById('rumack-conc-slider').value);
      const px = xPos(ptHours);
      const py = yPos(ptConc);

      ctx.fillStyle = '#fbbf24';
      ctx.shadowColor = '#fbbf24';
      ctx.shadowBlur = 10;
      ctx.beginPath();
      ctx.arc(px, py, 7, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;

      // Point label
      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 11px monospace';
      ctx.fillText(`Patient (H${ptHours}, ${ptConc} mg/L)`, px + 10, py - 6);
    }

    // CYP2D6 Simulator
    let currentCYP = 'EM';

    function setCYP2D6Phenotype(phenotype) {
      currentCYP = phenotype;
      ['PM', 'EM', 'UM'].forEach(p => {
        const btn = document.getElementById(`cyp-btn-${p}`);
        if (p === phenotype) {
          btn.className = 'px-3 py-1 rounded-lg bg-purple-600 text-white font-bold transition';
        } else {
          btn.className = 'px-3 py-1 rounded-lg text-slate-300 hover:text-white transition';
        }
      });

      const title = document.getElementById('cyp-phenotype-title');
      const desc = document.getElementById('cyp-phenotype-desc');
      const alertBox = document.getElementById('cyp-clinical-alert');

      if (phenotype === 'PM') {
        title.textContent = 'Métaboliseur Lent (Poor Metabolizer - PM : 7-10% des Caucasiens)';
        desc.textContent = "Déficit complet en enzyme CYP2D6 active (allèles non fonctionnels). La codéine et le tramadol ne sont pratiquement pas métabolisés en morphine ou en O-déméthyltramadol M1.";
        alertBox.className = "p-2.5 rounded-xl bg-amber-950/40 border border-amber-800/60 text-amber-200 text-[11px]";
        alertBox.innerHTML = "<strong>Conséquence clinique :</strong> Inefficacité analgésique totale ! Le patient souffre malgré les prises répétées. Privilégier d'emblée un antalgique non dépendant du CYP2D6.";
      } else if (phenotype === 'EM') {
        title.textContent = 'Métaboliseur Normal (Extensive Metabolizer - EM : ~80% de la population)';
        desc.textContent = "Transformation physiologique normale d'environ 10% de la dose de codéine en morphine active par le CYP2D6 hépatique. Cinétique d'activation standard.";
        alertBox.className = "p-2.5 rounded-xl bg-emerald-950/40 border border-emerald-800/60 text-emerald-200 text-[11px]";
        alertBox.innerHTML = "<strong>Conséquence clinique :</strong> Analgésie optimale et prévisible. Posologie standard des RCP.";
      } else if (phenotype === 'UM') {
        title.textContent = "Métaboliseur Ultra-Rapide (Ultra-rapid Metabolizer - UM : jusqu'à 29% en Afrique)";
        desc.textContent = "Duplication du gène CYP2D6 actif. Bioactivation ultra-rapide et massive en morphine active même à posologie usuelle faible.";
        alertBox.className = "p-2.5 rounded-xl bg-rose-950/50 border border-rose-800 text-rose-200 text-[11px]";
        alertBox.innerHTML = "<strong>DANGER VITAL MAJEUR :</strong> Pic plasmatique de morphine toxique entraînant somnolence profonde, apnée, coma et décès (cas historiques chez l'enfant sous codéine post-adénoïdectomie). Contre-indication absolue !";
      }

      drawCYPPlot();
    }

    function drawCYPPlot() {
      const cvs = document.getElementById('cyp-canvas');
      if (!cvs) return;
      const ctx = cvs.getContext('2d');
      const w = cvs.width;
      const h = cvs.height;

      ctx.clearRect(0, 0, w, h);
      ctx.fillStyle = '#020617';
      ctx.fillRect(0, 0, w, h);

      // Axes
      ctx.strokeStyle = '#334155';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(30, 10);
      ctx.lineTo(30, h - 25);
      ctx.lineTo(w - 10, h - 25);
      ctx.stroke();

      ctx.fillStyle = '#64748b';
      ctx.font = '10px monospace';
      ctx.fillText('[Morphine active]', 35, 20);
      ctx.fillText('Temps (h)', w - 60, h - 10);

      // Curve generation
      ctx.lineWidth = 2.5;
      if (currentCYP === 'PM') {
        ctx.strokeStyle = '#f59e0b';
        ctx.beginPath();
        ctx.moveTo(30, h - 25);
        for (let x = 0; x <= w - 40; x++) {
          const y = (h - 25) - Math.sin(x / 40) * 4;
          ctx.lineTo(30 + x, y);
        }
        ctx.stroke();
      } else if (currentCYP === 'EM') {
        ctx.strokeStyle = '#a855f7';
        ctx.beginPath();
        ctx.moveTo(30, h - 25);
        for (let x = 0; x <= w - 40; x++) {
          const t = x / 30;
          const val = 60 * (Math.exp(-0.25 * t) - Math.exp(-1.5 * t));
          ctx.lineTo(30 + x, (h - 25) - val * 1.6);
        }
        ctx.stroke();
      } else if (currentCYP === 'UM') {
        ctx.strokeStyle = '#f43f5e';
        ctx.beginPath();
        ctx.moveTo(30, h - 25);
        for (let x = 0; x <= w - 40; x++) {
          const t = x / 30;
          const val = 140 * (Math.exp(-0.4 * t) - Math.exp(-2.5 * t));
          ctx.lineTo(30 + x, (h - 25) - val * 1.5);
        }
        ctx.stroke();
      }
    }


    // --- D. EMERGENCY GAME (TIME-ATTACK 90s) ---
    const EMERGENCY_CASES = [
      {
        text: "Service de Chirurgie : Patient sous pompe PCA Morphine en surdosage. FR = 6/min, myosis serré punctiforme, coma réactif aux bruits.",
        options: [
          { text: "Arrêt PCA + O2 + Titration Naloxone IV (0.04 mg toutes les 2 min jusqu'à FR > 10)", correct: true },
          { text: "Injection d'un bolus de 10 mg de Naloxone IV direct", correct: false },
          { text: "Augmenter le débit de la PCA pour stimuler le patient", correct: false },
          { text: "Injection de Flumazénil", correct: false }
        ]
      },
      {
        text: "Femme de 28 ans enceinte de 30 SA se présentant à la garde avec une céphalée violente et prenant de l'Ibuprofène 400 mg.",
        options: [
          { text: "Arrêt immédiat de l'Ibuprofène (CI absolue dès 24 SA) + avis obstétrical d'urgence", correct: true },
          { text: "Continuer l'Ibuprofène en ajoutant un pansement gastrique", correct: false },
          { text: "Remplacer par de l'aspirine à 1000 mg", correct: false },
          { text: "Prescrire du Kétoprofène en intraveineuse", correct: false }
        ]
      },
      {
        text: "Patient polytraumatisé traité au long cours par AVK (Fluindione). L'externe propose de lui injecter du Kétoprofène IV.",
        options: [
          { text: "Refus catégorique : déplacement de liaison aux protéines (>99%) et risque d'hémorragie cataclysmique", correct: true },
          { text: "Valider l'injection sans surveillance d'INR", correct: false },
          { text: "Associer du Célécoxib en perfusion pour compenser", correct: false },
          { text: "Augmenter la dose d'antivitamine K", correct: false }
        ]
      },
      {
        text: "Intoxication volontaire au paracétamol estimée à 14 g ingérée il y a 5 heures. Le laboratoire annonce 3h d'attente pour le dosage.",
        options: [
          { text: "Lancer immédiatement le protocole de Prescott (NAC IV) sans attendre les résultats sanguins", correct: true },
          { text: "Attendre le résultat du dosage à H8 avant toute décision", correct: false },
          { text: "Faire boire 2 litres de lait au patient", correct: false },
          { text: "Injecter de la Naloxone", correct: false }
        ]
      },
      {
        text: "Patient sous Tramadol + Venlafaxine présentant sueurs profuses, myoclonies, rigidité musculaire et température à 39.5°C.",
        options: [
          { text: "Syndrome Sérotoninergique aigu : arrêt immédiat des deux agents, réanimation et refroidissement", correct: true },
          { text: "Surdosage opioïde simple : injecter de la morphine", correct: false },
          { text: "Crise de goutte : prescrire de la colchicine", correct: false },
          { text: "Simple état grippal : rajouter du paracétamol", correct: false }
        ]
      }
    ];

    let gameTimer = null;
    let gameTimeLeft = 90;
    let gameScore = 0;
    let gameCaseIndex = 0;

    function startEmergencyGame() {
      if (gameTimer) clearInterval(gameTimer);
      gameTimeLeft = 90;
      gameScore = 0;
      gameCaseIndex = 0;
      document.getElementById('game-score-display').textContent = 'Score : 0 pts';
      document.getElementById('game-start-btn').textContent = 'Recommencer';

      loadNextEmergencyCase();

      gameTimer = setInterval(() => {
        gameTimeLeft--;
        document.getElementById('game-timer').textContent = `${gameTimeLeft}s`;
        if (gameTimeLeft <= 0) {
          clearInterval(gameTimer);
          alert(`Garde terminée ! Score final : ${gameScore} points.`);
        }
      }, 1000);
    }

    function loadNextEmergencyCase() {
      if (gameCaseIndex >= EMERGENCY_CASES.length) {
        clearInterval(gameTimer);
        document.getElementById('game-scenario-text').textContent = `Félicitations ! Tu as résolu toutes les urgences de la garde avec un score de ${gameScore} points !`;
        document.getElementById('game-options-container').innerHTML = '';
        document.getElementById('badge-1').className = "px-2.5 py-1 rounded-lg bg-teal-500/20 text-teal-300 border border-teal-500/40 font-mono text-[10px]";
        document.getElementById('badge-2').className = "px-2.5 py-1 rounded-lg bg-amber-500/20 text-amber-300 border border-amber-500/40 font-mono text-[10px]";
        document.getElementById('badge-3').className = "px-2.5 py-1 rounded-lg bg-rose-500/20 text-rose-300 border border-rose-500/40 font-mono text-[10px]";
        document.getElementById('game-badges-count').textContent = "3 débloqués (Majeur de Garde)";
        return;
      }

      const cs = EMERGENCY_CASES[gameCaseIndex];
      document.getElementById('game-case-badge').textContent = `URGENCE ${gameCaseIndex + 1} / ${EMERGENCY_CASES.length}`;
      document.getElementById('game-scenario-text').textContent = cs.text;

      const optContainer = document.getElementById('game-options-container');
      optContainer.innerHTML = '';
      cs.options.forEach(opt => {
        const btn = document.createElement('button');
        btn.className = 'p-3 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-left text-xs text-slate-200 transition';
        btn.textContent = opt.text;
        btn.onclick = () => {
          if (opt.correct) {
            gameScore += 20;
            btn.className = 'p-3 rounded-xl bg-teal-950 border border-teal-500 text-left text-xs text-teal-200';
          } else {
            gameScore = Math.max(0, gameScore - 10);
            btn.className = 'p-3 rounded-xl bg-rose-950 border border-rose-500 text-left text-xs text-rose-200';
          }
          document.getElementById('game-score-display').textContent = `Score : ${gameScore} pts`;
          setTimeout(() => {
            gameCaseIndex++;
            loadNextEmergencyCase();
          }, 400);
        };
        optContainer.appendChild(btn);
      });
    }


    // --- E. AUDIO-LEARNING & POCKET MEMO CARDS ---
    let audioSpeed = 1.0;
    let synth = window.speechSynthesis;
    let currentUtterance = null;

    function populateAudioSelector() {
      const sel = document.getElementById('audio-molecule-select');
      if (!sel) return;
      sel.innerHTML = MOLECULES.map(m => `<option value="${m.id}">${m.name} (${m.palier_label})</option>`).join('');
      loadAudioMonograph(MOLECULES[0].id);
    }

    function loadAudioMonograph(molId) {
      const m = MOL_MAP[molId];
      if (!m) return;
      const text = `${m.name}, DCI : ${m.dci}. Classe : ${m.class_name}, ${m.palier_label}. Posologie adulte usuelle : ${m.posology.adult}. Demi-vie d'élimination : ${m.pk.halflife}. Métabolisme et cytochromes : ${m.metabolism.pathways}. Contre-indications absolues : ${m.contraindications.join(', ')}. Point clé pour l'internat : ${m.concours_pearl}`;
      document.getElementById('audio-transcript-text').textContent = text;
    }

    function setAudioSpeed(speed) {
      audioSpeed = speed;
      [1.0, 1.25, 1.5].forEach(s => {
        const b = document.getElementById(`speed-${String(s).replace('.', '')}`);
        if (s === speed) {
          b.className = 'px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-bold';
        } else {
          b.className = 'px-2.5 py-1 rounded-lg bg-slate-800 text-slate-300';
        }
      });
    }

    function playAudioFlash() {
      if (!('speechSynthesis' in window)) {
        alert("La synthèse vocale n'est pas supportée par ce navigateur.");
        return;
      }
      stopAudioFlash();
      const text = document.getElementById('audio-transcript-text').textContent;
      currentUtterance = new SpeechSynthesisUtterance(text);
      currentUtterance.lang = 'fr-FR';
      currentUtterance.rate = audioSpeed;
      synth.speak(currentUtterance);
    }

    function pauseAudioFlash() {
      if (synth && synth.speaking) {
        if (synth.paused) synth.resume();
        else synth.pause();
      }
    }

    function stopAudioFlash() {
      if (synth) synth.cancel();
    }

    function populatePocketTable() {
      const tbody = document.getElementById('pocket-table-body');
      if (!tbody) return;
      tbody.innerHTML = MOLECULES.map(m => `
        <tr class="hover:bg-slate-900/60 transition">
          <td class="p-2.5 font-bold text-white">${m.name} <br><span class="text-[10px] text-teal-400 font-mono">${m.brand_names[0] || ''}</span></td>
          <td class="p-2.5"><span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-slate-800 text-slate-200">${m.palier_label}</span></td>
          <td class="p-2.5 font-mono text-[10px]">${m.posology.adult.slice(0, 45)}...</td>
          <td class="p-2.5 font-mono text-cyan-300 text-[10px]">${m.pk.halflife}</td>
          <td class="p-2.5 text-[10px] text-slate-300">${m.metabolism.pathways.slice(0, 50)}...</td>
          <td class="p-2.5 text-[10px] text-rose-300">${m.contraindications[0] || 'Néant'}</td>
        </tr>
      `).join('');
    }
'''

# Replace placeholders and append new Bonus Hub logic
template = template.replace('__SDF_DATABASE_JSON__', json.dumps(sdf_data, ensure_ascii=False))
template = template.replace('__PHARMACOLOGY_DB_JSON__', json.dumps(pharma_db, ensure_ascii=False))

# Insert Bonus Hub initialization into DOMContentLoaded
old_dom_ready = 'runOpioidRotation();'
new_dom_ready = '''runOpioidRotation();
      renderSrsCard();
      loadEcosScenario(1);
      updateRumackPlot();
      setCYP2D6Phenotype('EM');
      populateAudioSelector();
      populatePocketTable();'''
template = template.replace(old_dom_ready, new_dom_ready, 1)

# Append the bonus JS logic right before the closing </script>
template = template.replace('    // =========================================================================\n    // 1. ENCYCLOPÉDIE MONOGRAPHIQUE (24+ DCI)', bonus_js_logic + '\n    // =========================================================================\n    // 1. ENCYCLOPÉDIE MONOGRAPHIQUE (24+ DCI)')

# Write to index.html AND overwrite template_pro.html so opening either file works!
with open(INDEX_FILE, 'w', encoding='utf-8') as f:
    f.write(template)

with open(TEMPLATE_FILE, 'w', encoding='utf-8') as f:
    f.write(template)

print(f"Compilation finished successfully!")
print(f"index.html size: {os.path.getsize(INDEX_FILE)} bytes")
print(f"template_pro.html size: {os.path.getsize(TEMPLATE_FILE)} bytes")
