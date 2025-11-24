# #!/bin/bash
# This script creates a new Python virtual environment with Python 3.14
python3.11 -m venv venv

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
