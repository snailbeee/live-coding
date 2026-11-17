# live-coding

Template project with a small local LLM, served by [llama-cpp-python](https://github.com/abetlen/llama-cpp-python).

## Requirements

- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Installation

### 1. Set up the environment

From a clone of this repo:

```sh
uv sync
```

This creates `.venv` and installs `my_pkg` in editable mode.

### 2. Download the model

The project uses [Qwen2.5-1.5B-Instruct-GGUF](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct-GGUF) (`q4_k_m` quantization), which is under the **Apache 2.0** license and allows commercial use.

```sh
uv run hf download Qwen/Qwen2.5-1.5B-Instruct-GGUF \
  qwen2.5-1.5b-instruct-q4_k_m.gguf \
  --local-dir ./models
```

The file ends up at `models/qwen2.5-1.5b-instruct-q4_k_m.gguf`.


## Usage

```sh
uv run python -m my_pkg
```

## Tests

```sh
uv run ruff check           # linter
uv run ruff format --check  # formatter
uv run pyrefly check        # type checker
uv run pytest               # unit tests
```

The LLM test is skipped if the model file hasn't been downloaded.
