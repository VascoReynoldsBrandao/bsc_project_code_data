import os
import json
from dotenv import load_dotenv

ENV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".." , "data"))
REF_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "references"))
load_dotenv(dotenv_path=ENV_PATH)

def get_api_key():
    return os.getenv("API_KEY")

def get_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    return DATA_DIR

def get_host_cols():
    with open(os.path.join(REF_DIR, "host_columns.json")) as f:
        data = json.load(f)
        return list(data.keys())

def get_service_cols():
    with open(os.path.join(REF_DIR, "service_columns.json")) as f:
        data = json.load(f)
        return list(data.keys())