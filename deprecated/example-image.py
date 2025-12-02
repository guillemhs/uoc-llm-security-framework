import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="fal-ai",
    api_key=os.environ["HF_INFERENCE_TOKEN"],
)

# output is a PIL.Image object
image = client.text_to_image(
    "A robot playing chess with a human",
    model="black-forest-labs/FLUX.1-dev",
)