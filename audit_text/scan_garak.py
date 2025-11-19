import sys
import subprocess

# Agafa el model_id des de la línia de comandes
model_id = sys.argv[1]  # p. ex. "openai-community/gpt2"

# Defineix la comanda Garak
comanda = [
    "garak",
    "--model", f"huggingface/{model_id}",
    "--output", "resultats_garak.json"
]

# Executa la comanda
resultat = subprocess.run(comanda, capture_output=True, text=True)

# Mostra la sortida i errors (si n'hi ha)
print("Sortida Garak:\n", resultat.stdout)
if resultat.stderr:
    print("Errors Garak:\n", resultat.stderr)

print("Anàlisi Garak completada. Resultats desats a resultats_garak.json")
