from __future__ import annotations

import asyncio
from typing import Dict, List, Optional, Union

from app.deepseek import ask_deepseek
from app.schema import Message


class LLM:
    """Minimal LLM wrapper that delegates to DeepSeek."""

    _instances: Dict[str, "LLM"] = {}

    def __new__(
        cls, config_name: str = "default", llm_config: Optional[dict] = None
    ) -> "LLM":
        if config_name not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[config_name] = instance
        return cls._instances[config_name]

    def __init__(
        self, config_name: str = "default", llm_config: Optional[dict] = None
    ) -> None:
        pass

    async def ask(
        self,
        messages: List[Union[dict, Message]],
        system_msgs: Optional[List[Union[dict, Message]]] = None,
        stream: bool = False,
        temperature: Optional[float] = None,
    ) -> str:
        prompt_parts = []
        if system_msgs:
            prompt_parts.extend(
                m["content"] if isinstance(m, dict) else m.content for m in system_msgs
            )
        prompt_parts.extend(
            m["content"] if isinstance(m, dict) else m.content for m in messages
        )
        prompt = "\n".join(prompt_parts)
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, ask_deepseek, prompt)

    async def ask_tool(
        self,
        messages: List[Union[dict, Message]],
        system_msgs: Optional[List[Union[dict, Message]]] = None,
        **kwargs,
    ) -> Message:
        response = await self.ask(messages, system_msgs, stream=False)
        return Message(role="assistant", content=response)
