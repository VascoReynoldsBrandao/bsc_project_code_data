import requests

def is_valid_modat_api_key(api_key: str) -> bool:
    """
    Validates the MODAT Magnify API key by making a test request.
    Returns True if the key is valid, False otherwise.
    """
    if not api_key:
        return False

    url = "https://api.magnify.modat.io/service/search/v1"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Dummy payload to avoid triggering real search logic
    data = {
        "query": "port=1",
        "page": 1,
        "page_size": 10
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False
