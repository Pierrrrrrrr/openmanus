import asyncio
import sys

from app.env import load_env
from app.logger import logger
from god_core import GodCore


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
zjbow5-codex/costruire-sistema-god-ai
    load_env(prompt_missing=True)

    load_env()
 main
    if in_colab():
        print("Running in Google Colab. Ensure GPU is allocated for Mixtral.")
    asyncio.run(run_cli())


if __name__ == "__main__":
    main()
