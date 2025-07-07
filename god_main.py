import asyncio

from app.agent.god import GodAgent
from app.logger import logger


async def main():
    agent = GodAgent()
    while True:
        try:
            prompt = input("Enter your prompt (or 'exit' to quit): ")
            if prompt.lower() == "exit":
                logger.info("Goodbye!")
                break
            if prompt.strip().isspace():
                logger.warning("Skipping empty prompt.")
                continue
            logger.warning("Processing your request...")
            result = await agent.run(prompt)
            logger.info(result)
        except KeyboardInterrupt:
            logger.warning("Goodbye!")
            break


if __name__ == "__main__":
    asyncio.run(main())
