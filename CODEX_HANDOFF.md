# Relais Codex — To Oumou

Date de reprise : 3 novembre 2026. Projet : `/home/ibrahim-tomota/Projects/Applications/To Oumou` (le dossier demandé dans `~/Documents/Projet/To Oumou` pointe vers ce projet). Branche `main`. Le site est maintenant publié sur Vercel ; les sections datées du 19 octobre ci-dessous documentent l'historique local.

## Publication du 3 novembre 2026 — état actuel

- URL publique : `https://pharmalab-pro-dfgsp2.vercel.app/`. Projet Vercel `pharmalab-pro-dfgsp2`, identifiant `prj_RaUqKlF60wiZVBUflzSoYOlqzaEb`, déploiement de production actif `dpl_5mWuduem5nTGgmbwTrcHK9T4FXRk` (état Ready, promu sur l'URL principale).
- Un contrôle après première publication a révélé que le lecteur PDF ouvrait le cours mais ne rendait pas la page en production : `UnknownErrorException`. PDF.js 6.4.299 standard utilisait des fonctions JavaScript non disponibles dans le navigateur. Les deux fichiers `vendor/pdfjs/pdf.mjs` et `pdf.worker.mjs` ont été remplacés par la **version legacy du même paquet**, testée avec le PDF local et le PDF servi par Vercel. `reader.js` charge les modules avec `?v=15` pour éviter l'ancien cache ; `sw.js` est en version `pharmalab-pro-v15` et précache ces URL.
- Vérification réelle sur l'URL publique : clic « Lire le PDF » depuis la carte immunologie, rendu visuel de la page 1, repère page 15, puis lien « Comprendre cette notion » vers `apprendre.html?cours=immuno_intro&etape=2`. L'accueil, l'atelier, le catalogue, PDF.js et le PDF répondent en HTTP 200. `.env.local` et `CODEX_HANDOFF.md` répondent en 404 grâce à `.vercelignore`.
- Le déploiement a été fait depuis le dossier local, **sans commit ni push Git**. Les changements restent dans l'arbre de travail. Avant un futur push ou une modification du site, vérifier `git status` et enregistrer les fichiers du site pour ne pas revenir à l'ancienne version du dépôt. Ce document de relais contient des chemins locaux et est exclu de Vercel ; éviter de le publier tel quel sur GitHub.

## Intention de l'utilisateur

Chaque PDF de cours doit rester disponible, avec une version pédagogique plus simple, plus explicative, plus détaillée et interactive. Les PDF pertinents de `~/Téléchargements` sont déjà présents à l'identique dans `cours/` (SHA-256 comparés). Le fichier `cours/semiologie/programme_cours_pharmacie3.pdf` est un programme de référence, pas un cours transformé. Ne pas toucher aux PDF ni inventer de validation clinique.

## Reprise du 19 octobre — état à jour

Les sections suivantes décrivent la première session. Les points 1 à 4 des anciennes « Prochaines actions concrètes » ont maintenant été exécutés pour la version locale :

- Sept cartes interactives ajoutées dans `learning_data.py` (34 repères sourcés). L’atelier affiche chaque notion et son lien vers la page PDF. Les cartes résument les cours fournis ; aucun protocole de soins n’a été ajouté.
- Sommaires repliés sur mobile, carte pédagogique repliée dans l’atelier sur petit écran, contrôles de page et de zoom regroupés dans le lecteur. Vérification visuelle de captures Chrome à 320, 360 et 1 440 pixels.
- Correction du sélecteur invalide `$('.main-panel')` qui provoquait une exception lors de la navigation après défilement. La navigation rejoint maintenant `#lesson-panel` avec gestion du focus et respect de la préférence de réduction des animations.
- Reprise à la première étape non parcourue si le lien ne précise pas `etape`. Stockage de progression nettoyé des doublons, valeurs hors limites et données invalides. Message de fin affiché lorsque toutes les étapes ont été marquées ; il ne prétend pas mesurer la maîtrise du cours.
- Renvois de biochimie corrigés après lecture du texte PDF : approvisionnement entre les repas page 21 et régulation hormonale page 27. Carte LADME alignée sur le vocabulaire du cours (« Élimination »).
- Au 19 octobre, `sw.js` était en **v13**. Il est en v15 depuis la publication du 3 novembre. Le PDF doit lui-même être chargé et mis en cache pour être lu hors ligne.
- `README.md` enrichi ; `index.html` et `learning-data.json` régénérés. Les PDF sont inchangés. Aucun commit, push ni déploiement n’a été effectué.

Vérifications finales réussies dans un Chrome sans fenêtre distinct du navigateur de l’utilisateur :

- Les sept PDF : première et dernière page, nombres de pages, zoom à 125 %, absence de débordement horizontal de la page sur écran de 360 pixels.
- Lecteur à 320, 768 et 1 440 pixels : zoom borné à 75–250 %, y compris après des clics rapides. Émulation mobile 360 pixels avec densité 2 : rendu et lien PDF → étape → page source corrects.
- Atelier à 320, 360, 768 et 1 440 pixels : détails, quiz, navigation après défilement, progression persistante, reprise, fin de parcours et données de progression invalides. Les 34 repères et leurs liens source ont été parcourus.
- Clic réel « Lire le PDF » du portail vers l’immunologie (titre avec apostrophe) : rendu réussi. Hors ligne : ouverture d’une nouvelle URL de parcours et rendu de la page 15 d’un PDF mis en cache.
- Aucune exception JavaScript non interceptée durant ces parcours. `node --check` pour les JS et scripts intégrés HTML, compilation Python, validation catalogue/pages et `git diff --check` réussis. Régénération reproductible vérifiée par SHA-256 des deux fichiers générés.

Les scripts de contrôle temporaires sont `/tmp/to_oumou_browser_check.py` et `/tmp/to_oumou_integration_check.py` ; ils utilisent le Chrome de test via CDP et le serveur local sur le port 8080. Captures finales : `/tmp/to-oumou-reader-mobile-final.png` et `/tmp/to-oumou-learning-mobile-final.png`. Ils ne font pas partie de l’application. La version locale est prête à être revue ; toute publication reste à traiter selon la demande de l’utilisateur.

## Travail présent dans le dossier (non commité)

- `learning_data.py` contient 7 parcours et 50 étapes, chacun avec explication simple, détaillée, exemple, question à choix et numéro de page source. `build_clean_dfgsp3.py` génère `learning-data.json` et `index.html`.
- `apprendre.html`, `learning.css`, `learning.js` fournissent le parcours guidé, progression en `localStorage`, quiz, sélection des cours et liens vers le PDF source.
- `subjects_data.py` affiche les vrais nombres de pages PDF (corrigés via `pdfinfo`).
- `index.html` affiche un encart « Les polycopiés prennent vie » et des actions sur chaque cours.
- Le bug « Lire le cours » a été reproduit sur le cours d'immunologie : titre contenant `'` injecté dans un `onclick` cassait le gestionnaire. Le générateur utilise maintenant un vrai lien `<a href="lire.html?cours=...">Lire le PDF</a>`. Le programme ouvre directement son PDF.
- `lire.html`, `reader.css`, `reader.js` constituent un lecteur avec repères par page, navigation, zoom de 75 à 250 % et lien vers l'étape expliquée correspondante. Les liens directs et téléchargement sont visibles.
- `vendor/pdfjs/pdf.mjs`, `vendor/pdfjs/pdf.worker.mjs` et `LICENSE` contiennent PDF.js 6.4.299 en local. `reader.js` rend la page choisie sur `<canvas>` ; le PDF reste disponible par lien direct et téléchargement.
- Lors de la première session, `sw.js` incluait les nouvelles pages et PDF.js (cache v11) ; voir la version v15 actuelle en tête de ce document.

## État réel du bug

Le clic « Lire le PDF » navigue maintenant vers `lire.html` (vérifié sur `immuno_intro`). L'ancienne iframe apparaissait noire dans le navigateur intégré ; **ce problème est corrigé** par le rendu PDF.js local sur `<canvas>`. Les pages 1 et 15 de l'immunologie et les pages 12 et 13 de la biochimie ont été vues dans le navigateur. La documentation primaire utilisée : `https://github.com/mozilla/pdf.js/blob/master/examples/learning/helloworld.html` et `https://mozilla.github.io/pdf.js/getting_started/`.

Le navigateur intégré est ouvert sur `http://127.0.0.1:8080/lire.html?cours=bioch_glucides&page=12`. Le serveur local a été relancé pendant cette session ; le relancer avec `python3 -m http.server 8080` depuis le projet s'il n'est plus disponible.

## Prochaines actions concrètes

1. Finir le contrôle visuel mobile et bureau ; une largeur d'environ 720 px a été vérifiée, mais un vrai petit écran reste à contrôler. Le zoom a été ajouté et vérifié à 125 % sur la page 12 de biochimie ; contrôler les autres tailles d'écran si le lecteur change.
2. Continuer l'amélioration pédagogique demandée (« tu peux mieux faire ») avec des interactions ancrées dans le contenu, par exemple des schémas simples ou des cartes de mécanismes. Conserver les renvois explicites au PDF original et vérifier toute affirmation sensible.
3. Mettre à jour la version de cache dans `sw.js` après tout changement de fichiers pour éviter le contenu périmé ; le service worker est en cache d'abord pour les PDF, réseau d'abord pour HTML/JS/CSS/JSON. Générer `index.html` et `learning-data.json` par `python3 build_clean_dfgsp3.py` si leurs sources changent.
4. Pour une future modification, refaire les contrôles : `node --check` sur chaque JS, `python3 -m py_compile` sur les Python, validation des pages PDF, `git diff --check`, et parcours dans un navigateur. Le déploiement du 3 novembre est décrit en tête de ce document ; aucun `git push` n'a eu lieu.

## Commandes et observations

- `python3 build_clean_dfgsp3.py` : succès ; génère un index d'environ 290 Ko et `learning-data.json`.
- `node --check reader.js`, `node --check learning.js`, `node --check sw.js`, `python3 -m py_compile build_clean_dfgsp3.py learning_data.py` et `git diff --check` : succès le 19 octobre après l'intégration de PDF.js.
- Catalogue vérifié : 7 cours, 50 étapes ; les 7 PDF existent, leurs nombres de pages correspondent au catalogue, et toutes les pages de référence des étapes sont valides.
- Avant l'arrêt du serveur de prévisualisation, la navigation `Comprendre cette notion` depuis la biochimie page 13 a ouvert `apprendre.html?cours=bioch_glucides&etape=2`, puis le retour `Voir la page 12 du cours original` a ouvert la bonne page du lecteur. La navigation entre pages du PDF a aussi fonctionné.
- Après relance du serveur et rechargement du lecteur, le bouton de zoom a affiché 125 % et la page 12 était visible dans le navigateur avec défilement horizontal.
- Avant la création du lecteur dédié, l'atelier (`apprendre.html`) a été testé : explication détaillée, quiz, progression persistante, changement de cours et lien PDF fonctionnaient. La progression de test a été remise à zéro.
- Le projet Vercel existant est `pharmalab-pro-dfgsp2` (`prj_RaUqKlF60wiZVBUflzSoYOlqzaEb`). Il a été déployé le 3 novembre ; voir l'état actuel en tête de ce document.

## Précautions

Les fichiers modifiés et ajoutés sont des changements de travail de l'utilisateur et de cette session, non commités. Ne pas les écraser ou supprimer. Ne pas prendre les anciens textes du README sur une application DFGSP2 comme preuve que la nouvelle plateforme DFGSP3 est déjà publiée. Le contenu porte sur la pharmacie et la sémiologie ; garder les explications pédagogiques distinctes des décisions de soins.
