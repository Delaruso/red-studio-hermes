#!/bin/bash
# Red Architecture — Hermes Session Logger
# Usage: source this file or call it as: hermes-log "command"
# Example: hermes-log "ls -la"

LOG_DIR="/home/sky/red studio hermes/logs"
SESSION=$(date +%Y-%m-%d_%H-%M-%S)
LOG_FILE="$LOG_DIR/session_$SESSION.log"

log() {
    echo "[$(date -Iseconds)] $*" | tee -a "$LOG_FILE"
}

log "=== SESSION START ==="
log "User: $USER"
log "PWD: $(pwd)"
log "Hermes Profile: default"

# If arguments provided, run them and log output
if [ $# -gt 0 ]; then
    log "RUN: $*"
    "$@" 2>&1 | tee -a "$LOG_FILE"
    log "EXIT: $?"
fi

log "=== SESSION END ==="
