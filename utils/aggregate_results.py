import json
import glob

# Ruta als fitxers de resultats
result_files = glob.glob('results/*.json')

# Diccionari per guardar tots els resultats
all_results = {}

# Llegeix cada fitxer de resultats i combina'ls
for file_path in result_files:
    if 'report' in file_path:  # Ignora el fitxer agregat si ja existeix
        continue
    with open(file_path, 'r') as file:
        test_name = file_path.split('/')[-1].replace('.json', '')
        all_results[test_name] = json.load(file)

# Escriu l'informe combinat
with open('results/report.json', 'w') as report_file:
    json.dump(all_results, report_file, indent=2)

print("Informe combinat generat a 'results/report.json'")