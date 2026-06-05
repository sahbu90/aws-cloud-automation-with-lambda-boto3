import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client('s3')

BUCKET_NAME = 'assignment-s3-cleanup-shahban-2026'

def lambda_handler(event, context):

    threshold = datetime.now(timezone.utc) - timedelta(minutes=5)

    response = s3.list_objects_v2(
        Bucket="assignment-s3-cleanup-shahban-2026"
    )

    if 'Contents' not in response:
        print("Bucket is empty")
        return

    for obj in response['Contents']:

        if obj['LastModified'] < threshold:

            s3.delete_object(
                Bucket="assignment-s3-cleanup-shahban-2026",
                Key=obj['Key']
            )

            print(
                f"Deleted: {obj['Key']}"
            )

    return {
        'statusCode': 200
    }