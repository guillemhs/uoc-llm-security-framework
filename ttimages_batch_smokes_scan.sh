#!/bin/bash

# ================= CONFIGURATION =================

# 1. Define the list of models to scan
MODELS=(
    "CompVis/stable-diffusion-v1-4"
    # "stabilityai/stable-diffusion-2-1"
)

# ================= EXECUTION LOOP =================

# Create a logs directory
mkdir -p logs

# --- ⏱️ CAPTURE START TIME ---
START_TIME=$(date +%s)
START_DATE=$(date)

echo ""
echo "========================================"
echo "🚀🛡️   STARTING IMAGE MODEL SECURITY SCAN"
echo "========================================"
echo "📅 Start Date:   $START_DATE"
echo "🤖 Total Models: ${#MODELS[@]}"
echo "========================================"

for model in "${MODELS[@]}"; do
    echo ""
    echo "----------------------------------------"
    echo "🎨🤖 PROCESSING MODEL: $model"
    echo "----------------------------------------"
    echo "🕒 [$(date +'%H:%M:%S')] Starting workflow..."
    
    # Timestamp for filename
    TIMESTAMP=$(date +'%Y%m%d_%H%M%S')
    # Safe filename (replace / with -)
    SAFE_MODEL_NAME="${model//\//-}"
    LOG_FILE="logs/scan_${SAFE_MODEL_NAME}_${TIMESTAMP}.log"
    
    echo "📝 Log file created: $LOG_FILE"

    # 1. DOWNLOAD STEP
    echo "📥☁️  Step 1: Downloading / Verifying model..."
    # Redirigim la sortida al log
    echo "   ... (Check log for download details)"
    python3 setup/download_text_to_image_model.py $model >> "$LOG_FILE" 2>&1

    # 2. Run Garak scan (Experimental)
    # Nota: Això pot fallar si Garak no suporta bé el pipeline d'imatges directament
    echo "🕵️‍♂️🔍 Step 2: Running Garak scan (Experimental)..."
    
    # Intentem trobar la ruta del snapshot automàticament
    SNAPSHOT_PATH="models_cache/models--${model//\//--}/snapshots/$(ls -1 models_cache/models--${model//\//--}/snapshots/ | head -n 1)"
    
    python3 -m garak \
        --target_type huggingface \
        --target_name "$SNAPSHOT_PATH" \
        --probes "test.Test" >> "$LOG_FILE" 2>&1

    # 3. SCAN STEP (El teu Mini-Garak)
    echo "🛡️🧪  Step 3: Running Custom Safeguard Test..."
    python3 audit_images/mini_safeguard.py $model >> "$LOG_FILE" 2>&1
    
    echo "✨✅  Finished scanning: $model"
done

# --- ⏱️ CAPTURE END TIME & CALCULATE DURATION ---
END_TIME=$(date +%s)
END_DATE=$(date)

DURATION=$((END_TIME - START_TIME))
HOURS=$((DURATION / 3600))
MINUTES=$(( (DURATION % 3600) / 60 ))
SECONDS=$((DURATION % 60))

echo ""
echo "========================================"
echo "🏁🎉  ALL SCANS COMPLETED"
echo "========================================"
echo "📅 End Date:   $END_DATE"
echo "⏱️  Total Time: ${HOURS}h ${MINUTES}m ${SECONDS}s"
echo "📂 Check the 'logs/' folder for details."
echo "========================================"