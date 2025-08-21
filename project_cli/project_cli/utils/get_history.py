import time
import requests
import json
from project_cli.project_cli.config.settings import  get_api_key

def get_service_history(since, ip, port, transport, save_json=False, path=None):
    API_KEY = get_api_key()
    if not API_KEY:
        raise RuntimeError("MODAT_MAGNIFY_API_KEY is not set in the environment variables.")
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
    except json.JSONDecodeError as e:
        raise RuntimeError("Error decoding JSON response.") from e
    return response_json