from io import BytesIO
import pandas as pd
import boto3
import io
import site
from importlib import reload
import sys

reload(site)
arg = sys.argv[2]
print(sys.argv)

input_loc = sys.argv[1]

output_loc = sys.argv[2]

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

lst = ['customer']

for i in lst:
        s3_resource.Object(output_loc_bucket, output_loc_prefix + i + '.parquet').put(Body=parquet_buffer.getvalue())


