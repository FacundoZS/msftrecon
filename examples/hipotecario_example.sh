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
# Redirect stderr to separate error log to preserve JSON integrity
ERROR_LOG="$OUTPUT_DIR/${DOMAIN}_errors.log"
JSON_OUTPUT="$OUTPUT_DIR/${DOMAIN}_results.json"

# Temporarily disable set -e to capture exit code
set +e
"$MSFTRECON_PATH" -d "$DOMAIN" -j > "$JSON_OUTPUT" 2>"$ERROR_LOG"
EXIT_CODE=$?
set -e

if [ $EXIT_CODE -eq 0 ]; then
    if [ -f "$JSON_OUTPUT" ]; then
        echo "[*] Reconnaissance complete!"
        echo "[*] Results saved to: $JSON_OUTPUT"
    else
        echo "[!] Warning: Scan reported success but output file was not created."
    fi
    # Remove error log if empty
    if [ ! -s "$ERROR_LOG" ]; then
        rm -f "$ERROR_LOG"
    fi
else
    echo "[!] Scan completed with errors (exit code: $EXIT_CODE)"
    if [ -f "$JSON_OUTPUT" ]; then
        echo "[*] Partial results may be available at: $JSON_OUTPUT"
    fi
    if [ -s "$ERROR_LOG" ]; then
        echo "[*] Error details: $ERROR_LOG"
    fi
fi
