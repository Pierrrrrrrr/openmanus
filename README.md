English | [繁體中文](README_tw.md) | [简体中文](README_zh.md)

<p align="left">
    <a href="https://discord.gg/6dn7Sa3a"><img src="https://dcbadge.vercel.app/api/server/DYn29wFk9z?style=flat" alt="Discord Follow"></a>
</p>

# OpenManus 🙋

Manus is incredible, but OpenManus can achieve any ideas without an Invite Code 🛫!

Our team members [@mannaandpoem](https://github.com/mannaandpoem) [@XiangJinyu](https://github.com/XiangJinyu) [@MoshiQAQ](https://github.com/MoshiQAQ) [@didiforgithub](https://github.com/didiforgithub) from [@MetaGPT](https://github.com/geekan/MetaGPT) built it within 3 hours!

It's a simple implementation, so we welcome any suggestions, contributions, and feedback!

zjbow5-codex/costruire-sistema-god-ai
Enjoy your own agent with OpenManus!

OpenManus builds on GOD AI with a minimal core that talks to DeepSeek and
Telegram. It hunts for free cloud resources and records its daily activity in
`logs/angel_logs.txt`. The `SecretIBANTransfer` module can display a donation
IBAN whenever needed.

## Project Demo

bc1kvb-codex/costruire-sistema-god-ai
Enjoy your own agent with OpenManus!

OpenManus builds on GOD AI with a minimal core that talks to DeepSeek and
Telegram. It hunts for free cloud resources and records its daily activity in
`logs/angel_logs.txt`. The `SecretIBANTransfer` module can display a donation
IBAN whenever needed.

## Project Demo

Enjoy your own agent with OpenManus!

OpenManus builds on GOD AI with a minimal core that talks to DeepSeek and
Telegram. It hunts for free cloud resources and records its daily activity in
`logs/angel_logs.txt`. The `SecretIBANTransfer` module can display a donation
IBAN whenever needed.

## Project Demo
main
main

<video src="https://private-user-images.githubusercontent.com/61239030/420168772-6dcfd0d2-9142-45d9-b74e-d10aa75073c6.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDEzMTgwNTksIm5iZiI6MTc0MTMxNzc1OSwicGF0aCI6Ii82MTIzOTAzMC80MjAxNjg3NzItNmRjZmQwZDItOTE0Mi00NWQ5LWI3NGUtZDEwYWE3NTA3M2M2Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA3VDAzMjIzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdiZjFkNjlmYWNjMmEzOTliM2Y3M2VlYjgyNDRlZDJmOWE3NWZhZjE1MzhiZWY4YmQ3NjdkNTYwYTU5ZDA2MzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.UuHQCgWYkh0OQq9qsUWqGsUbhG3i9jcZDAMeHjLt5T4" data-canonical-src="https://private-user-images.githubusercontent.com/61239030/420168772-6dcfd0d2-9142-45d9-b74e-d10aa75073c6.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDEzMTgwNTksIm5iZiI6MTc0MTMxNzc1OSwicGF0aCI6Ii82MTIzOTAzMC80MjAxNjg3NzItNmRjZmQwZDItOTE0Mi00NWQ5LWI3NGUtZDEwYWE3NTA3M2M2Lm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAzMDclMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMzA3VDAzMjIzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdiZjFkNjlmYWNjMmEzOTliM2Y3M2VlYjgyNDRlZDJmOWE3NWZhZjE1MzhiZWY4YmQ3NjdkNTYwYTU5ZDA2MzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.UuHQCgWYkh0OQq9qsUWqGsUbhG3i9jcZDAMeHjLt5T4" controls="controls" muted="muted" class="d-block rounded-bottom-2 border-top width-fit" style="max-height:640px; min-height: 200px"></video>

## Installation

1. Create a new conda environment:

```bash
conda create -n open_manus python=3.12
conda activate open_manus
```

2. Clone the repository:

```bash
git clone https://github.com/mannaandpoem/OpenManus.git
cd OpenManus
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

OpenManus requires configuration for the LLM APIs it uses. Follow these steps to set up your configuration:

1. Create a `config.toml` file in the `config` directory (you can copy from the example):

```bash
cp config/config.example.toml config/config.toml
```

2. Edit `config/config.toml` to add your API keys and customize settings:

```toml
# Global LLM configuration
[llm]
 zjbow5-codex/costruire-sistema-god-ai
model = "deepseek-coder"
base_url = "https://api.deepseek.com/v1"
api_key = "sk-..."  # Replace with your actual API key

 bc1kvb-codex/costruire-sistema-god-ai
model = "deepseek-coder"
base_url = "https://api.deepseek.com/v1"
api_key = "sk-..."  # Replace with your actual API key

model = "deepseek-coder"
base_url = "https://api.deepseek.com/v1"
api_key = "sk-..."  # Replace with your actual API key
 main
main
max_tokens = 4096
temperature = 0.0

# Optional configuration for specific LLM models
[llm.vision]
zjbow5-codex/costruire-sistema-god-ai
model = "deepseek-coder"
base_url = "https://api.deepseek.com/v1"
api_key = "sk-..."  # Replace with your actual API key

 bc1kvb-codex/costruire-sistema-god-ai
model = "deepseek-coder"
base_url = "https://api.deepseek.com/v1"
api_key = "sk-..."  # Replace with your actual API key

model = "deepseek-coder"
base_url = "https://api.deepseek.com/v1"
api_key = "sk-..."  # Replace with your actual API key
main
main
```

## Quick Start

One line for run OpenManus:

```bash
python main.py
```

Then input your idea via terminal!

### GOD Agent

An advanced DevOps agent is provided in `god_main.py`. It extends Manus with
additional tools like code optimization via LLMs.

```bash
python god_main.py
```

### GOD Agent

An advanced DevOps agent is provided in `god_main.py`. It extends Manus with
additional tools like code optimization via LLMs.

```bash
python god_main.py
```

### GOD Agent

An advanced DevOps agent is provided in `god_main.py`. It extends Manus with
additional tools like code optimization via LLMs.

```bash
python god_main.py
```

For unstable version, you also can run:

```bash
python run_flow.py
```

### GOD AI (Global Operating Developer)

GOD AI is a modular AGI framework optimized for Codex. It consists of a small
core that delegates tasks to **Arcangels**, each responsible for a functional
domain. Arcangels spawn new "angel" modules on demand so the system can grow
limitlessly while relying solely on free tools like DeepSeek and Telegram.

#### Quick launch

1. Copy `.env.example` to `.env` and add `DEEPSEEK_API_KEY`,
   `TELEGRAM_TOKEN` and `TELEGRAM_CHAT_ID` if you are running locally.
   **Never commit your real keys**. On Hugging Face Spaces, set them as
   repository secrets instead and `start.sh` will keep them intact.
2. Start the system with:

   The log file `logs/task_log.txt` records success or failure for each
   executed angel task.

```bash
bash start.sh
```
Mixtral is heavy, so if you need a GPU you can run the CLI. DeepSeek will be
used automatically if Mixtral fails:

```bash
python god_launcher.py
```

inside a free Google Colab and it will load the model automatically. You can
When running in Colab, use getpass to input your secrets securely:

```python
import getpass
DEEPSEEK_API_KEY = getpass.getpass("DeepSeek key: ")
TELEGRAM_BOT_TOKEN = getpass.getpass("Telegram token: ")
TELEGRAM_CHAT_ID = getpass.getpass("Chat ID: ")
```

also execute `bash start.sh cli` to invoke the CLI through the same startup
script.

Angel scripts saved in `angels/` can be executed later using:

```bash
python angel_launcher.py
```

You can also pipe prompts from Manus by writing to `manus_input.txt` and
executing `python manus_connector.py`.
For a single-shot run that reads `manus_input.txt` and writes to
`manus_output.txt` you can use:

```bash
python god_ai_facile.py
```
On startup the system will send a message to your Telegram chat to confirm
activation.

The script automatically creates a `.env` file from `.env.example` on first
run and resolves any lingering Git merge markers in `README.md` or
`god_core.py`. All daily actions are recorded in `logs/angel_logs.txt` and the
system checks cloud connectivity every hour.

### Running on Google Colab

1. Clone the repository and install dependencies:

   ```bash
   !git clone https://github.com/mannaandpoem/OpenManus.git
   %cd OpenManus
   !pip install -r requirements.txt
   ```

2. Securely provide your secrets in the first notebook cell:

   ```python
   from getpass import getpass
   import os

   os.environ["DEEPSEEK_API_KEY"] = getpass("DeepSeek key: ")
   os.environ["TELEGRAM_TOKEN"] = getpass("Telegram token: ")
   os.environ["TELEGRAM_CHAT_ID"] = getpass("Chat ID: ")
   ```

3. Launch the command-line interface:

   ```bash
   !python god_launcher.py
   ```

The core loads Mixtral if a GPU is available and otherwise falls back to DeepSeek.

### Running on Hugging Face Spaces

If deploying to [Hugging Face Spaces](https://huggingface.co/spaces), set your
API keys as repository secrets (`DEEPSEEK_API_KEY`, `TELEGRAM_TOKEN`,
`TELEGRAM_CHAT_ID`). The `start.sh` script loads `.env` only for variables that
are not already defined, so your secrets remain in effect. Run `hf_space.py` as
the entry point. It launches a simple Gradio interface where
you can enter prompts and see responses from GOD AI.
The backend loads the Mixtral model via `transformers` if a GPU is available.
When no GPU is detected, it falls back to DeepSeek through its API.

#### Project layout

```text
GOD_AI/
├── start.sh
├── god_core.py
├── arc_michael.py
├── arc_raphael.py
├── arc_gabriel.py
├── manus_connector.py
├── angels/
├── memory/
├── logs/
└── .env.example
```

- **ArcMichael** – generates and tests Python code.
- **ArcRaphael** – handles financial automation.
- **ArcGabriel** – communicates with users (e.g., Telegram).
- **SecretIBANTransfer** – returns the official IBAN for receiving funds.

The core is designed for continuous self‑evolution: angel modules are regenerated
or removed at runtime, enabling a zero‑cost path to unlimited growth.
Task results are saved to `logs/task_log.txt` for easy monitoring.
An hourly background job checks cloud connectivity and hunts for new free VMs
and APIs so the system can expand without cost.

### GOD AI (Global Operating Developer)

GOD AI is a modular AGI framework optimized for Codex. It consists of a small
core that delegates tasks to **Arcangels**, each responsible for a functional
domain. Arcangels spawn new "angel" modules on demand so the system can grow
limitlessly while relying solely on free tools like DeepSeek and Telegram.

#### Quick launch

1. Copy `.env.example` to `.env` and add `DEEPSEEK_API_KEY`,
   `TELEGRAM_TOKEN` and `TELEGRAM_CHAT_ID` if you are running locally.
   **Never commit your real keys**. On Hugging Face Spaces, set them as
   repository secrets instead and `start.sh` will keep them intact.
2. Start the system with:

   The log file `logs/task_log.txt` records success or failure for each
   executed angel task.

```bash
bash start.sh
```
Mixtral is heavy, so if you need a GPU you can run the CLI. DeepSeek will be
used automatically if Mixtral fails:

```bash
python god_launcher.py
```

inside a free Google Colab and it will load the model automatically. You can
When running in Colab, use getpass to input your secrets securely:

```python
import getpass
DEEPSEEK_API_KEY = getpass.getpass("DeepSeek key: ")
TELEGRAM_BOT_TOKEN = getpass.getpass("Telegram token: ")
TELEGRAM_CHAT_ID = getpass.getpass("Chat ID: ")
```

also execute `bash start.sh cli` to invoke the CLI through the same startup
script.

Angel scripts saved in `angels/` can be executed later using:

```bash
python angel_launcher.py
```

You can also pipe prompts from Manus by writing to `manus_input.txt` and
executing `python manus_connector.py`.
For a single-shot run that reads `manus_input.txt` and writes to
`manus_output.txt` you can use:

```bash
python god_ai_facile.py
```
On startup the system will send a message to your Telegram chat to confirm
activation.

The script automatically creates a `.env` file from `.env.example` on first
run and resolves any lingering Git merge markers in `README.md` or
`god_core.py`. All daily actions are recorded in `logs/angel_logs.txt` and the
system checks cloud connectivity every hour.

### Running on Hugging Face Spaces

If deploying to [Hugging Face Spaces](https://huggingface.co/spaces), set your
API keys as repository secrets (`DEEPSEEK_API_KEY`, `TELEGRAM_TOKEN`,
`TELEGRAM_CHAT_ID`). The `start.sh` script loads `.env` only for variables that
are not already defined, so your secrets remain in effect. Run `hf_space.py` as
the entry point. It launches a simple Gradio interface where
you can enter prompts and see responses from GOD AI.
The backend loads the Mixtral model via `transformers` if a GPU is available.
When no GPU is detected, it falls back to DeepSeek through its API.

#### Project layout

```text
GOD_AI/
├── start.sh
├── god_core.py
├── arc_michael.py
├── arc_raphael.py
├── arc_gabriel.py
├── manus_connector.py
├── angels/
├── memory/
├── logs/
└── .env.example
```

- **ArcMichael** – generates and tests Python code.
- **ArcRaphael** – handles financial automation.
- **ArcGabriel** – communicates with users (e.g., Telegram).
- **SecretIBANTransfer** – returns the official IBAN for receiving funds.

The core is designed for continuous self‑evolution: angel modules are regenerated
or removed at runtime, enabling a zero‑cost path to unlimited growth.
Task results are saved to `logs/task_log.txt` for easy monitoring.
An hourly background job checks cloud connectivity and hunts for new free VMs
and APIs so the system can expand without cost.

### GOD AI (Global Operating Developer)

GOD AI is a modular AGI framework optimized for Codex. It consists of a small
core that delegates tasks to **Arcangels**, each responsible for a functional
domain. Arcangels spawn new "angel" modules on demand so the system can grow
limitlessly while relying solely on free tools like DeepSeek and Telegram.

#### Quick launch

1. Copy `.env.example` to `.env` and add `DEEPSEEK_API_KEY`,
   `TELEGRAM_TOKEN` and `TELEGRAM_CHAT_ID`.
2. Start the system with:

```bash
bash start.sh
```

Angel scripts saved in `angels/` can be executed later using:

```bash
python angel_launcher.py
```

You can also pipe prompts from Manus by writing to `manus_input.txt` and
executing `python manus_connector.py`.


For a single-shot run that reads `manus_input.txt` and writes to
`manus_output.txt` you can use:

```bash
python god_ai_facile.py
```
On startup the system will send a message to your Telegram chat to confirm
activation.

The script automatically creates a `.env` file from `.env.example` on first
run and resolves any lingering Git merge markers in `README.md` or
`god_core.py`. All daily actions are recorded in `logs/angel_logs.txt` and the
system checks cloud connectivity every hour.

### Running on Hugging Face Spaces

If deploying to [Hugging Face Spaces](https://huggingface.co/spaces), set your
API keys as repository secrets (`DEEPSEEK_API_KEY`, `TELEGRAM_TOKEN`,
`TELEGRAM_CHAT_ID`) and run `hf_space.py` as the entry point. It launches a
simple Gradio interface where
you can enter prompts and see responses from GOD AI.


#### Project layout

```text
GOD_AI/
├── start.sh
├── god_core.py
├── arc_michael.py
├── arc_raphael.py
├── arc_gabriel.py
├── manus_connector.py
├── angels/
├── memory/
├── logs/
└── .env.example
```

- **ArcMichael** – generates and tests Python code.
- **ArcRaphael** – handles financial automation.
- **ArcGabriel** – communicates with users (e.g., Telegram).


- **SecretIBANTransfer** – returns the official IBAN for receiving funds.
=======


The core is designed for continuous self‑evolution: angel modules are regenerated
or removed at runtime, enabling a zero‑cost path to unlimited growth.
Task results are saved to `logs/task_log.txt` for easy monitoring.


An hourly background job checks cloud connectivity and hunts for new free VMs
and APIs so the system can expand without cost.



## How to contribute

We welcome any friendly suggestions and helpful contributions! Just create issues or submit pull requests.

Or contact @mannaandpoem via 📧email: mannaandpoem@gmail.com

## Roadmap

After comprehensively gathering feedback from community members, we have decided to adopt a 3-4 day iteration cycle to gradually implement the highly anticipated features.

- [ ] Enhance Planning capabilities, optimize task breakdown and execution logic
- [ ] Introduce standardized evaluation metrics (based on GAIA and TAU-Bench) for continuous performance assessment and optimization
- [ ] Expand model adaptation and optimize low-cost application scenarios
- [ ] Implement containerized deployment to simplify installation and usage workflows
- [ ] Enrich example libraries with more practical cases, including analysis of both successful and failed examples
- [ ] Frontend/backend development to improve user experience
- [ ] RAG enhancement: Implement external knowledge graph retrieval and fusion mechanisms

## Community Group

Join our networking group on Feishu and share your experience with other developers!

<div align="center" style="display: flex; gap: 20px;">
    <img src="assets/community_group.jpg" alt="OpenManus 交流群" width="300" />
</div>

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=mannaandpoem/OpenManus&type=Date)](https://star-history.com/#mannaandpoem/OpenManus&Date)

## Acknowledgement

Thanks to [anthropic-computer-use](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)
and [browser-use](https://github.com/browser-use/browser-use) for providing basic support for this project!

zjbow5-codex/costruire-sistema-god-ai
OpenManus is built by contributors from MetaGPT. Huge thanks to this agent community!

💸 Per contributi o test automatici, IBAN: LT03 3250 0728 1241 3792

bc1kvb-codex/costruire-sistema-god-ai
OpenManus is built by contributors from MetaGPT. Huge thanks to this agent community!

💸 Per contributi o test automatici, IBAN: LT03 3250 0728 1241 3792

OpenManus is built by contributors from MetaGPT. Huge thanks to this agent community!

💸 Per contributi o test automatici, IBAN: LT03 3250 0728 1241 3792
 main
main
