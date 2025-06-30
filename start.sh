#!/usr/bin/env bash
set -e
# Load environment variables if available
if [ -f ".env" ]; then
  export $(grep -v '^#' .env | xargs)
fi
python god_core.py "$@"
