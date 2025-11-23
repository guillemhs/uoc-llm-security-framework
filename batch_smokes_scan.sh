#!/bin/bash

# ================= CONFIGURATION =================

# 1. Define the list of probes (Comma separated, no spaces)
PROBES="dan.DAN_Jailbreak,dan.ChatGPT_Developer_Mode_v2,encoding.InjectBase64,promptinject.HijackHateHumansMini,realtoxicityprompts.RTPInsult,knownbadsignatures.EICAR,malwaregen.TopLevel,packagehallucination.Python,xss.MarkdownImageExfil"

# 2. Define the list of models to scan
# You can comment out lines with # to skip them
MODELS=(
    "openai-community/gpt2"
    "Qwen/Qwen3-0.6B"
    "Gensyn/Qwen2.5-0.5B-Instruct"
    "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    "meta-llama/Llama-3.2-1B-Instruct"
    "distilbert/distilgpt2"
    "google/gemma-2-2b-it"  # Note: Changed 'gemma-3' to 'gemma-2' as 3 is not standard yet, check your specific model name
)

# ================= EXECUTION LOOP =================

# Ensure the single run script is executable
chmod +x run_garak.sh

# Create a logs directory to keep things tidy
mkdir -p logs

echo "========================================"
echo "🚀 STARTING BATCH SCAN"
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
    # We use '2>&1' to capture errors too
    ./run_garak.sh "$model" "$PROBES" | tee "$LOG_FILE"
    
    echo "✅ Finished: $model"
    echo "📄 Log saved to: $LOG_FILE"
done

echo ""
echo "========================================"
echo "🏁 ALL SCANS COMPLETED"
echo "========================================"
