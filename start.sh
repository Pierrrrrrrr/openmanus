#!/usr/bin/env bash
set -e
# Auto-create .env from the example on first run
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
  cp .env.example .env
fi

zjbow5-codex/costruire-sistema-god-ai

bc1kvb-codex/costruire-sistema-god-ai
 main
# Load variables from .env only when not already set (keeps HF secrets intact)
if [ -f ".env" ]; then
  while IFS='=' read -r key value; do
    if [ -n "$key" ] && [ -z "${!key}" ]; then
      export "$key"="$value"
    fi
  done < <(grep -v '^#' .env)
fi
if [ "$1" = "cli" ]; then
  shift
  python god_launcher.py "$@"
else
  python hf_space.py "$@"
fi
 zjbow5-codex/costruire-sistema-god-ai



# Load environment variables if available
if [ -f ".env" ]; then
  export $(grep -v '^#' .env | xargs)
fi

python hf_space.py "$@"

python god_core.py "$@"

main
main
