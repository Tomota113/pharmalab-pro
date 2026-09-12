import json

with open('data/pharmacology_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

more_molecules = [
    {
        "id": "naproxene",
        "name": "Naproxène",
        "dci": "Naproxène / Naproxène sodique",
        "brand_names": ["Apranax®", "Naprosyne®", "Aleve®"],
        "class_name": "AINS dérivé de l'acide arylpropionique à longue demi-vie",
        "palier": 1,
        "palier_label": "Palier I OMS",
        "legal_status": "Liste II pour les dosages faibles (220mg) ; Liste I pour 550mg et 750mg",
        "formula": "C14H14O3",
        "mol_weight": 230.26,
        "pk": {
            "bioavailability": "Quasi-complète (F > 95 %)",
            "tmax": "2 à 4 heures (forme acide) ; 1 à 2 heures (forme sel de sodium)",
            "vd": "0.16 L/kg",
            "protein_binding": "> 99 % (saturable à forte dose)",
            "halflife": "12 à 15 heures (permet une prise biquotidienne matin et soir)",
            "clearance": "0.13 mL/min/kg",
            "ka": 1.1,
            "ke": 0.05,
            "therapeutic_window": "30 à 90 mg/L"
        },
        "metabolism": {
            "pathways": "O-déméthylation hépatique par le CYP2C9 et CYP1A2 en 6-O-desméthylnaproxène inactif, puis glucuroconjugaison.",
            "toxic_intermediate": "Aucun.",
            "excretion": "Excrétion urinaire à 95% sous forme métabolisée et moins de 1% inchangé."
        },
        "pharmacodynamics": {
            "mechanism": "Inhibiteur puissant et équilibré de COX-1 et COX-2. Sa longue demi-vie assure une suppression soutenue de la synthèse de TXA2 plaquettaire et de PGE2 inflammatoire.",
            "peripheral_effect": "AINS considéré dans les méta-analyses comme ayant le PROFIL CARDIOVASCULAIRE LE MOINS DÉLÉTÈRE parmi les AINS traditionnels (moindre risque relatif d'infarctus du myocarde par rapport au diclofénac ou aux coxibs)."
        },
        "posology": {
            "adult": "500 à 1 000 mg par jour en 2 prises (matin et soir au cours des repas). Ex. Apranax® 550 mg : 1 cp matin et soir.",
            "pediatric": "Réservé à l'enfant à partir de 25 kg (arthrite juvénile idiopathique).",
            "renal_adjustment": "Contre-indiqué si DFG < 30 mL/min.",
            "elderly": "Réduire la posologie initiale de moitié."
        },
        "contraindications": [
            "Grossesse dès le 6e mois (24 SA) : CONTRE-INDICATION ABSOLUE.",
            "Ulcère gastrique en évolution.",
            "Insuffisance rénale sévère."
        ],
        "precautions": ["Surveillance de la muqueuse gastrique chez le sujet à risque."],
        "interactions": [
            { "drug": "Anticoagulants oraux", "level": "Association déconseillée", "mechanism": "Majoration du risque hémorragique digestif." }
        ],
        "antidote": { "name": "Traitement symptomatique", "protocol": "Protection gastrique par IPP, hydratation IV." },
        "concours_pearl": "Le naproxène est l'AINS de premier choix chez les patients présentant un risque cardiovasculaire modéré nécessitant impérativement un traitement anti-inflammatoire, en raison de son inhibition plaquettaire continue tout au long des 24h."
    },
    {
        "id": "diclofenac",
        "name": "Diclofénac",
        "dci": "Diclofénac sodique / potassique",
        "brand_names": ["Voltarène® (comprimés, suppositoires, injectable)", "Flector® (gel/emplâtre)"],
        "class_name": "AINS dérivé de l'acide phénylacétique",
        "palier": 1,
        "palier_label": "Palier I OMS",
        "legal_status": "Liste I (Prescription médicale obligatoire)",
        "formula": "C14H11Cl2NO2",
        "mol_weight": 296.15,
        "pk": {
            "bioavailability": "50 à 60 % (effet de premier passage hépatique important d'environ 50%)",
            "tmax": "1.5 à 2 heures (forme gastro-résistante)",
            "vd": "0.12 à 0.17 L/kg (très forte pénétration et rétention dans le liquide synovial)",
            "protein_binding": "> 99.5 %",
            "halflife": "1.2 à 2 heures",
            "clearance": "260 mL/min",
            "ka": 1.8,
            "ke": 0.40,
            "therapeutic_window": "0.5 à 2 mg/L"
        },
        "metabolism": {
            "pathways": "Hydroxylation hépatique par le CYP2C9 (formation du 4'-hydroxy-diclofénac) et le CYP3A4, puis glucuroconjugaison.",
            "toxic_intermediate": "Formation de quinone-imines réactives pouvant contribuer à de rares hépatites immuno-allergiques ou toxiques (surveillance transaminases).",
            "excretion": "60% urinaire sous forme métabolisée et 35% fécale/biliaire."
        },
        "pharmacodynamics": {
            "mechanism": "Inhibition puissante de COX-1 et COX-2 avec une sélectivité relative préférentielle pour COX-2 (intermédiaire entre les AINS non sélectifs et les coxibs purs).",
            "peripheral_effect": "Anti-inflammatoire de référence en rhumatologie. Attention : profil cardiovasculaire proche des coxibs (sur-risque thrombotique documenté par l'ANSM)."
        },
        "posology": {
            "adult": "75 à 150 mg par jour en 2 ou 3 prises (comprimés dosés à 25 mg, 50 mg ou Voltarène LP 75 mg).",
            "pediatric": "Réservé à l'enfant de plus de 35 kg.",
            "renal_adjustment": "Contre-indiqué si DFG < 30 mL/min.",
            "elderly": "Prudence cardiovasculaire et rénale."
        },
        "contraindications": [
            "Insuffisance cardiaque congestive (NYHA II-IV), cardiopathie ischémique, artériopathie périphérique, antécédents d'AVC : CONTRE-INDICATION ABSOLUE.",
            "Grossesse dès 24 SA.",
            "Ulcère gastroduodénal évolutif."
        ],
        "precautions": ["Bilan hépatique de contrôle en cas d'utilisation prolongée."],
        "interactions": [
            { "drug": "Lithium, Méthotrexate, Digoxine", "level": "Association déconseillée / Précaution", "mechanism": "Élévation toxique des concentrations plasmatiques par baisse de clairance rénale." }
        ],
        "antidote": { "name": "Traitement symptomatique", "protocol": "Protection muqueuse par IPP et maintien de la volémie." },
        "concours_pearl": "Recommandation européenne de pharmacovigilance (PRAC) : En raison de sa sélectivité COX-2 marquée, le diclofénac présente les mêmes contre-indications cardiovasculaires strictes que les coxibs (Célécoxib, Étoricoxib)."
    },
    {
        "id": "dihydrocodeine",
        "name": "Dihydrocodéine",
        "dci": "Tartrate de Dihydrocodéine",
        "brand_names": ["Dicodin® LP 60 mg"],
        "class_name": "Opioïde de Palier II semi-synthétique à libération prolongée",
        "palier": 2,
        "palier_label": "Palier II OMS",
        "legal_status": "STUPÉFIANT (Ordonnance sécurisée, 28 jours)",
        "formula": "C18H23NO3",
        "mol_weight": 301.38,
        "pk": {
            "bioavailability": "20 % (effet de premier passage hépatique important)",
            "tmax": "3 à 5 heures (forme matricielle LP Dicodin)",
            "vd": "1 L/kg",
            "protein_binding": "Moins de 10 %",
            "halflife": "3.5 à 4.5 heures (effet thérapeutique prolongé sur 12 heures grâce à la matrice LP)",
            "clearance": "500 mL/min",
            "ka": 0.4,
            "ke": 0.16,
            "therapeutic_window": "20 à 80 ng/mL"
        },
        "metabolism": {
            "pathways": "O-déméthylation par le CYP2D6 en dihydromorphine (antalgique très puissant) et N-déméthylation par le CYP3A4 en nordihydrocodéine.",
            "toxic_intermediate": "Sensible au polymorphisme du CYP2D6.",
            "excretion": "Excrétion urinaire à 90%."
        },
        "pharmacodynamics": {
            "mechanism": "Agoniste des récepteurs mu-opioïdes avec une puissance environ deux fois supérieure à celle de la codéine.",
            "peripheral_effect": "Constipation marquée et sédation."
        },
        "posology": {
            "adult": "Dicodin® LP 60 mg : 1 comprimé matin et soir à 12 heures d'intervalle (max 120 mg/j). Avaler entier sans croquer ni écraser !",
            "pediatric": "Contre-indiqué chez l'enfant.",
            "renal_adjustment": "Espacer les prises si DFG < 50 mL/min.",
            "elderly": "Débuter à 60 mg/jour en une prise le soir."
        },
        "contraindications": ["Insuffisance respiratoire sévère", "Allaitement", "Enfant"],
        "precautions": ["Ne jamais écraser le comprimé matriciel LP sous peine de libération massive toxique (dose-dumping)."],
        "interactions": [{ "drug": "Alcool et BZD", "level": "Association déconseillée", "mechanism": "Dépression respiratoire." }],
        "antidote": { "name": "Naloxone IV", "protocol": "0.4 mg IV titré." },
        "concours_pearl": "Le Dicodin® LP est le seul antalgique de Palier II soumis à la réglementation complète des STUPÉFIANTS en France (ordonnance sécurisée de 28 jours, prescription en toutes lettres)."
    },
    {
        "id": "poudre_opium",
        "name": "Poudre d'Opium",
        "dci": "Poudre d'Opium titrée à 10% de morphine",
        "brand_names": ["Lamaline® (Opium + Paracétamol + Caféine)", "Izalgi® (Opium 25mg + Paracétamol 500mg)"],
        "class_name": "Opioïde faible naturel de Palier II",
        "palier": 2,
        "palier_label": "Palier II OMS",
        "legal_status": "Liste I (Ordonnance médicale)",
        "formula": "Mélange naturel d'alcaloïdes (Morphine, Codéine, Papavérine, Noscapine)",
        "mol_weight": 0,
        "pk": {
            "bioavailability": "30 % (correspondant à la fraction de morphine naturelle absorbée)",
            "tmax": "1 heure",
            "vd": "3 L/kg",
            "protein_binding": "30 %",
            "halflife": "2 à 3 heures",
            "clearance": "1 000 mL/min",
            "ka": 1.5,
            "ke": 0.28,
            "therapeutic_window": "Équivalence : 25 mg de poudre d'opium = 2.5 mg de morphine"
        },
        "metabolism": {
            "pathways": "Glucuroconjugaison hépatique de la fraction morphinique en M3G et M6G.",
            "toxic_intermediate": "Accumulation de métabolites en cas d'insuffisance rénale sévère.",
            "excretion": "Excrétion rénale."
        },
        "pharmacodynamics": {
            "mechanism": "Effet agoniste mu-opioïde apporté par la morphine titrée (10%), potentialisé par les alcaloïdes accessoires (la papavérine apporte une composante spasmolytique viscérale musculaire lisse).",
            "peripheral_effect": "Très efficace dans les douleurs viscérales et spasmodiques digestives ou gynécologiques."
        },
        "posology": {
            "adult": "Izalgi® (500/25 mg) ou Lamaline® : 1 gélule par prise, 2 à 4 fois par jour si besoin (max 4 gélules/j).",
            "pediatric": "Contre-indiqué chez l'enfant de moins de 15 ans.",
            "renal_adjustment": "Espacer les prises de 8 heures si DFG < 30 mL/min.",
            "elderly": "Réduire la dose."
        },
        "contraindications": ["Insuffisance hépatocellulaire sévère", "Insuffisance respiratoire", "Allaitement"],
        "precautions": ["Ne pas associer à d'autres médicaments contenant du paracétamol."],
        "interactions": [{ "drug": "Alcool, dépresseurs du SNC", "level": "Association déconseillée", "mechanism": "Sommation sédative." }],
        "antidote": { "name": "Naloxone IV", "protocol": "0.4 mg IV." },
        "concours_pearl": "Dans l'Izalgi®, 25 mg de poudre d'opium apporte très exactement 2.5 mg de morphine pure par gélule, ce qui classe la spécialité en Palier II (et non en stupéfiant de Palier III)."
    },
    {
        "id": "hydromorphone",
        "name": "Hydromorphone",
        "dci": "Chlorhydrate d'Hydromorphone",
        "brand_names": ["Sophidone® LP (gélules de 4 mg, 8 mg, 16 mg, 24 mg)"],
        "class_name": "Opioïde fort semi-synthétique de Palier III, dérivé cétonique de la morphine",
        "palier": 3,
        "palier_label": "Palier III OMS",
        "legal_status": "STUPÉFIANT (Prescription sur ordonnance sécurisée pour 28 jours)",
        "formula": "C17H19NO3",
        "mol_weight": 285.34,
        "pk": {
            "bioavailability": "50 % par voie orale",
            "tmax": "6 à 8 heures (forme matricielle à libération prolongée Sophidone)",
            "vd": "4 L/kg",
            "protein_binding": "8 à 19 % (liaison protéique très faible)",
            "halflife": "2.5 heures (durée d'action de 12 heures grâce à la matrice LP)",
            "clearance": "1 200 mL/min",
            "ka": 0.3,
            "ke": 0.25,
            "therapeutic_window": "Puissance analgésique 7.5 fois supérieure à la morphine orale"
        },
        "metabolism": {
            "pathways": "Glucuroconjugaison hépatique majeure en hydromorphone-3-glucuronide (H3G) dénué d'activité analgésique mais neurotoxique à forte dose. Absence de métabolite 6-glucuronide !",
            "toxic_intermediate": "L'absence de métabolite 6-glucuronide rend son profil souvent plus tolérable que la morphine chez l'insuffisant rénal modéré.",
            "excretion": "Excrétion rénale des métabolites glucuronés."
        },
        "pharmacodynamics": {
            "mechanism": "Agoniste pur des récepteurs mu-opioïdes avec une affinité supérieure à celle de la morphine.",
            "peripheral_effect": "Constipation opiniâtre, sédation initiale."
        },
        "posology": {
            "adult": "Sophidone® LP : prise toutes les 12 heures à heures fixes (matin et soir). Ratio d'équi-analgésie de référence : 4 mg d'Hydromorphone orale LP ≈ 30 mg de Morphine orale LP (facteur de conversion = multiplier la dose d'hydromorphone par 7.5 pour trouver la dose équivalente de morphine orale).",
            "breakthrough_pain": "Pour les accès douloureux, utiliser de la morphine LI (Actiskenan) ou de l'oxynorm LI car il n'existe pas de forme LI d'hydromorphone commercialisée en France.",
            "renal_adjustment": "Diminuer les doses de 50% si DFG < 50 mL/min.",
            "elderly": "Prudence et titration progressive."
        },
        "contraindications": ["Insuffisance respiratoire décompensée", "Insuffisance hépatique sévère", "Iléus"],
        "precautions": ["Laxatif osmotique impératif dès J1."],
        "interactions": [{ "drug": "Buprénorphine", "level": "Contre-indication", "mechanism": "Sevrage aigu." }],
        "antidote": { "name": "Naloxone IV", "protocol": "Titration prudente par bolus de 0.04 mg." },
        "concours_pearl": "Règle de conversion Sophidone LP <-> Morphine orale LP : Multiplier la dose de Sophidone par 7.5 pour obtenir la dose équivalente de morphine (ex. 8 mg d'hydromorphone x 7.5 = 60 mg de morphine orale LP par jour)."
    },
    {
        "id": "buprenorphine",
        "name": "Buprénorphine",
        "dci": "Chlorhydrate de Buprénorphine",
        "brand_names": ["Temgesic® (0.2 mg sublingual - indication antalgique)", "Subutex® (0.4/2/8 mg sublingual - traitement substitutif des opioïdes TSO)"],
        "class_name": "Opioïde de Palier III, agoniste partiel mu et antagoniste kappa",
        "palier": 3,
        "palier_label": "Palier III OMS (Agoniste Partiel)",
        "legal_status": "Liste I (Soumise à la réglementation des stupéfiants pour le Subutex avec ordonnance sécurisée limitée à 28 jours et mention du pharmacien dispensateur)",
        "formula": "C29H41NO4",
        "mol_weight": 467.64,
        "pk": {
            "bioavailability": "Sublinguale : 30 à 50 % ; Per os : nulle (< 5%, dégradation gastrique et premier passage hépatique massif)",
            "tmax": "1 à 2 heures par voie sublinguale",
            "vd": "3 à 5 L/kg (très lipophile)",
            "protein_binding": "96 %",
            "halflife": "20 à 40 heures (liaison aux récepteurs mu quasi-irréversible avec cinétique de dissociation très lente)",
            "clearance": "1 000 mL/min",
            "ka": 0.9,
            "ke": 0.025,
            "therapeutic_window": "Effet plafond analgésique et respiratoire"
        },
        "metabolism": {
            "pathways": "N-désalkylation par le CYP3A4 en norbuprénorphine (agoniste plein à activité respiratoire modérée), puis glucuroconjugaison.",
            "toxic_intermediate": "Aucun.",
            "excretion": "Élimination principalement fécale et biliaire (70%) et rénale (30%). Sécurité remarquable en cas d'insuffisance rénale !"
        },
        "pharmacodynamics": {
            "mechanism": "Pharmacodynamie unique : 1) Agoniste PARTIEL des récepteurs mu-opioïdes : possède une affinité de liaison extrêmement élevée (supérieure à la morphine, au fentanyl et à la naloxone), mais une activité intrinsèque partielle (alpha < 1). Présente un 'effet plafond' sur la dépression respiratoire (risque d'asphyxie très inférieur aux agonistes pleins). 2) Antagoniste des récepteurs kappa-opioïdes.",
            "peripheral_effect": "Moins de constipation et moins de sédation que les agonistes purs."
        },
        "posology": {
            "adult": "Antalgique (Temgesic® 0.2 mg) : 1 à 2 comprimés sublinguaux à laisser fondre sous la langue toutes les 6 à 8 heures (max 1.2 mg/j). NE PAS AVALER LE COMPRIMÉ !",
            "pediatric": "Réservé à l'adulte.",
            "renal_adjustment": "AUCUN AJUSTEMENT NÉCESSAIRE. Élimination principalement biliaire.",
            "elderly": "Bien tolérée."
        },
        "contraindications": [
            "Association avec les agonistes opioïdes purs de Palier III (Morphine, Fentanyl, Oxycodone) : CONTRE-INDICATION ABSOLUE.",
            "Insuffisance respiratoire sévère.",
            "Insuffisance hépatique sévère."
        ],
        "precautions": [
            "Prise concomitante de benzodiazépines : principale cause de décès par surdose chez les usagers sous buprénorphine (dépression respiratoire centrale synergique non surmontable).",
            "Respecter la voie SUBLINGUALE stricte."
        ],
        "interactions": [
            { "drug": "Morphine, Fentanyl, Oxycodone, Méthadone (Agonistes purs)", "level": "CONTRE-INDICATION ABSOLUE", "mechanism": "La buprénorphine possède une affinité pour les récepteurs mu bien supérieure à celle de la morphine. Elle déplace instantanément l'agoniste pur de ses récepteurs et précipite un SYNDROME DE SEVRAGE AIGU SÉVÈRE et une perte brutale de l'analgésie !" },
            { "drug": "Benzodiazépines", "level": "Association déconseillée / Surveillance extrême", "mechanism": "Synergie toxique sur le centre respiratoire responsable d'arrêts respiratoires fatals." }
        ],
        "antidote": {
            "name": "Naloxone IV à très fortes doses en perfusion continue",
            "protocol": "En raison de la liaison pseudo-irréversible de la buprénorphine sur le récepteur mu, la naloxone ne parvient pas à la déplacer aux doses usuelles. Il faut administrer de très fortes doses de naloxone (2 à 4 mg en bolus répétés puis perfusion continue sur plusieurs heures)."
        },
        "concours_pearl": "Pourquoi la buprénorphine a-t-elle un profil de sécurité respiratoire supérieur à la morphine ? En raison de son activité intrinsèque partielle : même à des doses suprathérapeutiques massives, la courbe dose-réponse de la dépression respiratoire atteint un 'effet plafond' (plateau). En monothérapie sans benzodiazépines, le risque de décès par apnée est quasi-nul."
    },
    {
        "id": "methadone",
        "name": "Méthadone",
        "dci": "Chlorhydrate de Méthadone",
        "brand_names": ["Méthadone AP-HP® (sirop et gélules)"],
        "class_name": "Opioïde fort synthétique de Palier III, agoniste mu et antagoniste NMDA",
        "palier": 3,
        "palier_label": "Palier III OMS",
        "legal_status": "STUPÉFIANT (Ordonnance sécurisée pour 14 jours en sirop ou 28 jours en gélules, délivrance fractionnée par périodes de 7 jours, initiation réservée aux CSAPA ou médecins hospitaliers)",
        "formula": "C21H27NO",
        "mol_weight": 309.45,
        "pk": {
            "bioavailability": "80 à 90 % par voie orale",
            "tmax": "2 à 4 heures",
            "vd": "4 à 5 L/kg (accumulation tissulaire massive)",
            "protein_binding": "85 à 90 %",
            "halflife": "24 à 36 heures (très longue et très variable interindividuellement : de 15 à 60 heures !)",
            "clearance": "100 mL/min",
            "ka": 1.0,
            "ke": 0.02,
            "therapeutic_window": "Large variabilité génétique"
        },
        "metabolism": {
            "pathways": "N-déméthylation hépatique majeure par le CYP3A4, CYP2B6 et CYP2C19 en EDDP inactif.",
            "toxic_intermediate": "Allongement de l'intervalle QT dose-dépendant (blocage des canaux potassiques cardiaques hERG) : risque de torsades de pointes mortelles.",
            "excretion": "Excrétion rénale et fécale équilibrée."
        },
        "pharmacodynamics": {
            "mechanism": "Double mécanisme remarquable : 1) Agoniste pur puissant des récepteurs mu-opioïdes. 2) Antagoniste non compétitif des récepteurs glutamatergiques NMDA (empêche la sensibilisation centrale et combat la tolérance aux opioïdes et l'hyperalgie). 3) Inhibiteur de la recapture de la sérotonine et de la noradrénaline.",
            "peripheral_effect": "Très efficace dans les douleurs cancéreuses réfractaires et les douleurs neuropathiques sévères résistantes."
        },
        "posology": {
            "adult": "En cancérologie/douleur réfractaire : titration ultra-prudente par des équipes spécialisées de soins palliatifs (ratio d'équi-analgésie variable et progressif : pour des doses élevées de morphine, 1 mg de méthadone peut valoir 10 à 20 mg de morphine !). En TSO : dose quotidienne unique.",
            "pediatric": "Non indiqué.",
            "renal_adjustment": "Pas d'ajustement nécessaire.",
            "elderly": "Prudence extrême en raison de l'accumulation sur 3 à 5 jours."
        },
        "contraindications": ["Insuffisance respiratoire", "Insuffisance hépatique sévère", "Allongement du QT congénital ou acquis"],
        "precautions": ["Réaliser systématiquement un ECG avant initiation et après augmentation posologique (mesure du QTc)."],
        "interactions": [{ "drug": "Inhibiteurs du CYP3A4 (Clarithromycine, Kétoconazole) ou médicaments allongeant le QT", "level": "Association déconseillée / Contre-indication", "mechanism": "Torsades de pointes et surdosage." }],
        "antidote": { "name": "Naloxone IV en perfusion continue prolongée", "protocol": "En raison de la demi-vie de 24-36h de la méthadone, la perfusion de naloxone doit être maintenue pendant au moins 24 à 48 heures." },
        "concours_pearl": "Le piège de la titration de la méthadone : La demi-vie plasmatique (24-36h) est beaucoup plus longue que la durée d'action analgésique (6-8h). L'état d'équilibre (steady-state) n'est atteint qu'au bout de 4 à 7 jours. Une augmentation trop rapide des doses entraîne une accumulation insidieuse et une overdose mortelle au 4e ou 5e jour !"
    },
    {
        "id": "gabapentine",
        "name": "Gabapentine",
        "dci": "Gabapentine",
        "brand_names": ["Neurontin® (gélules 100 mg, 300 mg, 400 mg, 600 mg, 800 mg)"],
        "class_name": "Co-analgésique adjuvant, ligand de la sous-unité alpha-2-delta des canaux calciques",
        "palier": 0,
        "palier_label": "Adjuvant / Co-analgésique",
        "legal_status": "Liste I (Prescription médicale obligatoire)",
        "formula": "C9H17NO2",
        "mol_weight": 171.24,
        "pk": {
            "bioavailability": "Biodisponibilité non linéaire et SATURABLE (60% à 900 mg/j, diminuant à 35% à 3 600 mg/j par saturation du transporteur intestinal L-aminoacide LAT1)",
            "tmax": "2 à 3 heures",
            "vd": "0.8 L/kg",
            "protein_binding": "0 %",
            "halflife": "5 à 7 heures",
            "clearance": "Égale à la clairance rénale",
            "ka": 0.9,
            "ke": 0.12,
            "therapeutic_window": "900 à 3 600 mg/jour"
        },
        "metabolism": {
            "pathways": "AUCUN métabolisme chez l'homme. La gabapentine n'induit ni n'inhibe aucun cytochrome P450.",
            "toxic_intermediate": "Aucun.",
            "excretion": "Excrétion rénale sous forme inchangée à 100% par filtration glomérulaire."
        },
        "pharmacodynamics": {
            "mechanism": "Liaison sélective à la sous-unité alpha-2-delta-1 (α2-δ) des canaux calciques voltage-dépendants présynaptiques dans le système nerveux central. Réduction de l'influx calcique et inhibition de la libération des acides aminés excitateurs (glutamate) au niveau de la corne dorsale de la moelle.",
            "peripheral_effect": "Sédation, somnolence, vertiges, prise de poids, œdèmes malléolaires."
        },
        "posology": {
            "adult": "Douleurs neuropathiques périphériques (zona, diabète) : J1 : 300 mg une fois par jour. J2 : 300 mg deux fois par jour. J3 : 300 mg trois fois par jour (900 mg/j). Augmentation progressive par paliers de 300 mg tous les 2-3 jours jusqu'à la dose efficace habituelle de 1 800 à 2 400 mg/jour en 3 prises (max 3 600 mg/j).",
            "pediatric": "Non indiqué dans la douleur neuropathique chez l'enfant.",
            "renal_adjustment": "ADAPTATION OBLIGATOIRE AU DFG : DFG 50-79 mL/min : max 1 800 mg/j ; DFG 30-49 mL/min : max 900 mg/j ; DFG 15-29 mL/min : max 600 mg/j ; DFG < 15 mL/min : max 300 mg/j.",
            "elderly": "Adapter impérativement au DFG estimé."
        },
        "contraindications": ["Hypersensibilité à la gabapentine"],
        "precautions": ["Idées suicidaires, arrêt brutal à proscrire (diminution par paliers sur 1 semaine au moins)."],
        "interactions": [{ "drug": "Antiacides (sels d'aluminium et magnésium : Maalox)", "level": "Précaution", "mechanism": "Diminution de 20% de la biodisponibilité de la gabapentine par chélation (espacer de 2 heures)." }],
        "antidote": { "name": "Hémodialyse", "protocol": "Élimination efficace par dialyse." },
        "concours_pearl": "Pourquoi la biodisponibilité de la gabapentine diminue-t-elle quand on augmente les doses ? Contrairement à la prégabaline qui a une cinétique linéaire (absorption proportionnelle à la dose jusqu'à 600 mg/j), la gabapentine utilise un transporteur saturable dans le duodénum : plus on monte la dose, plus le pourcentage absorbé chute (60% à 900mg/j contre seulement 33% à 3600mg/j)."
    },
    {
        "id": "duloxetine",
        "name": "Duloxétine",
        "dci": "Chlorhydrate de Duloxétine",
        "brand_names": ["Cymbalta® (gélules gastro-résistantes 30 mg et 60 mg)"],
        "class_name": "Co-analgésique de première ligne dans les douleurs neuropathiques, inhibiteur de la recapture de la sérotonine et de la noradrénaline (IRSNa)",
        "palier": 0,
        "palier_label": "Adjuvant / Co-analgésique",
        "legal_status": "Liste I (Prescription médicale obligatoire)",
        "formula": "C18H19NOS",
        "mol_weight": 297.41,
        "pk": {
            "bioavailability": "50 % (retardée de 2h par la formulation gastro-résistante pour éviter la dégradation acide gastrique)",
            "tmax": "6 heures",
            "vd": "20 L/kg (forte distribution lipophile)",
            "protein_binding": "> 96 %",
            "halflife": "12 heures",
            "clearance": "1 000 mL/min",
            "ka": 0.4,
            "ke": 0.058,
            "therapeutic_window": "30 à 120 mg/jour"
        },
        "metabolism": {
            "pathways": "Biotransformation hépatique intensive par le CYP1A2 et le CYP2D6 en multiples métabolites inactifs sulfatés et glucuronés.",
            "toxic_intermediate": "Inhibiteur modéré du CYP2D6.",
            "excretion": "Excrétion urinaire à 70% et fécale à 20% sous forme de métabolites."
        },
        "pharmacodynamics": {
            "mechanism": "Inhibition puissante et équilibrée de la recapture synaptique de la sérotonine et de la noradrénaline (sans affinité significative pour les récepteurs histaminiques, dopaminergiques, cholinergiques ou adrénergiques). Renforce puissamment les voies inhibitrices descendantes bulbo-spinales de la douleur.",
            "peripheral_effect": "Augmentation de la pression artérielle et de la fréquence cardiaque (effet noradrénergique), nausées transitoires, sueurs, sécheresse buccale."
        },
        "posology": {
            "adult": "Neuropathie diabétique périphérique douloureuse : 60 mg une fois par jour le matin au milieu du repas. Évaluation de l'efficacité après 2 à 4 mois.",
            "pediatric": "Non indiqué chez l'enfant.",
            "renal_adjustment": "CONTRE-INDIQUÉ en cas d'insuffisance rénale sévère (DFG < 30 mL/min).",
            "elderly": "Débuter à 30 mg/jour."
        },
        "contraindications": [
            "Insuffisance rénale sévère (DFG < 30 mL/min).",
            "Insuffisance hépatique.",
            "Association aux inhibiteurs puissants du CYP1A2 (Fluvoxamine, Ciprofloxacine).",
            "Association aux IMAO.",
            "Hypertension artérielle non contrôlée."
        ],
        "precautions": ["Surveillance de la pression artérielle, arrêt progressif pour éviter un syndrome de sevrage."],
        "interactions": [
            { "drug": "Fluvoxamine, Ciprofloxacine (Inhibiteurs puissants CYP1A2)", "level": "CONTRE-INDICATION ABSOLUE", "mechanism": "Multiplication par 6 des concentrations plasmatiques de duloxétine et risque toxique sévère." },
            { "drug": "Tramadol", "level": "Association déconseillée", "mechanism": "Risque majeur de syndrome sérotoninergique et convulsions." }
        ],
        "antidote": { "name": "Traitement symptomatique", "protocol": "Refroidissement et benzodiazépines si syndrome sérotoninergique." },
        "concours_pearl": "Indication spécifique : La duloxétine est le seul antidépresseur possédant une AMM officielle spécifique dans le traitement de la douleur neuropathique périphérique du patient DIABÉTIQUE en France."
    },
    {
        "id": "phloroglucinol",
        "name": "Phloroglucinol",
        "dci": "Phloroglucinol / Triméthylphloroglucinol",
        "brand_names": ["Spasfon® (comprimés, lyoc sublingual, injectable)"],
        "class_name": "Antispasmodique musculotrope / myotrope pur",
        "palier": 0,
        "palier_label": "Adjuvant Spasmolytique",
        "legal_status": "Médicament de médication officinale (hors liste)",
        "formula": "C6H6O3",
        "mol_weight": 126.11,
        "pk": {
            "bioavailability": "Rapide par voie sublinguale (lyoc)",
            "tmax": "15 à 30 min (forme lyoc), 1h (comprimé)",
            "vd": "0.3 L/kg",
            "protein_binding": "Faible",
            "halflife": "1.5 heures",
            "clearance": "Rénale",
            "ka": 2.5,
            "ke": 0.46,
            "therapeutic_window": "Symptomatique"
        },
        "metabolism": {
            "pathways": "Glucuroconjugaison hépatique directe.",
            "toxic_intermediate": "Aucun.",
            "excretion": "Excrétion urinaire rapide."
        },
        "pharmacodynamics": {
            "mechanism": "Spasmolytique musculotrope pur : lève le spasme des fibres musculaires lisses viscérales (digestives, biliaires, urologiques et gynécologiques) sans posséder aucun effet anticholinergique/atropinique.",
            "peripheral_effect": "Dénué d'effets atropiniques : pas de sécheresse buccale, pas de glaucome, pas de tachycardie, pas de rétention d'urine."
        },
        "posology": {
            "adult": "2 comprimés ou 2 lyocs au moment de la crise douloureuse, à renouveler si besoin (max 6 prises par jour).",
            "pediatric": "Forme lyoc adaptée à l'enfant de plus de 2 ans.",
            "renal_adjustment": "Pas d'ajustement nécessaire.",
            "elderly": "Très bien toléré."
        },
        "contraindications": ["Hypersensibilité au phloroglucinol"],
        "precautions": ["Éviter chez la femme qui allaite par manque de données."],
        "interactions": [{ "drug": "Antalgiques majeurs (Morphine)", "level": "Synergie clinique favorable", "mechanism": "Lève la composante spastique de la douleur viscérale." }],
        "antidote": { "name": "N/A", "protocol": "N/A" },
        "concours_pearl": "Avantage clinique majeur du phloroglucinol par rapport aux antispasmodiques atropiniques (comme le bromure de tiémonium ou la scopolamine) : il peut être prescrit en toute sécurité chez les patients souffrant de glaucome à angle fermé ou d'adénome prostatique car il n'exerce aucun blocage des récepteurs muscariniques."
    }
]

# Append new molecules if not existing
existing_ids = {m['id'] for m in db['molecules']}
count = 0
for m in more_molecules:
    if m['id'] not in existing_ids:
        db['molecules'].append(m)
        count += 1

db['total'] = len(db['molecules'])

with open('data/pharmacology_db.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

print(f"Appended {count} more molecules. Total in database: {db['total']}!")
