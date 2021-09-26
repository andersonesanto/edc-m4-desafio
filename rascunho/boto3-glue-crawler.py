import boto3
import os

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
glue = boto3.client(
    'glue',
    region_name='us-east-2',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)


try:
    glue.get_crawler(Name='crawler_m4_enade')
except glue.exceptions.EntityNotFoundException:
    glue.create_crawler(
        Name='crawler_m4_enade',
        Role='arn:aws:iam::597495568095:role/santo-glue-service-role',
        DatabaseName='enade2017',
        Description='Crawler enade 2017 ',
        Targets={
            'S3Targets': [
                {
                    'Path': 's3://m4-597495568095/processing-zone/enade/',
                    'Exclusions': []
                },
            ]
        }
    )

#glue.start_crawler(
#    Name='crawler_m4_enade'
#)
