"""Simple logging utilities for G.O.D."""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Optional


@dataclass
class TelegramConfig:
    token: str
    chat_id: str


class Logger:
    """Minimal logger with optional Telegram reporting."""

    def __init__(self, telegram: Optional[TelegramConfig] = None) -> None:
        self.telegram = telegram
        logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

    def info(self, message: str) -> None:
        logging.info(message)
        self._send_telegram(message)

    def error(self, message: str) -> None:
        logging.error(message)
        self._send_telegram(message)

    def _send_telegram(self, message: str) -> None:
        if not self.telegram:
            return
        try:
            import requests

            url = f"https://api.telegram.org/bot{self.telegram.token}/sendMessage"
            data = {"chat_id": self.telegram.chat_id, "text": message}
            requests.post(url, data=data, timeout=10)
        except Exception as exc:  # pragma: no cover - network may fail
            logging.error("Telegram notification failed: %s", exc)
