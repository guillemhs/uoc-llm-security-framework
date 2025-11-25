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

hf auth login --token YOUR_HUGGINGFACE_API_TOKEN_HERE

export HUGGINGFACE_HUB_TOKEN=YOUR_HUGGINGFACE_API_TOKEN_HERE

# Reinstall your libraries
pip install -r requirements.txt

# Test the installation
./batch_test_scan.sh