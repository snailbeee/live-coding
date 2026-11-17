import sys

from my_pkg.constants import MODEL_PATH
from my_pkg.llm import LlamaLLM


def main():
    llm = LlamaLLM(str(MODEL_PATH))
    try:
        out = llm.chat_reponse("The sun rises in West.")
    finally:
        llm.close()
    print(out)
    return 0


sys.exit(main())
