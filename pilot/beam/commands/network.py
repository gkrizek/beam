import requests
from utils import get_metadata

METADATA_URL = "http://169.254.169.254/latest/meta-data"

def get_local_ip():
    request = requests.get('%s/local-ivp4')
    return request.content


def get_public_ip():
    request = requests.get('https://ipinfo.io/ip')
    return request.content
