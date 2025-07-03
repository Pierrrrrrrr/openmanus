from functools import lru_cache

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


@lru_cache()
def _load(model_name: str = "mistralai/Mixtral-8x7B-Instruct-v0.1"):
    """Load Mixtral model and tokenizer with CPU/GPU detection."""
    use_gpu = torch.cuda.is_available()
    torch_dtype = torch.float16 if use_gpu else torch.float32
    device_map = "auto" if use_gpu else None

    tok = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch_dtype,
        device_map=device_map,
        trust_remote_code=True,
    )
    model.eval()
    return tok, model


def ask_mixtral(prompt: str, max_new_tokens: int = 256) -> str:
    """Generate a response from Mixtral."""
    tok, model = _load()
    device = model.device
    inputs = tok(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(
            input_ids=inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_new_tokens=max_new_tokens,
        )
    return tok.decode(outputs[0], skip_special_tokens=True)
