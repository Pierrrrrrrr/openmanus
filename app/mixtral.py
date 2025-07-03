from functools import lru_cache

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


@lru_cache()
def _load(model_name: str = "mistralai/Mixtral-8x7B-Instruct-v0.1"):
    """Load Mixtral model and tokenizer."""
    tok = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
    )
    return pipeline("text-generation", model=model, tokenizer=tok)


def ask_mixtral(prompt: str, max_new_tokens: int = 256) -> str:
    """Generate a response from Mixtral."""
    pipe = _load()
    out = pipe(prompt, max_new_tokens=max_new_tokens)
    return out[0]["generated_text"]
