"""Core engine that manages angels and tasks."""
from __future__ import annotations

from typing import Dict, List, Type

from .angels import Angel, Task
from .logger import Logger
from .task_storage import TaskStorage


class GodCore:
    """Minimal task orchestrator."""

    def __init__(self, storage: TaskStorage, logger: Logger) -> None:
        self.storage = storage
        self.logger = logger
        self.angels: Dict[str, Angel] = {}
        self.tasks: List[Task] = self.storage.load()

    def register_angel(self, angel_cls: Type[Angel]) -> None:
        angel = angel_cls()
        self.angels[angel.name] = angel
        self.logger.info(f"Registered angel: {angel.name}")

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
        self.storage.save(self.tasks)
        self.logger.info(f"Added task: {task.description}")

    def run(self) -> None:
        self.logger.info("Starting G.O.D. core loop")
        idx = 0
        while idx < len(self.tasks):
            task = self.tasks[idx]
            angel = self.angels.get(task.description)
            if not angel:
                self.logger.error(f"No angel found for task {task.description}")
                idx += 1
                continue
            result, new_tasks = angel.run(task)
            self.logger.info(f"Task {task.description} result: {result}")
            for nt in new_tasks:
                self.add_task(nt)
            idx += 1
