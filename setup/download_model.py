from transformers import AutoModelForCausalLM, AutoTokenizer
import os
import sys

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