from pathlib import Path

import pytest

from my_pkg.constants import MODEL_PATH
from my_pkg.llm import LlamaLLM


@pytest.mark.skipif(not Path(MODEL_PATH).exists(), reason="GGUF model not doawnloaded.")
def test_llm_detects_obvious_question():
    llm = LlamaLLM(str(MODEL_PATH))

    try:
        assert llm.chat_reponse("The sun rises in the West.") is False
    finally:
        llm.close()
