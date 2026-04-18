#!/bin/bash
set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="$PROJECT_DIR/logs"
mkdir -p "$LOG_DIR"

cd "$PROJECT_DIR"

pkill -f "python3 app/main.py" || true
pkill -f "python3 app/dashboard.py" || true

nohup python3 app/main.py > "$LOG_DIR/tester_stdout.log" 2>&1 &
nohup python3 app/dashboard.py > "$LOG_DIR/dashboard_stdout.log" 2>&1 &

echo "Amir Orange Cable Tester started."
echo "Dashboard: http://0.0.0.0:8080"
