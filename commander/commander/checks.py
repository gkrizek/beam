import requests


def CheckHealth(host):

    try:
        request = requests.get('http://%s' % (host), timeout=5)
    except requests.exceptions.ConnectTimeout as e:
        request = {
            'status': 'offline',
            'message': e
        }
    return request
