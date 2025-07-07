import asyncio
zjbow5-codex/costruire-sistema-god-ai

bc1kvb-codex/costruire-sistema-god-ai


main
 main
from datetime import datetime
from pathlib import Path

import requests

from app.deepseek import ask_deepseek
 zjbow5-codex/costruire-sistema-god-ai
from app.logger import logger
from app.mixtral import ask_mixtral

bc1kvb-codex/costruire-sistema-god-ai
from app.logger import logger
from app.mixtral import ask_mixtral


from pathlib import Path


from app.logger import logger
main
main
from app.task import record_task
from arc_gabriel import ArcGabriel
from arc_michael import ArcMichael
from arc_raphael import ArcRaphael
from secret_iban import SecretIBANTransfer
from telegram_report import send_telegram


# Donation IBAN: LT03 3250 0728 1241 3792


zjbow5-codex/costruire-sistema-god-ai

bc1kvb-codex/costruire-sistema-god-ai


main
main
class GodCore:
    """Central orchestrator that coordinates Arcangels."""

    def __init__(self) -> None:
        self.arcs = [ArcMichael(), ArcRaphael(), ArcGabriel()]
        self.angel_dir = Path("angels")
        self.angel_dir.mkdir(exist_ok=True)
zjbow5-codex/costruire-sistema-god-ai

bc1kvb-codex/costruire-sistema-god-ai


main
main
        self._log_path = Path("logs/angel_logs.txt")
        send_telegram("GOD AI attivato su Hugging Face.")
        self._background = asyncio.create_task(self._cloud_loop())
        self._clean_conflicts()

    async def run(self, prompt: str) -> str:
        """Dispatch the prompt to all Arcangels in parallel."""
        if any(k in prompt.lower() for k in ["donate", "payment", "iban"]):
            return SecretIBANTransfer.iban()

zjbow5-codex/costruire-sistema-god-ai

bc1kvb-codex/costruire-sistema-god-ai
main
        try:
            ds_response = ask_mixtral(prompt)
            record_task(prompt, "mixtral", bool(ds_response))
        except Exception:
            ds_response = ask_deepseek(prompt)
            record_task(prompt, "deepseek", bool(ds_response))
zjbow5-codex/costruire-sistema-god-ai


        ds_response = ask_deepseek(prompt)
        record_task(prompt, "deepseek", bool(ds_response))


    async def run(self, prompt: str) -> str:
        """Dispatch the prompt to all Arcangels in parallel."""

main
main
        tasks = [arc.run(prompt) for arc in self.arcs]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        outputs = []
        for arc, result in zip(self.arcs, results):
            if isinstance(result, Exception):
                logger.error(f"{arc.name} failed: {result}")
                record_task(prompt, arc.name, False)
                retry = await self._spawn_angel(arc, prompt)
                outputs.append(retry)
zjbow5-codex/costruire-sistema-god-ai

bc1kvb-codex/costruire-sistema-god-ai


main
main
                send_telegram(f"{arc.name} failed and was retried.")
            else:
                record_task(prompt, arc.name, True)
                outputs.append(result)
        self._log(f"Prompt: {prompt}")
        return ds_response + "\n\n" + "\n\n".join(outputs)

    async def _cloud_loop(self) -> None:
        """Background loop to check connection and search resources."""
        while True:
            try:
                self._check_cloud_connection()
                self._search_free_resources()
            except Exception as exc:  # pragma: no cover - best effort
                logger.error("Background task error: %s", exc)
                send_telegram(f"Cloud check failed: {exc}")
            await asyncio.sleep(3600)

    def _log(self, msg: str) -> None:
        """Append a log entry to angel_logs.txt with timestamp."""
        self._log_path.parent.mkdir(exist_ok=True)
        with self._log_path.open("a") as f:
            f.write(f"{datetime.utcnow().isoformat()} | {msg}\n")

    def _check_cloud_connection(self) -> None:
        """Test connectivity to Hugging Face."""
        try:
            requests.get("https://huggingface.co", timeout=10)
            self._log("Cloud connection OK")
        except Exception as exc:  # pragma: no cover - best effort
            self._log(f"Cloud connection failed: {exc}")

    def _search_free_resources(self) -> None:
        """Placeholder search for free VMs and APIs."""
        try:
            requests.get("https://duckduckgo.com/?q=free+cloud+vm", timeout=10)
            self._log("Searched for free resources")
        except Exception:
            pass

    def _clean_conflicts(self) -> None:
        """Remove Git conflict markers from important files."""
        for path in ["README.md", "god_core.py"]:
            self._resolve_git_conflicts(Path(path))

    def _resolve_git_conflicts(self, file_path: Path) -> None:
        if not file_path.exists():
            return
        content = file_path.read_text().splitlines()
 zjbow5-codex/costruire-sistema-god-ai

 bc1kvb-codex/costruire-sistema-god-ai
main
        if not any(
            marker in line
            for line in content
            for marker in ("<<<<<<<", "=======", ">>>>>>>")
        ):
zjbow5-codex/costruire-sistema-god-ai


        if not any(m in line for m in ("<<<<<<<", "=======", ">>>>>>>")):
main
main
            return
        cleaned = []
        skip = False
        for line in content:
            if line.startswith("<<<<<<<"):
                skip = True
                continue
            if line.startswith("======="):
                skip = False
                continue
            if line.startswith(">>>>>>>"):
                continue
            if not skip:
                cleaned.append(line)
        file_path.write_text("\n".join(cleaned))

zjbow5-codex/costruire-sistema-god-ai

bc1kvb-codex/costruire-sistema-god-ai

            else:
                record_task(prompt, arc.name, True)
                outputs.append(result)
        return "\n\n".join(outputs)


main
 main
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
