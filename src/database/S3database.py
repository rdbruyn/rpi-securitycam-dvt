from database.Database import Database
import boto3


class S3database(Database):
    def __init__(self):
        self.s3_client = boto3.client('s3')

    def connect(self):
        self.s3_client = boto3.client('s3')

    def save_footage(self, footage_stream, filename: str):
        self.s3_client.upload_fileobj(
            footage_stream,
            'rdbruyn-test-bucket',
            filename,
            ExtraArgs={
                'ContentType': 'video/mp4'
            }
        )

    def close(self):
        # session expires by itself
        pass
