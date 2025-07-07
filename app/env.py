import os
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
