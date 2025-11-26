from diffusers import DiffusionPipeline
from dotenv import load_dotenv
from huggingface_hub import login
import os
import sys
import torch

# Carrega variables del fitxer .env
load_dotenv()
token = os.getenv("HUGGINGFACE_HUB_TOKEN")

if not token:
    raise ValueError("No s'ha trobat el token al fitxer .env")

login(token)

CACHE_DIR = "./models_cache"

def download_image_model(model_name, cache_dir=None):
    final_path = os.path.abspath(cache_dir) if cache_dir else "Directori per defecte"
    print(f"Descarregant el model d'imatge '{model_name}' a: {final_path} ...")
    
    try:
        # CANVI CLAU: Utilitzem DiffusionPipeline en lloc d'AutoModelForCausalLM
        pipeline = DiffusionPipeline.from_pretrained(
            model_name,
            cache_dir=cache_dir,
            torch_dtype=torch.float16, # Opcional: estalvia espai i memòria
            use_safetensors=True
        )
        
        print(f"Model descarregat correctament.")
        print(f"Components del pipeline: {pipeline.config.keys()}")
        
        # Opcional: Moure a GPU si vols executar-lo ara
        # pipeline.to("cuda") # o "mps" per a Mac
        
    except Exception as e:
        print(f"Error descarregant el model: {e}")
        print("Assegura't que el model és un model de 'diffusers' (ex: stable-diffusion) i no un LLM.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        model_name = sys.argv[1]
    else:
        # Canviem el model per defecte a un d'imatge, ja que Granite és només text
        model_name = "CompVis/stable-diffusion-v1-4" 

    download_image_model(model_name, CACHE_DIR)