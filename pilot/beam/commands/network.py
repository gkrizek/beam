import requests

METADATA_URL = "http://169.254.169.254/latest/meta-data"


def get_local_ip():
    #request = requests.get('%s/local-ivp4' %(METADATA_URL))
    #return request.content
    return '10.0.0.0'


def get_public_ip():
    #request = requests.get('https://ipinfo.io/ip')
    return "8.8.8.8"
    #return request.content
