import subprocess
from pathlib import Path


def main() -> None:
    for script in Path("angels").glob("*.py"):
        subprocess.run(["python", str(script)], check=False)


if __name__ == "__main__":
    main()
