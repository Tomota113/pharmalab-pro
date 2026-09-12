#!/usr/bin/env bash

# ==============================================================================
# PharmaLab Pro (DFGSP2) - Lanceur Automatique 1-Clic
# Conçu pour une installation et un démarrage sans friction
# ==============================================================================

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

echo "=================================================================="
echo "  🏥 INITIALISATION DE PHARMALAB PRO (DFGSP2)"
echo "  L'Univers Interactif & Clinique des Antalgiques"
echo "=================================================================="

# 1. Vérification de Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ Erreur : Python 3 n'est pas installé sur cette machine."
    echo "Veuillez installer Python 3 (ex: sudo apt install python3) puis relancer."
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1)
echo "✅ $PYTHON_VERSION détecté."

# 2. Choix du port
PORT=8080
if lsof -Pi :8080 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "⚠️ Le port 8080 est déjà occupé, bascule sur le port 8081..."
    PORT=8081
fi

echo "🚀 Démarrage du serveur PharmaLab Pro sur http://localhost:$PORT ..."
python3 "$DIR/app.py" "$PORT" &
SERVER_PID=$!

# Fonction de nettoyage à l'arrêt
cleanup() {
    echo ""
    echo "🛑 Arrêt du serveur PharmaLab Pro (PID $SERVER_PID)..."
    kill $SERVER_PID 2>/dev/null || true
    echo "Au revoir !"
    exit 0
}
trap cleanup SIGINT SIGTERM

# 3. Attente du démarrage effectif du serveur
sleep 1.5

LOCAL_IP=$(python3 -c "import socket; s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(('8.8.8.8', 80)); print(s.getsockname()[0]); s.close()" 2>/dev/null || echo "127.0.0.1")
MOBILE_URL="http://$LOCAL_IP:$PORT"

echo ""
echo "=================================================================="
echo "  🎉 PHARMALAB PRO EST OPÉRATIONNEL !"
echo "  💻 Accès Ordinateur : $URL"
echo "  📱 Accès iPhone / iPad (même Wi-Fi) : $MOBILE_URL"
echo "  📚 Base de données : 24+ monographies DFGSP2 chargées"
echo "  🔬 Moteur Pharmacocinétique & Studio 3D actifs"
echo "=================================================================="
echo ""
echo "💡 Sur iPhone : Ouvrez Safari et collez : $MOBILE_URL"
echo "👉 Appuyez sur Ctrl+C dans ce terminal pour fermer l'application."
echo ""

# 4. Ouverture automatique du navigateur
if command -v xdg-open &> /dev/null; then
    xdg-open "$URL" >/dev/null 2>&1 || true
elif command -v open &> /dev/null; then
    open "$URL" >/dev/null 2>&1 || true
elif command -v google-chrome &> /dev/null; then
    google-chrome "$URL" >/dev/null 2>&1 || true
elif command -v firefox &> /dev/null; then
    firefox "$URL" >/dev/null 2>&1 || true
else
    echo "💡 Ouvrez manuellement votre navigateur et collez l'URL : $URL"
fi

# Maintien du processus au premier plan
wait $SERVER_PID
