import os
import dotenv

## Getting the variables from .env ##
dotenv.load_dotenv()
api_key = os.getenv('OPENROUTER_API_KEY')
default_model = os.getenv('DEFAULT_MODEL')
default_system_prompt = os.getenv('DEFAULT_SYSTEM_PROMPT')
current_model = default_model

def set_model(model):
    global current_model
    current_model = model
