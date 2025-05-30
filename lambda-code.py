# This code is for lambda function which will trigger if any content uploaded to the s3 bucket. 
# It’ll send the notification to the users/owner with the Bucket name and the content name which was uploaded to the s3 bucket.


import json
import boto3

sns_client = boto3.client("sns")
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:your-account-id:S3UploadNotifications"

def lambda_handler(event, context):
    # Extract bucket name and object key
    for record in event["Records"]:
        bucket_name = record["s3"]["bucket"]["name"]
        object_key = record["s3"]["object"]["key"]

        # Construct the message
        message = f"New content uploaded to S3:\nBucket: {bucket_name}\nFile: {object_key}"

        # Publish to SNS
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject="S3 Upload Notification"
        )

    return {
        "statusCode": 200,
        "body": json.dumps("Notification Sent Successfully")
    }

