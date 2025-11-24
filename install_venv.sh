# #!/bin/bash
# This script creates a new Python virtual environment with Python 3.14
#python3.11 -m venv venv
python3.12 -m venv venv

# Activate the new env
source venv/bin/activate

# Check the version to be sure
python --version
# (Should say Python 3.11.x)

# Update pip first (good practice)
pip install --upgrade pip

# Reinstall your libraries
pip install -r requirements_text.txt
pip install -r requirements_images.txt

# Uninstall garak if already installed
pip uninstall -y garak

# Install garak from the main branch without dependencies (they are already installed)
pip install git+https://github.com/leondz/garak.git@main --no-deps

# Execute one model to test everything is working
# Set the URL to Hugging Face
export OPENAI_API_BASE="https://router.huggingface.co/v1"

# Put your HF Token in the OpenAI Key slot
export OPENAI_API_KEY="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxx" 
hf auth login --token YOUR_HUGGINGFACE_API_TOKEN_HERE
python3 -m garak --model_type huggingface.InferenceAPI --model_name Qwen/Qwen3-0.6B --probes test.Test

python3 -m garak --target_type huggingface --target_name gpt2 --probes test.Test