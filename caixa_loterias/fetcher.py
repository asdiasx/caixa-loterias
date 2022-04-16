import requests


def fetch(url: str) -> bytes:
    """
    Fetch data from URL
    """
    response = requests.get(url)
    return response.content
