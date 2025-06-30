from app.llm import LLM
from app.logger import logger
from app.tool.base import BaseTool


class AutoReflector(BaseTool):
    """Analyze outputs and suggest improvements."""

    name: str = "self_reflect"
    description: str = "Reflect on recent output and propose code improvements"
    parameters: dict = {
        "type": "object",
        "properties": {
            "output": {"type": "string", "description": "Output to reflect on"}
        },
        "required": ["output"],
    }

    llm: LLM = LLM()

    async def execute(self, output: str) -> dict:
        prompt = (
            "You are a senior engineer. Analyze the following output and suggest "
            "code improvements.\n\n" + output
        )
        suggestion = await self.llm.ask(
            [{"role": "user", "content": prompt}], stream=False
        )
        logger.info("Reflection suggestion: %s", suggestion.strip())
        return {"observation": suggestion}
