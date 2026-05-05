import config
import conversation
import json
import sys
import requests
from rich.text import Text
from rich.markdown import Markdown
from rich.console import Console
console = Console(force_terminal=True)


def handle_command(input):
    f_input = input.lower().strip()
    s_input = f_input.split(" ")
    if s_input[0] == "/model":
        free_models = get_free_models()
        model_select = console.input("[blue]Select model[/blue]\n> ").strip()
        if model_select in free_models:
            config.set_model(model_select)
        elif model_select == "/none":
            return True
        else:
            console.print("[red]Model not found![/red]")
        return True

    elif s_input[0] == "/system":
        conversation.set_system_prompt(s_input[1])
        return True

    elif s_input[0] == "/save":
        try:
            with open("conversations.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append(conversation.get_history())

        with open ("conversations.json", "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return True

    elif s_input[0] == "/clear":
        conversation.clear_history()
        return True

    elif s_input[0] == "/clearjson":
        with open("conversations.json", "w") as f:
            json.dump([],f)
        return True

    elif s_input[0] == "/exit":
        console.print("[red]Thanks for using llm-terminal![/red]")
        sys.exit()

    else:
        return False


def  get_free_models():
    response = requests.get(
        "https://openrouter.ai/api/v1/models",
        headers={"Authorization": f"Bearer {config.api_key}"}
    )
    free_models = []
    data = response.json()
    for model in data["data"]:
        if model["pricing"]["prompt"] == "0":
            free_models.append(model["id"])
            console.print(f"[blue]{model['name']}\n-- ID: {model['id']}[/blue]\n-- [blue]{model['description']}[/blue]")

    return free_models







