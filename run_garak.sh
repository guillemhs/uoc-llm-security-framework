#!/bin/bash

# 1. Check if a model name was provided
if [ -z "$1" ]; then
    echo "Error: No model name provided."
    echo "Usage: ./run_garak.sh <Model_ID> [Probes]"
    echo "Example: ./run_garak.sh Qwen/Qwen3-0.6B dan.DAN_Jailbreak"
    exit 1
fi

MODEL_ID=$1
# Default to 'continuation.Numbers' if no probe is specified
PROBES=${2:-continuation.Numbers} 

# 2. Activate Virtual Environment
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "Error: 'venv' directory not found."
    exit 1
fi

# 3. Download the model
echo "⬇️  Downloading/Verifying model: $MODEL_ID..."
python3 setup/download_model.py "$MODEL_ID"

# Check if download script succeeded
if [ $? -ne 0 ]; then
    echo "❌ Download failed."
    exit 1
fi

# 4. Dynamically find the snapshot path
# Hugging Face converts "/" to "--" in folder names (e.g., Qwen/Qwen3 -> models--Qwen--Qwen3)
DIR_NAME="models--${MODEL_ID//\//--}"
SNAPSHOTS_PATH="models_cache/$DIR_NAME/snapshots"

# Check if the directory exists
if [ ! -d "$SNAPSHOTS_PATH" ]; then
    echo "❌ Error: Could not find model directory at: $SNAPSHOTS_PATH"
    exit 1
fi

# Get the specific hash folder (takes the most recent one if multiple exist)
# We use 'ls' to get the folder name inside snapshots
HASH_FOLDER=$(ls -1 "$SNAPSHOTS_PATH" | head -n 1)
FULL_MODEL_PATH="$SNAPSHOTS_PATH/$HASH_FOLDER"

echo "✅ Model located at: $FULL_MODEL_PATH"

# 5. Run Garak
echo "🚀 Starting Garak scan with probes: $PROBES"
python3 -m garak \
    --model_type huggingface \
    --model_name "$FULL_MODEL_PATH" \
    --probes "$PROBES"

echo "🏁 Scan complete."