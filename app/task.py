from datetime import datetime
from pathlib import Path

from app.logger import logger


LOG_PATH = Path("logs/task_log.txt")


def record_task(prompt: str, arc: str, success: bool) -> None:
    """Record the outcome of a task."""
    LOG_PATH.parent.mkdir(exist_ok=True)
    status = "SUCCESS" if success else "FAIL"
    line = f"{datetime.utcnow().isoformat()} | {arc} | {status} | {prompt}\n"
    with LOG_PATH.open("a") as f:
        f.write(line)
    logger.info(f"Task record: {arc} -> {status}")
