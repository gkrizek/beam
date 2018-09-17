from .auth import CheckAuth


def Switch(action, headers, body):

    """Authorization"""
    # If headers are sent, check Authorization
    # If there are no headers we know it was a manual invocation of Lambda.
    if headers:
        access = CheckAuth(headers, body)
        if access != 'granted':
            return {
                'statusCode': 401,
                'body': 'Access Denied'
            }

    """Execute Function""""

    if action == 'start_healthcheck':
        return 'start_healthcheck'
    elif action == 'config_file':
        return 'config_file'
    elif action == 'list':
        return 'list'
    elif action == 'report':
        return 'report'
    else:
        return {
            'statusCode': 200,
            'body': 'Unknown Command'
        }
