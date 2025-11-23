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
    print(f"Descarregant el model '{model_name}'...")
    model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir)
    tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
    print(f"Model i tokenizer descarregats correctament a '{cache_dir or os.path.expanduser('~/.cache/huggingface')}'.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        model_name = sys.argv[1]
    else:
        model_name = "ibm-granite/granite-4.0-1b"  # Valor per defecte

    download_model(model_name, CACHE_DIR)