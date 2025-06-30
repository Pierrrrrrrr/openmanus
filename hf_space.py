import asyncio

import gradio as gr

from god_core import GodCore


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
