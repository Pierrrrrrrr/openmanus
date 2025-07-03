import asyncio
import os
import sys
from pathlib import Path

from app.logger import logger
from god_core import GodCore


def load_env() -> None:
    env = Path(".env")
    if not env.exists():
        return
    for line in env.read_text().splitlines():
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k, v)


def in_colab() -> bool:
    return "google.colab" in sys.modules


async def run_cli() -> None:
    core = GodCore()
    logger.info("GOD AI ready. Type 'exit' to quit.")
    while True:
        try:
            prompt = input("GOD> ")
            if prompt.lower() == "exit":
                break
            if not prompt.strip():
                continue
            result = await core.run(prompt)
            print(result)
        except KeyboardInterrupt:
            break


def main() -> None:
    load_env()
    if in_colab():
        print("Running in Google Colab. Ensure GPU is allocated for Mixtral.")
    asyncio.run(run_cli())


if __name__ == "__main__":
    main()
