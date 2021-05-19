import boto3
import pandas as pd
client = boto3.client('s3')
path ='s3://pytest-json-and-csv-data/input/Customers.csv'
df = pd.read_csv(path)
print(df)

import awswrangler as wr
# raw_s3_bucket = "pytest-json-and-csv-data"
# raw_path_dir = "output/Customer order master.parquet"
# raw_path = f"s3://{raw_s3_bucket}/{raw_path_dir}"
raw_df = wr.s3.read_parquet(path="s3://pytest-json-and-csv-data/output/customer address.parquet")
print(raw_df)


