import os

import requests

from app.logger import logger


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
