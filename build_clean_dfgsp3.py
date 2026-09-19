import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, 'data', 'pharmacology_db.json')
SDF1_FILE = os.path.join(BASE_DIR, 'sdf_data.json')
SDF2_FILE = os.path.join(BASE_DIR, 'sdf_opioids.json')
OUTPUT_FILE = os.path.join(BASE_DIR, 'index.html')

with open(DB_FILE, 'r', encoding='utf-8') as f:
    pharma_db = json.load(f)

with open(SDF1_FILE, 'r', encoding='utf-8') as f:
    sdf1 = json.load(f)

with open(SDF2_FILE, 'r', encoding='utf-8') as f:
    sdf2 = json.load(f)

all_sdfs = {**sdf1, **sdf2}

# 8 Clinical Cases
CLINICAL_CASES = [
    {
        "id": 1,
        "title": "Amina, 28 ans",
        "badge": "Grossesse & AINS",
        "context": "Grossesse 31 SA (3e trimestre) • Pulpite dentaire aiguë hyperalgique",
        "rx_patient": "Patiente : Amina B. (28 ans, Enceinte 31 SA)",
        "rx_lines": "• Ibuprofène 400 mg : 1 comprimé 3 fois par jour au cours des repas pendant 5 jours.",
        "pearl": "Même une prise unique d'AINS à partir du 6e mois de grossesse (24 SA) peut causer la fermeture irréversible in utero du canal artériel fœtal et une anurie fœtale (oligoamnios). Contre-indication formelle et absolue !",
        "options": [
            {
                "text": "A. Dispenser l'Ibuprofène 400 mg en conseillant de bien le prendre au cours d'un repas",
                "correct": False,
                "feedback": "🚨 ERREUR GRAVE / FAUTE MÉDICALE : Les AINS sont formellement contre-indiqués dès le début du 6e mois (24 SA). Risque d'insuffisance cardiaque droite fœtale par fermeture prématurée du canal artériel et d'anurie fœtale irréversible.",
                "status": "DANGER FŒTAL MAJEUR 🚨"
            },
            {
                "text": "B. Refuser la délivrance d'Ibuprofène, orienter vers le dentiste et proposer du Paracétamol 1g",
                "correct": True,
                "feedback": "✅ CONDUITE PARFAITE : Le paracétamol est l'antalgique de référence sécurisé pendant toute la grossesse (posologie usuelle 1g toutes les 6h, max 4g/j). Explication à la patiente et orientation vers les urgences dentaires.",
                "status": "PATIENTE & FŒTUS PROTÉGÉS ✅"
            }
        ]
    },
    {
        "id": 2,
        "title": "Gérard, 74 ans",
        "badge": "Triple Whammy Rénal",
        "context": "Hypertendu sous Ramipril (IEC) + Furosémide (Diurétique) • DFG de base : 45 mL/min",
        "rx_patient": "Patient : Gérard M. (74 ans, Insuffisant Rénal Modéré)",
        "rx_lines": "• Bi-Profénid (Kétoprofène LP) 150 mg : 1 comprimé matin et soir pendant 10 jours pour poussée d'arthrose.",
        "pearl": "Le 'Triple Whammy' : Diurétique (hypovolémie) + IEC (dilatation artériole efférente) + AINS (constriction artériole afférente) anéantit la pression d'ultrafiltration glomérulaire -> Insuffisance rénale aiguë oligo-anurique brutale.",
        "options": [
            {
                "text": "A. Valider l'ordonnance en conseillant de boire 1.5L d'eau par jour",
                "correct": False,
                "feedback": "🚨 DÉCOMPENSATION RÉNALE AIGUË : L'association Diurétique + IEC + AINS détruit l'autorégulation glomérulaire. Le DFG chute brutalement vers 10-15 mL/min avec risque d'hyperkaliémie mortelle.",
                "status": "INSUFFISANCE RÉNALE AIGUË 🚨"
            },
            {
                "text": "B. Refuser l'AINS oral, alerter le prescripteur sur le Triple Whammy et proposer Paracétamol ou AINS topique localisé",
                "correct": True,
                "feedback": "✅ RÉFLEXE DE SÉCURITÉ CLINIQUE : Vous évitez une hospitalisation d'urgence en néphrologie. Le médecin adaptera l'antalgie (paracétamol 3g/j max chez le sujet âgé, ou AINS topique sur le genou sans passage systémique significatif).",
                "status": "FONCTION RÉNALE PRÉSERVÉE ✅"
            }
        ]
    },
    {
        "id": 3,
        "title": "Thomas, 35 ans",
        "badge": "Tramadol & Sérotonine",
        "context": "Lombalgie chronique sous Tramadol 200 mg/j • Nouvelle ordonnance de Paroxétine (Deroxat®)",
        "rx_patient": "Patient : Thomas L. (35 ans, Douleur Rachidienne)",
        "rx_lines": "• Deroxat (Paroxétine) 20 mg : 1 comprimé le matin pour épisode dépressif caractérisé.",
        "pearl": "Double piège : 1) La paroxétine inhibe puissamment le CYP2D6, bloquant la conversion du tramadol en métabolite actif M1 (perte d'effet analgésique). 2) Sommation sérotoninergique -> Risque majeur de syndrome sérotoninergique.",
        "options": [
            {
                "text": "A. Dispenser les deux traitements sans avertissement particulier",
                "correct": False,
                "feedback": "🚨 RISQUE DE SYNDROME SÉROTONINERGIQUE : Hyperthermie, myoclonies, tremblements, sueurs profuses et perte totale d'efficacité analgésique du tramadol par inhibition du CYP2D6.",
                "status": "SYNDROME SÉROTONINERGIQUE 🚨"
            },
            {
                "text": "B. Contacter le médecin pour remplacer le Tramadol ou choisir un antidépresseur sans inhibition CYP2D6 (ex: Sertraline)",
                "correct": True,
                "feedback": "✅ EXCELLENTE INTERVENTION PHARMACEUTIQUE : Choix d'un antidépresseur sans interaction 2D6 ou bascule du tramadol vers un autre palier sous surveillance.",
                "status": "INTERACTION ÉVITÉE ✅"
            }
        ]
    },
    {
        "id": 4,
        "title": "Christian, 62 ans",
        "badge": "Morphine & Interdoses",
        "context": "Cancer avec métastases osseuses • Sous Morphine LP 60 mg matin et soir (120 mg/j)",
        "rx_patient": "Patient : Christian V. (62 ans, Suivi Oncologique)",
        "rx_lines": "• Skenan LP 60 mg : 1 gélule matin et soir.\n• Plainte : 3 crises de douleurs intolérables par nuit et constipation sévère depuis 6 jours.",
        "pearl": "Pour les accès douloureux paroxystiques (ADP), calculer l'interdose en Morphine LI selon la règle du 1/6e de la dose totale journalière (120 mg / 6 = 20 mg LI). Et coprescrire d'urgence un laxatif osmotique !",
        "options": [
            {
                "text": "A. Conseiller d'augmenter le Skenan LP à 120 mg le soir sans rien d'autre",
                "correct": False,
                "feedback": "❌ MAUVAISE PRATIQUE : On n'augmente pas la dose de fond LP sans avoir d'abord couvert les accès paroxystiques par des interdoses LI, et l'absence de laxatif expose au fécalome et à l'occlusion intestinale.",
                "status": "RISQUE D'OCCLUSION SUR FÉCALOME 🚨"
            },
            {
                "text": "B. Délivrer Actiskenan (Morphine LI) 20 mg pour les accès + Macrogol (laxatif osmotique systématique)",
                "correct": True,
                "feedback": "✅ PROTOCOLE ONCOLOGIQUE CONFORME : 1) Interdose de 20 mg LI (1/6e de 120 mg/j). 2) Traitement réflexe de la constipation induite par les opioïdes (aucun phénomène de tolérance sur le récepteur µ intestinal).",
                "status": "ANALGÉSIE COMPLÈTE & TRANSIT SÉCURISÉ ✅"
            }
        ]
    },
    {
        "id": 5,
        "title": "Sophie, 42 ans",
        "badge": "Lithium & AINS",
        "context": "Trouble bipolaire stabilisé sous Carbonate de Lithium (Téralithe® LP 400)",
        "rx_patient": "Patiente : Sophie D. (42 ans, Traitement Bipolaire)",
        "rx_lines": "• Kétoprofène 100 mg : 1 comprimé 3 fois par jour pour tendinite de l'épaule.",
        "pearl": "Les AINS diminuent la filtration glomérulaire et majorent la réabsorption tubulaire du lithium, provoquant un surdosage toxique avec tremblements, confusion et coma.",
        "options": [
            {
                "text": "A. Dispenser le Kétoprofène 100 mg en conseillant de boire beaucoup d'eau",
                "correct": False,
                "feedback": "🚨 SURDOSAGE TOXIQUE EN LITHIUM : Les AINS diminuent l'élimination rénale du lithium. La lithémie dépasse le seuil toxique (> 1.2 mEq/L) avec vertiges, encéphalopathie et défaillance rénale.",
                "status": "INTOXICATION AU LITHIUM 🚨"
            },
            {
                "text": "B. Refuser l'AINS oral, orienter vers le Paracétamol et prévenir le prescripteur",
                "correct": True,
                "feedback": "✅ SÉCURITÉ OFFICINALE : L'association AINS + Lithium est formellement déconseillée. En cas de nécessité absolue, une surveillance quotidienne étroite de la lithémie est requise.",
                "status": "LITHIÉMIE STABLE & SÉCURISÉE ✅"
            }
        ]
    },
    {
        "id": 6,
        "title": "Julien, 6 ans",
        "badge": "Varicelle & AINS",
        "context": "Varicelle fébrile avec vésicules cutanées prurigineuses (Fièvre 39.2°C)",
        "rx_patient": "Patient : Julien T. (6 ans, 21 kg)",
        "rx_lines": "• Demande de la maman au comptoir : « Donnez-moi de l'aspirine ou de l'ibuprofène pour faire chuter sa fièvre rapidement ! »",
        "pearl": "1) Risque mortel de Syndrome de Reye sous aspirine lors d'épisodes viraux. 2) Risque de fasciite nécrosante et surinfections bactériennes cutanées graves sous AINS en cas de varicelle.",
        "options": [
            {
                "text": "A. Conseiller un sirop d'ibuprofène (Advil pédiatrique) à la pipette kilo",
                "correct": False,
                "feedback": "🚨 ALERTE COMPLICATIONS BACTÉRIENNES NÉCROSANTES : En cas de varicelle, les AINS sont formellement contre-indiqués par l'ANSM en raison du risque de surinfections cutanées graves à streptocoque (fasciite nécrosante).",
                "status": "RISQUE DE FASCIITE NÉCROSANTE 🚨"
            },
            {
                "text": "B. Proscrire strictement l'Aspirine et les AINS, délivrer du Paracétamol pédiatrique à 15 mg/kg/prise",
                "correct": True,
                "feedback": "✅ CONSEIL PÉDIATRIQUE DE RÉFÉRENCE : Le paracétamol est l'unique antipyrétique sécurisé dans la varicelle (60 mg/kg/j en 4 prises). Pas de risque de syndrome de Reye ni de fasciite.",
                "status": "ENFANT PARFAITEMENT PROTÉGÉ ✅"
            }
        ]
    },
    {
        "id": 7,
        "title": "Patrick, 68 ans",
        "badge": "Douleur Neuropathique",
        "context": "Douleur neuropathique post-zostérienne (brûlures thoraciques, score DN4 = 6/10)",
        "rx_patient": "Patient : Patrick G. (68 ans, Névralgie post-zona)",
        "rx_lines": "• Doliprane 1000 mg 3x/j + Tramadol 50 mg 3x/j.\n• Patient : « Ça ne me soulage absolument rien du tout ! »",
        "pearl": "Les antalgiques conventionnels purs sont inefficaces sur les douleurs neuropathiques. L'introduction titrée d'un co-analgésique (Prégabaline, Gabapentine, Amitriptyline ou emplâtre de Lidocaïne) est indispensable.",
        "options": [
            {
                "text": "A. Proposer de doubler la dose de Tramadol à 100 mg 3 fois par jour",
                "correct": False,
                "feedback": "❌ ÉCHEC THÉRAPEUTIQUE : Augmenter les opioïdes sur une douleur neuropathique pure n'apporte que des effets indésirables (nausées, somnolence, constipation) sans analgésie significative.",
                "status": "ÉCHEC ANALGÉSIQUE & EFFETS INDÉSIRABLES ❌"
            },
            {
                "text": "B. Alerter le médecin sur la nature neuropathique (score DN4 ≥ 4) et proposer l'instauration de Prégabaline ou Gabapentine",
                "correct": True,
                "feedback": "✅ DIAGNOSTIC ET PRISE EN CHARGE ADAPTÉE : Les gabapentinoïdes bloquent la sous-unité alpha-2-delta des canaux calciques présynaptiques et calment l'hyperexcitabilité neuronale.",
                "status": "SOULAGEMENT NEUROPATHIQUE PROGRESSIF ✅"
            }
        ]
    },
    {
        "id": 8,
        "title": "Marie, 22 ans",
        "badge": "Intoxication Paracétamol",
        "context": "Intoxication aiguë volontaire au Paracétamol (15 grammes ingérés il y a 6 heures)",
        "rx_patient": "Patiente : Marie S. (22 ans, Admission Urgences)",
        "rx_lines": "• Bilan : Prise de 15g de Doliprane à 14h00. Arrivée aux urgences à 20h00.\n• La patiente dit : « Je me sens bien, j'ai juste un peu mal au ventre ».",
        "pearl": "Le piège de la phase quiescente (H0-H24) : Le patient intoxiqué se sent faussement bien alors que le NAPQI détruit insidieusement les hépatocytes. Mise en route immédiate du protocole de Prescott à la N-acétylcystéine (NAC) !",
        "options": [
            {
                "text": "A. Rassurer la patiente et la laisser rentrer car elle n'a aucun signe de gravité apparent",
                "correct": False,
                "feedback": "🚨 DÉCÈS PAR HÉPATITE FULMINANTE À H72 : À 6h de l'ingestion de 15g, les réserves hépatiques en glutathion sont épuisées. Sans antidote, la cytolyse centrolobulaire devient irréversible à H48.",
                "status": "HÉPATITE FULMINANTE MORTELLE 🚨"
            },
            {
                "text": "B. Dosage immédiat de la paracétamolémie et mise en route sans attendre de la N-acétylcystéine IV (Prescott)",
                "correct": True,
                "feedback": "✅ PROTOCOLE D'URGENCE VITAL : 150 mg/kg de NAC en 1h, puis 50 mg/kg en 4h, puis 100 mg/kg en 16h. Efficacité quasi-totale si débuté dans les 8 à 10 heures suivant l'ingestion.",
                "status": "FOIE ENTIÈREMENT SAUVÉ ✅"
            }
        ]
    }
]

# 15 High-Yield Flashcards
SRS_CARDS = [
    {
        "id": 1,
        "cat": "palier1",
        "tag": "Palier I • Aspirine",
        "q": "Pourquoi l'aspirine à faible dose (75 à 160 mg/j) possède-t-elle un effet antiagrégant durant 7 à 10 jours ?",
        "hint": "Type de liaison avec la COX-1 et particularité des plaquettes sanguines.",
        "a": "L'aspirine acétyle de façon irréversible et covalente la Sérine 529 de la COX-1 plaquettaire, bloquant définitivement la synthèse de Thromboxane A2 (TXA2). Comme les plaquettes sont anucléées, elles ne peuvent pas fabriquer de nouvelles enzymes : l'effet dure toute leur vie circulante (7 à 10 jours).",
        "pearl": "L'arrêt préopératoire de l'aspirine antiagrégante doit être planifié 5 à 7 jours avant une chirurgie à risque hémorragique."
    },
    {
        "id": 2,
        "cat": "palier1",
        "tag": "Palier I • Paracétamol",
        "q": "Quelle est la posologie pédiatrique stricte du paracétamol et quel est le risque en cas d'erreur de calcul ?",
        "hint": "Dose en mg/kg/jour et fractionnement des prises.",
        "a": "Strictement 60 mg/kg/jour répartis en 4 à 6 prises, soit 15 mg/kg toutes les 6 heures (ou 10 mg/kg toutes les 4h). Ne jamais dépasser 15 mg/kg par prise ni 4 g/jour. Risque majeur d'hépatite fulminante par accumulation de NAPQI.",
        "pearl": "Toujours utiliser la pipette doseuse graduée en kg fournie avec le flacon."
    },
    {
        "id": 3,
        "cat": "tox",
        "tag": "Toxicologie • Paracétamol",
        "q": "Quel est le métabolite hépatotoxique du paracétamol, comment est-il détoxifié à dose usuelle et que se passe-t-il en cas de surdosage ?",
        "hint": "CYP2E1 et réserve hépatique en antioxydant soufré.",
        "a": "Le métabolite est le NAPQI, produit par le CYP2E1. À dose normale, il est immédiatement neutralisé par le glutathion réduit (GSH). En cas de surdosage (> 8-10 g chez l'adulte, > 150 mg/kg chez l'enfant), les stocks de glutathion s'épuisent (> 70%) : le NAPQI libre se lie aux protéines hépatocytaires et entraîne une nécrose centrolobulaire massive.",
        "pearl": "L'antidote N-Acétylcystéine (NAC) reconstitue directement les stocks hépatiques de glutathion."
    },
    {
        "id": 4,
        "cat": "palier1",
        "tag": "Palier I • Contre-indications AINS",
        "q": "À partir de quel terme de la grossesse les AINS sont-ils formellement et absolument contre-indiqués et pourquoi ?",
        "hint": "Semaines d'aménorrhée (SA) et répercussions cardiorespiratoires et rénales fœtales.",
        "a": "Contre-indication FORMELLE et ABSOLUE dès le début du 6e mois de grossesse (24 semaines d'aménorrhée - SA). Risques pour le fœtus : 1) Fermeture prématurée in utero du canal artériel (insuffisance cardiaque droite fœtale). 2) Insuffisance rénale fœtale avec anamnios.",
        "pearl": "Cette contre-indication s'applique à TOUS les AINS, y compris en prise unique et y compris par voie cutanée ou collyre."
    },
    {
        "id": 5,
        "cat": "palier1",
        "tag": "Palier I • Interactions AINS",
        "q": "Qu'appelle-t-on l'interaction du « Triple Whammy » et quelles en sont les conséquences rénales ?",
        "hint": "Association de 3 classes médicamenteuses courantes chez le patient hypertendu.",
        "a": "C'est l'association AINS + Diurétique + IEC (ou ARA2). L'AINS bloque les prostaglandines vasodilatatrices de l'artériole afférente. L'IEC bloque l'angiotensine II vasoconstrictrice de l'artériole efférente. Le diurétique induit une hypovolémie. Résultat : effondrement de la pression d'ultrafiltration glomérulaire et Insuffisance Rénale Aiguë (IRA).",
        "pearl": "Un grand classique d'examen : toujours surveiller la créatinine et la kaliémie lors de cette association."
    },
    {
        "id": 6,
        "cat": "opioides",
        "tag": "Palier II • Pharmacogénétique",
        "q": "Pourquoi la codéine et le tramadol sont-ils inefficaces chez 7-10% des patients et potentiellement toxiques chez d'autres ?",
        "hint": "Cytochrome hépatique et métaboliseurs lents vs ultra-rapides.",
        "a": "Ce sont des prodrogues bioactivées par le CYP2D6 (en Morphine pour la codéine, en O-déméthyltramadol M1 pour le tramadol). Chez les Métaboliseurs Lents (PM), aucune transformation = inefficacité analgésique totale. Chez les Métaboliseurs Ultra-Rapides (UM), surproduction massive et rapide de métabolite actif = dépression respiratoire grave.",
        "pearl": "La codéine est contre-indiquée chez les moins de 12 ans et les femmes allaitantes pour cette raison génétique."
    },
    {
        "id": 7,
        "cat": "opioides",
        "tag": "Palier II • Tramadol",
        "q": "Quels sont les deux mécanismes d'action distincts du tramadol et quelle interaction redoutable en découle ?",
        "hint": "Récepteur opioïde + recapture des monoamines.",
        "a": "Mécanisme dual : 1) Agoniste faible des récepteurs opioïdes µ (via le métabolite M1). 2) Inhibiteur de la recapture de la Sérotonine et de la Noradrénaline. Interaction majeure : avec les antidépresseurs ISRS/IRSNA ou triptans, risque de Syndrome Sérotoninergique potentiellement létal.",
        "pearl": "Le tramadol abaisse également le seuil épileptogène : grande prudence chez le patient épileptique."
    },
    {
        "id": 8,
        "cat": "opioides",
        "tag": "Palier III • Morphine & Rein",
        "q": "Quels sont les deux métabolites glucuroconjugués de la morphine et pourquoi posent-ils problème chez l'insuffisant rénal ?",
        "hint": "M6G vs M3G et élimination glomérulaire.",
        "a": "1) Morphine-6-Glucuronide (M6G) : actif, puissant analgésique et dépresseur respiratoire. 2) Morphine-3-Glucuronide (M3G) : dépourvu d'action analgésique, neurotoxique (hyperalgésie, myoclonies, convulsions). Tous deux sont éliminés par le rein et s'accumulent dangereusement si DFG < 30 mL/min.",
        "pearl": "Chez l'insuffisant rénal sévère, on privilégie l'Oxycodone (à dose réduite) ou le Fentanyl dont les métabolites sont inactifs."
    },
    {
        "id": 9,
        "cat": "opioides",
        "tag": "Palier III • Règle de Titration",
        "q": "Comment calcule-t-on la dose d'une interdose pour Accès Douloureux Paroxystique (ADP) chez un patient sous morphine LP ?",
        "hint": "Règle mathématique du 1/6e.",
        "a": "La dose d'interdose en Libération Immédiate (LI, ex: Actiskénan®) est égale à 1/6e (ou 10-15%) de la dose totale quotidienne de morphine orale. Exemple : sous Skenan® 60 mg matin et soir (total 120 mg/24h), chaque interdose d'ADP sera de 120 / 6 = 20 mg LI.",
        "pearl": "Si le patient prend plus de 4 interdoses par 24h, il faut réévaluer et augmenter la dose de fond LP."
    },
    {
        "id": 10,
        "cat": "opioides",
        "tag": "Palier III • Rotation des Opioïdes",
        "q": "Lors d'une rotation d'un opioïde fort vers un autre, pourquoi applique-t-on un abattement de 25% à 50% de la dose équianalgésique calculée ?",
        "hint": "Tolérance croisée incomplète.",
        "a": "En raison du phénomène de 'Tolérance Croisée Incomplète'. Les différents opioïdes n'activent pas les sous-populations de récepteurs µ avec la même affinité. Le patient n'étant pas pleinement tolérant à la nouvelle molécule, lui administrer 100% de la dose équivalente théorique provoquerait un surdosage aigu et une dépression respiratoire.",
        "pearl": "La règle SFAP recommande de calculer la dose théorique, puis d'appliquer une réduction systématique de 25 à 30% (voire 50% pour la méthadone)."
    },
    {
        "id": 11,
        "cat": "reglementation",
        "tag": "Réglementation • Stupéfiants",
        "q": "Quelles sont les règles de prescription et délivrance des morphiniques en France (Ordonnance Sécurisée) ?",
        "hint": "Durée maximale, rédaction des doses, chevauchement.",
        "a": "Prescription sur Ordonnance Sécurisée. Durée maximale de prescription : 28 jours (ou 14 jours pour certaines formes injectables). Posologies et doses rédigées EN TOUTES LETTRES. Règle du non-chevauchement : délivrance interdite pour une période déjà couverte sauf mention expresse du médecin 'en complément de'.",
        "pearl": "Le fentanyl transdermique (Durogesic®) est limité à 28 jours avec fractionnement de délivrance de 14 jours par défaut."
    },
    {
        "id": 12,
        "cat": "tox",
        "tag": "Antidote • Opioïdes",
        "q": "Quel est l'antidote spécifique de l'overdose aux morphiniques, sa voie d'administration et la précaution capitale de sa durée d'action ?",
        "hint": "Naloxone et risque de rebond de dépression respiratoire.",
        "a": "La Naloxone (Narcan®). Antagoniste pur compétitif des récepteurs µ. Titration IV : ampoule de 0.4 mg diluée dans 9 mL de sérum physiologique, injecter 1 à 2 mL (0.04 à 0.08 mg) toutes les 2 min jusqu'à FR > 10. Précaution capitale : demi-vie très courte (30 à 60 min), inférieure à celle de la morphine (2-3h) ou de la méthadone (24-36h). Risque de rechute en coma apnéique imposant une surveillance continue.",
        "pearl": "Une titration trop rapide peut déclencher un syndrome de sevrage aigu violent avec œdème pulmonaire catécholaminergique."
    },
    {
        "id": 13,
        "cat": "tox",
        "tag": "Antidote • Prescott",
        "q": "Décrivez le protocole de Prescott complet pour l'administration de la N-Acétylcystéine (NAC) en perfusion IV.",
        "hint": "Dose totale 300 mg/kg répartie en 3 phases sur 21 heures.",
        "a": "Protocole IV en 3 perfusions dans du sérum glucosé G5% : 1) Dose de charge : 150 mg/kg dans 200 mL G5% en 60 minutes. 2) Deuxième perfusion : 50 mg/kg dans 500 mL G5% en 4 heures. 3) Troisième perfusion : 100 mg/kg dans 1000 mL G5% en 16 heures. Total = 300 mg/kg en 21 heures.",
        "pearl": "Le traitement est efficace à 100% s'il est débuté dans les 8 premières heures suivant l'ingestion du paracétamol."
    },
    {
        "id": 14,
        "cat": "opioides",
        "tag": "Palier III • Buprénorphine",
        "q": "Pourquoi est-il formellement contre-indiqué d'associer la Buprénorphine (Subutex®, Temgesic®) avec la Morphine ?",
        "hint": "Agoniste partiel à très haute affinité vs agoniste pur.",
        "a": "La Buprénorphine est un agoniste partiel des récepteurs µ avec une affinité de liaison extrêmement forte, bien supérieure à celle de la morphine. Elle déplace instantanément la morphine de ses récepteurs, mais n'active le récepteur qu'à 40-50% (faible activité intrinsèque) : cela déclenche immédiatement un Syndrome de Sevrage Aigu précipité et une réapparition brutale de la douleur.",
        "pearl": "La buprénorphine a un effet plafond sur la dépression respiratoire, mais son antidote naloxone doit être utilisé à doses plus élevées."
    },
    {
        "id": 15,
        "cat": "palier1",
        "tag": "Palier I • Sélectivité COX-2",
        "q": "Quelle différence structurale au niveau du site actif explique la sélectivité des Coxibs (Célécoxib) pour la COX-2 ?",
        "hint": "Acide aminé en position 523.",
        "a": "En position 523 : la COX-1 possède une volumineuse Isoleucine (Ile523) qui encombre l'entrée. La COX-2 possède une Valine (Val523), plus petite d'un groupement méthyle (-CH3), ce qui libère une poche latérale hydrophobe supplémentaire de 20%. Le groupement sulfonamide encombrant du célécoxib ne peut s'insérer que dans la COX-2.",
        "pearl": "L'inhibition sélective de COX-2 préserve l'estomac mais supprime la PGI2 endothéliale vasodilatatrice sans bloquer le TXA2 plaquettaire : sur-risque thrombotique cardiovasculaire."
    }
]

html_template = """<!DOCTYPE html>
<html lang="fr" class="h-full">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>PharmaLab Pro • Pharmacologie Clinique des Antalgiques | 3e Année DFGSP3</title>
  
  <!-- PWA Manifest & App Icons -->
  <link rel="manifest" href="manifest.json">
  <meta name="theme-color" content="#1e40af">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta name="apple-mobile-web-app-title" content="PharmaLab">
  <link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
  <link rel="icon" type="image/svg+xml" href="icons/icon.svg">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- 3Dmol.js (WebGL Molecular Viewer) -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/3Dmol/2.0.4/3Dmol-min.js"></script>
  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <!-- Chart.js (Pharmacokinetics Plotter) -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  
  <!-- Google Fonts: Plus Jakarta Sans & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          },
          colors: {
            medical: {
              50: '#eff6ff',
              100: '#dbeafe',
              200: '#bfdbfe',
              300: '#93c5fd',
              400: '#60a5fa',
              500: '#3b82f6',
              600: '#2563eb',
              700: '#1d4ed8',
              800: '#1e40af',
              900: '#1e3a8a',
            },
            sage: {
              50: '#ecfdf5',
              100: '#d1fae5',
              200: '#a7f3d0',
              500: '#10b981',
              600: '#059669',
              700: '#047857',
              800: '#065f46',
            }
          }
        }
      }
    }
  </script>
  
  <style>
    ::-webkit-scrollbar { width: 5px; height: 5px; }
    ::-webkit-scrollbar-track { background: #f8fafc; }
    ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 9999px; }
    ::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
    
    body {
      background-color: #f8fafc;
      color: #0f172a;
      -webkit-tap-highlight-color: transparent;
    }
    
    .bottom-nav-btn.active {
      color: #1e40af;
      font-weight: 700;
    }
    .bottom-nav-btn.active i {
      stroke-width: 2.5;
    }
    
    .desk-tab-btn.active {
      background-color: #1e40af;
      color: #ffffff;
      box-shadow: 0 4px 6px -1px rgb(30 64 175 / 0.2);
    }
    
    #g3d-container {
      width: 100%;
      height: 340px;
      position: relative;
      background: #f1f5f9;
      border-radius: 1rem;
    }
  </style>
</head>
<body class="bg-slate-50 text-slate-900 font-sans min-h-screen flex flex-col antialiased selection:bg-blue-600 selection:text-white">

  <!-- TOP NAVIGATION HEADER -->
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200 shadow-sm">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 h-14 sm:h-16 flex items-center justify-between">
      
      <div class="flex items-center space-x-2.5 shrink-0">
        <div class="w-8 h-8 sm:w-9 sm:h-9 rounded-xl bg-blue-800 flex items-center justify-center text-white shadow-sm">
          <i data-lucide="cross" class="w-4 h-4 sm:w-5 sm:h-5"></i>
        </div>
        <div>
          <div class="flex items-center space-x-2">
            <span class="font-extrabold text-base sm:text-lg tracking-tight text-blue-900">
              PharmaLab
            </span>
            <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-50 text-blue-800 border border-blue-200">
              DFGSP3
            </span>
          </div>
          <p class="text-[10px] text-slate-500 hidden sm:block">Pharmacologie Clinique des Antalgiques</p>
        </div>
      </div>

      <nav class="hidden md:flex items-center space-x-1 text-xs font-semibold">
        <button onclick="switchMasterTab('drugs')" id="desk-btn-drugs" class="desk-tab-btn active px-3.5 py-2 rounded-xl transition flex items-center space-x-1.5 text-slate-600 hover:text-slate-900 hover:bg-slate-100">
          <i data-lucide="book-open" class="w-4 h-4"></i>
          <span>Fiches Médicaments</span>
        </button>
        <button onclick="switchMasterTab('rules')" id="desk-btn-rules" class="desk-tab-btn px-3.5 py-2 rounded-xl transition flex items-center space-x-1.5 text-slate-600 hover:text-slate-900 hover:bg-slate-100">
          <i data-lucide="alert-triangle" class="w-4 h-4"></i>
          <span>Pièges d'Examen</span>
        </button>
        <button onclick="switchMasterTab('cases')" id="desk-btn-cases" class="desk-tab-btn px-3.5 py-2 rounded-xl transition flex items-center space-x-1.5 text-slate-600 hover:text-slate-900 hover:bg-slate-100">
          <i data-lucide="stethoscope" class="w-4 h-4"></i>
          <span>Cas Cliniques</span>
        </button>
        <button onclick="switchMasterTab('flashcards')" id="desk-btn-flashcards" class="desk-tab-btn px-3.5 py-2 rounded-xl transition flex items-center space-x-1.5 text-slate-600 hover:text-slate-900 hover:bg-slate-100">
          <i data-lucide="zap" class="w-4 h-4"></i>
          <span>Flashcards Anki</span>
        </button>
      </nav>

      <div class="flex items-center space-x-2">
        <button onclick="openToolsModal()" class="flex items-center space-x-1.5 px-3 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-bold border border-slate-300 transition">
          <i data-lucide="box" class="w-3.5 h-3.5 text-blue-700"></i>
          <span>Outils &amp; 3D</span>
        </button>
        <button id="btn-pwa-install" onclick="triggerPWAInstall()" class="hidden sm:flex items-center space-x-1.5 px-3 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-bold transition shadow-sm">
          <i data-lucide="download" class="w-3.5 h-3.5"></i>
          <span>Installer</span>
        </button>
      </div>

    </div>
  </header>

  <!-- MAIN CONTENT AREA -->
  <main class="flex-1 max-w-6xl w-full mx-auto px-3 sm:px-6 py-4 sm:py-6 pb-24 md:pb-8">

    <!-- SECTION 1 : FICHES MÉDICAMENTS ESSENTIELLES -->
    <section id="sec-drugs" class="space-y-4">
      
      <div class="bg-white border border-slate-200/90 rounded-2xl p-4 shadow-sm space-y-3">
        <div class="relative">
          <i data-lucide="search" class="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2"></i>
          <input type="text" id="drug-search" oninput="filterDrugs()" placeholder="Rechercher une DCI ou marque (Doliprane, Advil, Tramadol, Skénan...)"
            class="w-full pl-10 pr-4 py-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs sm:text-sm text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-600 focus:bg-white transition">
        </div>

        <div class="flex items-center space-x-1.5 overflow-x-auto pb-1 text-xs font-medium no-scrollbar">
          <button onclick="filterCategory('all')" id="cat-all" class="cat-pill active px-3 py-1.5 rounded-lg bg-blue-800 text-white font-bold whitespace-nowrap shadow-sm">Toutes (24)</button>
          <button onclick="filterCategory('palier1')" id="cat-palier1" class="cat-pill px-3 py-1.5 rounded-lg bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap">Palier I (Non Opioïdes)</button>
          <button onclick="filterCategory('palier2')" id="cat-palier2" class="cat-pill px-3 py-1.5 rounded-lg bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap">Palier II (Opioïdes Faibles)</button>
          <button onclick="filterCategory('palier3')" id="cat-palier3" class="cat-pill px-3 py-1.5 rounded-lg bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap">Palier III (Opioïdes Forts)</button>
          <button onclick="filterCategory('adjuvants')" id="cat-adjuvants" class="cat-pill px-3 py-1.5 rounded-lg bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap">Adjuvants &amp; Antidotes</button>
        </div>
      </div>

      <div id="drugs-grid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3.5">
      </div>

    </section>

    <!-- SECTION 2 : PIÈGES D'EXAMEN & RÈGLES D'OR -->
    <section id="sec-rules" class="space-y-4 hidden">
      
      <div class="bg-blue-900 text-white rounded-2xl p-5 sm:p-6 shadow-sm space-y-1.5">
        <span class="px-2.5 py-0.5 rounded-md bg-blue-800 text-blue-200 text-[10px] font-bold uppercase tracking-wider">
          Fiches Réflexe 3e Année
        </span>
        <h1 class="text-xl sm:text-2xl font-black">Les 7 Règles d'Or &amp; Pièges d'Examen</h1>
        <p class="text-xs sm:text-sm text-blue-100 leading-relaxed">
          Les points indispensables pour réussir vos partiels de pharmacologie et sécuriser la dispensation en stage officinal ou hospitalier.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        
        <!-- Rule 1: Paliers OMS -->
        <div class="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-sm space-y-3">
          <div class="flex items-center space-x-2">
            <span class="w-7 h-7 rounded-lg bg-blue-100 text-blue-800 flex items-center justify-center text-xs font-black">1</span>
            <h3 class="font-bold text-slate-900 text-sm">Les 3 Paliers OMS &amp; L'Ascenseur Antalgique</h3>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed">
            La prise en charge de la douleur aiguë s'adapte à l'évaluation sur l'échelle visuelle analogique (EVA) :
          </p>
          <ul class="text-xs text-slate-700 space-y-1.5 bg-slate-50 p-3 rounded-xl border border-slate-100">
            <li>• <strong class="text-blue-900">EVA 1 à 3 (Légère) :</strong> Palier I (Paracétamol, AINS si composante inflammatoire).</li>
            <li>• <strong class="text-blue-900">EVA 4 à 6 (Modérée) :</strong> Palier II (Tramadol, Codéine, Poudre d'opium).</li>
            <li>• <strong class="text-blue-900">EVA &ge; 7 (Sévère) :</strong> Palier III direct (Morphine, Oxycodone, Fentanyl). <em>Règle de l'ascenseur : ne jamais attendre pour introduire le palier III si la douleur est d'emblée aiguë et intolérable !</em></li>
          </ul>
          <div class="p-2.5 rounded-xl bg-rose-50 border border-rose-200 text-[11px] text-rose-800">
            <strong>🚫 Interdiction absolue :</strong> Ne JAMAIS associer deux opioïdes de même palier, ni un palier II avec un palier III (sommation des toxicités sans gain d'analgésie).
          </div>
        </div>

        <!-- Rule 2: Triple Whammy -->
        <div class="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-sm space-y-3">
          <div class="flex items-center space-x-2">
            <span class="w-7 h-7 rounded-lg bg-rose-100 text-rose-800 flex items-center justify-center text-xs font-black">2</span>
            <h3 class="font-bold text-slate-900 text-sm">La Triade Létale : Le « Triple Whammy »</h3>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed">
            L'association simultanée de 3 classes courantes anéantit l'autorégulation de la filtration glomérulaire rénale :
          </p>
          <div class="grid grid-cols-3 gap-2 text-center text-[10px] font-bold">
            <div class="p-2 bg-slate-100 rounded-lg border border-slate-200">
              <span class="text-blue-900 block">AINS</span>
              <span class="font-normal text-slate-600">Constriction afférente</span>
            </div>
            <div class="p-2 bg-slate-100 rounded-lg border border-slate-200">
              <span class="text-blue-900 block">IEC / ARA2</span>
              <span class="font-normal text-slate-600">Dilatation efférente</span>
            </div>
            <div class="p-2 bg-slate-100 rounded-lg border border-slate-200">
              <span class="text-blue-900 block">Diurétique</span>
              <span class="font-normal text-slate-600">Hypovolémie</span>
            </div>
          </div>
          <div class="p-2.5 rounded-xl bg-rose-50 border border-rose-200 text-[11px] text-rose-800">
            <strong>⚠️ Conséquence :</strong> Effondrement brutal de la pression d'ultrafiltration glomérulaire &rarr; <strong>Insuffisance rénale aiguë oligo-anurique</strong> avec hyperkaliémie menaçante.
          </div>
        </div>

        <!-- Rule 3: Samter-Widal -->
        <div class="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-sm space-y-3">
          <div class="flex items-center space-x-2">
            <span class="w-7 h-7 rounded-lg bg-amber-100 text-amber-800 flex items-center justify-center text-xs font-black">3</span>
            <h3 class="font-bold text-slate-900 text-sm">Le Piège de Samter-Widal (AINS &amp; Asthme)</h3>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed">
            La maladie de Widal associe une triade classique : <strong>Asthme + Polypose naso-sinusienne + Intolérance majeure à l'aspirine et aux AINS</strong>.
          </p>
          <ul class="text-xs text-slate-700 space-y-1.5 bg-slate-50 p-3 rounded-xl border border-slate-100">
            <li>• <strong>Mécanisme :</strong> Le blocage de la COX-1 dévie tout l'acide arachidonique vers la voie de la 5-Lipoxygénase (5-LOX).</li>
            <li>• <strong>Résultat :</strong> Surproduction massive de leucotriènes bronchoconstricteurs (LTC4, LTD4, LTE4).</li>
          </ul>
          <div class="p-2.5 rounded-xl bg-amber-50 border border-amber-200 text-[11px] text-amber-800">
            <strong>💡 Conduite à tenir :</strong> Contre-indication absolue à tous les AINS et aspirine chez ce patient. Le paracétamol reste généralement bien toléré.
          </div>
        </div>

        <!-- Rule 4: Paracétamol & Rumack-Matthew -->
        <div class="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-sm space-y-3">
          <div class="flex items-center space-x-2">
            <span class="w-7 h-7 rounded-lg bg-emerald-100 text-emerald-800 flex items-center justify-center text-xs font-black">4</span>
            <h3 class="font-bold text-slate-900 text-sm">Surdosage Paracétamol &amp; Protocole de Prescott</h3>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed">
            Le seuil toxique est de <strong>&gt; 8 à 10 g</strong> chez l'adulte (ou <strong>&gt; 150 mg/kg</strong> chez l'enfant). À dose toxique, le NAPQI sature les réserves de glutathion hépatique (&gt; 70% de déplétion) et provoque une nécrose centrolobulaire hépatique.
          </p>
          <div class="text-xs text-slate-700 bg-slate-50 p-3 rounded-xl border border-slate-100 space-y-1">
            <p><strong>Protocole de Prescott (N-Acétylcystéine IV en 21h) :</strong></p>
            <p>1. Dose de charge : 150 mg/kg dans 200 mL G5% en 1 heure.</p>
            <p>2. Deuxième perfusion : 50 mg/kg dans 500 mL G5% en 4 heures.</p>
            <p>3. Troisième perfusion : 100 mg/kg dans 1 000 mL G5% en 16 heures.</p>
          </div>
          <div class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-[11px] text-emerald-800">
            <strong>🌟 Efficacité :</strong> 100% protecteur si administré dans les 8 à 10 heures suivant l'ingestion (nomogramme de Rumack-Matthew).
          </div>
        </div>

        <!-- Rule 5: Opioïdes Stupéfiants -->
        <div class="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-sm space-y-3">
          <div class="flex items-center space-x-2">
            <span class="w-7 h-7 rounded-lg bg-purple-100 text-purple-800 flex items-center justify-center text-xs font-black">5</span>
            <h3 class="font-bold text-slate-900 text-sm">Réglementation des Morphiniques (Stupéfiants)</h3>
          </div>
          <ul class="text-xs text-slate-700 space-y-1.5 bg-slate-50 p-3 rounded-xl border border-slate-100">
            <li>• <strong>Ordonnance sécurisée :</strong> Papier filigrané, identification du prescripteur, carré de sécurité.</li>
            <li>• <strong>Durée maximale :</strong> 28 jours (ou 14 jours pour certaines formes injectables).</li>
            <li>• <strong>Rédaction en toutes lettres :</strong> Nombre d'unités thérapeutiques par prise, nombre de prises et dosage.</li>
            <li>• <strong>Chevauchement interdit :</strong> Délivrance interdite pour une période déjà couverte, sauf mention expresse « en complément de ».</li>
          </ul>
          <div class="p-2.5 rounded-xl bg-purple-50 border border-purple-200 text-[11px] text-purple-800">
            <strong>💊 Règle clinique d'or :</strong> Toujours prescrire et délivrer systématiquement un <strong>laxatif osmotique</strong> (Macrogol) dès l'initiation d'un opioïde au long cours (pas d'accoutumance sur la constipation).
          </div>
        </div>

        <!-- Rule 6: Titration Morphine -->
        <div class="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-sm space-y-3">
          <div class="flex items-center space-x-2">
            <span class="w-7 h-7 rounded-lg bg-blue-100 text-blue-800 flex items-center justify-center text-xs font-black">6</span>
            <h3 class="font-bold text-slate-900 text-sm">Titration de la Morphine &amp; Règle du 1/6e</h3>
          </div>
          <p class="text-xs text-slate-600 leading-relaxed">
            Pour les Accès Douloureux Paroxystiques (ADP) chez un patient sous morphine LP de fond :
          </p>
          <div class="p-3 bg-blue-50/60 rounded-xl border border-blue-200 text-xs text-blue-900 space-y-1">
            <p class="font-bold">Dose d'interdose (LI) = Dose quotidienne totale / 6</p>
            <p class="text-slate-600">Exemple : Skenan® LP 60 mg matin et soir (120 mg/j). L'interdose d'Actiskénan® LI sera de : <strong>120 / 6 = 20 mg</strong> par prise si besoin.</p>
          </div>
          <div class="p-2.5 rounded-xl bg-amber-50 border border-amber-200 text-[11px] text-amber-800">
            <strong>⚠️ Alerte clinique :</strong> Si le patient consomme plus de 4 interdoses par 24 heures, la dose de fond LP est insuffisante et doit être réévaluée à la hausse.
          </div>
        </div>

        <!-- Rule 7: Rotation des Opioïdes -->
        <div class="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-sm space-y-3 md:col-span-2">
          <div class="flex items-center space-x-2">
            <span class="w-7 h-7 rounded-lg bg-emerald-100 text-emerald-800 flex items-center justify-center text-xs font-black">7</span>
            <h3 class="font-bold text-slate-900 text-sm">Rotation des Opioïdes &amp; Tolérance Croisée Incomplète</h3>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs text-slate-700">
            <div class="bg-slate-50 p-3 rounded-xl border border-slate-100 space-y-1">
              <span class="font-bold text-slate-900 block">Équivalences orales (SFAP) :</span>
              <p>• 10 mg Morphine PO = 5 mg Oxycodone PO (ratio 1:2)</p>
              <p>• 100 mg Tramadol PO = 20 mg Morphine PO (ratio 1:5)</p>
              <p>• 100 mg Codéine PO = 15 mg Morphine PO (ratio 1:6.6)</p>
            </div>
            <div class="bg-slate-50 p-3 rounded-xl border border-slate-100 space-y-1">
              <span class="font-bold text-slate-900 block">La Règle de l'Abattement :</span>
              <p>En raison du phénomène de <strong>Tolérance Croisée Incomplète</strong>, les récepteurs µ ne réagissent pas identiquement à la nouvelle molécule.</p>
              <p class="font-bold text-emerald-800">Réduire obligatoirement la dose théorique calculée de 25% à 30% pour éviter un surdosage aigu mortel.</p>
            </div>
          </div>
        </div>

      </div>

    </section>

    <!-- SECTION 3 : CAS CLINIQUES & AUDIT D'ORDONNANCES -->
    <section id="sec-cases" class="space-y-4 hidden">
      
      <div class="bg-white border border-slate-200 rounded-2xl p-4 sm:p-5 shadow-sm flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div>
          <span class="px-2.5 py-0.5 rounded-md bg-emerald-50 text-emerald-800 text-[10px] font-bold uppercase border border-emerald-200">
            Entraînement Officinal &amp; Hospitalier
          </span>
          <h2 class="text-lg sm:text-xl font-black text-slate-900 mt-1">8 Cas Cliniques d'Audit d'Ordonnances</h2>
          <p class="text-xs text-slate-500">Mettez-vous en situation de validation pharmaceutique au comptoir.</p>
        </div>

        <div class="flex items-center space-x-2">
          <span class="text-xs text-slate-500 font-bold shrink-0">Cas :</span>
          <select id="case-select" onchange="loadCase(parseInt(this.value))" class="text-xs font-bold p-2.5 rounded-xl bg-slate-50 border border-slate-300 text-slate-800 focus:ring-2 focus:ring-blue-600 focus:outline-none">
            <option value="1">1. Amina (Grossesse &amp; AINS)</option>
            <option value="2">2. Gérard (Triple Whammy)</option>
            <option value="3">3. Thomas (Tramadol &amp; Sérotonine)</option>
            <option value="4">4. Christian (Morphine &amp; Interdoses)</option>
            <option value="5">5. Sophie (Lithium &amp; AINS)</option>
            <option value="6">6. Julien (Varicelle &amp; AINS)</option>
            <option value="7">7. Patrick (Douleur Neuropathique)</option>
            <option value="8">8. Marie (Intoxication Paracétamol)</option>
          </select>
        </div>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 sm:p-6 shadow-sm space-y-5">
        
        <div class="flex items-start justify-between border-b border-slate-100 pb-4">
          <div class="flex items-center space-x-3">
            <div id="case-avatar" class="w-10 h-10 rounded-xl bg-blue-100 text-blue-800 flex items-center justify-center font-black text-sm">
              1
            </div>
            <div>
              <h3 id="case-title" class="font-extrabold text-slate-900 text-base">Amina, 28 ans</h3>
              <p id="case-context" class="text-xs text-slate-500">Grossesse 31 SA (3e trimestre) • Pulpite dentaire aiguë hyperalgique</p>
            </div>
          </div>
          <span id="case-status-badge" class="px-2.5 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-600 border border-slate-200">
            En attente de décision
          </span>
        </div>

        <div class="bg-slate-50 border border-slate-200 rounded-xl p-4 space-y-2">
          <span class="text-[10px] uppercase font-bold text-slate-500 tracking-wider flex items-center space-x-1">
            <i data-lucide="file-text" class="w-3.5 h-3.5 text-blue-700"></i>
            <span>Ordonnance Présentée au Comptoir :</span>
          </span>
          <p id="case-rx-patient" class="text-xs font-bold text-slate-800">Patiente : Amina B. (28 ans, Enceinte 31 SA)</p>
          <div id="case-rx-lines" class="text-xs text-slate-700 font-mono bg-white p-3 rounded-lg border border-slate-200 leading-relaxed">
            • Ibuprofène 400 mg : 1 comprimé 3 fois par jour au cours des repas pendant 5 jours.
          </div>
        </div>

        <div class="p-3.5 rounded-xl bg-blue-50/60 border border-blue-200 text-xs text-blue-900">
          <strong class="block mb-1 flex items-center space-x-1 font-bold">
            <i data-lucide="info" class="w-3.5 h-3.5 text-blue-800"></i>
            <span>Point de repère pharmacologique :</span>
          </strong>
          <span id="case-pearl-text">Même une prise unique d'AINS à partir du 6e mois de grossesse (24 SA) peut causer la fermeture irréversible in utero du canal artériel fœtal et une anurie fœtale (oligoamnios). Contre-indication formelle et absolue !</span>
        </div>

        <div class="space-y-2.5">
          <span class="text-xs font-bold text-slate-800 block">Quelle est votre décision pharmaceutique ?</span>
          <div id="case-options-box" class="space-y-2">
          </div>
        </div>

        <div id="case-feedback-box" class="hidden p-4 rounded-xl text-xs leading-relaxed">
        </div>

      </div>

    </section>

    <!-- SECTION 4 : FLASHCARDS RÉVISION RAPIDE (ANKI SRS) -->
    <section id="sec-flashcards" class="space-y-4 hidden">
      
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
        <div class="bg-white border border-slate-200 rounded-xl p-3 shadow-sm">
          <span class="text-[10px] font-bold text-slate-400 uppercase block">Deck Antalgiques</span>
          <span id="srs-count" class="text-base font-black text-blue-900 font-mono">15 cartes</span>
        </div>
        <div class="bg-white border border-slate-200 rounded-xl p-3 shadow-sm">
          <span class="text-[10px] font-bold text-slate-400 uppercase block">Rétention</span>
          <span class="text-base font-black text-emerald-700 font-mono">94%</span>
        </div>
        <div class="bg-white border border-slate-200 rounded-xl p-3 shadow-sm">
          <span class="text-[10px] font-bold text-slate-400 uppercase block">Série (Streak)</span>
          <span class="text-base font-black text-amber-700 font-mono">🔥 4 jours</span>
        </div>
        <div class="bg-white border border-slate-200 rounded-xl p-3 shadow-sm flex items-center justify-between">
          <div>
            <span class="text-[10px] font-bold text-slate-400 uppercase block">Progression</span>
            <span id="srs-progress" class="text-base font-black text-slate-800 font-mono">1 / 15</span>
          </div>
          <button onclick="resetSrs()" title="Recommencer" class="p-1.5 rounded-lg hover:bg-slate-100 text-slate-400 hover:text-slate-700">
            <i data-lucide="rotate-ccw" class="w-4 h-4"></i>
          </button>
        </div>
      </div>

      <div class="flex items-center space-x-1.5 overflow-x-auto pb-1 text-xs font-medium no-scrollbar">
        <button onclick="filterSrs('all')" id="srs-btn-all" class="srs-cat active px-3 py-1.5 rounded-lg bg-blue-800 text-white font-bold whitespace-nowrap shadow-sm">Toutes (15)</button>
        <button onclick="filterSrs('palier1')" id="srs-btn-palier1" class="srs-cat px-3 py-1.5 rounded-lg bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 whitespace-nowrap">Palier I &amp; AINS</button>
        <button onclick="filterSrs('opioides')" id="srs-btn-opioides" class="srs-cat px-3 py-1.5 rounded-lg bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 whitespace-nowrap">Opioïdes (II &amp; III)</button>
        <button onclick="filterSrs('tox')" id="srs-btn-tox" class="srs-cat px-3 py-1.5 rounded-lg bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 whitespace-nowrap">Toxicologie &amp; Antidotes</button>
        <button onclick="filterSrs('reglementation')" id="srs-btn-reglementation" class="srs-cat px-3 py-1.5 rounded-lg bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 whitespace-nowrap">Réglementation</button>
      </div>

      <div class="bg-white border border-slate-200 rounded-2xl p-5 sm:p-7 shadow-sm min-h-[300px] flex flex-col justify-between space-y-4">
        
        <div class="flex items-center justify-between">
          <span id="srs-tag" class="px-2.5 py-0.5 rounded-md text-[10px] font-bold uppercase bg-blue-50 text-blue-800 border border-blue-200">
            Palier I • Aspirine
          </span>
          <span id="srs-index" class="text-xs font-mono text-slate-400">Carte 1 sur 15</span>
        </div>

        <div id="srs-front" class="my-auto space-y-2">
          <h2 id="srs-question" class="text-base sm:text-lg font-bold text-slate-900 leading-snug">
            Pourquoi l'aspirine à faible dose (75 à 160 mg/j) possède-t-elle un effet antiagrégant durant 7 à 10 jours ?
          </h2>
          <p id="srs-hint" class="text-xs text-slate-500 italic">Indice : Type de liaison avec la COX-1 et particularité des plaquettes sanguines.</p>
        </div>

        <div id="srs-back" class="hidden my-auto space-y-3 p-4 rounded-xl bg-slate-50 border border-slate-200">
          <div>
            <span class="text-[10px] font-bold text-emerald-800 uppercase tracking-wider block mb-1">Réponse synthétique :</span>
            <p id="srs-answer" class="text-xs sm:text-sm text-slate-800 leading-relaxed font-medium">
              L'aspirine acétyle de façon irréversible et covalente la Sérine 529 de la COX-1 plaquettaire, bloquant définitivement la synthèse de TXA2. Les plaquettes étant anucléées, l'inhibition dure toute leur vie circulante (7 à 10 jours).
            </p>
          </div>
          <div class="p-2.5 rounded-lg bg-amber-50 border border-amber-200 text-[11px] text-amber-800">
            <strong>💡 Perle d'examen :</strong>
            <span id="srs-pearl">L'arrêt préopératoire de l'aspirine antiagrégante doit être planifié 5 à 7 jours avant une chirurgie à risque hémorragique.</span>
          </div>
        </div>

        <div class="pt-3 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-3">
          <button id="srs-btn-reveal" onclick="revealSrs()" class="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-blue-800 hover:bg-blue-900 text-white font-bold text-xs transition flex items-center justify-center space-x-2 shadow-sm">
            <i data-lucide="eye" class="w-4 h-4"></i>
            <span>Afficher la Réponse</span>
          </button>

          <div id="srs-ratings" class="hidden w-full sm:w-auto flex items-center space-x-1.5">
            <button onclick="rateSrs(1)" class="flex-1 sm:flex-initial px-3 py-2 rounded-xl bg-rose-50 hover:bg-rose-100 border border-rose-200 text-rose-800 text-xs font-bold transition text-center">
              À revoir
            </button>
            <button onclick="rateSrs(2)" class="flex-1 sm:flex-initial px-3 py-2 rounded-xl bg-amber-50 hover:bg-amber-100 border border-amber-200 text-amber-800 text-xs font-bold transition text-center">
              Difficile
            </button>
            <button onclick="rateSrs(3)" class="flex-1 sm:flex-initial px-3 py-2 rounded-xl bg-emerald-50 hover:bg-emerald-100 border border-emerald-200 text-emerald-800 text-xs font-bold transition text-center">
              Correct
            </button>
            <button onclick="rateSrs(4)" class="flex-1 sm:flex-initial px-3 py-2 rounded-xl bg-blue-50 hover:bg-blue-100 border border-blue-200 text-blue-800 text-xs font-bold transition text-center">
              Facile
            </button>
          </div>
        </div>

      </div>

    </section>

  </main>

  <!-- MOBILE BOTTOM NAVIGATION BAR -->
  <nav class="fixed bottom-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md border-t border-slate-200 px-3 py-1.5 flex items-center justify-around shadow-lg md:hidden">
    <button onclick="switchMasterTab('drugs')" id="mob-btn-drugs" class="bottom-nav-btn active flex flex-col items-center justify-center py-1 px-2.5 text-[11px] font-medium text-slate-500 transition active:scale-95">
      <i data-lucide="book-open" class="w-5 h-5 mb-0.5"></i>
      <span>Fiches</span>
    </button>
    <button onclick="switchMasterTab('rules')" id="mob-btn-rules" class="bottom-nav-btn flex flex-col items-center justify-center py-1 px-2.5 text-[11px] font-medium text-slate-500 transition active:scale-95">
      <i data-lucide="alert-triangle" class="w-5 h-5 mb-0.5"></i>
      <span>Pièges</span>
    </button>
    <button onclick="switchMasterTab('cases')" id="mob-btn-cases" class="bottom-nav-btn flex flex-col items-center justify-center py-1 px-2.5 text-[11px] font-medium text-slate-500 transition active:scale-95">
      <i data-lucide="stethoscope" class="w-5 h-5 mb-0.5"></i>
      <span>Cas</span>
    </button>
    <button onclick="switchMasterTab('flashcards')" id="mob-btn-flashcards" class="bottom-nav-btn flex flex-col items-center justify-center py-1 px-2.5 text-[11px] font-medium text-slate-500 transition active:scale-95">
      <i data-lucide="zap" class="w-5 h-5 mb-0.5"></i>
      <span>Quiz</span>
    </button>
  </nav>

  <!-- DRUG DETAIL SLIDE-OVER DRAWER -->
  <div id="drug-drawer-backdrop" onclick="closeDrugDrawer()" class="fixed inset-0 z-50 bg-slate-900/40 backdrop-blur-xs hidden transition-opacity"></div>
  <aside id="drug-drawer" class="fixed top-0 right-0 bottom-0 z-50 w-full max-w-xl bg-white shadow-2xl transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col overflow-hidden">
    
    <div class="px-5 py-4 border-b border-slate-200 flex items-center justify-between bg-slate-50">
      <div class="space-y-0.5">
        <div class="flex items-center space-x-2">
          <span id="drawer-palier" class="px-2 py-0.5 rounded text-[10px] font-bold uppercase bg-blue-100 text-blue-800">
            Palier I
          </span>
          <span id="drawer-legal" class="text-[11px] text-slate-500 font-mono">Médication officinale</span>
        </div>
        <h2 id="drawer-title" class="text-lg font-black text-slate-900">Paracétamol</h2>
        <p id="drawer-brands" class="text-xs text-slate-500">Doliprane®, Dafalgan®, Efferalgan®</p>
      </div>
      <button onclick="closeDrugDrawer()" class="p-2 rounded-xl hover:bg-slate-200 text-slate-500 transition">
        <i data-lucide="x" class="w-5 h-5"></i>
      </button>
    </div>

    <div class="flex-1 p-5 overflow-y-auto space-y-4 text-xs text-slate-700">
      
      <div id="drawer-3d-banner" class="p-3.5 rounded-xl bg-blue-50 border border-blue-200 flex items-center justify-between">
        <div>
          <span class="font-bold text-blue-900 block text-xs">Visualisation 3D Disponible</span>
          <span class="text-[11px] text-blue-700">Explorez la structure spatiale de cette molécule.</span>
        </div>
        <button id="drawer-btn-3d" onclick="open3dForCurrentDrug()" class="px-3 py-1.5 rounded-lg bg-blue-800 hover:bg-blue-900 text-white font-bold text-xs flex items-center space-x-1 shadow-sm transition">
          <i data-lucide="cuboid" class="w-3.5 h-3.5"></i>
          <span>Ouvrir en 3D</span>
        </button>
      </div>

      <div class="space-y-2">
        <h3 class="font-bold text-slate-900 text-xs flex items-center space-x-1.5 text-blue-900 uppercase tracking-wider">
          <i data-lucide="clock" class="w-3.5 h-3.5"></i>
          <span>Posologies Usuelles &amp; Adaptations</span>
        </h3>
        <div class="bg-slate-50 p-3 rounded-xl border border-slate-200 space-y-1.5">
          <div><strong class="text-slate-900">Adulte :</strong> <span id="drawer-poso-adult"></span></div>
          <div><strong class="text-slate-900">Pédiatrie :</strong> <span id="drawer-poso-ped"></span></div>
          <div><strong class="text-slate-900">Insuffisance Rénale :</strong> <span id="drawer-poso-renal"></span></div>
          <div><strong class="text-slate-900">Sujet Âgé :</strong> <span id="drawer-poso-elderly"></span></div>
        </div>
      </div>

      <div class="space-y-2">
        <h3 class="font-bold text-slate-900 text-xs flex items-center space-x-1.5 text-rose-800 uppercase tracking-wider">
          <i data-lucide="shield-alert" class="w-3.5 h-3.5"></i>
          <span>Contre-indications Absolues</span>
        </h3>
        <ul id="drawer-ci" class="space-y-1 bg-rose-50/60 p-3 rounded-xl border border-rose-200 text-rose-900">
        </ul>
      </div>

      <div class="space-y-2">
        <h3 class="font-bold text-slate-900 text-xs flex items-center space-x-1.5 text-amber-800 uppercase tracking-wider">
          <i data-lucide="alert-circle" class="w-3.5 h-3.5"></i>
          <span>Précautions d'Emploi &amp; Points de Vigilance</span>
        </h3>
        <ul id="drawer-precautions" class="space-y-1 bg-amber-50/60 p-3 rounded-xl border border-amber-200 text-amber-900">
        </ul>
      </div>

      <div class="space-y-2">
        <h3 class="font-bold text-slate-900 text-xs flex items-center space-x-1.5 text-purple-800 uppercase tracking-wider">
          <i data-lucide="git-merge" class="w-3.5 h-3.5"></i>
          <span>Interactions Médicamenteuses Majeures</span>
        </h3>
        <div id="drawer-interactions" class="space-y-2">
        </div>
      </div>

      <div class="space-y-2">
        <h3 class="font-bold text-slate-900 text-xs flex items-center space-x-1.5 text-slate-700 uppercase tracking-wider">
          <i data-lucide="activity" class="w-3.5 h-3.5"></i>
          <span>Pharmacocinétique &amp; Métabolisme</span>
        </h3>
        <div class="bg-slate-50 p-3 rounded-xl border border-slate-200 space-y-1 text-slate-600">
          <div><strong class="text-slate-900">Biodisponibilité :</strong> <span id="drawer-pk-f"></span></div>
          <div><strong class="text-slate-900">Tmax :</strong> <span id="drawer-pk-tmax"></span></div>
          <div><strong class="text-slate-900">Demi-vie (t1/2) :</strong> <span id="drawer-pk-t12"></span></div>
          <div><strong class="text-slate-900">Voies métaboliques :</strong> <span id="drawer-metab-path"></span></div>
          <div id="drawer-metab-tox-box" class="mt-1 pt-1 border-t border-slate-200">
            <strong class="text-rose-800">Métabolite toxique :</strong> <span id="drawer-metab-tox"></span>
          </div>
        </div>
      </div>

      <div class="p-3.5 rounded-xl bg-blue-50 border border-blue-200 text-xs text-blue-900">
        <strong class="block mb-1 flex items-center space-x-1">
          <i data-lucide="sparkles" class="w-3.5 h-3.5 text-blue-700"></i>
          <span>Perle de Concours &amp; Officine :</span>
        </strong>
        <p id="drawer-pearl" class="leading-relaxed"></p>
      </div>

    </div>
  </aside>

  <!-- MODAL : OUTILS AVANCÉS (3D MOLÉCULAIRE & SIMULATEUR PK) -->
  <div id="tools-modal" class="fixed inset-0 z-50 bg-slate-900/50 backdrop-blur-xs hidden flex items-center justify-center p-3 sm:p-6">
    <div class="bg-white border border-slate-200 w-full max-w-4xl rounded-2xl shadow-2xl overflow-hidden flex flex-col max-h-[90vh]">
      
      <div class="px-5 py-3.5 border-b border-slate-200 flex items-center justify-between bg-slate-50">
        <div class="flex items-center space-x-2">
          <div class="w-7 h-7 rounded-lg bg-blue-800 text-white flex items-center justify-center">
            <i data-lucide="box" class="w-4 h-4"></i>
          </div>
          <h2 class="font-bold text-slate-900 text-sm">Outils Avancés &amp; Visualisation 3D</h2>
        </div>
        <button onclick="closeToolsModal()" class="p-1.5 rounded-lg hover:bg-slate-200 text-slate-500 transition">
          <i data-lucide="x" class="w-4 h-4"></i>
        </button>
      </div>

      <div class="flex border-b border-slate-200 bg-white px-4 text-xs font-semibold space-x-2 pt-2">
        <button onclick="switchToolsTab('3d')" id="tools-tab-btn-3d" class="pb-2.5 px-3 border-b-2 border-blue-800 text-blue-800 font-bold transition">
          1. Visualiseur 3D
        </button>
        <button onclick="switchToolsTab('pk')" id="tools-tab-btn-pk" class="pb-2.5 px-3 border-b-2 border-transparent text-slate-500 hover:text-slate-800 transition">
          2. Simulateur PK C(t)
        </button>
      </div>

      <div class="p-4 sm:p-5 overflow-y-auto flex-1 space-y-4">
        
        <!-- Tab 1 : Visualiseur 3D -->
        <div id="tools-panel-3d" class="space-y-3">
          <div class="flex flex-wrap items-center justify-between gap-2">
            <div class="flex items-center space-x-2 text-xs">
              <span class="text-slate-600 font-bold">Molécule :</span>
              <select id="mol-select" onchange="render3D(this.value)" class="p-2 rounded-xl bg-slate-50 border border-slate-300 font-bold text-slate-800 text-xs focus:outline-none">
                <option value="paracetamol">Paracétamol (Palier I)</option>
                <option value="aspirine">Aspirine (Palier I)</option>
                <option value="ibuprofene">Ibuprofène (Palier I)</option>
                <option value="celecoxib">Célécoxib (Sélectif COX-2)</option>
                <option value="codeine">Codéine (Palier II)</option>
                <option value="tramadol">Tramadol (Palier II)</option>
                <option value="morphine">Morphine (Palier III)</option>
                <option value="fentanyl">Fentanyl (Palier III)</option>
                <option value="naloxone">Naloxone (Antidote)</option>
              </select>
            </div>

            <div class="flex items-center space-x-1 text-xs">
              <button onclick="set3dStyle('stick')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold border border-slate-300">Bâtonnets</button>
              <button onclick="set3dStyle('sphere')" class="px-2.5 py-1 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold border border-slate-300">Sphères CPK</button>
            </div>
          </div>

          <div id="g3d-container" class="border border-slate-200 shadow-inner"></div>
          <p class="text-[11px] text-slate-400 text-center">Faites glisser pour tourner • Molette ou pincement pour zoomer</p>
        </div>

        <!-- Tab 2 : Simulateur PK -->
        <div id="tools-panel-pk" class="hidden space-y-4">
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 text-xs">
            <div class="bg-slate-50 p-3 rounded-xl border border-slate-200 space-y-1">
              <span class="text-slate-500 font-bold block">Dose unitaire (mg) :</span>
              <input type="range" id="pk-dose" min="200" max="2000" step="100" value="1000" oninput="updatePkChart()" class="w-full accent-blue-800">
              <span id="pk-dose-val" class="font-mono text-blue-900 font-bold">1000 mg</span>
            </div>
            <div class="bg-slate-50 p-3 rounded-xl border border-slate-200 space-y-1">
              <span class="text-slate-500 font-bold block">Intervalle (&tau;) :</span>
              <input type="range" id="pk-tau" min="4" max="24" step="2" value="6" oninput="updatePkChart()" class="w-full accent-blue-800">
              <span id="pk-tau-val" class="font-mono text-blue-900 font-bold">Toutes les 6h</span>
            </div>
            <div class="bg-slate-50 p-3 rounded-xl border border-slate-200 space-y-1">
              <span class="text-slate-500 font-bold block">Fonction Rénale (DFG) :</span>
              <input type="range" id="pk-dfg" min="15" max="120" step="5" value="110" oninput="updatePkChart()" class="w-full accent-emerald-700">
              <span id="pk-dfg-val" class="font-mono text-emerald-800 font-bold">110 mL/min</span>
            </div>
          </div>

          <div class="h-64 relative bg-slate-50 p-3 rounded-xl border border-slate-200">
            <canvas id="pkChart"></canvas>
          </div>
        </div>

      </div>

    </div>
  </div>

  <!-- JAVASCRIPT LOGIC & EMBEDDED DATABASES -->
  <script>
    const PHARMA_DB = %PHARMA_DB_JSON%;
    const SDF_DATA = %SDF_DATA_JSON%;
    const CLINICAL_CASES = %CLINICAL_CASES_JSON%;
    const SRS_CARDS = %SRS_CARDS_JSON%;

    let currentCategory = 'all';
    let currentDrugFor3d = 'paracetamol';
    let viewer3d = null;
    let pkChartInstance = null;
    let srsActiveDeck = [...SRS_CARDS];
    let srsIndex = 0;

    document.addEventListener('DOMContentLoaded', () => {
      renderDrugCards();
      loadCase(1);
      initSrsCard();
      safeCreateIcons();
    });

    function safeCreateIcons() {
      if (window.lucide && lucide.createIcons) {
        lucide.createIcons();
      }
    }

    function switchMasterTab(tabId) {
      const sections = ['drugs', 'rules', 'cases', 'flashcards'];
      sections.forEach(s => {
        const secEl = document.getElementById(`sec-${s}`);
        if (secEl) {
          if (s === tabId) secEl.classList.remove('hidden');
          else secEl.classList.add('hidden');
        }
        const deskBtn = document.getElementById(`desk-btn-${s}`);
        if (deskBtn) {
          if (s === tabId) deskBtn.classList.add('active');
          else deskBtn.classList.remove('active');
        }
        const mobBtn = document.getElementById(`mob-btn-${s}`);
        if (mobBtn) {
          if (s === tabId) mobBtn.classList.add('active');
          else mobBtn.classList.remove('active');
        }
      });
      window.scrollTo({ top: 0, behavior: 'smooth' });
      safeCreateIcons();
    }

    function renderDrugCards() {
      const grid = document.getElementById('drugs-grid');
      if (!grid) return;
      grid.innerHTML = '';

      const query = (document.getElementById('drug-search')?.value || '').toLowerCase().trim();

      const filtered = PHARMA_DB.molecules.filter(m => {
        if (currentCategory === 'palier1' && m.palier !== 1) return false;
        if (currentCategory === 'palier2' && m.palier !== 2) return false;
        if (currentCategory === 'palier3' && m.palier !== 3) return false;
        if (currentCategory === 'adjuvants' && m.palier !== 4 && m.palier !== 'antidote' && m.palier !== 0) return false;

        if (query) {
          const matchName = m.name.toLowerCase().includes(query);
          const matchDci = m.dci.toLowerCase().includes(query);
          const matchBrands = m.brand_names.some(b => b.toLowerCase().includes(query));
          if (!matchName && !matchDci && !matchBrands) return false;
        }
        return true;
      });

      if (filtered.length === 0) {
        grid.innerHTML = `
          <div class="col-span-full py-12 text-center text-slate-400">
            <i data-lucide="search-x" class="w-8 h-8 mx-auto mb-2 opacity-50"></i>
            <p class="text-xs">Aucun médicament ne correspond à votre recherche.</p>
          </div>
        `;
        safeCreateIcons();
        return;
      }

      filtered.forEach(m => {
        let badgeClass = "bg-blue-50 text-blue-800 border-blue-200";
        if (m.palier === 2) badgeClass = "bg-amber-50 text-amber-800 border-amber-200";
        else if (m.palier === 3) badgeClass = "bg-rose-50 text-rose-800 border-rose-200";
        else if (m.palier === 4 || m.palier === 'antidote' || m.palier === 0) badgeClass = "bg-emerald-50 text-emerald-800 border-emerald-200";

        const brands = m.brand_names.slice(0, 2).join(', ');
        const card = document.createElement('div');
        card.className = "bg-white border border-slate-200/90 rounded-2xl p-4 sm:p-5 shadow-sm hover:shadow-md transition flex flex-col justify-between space-y-3";
        
        card.innerHTML = `
          <div class="space-y-2">
            <div class="flex items-start justify-between gap-2">
              <div>
                <h3 class="font-extrabold text-slate-900 text-sm sm:text-base tracking-tight">${m.name}</h3>
                <p class="text-[11px] text-slate-500 font-medium">${brands || m.class_name}</p>
              </div>
              <span class="px-2 py-0.5 rounded-md text-[10px] font-bold uppercase border ${badgeClass} shrink-0">
                ${m.palier_label || 'Palier I'}
              </span>
            </div>

            <div class="space-y-1.5 pt-1 text-xs">
              <div class="flex items-start space-x-1.5">
                <span class="text-blue-700 font-bold shrink-0">💊 Poso :</span>
                <span class="text-slate-700 font-medium line-clamp-2">${m.posology?.adult || 'Selon prescription'}</span>
              </div>
              <div class="flex items-start space-x-1.5">
                <span class="text-rose-700 font-bold shrink-0">🚫 CI :</span>
                <span class="text-slate-700 font-medium line-clamp-2">${m.contraindications?.[0] || 'Hypersensibilité'}</span>
              </div>
              <div class="flex items-start space-x-1.5">
                <span class="text-emerald-700 font-bold shrink-0">💡 Règle :</span>
                <span class="text-slate-700 font-medium line-clamp-2">${m.concours_pearl || m.pharmacodynamics?.mechanism?.slice(0, 100) + '...'}</span>
              </div>
            </div>
          </div>

          <button onclick="openDrugDrawer('${m.id}')" class="w-full mt-2 py-2 px-3 rounded-xl bg-slate-50 hover:bg-blue-50 text-blue-900 hover:text-blue-800 text-xs font-bold border border-slate-200 hover:border-blue-300 transition flex items-center justify-center space-x-1.5">
            <span>Fiche Complète &amp; 3D</span>
            <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
          </button>
        `;
        grid.appendChild(card);
      });

      safeCreateIcons();
    }

    function filterCategory(cat) {
      currentCategory = cat;
      document.querySelectorAll('.cat-pill').forEach(btn => {
        if (btn.id === `cat-${cat}`) {
          btn.className = "cat-pill active px-3 py-1.5 rounded-lg bg-blue-800 text-white font-bold whitespace-nowrap shadow-sm";
        } else {
          btn.className = "cat-pill px-3 py-1.5 rounded-lg bg-slate-100 text-slate-600 hover:bg-slate-200 whitespace-nowrap";
        }
      });
      renderDrugCards();
    }

    function filterDrugs() {
      renderDrugCards();
    }

    function openDrugDrawer(drugId) {
      const drug = PHARMA_DB.molecules.find(m => m.id === drugId);
      if (!drug) return;

      currentDrugFor3d = drug.id;

      document.getElementById('drawer-title').textContent = drug.name;
      document.getElementById('drawer-brands').textContent = drug.brand_names.join(', ') || drug.dci;
      document.getElementById('drawer-palier').textContent = drug.palier_label;
      document.getElementById('drawer-legal').textContent = drug.legal_status || 'Non soumis à prescription';

      document.getElementById('drawer-poso-adult').textContent = drug.posology?.adult || 'Non renseigné';
      document.getElementById('drawer-poso-ped').textContent = drug.posology?.pediatric || 'Contre-indiqué ou non adapté';
      document.getElementById('drawer-poso-renal').textContent = drug.posology?.renal_adjustment || 'Aucun ajustement nécessaire';
      document.getElementById('drawer-poso-elderly').textContent = drug.posology?.elderly || 'Dose adulte habituelle avec prudence';

      const ciBox = document.getElementById('drawer-ci');
      ciBox.innerHTML = '';
      (drug.contraindications || []).forEach(ci => {
        const li = document.createElement('li');
        li.textContent = `• ${ci}`;
        ciBox.appendChild(li);
      });

      const precBox = document.getElementById('drawer-precautions');
      precBox.innerHTML = '';
      (drug.precautions || []).forEach(pr => {
        const li = document.createElement('li');
        li.textContent = `• ${pr}`;
        precBox.appendChild(li);
      });

      const interBox = document.getElementById('drawer-interactions');
      interBox.innerHTML = '';
      (drug.interactions || []).forEach(inter => {
        const div = document.createElement('div');
        div.className = "p-2.5 rounded-lg bg-slate-50 border border-slate-200 space-y-0.5";
        div.innerHTML = `
          <strong class="text-slate-900 block">${inter.drug} (${inter.level})</strong>
          <span class="text-slate-600">${inter.mechanism}</span>
        `;
        interBox.appendChild(div);
      });

      document.getElementById('drawer-pk-f').textContent = drug.pk?.bioavailability || 'N/A';
      document.getElementById('drawer-pk-tmax').textContent = drug.pk?.tmax || 'N/A';
      document.getElementById('drawer-pk-t12').textContent = drug.pk?.halflife || 'N/A';
      document.getElementById('drawer-metab-path').textContent = drug.metabolism?.pathways || 'N/A';
      
      const toxBox = document.getElementById('drawer-metab-tox-box');
      if (drug.metabolism?.toxic_intermediate) {
        toxBox.classList.remove('hidden');
        document.getElementById('drawer-metab-tox').textContent = drug.metabolism.toxic_intermediate;
      } else {
        toxBox.classList.add('hidden');
      }

      document.getElementById('drawer-pearl').textContent = drug.concours_pearl || drug.pharmacodynamics?.mechanism;

      const has3d = !!SDF_DATA[drug.id];
      const banner3d = document.getElementById('drawer-3d-banner');
      if (has3d) banner3d.classList.remove('hidden');
      else banner3d.classList.add('hidden');

      document.getElementById('drug-drawer-backdrop').classList.remove('hidden');
      document.getElementById('drug-drawer').classList.remove('translate-x-full');
      safeCreateIcons();
    }

    function closeDrugDrawer() {
      document.getElementById('drug-drawer-backdrop').classList.add('hidden');
      document.getElementById('drug-drawer').classList.add('translate-x-full');
    }

    function open3dForCurrentDrug() {
      closeDrugDrawer();
      openToolsModal();
      switchToolsTab('3d');
      if (SDF_DATA[currentDrugFor3d]) {
        document.getElementById('mol-select').value = currentDrugFor3d;
        render3D(currentDrugFor3d);
      }
    }

    function loadCase(caseId) {
      const c = CLINICAL_CASES.find(item => item.id === caseId);
      if (!c) return;

      document.getElementById('case-select').value = caseId;
      document.getElementById('case-avatar').textContent = c.id;
      document.getElementById('case-title').textContent = c.title;
      document.getElementById('case-context').textContent = c.context;
      document.getElementById('case-rx-patient').textContent = c.rx_patient;
      document.getElementById('case-rx-lines').innerHTML = c.rx_lines.replace(/\\n/g, '<br>');
      document.getElementById('case-pearl-text').textContent = c.pearl;

      document.getElementById('case-status-badge').textContent = "En attente de décision";
      document.getElementById('case-status-badge').className = "px-2.5 py-1 rounded-full text-xs font-bold bg-slate-100 text-slate-600 border border-slate-200";

      const optBox = document.getElementById('case-options-box');
      optBox.innerHTML = '';

      c.options.forEach((opt, idx) => {
        const btn = document.createElement('button');
        btn.className = "w-full p-3 rounded-xl bg-slate-50 hover:bg-blue-50 border border-slate-200 hover:border-blue-300 text-left text-xs font-semibold text-slate-800 transition";
        btn.textContent = opt.text;
        btn.onclick = () => selectCaseOption(caseId, idx);
        optBox.appendChild(btn);
      });

      const fb = document.getElementById('case-feedback-box');
      fb.classList.add('hidden');
      fb.innerHTML = '';
      safeCreateIcons();
    }

    function selectCaseOption(caseId, idx) {
      const c = CLINICAL_CASES.find(item => item.id === caseId);
      const opt = c.options[idx];
      const fb = document.getElementById('case-feedback-box');

      fb.classList.remove('hidden');
      if (opt.correct) {
        fb.className = "p-4 rounded-xl bg-emerald-50 border border-emerald-300 text-xs text-emerald-900 leading-relaxed";
        document.getElementById('case-status-badge').textContent = opt.status;
        document.getElementById('case-status-badge').className = "px-2.5 py-1 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800 border border-emerald-300";
      } else {
        fb.className = "p-4 rounded-xl bg-rose-50 border border-rose-300 text-xs text-rose-900 leading-relaxed";
        document.getElementById('case-status-badge').textContent = opt.status;
        document.getElementById('case-status-badge').className = "px-2.5 py-1 rounded-full text-xs font-bold bg-rose-100 text-rose-800 border border-rose-300";
      }

      fb.innerHTML = `<strong>Diagnostic de Validation :</strong><br>${opt.feedback}`;
    }

    function initSrsCard() {
      if (!srsActiveDeck.length) return;
      const card = srsActiveDeck[srsIndex];
      document.getElementById('srs-tag').textContent = card.tag;
      document.getElementById('srs-index').textContent = `Carte ${srsIndex + 1} sur ${srsActiveDeck.length}`;
      document.getElementById('srs-progress').textContent = `${srsIndex + 1} / ${srsActiveDeck.length}`;
      document.getElementById('srs-question').textContent = card.q;
      document.getElementById('srs-hint').textContent = `Indice : ${card.hint}`;
      document.getElementById('srs-answer').textContent = card.a;
      document.getElementById('srs-pearl').textContent = card.pearl;

      document.getElementById('srs-back').classList.add('hidden');
      document.getElementById('srs-btn-reveal').classList.remove('hidden');
      document.getElementById('srs-ratings').classList.add('hidden');
    }

    function revealSrs() {
      document.getElementById('srs-back').classList.remove('hidden');
      document.getElementById('srs-btn-reveal').classList.add('hidden');
      document.getElementById('srs-ratings').classList.remove('hidden');
    }

    function rateSrs(rating) {
      srsIndex = (srsIndex + 1) % srsActiveDeck.length;
      initSrsCard();
    }

    function resetSrs() {
      srsIndex = 0;
      initSrsCard();
    }

    function filterSrs(cat) {
      if (cat === 'all') srsActiveDeck = [...SRS_CARDS];
      else srsActiveDeck = SRS_CARDS.filter(c => c.cat === cat);
      srsIndex = 0;

      document.querySelectorAll('.srs-cat').forEach(b => {
        if (b.id === `srs-btn-${cat}`) {
          b.className = "srs-cat active px-3 py-1.5 rounded-lg bg-blue-800 text-white font-bold whitespace-nowrap shadow-sm";
        } else {
          b.className = "srs-cat px-3 py-1.5 rounded-lg bg-white border border-slate-200 text-slate-600 hover:bg-slate-50 whitespace-nowrap";
        }
      });

      document.getElementById('srs-count').textContent = `${srsActiveDeck.length} cartes`;
      initSrsCard();
    }

    function openToolsModal() {
      document.getElementById('tools-modal').classList.remove('hidden');
      setTimeout(() => {
        render3D(document.getElementById('mol-select').value);
      }, 100);
      safeCreateIcons();
    }

    function closeToolsModal() {
      document.getElementById('tools-modal').classList.add('hidden');
    }

    function switchToolsTab(tab) {
      const p3d = document.getElementById('tools-panel-3d');
      const ppk = document.getElementById('tools-panel-pk');
      const b3d = document.getElementById('tools-tab-btn-3d');
      const bpk = document.getElementById('tools-tab-btn-pk');

      if (tab === '3d') {
        p3d.classList.remove('hidden');
        ppk.classList.add('hidden');
        b3d.className = "pb-2.5 px-3 border-b-2 border-blue-800 text-blue-800 font-bold transition";
        bpk.className = "pb-2.5 px-3 border-b-2 border-transparent text-slate-500 hover:text-slate-800 transition";
        setTimeout(() => { render3D(document.getElementById('mol-select').value); }, 50);
      } else {
        p3d.classList.add('hidden');
        ppk.classList.remove('hidden');
        bpk.className = "pb-2.5 px-3 border-b-2 border-blue-800 text-blue-800 font-bold transition";
        b3d.className = "pb-2.5 px-3 border-b-2 border-transparent text-slate-500 hover:text-slate-800 transition";
        setTimeout(() => { updatePkChart(); }, 50);
      }
    }

    function render3D(molKey) {
      const sdf = SDF_DATA[molKey];
      const container = document.getElementById('g3d-container');
      if (!sdf || !container) return;

      container.innerHTML = '';
      viewer3d = $3Dmol.createViewer(container, { backgroundColor: 'white' });
      viewer3d.addModel(sdf, 'sdf');
      viewer3d.setStyle({}, { stick: { radius: 0.2, colorscheme: 'Jmol' } });
      viewer3d.zoomTo();
      viewer3d.render();
      viewer3d.spin('y', 0.5);
    }

    function set3dStyle(style) {
      if (!viewer3d) return;
      if (style === 'sphere') {
        viewer3d.setStyle({}, { sphere: { scale: 0.3, colorscheme: 'Jmol' } });
      } else {
        viewer3d.setStyle({}, { stick: { radius: 0.2, colorscheme: 'Jmol' } });
      }
      viewer3d.render();
    }

    function updatePkChart() {
      const dose = parseFloat(document.getElementById('pk-dose').value);
      const tau = parseFloat(document.getElementById('pk-tau').value);
      const dfg = parseFloat(document.getElementById('pk-dfg').value);

      document.getElementById('pk-dose-val').textContent = `${dose} mg`;
      document.getElementById('pk-tau-val').textContent = `Toutes les ${tau}h`;
      document.getElementById('pk-dfg-val').textContent = `${dfg} mL/min`;

      const ctx = document.getElementById('pkChart')?.getContext('2d');
      if (!ctx) return;

      const labels = [];
      const data = [];
      const ke = 0.25 * (dfg / 100);
      const ka = 1.8;
      const vd = 0.9 * 70;

      for (let t = 0; t <= 48; t += 0.5) {
        labels.push(`${t}h`);
        let c = 0;
        for (let doseTime = 0; doseTime <= t; doseTime += tau) {
          const dt = t - doseTime;
          c += (dose / vd) * (ka / (ka - ke)) * (Math.exp(-ke * dt) - Math.exp(-ka * dt));
        }
        data.push(Math.max(0, c).toFixed(1));
      }

      if (pkChartInstance) {
        pkChartInstance.destroy();
      }

      pkChartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: 'Concentration Sérique C(t) mg/L',
            data: data,
            borderColor: '#1e40af',
            backgroundColor: 'rgba(30, 64, 175, 0.08)',
            fill: true,
            tension: 0.3,
            borderWidth: 2,
            pointRadius: 0
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false }
          },
          scales: {
            x: { ticks: { maxTicksLimit: 12, font: { size: 10 } } },
            y: { title: { display: true, text: 'mg / L', font: { size: 10 } }, font: { size: 10 } }
          }
        }
      });
    }

    let deferredPrompt;
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      deferredPrompt = e;
      const btn = document.getElementById('btn-pwa-install');
      if (btn) btn.classList.remove('hidden');
    });

    function triggerPWAInstall() {
      if (deferredPrompt) {
        deferredPrompt.prompt();
        deferredPrompt.userChoice.then(() => {
          deferredPrompt = null;
          document.getElementById('btn-pwa-install').classList.add('hidden');
        });
      }
    }

    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('sw.js').catch(err => console.log('SW reg error:', err));
    }
  </script>
</body>
</html>
"""

# Replace placeholders with JSON strings
final_html = html_template.replace(
    '%PHARMA_DB_JSON%', json.dumps(pharma_db, ensure_ascii=False)
).replace(
    '%SDF_DATA_JSON%', json.dumps(all_sdfs, ensure_ascii=False)
).replace(
    '%CLINICAL_CASES_JSON%', json.dumps(CLINICAL_CASES, ensure_ascii=False)
).replace(
    '%SRS_CARDS_JSON%', json.dumps(SRS_CARDS, ensure_ascii=False)
)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Successfully generated clean DFGSP3 index.html ({len(final_html)} bytes)")
