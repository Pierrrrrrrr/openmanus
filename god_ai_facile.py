import asyncio
from pathlib import Path

from app.env import load_env
from app.logger import logger
from god_core import GodCore


async def main() -> None:
    load_env(prompt_missing=True)
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
