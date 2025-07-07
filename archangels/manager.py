import asyncio
from importlib import import_module
from typing import List

from app.agent.god import GodAgent


class ArchangelManager:
    """Load and coordinate archangels dynamically."""

    names = [
        "prometheus",
        "hermes",
        "albedo",
        "metatron",
        "azazel",
        "bezalel",
        "sandalphon",
        "raphael",
        "samael",
        "uriel",
        "raziel",
        "ariel",
    ]

    def __init__(self) -> None:
        self.archangels: List[GodAgent] = []
        for name in self.names:
            mod = import_module(f"archangels.{name}")
            cls = next(
                obj
                for obj in mod.__dict__.values()
                if isinstance(obj, type) and issubclass(obj, GodAgent)
            )
            self.archangels.append(cls())

    async def run_all(self, prompt: str) -> List[str]:
        tasks = [arc.run(prompt) for arc in self.archangels]
        return await asyncio.gather(*tasks)
