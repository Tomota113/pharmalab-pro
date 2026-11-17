/* ========================================================================= */
/* PharmaLab Pro • Service Worker (Offline Engine & PWA Caching)             */
/* ========================================================================= */

const CACHE_NAME = 'pharmalab-pro-v15';

const PRECACHE_ASSETS = [
  './',
  './index.html',
  './apprendre.html',
  './lire.html',
  './learning.css',
  './learning.js',
  './learning-data.json',
  './reader.css',
  './reader.js',
  './vendor/pdfjs/pdf.mjs?v=15',
  './vendor/pdfjs/pdf.worker.mjs?v=15',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon.svg',
  './icons/apple-touch-icon.png'
];

/* Installation: Pre-cache core application shell */
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[ServiceWorker] Mise en cache de l\'application shell...');
      return cache.addAll(PRECACHE_ASSETS).catch((err) => {
        console.warn('[ServiceWorker] Avertissement sur certains assets de pré-cache:', err);
      });
    }).then(() => self.skipWaiting())
  );
});

/* Activation: Clean up older cache versions */
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames.map((cache) => {
          if (cache !== CACHE_NAME) {
            console.log('[ServiceWorker] Purge de l\'ancien cache:', cache);
            return caches.delete(cache);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

/* Fetch: Stale-While-Revalidate / Cache-First strategy */
self.addEventListener('fetch', (event) => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;

  // Les corrections des cours doivent apparaître dès la première visite en ligne.
  // Le cache reste disponible si la connexion est absente.
  const url = new URL(event.request.url);
  const isLearningAsset = url.origin === self.location.origin &&
    /\/(?:index\.html|apprendre\.html|lire\.html|learning-data\.json|learning\.js|learning\.css|reader\.js|reader\.css)$/.test(url.pathname);
  if (event.request.mode === 'navigate' || isLearningAsset) {
    event.respondWith(
      fetch(event.request).then((response) => {
        if (response.ok) {
          const copy = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, copy));
        }
        return response;
      }).catch(async () => {
        const cached = await caches.match(event.request);
        if (cached) return cached;
        if (event.request.mode === 'navigate') {
          // Les paramètres choisissent le cours côté JS : le même HTML suffit
          // même si cette combinaison de cours/page n'a jamais été visitée.
          const shell = await caches.match(url.pathname, {ignoreSearch: true});
          return shell || await caches.match('./index.html') || Response.error();
        }
        return Response.error();
      })
    );
    return;
  }

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        // Return from cache, but update cache in background if online
        fetch(event.request).then((networkResponse) => {
          if (networkResponse && networkResponse.status === 200) {
            const clone = networkResponse.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
          }
        }).catch(() => {
          // Offline, cached response was already served
        });
        return cachedResponse;
      }

      // Not in cache: fetch from network and store in cache
      return fetch(event.request).then((networkResponse) => {
        if (!networkResponse || networkResponse.status !== 200) {
          return networkResponse;
        }
        const clone = networkResponse.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, clone);
        });
        return networkResponse;
      }).catch(() => {
        // If offline and requesting an HTML document, fallback to index.html
        if (event.request.headers.get('accept')?.includes('text/html')) {
          return caches.match('./index.html');
        }
      });
    })
  );
});
