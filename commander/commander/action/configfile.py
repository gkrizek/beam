from ..s3 import GetFile


def ConfigFile(body):

    config_file = GetFile(
        Key='config/gaiad.latest'
    )
    return config_file