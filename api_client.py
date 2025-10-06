import requests

def post_data_to_api(api_url, data, headers=None):
    response = requests.post(api_url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()