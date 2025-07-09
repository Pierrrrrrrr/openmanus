"""Launches the G.O.D. core."""
from __future__ import annotations

import argparse

from .angels import Task
from .angels.angel_code import CodeAngel
from .angels.angel_scraper import ScraperAngel
from .angels.angel_text import TextAngel
from .god_core import GodCore
from .logger import Logger, TelegramConfig
from .task_storage import TaskStorage


def create_core(args: argparse.Namespace) -> GodCore:
    telegram = None
    if args.telegram_token and args.telegram_chat:
        telegram = TelegramConfig(args.telegram_token, args.telegram_chat)
    logger = Logger(telegram)
    storage = TaskStorage(args.task_file)
    core = GodCore(storage, logger)
    core.register_angel(TextAngel)
    core.register_angel(ScraperAngel)
    core.register_angel(CodeAngel)
    return core


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run G.O.D. engine")
    parser.add_argument(
        "--task-file", default="god_tasks.json", help="Path to task storage file"
    )
    parser.add_argument("--telegram-token", help="Telegram bot token")
    parser.add_argument("--telegram-chat", help="Telegram chat id")
    args = parser.parse_args(argv)

    core = create_core(args)

    # Example tasks - mapping description to angel name
    core.add_task(Task(description="text_angel", data="hello world"))
    core.add_task(Task(description="scraper_angel", data="https://example.com"))
    core.add_task(Task(description="code_angel", data="print('hi')"))

    core.run()


if __name__ == "__main__":  # pragma: no cover - manual execution
    main()
