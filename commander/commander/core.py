from .action.configfile import ConfigFile
from .action.healthcheck import HealthCheck
from .action.list import List
from .action.report import Report
from .auth import CheckAuth


def Switch(action, headers, body, context):

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

    """Execute Actions""""

    if action == 'config_file':
        result = ConfigFile(body)
        return result
    elif action == 'healthcheck':
        result = HealthCheck(body, context)
        return result
    elif action == 'list':
        result = List(body)
        return result
    elif action == 'report':
        result = Report(body)
        return result
    else:
        return {
            'statusCode': 404,
            'body': 'Unknown Command'
        }
