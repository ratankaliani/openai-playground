# Overview

## Setup

Install python3.

Install uv. (Fast python package installer)

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Create a virtual environment for installing the packages required for this project.

```
uv venv # Create a virtual environment at .venv.

source .venv/bin/activate
```

Install dotenv and openai

```
uv pip install python-dotenv
uv pip install openai
```

## Generate OpenAI key

TODO: Link to docs

Place OpenAI key in `.env`

```
OPENAI_API_KEY=sk-<your-key>
```
