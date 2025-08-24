import requests
import time

def get_location(ip):
    """
    Get location information for a given IP address. 
    (This is a Legacy Free Non-Authenticated API with a rate limit of 50,000 requests per month)
    """
    url = f'https://ipinfo.io/{ip}/json'
    
    response = requests.get(url)

    count = 0
    while response.status_code != 200 and count < 3:
        time.sleep(1)
        response = requests.get(url)
        count += 1

    if response.status_code == 200:
        info = response.json()
        loc = info['loc'].split(',')
        hostname = info['hostname']
        country = info['country']
        city = info['city']
        region = info['region']
        return {
            "latitude": float(loc[0]), 
            "longitude": float(loc[1]), 
            "hostname": hostname, 
            "country": country, 
            "city": city, 
            "region": region
        }
    else:
        raise RuntimeError(f"Error fetching location for IP {ip}: {response.status_code} - {response.text}")