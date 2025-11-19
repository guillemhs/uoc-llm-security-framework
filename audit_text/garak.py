import sys
import garak

# Utilitza el nom del model de Hugging Face o el camí local des de la línia de comandes
model_id = sys.argv[1]  # p. ex. "gpt2" o "/camí/al/model/local"

# Executa l'anàlisi Garak sobre el model
resultats = garak.scan(f"huggingface/{model_id}")

# Desa els resultats en un fitxer JSON
import json
with open('resultats_garak.json', 'w') as f:
    json.dump(resultats, f, indent=2, ensure_ascii=False)

print("Anàlisi Garak completada. Resultats desats a resultats_garak.json")