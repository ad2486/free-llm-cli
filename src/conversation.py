## Creating the chat history ##
history = []


## Adding message to the history ##
def add_message(role, content):
    global history
    history.append({"role": role, "content": content})


## Function to clear history ##
def clear_history():
    global history
    history.clear()


## Clears the history and adds the new system prompt ##
def set_system_prompt(prompt):
    global history
    history.clear()
    history.append({"role": "system", "content": prompt})


## Returns the history ##
def get_history():
    global history
    return history


