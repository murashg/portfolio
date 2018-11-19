# Greg Murashige
# Extract files from portfoliobuild.shigtech.com
# and move them to portfolio.shigtech.com
# files in build are encrypted and zipped so we
# need to decrypt and unzip, then onces uploaded
# to bucket we set the type to be the same using
# mimetype and give them public-read access
# afterwards create an sns topic to confirm deployment
# the bucket will be the bucket that from the codepipeline job
# defaults to portfoliobuild.shigtech.com
# then tells codepipeline that function is done after upload

import json
import io
import boto3
from botocore.client import Config
import zipfile
import mimetypes

def lambda_handler(event, context):

    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:499263111735:deployPortfolioTopic')

    location = {
        "bucketName": 'portfoliobuild.shigtech.com',
        "objectKey": 'portfoliobuild.zip'
    }

    try:
        job = event.get("CodePipeline.job")

        if job:
            for artifact in job["data"]["inputArtifacts"]:
                if artifact["name"] == "MyAppBuild":
                    location = artifact["location"]["s3Location"]

        print("Building portfolio from " + str(location))

        s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

        portfolio_bucket = s3.Bucket('portfolio.shigtech.com')
        build_bucket = s3.Bucket(location["bucketName"])

        portfolio_zip = io.BytesIO()
        build_bucket.download_fileobj(location["objectKey"], portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)
                portfolio_bucket.upload_fileobj(obj, nm,
                    ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
             #  portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
        print("Job done")

        topic.publish(Subject="Portfolio Deployed", Message="Portfolio Deployed Successfully")

        if job:
            codepipeline = boto3.client('codepipeline')
            codepipeline.put_job_success_result(jobId=job["id"])

    except:
        topic.publish(Subject="Portfolio Deploy Failed", Message="The Portfolio Was Not Deployed")
        raise

    return {
        'statusCode': 200,
        'body': json.dumps('Success Deploying!')
    }
