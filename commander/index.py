from .commander.core import Switch


def handler(event, context):
    if event:
        print("Event Data:\n%s" % (str(event)))

        """Execute Main Routing Switch"""

        # Handle API Gateway requests
        if 'requestContext' in event:
            action = event['path']
            headers = event['headers']
            body = event['body']
        else:
            action = event['action']
            headers = None
            body = event['body']

        result = Switch(action, headers, body, context)
        return result
    else:
        return {
            'statusCode': 400,
            'body': 'missing event data'
        }
