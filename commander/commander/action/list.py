from ..s3 import GetFile

def List(body):

    if body['type'] == 'sentrys':
        key = 'list/sentrys.latest'
    else if body['type'] == 'validators':
        key = 'list/validators.latest'

    list_file = GetFile(
        Key=key
    )
    return list_file['body']
