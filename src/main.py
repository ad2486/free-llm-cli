import client
import utils
import config
import conversation
from rich.text import Text
from rich.markdown import Markdown
from rich.console import Console
console = Console(force_terminal=True)

while True:
    try:
        user_input = console.input(f"[blue]\\[{config.current_model}][/blue][bold green] >[/bold green] ")
        if utils.handle_command(user_input):
            pass
        else:
            text = client.send_message(user_input)
            if text:
                console.print(Markdown(text))
            else:
                console.print(Text("[red]No response from the model.[/red]"))
    except KeyboardInterrupt:
        console.print("[red]Cancelled by user[/red]")

