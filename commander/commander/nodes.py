from .s3 import GetFile


def GetSentryIps():
    hosts = GetFile('nodes/sentrys.latest')
    return hosts['body']


def GetValidatorIps():
    hosts = GetFile('nodes/sentrys.latest')
    return hosts['body']
