from pydantic import Field

from app.agent.manus import Manus
from app.tool import (
    AutoReflector,
    BrowserUseTool,
    FileSaver,
    GoogleSearch,
    PythonExecute,
    Terminate,
    ToolCollection,
)
from app.tool.code_optimizer import CodeOptimizerTool


class GodAgent(Manus):
    """Advanced agent that extends Manus with code optimization abilities."""

    name: str = "god"
    description: str = (
        "Autonomous DevOps agent combining Manus capabilities with code optimization."
    )

    available_tools: ToolCollection = Field(
        default_factory=lambda: ToolCollection(
            PythonExecute(),
            GoogleSearch(),
            BrowserUseTool(),
            FileSaver(),
            CodeOptimizerTool(),
            AutoReflector(),
            Terminate(),
        )
    )
