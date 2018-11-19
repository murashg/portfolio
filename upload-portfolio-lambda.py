# Greg Murashige
# Extract files from portfoliobuild.shigtech.com
# and move them to portfolio.shigtech.com
# files in build are encrypted and zipped so we
# need to decrypt and unzip, then onces uploaded
# to bucket we set the type to be the same using
# mimetype and give them public-read access

import json
import io
import boto3
from botocore.client import Config
import zipfile
import mimetypes

def lambda_handler(event, context):

    s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

    portfolio_bucket = s3.Bucket('portfolio.shigtech.com')
    build_bucket = s3.Bucket('portfoliobuild.shigtech.com')

    portfolio_zip = io.BytesIO()
    build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)

    with zipfile.ZipFile(portfolio_zip) as myzip:
        for nm in myzip.namelist():
            obj = myzip.open(nm)
            portfolio_bucket.upload_fileobj(obj, nm,
                ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
         #  portfolio_bucket.Object(nm).Acl().put(ACL='public-read')

    return {
        'statusCode': 200,
        'body': json.dumps('Success Deploying!')
    }
