import boto3

s3 = boto3.client('s3')

s3.upload_file(
    'trades.csv',
    'trade-financial',
    'raw/trades.csv'
)

print("Uploaded to S3")
