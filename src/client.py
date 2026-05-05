from openai import OpenAI
import config
import conversation



## Passing the api_key and base_url to the instance ##
client = OpenAI(
    api_key=config.api_key,
    base_url="https://openrouter.ai/api/v1"
)

## Sending the message ##
def send_message(message):
    conversation.add_message("user", message)
    response = client.chat.completions.create(
        model=config.current_model,
        messages=conversation.get_history()
    )
    text = response.choices[0].message.content
    print()
    conversation.add_message("assistant", text)
    return text

