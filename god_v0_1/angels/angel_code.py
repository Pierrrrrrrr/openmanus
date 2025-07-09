"""Angel for code generation."""
from __future__ import annotations

import os

from transformers import AutoModelForCausalLM, AutoTokenizer

from . import Angel, Task


class CodeAngel(Angel):
    """Angel that generates code using a language model."""

    name = "code_angel"

    def __init__(self, model_name: str | None = None) -> None:
        self.model_name = model_name or os.getenv("GOD_MODEL", "gpt2")
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        except Exception:  # pragma: no cover - model may not download
            self.tokenizer = None
            self.model = None

    def run(self, task: Task) -> tuple[str, list[Task]]:
        prompt = str(task.data or "")
        generated_code = f"# Code generated for: {prompt}\npass"
        if self.model and self.tokenizer:
            inputs = self.tokenizer(prompt, return_tensors="pt")
            outputs = self.model.generate(**inputs, max_new_tokens=128)
            generated_code = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_code, []
