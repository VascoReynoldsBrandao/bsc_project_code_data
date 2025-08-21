import os
from dotenv import load_dotenv

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
load_dotenv(dotenv_path=ENV_PATH)

def get_api_key():
    return os.getenv("API_KEY")
