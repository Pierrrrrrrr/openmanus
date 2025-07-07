import os
zjbow5-codex/costruire-sistema-god-ai
from getpass import getpass
from pathlib import Path


def load_env(path: str = ".env", prompt_missing: bool = False) -> None:
    """Load environment variables from a .env file and optionally prompt for missing keys."""
    env_file = Path(path)
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key, value)

    if prompt_missing:
        for key in ("DEEPSEEK_API_KEY", "TELEGRAM_TOKEN", "TELEGRAM_CHAT_ID"):
            if not os.getenv(key):
                try:
                    os.environ[key] = getpass(f"{key}: ")
                except Exception:
                    pass

from pathlib import Path


def load_env(path: str = ".env") -> None:
    """Load environment variables from a .env file if not already set."""
    env_file = Path(path)
    if not env_file.exists():
        return
    for line in env_file.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key, value)
 main
