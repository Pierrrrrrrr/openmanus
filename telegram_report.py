import os

import requests


def send_telegram(message: str) -> None:
    """Send a text message via Telegram bot."""
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not (token and chat_id):
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, data=data, timeout=10)
    except Exception as e:  # pragma: no cover - best effort
        print(f"Telegram Error: {e}")
