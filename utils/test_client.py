import os
from openai import OpenAI

# Ensure your token is set in your terminal: export HF_INFERENCE_TOKEN="hf_..."
token = os.getenv("HF_INFERENCE_TOKEN")

if not token:
    raise ValueError("Please set the HF_INFERENCE_TOKEN environment variable.")

# Configure the client to point to Hugging Face's Router
client = OpenAI(
    base_url="https://router.huggingface.co/v1", 
    api_key=token
)

# You must use a model supported by the Inference API (e.g., Qwen, Llama, etc.)
# GPT-2 often fails on the chat/v1 endpoint, so we use a newer model for the test.
model_name = "google/gemma-3-1b-it" 

try:
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": "Hello, are you working?"}
        ],
        max_tokens=50
    )
    print(f"Success! Response from {model_name}:")
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}")
