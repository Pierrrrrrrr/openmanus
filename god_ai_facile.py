import asyncio
bc1kvb-codex/costruire-sistema-god-ai
from pathlib import Path

from app.env import load_env

import os
from pathlib import Path

main
from app.logger import logger
from god_core import GodCore


bc1kvb-codex/costruire-sistema-god-ai

def load_env() -> None:
    """Load variables from .env if present."""
    env_file = Path(".env")
    if not env_file.exists():
        return
    for line in env_file.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key, value)


main
async def main() -> None:
    load_env()
    inp = Path("manus_input.txt")
    out = Path("manus_output.txt")
    inp.touch(exist_ok=True)
    out.touch(exist_ok=True)
    prompt = inp.read_text().strip()
    if not prompt:
        prompt = input("Enter prompt: ")
    if not prompt:
        logger.error("No prompt provided.")
        return
    core = GodCore()
    result = await core.run(prompt)
    out.write_text(result)
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
