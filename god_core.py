import asyncio
import os
from pathlib import Path

import requests

from app.logger import logger
from app.task import record_task
from arc_gabriel import ArcGabriel
from arc_michael import ArcMichael
from arc_raphael import ArcRaphael
from telegram_report import send_telegram


def ask_deepseek(prompt: str) -> str:
    """Query DeepSeek API and return the response text."""
    headers = {
        "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY', '')}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "deepseek-coder",
        "messages": [{"role": "user", "content": prompt}],
    }
    try:
        resp = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        data = resp.json()
        return data["choices"][0]["message"]["content"]
    except Exception as exc:  # pragma: no cover - best effort
        logger.error("DeepSeek request failed: %s", exc)
        return ""


class GodCore:
    """Central orchestrator that coordinates Arcangels."""

    def __init__(self) -> None:
        self.arcs = [ArcMichael(), ArcRaphael(), ArcGabriel()]
        self.angel_dir = Path("angels")
        self.angel_dir.mkdir(exist_ok=True)
        send_telegram("GOD AI attivato su Hugging Face.")

    async def run(self, prompt: str) -> str:
        """Dispatch the prompt to all Arcangels in parallel."""
        ds_response = ask_deepseek(prompt)
        record_task(prompt, "deepseek", bool(ds_response))
        tasks = [arc.run(prompt) for arc in self.arcs]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        outputs = []
        for arc, result in zip(self.arcs, results):
            if isinstance(result, Exception):
                logger.error(f"{arc.name} failed: {result}")
                record_task(prompt, arc.name, False)
                retry = await self._spawn_angel(arc, prompt)
                outputs.append(retry)
            else:
                record_task(prompt, arc.name, True)
                outputs.append(result)
        return ds_response + "\n\n" + "\n\n".join(outputs)

    async def _spawn_angel(self, arc, prompt: str) -> str:
        """Create a simple angel script and retry the task."""
        idx = len(list(self.angel_dir.glob(f"{arc.name}_*.py"))) + 1
        path = self.angel_dir / f"{arc.name}_{idx:03d}.py"
        content = (
            f"from {arc.__class__.__module__} import {arc.__class__.__name__}\n\n"
            f"class Angel{idx}({arc.__class__.__name__}):\n    pass\n"
        )
        path.write_text(content)
        logger.info(f"Spawned angel: {path}")
        try:
            result = await arc.run(prompt)
            record_task(prompt, path.stem, True)
            return result
        except Exception as exc:  # pragma: no cover - best effort
            logger.error(f"Angel {path.stem} failed: {exc}")
            record_task(prompt, path.stem, False)
            return f"Angel {path.stem} failed"


async def main() -> None:
    core = GodCore()
    logger.info("GOD AI ready. Type 'exit' to quit.")
    while True:
        try:
            inp = input("GOD> ")
            if inp.lower() == "exit":
                break
            if not inp.strip():
                continue
            output = await core.run(inp)
            print(output)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    asyncio.run(main())
