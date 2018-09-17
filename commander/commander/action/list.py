from ..s3 import GetFile

def List(body):

    # TODO: Maybe support different types here. 
    # Like `list/sentry.latest`, `list/validator.latest`. 
    # Or we can make `node.latest` a toml file and have sections
    list_file = GetFile(
        Key='list/node.latest'
    )
    return list_file
