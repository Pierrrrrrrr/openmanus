import asyncio

from app.logger import logger
from god_core import GodCore


async def main() -> None:
    try:
        with open("manus_input.txt", "r") as f:
            prompt = f.read().strip()
    except FileNotFoundError:
        logger.error("manus_input.txt not found")
        return

    if not prompt:
        logger.error("No prompt provided in manus_input.txt")
        return

    core = GodCore()
    result = await core.run(prompt)

    with open("manus_output.txt", "w") as f:
        f.write(result)
    logger.info("Response written to manus_output.txt")


if __name__ == "__main__":
    asyncio.run(main())
