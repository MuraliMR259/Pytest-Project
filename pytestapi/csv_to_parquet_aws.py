from io import BytesIO
import pandas as pd
import boto3
import os
import io
import site
from importlib import reload
import sys
from setuptools.command import easy_install
reload(site)
import pyarrow

input_loc ="pytest-json-and-csv-data/input/Customers.csv" and "pytest-json-and-csv-data/input/Customer Address.csv" and "pytest-json-and-csv-data/input/customer order details.csv" and "pytest-json-and-csv-data/input/customer order master.csv" and "pytest-json-and-csv-data/input/payment details.csv"
output_loc = "pytest-json-and-csv-data/output/"

input_bucket = input_loc.split('/', 1)[0]
object_key = input_loc.split('/', 1)[1]

output_loc_bucket = output_loc.split('/', 1)[0]
output_loc_prefix = output_loc.split('/', 1)[1]

s3 = boto3.client('s3')
obj = s3.get_object(Bucket=input_bucket, Key=object_key)
df = pd.read_csv(io.BytesIO(obj['Body'].read()))

parquet_buffer = BytesIO()
s3_resource = boto3.resource('s3')
df.to_parquet(parquet_buffer, index=False)

#s3_resource.Object(output_loc_bucket, output_loc_prefix + 'order master' + '.parquet').put(Body=parquet_buffer.getvalue())

lst = ['customer','customer address','customer order details','customer order master','payment details']

for i in lst:
    s3_resource.Object(output_loc_bucket, output_loc_prefix + i + '.parquet').put(Body=parquet_buffer.getvalue())
