from typing import Dict

from app.llm import LLM
from app.tool.base import BaseTool


class CodeOptimizerTool(BaseTool):
    """Use an LLM to improve a piece of Python code."""

    name: str = "code_optimize"
    description: str = (
        "Generate an optimized version of the provided Python code using an LLM."
    )
    parameters: dict = {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": "Python source code to optimize",
            }
        },
        "required": ["code"],
    }

    llm: LLM = LLM()

    async def execute(self, code: str) -> Dict[str, str]:
        prompt = (
            "You are a senior Python developer. Refactor and optimize the "
            "following code. Only return the improved code.\n\n" + code
        )
        optimized = await self.llm.ask(
            [{"role": "user", "content": prompt}], stream=False
        )
        return {"observation": optimized}
