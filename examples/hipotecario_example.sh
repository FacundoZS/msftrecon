#!/bin/bash

# Example script to run msftrecon against hipotecario.com.ar domain
# This demonstrates how to execute the tool for reconnaissance

DOMAIN="hipotecario.com.ar"
OUTPUT_DIR="./output"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

echo "[*] Running msftrecon against domain: $DOMAIN"
echo "[*] Starting reconnaissance..."
echo ""

# Run basic scan
echo "[+] Executing basic scan..."
./msftrecon.py -d "$DOMAIN"

echo ""
echo "[+] Executing scan with JSON output..."
# Run scan with JSON output and save to file
./msftrecon.py -d "$DOMAIN" -j > "$OUTPUT_DIR/${DOMAIN}_results.json" 2>&1

echo ""
echo "[*] Reconnaissance complete!"
echo "[*] Results saved to: $OUTPUT_DIR/${DOMAIN}_results.json"
