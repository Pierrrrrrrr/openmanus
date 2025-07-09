# G.O.D. v0.1

This folder contains a minimal autonomous AI system named **G.O.D.** (Global Operating Development).
The architecture is intentionally simple and modular to provide a clean starting
point for further development.

Main components:

- `god_core.py` – the core engine that dispatches tasks to "angels".
- `god_launcher.py` – example launcher script that runs the engine.
- `angels/` – package with autonomous agents:
  - `angel_text.py` – basic text processing.
  - `angel_scraper.py` – basic web scraping.
- `angel_code.py` – code generation using HuggingFace models (e.g. Mixtral,
  DeepSeek, GPT4All, GPT-2).
- `task_storage.py` – utilities to persist tasks in JSON format.
- `logger.py` – simple logging facility with a placeholder for Telegram support.

The code is documented and intentionally lightweight so it can run in a local
Python environment or inside a Colab notebook. Future improvements may include
integration with vector databases, additional agent types, and real model
integration for smarter behaviors.

Tasks are persisted to a JSON file and processed sequentially. Angels can
return additional tasks which are queued for execution, allowing the system to
learn from and build upon previous results.
