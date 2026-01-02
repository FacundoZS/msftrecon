#!/bin/bash
set -e

# Example script to run msftrecon against hipotecario.com.ar domain
# This demonstrates how to execute the tool for reconnaissance

DOMAIN="hipotecario.com.ar"
OUTPUT_DIR="./output"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MSFTRECON_PATH="${SCRIPT_DIR}/../msftrecon.py"

# Verify msftrecon.py exists
if [ ! -f "$MSFTRECON_PATH" ]; then
    echo "[!] Error: msftrecon.py not found at $MSFTRECON_PATH"
    exit 1
fi

# Make sure it's executable
if [ ! -x "$MSFTRECON_PATH" ]; then
    chmod +x "$MSFTRECON_PATH"
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

echo "[*] Running msftrecon against domain: $DOMAIN"
echo "[*] Starting reconnaissance..."
echo ""

# Run basic scan
echo "[+] Executing basic scan..."
"$MSFTRECON_PATH" -d "$DOMAIN"

echo ""
echo "[+] Executing scan with JSON output..."
# Run scan with JSON output and save to file
if "$MSFTRECON_PATH" -d "$DOMAIN" -j > "$OUTPUT_DIR/${DOMAIN}_results.json"; then
    echo "[*] Reconnaissance complete!"
    echo "[*] Results saved to: $OUTPUT_DIR/${DOMAIN}_results.json"
else
    echo "[!] Scan completed with errors. Check $OUTPUT_DIR/${DOMAIN}_results.json for details."
fi
