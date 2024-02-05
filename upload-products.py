import pandas as pd
import boto3
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from io import StringIO
from datetime import datetime

load_dotenv()


def create_csv_file(db_url, sql_query):
  # Create a database engine
  engine = create_engine(db_url)

  # Execute the query and store the result in a pandas dataframe
  df = pd.read_sql_query(sql_query, engine)

  # Convert the dataframe to CSV
  csv_buffer = StringIO()
  df.to_csv(csv_buffer, index=False)
  return csv_buffer;

def upload_buffer_to_s3(csv_buffer, config):
# Upload the CSV to S3
  s3_resource = boto3.resource(
      's3',
      aws_access_key_id=config.get('aws_access_key_id'),
      aws_secret_access_key=config.get('aws_secret_access_key'),
      region_name=config.get('region_name'),
      endpoint_url=config.get('endpoint_url')
  )
  s3_resource.Object(config.get('bucket_name'), config.get('s3_file_path')).put(Body=csv_buffer.getvalue())

  print(f'File successfully uploaded to')

def main():
  # Database connection parameters
  DATABASE_TYPE = os.getenv('DATABASE_TYPE')
  DBAPI = os.getenv('DBAPI')
  ENDPOINT = os.getenv('ENDPOINT')
  DBUSER = os.getenv('DBUSER')
  DBPASSWORD = os.getenv('DBPASSWORD')
  PORT = os.getenv('PORT')
  DATABASE = os.getenv('DATABASE')
  db_url = f'{DATABASE_TYPE}+{DBAPI}://{DBUSER}:{DBPASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}'

  # SQL Query
  sql_query = f""" """

  # AWS Parameters

  current_time = datetime.now()
  formatted_time = current_time.strftime('%Y%m%d_%H%M%S')

  config = {
    "aws_access_key_id": os.getenv('AWS_ACCESS_KEY_ID'),
    "aws_secret_access_key": os.getenv('AWS_SECRET_ACCESS_KEY'),
    "bucket_name": os.getenv('S3_BUCKET_NAME'),
    "region_name": os.getenv('AWS_REGION'),
    "endpoint_url": os.getenv('AWS_ENDPOINT_URL'),
    "s3_file_path": f"{os.getenv('ARMI_STORE_ID')}/{formatted_time}.csv"
  }

  csv_buffer = create_csv_file(db_url, sql_query)
  upload_buffer_to_s3(csv_buffer, config)

main()
