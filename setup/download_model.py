from transformers import AutoModelForCausalLM, AutoTokenizer
import os

# Defineix el nom del model que vols descarregar
#MODEL_NAME = "openai-community/gpt2"  # Substitueix pel model que necessitis
MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"  # Substitueix pel model que necessitis

# Opcional: Ruta personalitzada per descarregar el model (deixa-ho buit per usar la cache predeterminada)
CACHE_DIR = "./models_cache"  # Pots canviar-ho o deixar-ho com None per usar ~/.cache/huggingface

def download_model(model_name, cache_dir=None):
    """
    Descarrega el model i el tokenizer de HuggingFace i els guarda a la cache local.
    :param model_name: Nom del model a descarregar (HuggingFace model hub).
    :param cache_dir: Ruta personalitzada per a la cache (opcional).
    """
    print(f"Descarregant el model '{model_name}'...")
    model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=cache_dir)
    tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
    print(f"Model i tokenizer descarregats correctament a '{cache_dir or os.path.expanduser('~/.cache/huggingface')}'.")

if __name__ == "__main__":
    download_model(MODEL_NAME, CACHE_DIR)