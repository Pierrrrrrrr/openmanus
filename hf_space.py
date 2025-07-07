import asyncio

import gradio as gr

from app.env import load_env
from god_core import GodCore


load_env(prompt_missing=True)
core = GodCore()


async def _process(prompt: str) -> str:
    return await core.run(prompt)


def process(prompt: str) -> str:
    return asyncio.run(_process(prompt))


with gr.Blocks() as demo:
    gr.Markdown("# GOD AI")
    with gr.Row():
        inp = gr.Textbox(label="Prompt", lines=4)
    out = gr.Textbox(label="Response", lines=10)
    btn = gr.Button("Run")
    btn.click(process, inp, out)

if __name__ == "__main__":
    demo.launch()
