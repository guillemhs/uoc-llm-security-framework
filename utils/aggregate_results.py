import json
import glob
import sys
from datetime import datetime

# Comprova que el nom del model es passa com a argument
if len(sys.argv) < 2:
    print("Ús: python script.py <nom_model>")
    sys.exit(1)

model_name = sys.argv[1]
# Substitueix espais, barres i guions per guions baixos per evitar errors en el nom del fitxer
model_name_clean = (
    model_name.replace(' ', '_')
              .replace('/', '_')
              .replace('-', '_')
)

# Recull tots els fitxers de resultats del directori 'results'
result_files = glob.glob('results/*.json')

# Diccionari per guardar tots els resultats
all_results = {}

# Llegeix cada fitxer de resultats i els combina en un sol diccionari
for file_path in result_files:
    if 'report' in file_path:  # Ignora els fitxers d'informe existents
        continue
    with open(file_path, 'r') as file:
        test_name = file_path.split('/')[-1].replace('.json', '')
        all_results[test_name] = json.load(file)

# Afegeix la data/hora actual i el nom del model
timestamp = datetime.now().isoformat(timespec='seconds')
timestamp_filename = timestamp.replace('-', '_').replace(':', '_')
report = {
    "timestamp": timestamp,
    "model_name": model_name,
    "results": all_results
}

# Genera el nom del fitxer d'informe amb el format desitjat
report_filename = f'results/report_{model_name_clean}_{timestamp_filename}.json'

# Escriu l'informe combinat al fitxer corresponent
with open(report_filename, 'w') as report_file:
    json.dump(report, report_file, indent=2, ensure_ascii=False)

print(f"Informe combinat generat a '{report_filename}'")