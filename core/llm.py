"""
LiteLLM-backed chat client with an OpenAI-style call surface.

The agents in this repo are written against the OpenAI SDK's
`client.chat.completions.create(...)` shape. This thin wrapper keeps that exact
call surface but routes every request through LiteLLM, so any LiteLLM-supported
provider works just by setting `LLM_MODEL` to `<provider>/<model>` — e.g.
`groq/llama-3.3-70b-versatile`, `openai/gpt-4o-mini`,
`anthropic/claude-3-5-haiku-20241022`, or `ollama/llama3` for a local model.

The API key is read from `LLM_API_KEY`.
"""

from __future__ import annotations

import os
from typing import Any

import litellm


class _Completions:
    def create(self, model: str, messages: list[dict], **kwargs: Any) -> Any:
        return litellm.completion(
            model=model,
            messages=messages,
            api_key=os.getenv("LLM_API_KEY") or None,
            **kwargs,
        )


class _Chat:
    def __init__(self) -> None:
        self.completions = _Completions()


class LLMClient:
    """Provider-agnostic LLM client with an OpenAI-compatible call surface."""

    def __init__(self) -> None:
        self.chat = _Chat()
