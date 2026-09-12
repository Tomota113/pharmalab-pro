# 🚀 Guide de Déploiement Cloud & Installation PWA (PharmaLab Pro)

Ce guide permet de déployer **PharmaLab Pro** en ligne en moins de 2 minutes pour donner à Oumou une URL sécurisée (ex: `https://oumou-pharmalab.vercel.app`) accessible sur tous ses appareils (ordinateur, tablette, smartphone) avec installation en application mobile (PWA).

---

## ⚡ Méthode 1 : Déploiement en 1 Clic sur Vercel (Recommandé & Gratuit)

Vercel est la plateforme d'hébergement la plus rapide au monde (propulsée par le réseau mondial Cloudflare/AWS).

### Option A : En ligne de commande (CLI Vercel)
Ouvrez votre terminal dans le dossier du projet et lancez :
```bash
npx vercel
```
1. Répondez `Y` (Oui) pour vous connecter ou créer un compte gratuit.
2. Acceptez les options par défaut (`Set up and deploy? [Y]`).
3. En **30 secondes**, Vercel vous donne une URL publique HTTPS sécurisée !

### Option B : Via GitHub (Déploiement Automatique Continu)
1. Créez un dépôt GitHub privé ou public et poussez le dossier :
   ```bash
   git init
   git add .
   git commit -m "feat: PharmaLab Pro PWA"
   git remote add origin https://github.com/VOTRE_COMPTE/pharmalab-pro.git
   git push -u origin main
   ```
2. Rendez-vous sur [vercel.com](https://vercel.com) et connectez-vous avec GitHub.
3. Cliquez sur **"Add New Project"**, sélectionnez votre dépôt `pharmalab-pro` et cliquez sur **"Deploy"**.
4. ✨ Votre site est en ligne avec certificat SSL gratuit ! Chaque fois que vous ferez un `git push`, le site se mettra à jour tout seul.

---

## 📱 Comment Oumou installe l'application sur son appareil (PWA)

Une fois le lien envoyé à Oumou (ex: `https://oumou-pharmalab.vercel.app`) :

### Sur iPhone / iPad (Safari) :
1. Elle ouvre le lien dans **Safari**.
2. Elle clique sur le bouton de partage en bas (l'icône avec le carré et la flèche vers le haut ⬆️).
3. Elle sélectionne **« Sur l'écran d'accueil »** (Add to Home Screen).
4. 🎉 L'icône **PharmaLab** apparaît sur son écran d'accueil comme n'importe quelle application téléchargée sur l'App Store. Elle s'ouvre en plein écran et fonctionne hors-ligne.

### Sur Android (Google Chrome) :
1. Elle ouvre le lien dans **Chrome**.
2. Un bouton vert **« 📲 Installer l'App »** apparaît en haut, ou elle clique sur les 3 points verticaux en haut à droite.
3. Elle clique sur **« Installer l'application »**.
4. 🎉 L'application est installée directement dans son tiroir d'applications.

### Sur Ordinateur (Mac / Windows / Chrome / Edge) :
1. Une petite icône d'installation apparaît dans la barre d'adresse du navigateur.
2. Un simple clic installe PharmaLab comme un logiciel de bureau indépendant de la fenêtre du navigateur.

---

## 🛡️ Fonctionnalités Hors-Ligne (Offline First)
Grâce au fichier `sw.js` (Service Worker) :
* Lors de la première visite, toutes les 24 monographies, structures 3D, simulateurs et cartes mémoires Anki sont automatiquement stockées dans le cache du navigateur.
* **Même sans 4G ni Wi-Fi** (dans le métro, à l'hôpital ou en voyage), l'application s'ouvre instantanément et toutes les fonctionnalités restent opérationnelles !
