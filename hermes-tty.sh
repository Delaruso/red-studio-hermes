#!/bin/bash
# Hermes-Style Terminal Monitor
# Opens a tmux session named 'hermes-out' that tails the live log.
# Usage: hermes-tty
SESSION="hermes-out"
LOG_GLOB="/home/sky/red\ studio\ hermes/logs/session_*.log"
tmux has-session -t "$SESSION" 2>/dev/null || tmux new-session -d -s "$SESSION" "bash -lc 'tail -F $LOG_GLOB || echo LOG_GLOB_MISSING; exec bash'"
tmux attach -t "$SESSION"
