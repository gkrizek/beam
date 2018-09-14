from hashlib import sha256


def get_moniker(ip,type):
    if type == 'sentry':
        sha = sha256(ip.encode('utf-8')).hexdigest()
        return sha[:10]
    elif type == 'validator':
        # TODO need to handle validator moniker
        return 'validator'
