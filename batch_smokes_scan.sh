#!/bin/bash

# ================= CONFIGURATION =================

# 1. Define the list of probes (Comma separated, no spaces)
# NOTE: Using garak LLM vulnerability scanner v0.13.3.pre1 
#PROBES="test.Test" 
PROBES="encoding.InjectBase64,dan.DanInTheWild,promptinject.HijackHateHumans,packagehallucination.Python,exploitation.SQLInjectionEcho,lmrc.SlurUsage,glitch.Glitch"

# 2. Define the list of models to scan
MODELS=(
    "openai-community/gpt2"
    "Qwen/Qwen3-0.6B"
    "Gensyn/Qwen2.5-0.5B-Instruct"
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    "meta-llama/Llama-3.2-1B-Instruct"
    "distilbert/distilgpt2"
    "google/embeddinggemma-300m" 
)

# ================= EXECUTION LOOP =================

# Ensure the single run script is executable
chmod +x run_garak.sh

# Create a logs directory to keep things tidy
mkdir -p logs

# --- ⏱️ CAPTURE START TIME ---
START_TIME=$(date +%s)
START_DATE=$(date)

echo "========================================"
echo "🚀 STARTING BATCH SCAN"
echo "📅 Start Date: $START_DATE"
echo "Total Models: ${#MODELS[@]}"
echo "========================================"

for model in "${MODELS[@]}"; do
    echo ""
    echo "----------------------------------------"
    echo "🕒 [$(date +'%H:%M:%S')] Starting scan for: $model"
    echo "----------------------------------------"
    
    # Create a safe filename for the log (replace / with -)
    LOG_FILE="logs/scan_${model//\//-}.log"
    
    # Execute the script and pipe output to both screen and log file
    ./run_garak.sh "$model" "$PROBES" | tee "$LOG_FILE"
    
    echo "✅ Finished: $model"
    echo "📄 Log saved to: $LOG_FILE"
done

# --- ⏱️ CAPTURE END TIME & CALCULATE DURATION ---
END_TIME=$(date +%s)
END_DATE=$(date)

# Calculate duration in seconds
DURATION=$((END_TIME - START_TIME))

# Convert to Hours, Minutes, Seconds
HOURS=$((DURATION / 3600))
MINUTES=$(( (DURATION % 3600) / 60 ))
SECONDS=$((DURATION % 60))

echo ""
echo "========================================"
echo "🏁 ALL SCANS COMPLETED"
echo "📅 End Date:   $END_DATE"
echo "⏱️  Total Time: ${HOURS}h ${MINUTES}m ${SECONDS}s"
echo "========================================"