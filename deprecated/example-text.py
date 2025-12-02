import os
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_INFERENCE_TOKEN"],
)

completion = client.chat.completions.create(
#openai-community/gpt2
#Qwen/Qwen3-0.6B
#Gensyn/Qwen2.5-0.5B-Instruct
#TinyLlama/TinyLlama-1.1B-Chat-v1.0
#meta-llama/Llama-3.2-1B-Instruct
#distilbert/distilgpt2
#google/gemma-3-1b-it

    model="moonshotai/Kimi-K2-Instruct-0905",
    messages=[
        {
            "role": "user",
            "content": "Describe the process of photosynthesis."
        }
    ],
)

print(completion.choices[0].message)