"""Angel for simple text processing."""
from __future__ import annotations

from . import Angel, Task


class TextAngel(Angel):
    name = "text_angel"

    def run(self, task: Task) -> tuple[str, list[Task]]:
        text = str(task.data or "")
        # Example text processing: return length and uppercase version
        result = f"Length: {len(text)} - Upper: {text.upper()}"
        return result, []
