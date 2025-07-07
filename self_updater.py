from __future__ import annotations

import hashlib
import shutil
from datetime import datetime
from pathlib import Path


class SelfUpdater:
    """Modify project files safely with backups and integrity checks."""

    @staticmethod
    def _checksum(path: Path) -> str:
        h = hashlib.sha256()
        with path.open("rb") as f:
            h.update(f.read())
        return h.hexdigest()

    @staticmethod
    def backup(path: Path) -> Path:
        backup_dir = Path("backups")
        backup_dir.mkdir(exist_ok=True)
        ts = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        dest = backup_dir / f"{path.name}.{ts}.bak"
        shutil.copy2(path, dest)
        return dest

    @classmethod
    def apply_patch(cls, file_path: str, new_content: str) -> bool:
        path = Path(file_path)
        if not path.exists():
            return False
        original = cls._checksum(path)
        cls.backup(path)
        path.write_text(new_content)
        return cls._checksum(path) != original
