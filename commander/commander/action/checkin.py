from ..s3 import GetFile, UploadFromContent


def CheckIn(body):
    local_ip = body['local_ip']
    public_ip = body['public_ip']
    moniker = body['moniker']
    node_type = body['type']

    if node_type == 'sentry':
        # TODO: Get file (if file doesn't exist, it's ok). Then json.loads it
        # Payload should be:
        '''
        {
            "sentrys": [
                "10.0.0.0:93939",
                "10.0.0.0:93939"
            ]
        }
        '''
        # Write a nodes/sentrys/10-0-0-0.json
        # write a new nodes/sentrys.latest
        current_file = GetFile('nodes/sentrys.latest')
        sentr
    elif node_type == 'validator':


    return
