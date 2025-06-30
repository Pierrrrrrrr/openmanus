#!/usr/bin/env bash
set -e
# Auto-create .env from the example on first run
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
  cp .env.example .env
fi


# Load environment variables if available
if [ -f ".env" ]; then
  export $(grep -v '^#' .env | xargs)
fi

python hf_space.py "$@"

python god_core.py "$@"

