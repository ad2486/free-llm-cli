# Free LLM CLI

A ready-to-go and modifiable terminal CLI to chat with free LLM models from [OpenRouter](https://openrouter.ai).

## Features

- 🔍 Automatically filters and lists free models from OpenRouter
- 💬 Multi-turn conversation with message history
- 🎨 Markdown rendering in the terminal
- 💾 Save conversations to a JSON file
- ⚙️ Configurable system prompt
- 🔄 Switch models during the conversation

## Requirements

- Python 3.10+
- An [OpenRouter](https://openrouter.ai) API key (free to create)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ad2486/free-llm-cli.git
cd free-llm-cli
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Create your `.env` file based on the example:
```bash
cp .env.example .env
```

4. Add your OpenRouter API key to `.env`:
```
OPENROUTER_API_KEY=your_api_key_here
DEFAULT_MODEL=google/gemma-3-27b-it:free
DEFAULT_SYSTEM_PROMPT=
```

5. Run the CLI:
```bash
python src/main.py
```

## Usage

Just type your message and press Enter to chat. You can also use the following commands:

| Command | Description |
|---|---|
| `/model` | List free models and switch to another one |
| `/system <prompt>` | Change the system prompt |
| `/save` | Save the current conversation to `conversations.json` |
| `/clear` | Clear the conversation history |
| `/clearjson` | Clear the `conversations.json` file |
| `/help` | Show available commands |
| `/exit` | Exit the CLI |


## About

Hi! I'm **Arthur Duarte**, a Brazilian high school student passionate about programming.

I'm currently learning HTML/CSS/JS for fullstack freelance work, and I've already built backend projects with Python and Flask. My goal is to study Computer Science in college and work as a developer.

This CLI was one of my first real-world Python projects, built to learn about API integration, project structure, and terminal applications.

- 🐙 GitHub: [@ad2486](https://github.com/ad2486)


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
