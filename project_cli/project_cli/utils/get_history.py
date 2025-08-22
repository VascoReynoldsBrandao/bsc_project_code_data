import time
from datetime import datetime
import requests
import json
import os
from project_cli.config.settings import  get_api_key, get_data_dir
from project_cli.utils.key_validator import is_valid_modat_api_key

def get_history(since, ip, port, transport, save_json=False):
    API_KEY = get_api_key()
    if not is_valid_modat_api_key(API_KEY):
        raise RuntimeError("Invalid API key or not set")
    url = "https://api.magnify.modat.io/service/history/v1"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json", 
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "since": since,
        "ip": ip,
        "port": port,
        "transport": transport
    }
    time.sleep(1)  # Adding a delay to avoid hitting rate limits
    response = requests.post(url, headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        raise RuntimeError(f"Error: {query}\n{response.text}\ndata: {data}")
    try:
        response_json = response.json()
        if save_json:
            now = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
            file_path = os.path.join(get_data_dir(), f"history_{now}.json")
            with open(file_path, "w") as f:
                json.dump(response_json, f, indent=4)
    except json.JSONDecodeError as e:
        raise RuntimeError("Error decoding JSON response.") from e
    return response_json