from transformers import AutoModelForCausalLM, AutoTokenizer
from dotenv import load_dotenv
from huggingface_hub import login
import os
import sys

# Carrega variables del fitxer .env
load_dotenv()
token = os.getenv("HUGGINGFACE_HUB_TOKEN")

print(f"Valor del token: {token}")  # Mostra el valor carregat

if not token:
    raise ValueError("No s'ha trobat el token HUGGINGFACE_HUB_TOKEN al fitxer .env")

login(token)

CACHE_DIR = "./models_cache"  # Pots canviar-ho o deixar-ho com None

def download_model(model_name, cache_dir=None):
    # Determinem la ruta real per mostrar-la al print
    final_path = os.path.abspath(cache_dir) if cache_dir else "Directori per defecte (~/.cache/huggingface)"
    
    print(f"Descarregant el model '{model_name}' a la carpeta: {final_path} ...")
    
    # Opció B: device_map="auto" (Requereix 'pip install accelerate')
    # Això carregarà el model a la GPU (MPS) si està disponible, o CPU si no.
    model = AutoModelForCausalLM.from_pretrained(
        model_name, 
        cache_dir=cache_dir, 
        device_map="auto"
    )
    
    print(f"El model s'ha carregat al dispositiu: {model.device}")

    tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
    print(f"Model i tokenizer descarregats i carregats correctament.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        model_name = sys.argv[1]
    else:
        model_name = "ibm-granite/granite-4.0-1b"  # Valor per defecte

    download_model(model_name, CACHE_DIR)