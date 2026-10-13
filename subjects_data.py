# -*- coding: utf-8 -*-
"""
DFGSP3 Subjects & Course Catalog
Faculté de Pharmacie de Bamako (USTTB)
UKM Pharmacie 3 • 2025-2026
"""

SUBJECTS_DATA = [
    {
        'id': 'pharmacologie',
        'name': 'Pharmacologie',
        'icon': 'pill',
        'color': 'blue',
        'badge_color': 'bg-blue-50 text-blue-800 border-blue-200',
        'dept': 'DER Sciences du Médicament • Faculté de Pharmacie USTTB',
        'teachers': 'Pr Sékou BAH (Maître de Conférences) • Dr Karim TRAORE • Dr Abdoulaye GUINDO',
        'badge': 'DFGSP3 • Fondamental & Clinique',
        'courses': [
            {
                'id': 'pharmaco_cours1',
                'title': 'Cours 1 : Notions Générales de Pharmacologie',
                'teacher': 'Pr Sékou BAH',
                'pages': 21,
                'file': 'cours/pharmacologie/cours1_notions_generales_pharmacologie.pdf',
                'badge': 'Cours Magistral Clé',
                'summary': [
                    'Étymologie fondamentale : Mot grec composé de « Pharmakon » (remède, poison) et « Logos » (discours, science raisonnée).',
                    'Objectif central : Étude des interactions entre les substances chimiques actives et les systèmes vivants (organismes sains ou pathologiques).',
                    'Les deux piliers de la pharmacologie : 1) Pharmacocinétique (PK) = devenir du principe actif dans l\'organisme (Absorption, Distribution, Métabolisme, Élimination - ADME) ; 2) Pharmacodynamie (PD) = effets biochimiques, physiologiques et mécanismes d\'action sur les récepteurs/cibles.',
                    'Disciplines frontières : Chimie thérapeutique (synthèse et RSA), Pharmacognosie (matière médicale naturelle végétale/animale), Pharmacologie clinique et Pharmacovigilance.',
                    'Définition légale du médicament : Toute substance ou composition présentée comme possédant des propriétés curatives ou préventives à l\'égard des maladies humaines, ainsi que toute substance pouvant être administrée en vue d\'établir un diagnostic médical ou de restaurer, corriger ou modifier des fonctions physiologiques.'
                ],
                'quiz': [
                    {
                        'q': 'Quelle est la différence fondamentale entre Pharmacocinétique et Pharmacodynamie ?',
                        'a': 'La Pharmacocinétique (PK) décrit ce que l\'organisme fait au médicament (processus ADME : Absorption, Distribution, Métabolisme, Élimination). La Pharmacodynamie (PD) décrit ce que le médicament fait à l\'organisme (mécanismes moléculaires d\'action, affinité réceptorielle, efficacité et effets thérapeutiques/toxiques).'
                    },
                    {
                        'q': 'Comment la Pharmacopée définit-elle légalement le médicament ?',
                        'a': 'Toute substance ou composition présentée comme possédant des propriétés curatives ou préventives à l\'égard des maladies humaines ou animales, ou pouvant être utilisée en vue d\'établir un diagnostic médical ou de restaurer, corriger ou modifier des fonctions physiologiques.'
                    },
                    {
                        'q': 'Quel est le rôle primordial de la Pharmacovigilance selon le cours du Pr BAH ?',
                        'a': 'La détection, l\'évaluation, la compréhension et la prévention des risques d\'effets indésirables ou de tout autre problème lié à l\'utilisation du médicament après sa mise sur le marché.'
                    }
                ]
            }
        ],
        'has_pharma_modules': True
    },
    {
        'id': 'immunologie',
        'name': 'Immunologie',
        'icon': 'shield',
        'color': 'indigo',
        'badge_color': 'bg-indigo-50 text-indigo-800 border-indigo-200',
        'dept': 'PMRTC • Faculté de Pharmacie USTTB',
        'teachers': 'Pr Charles ARAMA (PharmD, MSc, PhD • MCA)',
        'badge': 'UKM Pharmacie 3 • 2025-2026',
        'courses': [
            {
                'id': 'immuno_intro',
                'title': 'Cours 1 : Introduction à l\'Immunologie (Histoire & Évolution)',
                'teacher': 'Pr Charles ARAMA',
                'pages': 42,
                'file': 'cours/immunologie/intro_immunologie_histoire_evolution.pdf',
                'badge': 'Histoire & Fondements',
                'summary': [
                    'Objectif 1 (Exam) : Citer 4 noms célèbres ayant révolutionné l\'immunologie : Edward Jenner, Louis Pasteur, Emil von Behring, Elie Metchnikov et Paul Ehrlich.',
                    'Objectif 2 (Exam) : 4 étapes historiques majeures : 1) La variolisation puis la vaccination antivariolique par Jenner (1796, virus de la vaccine) ; 2) Les vaccins vivants atténués de Pasteur (1880 choléra aviaire, 1885 vaccin antirabique chez Joseph Meister) ; 3) La découverte de la phagocytose cellulaire par Metchnikov (1883) ; 4) La découverte de la sérothérapie et des antitoxines/anticorps par Von Behring & Kitasato (1890, diphtérie et tétanos).',
                    'Paul Ehrlich et la théorie des chaînes latérales (précurseur de la sélection clonale des récepteurs d\'anticorps).',
                    'Grandes avancées du XXe siècle : Groupes sanguins ABO (Karl Landsteiner, 1901), Découverte du Complexe Majeur d\'Histocompatibilité (HLA/CMH par Jean Dausset, 1958), et réarrangement des gènes des immunoglobulines (Susumu Tonegawa, 1976).'
                ],
                'quiz': [
                    {
                        'q': 'Citez 4 savants historiques incontournables et leurs découvertes majeures en immunologie :',
                        'a': '1) Edward Jenner (1796 : 1re vaccination avec la vaccine contre la variole) ; 2) Louis Pasteur (1885 : atténuation des germes et vaccin contre la rage) ; 3) Elie Metchnikov (1883 : découverte de la phagocytose et immunité cellulaire) ; 4) Emil von Behring (1890 : découverte des anticorps sériques antitoxines diphtérique/tétanique).'
                    },
                    {
                        'q': 'Quelle théorie fondamentale Paul Ehrlich a-t-il proposée au début du XXe siècle ?',
                        'a': 'La théorie des chaînes latérales (Side-chain theory), postulant que les cellules expriment à leur surface des récepteurs spécifiques capables de lier des toxines et d\'être sécrétés sous forme d\'anticorps en excès dans le sérum.'
                    },
                    {
                        'q': 'Qui a découvert le système HLA / CMH et quelle est sa signification biologique ?',
                        'a': 'Jean Dausset (Prix Nobel 1980). Le système HLA (Human Leukocyte Antigen) / CMH correspond aux molécules de surface qui présentent les peptides antigéniques aux lymphocytes T et déterminent la compatibilité des greffes.'
                    }
                ]
            },
            {
                'id': 'immuno_concept',
                'title': 'Cours 2 : Concept d\'Immunité & Système Immunitaire',
                'teacher': 'Pr Charles ARAMA',
                'pages': 36,
                'file': 'cours/immunologie/concept_immunite_ukm.pdf',
                'badge': 'Concepts Clés & Cellules',
                'summary': [
                    'Définition : Système immunitaire = ensemble intégré de molécules, cellules, tissus et organes assurant la défense de l\'organisme contre les agents pathogènes (bactéries, virus, parasites, champignons) et la surveillance antitumorale.',
                    'Immunité Innée (Non spécifique / Naturelle) : Première ligne de défense immédiate (0 à 12h), sans phase de latence, non spécifique d\'antigène, absence de mémoire immunologique. Mécanismes : barrières physico-chimiques (peau, muqueuses), phagocytes (PNN, macrophages), cellules NK, système du complément et cytokines inflammatoires.',
                    'Immunité Adaptative (Spécifique / Acquise) : Mise en jeu retardée (jours), hautement spécifique grâce à des récepteurs clonaux diversifiés (BCR sur LB, TCR sur LT), mémoire immunologique durable. Deux branches : Humorale (LB -> plasmocytes sécrétant des anticorps) et Cellulaire (LT CD4+ auxiliaires et LT CD8+ cytotoxiques).',
                    'Organes lymphoïdes primaires (Centraux) : Moelle osseuse hématopoïétique (site de maturation des lymphocytes B) et Thymus (site de maturation et sélection des lymphocytes T).',
                    'Organes lymphoïdes secondaires (Périphériques) : Ganglions lymphatiques, Rate et MALT (tissus lymphoïdes associés aux muqueuses) où s\'initie la réponse adaptative.'
                ],
                'quiz': [
                    {
                        'q': 'Quelles sont les 4 différences fondamentales entre Immunité Innée et Immunité Adaptative ?',
                        'a': '1) Délai de réponse : Immédiate (0-12h) pour l\'innée vs Retardée (plusieurs jours) pour l\'adaptative ; 2) Spécificité : Motifs microbiens généraux (PAMPs via PRR) pour l\'innée vs Épitopes antigéniques très précis pour l\'adaptative ; 3) Mémoire immunologique : Absente pour l\'innée vs Présente et durable pour l\'adaptative ; 4) Récepteurs : Invariants encodés dans la lignée germinale vs Réarrangés de manière clonale (BCR/TCR).'
                    },
                    {
                        'q': 'Quels sont les deux organes lymphoïdes primaires et quelle est leur fonction respective ?',
                        'a': 'La Moelle Osseuse (génération de tous les éléments figurés du sang et maturation des Lymphocytes B) et le Thymus (maturation, sélection positive et négative des Lymphocytes T afin d\'éliminer les clones autoréactifs).'
                    }
                ]
            }
        ],
        'has_pharma_modules': False
    },
    {
        'id': 'biochimie',
        'name': 'Biochimie Clinique',
        'icon': 'dna',
        'color': 'emerald',
        'badge_color': 'bg-emerald-50 text-emerald-800 border-emerald-200',
        'dept': 'Laboratoire de Biochimie Médicale • Faculté de Pharmacie USTTB',
        'teachers': 'Pr Bakary CISSÉ • Pr Yaya GOITA',
        'badge': 'DFGSP3 • Métabolisme Glucidique',
        'courses': [
            {
                'id': 'bioch_glucides',
                'title': 'Cours : Métabolisme et Troubles Métaboliques Glucidiques',
                'teacher': 'Pr Bakary CISSÉ & Pr Yaya GOITA',
                'pages': 42,
                'file': 'cours/biochimie/metabolisme_troubles_glucidiques.pdf',
                'badge': 'Métabolisme & Diabète',
                'summary': [
                    'Rôle physiologique du glucose : Carburant énergétique indispensable de l\'organisme, substrat obligatoire exclusif du cerveau et des hématies.',
                    'Les 4 voies métaboliques fondamentales : 1) Glycolyse (voie d\'oxydation du glucose en pyruvate en aérobiose ou lactate en anaérobiose, production d\'ATP) ; 2) Néoglucogenèse hépatique et rénale (synthèse de novo de glucose à partir de lactate, glycérol et acides aminés glucoformateurs comme l\'alanine) ; 3) Glycogénogenèse (stockage sous forme de glycogène dans le foie et les muscles) ; 4) Glycogénolyse (libération rapide de glucose-6-phosphate).',
                    'Régulation hormonale : L\'Insuline (cellules bêta pancréatiques) est la SEULE hormone hypoglycémiante de l\'organisme (favorise captation périphérique via GLUT4, glycolyse et glycogénogenèse). Les hormones de contre-régulation hyperglycémiantes : Glucagon, Adrénaline, Cortisol et Hormone de croissance (GH).',
                    'Critères diagnostiques OMS du Diabète Sucré : 1) Glycémie à jeun ≥ 1,26 g/L (7,0 mmol/L) vérifiée à 2 reprises ; OU 2) Glycémie aléatoire ≥ 2,00 g/L (11,1 mmol/L) avec syndrome polyuro-polydipsique ; OU 3) HbA1c ≥ 6,5% (48 mmol/mol).',
                    'Différenciation clinique et métabolique : Diabète de Type 1 (carence absolue en insuline par destruction auto-immune des cellules bêta, sujet jeune mince, tendance à l\'acidocétose) vs Diabète de Type 2 (insulinorésistance périphérique associée à une insulinopénie relative, sujet mature souvent en surpoids).'
                ],
                'quiz': [
                    {
                        'q': 'Quels sont les 3 critères diagnostiques biologiques officiels du Diabète selon l\'OMS ?',
                        'a': '1) Glycémie à jeun (après 8h de jeûne) ≥ 1,26 g/L (7,0 mmol/L) confirmée à deux reprises ; OU 2) Glycémie veineuse à n\'importe quel moment de la journée ≥ 2,00 g/L (11,1 mmol/L) avec symptômes cardinaux (polyurie, polydipsie, amaigrissement) ; OU 3) Hémoglobine glyquée (HbA1c) ≥ 6,5%.'
                    },
                    {
                        'q': 'Pourquoi l\'insuline est-elle qualifiée d\'unique hormone hypoglycémiante ?',
                        'a': 'Parce qu\'elle est la seule hormone capable d\'abaisser la glycémie sanguine en stimulant l\'entrée cellulaire du glucose (transporteurs GLUT4 musculaires et adipeux), en activant la glycolyse et la glycogénogenèse, tout en inhibant la néoglucogenèse et la glycogénolyse hépatiques.'
                    },
                    {
                        'q': 'Quels sont les principaux substrats glucoformateurs de la Néoglucogenèse ?',
                        'a': 'Le Lactate (via le cycle de Cori), le Glycérol (issu de l\'hydrolyse des triglycérides adipeux), et les Acides Aminés glucoformateurs (principalement l\'Alanine via le cycle glucose-alanine, et la Glutamine).'
                    }
                ]
            }
        ],
        'has_pharma_modules': False
    },
    {
        'id': 'galenique',
        'name': 'Pharmacie Galénique',
        'icon': 'flask-conical',
        'color': 'teal',
        'badge_color': 'bg-teal-50 text-teal-800 border-teal-200',
        'dept': 'DER Sciences Pharmaceutiques • Faculté de Pharmacie USTTB',
        'teachers': 'Dr Hamma MAIGA',
        'badge': 'DFGSP3 • Formes Sèches',
        'courses': [
            {
                'id': 'galen_poudres',
                'title': 'Cours N°1 : Les Formes Sèches — Les Poudres',
                'teacher': 'Dr Hamma MAIGA',
                'pages': 48,
                'file': 'cours/galenique/cours_poudres_formes_seches.pdf',
                'badge': 'Technologie & Formulations',
                'summary': [
                    'Définition Pharmacopée : Préparations solides constituées de particules solides, sèches, libres et plus ou moins fines, obtenues par pulvérisation de substances végétales, animales ou chimiques.',
                    'Classification : Poudres simples (constituées d\'une seule substance médicamenteuse active) vs Poudres composées (mélange de plusieurs principes actifs ou principes actifs + excipients de charge/diluants).',
                    'Intérêt et applications : Forme galénique finale (poudres orales en sachets, poudres pour application cutanée) ou intermédiaire indispensable pour la fabrication de la quasi-totalité des formes pharmaceutiques sèches (comprimés par compression, gélules par remplissage, suspensions).',
                    'Paramètre clé de la Granulométrie : La taille et la forme des particules conditionnent directement la surface spécifique de contact, la vitesse de dissolution (équation de Noyes-Whitney), la biodisponibilité du principe actif, ainsi que l\'aptitude à l\'écoulement (coulabilité) et à la compression.',
                    'Opérations fondamentales : 1) Division / Pulvérisation (broyage par écrasement, percussion ou cisaillement) ; 2) Tamisage (calibrage dimensionnel à l\'aide de tamis normalisés selon la Pharmacopée) ; 3) Mélangeage (obtention d\'un mélange homogène selon la règle des dilutions géométriques).'
                ],
                'quiz': [
                    {
                        'q': 'Comment la Pharmacopée définit-elle les poudres pharmaceutiques ?',
                        'a': 'Des préparations solides constituées de particules solides, sèches, libres et plus ou moins fines. Elles peuvent être simples (un seul constituant) ou composées (mélange de plusieurs substances).'
                    },
                    {
                        'q': 'Pourquoi la granulométrie est-elle cruciale pour l\'efficacité thérapeutique d\'un médicament sous forme de poudre ?',
                        'a': 'Une réduction de la taille des particules augmente la surface spécifique exposée aux sucs digestifs. Selon l\'équation de Noyes-Whitney, la vitesse de dissolution augmente proportionnellement à cette surface, ce qui accélère l\'absorption digestive et optimise la biodisponibilité du principe actif.'
                    },
                    {
                        'q': 'Qu\'est-ce que la règle des dilutions géométriques lors du mélange de poudres ?',
                        'a': 'Une méthode consistant à mélanger le principe actif minoritaire avec une quantité égale d\'excipient diluant, puis à doubler à chaque étape le volume ajouté afin de garantir une dispersion rigoureusement homogène des composants sans surdosage localisé.'
                    }
                ]
            }
        ],
        'has_pharma_modules': False
    },
    {
        'id': 'chimie_therapeutique',
        'name': 'Chimie Thérapeutique',
        'icon': 'atom',
        'color': 'purple',
        'badge_color': 'bg-purple-50 text-purple-800 border-purple-200',
        'dept': 'DER Chimie Thérapeutique • Faculté de Pharmacie USTTB',
        'teachers': 'Pr Ousmane DOUMBIA • Pr Dominique P. ARAMA',
        'badge': 'DFGSP3 • Chimie Médicinale',
        'courses': [
            {
                'id': 'chimie_intro',
                'title': 'Cours 1 : Introduction à la Chimie Médicinale',
                'teacher': 'Pr Ousmane DOUMBIA & Pr Dominique P. ARAMA',
                'pages': 42,
                'file': 'cours/chimie_therapeutique/intro_chimie_medicinale.pdf',
                'badge': 'RSA & Pharmacophore',
                'summary': [
                    'Définition : La Chimie Thérapeutique (Chimie Médicinale ou Pharmacie Chimique) a pour objet l\'étude des composés chimiques définis utilisés en thérapeutique humaine : structure moléculaire, méthodes de synthèse, propriétés physico-chimiques, stabilité et relations entre structure chimique et activité biologique (RSA).',
                    'Différenciation des 3 piliers pharmaceutiques : 1) Matière Médicale (histoire naturelle des drogues brutes d\'origine végétale ou animale) ; 2) Chimie Thérapeutique (molécules pures, modélisation moléculaire et modifications structurales) ; 3) Pharmacologie (mode d\'action et devenir dans l\'organisme).',
                    'Concept central de Pharmacophore : L\'assemblage tridimensionnel précis des fonctionnalités stériques et électroniques d\'une molécule (donneurs/accepteurs de liaison H, groupements lipophiles aromatiques, centres chargés) strictement indispensables pour déclencher ou bloquer une réponse biologique sur sa cible.',
                    'Relations Structure-Activité (RSA / SAR) : Démarche scientifique consistant à modifier systématiquement certains groupements chimiques d\'une molécule chef de file (lead compound) pour accroître sa puissance, sa sélectivité pour le récepteur, ou diminuer sa toxicité.',
                    'Importance de la Chiralité : Les cibles biologiques étant chirales, les énantiomères (images l\'un de l\'autre dans un miroir) interagissent différemment : l\'eutonmère possède l\'activité désirée tandis que le distomère peut être inactif ou responsable d\'effets indésirables sévères.'
                ],
                'quiz': [
                    {
                        'q': 'Qu\'est-ce qu\'un Pharmacophore en chimie médicinale ?',
                        'a': 'C\'est l\'ensemble des caractéristiques structurales et électroniques tridimensionnelles d\'une molécule (motifs aromatiques, donneurs/accepteurs de liaisons hydrogène, charges) strictement requises pour reconnaître et activer (ou inhiber) sa cible macromoléculaire.'
                    },
                    {
                        'q': 'Comment distingue-t-on Matière Médicale, Chimie Thérapeutique et Pharmacologie ?',
                        'a': 'La Matière Médicale étudie les drogues naturelles brutes d\'origine végétale ou animale ; la Chimie Thérapeutique s\'intéresse aux structures chimiques pures, synthèses et relations structure-activité ; la Pharmacologie étudie l\'action et le métabolisme de ces molécules sur l\'organisme vivant.'
                    },
                    {
                        'q': 'Quelle est l\'importance clinique de la stéréoisomérie optique des principes actifs ?',
                        'a': 'Les récepteurs et enzymes biologiques étant asymétriques et chiraux, deux énantiomères d\'une même molécule peuvent avoir des profils pharmacologiques très différents : l\'un peut être très actif (eutonmère) et l\'autre inactif voire hautement toxique (distomère).'
                    }
                ]
            }
        ],
        'has_pharma_modules': False
    },
    {
        'id': 'semiologie',
        'name': 'Sémiologie Médicale',
        'icon': 'heart-pulse',
        'color': 'rose',
        'badge_color': 'bg-rose-50 text-rose-800 border-rose-200',
        'dept': 'Faculté de Pharmacie & Faculté de Médecine USTTB',
        'teachers': 'Pr Djenebou TRAORE MENTA (Médecine Interne) • Pr Sékou BAH',
        'badge': 'DFGSP3 • Cardio-Vasculaire & Programme',
        'courses': [
            {
                'id': 'semio_cardio',
                'title': 'Cours : Sémiologie de l\'Appareil Cardio-Vasculaire',
                'teacher': 'Pr Djenebou TRAORE MENTA',
                'pages': 18,
                'file': 'cours/semiologie/semiologie_cardiovasculaire.pdf',
                'badge': 'Cardiologie & Examen Clinique',
                'summary': [
                    'Rappels physiologiques : Le cycle cardiaque comprend la systole (contraction ventriculaire et éjection) et la diastole (remplissage ventriculaire). Les bruits physiologiques du cœur à l\'auscultation : B1 (fermeture des valves auriculo-ventriculaires mitrale et tricuspide, début de la systole) et B2 (fermeture des valves sigmoïdes aortique et pulmonaire, fin de la systole).',
                    'Sémiologie fonctionnelle : 1) Douleur thoracique de l\'angor : rétrosternale médiothoracique, constrictive (« en étau »), irradiant vers l\'épaule et le bras gauche, le dos ou la mâchoire, survenant à l\'effort, cédant au repos et à la trinitrine sous la langue en moins de 5 min (si douleur prolongée > 20 min résistante : suspecter un infarctus du myocarde - IDM).',
                    '2) Dyspnée cardiaque : Dyspnée d\'effort évaluée selon la classification NYHA (Stade I à IV), Orthopnée (dyspnée de décubitus imposant au patient de dormir redressé avec plusieurs oreillers, signe cardial de l\'insuffisance cardiaque gauche), Dyspnée paroxystique nocturne (œdème aigu du poumon - OAP).',
                    '3) Signes d\'insuffisance cardiaque droite : Œdèmes des membres inférieurs (OMI : bilatéraux, blancs, mous, indolores, prenant le godet), Turgescence des veines jugulaires et Reflux hépato-jugulaire.',
                    'Signes physiques auscultatoires : Souffles cardiaques (souffles systoliques d\'éjection aortique ou de régurgitation mitrale ; souffles diastoliques d\'insuffisance aortique ou de rétrécissement mitral), Bruits de galop (B3 ou B4 traduisant une défaillance myocardique).'
                ],
                'quiz': [
                    {
                        'q': 'Quels sont les 5 critères cliniques typiques d\'une douleur angineuse (Angor) ?',
                        'a': '1) Siège rétrosternal médiorégional ; 2) Type constrictif (« sensation d\'étau ») ; 3) Irradiations caractéristiques au bras gauche, épaule gauche et mâchoire ; 4) Circonstances de survenue à l\'effort physique ou au froid ; 5) Durée brève (< 15 min) avec disparition rapide au repos ou après prise sublinguale de dérivés nitrés.'
                    },
                    {
                        'q': 'Quelles sont les caractéristiques séméiologiques des Œdèmes des Membres Inférieurs (OMI) d\'origine cardiaque ?',
                        'a': 'Ils sont bilatéraux, symétriques, déclives (prédominant aux chevilles et jambes en position debout), blancs, mous, indolores et prennent l\'empreinte du doigt lors de la pression (« signe du godet »).'
                    },
                    {
                        'q': 'Qu\'est-ce que l\'Orthopnée et quel diagnostic évoque-t-elle en priorité ?',
                        'a': 'C\'est une difficulté respiratoire majeure apparaissant en position couchée (décubitus) et améliorée dès que le patient s\'assied ou se tient debout. Elle traduit une stase pulmonaire liée à une insuffisance ventriculaire gauche.'
                    }
                ]
            },
            {
                'id': 'semio_programme',
                'title': 'Document Officiel : Programme des Cours de Pharmacie 3',
                'teacher': 'DER Sciences du Médicament (Pr Sékou BAH)',
                'pages': 15,
                'file': 'cours/semiologie/programme_cours_pharmacie3.pdf',
                'badge': 'Référentiel FAPH USTTB',
                'summary': [
                    'Programme officiel des cours magistraux et travaux dirigés de Pharmacie 3 (Année Universitaire 2025-2026, Faculté de Pharmacie de Bamako).',
                    'Encadrement pédagogique : Pr Sékou BAH (responsable du DER), assisté des Dr Karim TRAORE et Dr Abdoulaye GUINDO.',
                    'Grands thèmes abordés : Notions générales de pharmacologie et histoire, Les médicaments et la Pharmacopée, Pharmacovigilance et iatrogénie, Pharmacologie spéciale des grands systèmes physiologiques.'
                ],
                'quiz': [
                    {
                        'q': 'Quel département pilote le programme de pharmacologie à la FAPH de Bamako ?',
                        'a': 'Le DER Sciences du Médicament, dirigé par le Pr Sékou BAH, responsable de la formation théorique et pratique des étudiants de DFGSP3.'
                    }
                ]
            }
        ],
        'has_pharma_modules': False
    }
]
