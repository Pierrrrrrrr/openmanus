"""Utilities to persist tasks."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List

from .angels import Task


class TaskStorage:
    """Save and load tasks from a JSON file."""

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        if not self.path.exists():
            self.path.write_text("[]")

    def load(self) -> List[Task]:
        data = json.loads(self.path.read_text())
        return [Task(**item) for item in data]

    def save(self, tasks: Iterable[Task]) -> None:
        json.dump([task.__dict__ for task in tasks], self.path.open("w"), indent=2)
