import json
from collections.abc import Iterator

from llama_cpp import Llama


class LlamaLLM:
    SYSTEM = 'You are a helper. Answer only in JSON: {"key": true} or {"key": false}.'

    def __init__(self, model_path: str):
        self.llm = Llama(
            model_path=model_path, n_ctx=2048, n_gpu_layers=0, verbose=False
        )

    def chat_reponse(self, text: str) -> bool | None:
        prompt = f'Given sentence: "{text}"\nDecide whether the sentence is correct.'
        out = self.llm.create_chat_completion(
            messages=[
                {"role": "system", "content": self.SYSTEM},
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
            max_tokens=20,
            response_format={"type": "json_object"},
        )
        if isinstance(out, Iterator):  # only happens with stream=True
            raise TypeError("unexpected streaming response")
        content = out["choices"][0]["message"]["content"]
        if content is None:
            return None
        try:
            value = json.loads(content).get("key")
        except json.JSONDecodeError, AttributeError:
            return None
        return value if isinstance(value, bool) else None

    def close(self) -> None:
        self.llm.close()
