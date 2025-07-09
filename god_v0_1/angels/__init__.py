"""Angel base class and default angels."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Tuple


@dataclass
class Task:
    """A simple task object."""

    description: str
    data: Any | None = None


class Angel:
    """Base class for all angels."""

    name: str = "angel"

    def run(self, task: Task) -> Tuple[str, List[Task]]:
        """Process a task and optionally return new tasks."""
        raise NotImplementedError
