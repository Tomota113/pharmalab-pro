#!/usr/bin/env python3
"""
PharmaLab Pro Server (DFGSP2)
Serveur applicatif autonome pour l'apprentissage de la pharmacologie des antalgiques.
Zéro dépendance externe requise (utilise la bibliothèque standard Python 3).
"""

import http.server
import socketserver
import json
import os
import math
import urllib.parse

PORT = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, 'data', 'pharmacology_db.json')

# Load database once into memory
with open(DB_FILE, 'r', encoding='utf-8') as f:
    DB = json.load(f)

MOLECULES_MAP = {m['id']: m for m in DB['molecules']}


def simulate_pk(dose, ka, ke, vd, f_bio, interval_tau=6, num_doses=4, points_per_hour=10):
    """
    Simulation pharmacocinétique modèle ouvert à 1 compartiment avec absorption extravasculaire.
    C(t) = [ (F * Dose * ka) / (Vd * (ka - ke)) ] * [ exp(-ke * t) - exp(-ka * t) ]
    Pour doses répétées : principe de superposition linéaire.
    """
    dose = float(dose)
    ka = float(ka)
    ke = float(ke)
    vd = float(vd)
    f_bio = float(f_bio)
    interval_tau = float(interval_tau)
    num_doses = int(num_doses)

    total_time = interval_tau * num_doses
    step = 1.0 / points_per_hour
    time_points = []
    current_t = 0.0

    while current_t <= total_time:
        time_points.append(round(current_t, 2))
        current_t += step

    concentrations = []
    c_max_all = 0.0

    for t in time_points:
        c_total = 0.0
        # Sum contributions from all previous doses up to time t
        for d in range(num_doses):
            t_dose = d * interval_tau
            if t >= t_dose:
                dt = t - t_dose
                if abs(ka - ke) > 1e-4:
                    c = ((f_bio * dose * ka) / (vd * (ka - ke))) * (math.exp(-ke * dt) - math.exp(-ka * dt))
                else:
                    c = ((f_bio * dose * ka) / vd) * dt * math.exp(-ke * dt)
                if c > 0:
                    c_total += c
        
        c_val = round(max(0.0, c_total), 2)
        concentrations.append(c_val)
        if c_val > c_max_all:
            c_max_all = c_val

    # Steady state theoretical approximations
    # Css_max = [ (F * Dose * ka) / (Vd * (ka - ke)) ] * [ 1 / (1 - exp(-ke * tau)) ] (approx)
    r_factor = 1.0 / (1.0 - math.exp(-ke * interval_tau))
    c_ss_max = round(c_max_all * 0.95 * min(r_factor, 3.0), 2)
    c_ss_min = round(concentrations[-1], 2)
    t_half = round(math.log(2) / ke, 1)

    return {
        "time_points": time_points,
        "concentrations": concentrations,
        "c_max": round(c_max_all, 2),
        "c_ss_min": c_ss_min,
        "c_ss_max": c_ss_max,
        "t_half": t_half,
        "dose": dose,
        "interval_tau": interval_tau,
        "num_doses": num_doses
    }


def calculate_opioid_rotation(from_drug, to_drug, dose_24h, cross_tolerance_reduction=0.30):
    """
    Calcul hospitalier de rotation d'opioïdes avec tolérance croisée incomplète (SFAP / ANSM).
    """
    dose_24h = float(dose_24h)
    red = float(cross_tolerance_reduction)

    # Conversion factors to Morphine Orale (Per Os) base in mg/24h
    TO_MORPHINE_PO = {
        "morphine_po": 1.0,
        "morphine_sc": 2.0,      # 1 mg SC = 2 mg PO
        "morphine_iv": 3.0,      # 1 mg IV = 3 mg PO
        "oxycodone_po": 2.0,     # 1 mg Oxycodone PO ~ 2 mg Morphine PO
        "oxycodone_iv": 4.0,     # 1 mg Oxycodone IV ~ 4 mg Morphine PO
        "fentanyl_patch": 2.4,   # 25 µg/h patch ~ 60 mg/j morphine PO => ratio 60/25 = 2.4
        "hydromorphone_po": 7.5, # 4 mg Sophidone ~ 30 mg Morphine PO => ratio 7.5
        "tramadol_po": 0.2,      # 100 mg Tramadol ~ 20 mg Morphine PO => ratio 0.2
        "codeine_po": 0.1667     # 60 mg Codéine ~ 10 mg Morphine PO => ratio 1/6
    }

    equiv_morphine_po = dose_24h * TO_MORPHINE_PO.get(from_drug, 1.0)
    
    # Target conversion
    to_ratio = TO_MORPHINE_PO.get(to_drug, 1.0)
    target_dose_brute = equiv_morphine_po / to_ratio
    
    # Apply cross tolerance reduction (usually 25% to 50% decrease)
    target_dose_recommandee = target_dose_brute * (1.0 - red)
    
    # Breakthrough pain dose (ADP) : 1/6th of total daily dose
    adp_interdose = round(target_dose_recommandee / 6.0, 1)

    return {
        "from_drug": from_drug,
        "to_drug": to_drug,
        "initial_dose": dose_24h,
        "equiv_morphine_po_24h": round(equiv_morphine_po, 1),
        "target_dose_brute": round(target_dose_brute, 1),
        "cross_tolerance_percent": int(red * 100),
        "target_dose_recommandee": round(target_dose_recommandee, 1),
        "adp_interdose_li": adp_interdose
    }


class PharmaLabHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Enable CORS for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == '/api/molecules':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            # Summary list
            summary = [
                {
                    "id": m["id"],
                    "name": m["name"],
                    "dci": m["dci"],
                    "class_name": m["class_name"],
                    "palier": m["palier"],
                    "palier_label": m["palier_label"],
                    "formula": m["formula"]
                }
                for m in DB['molecules']
            ]
            self.wfile.write(json.dumps({"total": len(summary), "molecules": summary}, ensure_ascii=False).encode('utf-8'))
            return

        elif path.startswith('/api/molecules/'):
            mol_id = path.replace('/api/molecules/', '').strip()
            if mol_id in MOLECULES_MAP:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps(MOLECULES_MAP[mol_id], ensure_ascii=False).encode('utf-8'))
            else:
                self.send_error(404, f"Molecule '{mol_id}' non trouvée.")
            return

        elif path == '/api/health':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "app": "PharmaLab Pro", "version": "2.0"}).encode('utf-8'))
            return

        # Serve static files from current directory
        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        content_len = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_len)

        try:
            req_data = json.loads(post_body.decode('utf-8')) if post_body else {}
        except Exception:
            req_data = {}

        if path == '/api/pk-simulate':
            dose = req_data.get('dose', 1000)
            ka = req_data.get('ka', 1.8)
            ke = req_data.get('ke', 0.28)
            vd = req_data.get('vd', 60.0)
            f_bio = req_data.get('f_bio', 0.85)
            interval_tau = req_data.get('interval_tau', 6.0)
            num_doses = req_data.get('num_doses', 4)

            # Adjust ke if renal function DFG is given
            dfg = req_data.get('dfg', 100)
            if dfg < 30:
                ke = ke * 0.45  # significant elongation of half-life
            elif dfg < 60:
                ke = ke * 0.75

            sim_result = simulate_pk(dose, ka, ke, vd, f_bio, interval_tau, num_doses)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(sim_result).encode('utf-8'))
            return

        elif path == '/api/opioid-rotation':
            from_drug = req_data.get('from_drug', 'morphine_po')
            to_drug = req_data.get('to_drug', 'oxycodone_po')
            dose = req_data.get('dose_24h', 60)
            reduction = req_data.get('cross_tolerance_reduction', 0.30)

            rot_result = calculate_opioid_rotation(from_drug, to_drug, dose, reduction)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(rot_result).encode('utf-8'))
            return

        self.send_error(404, "Endpoint POST non trouvé")


def run_server(port=PORT):
    handler = PharmaLabHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"===============================================================")
        print(f"🏥 PHARMALAB PRO SERVER DÉMARRÉ SUR : http://localhost:{port}")
        print(f"📚 Base Pharmacologique : {len(MOLECULES_MAP)} molécules chargées")
        print(f"===============================================================")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nArrêt du serveur PharmaLab Pro.")
            httpd.server_close()


if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    run_server(port)
