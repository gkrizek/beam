import boto3
import os

s3 = boto3.client('s3')


def GetFile(Key):
   try:
        s3_bucket = os.environ['COMMANDER_S3_BUCKET']
    except KeyError as e:
        message = ('Error finding the `COMMANDER_S3_BUCKET` environment variable.\n'
                   'Please make sure it is present.')
        print(message)
        return {
            'statusCode': 500,
            'body': message
        }

    s3_file = s3.GetFile(
        Bucket=s3_bucket,
        Key=Key
    )
    return {
        'statusCode': 200,
        'body': s3_file
    }


def UploadFromContent(Bucket, Key, Content):
    result = s3.put_object(
        Bucket=Bucket,
        Key=Key,
        Body=Content
    )
    return result
