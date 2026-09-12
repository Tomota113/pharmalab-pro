import json

# 1. Load SDF Database
with open('sdf_data.json', 'r', encoding='utf-8') as f:
    sdf_dict = json.load(f)
sdf_json_str = json.dumps(sdf_dict)

# 2. Load Full Pharmacology Database
with open('data/pharmacology_db.json', 'r', encoding='utf-8') as f:
    pharma_db = json.load(f)
pharma_json_str = json.dumps(pharma_db, ensure_ascii=False)

print(f"Loaded {len(sdf_dict)} 3D models and {len(pharma_db['molecules'])} complete drug monographs.")

# Read template_pro.html and replace placeholders
with open('template_pro.html', 'r', encoding='utf-8') as f:
    template = f.read()

output = template.replace('__SDF_DATABASE_JSON__', sdf_json_str)
output = output.replace('__PHARMACOLOGY_DB_JSON__', pharma_json_str)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(output)

print(f"Generated index.html successfully! Final size: {len(output)} bytes.")
